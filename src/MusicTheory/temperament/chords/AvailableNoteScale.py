#https://ja.wikipedia.org/wiki/%E3%83%86%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%B3_(%E9%9F%B3%E6%A5%BD)
#https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%B4%E3%82%A7%E3%82%A4%E3%83%A9%E3%83%96%E3%83%AB%E3%83%BB%E3%83%8E%E3%83%BC%E3%83%88%E3%83%BB%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%AB
#テンション・ノート
#12平均律で複雑で不安定な響きを得たいときに使う。純正律で綺麗な和音を得たいときには絶対に使わない。
#アヴェイラブル・ノート・スケール
#コード上でメロディーに使うことが可能な音を音階として表したものが、アヴェイラブル・ノート・スケールである。
#長調（major）・短調（minor）上で用いられる。
class AvailableNoteScale:
    def GetTones(self, scale, scaleKeyId): 
        return ('ChordTones': (), 'AvoidTones': (), 'TensionTones': ())
    #ScaleKey=0(C)の場合
    def GetTonesMajor(self, scaleKeyId):
        if 0 == scaleKeyId: return ('ChordTones': (0, 4, 7, 11), 'AvoidTones': (5+12), 'TensionTones': (2+12, 9+12))
        if 2 == scaleKeyId: return ('ChordTones': (2, 5, 9, 0+12), 'AvoidTones': (11+12), 'TensionTones': (4+12, 7+12))
        if 4 == scaleKeyId: return ('ChordTones': (4, 7, 11, 2+12), 'AvoidTones': (5+12, 12+12), 'TensionTones': (9+12))
        if 5 == scaleKeyId: return ('ChordTones': (5, 9, 0+12, 4+12), 'AvoidTones': (), 'TensionTones': (7+12, 11+12, 2+12))
        if 7 == scaleKeyId: return ('ChordTones': (7, 11, 2+12, 5+12), 'AvoidTones': (0+12), 'TensionTones': (9+12, 4+12))
        if 9 == scaleKeyId: return ('ChordTones': (9, 0+12, 4+12, 7+12), 'AvoidTones': (5+12), 'TensionTones': (11+12, 2+12))
        if 11 == scaleKeyId: return ('ChordTones': (11, 2+12, 5+12, 9+12), 'AvoidTones': (0+12), 'TensionTones': (4+12, 7+12))
        else: return ('ChordTones': (), 'AvoidTones': (), 'TensionTones': ())
    """
    def GetTonesMinor(self, scaleKeyId): 
        if 0 == scaleKeyId: return ('ChordTones': (0, 4, 7, 11), 'AvoidTones': (5+12), 'TensionTones': (2+12, 9+12))
        if 2 == scaleKeyId: return ('ChordTones': (2, 5, 9, 0+12), 'AvoidTones': (11+12), 'TensionTones': (4+12, 7+12))
        if 3 == scaleKeyId: return ('ChordTones': (4, 7, 11, 2+12), 'AvoidTones': (2+12, 9+12), 'TensionTones': (9+12))
        if 5 == scaleKeyId: return ('ChordTones': (5, 9, 0+12, 4+12), 'AvoidTones': (), 'TensionTones': (7+12, 11+12, 2+12))
        if 7 == scaleKeyId: return ('ChordTones': (7, 11, 2+12, 5+12), 'AvoidTones': (0+12), 'TensionTones': (9+12, 4+12))
        if 8 == scaleKeyId: return ('ChordTones': (9, 0+12, 4+12, 7+12), 'AvoidTones': (5+12), 'TensionTones': (11+12, 2+12))
        if 10 == scaleKeyId: return ('ChordTones': (11, 2+12, 5+12, 9+12), 'AvoidTones': (0+12), 'TensionTones': (4+12, 7+12))
        else: return ('ChordTones': (), 'AvoidTones': (), 'TensionTones': ())
    """
    #二和音
    #エレキギター
    Power = (0, 7)#('P1', 'P5')
    
    #三和音(トライアド) https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
    Major = (0, 4, 7)#('P1', 'M3', 'P5') 長三和音(トライアド) "CM", "C△"
    Minor = (0, 3, 7)#('P1', 'm3', 'P5') 短三和音(トライアド) "Cm"
    Augmented = (0, 4, 7+1)#('P1', 'm3', 'a5') 増三和音(トライアド) "Caug", "C(#5)", "C+"
    Diminished = (0, 3, 7-1)#('P1', 'm3', 'd5') 減三和音(トライアド) Cdim、Co、Co△、Cm-5、Cm(♭5)、C--5、C-(♭5)、C dim (triad)、Cdim△
    Sus4 = (0, 5, 7)#('P1', 'P4', 'P5') サスフォー
    
    #四和音（テトラッド） https://ja.wikipedia.org/wiki/%E5%9B%9B%E5%92%8C%E9%9F%B3
    Seventh = (0, 4, 7, 10)#('P1', 'M3', 'P5', 'm7') 属七の和音 C7 
    MinorSeventh = (0, 3, 7, 10)#('P1', 'm3', 'P5', 'm7') 短七の和音 C7 
    MajorSeventh = (0, 4, 7, 11)#('P1', 'm3', 'P5', 'M7') 長七の和音
    AugmentedSeventh = (0, 3, 7, 9)#('P1', 'm3', 'P5', 'd7') 減七の和音
    HalfDiminishedSeventh = (0, 3, 7-1, 10)#('P1', 'm3', 'd5', 'm7') 減五短七の和音 Cm7-5、Cm7(♭5)、Csemidim、Cmi7(♭5)、CØ、C-7-5、C-7(♭5)
    MinorMajorSeventh = (0, 3, 7-1, 11)#('P1', 'm3', 'P5', 'M7') 短三長七の和音
    
    MajorSix = (0, 4, 7, 9)
    MinorSix = (0, 3, 7, 9)
    
    #五和音（テンション・コード） https://www.aki-f.com/kouza/riron/riron_6.htm
    

if __name__ == '__main__':
    print('========== 一般スケール ==========')
    print('----- 2和音 -----')
    print(ChordIntervals.Power)
    print('----- 3和音 -----')
    print(ChordIntervals.Major)
    print(ChordIntervals.Minor)
    print(ChordIntervals.Augmented)
    print(ChordIntervals.Diminished)
    print('----- 4和音 -----')
    print(ChordIntervals.Seventh)
    print(ChordIntervals.MinorSeventh)
    print(ChordIntervals.MajorSeventh)
    print(ChordIntervals.AugmentedSeventh)
    print(ChordIntervals.HalfDiminishedSeventh)
    print(ChordIntervals.MinorMajorSeventh)
    print(ChordIntervals.MajorSix)
    print(ChordIntervals.MinorSix)

