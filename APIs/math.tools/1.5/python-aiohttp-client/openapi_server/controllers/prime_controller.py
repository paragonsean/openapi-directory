from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_prime_factors_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_factors_get

    Get the prime factors of a given number.

    :param number: Number to get the factors
    :type number: int

    """
    return web.Response(status=200)


async def numbers_prime_is_fermat_prime_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_is_fermat_prime_get

    Checks whether a given number is a known fermat prime number or not.

    :param number: Number to check
    :type number: int

    """
    return web.Response(status=200)


async def numbers_prime_is_fibonacci_prime_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_is_fibonacci_prime_get

    Checks whether a given number is a known fibonacci prime number or not.

    :param number: Number to check
    :type number: int

    """
    return web.Response(status=200)


async def numbers_prime_is_mersenne_prime_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_is_mersenne_prime_get

    Checks whether a given number is a known mersenne prime number or not.

    :param number: Number to check
    :type number: int

    """
    return web.Response(status=200)


async def numbers_prime_is_partition_prime_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_is_partition_prime_get

    Checks whether a given number is a known partition prime number or not.

    :param number: Number to check
    :type number: int

    """
    return web.Response(status=200)


async def numbers_prime_is_pell_prime_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_is_pell_prime_get

    Checks whether a given number is a known pell prime number or not.

    :param number: Number to check
    :type number: int

    """
    return web.Response(status=200)


async def numbers_prime_is_perfect_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_is_perfect_get

    Checks whether a given number is a perfect number or not.

    :param number: Number to check
    :type number: int

    """
    return web.Response(status=200)


async def numbers_prime_is_prime_get(request: web.Request, number=None) -> web.Response:
    """numbers_prime_is_prime_get

    Checks whether a given number is a known prime number or not.

    :param number: Number to check
    :type number: int

    """
    return web.Response(status=200)
