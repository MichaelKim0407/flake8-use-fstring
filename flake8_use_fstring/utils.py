import re as _re
import token as _token
from tokenize import TokenInfo as _TokenInfo

PREFIX_RE = _re.compile(r"^[^'\"]*")


def is_text_string_token(token: _TokenInfo) -> bool:
    if not token.type == _token.STRING:
        return False  # Not a string at all? Ignore.
    # Get the prefix of the string (anything before the first quote)
    prefix = PREFIX_RE.match(token.string).group(0).lower()
    if 'b' in prefix:
        return False  # Smells like a bytestring. Ignore it.
    return True
