# -*- coding: utf-8 -*-
import datetime


ERA_JP = (
    (u"M", u"明治"),
    (u"T", u"大正"),
    (u"S", u"昭和"),
    (u"H", u"平成"),
)


class NotExceptedTimeException(Exception):
    pass


def strjpftime(time=datetime.datetime.today(), format=u"%o%E.%m.%d"):
    """
    Convert to Japanese era
    :param time:
    :param format: strftime format
        New available here
            - %o : alphabet era
            - %O : Chinese character era
            - %E : era year
    :return:
    """
    era_year, era, era_ch = None, None, None
    if time < datetime.datetime(1868, 9, 8):
        raise NotExceptedTimeException("time is expected later than 1868.09.08.")
    elif time < datetime.datetime(1912, 7, 30):
        era_year = time.year - 1867
        era, era_ch = ERA_JP[0]
    elif time < datetime.datetime(1926, 12, 25):
        era_year = time.year - 1911
        era, era_ch = ERA_JP[1]
    elif time < datetime.datetime(1989, 1, 8):
        era_year = time.year - 1925
        era, era_ch = ERA_JP[2]
    else:
        era_year = time.year - 1988
        era, era_ch = ERA_JP[3]
    if era_year == 1 and format.find(u"%O") > -1:
        era_year = u"元"
    else:
        era_year = str(era_year)

    format = format.replace(u"%o", era).replace(u"%O", era_ch).replace(u"%E", era_year)
    strttime = time.strftime(format.encode("utf-8")).decode("utf-8")
    return strttime
