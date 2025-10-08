from app.user_service import get_user_profile, is_admin

def test_is_admin():
    assert is_admin("ADMIN") is True
