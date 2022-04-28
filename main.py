music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.play_tone(294, music.beat(BeatFraction.HALF))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(262, music.beat(BeatFraction.WHOLE))
music.play_tone(294, music.beat(BeatFraction.WHOLE))
music.play_tone(330, music.beat(BeatFraction.WHOLE))
music.play_tone(349, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.WHOLE))
music.play_tone(392, music.beat(BeatFraction.DOUBLE))

def on_forever():
    pass
basic.forever(on_forever)
