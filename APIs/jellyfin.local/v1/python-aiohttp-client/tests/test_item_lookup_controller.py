# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album_info_remote_search_query import AlbumInfoRemoteSearchQuery
from openapi_server.models.artist_info_remote_search_query import ArtistInfoRemoteSearchQuery
from openapi_server.models.book_info_remote_search_query import BookInfoRemoteSearchQuery
from openapi_server.models.box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery
from openapi_server.models.external_id_info import ExternalIdInfo
from openapi_server.models.movie_info_remote_search_query import MovieInfoRemoteSearchQuery
from openapi_server.models.music_video_info_remote_search_query import MusicVideoInfoRemoteSearchQuery
from openapi_server.models.person_lookup_info_remote_search_query import PersonLookupInfoRemoteSearchQuery
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.remote_search_result import RemoteSearchResult
from openapi_server.models.series_info_remote_search_query import SeriesInfoRemoteSearchQuery
from openapi_server.models.trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_apply_search_criteria(client):
    """Test case for apply_search_criteria

    Applies search criteria to an item and refreshes metadata.
    """
    body = {"IndexNumberEnd":6,"ProductionYear":5,"PremiereDate":"2000-01-23T04:56:07.000+00:00","ImageUrl":"ImageUrl","IndexNumber":0,"Overview":"Overview","ParentIndexNumber":1,"SearchProviderName":"SearchProviderName","Artists":[null,null],"ProviderIds":{"key":"ProviderIds"},"Name":"Name"}
    params = [('replaceAllImages', True)]
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/Apply/{item_id}'.format(item_id='item_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_book_remote_search_results(client):
    """Test case for get_book_remote_search_results

    Get book remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","SeriesName":"SeriesName","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/Book',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_box_set_remote_search_results(client):
    """Test case for get_box_set_remote_search_results

    Get box set remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/BoxSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_external_id_infos(client):
    """Test case for get_external_id_infos

    Get the item's external id info.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{item_id}/ExternalIdInfos'.format(item_id='item_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_movie_remote_search_results(client):
    """Test case for get_movie_remote_search_results

    Get movie remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/Movie',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_music_album_remote_search_results(client):
    """Test case for get_music_album_remote_search_results

    Get music album remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","PremiereDate":"2000-01-23T04:56:07.000+00:00","SongInfos":[{"Path":"Path","MetadataLanguage":"MetadataLanguage","PremiereDate":"2000-01-23T04:56:07.000+00:00","Album":"Album","MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":5,"IsAutomated":True,"Name":"Name","AlbumArtists":["AlbumArtists","AlbumArtists"],"Year":5,"IndexNumber":1,"Artists":["Artists","Artists"],"ProviderIds":{"key":"ProviderIds"}},{"Path":"Path","MetadataLanguage":"MetadataLanguage","PremiereDate":"2000-01-23T04:56:07.000+00:00","Album":"Album","MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":5,"IsAutomated":True,"Name":"Name","AlbumArtists":["AlbumArtists","AlbumArtists"],"Year":5,"IndexNumber":1,"Artists":["Artists","Artists"],"ProviderIds":{"key":"ProviderIds"}}],"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ArtistProviderIds":{"key":"ArtistProviderIds"},"IsAutomated":True,"Name":"Name","AlbumArtists":["AlbumArtists","AlbumArtists"],"Year":2,"IndexNumber":0,"ProviderIds":{"key":"ProviderIds"}},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/MusicAlbum',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_music_artist_remote_search_results(client):
    """Test case for get_music_artist_remote_search_results

    Get music artist remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"SongInfos":[{"Path":"Path","MetadataLanguage":"MetadataLanguage","PremiereDate":"2000-01-23T04:56:07.000+00:00","Album":"Album","MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":5,"IsAutomated":True,"Name":"Name","AlbumArtists":["AlbumArtists","AlbumArtists"],"Year":5,"IndexNumber":1,"Artists":["Artists","Artists"],"ProviderIds":{"key":"ProviderIds"}},{"Path":"Path","MetadataLanguage":"MetadataLanguage","PremiereDate":"2000-01-23T04:56:07.000+00:00","Album":"Album","MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":5,"IsAutomated":True,"Name":"Name","AlbumArtists":["AlbumArtists","AlbumArtists"],"Year":5,"IndexNumber":1,"Artists":["Artists","Artists"],"ProviderIds":{"key":"ProviderIds"}}],"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/MusicArtist',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_music_video_remote_search_results(client):
    """Test case for get_music_video_remote_search_results

    Get music video remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"Artists":["Artists","Artists"],"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/MusicVideo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_person_remote_search_results(client):
    """Test case for get_person_remote_search_results

    Get person remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/Person',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_search_image(client):
    """Test case for get_remote_search_image

    Gets a remote image.
    """
    params = [('imageUrl', 'image_url_example'),
                    ('providerName', 'provider_name_example')]
    headers = { 
        'Accept': 'image/*',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/RemoteSearch/Image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_series_remote_search_results(client):
    """Test case for get_series_remote_search_results

    Get series remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/Series',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_trailer_remote_search_results(client):
    """Test case for get_trailer_remote_search_results

    Get trailer remote search.
    """
    body = {"SearchInfo":{"Path":"Path","MetadataLanguage":"MetadataLanguage","Year":1,"PremiereDate":"2000-01-23T04:56:07.000+00:00","IndexNumber":0,"MetadataCountryCode":"MetadataCountryCode","ParentIndexNumber":6,"ProviderIds":{"key":"ProviderIds"},"IsAutomated":True,"Name":"Name"},"IncludeDisabledProviders":True,"SearchProviderName":"SearchProviderName","ItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Items/RemoteSearch/Trailer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

