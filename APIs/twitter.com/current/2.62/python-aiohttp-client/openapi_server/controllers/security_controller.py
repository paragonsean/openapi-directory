from typing import List


def info_from_BearerToken(token: str) -> dict:
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    Should return None if auth is invalid or does not allow access to called API.
    """
    return {'uid': 'user_id'}


def info_from_OAuth2UserToken(token: str) -> dict:
    """
    Validate and decode token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    'scope' or 'scopes' will be passed to scope validation function.
    Should return None if token is invalid or does not allow access to called API.
    """
    return {'scopes': ['read:pets', 'write:pets'], 'uid': 'user_id'}


def validate_scope_OAuth2UserToken(required_scopes: List[str], token_scopes: List[str]) -> bool:
    """ Validate required scopes are included in token scope """
    return set(required_scopes).issubset(set(token_scopes))

