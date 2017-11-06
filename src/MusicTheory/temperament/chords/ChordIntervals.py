#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#各種音階における音程 29種類
class ChordIntervals:
    #二和音 2
    #エレキギター
    Power = (0, 7)#('P1', 'P5')
    Octave = (0, 12)#('P1', 'P8')
    
    #三和音(トライアド) 4 https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
    Major = (0, 4, 7)#('P1', 'M3', 'P5') 長三和音(トライアド) "CM", "C△"
    Minor = (0, 3, 7)#('P1', 'm3', 'P5') 短三和音(トライアド) "Cm"
    Augmented = (0, 4, 7+1)#('P1', 'm3', 'a5') 増三和音(トライアド) "Caug", "C(#5)", "C+"
    Diminished = (0, 3, 7-1)#('P1', 'm3', 'd5') 減三和音(トライアド) Cdim、Co、Co△、Cm-5、Cm(♭5)、C--5、C-(♭5)、C dim (triad)、Cdim△
    
    #四和音（テトラッド）9 https://ja.wikipedia.org/wiki/%E5%9B%9B%E5%92%8C%E9%9F%B3
    ## 四和音-七の和音 7
    Seventh = (0, 4, 7, 10)#('P1', 'M3', 'P5', 'm7') 属七の和音 C7 
    MinorSeventh = (0, 3, 7, 10)#('P1', 'm3', 'P5', 'm7') 短七の和音 Cm7
    MajorSeventh = (0, 4, 7, 11)#('P1', 'm3', 'P5', 'M7') 長七の和音 CM7
    DiminishedSeventh = (0, 3, 7-1, 9)#('P1', 'm3', 'd5', 'd7')減七の和音 Cdim7
    AugmentedSeventh = (0, 4, 7+1, 11)#('P1', 'M3', 'a5', 'M7') 増七の和音 Caug M7 CM7+5 http://楽典.com/gakuten/7nowaon.html
    HalfDiminishedSeventh = (0, 3, 7-1, 10)#('P1', 'm3', 'd5', 'm7') 減五短七の和音 Cm7-5、Cm7(♭5)、Csemidim、Cmi7(♭5)、CØ、C-7-5、C-7(♭5)
    MinorMajorSeventh = (0, 3, 7, 11)#('P1', 'm3', 'P5', 'M7') 短三長七の和音 http://楽典.com/gakuten/chordname.html
    ## 四和音-六の和音 2
    MajorSix = (0, 4, 7, 9)#('P1', 'M3', 'P5', 'M6') C6
    MinorSix = (0, 3, 7, 9)#('P1', 'm3', 'P5', 'M6') Cm6

    #五和音 2（テンション・コード） https://www.aki-f.com/kouza/riron/riron_6.htm
    Ninth = Seventh + (2+12,) # C9, C7(9)
    MajorNinth = Seventh + (2-1+12,) # C7(♭9)
    
    #その他の和音 12
    SeventhAdd9 = Seventh + (2+12,) #C7(#9) または C7(♭10)
    Sus4 = (0, 5, 7)#('P1', 'P4', 'P5') サスフォー
    SeventhSus4 = (0, 5, 7, 10) #C7sus4
    Sus2 = (0, 2, 7) #Csus2
    SeventhSharp11 = Seventh + (5+1+12,)# C7(#11)
    MajorSeventhSharp11 = MajorSeventh + (5+1+12,)# CM7(#11)
    Seventh13 = (0, 4, 10, 9+12)# C7(13) Seventhから5thを省いて13thを追加
    SeventhFlat13 = (0, 4, 10, 9+12-1)# C7(♭13) Seventhから5thを省いて♭13thを追加
    Add9 = Major + (2+12,) # C(add9)
    Add4 = (0, 4, 5, 7) # C(add4)
    Dim5 = (0, 4, 7-1) # C-5, CM-5
    SeventhDim5 = (0, 4, 7-1, 10) # C7-5
    
    __names = []
    @classmethod
    def Get(cls, name=None):
        if None is name or '' == name: return {'Intervals':(0,4,7), 'DegreeNames':('P1','M3','P5'), 'Name':('M','△'), 'JA':('長三和音',), 'EN':('Major',)}
        
    """
    def Get(name=None, JA='長三和音', EN='Major', degreename=('P1','M3','P5'), intervals=(0,4,7)):
#        if None is name or '' == name: return 0,4,7    P1,M3,P5    M,△    長三和音    Major
#        if None is name or '' == name: return (0,4,7)    (P1,M3,P5)    (M,△)    (長三和音)    (Major)
        if None is name or '' == name: return {'Intervals':(0,4,7), 'DegreeNames':('P1','M3','P5'), 'Name':('M','△'), 'JA':('長三和音',), 'EN':('Major',)}        
    """
    
    @classmethod
    def Load(cls):
        import csv
        with open('Chords.tsv', 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            header = next(reader)  # ヘッダーを読み飛ばす
            for row in reader:
                print(row)

    
if __name__ == '__main__':
    print('========== 和声音 ==========')
    print('----- 2和音 -----')
    print(ChordIntervals.Power)
    print(ChordIntervals.Octave)
    print('----- 3和音 -----')
    print(ChordIntervals.Major)
    print(ChordIntervals.Minor)
    print(ChordIntervals.Augmented)
    print(ChordIntervals.Diminished)
    print('----- 4和音 -----')
    print(ChordIntervals.Seventh)
    print(ChordIntervals.MinorSeventh)
    print(ChordIntervals.MajorSeventh)
    print(ChordIntervals.DiminishedSeventh)
    print(ChordIntervals.AugmentedSeventh)
    print(ChordIntervals.HalfDiminishedSeventh)
    print(ChordIntervals.MinorMajorSeventh)
    print(ChordIntervals.MajorSix)
    print(ChordIntervals.MinorSix)
    print('----- 5和音 -----')
    print(ChordIntervals.Ninth)
    print(ChordIntervals.MajorNinth)
    print('----- その他の和音 -----')
    print(ChordIntervals.SeventhAdd9)
    print(ChordIntervals.Sus4)
    print(ChordIntervals.SeventhSus4)
    print(ChordIntervals.SeventhSharp11)
    print(ChordIntervals.MajorSeventhSharp11)
    print(ChordIntervals.Seventh13)
    print(ChordIntervals.SeventhFlat13)
    print(ChordIntervals.Add9)
    print(ChordIntervals.Add4)
    print(ChordIntervals.Dim5)
    print(ChordIntervals.SeventhDim5)
    print('========== 非和声音（未実装） ==========')

    print('========== 名前一覧 ==========')
    items = [a for a in dir(ChordIntervals) if not(a.startswith('__') and a.endswith('__'))]
    print(len(items), items)
