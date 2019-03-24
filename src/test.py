import data2midi as d

t =  d.data2midi('lc_test.csv', 'csv', 120)

t.scaleNumbersToNotes(t.listarr[0])
