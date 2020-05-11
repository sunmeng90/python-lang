import argparse
import os
import random
import time

from logger import logger

log = logger.get_logger(__name__)

# python -m tools.youget.download
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="video url")
    parser.add_argument("-o", "--output", help="output folder for downloading", default=".")
    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")  # flag, if specified True
    args = parser.parse_args()
    output = os.path.abspath(args.output)
    log.info(f"start downloading video on {args.url} to {output}")
    os.chdir(output)  # change working dir
    for n in range(144, 149):
        cmd = 'you-get --format=dash-flv480 https://www.bilibili.com/video/BV1w7411v74u?p=' + str(n)
        log.info("executing: " + cmd)
        time.sleep(random.randint(0, 3))  # mock human  behavior
        res = os.system(cmd)
        if res == 0:
            print(cmd + ' success')
