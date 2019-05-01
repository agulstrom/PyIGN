#from ignition.core
from functions import getData, funcEval, ptArray, ptIndex
#import core as cr



if __name__ == '__main__':
    data1 = getData('test_pres_data.txt')
    #print(data1)

    data2 = funcEval(data1)
    #print(data2)

    #data3 = ptArray(data1)
    #print(data3)

    #dataIndex = ptArray(data1)
    #print(dataIndex)

    #dataIndex = ptIndex(data1)
    #print(dataIndex)



    def test_getData_initial():
        assert data1[0] == 100
    test_getData_initial()

    def test_getData_mid():
        assert data1[2] == 230
    test_getData_mid()

    def test_getData_final():
        assert data1[4] == -400
    test_getData_final()

    def test_funcEval():
        assert funcEval(data1) == 900
    test_funcEval()

    def test_ptIndex():
        assert ptIndex(data1) == [0, 0, 0, 4, 0]
    test_funcEval()
