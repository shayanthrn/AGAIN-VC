import subprocess
import os

_cuda_command = 'nvidia-smi -q | grep "Minor\|Processes" | grep "None" -B1 | tr -d " " | cut -d ":" -f2 | grep -v "None" | tail -1'


def set_cuda_visible_devices(use_gpu=True, logger=None):
    try:
        if use_gpu:
            free_gpu = subprocess.check_output(_cuda_command, shell=True)
            if len(free_gpu) == 0:
                if logger is not None:
                    logger.info("No GPU seems to be available and I cannot continue without GPU.")
                raise Exception("No GPU seems to be available and I cannot continue without GPU.")
            else:
                os.environ["CUDA_VISIBLE_DEVICES"] = free_gpu.decode().strip()
            if logger is not None:
                logger.info("CUDA_VISIBLE_DEVICES " + os.environ["CUDA_VISIBLE_DEVICES"])
        else:
            os.environ["CUDA_VISIBLE_DEVICES"] = ''
    except subprocess.CalledProcessError:
        if logger is not None:
            logger.info("No GPU seems to be available and I cannot continue without GPU.")
        os.environ["CUDA_VISIBLE_DEVICES"] = ''
        if use_gpu:
            raise

