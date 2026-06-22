from moviepy.editor import *

# Background (black screen for cinematic feel)
background = ColorClip(size=(1280, 720), color=(0,0,0), duration=8)

# Title text
title = TextClip("Doteng Lower Secondary School",
                 fontsize=80,
                 color='white',
                 font='Arial-Bold',
                 stroke_color='blue',
                 stroke_width=3).set_position('center').set_duration(8)

# Subtitle text (school environment)
subtitle = TextClip("Learning in a Creative Environment",
                    fontsize=50,
                    color='yellow',
                    font='Arial-BoldItalic',
                    stroke_color='black',
                    stroke_width=2).set_position(('center', 400)).set_duration(8)

# Fade-in and fade-out transitions
title = title.fadein(2).fadeout(2)
subtitle = subtitle.fadein(3).fadeout(2)

# Composite video
final = CompositeVideoClip([background, title, subtitle])

# Export video file
final.write_videofile("school_intro.mp4", fps=24)
