# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:09:48 2021

@author: MYM
"""

import os


method = "h265"
if method == "h264":
    #对excel视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i excel_01.yuv -pix_fmt yuv420p excel420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i excel420.yuv -vcodec libx264 -f h264 excelh264.h264 -y")
    os.system("ffmpeg -i excelh264.h264 -r 25 -pix_fmt yuv420p -vcodec h264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 excel_enc.h264 -y")
    os.system("ffmpeg -i excel_enc.h264 -c:v rawvideo -pix_fmt yuv444p excel_dec.yuv -y")
     #对ppt视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i ppt_02.yuv -pix_fmt yuv420p ppt420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i ppt420.yuv -vcodec libx264 -f h264 ppth264.h264 -y")
    os.system("ffmpeg -i ppth264.h264 -r 25 -pix_fmt yuv420p -vcodec h264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 ppt_enc.h264 -y")
    os.system("ffmpeg -i ppt_enc.h264 -c:v rawvideo -pix_fmt yuv444p ppt_dec.yuv -y")
     #对web视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i web_03.yuv -pix_fmt yuv420p web420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i web420.yuv -vcodec libx264 -f h264 webh264.h264 -y")
    os.system("ffmpeg -i webh264.h264 -r 25 -pix_fmt yuv420p -vcodec h264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 web_enc.h264 -y")
    os.system("ffmpeg -i web_enc.h264 -c:v rawvideo -pix_fmt yuv444p web_dec.yuv -y")
     #对word视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i word_04.yuv -pix_fmt yuv420p word420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i word420.yuv -vcodec libx264 -f h264 wordh264.h264 -y")
    os.system("ffmpeg -i wordh264.h264 -r 25 -pix_fmt yuv420p -vcodec h264 -preset veryslow -profile:v baseline  -crf 23 -acodec aac -b:a 32k -strict -5 word_enc.h264 -y")
    os.system("ffmpeg -i word_enc.h264 -c:v rawvideo -pix_fmt yuv444p word_dec.yuv -y")
else:
    #对excel视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i excel_01.yuv -pix_fmt yuv420p excel420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i excel420.yuv -vcodec libx265 excel265.265 -y")
    os.system("ffmpeg -i excel265.265 -r 25 -pix_fmt yuv420p  -vcodec libx265 -preset  veryslow -b:v 32k -profile main -crf  32 -strict -2 excel_enc.265 -y")
    os.system("ffmpeg -i excel_enc.265 -c:v rawvideo -pix_fmt yuv444p excel_dec.yuv -y")
    #对ppt视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i ppt_02.yuv -pix_fmt yuv420p ppt420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i ppt420.yuv -vcodec libx265 ppt265.265 -y")
    os.system("ffmpeg -i ppt265.265 -r 25 -pix_fmt yuv420p  -vcodec libx265 -preset  veryslow  -b:v 32k -profile main -crf  32 -strict -2 ppt_enc.265 -y")
    os.system("ffmpeg -i ppt_enc.265 -c:v rawvideo -pix_fmt yuv444p ppt_dec.yuv -y")
     #对web视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i web_03.yuv -pix_fmt yuv420p web420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i web420.yuv -vcodec libx265 web265.265 -y")
    os.system("ffmpeg -i web265.265 -r 25 -pix_fmt yuv420p  -vcodec libx265 -preset  veryslow  -b:v 32k -profile main -crf  32 -strict -2 web_enc.265 -y")
    os.system("ffmpeg -i web_enc.265 -c:v rawvideo -pix_fmt yuv444p web_dec.yuv -y")
     #对word视频编解码
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv444p -i word_04.yuv -pix_fmt yuv420p word420.yuv -y")
    os.system("ffmpeg -s 1280*720 -pix_fmt yuv420p -i word420.yuv -vcodec libx265 word265.265 -y")
    os.system("ffmpeg -i word265.265 -r 25 -pix_fmt yuv420p  -vcodec libx265 -preset veryslow  -b:v 32k -profile main -crf  32 -strict -2 word_enc.265 -y")
    os.system("ffmpeg -i word_enc.265 -c:v rawvideo -pix_fmt yuv444p word_dec.yuv -y")