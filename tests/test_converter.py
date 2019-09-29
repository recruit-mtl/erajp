# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from unittest import TestCase

from nose.tools import eq_, raises

from erajp.converter import strjpftime, NotExpectedTimeException


class TestConverter(TestCase):
    @raises(NotExpectedTimeException)
    def test_not_Expected_time(self):
        exception_time = datetime.datetime(1868, 9, 7)
        strjpftime(exception_time)

    def test_expected_time(self):
        last_meiji_time = datetime.datetime(1912, 7, 29)
        eq_(strjpftime(last_meiji_time), "M45.07.29")
        eq_(strjpftime(last_meiji_time, "%O%E年"), "明治45年")

        first_taisho_time = datetime.datetime(1912, 7, 30)
        eq_(strjpftime(first_taisho_time), "T1.07.30")
        eq_(strjpftime(first_taisho_time, "%O%E年"), "大正元年")

        last_taisho_time = datetime.datetime(1926, 12, 24)
        eq_(strjpftime(last_taisho_time), "T15.12.24")
        eq_(strjpftime(last_taisho_time, "%O%E年"), "大正15年")

        first_showa_time = datetime.datetime(1926, 12, 25)
        eq_(strjpftime(first_showa_time), "S1.12.25")
        eq_(strjpftime(first_showa_time, "%O%E年"), "昭和元年")

        last_showa_time = datetime.datetime(1989, 1, 7)
        eq_(strjpftime(last_showa_time), "S64.01.07")
        eq_(strjpftime(last_showa_time, "%O%E年"), "昭和64年")


        first_heisei_time = datetime.datetime(1989, 1, 8)
        eq_(strjpftime(first_heisei_time), "H1.01.08")
        eq_(strjpftime(first_heisei_time, "%O%E年"), "平成元年")

        heisei_time = datetime.datetime(2015, 8, 5)
        eq_(strjpftime(heisei_time), "H27.08.05")
        eq_(strjpftime(heisei_time, "%O%E年"), "平成27年")
