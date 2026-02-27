from ingestion.load import load_rows

def test_load_rows():
    assert load_rows([(1,"a"),(2,"b")]) == 2
