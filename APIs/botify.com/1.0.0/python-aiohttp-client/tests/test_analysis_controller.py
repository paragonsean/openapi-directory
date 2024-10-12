# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_detail import AnalysisDetail
from openapi_server.models.crawl_datamodel import CrawlDatamodel
from openapi_server.models.crawl_statistics import CrawlStatistics
from openapi_server.models.crawl_statistics_time import CrawlStatisticsTime
from openapi_server.models.csv_export_status import CsvExportStatus
from openapi_server.models.default_payload import DefaultPayload
from openapi_server.models.get_ganalytics_orphan_urls200_response import GetGanalyticsOrphanURLs200Response
from openapi_server.models.get_links_top_domains200_response import GetLinksTopDomains200Response
from openapi_server.models.get_sitemaps_samples_out_of_config200_response import GetSitemapsSamplesOutOfConfig200Response
from openapi_server.models.get_urls200_response import GetUrls200Response
from openapi_server.models.get_urls_exports200_response import GetUrlsExports200Response
from openapi_server.models.links_percentiles import LinksPercentiles
from openapi_server.models.page_rank_lost import PageRankLost
from openapi_server.models.sitemaps_report import SitemapsReport
from openapi_server.models.urls_aggs_query import UrlsAggsQuery
from openapi_server.models.urls_query import UrlsQuery


pytestmark = pytest.mark.asyncio

async def test_create_urls_export(client):
    """Test case for create_urls_export

    Creates a new UrlExport object and starts a task that will export the results into a csv
    """
    body = {"filters":"{}","sort":["{}","{}"],"fields":["fields","fields"]}
    params = [('area', current)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls/export'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_analysis_summary(client):
    """Test case for get_analysis_summary

    Get an Analysis detail
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crawl_statistics(client):
    """Test case for get_crawl_statistics

    Return global statistics for an analysis
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crawl_statistics_by_frequency(client):
    """Test case for get_crawl_statistics_by_frequency

    Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min)
    """
    params = [('limit', 56),
                    ('frequency', 'frequency_example')]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics/time'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crawl_statistics_urls(client):
    """Test case for get_crawl_statistics_urls

    Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/crawl_statistics/urls/{list_type}'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example', list_type='list_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ganalytics_orphan_urls(client):
    """Test case for get_ganalytics_orphan_urls

    List of Orphan URLs
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/ganalytics/orphan_urls/{medium}/{source}'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example', medium='medium_example', source='source_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_links_percentiles(client):
    """Test case for get_links_percentiles

    Get inlinks percentiles
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/links/percentiles'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_links_top_domains(client):
    """Test case for get_links_top_domains

    Top domains
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/top_domains/domains'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_links_top_subdomains(client):
    """Test case for get_links_top_subdomains

    Top subddomains
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/top_domains/subdomains'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_page_rank_lost(client):
    """Test case for get_page_rank_lost

    Lost pagerank
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/pagerank/lost'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sitemaps_report(client):
    """Test case for get_sitemaps_report

    Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/report'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sitemaps_samples_out_of_config(client):
    """Test case for get_sitemaps_samples_out_of_config

    Sample list of URLs which were found in your sitemaps but outside of the
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/samples/out_of_config'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sitemaps_samples_sitemaps_only(client):
    """Test case for get_sitemaps_samples_sitemaps_only

    Sample list of URLs which were found in your sitemaps, within the project
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/sitemaps/samples/sitemap_only'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_url_detail(client):
    """Test case for get_url_detail

    Gets the detail of an URL for an analysis
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls/{url}'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example', url='url_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_urls(client):
    """Test case for get_urls

    Executes a query and returns a paginated response
    """
    body = {"filters":"{}","sort":["{}","{}"],"fields":["fields","fields"]}
    params = [('area', current),
                    ('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_urls_aggs(client):
    """Test case for get_urls_aggs

    Query aggregator
    """
    body = {"filters":"{}","aggs":["{}","{}"]}
    params = [('area', current)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls/aggs'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_urls_datamodel(client):
    """Test case for get_urls_datamodel

    Gets an Analysis datamodel
    """
    params = [('area', current)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls/datamodel'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_urls_export_status(client):
    """Test case for get_urls_export_status

    Checks the status of an CSVUrlExportJob object
    """
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls/export/{url_export_id}'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example', url_export_id='url_export_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_urls_exports(client):
    """Test case for get_urls_exports

    A list of the CSV Exports requests and their current status
    """
    params = [('page', 56),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls/export'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_urls_suggested_filters(client):
    """Test case for get_urls_suggested_filters

    Return most frequent segments (= suggested patterns in the previous version)
    """
    body = {"filters":"{}","aggs":["{}","{}"]}
    params = [('area', current)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DjangoRestToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/analyses/{username}/{project_slug}/{analysis_slug}/urls/suggested_filters'.format(username='username_example', project_slug='project_slug_example', analysis_slug='analysis_slug_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

