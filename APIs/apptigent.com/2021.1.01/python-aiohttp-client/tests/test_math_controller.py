# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_calculate_absolute(client):
    """Test case for calculate_absolute

    Math - Calculate Absolute
    """
    calculate_number = openapi_server.InputCalculateNumber()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateAbsolute',
        headers=headers,
        json=calculate_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_addition(client):
    """Test case for calculate_addition

    Math - Calculate Addition
    """
    calculate_numbers = openapi_server.InputCalculateNumbers()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateAddition',
        headers=headers,
        json=calculate_numbers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_average(client):
    """Test case for calculate_average

    Math - Calculate average
    """
    calculate_series = openapi_server.InputCalculateSeries()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateAverage',
        headers=headers,
        json=calculate_series,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_cosine(client):
    """Test case for calculate_cosine

    Math - Calculate Cosine
    """
    calculate_number = openapi_server.InputCalculateNumber()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateCosine',
        headers=headers,
        json=calculate_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_division(client):
    """Test case for calculate_division

    Math - Calculate Division
    """
    calculate_numbers = openapi_server.InputCalculateNumbers()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateDivision',
        headers=headers,
        json=calculate_numbers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_logarithm(client):
    """Test case for calculate_logarithm

    Math - Calculate Logarithm
    """
    calculate_number = openapi_server.InputCalculateNumber()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateLogarithm',
        headers=headers,
        json=calculate_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_median(client):
    """Test case for calculate_median

    Math - Calculate median
    """
    calculate_series = openapi_server.InputCalculateSeries()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateMedian',
        headers=headers,
        json=calculate_series,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_min_max(client):
    """Test case for calculate_min_max

    Math - Calculate minimum or maximum
    """
    calculate_series = openapi_server.InputCalculateMinMax()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateMinMax',
        headers=headers,
        json=calculate_series,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_modulo(client):
    """Test case for calculate_modulo

    Math - Calculate Modulo
    """
    calculate_numbers = openapi_server.InputCalculateNumbers()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateModulo',
        headers=headers,
        json=calculate_numbers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_multiplication(client):
    """Test case for calculate_multiplication

    Math - Calculate Multiplication
    """
    calculate_numbers = openapi_server.InputCalculateNumbers()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateMultiplication',
        headers=headers,
        json=calculate_numbers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_nth_root(client):
    """Test case for calculate_nth_root

    Math - Calculate Nth Root
    """
    calculate_numbers = openapi_server.InputCalculateNumbers()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateNthRoot',
        headers=headers,
        json=calculate_numbers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_power(client):
    """Test case for calculate_power

    Math - Calculate power
    """
    calculate_power = openapi_server.InputCalculatePower()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculatePower',
        headers=headers,
        json=calculate_power,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_sine(client):
    """Test case for calculate_sine

    Math - Calculate Sine
    """
    calculate_number = openapi_server.InputCalculateNumber()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateSine',
        headers=headers,
        json=calculate_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_square_root(client):
    """Test case for calculate_square_root

    Math - Calculate Square Root
    """
    calculate_number = openapi_server.InputCalculateNumber()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateSquareRoot',
        headers=headers,
        json=calculate_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_subtraction(client):
    """Test case for calculate_subtraction

    Math - Calculate Subtraction
    """
    calculate_numbers = openapi_server.InputCalculateNumbers()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateSubtraction',
        headers=headers,
        json=calculate_numbers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_sum(client):
    """Test case for calculate_sum

    Math - Calculate sum
    """
    calculate_series = openapi_server.InputCalculateSeries()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateSum',
        headers=headers,
        json=calculate_series,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_tangent(client):
    """Test case for calculate_tangent

    Math - Calculate Tangent
    """
    calculate_number = openapi_server.InputCalculateNumber()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateTangent',
        headers=headers,
        json=calculate_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_variance(client):
    """Test case for calculate_variance

    Math - Calculate variance
    """
    calculate_series = openapi_server.InputCalculateSeries()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CalculateVariance',
        headers=headers,
        json=calculate_series,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_angle(client):
    """Test case for convert_angle

    Math - Convert angle
    """
    convert_angle = openapi_server.InputConvertAngle()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertAngle',
        headers=headers,
        json=convert_angle,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_area(client):
    """Test case for convert_area

    Math - Convert area
    """
    convert_area = openapi_server.InputConvertArea()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertArea',
        headers=headers,
        json=convert_area,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_distance(client):
    """Test case for convert_distance

    Math - Convert distance
    """
    convert_distance = openapi_server.InputConvertDistance()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertDistance',
        headers=headers,
        json=convert_distance,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_duration(client):
    """Test case for convert_duration

    Math - Convert duration
    """
    convert_duration = openapi_server.InputConvertDuration()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertDuration',
        headers=headers,
        json=convert_duration,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_energy(client):
    """Test case for convert_energy

    Math - Convert energy
    """
    convert_energy = openapi_server.InputConvertEnergy()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertEnergy',
        headers=headers,
        json=convert_energy,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_power(client):
    """Test case for convert_power

    Math - Convert power
    """
    convert_power = openapi_server.InputConvertPower()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertPower',
        headers=headers,
        json=convert_power,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_speed(client):
    """Test case for convert_speed

    Math - Convert speed
    """
    convert_speed = openapi_server.InputConvertSpeed()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertSpeed',
        headers=headers,
        json=convert_speed,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_temperature(client):
    """Test case for convert_temperature

    Math - Convert temperature
    """
    convert_temperature = openapi_server.InputConvertTemperature()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertTemperature',
        headers=headers,
        json=convert_temperature,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_volume(client):
    """Test case for convert_volume

    Math - Convert volume
    """
    convert_volume = openapi_server.InputConvertVolume()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertVolume',
        headers=headers,
        json=convert_volume,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_weight(client):
    """Test case for convert_weight

    Math - Convert weight
    """
    convert_weight = openapi_server.InputConvertWeight()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertWeight',
        headers=headers,
        json=convert_weight,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_random_number(client):
    """Test case for random_number

    Math - Random number
    """
    number_range = openapi_server.InputNumberRange()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/RandomNumber',
        headers=headers,
        json=number_range,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_round_number(client):
    """Test case for round_number

    Math - Round number
    """
    calculate_number = openapi_server.InputCalculateNumber()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/RoundNumber',
        headers=headers,
        json=calculate_number,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_standard_deviation(client):
    """Test case for standard_deviation

    Math - Calculate standard deviation
    """
    calculate_series = openapi_server.InputCalculateSeries()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/StandardDeviation',
        headers=headers,
        json=calculate_series,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

