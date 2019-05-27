# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from hash_dict import HashDict
from hash_dict.comparer import (
    AnyComparer, ObjectComparer
)

def test_any_comparer():
    s = HashDict(AnyComparer())
    s[None] = 15
    assert s[None] == 15

def test_obj_comparer():
    s = HashDict(ObjectComparer())
    s[0] = 15
    assert s[0] == 15
