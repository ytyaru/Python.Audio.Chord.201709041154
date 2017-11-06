import csv
from collections import namedtuple

#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#各種音階における音程 29種類
class Chords:
    @classmethod
    def Get(cls, name=None):
        if None is name or '' == name: return [c for c in cls._chords if 'M' in c.names][0]
#        if None is name: return [c for c in cls._chords if 'M' in c.names][0]
        for c in cls._chords:
            if name in c.names: return c
        raise Exception(f'"{name}"は存在しない和音名です。存在する和音名を指定して下さい。')
    
    _chords = []
    @classmethod
    def Load(cls):
        cls._chords.clear()
        cls.__LoadChords()
        cls.__LoadChords2()
        
    @classmethod
    def __LoadChords(cls):
        with open('Chords.tsv', 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            header = next(reader)  # ヘッダーを読み飛ばす
            Chord = namedtuple('Chord', ('intervals','degreeNames','names','ja','en'))
            for row in reader:
                if 0 == len(row): continue
                #列数を超えた分は無視する
                if len(Chord._fields) < len(row): row = row[0:len(Chord._fields)-len(row)]
                #各列データをtupleにする
                for i, col in enumerate(row):
                    if 0 == i: row[i] = tuple([eval(v) for v in col.split(',')]) #`2-1+12`などの計算式を計算させる
                    else: row[i] = tuple(col.split(','))
                cls._chords.append(Chord._make(row))

    @classmethod
    def __LoadChords2(cls):
        chords = []
        with open('Chords2.tsv', 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            header = next(reader)  # ヘッダーを読み飛ばす
            Chord = namedtuple('Chord', ('names','degreeNames'))
            for row in reader:
                if 0 == len(row): continue
                #列数を超えた分は無視する
                if len(Chord._fields) < len(row): row = row[0:len(Chord._fields)-len(row)]
                #各列データをtupleにする
                for i, col in enumerate(row):
                    row[i] = tuple(col.split(','))
#                    if 1 == i: row[i] = tuple(col.split(','))
                print(row)
                chords.append(Chord._make(row))
        cls.print_markdown(chords)

    @classmethod
    def print_markdown(cls, chords=None):
        if None is chords: chords = Chords._chords
        html = []
        html.append(f'names|tones')
        html.append(f'-----|-----')
#        for c in chords: html.append(f'{c.names[0]}|{c.degreeNames}')
        for c in chords: html.append(f'{c.names[0]}|{", ".join(c.degreeNames)}')
        print('\n'.join(html))


if __name__ == '__main__':
    Chords.Load()

    print('----- Intervals(intervalsとdegreeNamesが一致しているか確認) -----')
    from IntervalName import IntervalName
    for c in Chords._chords:
#        print(c.names[0], c.degreeNames, c.intervals, end=': ')
#        print(f'{c.names[0]:6} {str(c.degreeNames):32} {c.intervals}: ', end='')
#        print(tuple(IntervalName.GetHalfNum(dn) for dn in c.degreeNames))
        print(f'{c.names[0]:6} {str(c.degreeNames):32} {c.intervals}')
        if not c.intervals == tuple(IntervalName.GetHalfNum(dn) for dn in c.degreeNames):
            print(f'不一致！ {c.names[0]} c.intervals={c.intervals}  TSV={tuple(IntervalName.GetHalfNum(dn) for dn in c.degreeNames)}')
        assert(c.intervals == tuple(IntervalName.GetHalfNum(dn) for dn in c.degreeNames))

    print('----- コードネーム確認 -----')
    print(len(Chords._chords))
    for c in Chords._chords:
        for name in c.names:
#            print(name, Chords.Get(name))
            print(f'{name:6} {Chords.Get(name)}')

    print('----- Get() -----')
    print('    ', Chords.Get(''))
    print(None, Chords.Get(None))
    print('m7  ', Chords.Get('m7'))
#    print('存在しない名前', Chords.Get('存在しない名前'))

    Chords.print_markdown()
    """
    html = []
    html.append(f'names|tones')
    html.append(f'-----|-----')
#    for c in Chords._chords: html.append(f'{c.names}|{c.degreeNames}')
    for c in Chords._chords: html.append(f'{c.names[0]}|{c.degreeNames}')
#    for c in Chords._chords: html.append(f'{str(c.names).replace('', '')}|{str(c.degreeNames)}')
    print('\n'.join(html))
    """
