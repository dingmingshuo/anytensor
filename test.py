import anytensor

data = anytensor.realworld.video.eagle()
print(data.shape)
anytensor.core.video.play_by_frame(data)
