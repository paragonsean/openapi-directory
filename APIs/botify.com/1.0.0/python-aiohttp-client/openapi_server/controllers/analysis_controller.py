from typing import List, Dict
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
from openapi_server import util


async def create_urls_export(request: web.Request, username, project_slug, analysis_slug, area=None, body=None) -> web.Response:
    """Creates a new UrlExport object and starts a task that will export the results into a csv

    Creates a new UrlExport object and starts a task that will export the results into a csv. Returns the model id that manages the task

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param area: 
    :type area: str
    :param body: 
    :type body: dict | bytes

    """
    body = UrlsQuery.from_dict(body)
    return web.Response(status=200)


async def get_analysis_summary(request: web.Request, username, project_slug, analysis_slug) -> web.Response:
    """Get an Analysis detail

    Get an Analysis detail

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str

    """
    return web.Response(status=200)


async def get_crawl_statistics(request: web.Request, username, project_slug, analysis_slug) -> web.Response:
    """Return global statistics for an analysis

    Return global statistics for an analysis

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str

    """
    return web.Response(status=200)


async def get_crawl_statistics_by_frequency(request: web.Request, username, project_slug, analysis_slug, frequency, limit=None) -> web.Response:
    """Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min)

    Return crawl statistics grouped by time frequency (1 min, 5 mins or 60 min) for an analysis

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param frequency: Aggregation frequency
    :type frequency: str
    :param limit: max number of elements to retrieve
    :type limit: int

    """
    return web.Response(status=200)


async def get_crawl_statistics_urls(request: web.Request, username, project_slug, analysis_slug, list_type) -> web.Response:
    """Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)

    Return a list of 1000 latest URLs crawled (all crawled URLs or only URLS with HTTP errors)

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param list_type: URLs list type (crawled URLs or error URLs)
    :type list_type: str

    """
    return web.Response(status=200)


async def get_ganalytics_orphan_urls(request: web.Request, username, project_slug, analysis_slug, medium, source, page=None, size=None) -> web.Response:
    """List of Orphan URLs

    List of Orphan URLs. URLs which generated visits from the selected source according to Google Analytics data, but were not crawled with by the Botify crawler (either because no links to them were found on the website, or because the crawler was not allowed to follow these links according to the project settings).   For a search engine (medium: origanic; sources: all, aol, ask, baidu, bing, google, naver, yahoo, yandex) or a social network (medium: social; sources: all, facebook, google+, linkedin, pinterest, reddit, tumblr, twitter)

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param medium: Type of traffic, value: &#39;organic&#39; (from search engine)or &#39;social&#39; (from a social network)
    :type medium: str
    :param source: Traffic source, value: name of the search engine or social network
    :type source: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def get_links_percentiles(request: web.Request, username, project_slug, analysis_slug) -> web.Response:
    """Get inlinks percentiles

    Get inlinks percentiles

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str

    """
    return web.Response(status=200)


async def get_links_top_domains(request: web.Request, username, project_slug, analysis_slug, page=None, size=None) -> web.Response:
    """Top domains

    Top domains

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def get_links_top_subdomains(request: web.Request, username, project_slug, analysis_slug, page=None, size=None) -> web.Response:
    """Top subddomains

    Top subddomains

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def get_page_rank_lost(request: web.Request, username, project_slug, analysis_slug) -> web.Response:
    """Lost pagerank

    Lost pagerank

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str

    """
    return web.Response(status=200)


async def get_sitemaps_report(request: web.Request, username, project_slug, analysis_slug) -> web.Response:
    """Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc

    Get global information of the sitemaps found (sitemaps indexes, invalid sitemaps urls, etc.)

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str

    """
    return web.Response(status=200)


async def get_sitemaps_samples_out_of_config(request: web.Request, username, project_slug, analysis_slug, page=None, size=None) -> web.Response:
    """Sample list of URLs which were found in your sitemaps but outside of the

    Sample list of URLs which were found in your sitemaps but outside of the crawl perimeter defined for the project, for instance domain/subdomain or protocol (HTTP/HTTPS) not allowed in the crawl settings.

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def get_sitemaps_samples_sitemaps_only(request: web.Request, username, project_slug, analysis_slug, page=None, size=None) -> web.Response:
    """Sample list of URLs which were found in your sitemaps, within the project

    Sample list of URLs which were found in your sitemaps, within the project allowed scope (allowed domains/subdomains/protocols), but not found by the Botify crawler.

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def get_url_detail(request: web.Request, username, project_slug, analysis_slug, url, fields=None) -> web.Response:
    """Gets the detail of an URL for an analysis

    Gets the detail of an URL for an analysis

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param url: (Urlencoded) Searched URL
    :type url: str
    :param fields: comma separated list of fields to return (c.f. URLs Datamodel)
    :type fields: List[str]

    """
    return web.Response(status=200)


async def get_urls(request: web.Request, username, project_slug, analysis_slug, area=None, page=None, size=None, body=None) -> web.Response:
    """Executes a query and returns a paginated response

    Executes a query and returns a paginated response

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param area: Analysis context to execute the query
    :type area: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int
    :param body: 
    :type body: dict | bytes

    """
    body = UrlsQuery.from_dict(body)
    return web.Response(status=200)


async def get_urls_aggs(request: web.Request, username, project_slug, analysis_slug, area=None, body=None) -> web.Response:
    """Query aggregator

    Query aggregator. It accepts multiple queries

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param area: 
    :type area: str
    :param body: 
    :type body: list | bytes

    """
    body = [UrlsAggsQuery.from_dict(d) for d in body]
    return web.Response(status=200)


async def get_urls_datamodel(request: web.Request, username, project_slug, analysis_slug, area=None) -> web.Response:
    """Gets an Analysis datamodel

    Gets an Analysis datamodel

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param area: 
    :type area: str

    """
    return web.Response(status=200)


async def get_urls_export_status(request: web.Request, username, project_slug, analysis_slug, url_export_id) -> web.Response:
    """Checks the status of an CSVUrlExportJob object

    Checks the status of an CSVUrlExportJob object. Returns json object with the status.

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param url_export_id: Url Export ID
    :type url_export_id: str

    """
    return web.Response(status=200)


async def get_urls_exports(request: web.Request, username, project_slug, analysis_slug, page=None, size=None) -> web.Response:
    """A list of the CSV Exports requests and their current status

    A list of the CSV Exports requests and their current status

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def get_urls_suggested_filters(request: web.Request, username, project_slug, analysis_slug, area=None, body=None) -> web.Response:
    """Return most frequent segments (&#x3D; suggested patterns in the previous version)

    Return most frequent segments (&#x3D; suggested patterns in the previous version) for a Botify Query.

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param analysis_slug: Analysis&#39; identifier
    :type analysis_slug: str
    :param area: 
    :type area: str
    :param body: 
    :type body: dict | bytes

    """
    body = UrlsAggsQuery.from_dict(body)
    return web.Response(status=200)
