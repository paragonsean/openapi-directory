from typing import List, Dict
from aiohttp import web

from openapi_server.models.input_calculate_min_max import InputCalculateMinMax
from openapi_server.models.input_calculate_number import InputCalculateNumber
from openapi_server.models.input_calculate_numbers import InputCalculateNumbers
from openapi_server.models.input_calculate_power import InputCalculatePower
from openapi_server.models.input_calculate_series import InputCalculateSeries
from openapi_server.models.input_convert_angle import InputConvertAngle
from openapi_server.models.input_convert_area import InputConvertArea
from openapi_server.models.input_convert_distance import InputConvertDistance
from openapi_server.models.input_convert_duration import InputConvertDuration
from openapi_server.models.input_convert_energy import InputConvertEnergy
from openapi_server.models.input_convert_power import InputConvertPower
from openapi_server.models.input_convert_speed import InputConvertSpeed
from openapi_server.models.input_convert_temperature import InputConvertTemperature
from openapi_server.models.input_convert_volume import InputConvertVolume
from openapi_server.models.input_convert_weight import InputConvertWeight
from openapi_server.models.input_number_range import InputNumberRange
from openapi_server.models.output_number import OutputNumber
from openapi_server.models.output_string import OutputString
from openapi_server import util


async def calculate_absolute(request: web.Request, calculate_number=None) -> web.Response:
    """Math - Calculate Absolute

    Calculate the absolute value of a number

    :param calculate_number: Number calculation parameters
    :type calculate_number: dict | bytes

    """
    calculate_number = InputCalculateNumber.from_dict(calculate_number)
    return web.Response(status=200)


async def calculate_addition(request: web.Request, calculate_numbers=None) -> web.Response:
    """Math - Calculate Addition

    Calculate the sum of two numbers

    :param calculate_numbers: Number calculation parameters
    :type calculate_numbers: dict | bytes

    """
    calculate_numbers = InputCalculateNumbers.from_dict(calculate_numbers)
    return web.Response(status=200)


async def calculate_average(request: web.Request, calculate_series=None) -> web.Response:
    """Math - Calculate average

    Calculate the average of two or more numbers

    :param calculate_series: Series calculation parameters
    :type calculate_series: dict | bytes

    """
    calculate_series = InputCalculateSeries.from_dict(calculate_series)
    return web.Response(status=200)


async def calculate_cosine(request: web.Request, calculate_number=None) -> web.Response:
    """Math - Calculate Cosine

    Calculate the cosine value of an angle

    :param calculate_number: Number calculation parameters
    :type calculate_number: dict | bytes

    """
    calculate_number = InputCalculateNumber.from_dict(calculate_number)
    return web.Response(status=200)


async def calculate_division(request: web.Request, calculate_numbers=None) -> web.Response:
    """Math - Calculate Division

    Calculate the quotient of two numbers

    :param calculate_numbers: Number calculation parameters
    :type calculate_numbers: dict | bytes

    """
    calculate_numbers = InputCalculateNumbers.from_dict(calculate_numbers)
    return web.Response(status=200)


async def calculate_logarithm(request: web.Request, calculate_number=None) -> web.Response:
    """Math - Calculate Logarithm

    Calculate the logarithm of a number

    :param calculate_number: Number calculation parameters
    :type calculate_number: dict | bytes

    """
    calculate_number = InputCalculateNumber.from_dict(calculate_number)
    return web.Response(status=200)


async def calculate_median(request: web.Request, calculate_series=None) -> web.Response:
    """Math - Calculate median

    Calculate the median of two or more numbers

    :param calculate_series: Series calculation parameters
    :type calculate_series: dict | bytes

    """
    calculate_series = InputCalculateSeries.from_dict(calculate_series)
    return web.Response(status=200)


async def calculate_min_max(request: web.Request, calculate_series=None) -> web.Response:
    """Math - Calculate minimum or maximum

    Calculate the minimum or maximum value in a sequence of numbers

    :param calculate_series: Series calculation parameters
    :type calculate_series: dict | bytes

    """
    calculate_series = InputCalculateMinMax.from_dict(calculate_series)
    return web.Response(status=200)


