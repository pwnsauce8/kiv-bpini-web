import os

DIR = '../seqGAN-tensorflow-master/'


def run():
    """
    Run generating process from another project and get result from output file
    """
    try:
        os.system("./run_seqgan.sh")
        with open(DIR + 'output/seqGAN_test.txt', 'r') as myfile:
            data = myfile.read()
    except ModuleNotFoundError as ex:
        return str(ex)

    return data


