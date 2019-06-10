# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 00:52:02 2018

@author: Xiang Guo
"""

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

os.chdir('/home/fang/study/data_set/UnderWaterDetection_UPRC2018/train/box')
path = '/home/fang/study/data_set/UnderWaterDetection_UPRC2018/train/box'

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('frame').text ,
                     #int(member.find('size')[0].text),
                     #int(member.find('size')[1].text),
                     member[0].text,
                     int(member[1][0].text),
                     int(member[1][1].text),
                     int(member[1][2].text),
                     int(member[1][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename',  'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = path
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('1_test.csv', index=None)
    print('Successfully converted xml to csv.')


main()
