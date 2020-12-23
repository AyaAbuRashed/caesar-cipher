from caesar_cipher.caesar_cipher import decrypt,encrypt,hack

def test_encrypt():
    actual = encrypt("my name is aya",5)
    expected = "rd sfrj nx fdf"
    assert actual == expected

def test_decrypt():
    actual = decrypt("rd sfrj nx fdf",5)
    expected = "my name is aya"
    assert actual == expected

def test_hack():
    actual = hack("rd sfrj nx fdf")
    expected = "my name is aya","key : 5"
    assert actual == expected




