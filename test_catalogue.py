import catalogue

def test_catalogue():
    catalogue.get_tree("goods.csv")
    assert catalogue.get_tree() == \
"""Toothbrush
  Manual
    Oral_B
      green
      red
    Adidas
      blue
  Automatic
    Samsung
      regular
      usb
    Meizu
      red"""