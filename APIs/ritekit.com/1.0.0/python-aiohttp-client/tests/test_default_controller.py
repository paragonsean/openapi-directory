# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_animate_image(client):
    """Test case for animate_image

    Animate Image
    """
    params = [('url', 'https://jpeg.org/images/jpeg-home.jpg'),
                    ('type', 'glint')]
    headers = { 
        'Accept': 'image/gif',
    }
    response = await client.request(
        method='GET',
        path='/v1/images/animate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_emojify(client):
    """Test case for auto_emojify

    Auto-Emojify
    """
    params = [('text', 'Why robots may soon steal all manufacturing jobs – but it’s not all bad news')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/emoji/auto-emojify',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auto_hashtag(client):
    """Test case for auto_hashtag

    Auto-Hashtag
    """
    params = [('post', 'Is artificial intelligence the future of customer service?'),
                    ('maxHashtags', 2),
                    ('hashtagPosition', 'auto')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/stats/auto-hashtag',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_logo(client):
    """Test case for company_logo

    Company Logo
    """
    params = [('domain', 'google.com')]
    headers = { 
        'Accept': 'image/png',
    }
    response = await client.request(
        method='GET',
        path='/v1/images/logo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_emoji_suggestions(client):
    """Test case for emoji_suggestions

    Emoji Suggestions
    """
    params = [('text', 'Why robots may soon steal all manufacturing jobs – but it’s not all bad news')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/emoji/suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hashtag_history(client):
    """Test case for hashtag_history

    Hashtag History
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/stats/history/{hashtag}'.format(hashtag='job'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hashtag_stats(client):
    """Test case for hashtag_stats

    Hashtag Stats
    """
    params = [('tags', [jobs,hello])]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/stats/multiple-hashtags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hashtag_suggestions(client):
    """Test case for hashtag_suggestions

    Hashtag Suggestions
    """
    params = [('text', 'seo')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/stats/hashtag-suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hashtags_cleaner(client):
    """Test case for hashtags_cleaner

    Hashtags cleaner
    """
    params = [('post', '#instaphotography #instabeauty #instagirls #instanature #instagirl #photography #beauty #girls #nature #girl #sky #water #lady #ladies #woman #women #photograph #photographs #beauties #sunlight #sitting #waters #skies #sit #photographies')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v2/instagram/hashtags-cleaner',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_of_ctas(client):
    """Test case for list_of_ctas

    List of CTAs
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/link/cta',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shorten_link(client):
    """Test case for shorten_link

    Shorten Link
    """
    params = [('url', 'https://ritekit.com'),
                    ('cta', 6530)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/link/short-link',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_text_to_image(client):
    """Test case for text_to_image

    Text to Image
    """
    params = [('quote', 'If you love life, don't waste time, for time is what life is made up of'),
                    ('author', 'Bruce Lee'),
                    ('fontSize', 60),
                    ('quoteFont', 'Lora'),
                    ('quoteFontColor', '#4f4f4f'),
                    ('authorFont', 'Lato Black'),
                    ('authorFontColor', '#e5e5e5'),
                    ('enableHighlight', 1),
                    ('highlightColor', '#f0ea66'),
                    ('bgType', 'gradient'),
                    ('backgroundColor', '#000000'),
                    ('gradientType', 'linear'),
                    ('gradientColor1', '#1ee691'),
                    ('gradientColor2', '#1ddad6'),
                    ('brandLogo', 'https://cdn.ritekit.com/assets/img/common/made-with-ritekit-white.png'),
                    ('animation', 'glint'),
                    ('showQuoteMark', 56)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/images/quote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trending_hashtags(client):
    """Test case for trending_hashtags

    Trending Hashtags
    """
    params = [('green', False),
                    ('latin', False)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/search/trending',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

