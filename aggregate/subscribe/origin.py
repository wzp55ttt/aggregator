# -*- coding: utf-8 -*-

# @Author  : wzdnzd
# @Time    : 2022-07-15

import enum
from dataclasses import dataclass
import sys


@dataclass
class ExpireInfo(object):
    name: str
    expire: int


class Origin(enum.Enum):
    OWNED = ExpireInfo(name="OWNED", expire=sys.maxsize)
    TELEGRAM = ExpireInfo(name="TELEGRAM", expire=3)
    TWITTER = ExpireInfo(name="TWITTER", expire=3)
    TEMPORARY = ExpireInfo(name="TEMPORARY", expire=6)
    GOOGLE = ExpireInfo(name="GOOGLE", expire=10)
    GITHUB = ExpireInfo(name="GITHUB", expire=20)
    REPO = ExpireInfo(name="REPO", expire=60)
    REMAIND = ExpireInfo(name="REMAIND", expire=sys.maxsize)

    @staticmethod
    def get_expire(name: str) -> int:
        try:
            name = name.upper()
            source = Origin.__getitem__(name)
        except:
            source = Origin.OWNED

        return source.value.expire
