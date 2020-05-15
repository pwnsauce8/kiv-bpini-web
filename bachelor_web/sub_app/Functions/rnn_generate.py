from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

import numpy as np


class RNN_generator:
    """
    Original code: https://www.tensorflow.org/tutorials/text/text_generation
    """
    checkpoint_dir = './sub_app/Data/rnn_checkpoints'
    vocab_path = './sub_app/Data/vocab.txt'
    # The embedding dimension
    embedding_dim = 256
    # Number of RNN units
    rnn_units = 1024

    def __init__(self, first_world):
        self.first_world = first_world + " "

    @property
    def first_world(self):
        return self._first_world

    @first_world.setter
    def first_world(self, value):
        self._first_world = value

    @staticmethod
    def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                      batch_input_shape=[batch_size, None]),
            tf.keras.layers.GRU(rnn_units,
                                return_sequences=True,
                                stateful=True,
                                recurrent_initializer='glorot_uniform'),
            tf.keras.layers.Dense(vocab_size)
        ])
        return model

    @staticmethod
    def generate_text(model, start_string, char2idx, idx2char):
        print(">>> " + tf.__version__)
        # Evaluation step (generating text using the learned model)

        # Number of characters to generate
        num_generate = 1000

        # Converting our start string to numbers (vectorizing)
        input_eval = [char2idx[s] for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)

        # Empty string to store our results
        text_generated = []

        # Low temperatures results in more predictable text.
        # Higher temperatures results in more surprising text.
        # Experiment to find the best setting.
        temperature = 1.0

        # Here batch size == 1
        model.reset_states()
        for i in range(num_generate):
            predictions = model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            # using a categorical distribution to predict the character returned by the model
            predictions = predictions / temperature
            predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()

            # We pass the predicted character as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)

            text_generated.append(idx2char[predicted_id])
        return start_string + ''.join(text_generated)

    def run(self):
        # Read vocab
        with open(self.vocab_path) as file_in:
            vocab = []
            for line in file_in:
                vocab.append(line.rstrip("\n"))

        vocab[0] = '\t'
        vocab[1] = '\n'
        print('{} unique characters'.format(len(vocab)))

        char2idx = {u: i for i, u in enumerate(vocab)}
        idx2char = np.array(vocab)

        # Length of the vocabulary in chars
        vocab_size = len(vocab)

        # Build model
        tf.train.latest_checkpoint(self.checkpoint_dir)
        model = self.build_model(vocab_size, self.embedding_dim, self.rnn_units, batch_size=1)

        model.load_weights(tf.train.latest_checkpoint(self.checkpoint_dir))

        model.build(tf.TensorShape([1, None]))
        model.summary()

        # Generate text
        return self.generate_text(model, start_string=self.first_world, char2idx=char2idx, idx2char=idx2char)
