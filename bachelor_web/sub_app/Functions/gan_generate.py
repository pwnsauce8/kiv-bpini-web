import subprocess


DIR = '../seqGAN-tensorflow-master/'


def run():
    """
    Run generating process from another project and get result from output file
    """
    try:
        result = subprocess.run(['python3', DIR + 'run.py'], stdout=subprocess.PIPE)
        with open(DIR + 'output/seqGAN_test.txt', 'r') as myfile:
            data = myfile.read()
    except ModuleNotFoundError as ex:
        return str(ex)

    return data


