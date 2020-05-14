# User documentation
This project contains web-application to demonstrate work of 2 neural networks models.

## Requirements

* Python 3
* pip 3
* django
* cotk
* TensorBoardX >= 1.4
* Tensorflow == 1.13.1
* Django == 3.0.6

## Other data and projects

For generating text, you need to download models. There are two SeqGAN models: based on big data-set and small data-set.

* **big_data_model** (is a folder with model checkpoints) - https://drive.google.com/open?id=15CjKztCk5r042Y8S3OWR2uOhxbIomAdh
* **small_data_model** (is a folder with model checkpoints) - 

This models need to be placed in a folder: `seqGAN-tensorflow-master/model/`

Example: `seqGAN-tensorflow-master/model/big_data_model`

## Changes
Initially, the project is configured to work with a model based on a large data-set. If you want to change data-set on small, you will need to change this:

1. Download and move `small_data_model` into the folder `seqGAN-tensorflow-master/model/`
2. Change settings in `seqGAN-tensorflow-master/run.py`: 
  * line 33 [https://github.com/pwnsauce8/kiv-bpini-web/blob/808a3ee2cb362de560cdd281fec55f09827b81af/seqGAN-tensorflow-master/run.py#L33] change `"../seqGAN-tensorflow-master/model/big_data_model"` on `"../seqGAN-tensorflow-master/model/small_data_model"`
3. Change input data-set in `seqGAN-tensorflow-master/data/`

## Structure
The work folder must be:

```
work_folder
|_ seqGAN-tensorflow-master
|_ bachelor_web
```

### Start
Change into the outer bachelor_web directory and run the following command to start server:

```
python3 manage . py runserver
```

You will see the following output on the command line:

```
System check identified no issues (0 silenced ) .
May 06 , 2020 - 17:28:30
Django version 3.0.4 , using settings ’ bachelor_web . settings ’
Starting development server at http ://127.0.0.1:8000/
Quit the server with CONTROL - C .
```

Now the server is running on localhost address. After visiting http://127.0.0.1:8000/
with browser, you will see a web-application.




