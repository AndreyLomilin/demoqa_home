from pages.swag_labs import SwagLabs


def test(browser):
    demo_swag = SwagLabs(browser)
    demo_swag.visit()
    assert demo_swag.exist_icon()
    assert demo_swag.field_name()
    assert demo_swag.field_password()
