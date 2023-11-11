from src.label_trans import keyword_search
import pytest

def test_label_trans():
    seacher = keyword_search()
    assert seacher.search('容器') == '/m/011q46kg'
    assert seacher.search('container') == '/m/011q46kg'
    assert seacher.search('女人') == '/m/03bt1vf'
    assert seacher.search('woman') == '/m/03bt1vf'

    with pytest.raises(KeyError) as excinfo:
        seacher.search('python')
    assert str(excinfo.value) == "'Keyword does not exist.'"

    with pytest.raises(KeyError) as excinfo:
        seacher.search('拍森')
    assert str(excinfo.value) == "'關鍵字不存在!'"  

    with pytest.raises(KeyError) as excinfo:
        seacher.search('パイソン')
    assert str(excinfo.value) == "'輸入格式錯誤'"  
    