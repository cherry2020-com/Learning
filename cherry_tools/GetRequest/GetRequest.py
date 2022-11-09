#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tools.fiddler import RawToPython
import json

filename = "./tt.head"


def modify_file(filename, PageNumber):
    with open(filename, encoding='utf-8') as f_r:
        lines = f_r.readlines()
        firstline = lines[0]
        list_firstline = firstline.split('&')
        list_firstline[9] = 'pageIndex=' + PageNumber
        str_line = '&'
        firstline = str_line.join(list_firstline)
        lines[0] = firstline
    with open(filename, "w", encoding="utf-8") as f_w:
        f_w.writelines(lines)
        f_w.close()


def get_all_postName_URL(filename):
    rtp = RawToPython(filename)
    web = rtp.requests(timeout=10)
    all_data = web.json()
    # all_data = json.loads(web.content)
    if all_data['Data']['Count'] != 0:
        all_postURL = [i['PostURL'] for i in all_data['Data']['Posts']]
        all_RecruitPostName = [i['RecruitPostName'] for i in all_data['Data']['Posts']]
        return all_postURL, all_RecruitPostName
    else:
        return None, None


if __name__ == '__main__':
    PageNumber = 132
    while (PageNumber > 0):
        modify_file(filename, str(PageNumber))
        PostURL, RecruitPostName = get_all_postName_URL(filename)
        PageNumber = PageNumber + 1
        print(PostURL)
        print(RecruitPostName)
        if PostURL == None:
            print(PageNumber)
            break