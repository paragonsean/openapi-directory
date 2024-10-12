# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_virtual_folder_dto import AddVirtualFolderDto
from openapi_server.models.media_path_dto import MediaPathDto
from openapi_server.models.media_path_info import MediaPathInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.update_library_options_dto import UpdateLibraryOptionsDto
from openapi_server.models.virtual_folder_info import VirtualFolderInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_media_path(client):
    """Test case for add_media_path

    Add a media path to a library.
    """
    body = {"Path":"Path","PathInfo":{"Path":"Path","NetworkPath":"NetworkPath"},"Name":"Name"}
    params = [('refreshLibrary', False)]
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/VirtualFolders/Paths',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_virtual_folder(client):
    """Test case for add_virtual_folder

    Adds a virtual folder.
    """
    body = {"LibraryOptions":{"SaveSubtitlesWithMedia":True,"EnableInternetProviders":True,"MetadataCountryCode":"MetadataCountryCode","MetadataSavers":["MetadataSavers","MetadataSavers"],"SaveLocalMetadata":True,"SeasonZeroDisplayName":"SeasonZeroDisplayName","EnableEmbeddedTitles":True,"EnableChapterImageExtraction":True,"AutomaticRefreshIntervalDays":0,"SubtitleFetcherOrder":["SubtitleFetcherOrder","SubtitleFetcherOrder"],"TypeOptions":[{"Type":"Type","MetadataFetcherOrder":["MetadataFetcherOrder","MetadataFetcherOrder"],"ImageFetchers":["ImageFetchers","ImageFetchers"],"ImageOptions":[{"Type":"Primary","Limit":0,"MinWidth":6},{"Type":"Primary","Limit":0,"MinWidth":6}],"ImageFetcherOrder":["ImageFetcherOrder","ImageFetcherOrder"],"MetadataFetchers":["MetadataFetchers","MetadataFetchers"]},{"Type":"Type","MetadataFetcherOrder":["MetadataFetcherOrder","MetadataFetcherOrder"],"ImageFetchers":["ImageFetchers","ImageFetchers"],"ImageOptions":[{"Type":"Primary","Limit":0,"MinWidth":6},{"Type":"Primary","Limit":0,"MinWidth":6}],"ImageFetcherOrder":["ImageFetcherOrder","ImageFetcherOrder"],"MetadataFetchers":["MetadataFetchers","MetadataFetchers"]}],"EnableRealtimeMonitor":True,"EnableAutomaticSeriesGrouping":True,"ExtractChapterImagesDuringLibraryScan":True,"SubtitleDownloadLanguages":["SubtitleDownloadLanguages","SubtitleDownloadLanguages"],"DisabledLocalMetadataReaders":["DisabledLocalMetadataReaders","DisabledLocalMetadataReaders"],"PreferredMetadataLanguage":"PreferredMetadataLanguage","EnableEmbeddedEpisodeInfos":True,"SkipSubtitlesIfAudioTrackMatches":True,"RequirePerfectSubtitleMatch":True,"EnablePhotos":True,"SkipSubtitlesIfEmbeddedSubtitlesPresent":True,"DisabledSubtitleFetchers":["DisabledSubtitleFetchers","DisabledSubtitleFetchers"],"PathInfos":[{"Path":"Path","NetworkPath":"NetworkPath"},{"Path":"Path","NetworkPath":"NetworkPath"}],"LocalMetadataReaderOrder":["LocalMetadataReaderOrder","LocalMetadataReaderOrder"]}}
    params = [('name', 'name_example'),
                    ('collectionType', 'collection_type_example'),
                    ('paths', ['paths_example']),
                    ('refreshLibrary', False)]
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/VirtualFolders',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_virtual_folders(client):
    """Test case for get_virtual_folders

    Gets all virtual folders.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Library/VirtualFolders',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_media_path(client):
    """Test case for remove_media_path

    Remove a media path.
    """
    params = [('name', 'name_example'),
                    ('path', 'path_example'),
                    ('refreshLibrary', False)]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Library/VirtualFolders/Paths',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_virtual_folder(client):
    """Test case for remove_virtual_folder

    Removes a virtual folder.
    """
    params = [('name', 'name_example'),
                    ('refreshLibrary', False)]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Library/VirtualFolders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_virtual_folder(client):
    """Test case for rename_virtual_folder

    Renames a virtual folder.
    """
    params = [('name', 'name_example'),
                    ('newName', 'new_name_example'),
                    ('refreshLibrary', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/VirtualFolders/Name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_library_options(client):
    """Test case for update_library_options

    Update library options.
    """
    body = {"LibraryOptions":{"SaveSubtitlesWithMedia":True,"EnableInternetProviders":True,"MetadataCountryCode":"MetadataCountryCode","MetadataSavers":["MetadataSavers","MetadataSavers"],"SaveLocalMetadata":True,"SeasonZeroDisplayName":"SeasonZeroDisplayName","EnableEmbeddedTitles":True,"EnableChapterImageExtraction":True,"AutomaticRefreshIntervalDays":0,"SubtitleFetcherOrder":["SubtitleFetcherOrder","SubtitleFetcherOrder"],"TypeOptions":[{"Type":"Type","MetadataFetcherOrder":["MetadataFetcherOrder","MetadataFetcherOrder"],"ImageFetchers":["ImageFetchers","ImageFetchers"],"ImageOptions":[{"Type":"Primary","Limit":0,"MinWidth":6},{"Type":"Primary","Limit":0,"MinWidth":6}],"ImageFetcherOrder":["ImageFetcherOrder","ImageFetcherOrder"],"MetadataFetchers":["MetadataFetchers","MetadataFetchers"]},{"Type":"Type","MetadataFetcherOrder":["MetadataFetcherOrder","MetadataFetcherOrder"],"ImageFetchers":["ImageFetchers","ImageFetchers"],"ImageOptions":[{"Type":"Primary","Limit":0,"MinWidth":6},{"Type":"Primary","Limit":0,"MinWidth":6}],"ImageFetcherOrder":["ImageFetcherOrder","ImageFetcherOrder"],"MetadataFetchers":["MetadataFetchers","MetadataFetchers"]}],"EnableRealtimeMonitor":True,"EnableAutomaticSeriesGrouping":True,"ExtractChapterImagesDuringLibraryScan":True,"SubtitleDownloadLanguages":["SubtitleDownloadLanguages","SubtitleDownloadLanguages"],"DisabledLocalMetadataReaders":["DisabledLocalMetadataReaders","DisabledLocalMetadataReaders"],"PreferredMetadataLanguage":"PreferredMetadataLanguage","EnableEmbeddedEpisodeInfos":True,"SkipSubtitlesIfAudioTrackMatches":True,"RequirePerfectSubtitleMatch":True,"EnablePhotos":True,"SkipSubtitlesIfEmbeddedSubtitlesPresent":True,"DisabledSubtitleFetchers":["DisabledSubtitleFetchers","DisabledSubtitleFetchers"],"PathInfos":[{"Path":"Path","NetworkPath":"NetworkPath"},{"Path":"Path","NetworkPath":"NetworkPath"}],"LocalMetadataReaderOrder":["LocalMetadataReaderOrder","LocalMetadataReaderOrder"]},"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/VirtualFolders/LibraryOptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_media_path(client):
    """Test case for update_media_path

    Updates a media path.
    """
    body = {"Path":"Path","NetworkPath":"NetworkPath"}
    params = [('name', 'name_example')]
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Library/VirtualFolders/Paths/Update',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

