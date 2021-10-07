# coding=utf-8

import logging
from random import randint
from typing import Final
import click

from . import Btree
from . import innerNode
from . import leafNode

LOG_FORMAT: Final = "%(asctime)s [%(name)s:%(levelname)s] %(message)s"


@click.command()
@click.option("--debug", is_flag=True, help="Output debug messages.")
def main(debug):
    # log設定
    logging.basicConfig(format=LOG_FORMAT)
    if debug:
        logging.getLogger().setLevel("DEBUG")
    logger = logging.getLogger(__name__)

    # 以下，メイン関数の処理
    # logger.debug("debug message")
    # logger.info("information message")
    # logger.warning("warning message")
    # logger.error("error message")
    # logger.critical("critical message")

    logger.setLevel("DEBUG")
    logger.debug("DEBUG START!!")
    Btree.logger.setLevel("DEBUG")
    innerNode.logger.setLevel("DEBUG")
    leafNode.logger.setLevel("DEBUG")

    bt = Btree.Btree()
    for i in range(1000):
        key = randint(0, 10000)
        value = randint(0, 10000)
        bt.upsert(key, value)

    bt.predecessor(-1)
    bt.successor(10001)


if __name__ == "__main__":
    main()
