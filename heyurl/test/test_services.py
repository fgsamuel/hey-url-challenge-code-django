from heyurl.services import create_short_url
import re


def test_short_url_pattern():
    short_url = create_short_url()
    result = re.match('^[a-zA-Z0-9]{1,5}$', short_url)
    assert result
