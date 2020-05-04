import testproject1234


def test_import():
    assert testproject1234.testmod.module_level_variable1 == 12345