async def calculate_modulo(request: web.Request, calculate_numbers=None) -> web.Response:
    """Math - Calculate Modulo

    Calculate the remainder of dividing two numbers

    :param calculate_numbers: Number calculation parameters
    :type calculate_numbers: dict | bytes

    """
    calculate_numbers = InputCalculateNumbers.from_dict(calculate_numbers)
    return web.Response(status=200)


async def calculate_multiplication(request: web.Request, calculate_numbers=None) -> web.Response:
    """Math - Calculate Multiplication

    Calculate the product of two numbers

    :param calculate_numbers: Number calculation parameters
    :type calculate_numbers: dict | bytes

    """
    calculate_numbers = InputCalculateNumbers.from_dict(calculate_numbers)
    return web.Response(status=200)


async def calculate_nth_root(request: web.Request, calculate_numbers=None) -> web.Response:
    """Math - Calculate Nth Root

    Calculate the n-th root of a number

    :param calculate_numbers: Number calculation parameters
    :type calculate_numbers: dict | bytes

    """
    calculate_numbers = InputCalculateNumbers.from_dict(calculate_numbers)
    return web.Response(status=200)


async def calculate_power(request: web.Request, calculate_power=None) -> web.Response:
    """Math - Calculate power

    Raise number to a specified power

    :param calculate_power: Power calculation parameters
    :type calculate_power: dict | bytes

    """
    calculate_power = InputCalculatePower.from_dict(calculate_power)
    return web.Response(status=200)


async def calculate_sine(request: web.Request, calculate_number=None) -> web.Response:
    """Math - Calculate Sine

    Calculate the sine value of an angle

    :param calculate_number: Number calculation parameters
    :type calculate_number: dict | bytes

    """
    calculate_number = InputCalculateNumber.from_dict(calculate_number)
    return web.Response(status=200)


async def calculate_square_root(request: web.Request, calculate_number=None) -> web.Response:
    """Math - Calculate Square Root

    Calculate the square root of a number

    :param calculate_number: Number calculation parameters
    :type calculate_number: dict | bytes

    """
    calculate_number = InputCalculateNumber.from_dict(calculate_number)
    return web.Response(status=200)


async def calculate_subtraction(request: web.Request, calculate_numbers=None) -> web.Response:
    """Math - Calculate Subtraction

    Calculate the difference between two numbers

    :param calculate_numbers: Number calculation parameters
    :type calculate_numbers: dict | bytes

    """
    calculate_numbers = InputCalculateNumbers.from_dict(calculate_numbers)
    return web.Response(status=200)


async def calculate_sum(request: web.Request, calculate_series=None) -> web.Response:
    """Math - Calculate sum

    Calculate the sum of two or more numbers

    :param calculate_series: Series calculation parameters
    :type calculate_series: dict | bytes

    """
    calculate_series = InputCalculateSeries.from_dict(calculate_series)
    return web.Response(status=200)


async def calculate_tangent(request: web.Request, calculate_number=None) -> web.Response:
    """Math - Calculate Tangent

    Calculate the tangent value of an angle

    :param calculate_number: Number calculation parameters
    :type calculate_number: dict | bytes

    """
    calculate_number = InputCalculateNumber.from_dict(calculate_number)
    return web.Response(status=200)


async def calculate_variance(request: web.Request, calculate_series=None) -> web.Response:
    """Math - Calculate variance

    Calculate the statistical variance of two or more numbers

    :param calculate_series: Series calculation parameters
    :type calculate_series: dict | bytes

    """
    calculate_series = InputCalculateSeries.from_dict(calculate_series)
    return web.Response(status=200)


async def convert_angle(request: web.Request, convert_angle=None) -> web.Response:
    """Math - Convert angle

    Convert value from one angle measurement to another

    :param convert_angle: 
    :type convert_angle: dict | bytes

    """
    convert_angle = InputConvertAngle.from_dict(convert_angle)
    return web.Response(status=200)


