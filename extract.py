from moviepy.editor import *
import datetime
import json

clips_array = []
video = VideoFileClip("sample.mp4")


timestamps =[{'start_time': 1, 'end_time': 10},
             {'start_time': 15, 'end_time': 22},
             {'start_time': 20, 'end_time': 29},
             {'start_time': 40, 'end_time': 50}]



for i in timestamps:
    starttime = int(datetime.datetime.fromtimestamp(i["start_time"]).strftime('%S'))
    endtime = int(datetime.datetime.fromtimestamp(i["end_time"]).strftime('%S'))
    clip = video.subclip(starttime, endtime)
    clips_array.append(clip)
final_clip = concatenate_videoclips(clips_array)
final_clip.write_videofile("Out_File.mp4")