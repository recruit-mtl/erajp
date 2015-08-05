# -*- coding: utf-8 -*-
from unittest import TestCase
import datetime
from nose.tools import eq_, raises
from erajp.converter import strjpftime, NotExceptedTimeException


class TestConverter(TestCase):
    @raises(NotExceptedTimeException)
    def test_not_excepted_time(self):
        exception_time = datetime.datetime(1868, 9, 7)
        strjpftime(exception_time)

    def test_excepted_time(self):
        last_meiji_time = datetime.datetime(1912, 7, 29)
        eq_(strjpftime(last_meiji_time), u"M45.07.29")
        eq_(strjpftime(last_meiji_time, u"%O%E年"), u"明治45年")

        first_taisho_time = datetime.datetime(1912, 7, 30)
        eq_(strjpftime(first_taisho_time), u"T1.07.30")
        eq_(strjpftime(first_taisho_time, u"%O%E年"), u"大正元年")

        last_taisho_time = datetime.datetime(1926, 12, 24)
        eq_(strjpftime(last_taisho_time), u"T15.12.24")
        eq_(strjpftime(last_taisho_time, u"%O%E年"), u"大正15年")

        first_showa_time = datetime.datetime(1926, 12, 25)
        eq_(strjpftime(first_showa_time), u"S1.12.25")
        eq_(strjpftime(first_showa_time, u"%O%E年"), u"昭和元年")

        last_showa_time = datetime.datetime(1989, 1, 7)
        eq_(strjpftime(last_showa_time), u"S64.01.07")
        eq_(strjpftime(last_showa_time, u"%O%E年"), u"昭和64年")


        first_heisei_time = datetime.datetime(1989, 1, 8)
        eq_(strjpftime(first_heisei_time), u"H1.01.08")
        eq_(strjpftime(first_heisei_time, u"%O%E年"), u"平成元年")

        heisei_time = datetime.datetime(2015, 8, 5)
        eq_(strjpftime(heisei_time), u"H27.08.05")
        eq_(strjpftime(heisei_time, u"%O%E年"), u"平成27年")









