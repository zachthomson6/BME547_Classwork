import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("22.0 lb", 10),
    ("200 oz", None),
    ("22lb", None),
    ("22 Lb", 10),
    ("22 lb", 10),
    ("22 LB", 10),
    ("22 pound", 10),
    ("22 lbs", 10),
    ("22", None),
    ("-22 lbs", -10),
    ("", None)
    ("44 pounds", 20)
    ])
    
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected

@pytest.mark.parametrize("input, expected", [
    (22.0, 10),
    (44.0, 20)
    ])
def test_convert_lb_to_kg(input, expected):