async def convert_area(request: web.Request, convert_area=None) -> web.Response:
    """Math - Convert area

    Convert value from one area measurement to another

    :param convert_area: 
    :type convert_area: dict | bytes

    """
    convert_area = InputConvertArea.from_dict(convert_area)
    return web.Response(status=200)


async def convert_distance(request: web.Request, convert_distance=None) -> web.Response:
    """Math - Convert distance

    Convert value from one distance measurement to another

    :param convert_distance: 
    :type convert_distance: dict | bytes

    """
    convert_distance = InputConvertDistance.from_dict(convert_distance)
    return web.Response(status=200)


async def convert_duration(request: web.Request, convert_duration=None) -> web.Response:
    """Math - Convert duration

    Convert value from one duration measurement to another

    :param convert_duration: 
    :type convert_duration: dict | bytes

    """
    convert_duration = InputConvertDuration.from_dict(convert_duration)
    return web.Response(status=200)


async def convert_energy(request: web.Request, convert_energy=None) -> web.Response:
    """Math - Convert energy

    Convert value from one energy measurement to another

    :param convert_energy: 
    :type convert_energy: dict | bytes

    """
    convert_energy = InputConvertEnergy.from_dict(convert_energy)
    return web.Response(status=200)


async def convert_power(request: web.Request, convert_power=None) -> web.Response:
    """Math - Convert power

    Convert value from one power measurement to another

    :param convert_power: 
    :type convert_power: dict | bytes

    """
    convert_power = InputConvertPower.from_dict(convert_power)
    return web.Response(status=200)


async def convert_speed(request: web.Request, convert_speed=None) -> web.Response:
    """Math - Convert speed

    Convert value from one speed measurement to another

    :param convert_speed: 
    :type convert_speed: dict | bytes

    """
    convert_speed = InputConvertSpeed.from_dict(convert_speed)
    return web.Response(status=200)


async def convert_temperature(request: web.Request, convert_temperature=None) -> web.Response:
    """Math - Convert temperature

    Convert value from one temperature measurement to another

    :param convert_temperature: 
    :type convert_temperature: dict | bytes

    """
    convert_temperature = InputConvertTemperature.from_dict(convert_temperature)
    return web.Response(status=200)


async def convert_volume(request: web.Request, convert_volume=None) -> web.Response:
    """Math - Convert volume

    Convert value from one volume measurement to another

    :param convert_volume: 
    :type convert_volume: dict | bytes

    """
    convert_volume = InputConvertVolume.from_dict(convert_volume)
    return web.Response(status=200)


async def convert_weight(request: web.Request, convert_weight=None) -> web.Response:
    """Math - Convert weight

    Convert value from one weight measurement to another

    :param convert_weight: 
    :type convert_weight: dict | bytes

    """
    convert_weight = InputConvertWeight.from_dict(convert_weight)
    return web.Response(status=200)


async def random_number(request: web.Request, number_range=None) -> web.Response:
    """Math - Random number

    Generate a random number within a specified range

    :param number_range: 
    :type number_range: dict | bytes

    """
    number_range = InputNumberRange.from_dict(number_range)
    return web.Response(status=200)


async def round_number(request: web.Request, calculate_number=None) -> web.Response:
    """Math - Round number

    Round a numeric value up or down

    :param calculate_number: Numeric calculation parameters
    :type calculate_number: dict | bytes

    """
    calculate_number = InputCalculateNumber.from_dict(calculate_number)
    return web.Response(status=200)


async def standard_deviation(request: web.Request, calculate_series=None) -> web.Response:
    """Math - Calculate standard deviation

    Calculate the standard deviation of two or more numbers

    :param calculate_series: Series calculation parameters
    :type calculate_series: dict | bytes

    """
    calculate_series = InputCalculateSeries.from_dict(calculate_series)
    return web.Response(status=200)
