from typing import List, Dict
from aiohttp import web

from openapi_server.models.classes_wrapper import ClassesWrapper
from openapi_server.models.competition import Competition
from openapi_server.models.competitions_wrapper import CompetitionsWrapper
from openapi_server.models.errors_wrapper import ErrorsWrapper
from openapi_server.models.events_wrapper import EventsWrapper
from openapi_server.models.market_groups_wrapper import MarketGroupsWrapper
from openapi_server.models.markets_wrapper import MarketsWrapper
from openapi_server.models.selections_wrapper import SelectionsWrapper
from openapi_server.models.sports_wrapper import SportsWrapper
from openapi_server.models.top_bets_wrapper import TopBetsWrapper
from openapi_server import util


async def get_classes_for_sport(request: web.Request, api_key, sport_id, is_published=None, fields=None, include=None, exclude=None, displayed=None, channel=None, status=None, sort=None, offset=None, limit=None, culture=None) -> web.Response:
    """Retrieves a list of classes for a given sport id.

    Retrieves a list of classes for a given sport id.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param sport_id: The sport id to retrieve information for.
    :type sport_id: str
    :param is_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type is_published: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param displayed: Specify whether to return displayed entities or not
    :type displayed: str
    :param channel: Specify a channel filter and only results from that channel will be returned
    :type channel: str
    :param status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type status: str
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param limit: Specify the number of results to return
    :type limit: int
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str

    """
    return web.Response(status=200)


async def get_competition(request: web.Request, api_key, competition_id, fields=None, include=None, exclude=None, culture=None) -> web.Response:
    """Retrieves a specific competition

    Retrieves a specific competition

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param competition_id: The competition id to retrieve information for.
    :type competition_id: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str

    """
    return web.Response(status=200)


async def get_competitions_for_class(request: web.Request, api_key, class_id, is_published=None, fields=None, include=None, exclude=None, displayed=None, channel=None, status=None, sort=None, offset=None, limit=None, culture=None) -> web.Response:
    """Retrieves a list of competitions for a given class id.

    Retrieves a list of competitions for a given class id.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param class_id: The class id to retrieve information for.
    :type class_id: str
    :param is_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type is_published: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param displayed: Specify whether to return displayed entities or not
    :type displayed: str
    :param channel: Specify a channel filter and only results from that channel will be returned
    :type channel: str
    :param status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type status: str
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param limit: Specify the number of results to return
    :type limit: int
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str

    """
    return web.Response(status=200)


async def get_competitions_for_sport(request: web.Request, api_key, sport_id, is_published=None, fields=None, include=None, exclude=None, displayed=None, channel=None, status=None, sort=None, offset=None, limit=None, culture=None) -> web.Response:
    """Retrieves a list of competitions for a given sport id.

    Retrieves a list of competitions for a given sport id.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param sport_id: The sport id to retrieve information for.
    :type sport_id: str
    :param is_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type is_published: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param displayed: Specify whether to return displayed entities or not
    :type displayed: str
    :param channel: Specify a channel filter and only results from that channel will be returned
    :type channel: str
    :param status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type status: str
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param limit: Specify the number of results to return
    :type limit: int
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str

    """
    return web.Response(status=200)


async def get_event(request: web.Request, api_key, event_id, include_all_descendants=None, fields=None, include=None, exclude=None, headline_summary=None, market_count=None, market_ids=None, include_empty=None, culture=None, market_published=None, market_status=None, market_displayed=None, market_channel=None, market_sort=None, market_ew=None, selection_status=None, selection_channel=None, selection_published=None) -> web.Response:
    """Retrieves a single event by ID.

    Retrieves a single event by ID.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param event_id: The event ID to retrieve information for.
    :type event_id: str
    :param include_all_descendants: Include every descendant in the below heirarchy
    :type include_all_descendants: bool
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param headline_summary: Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    :type headline_summary: bool
    :param market_count: Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    :type market_count: int
    :param market_ids: Comma-seaerated list of market IDs to filter by
    :type market_ids: List[str]
    :param include_empty: When declared as false it should exclude markets and events that have no selections / markets
    :type include_empty: bool
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param market_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type market_published: str
    :param market_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type market_status: str
    :param market_displayed: Specify whether to return displayed entities or not
    :type market_displayed: str
    :param market_channel: Specify a channel filter and only results from that channel will be returned
    :type market_channel: str
    :param market_sort: Filter by market sort (e.g. MR (match result) -- (Outright)).
    :type market_sort: str
    :param market_ew: Specify whether to return markets with each way betting or those without
    :type market_ew: str
    :param selection_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type selection_status: str
    :param selection_channel: Specify a channel filter and only results from that channel will be returned
    :type selection_channel: str
    :param selection_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type selection_published: str

    """
    return web.Response(status=200)


async def get_events(request: web.Request, api_key, ids=None, is_published=None, include_all_descendants=None, fields=None, include=None, exclude=None, channel=None, settled=None, include_empty=None, headline_summary=None, market_count=None, sort=None, offset=None, limit=None, market_ids=None, culture=None, market_published=None, market_status=None, market_displayed=None, market_channel=None, market_sort=None, market_ew=None, selection_status=None, selection_channel=None, selection_published=None) -> web.Response:
    """Retrieves a list of events for the provided IDs.

    Retrieves a list of events for the provided IDs.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param ids: A comma-separated list of selectionIds
    :type ids: List[str]
    :param is_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type is_published: str
    :param include_all_descendants: Include every descendant in the below heirarchy
    :type include_all_descendants: bool
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param channel: Specify a channel filter and only results from that channel will be returned
    :type channel: str
    :param settled: Specify wether only settled entities should be returned
    :type settled: bool
    :param include_empty: When declared as false it should exclude markets and events that have no selections / markets
    :type include_empty: bool
    :param headline_summary: Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    :type headline_summary: bool
    :param market_count: Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    :type market_count: int
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param limit: Specify the number of results to return
    :type limit: int
    :param market_ids: Comma-seaerated list of market IDs to filter by
    :type market_ids: List[str]
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param market_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type market_published: str
    :param market_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type market_status: str
    :param market_displayed: Specify whether to return displayed entities or not
    :type market_displayed: str
    :param market_channel: Specify a channel filter and only results from that channel will be returned
    :type market_channel: str
    :param market_sort: Filter by market sort (e.g. MR (match result) -- (Outright)).
    :type market_sort: str
    :param market_ew: Specify whether to return markets with each way betting or those without
    :type market_ew: str
    :param selection_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type selection_status: str
    :param selection_channel: Specify a channel filter and only results from that channel will be returned
    :type selection_channel: str
    :param selection_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type selection_published: str

    """
    return web.Response(status=200)


async def get_events_for_class(request: web.Request, api_key, class_id, is_published=None, fields=None, include=None, exclude=None, displayed=None, channel=None, settled=None, include_empty=None, status=None, sort=None, offset=None, limit=None, headline_summary=None, include_all_descendants=None, is_in_play=None, market_count=None, _date=None, date_from=None, date_to=None, event_sort=None, culture=None, market_published=None, market_status=None, market_displayed=None, market_channel=None, market_sort=None, market_ew=None, selection_status=None, selection_channel=None, selection_published=None) -> web.Response:
    """Retrieves a list of events for a given class id.

    Retrieves a list of events for a given class id. &#39;includeAllDescendants&#39; parameter should be accompanied with &#39;date&#39; filter or one of &#39;dateFrom&#39; and &#39;dateTo&#39; filters.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param class_id: The class id to retrieve information for.
    :type class_id: str
    :param is_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type is_published: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param displayed: Specify whether to return displayed entities or not
    :type displayed: str
    :param channel: Specify a channel filter and only results from that channel will be returned
    :type channel: str
    :param settled: Specify wether only settled entities should be returned
    :type settled: bool
    :param include_empty: When declared as false it should exclude markets and events that have no selections / markets
    :type include_empty: bool
    :param status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type status: str
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param limit: Specify the number of results to return
    :type limit: int
    :param headline_summary: Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    :type headline_summary: bool
    :param include_all_descendants: Include every descendant in the below heirarchy
    :type include_all_descendants: bool
    :param is_in_play: Show only events that are in-play
    :type is_in_play: bool
    :param market_count: Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    :type market_count: int
    :param _date: Return only events for the specified date (yyyy-MM-dd).
    :type _date: str
    :param date_from: The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    :type date_from: str
    :param date_to: The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    :type date_to: str
    :param event_sort: Filter event by event sort
    :type event_sort: str
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param market_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type market_published: str
    :param market_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type market_status: str
    :param market_displayed: Specify whether to return displayed entities or not
    :type market_displayed: str
    :param market_channel: Specify a channel filter and only results from that channel will be returned
    :type market_channel: str
    :param market_sort: Filter by market sort (e.g. MR (match result) -- (Outright)).
    :type market_sort: str
    :param market_ew: Specify whether to return markets with each way betting or those without
    :type market_ew: str
    :param selection_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type selection_status: str
    :param selection_channel: Specify a channel filter and only results from that channel will be returned
    :type selection_channel: str
    :param selection_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type selection_published: str

    """
    return web.Response(status=200)


async def get_events_for_competition(request: web.Request, api_key, competition_id, is_published=None, fields=None, include=None, exclude=None, displayed=None, channel=None, settled=None, include_empty=None, status=None, sort=None, offset=None, limit=None, headline_summary=None, include_all_descendants=None, is_in_play=None, market_count=None, _date=None, date_from=None, date_to=None, market_group_id=None, event_sort=None, culture=None, market_published=None, market_status=None, market_displayed=None, market_channel=None, market_sort=None, market_ew=None, selection_status=None, selection_channel=None, selection_published=None) -> web.Response:
    """Retrieves a list of events for a given competition id.

    Retrieves a list of events for a given competition id. &#39;headlineSummary&#39; and includeAllDescendants parameters should be accompanied with &#39;date&#39; filter or one of &#39;dateFrom&#39; and &#39;dateTo&#39; filters.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param competition_id: The competition id to retrieve information for.
    :type competition_id: str
    :param is_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type is_published: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param displayed: Specify whether to return displayed entities or not
    :type displayed: str
    :param channel: Specify a channel filter and only results from that channel will be returned
    :type channel: str
    :param settled: Specify wether only settled entities should be returned
    :type settled: bool
    :param include_empty: When declared as false it should exclude markets and events that have no selections / markets
    :type include_empty: bool
    :param status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type status: str
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param limit: Specify the number of results to return
    :type limit: int
    :param headline_summary: Return only headline markets (Markets with the lowest display order) Either 1 InPlay and 1 Pre-Match, or the amount specified in marketCount, if available. Markets and Outcomes will be returned.
    :type headline_summary: bool
    :param include_all_descendants: Include every descendant in the below heirarchy
    :type include_all_descendants: bool
    :param is_in_play: Show only events that are in-play
    :type is_in_play: bool
    :param market_count: Specify the number of markets to return when requesting headlineSummary. This count of InPlay and Pre-Match markets will be returned.For example, when specifying 1, 1 In Play and 1 Pre Match market will be returned.
    :type market_count: int
    :param _date: Return only events for the specified date (yyyy-MM-dd).
    :type _date: str
    :param date_from: The UTC datetime from the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    :type date_from: str
    :param date_to: The UTC datetime TO the events to be returned. (yyyy-MM-ddTHH:mm:ss)
    :type date_to: str
    :param market_group_id: Filter by marketGroupId (e.g. OB_MG1276585).
    :type market_group_id: str
    :param event_sort: Filter event by event sort
    :type event_sort: str
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param market_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type market_published: str
    :param market_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type market_status: str
    :param market_displayed: Specify whether to return displayed entities or not
    :type market_displayed: str
    :param market_channel: Specify a channel filter and only results from that channel will be returned
    :type market_channel: str
    :param market_sort: Filter by market sort (e.g. MR (match result) -- (Outright)).
    :type market_sort: str
    :param market_ew: Specify whether to return markets with each way betting or those without
    :type market_ew: str
    :param selection_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type selection_status: str
    :param selection_channel: Specify a channel filter and only results from that channel will be returned
    :type selection_channel: str
    :param selection_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type selection_published: str

    """
    return web.Response(status=200)


async def get_market_groups_for_competition(request: web.Request, api_key, competition_id, fields=None, include=None, exclude=None, sort=None, offset=None, limit=None, culture=None, name=None) -> web.Response:
    """Retrieves a list of market groups for a given competition id

    Retrieves a list of market groups for a given competition id

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param competition_id: The competition id to retrieve information for.
    :type competition_id: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param limit: Specify the number of results to return
    :type limit: int
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param name: Filter by market group name
    :type name: str

    """
    return web.Response(status=200)


async def get_markets(request: web.Request, api_key, event_id, ids=None, include_all_descendants=None, fields=None, include=None, exclude=None, include_empty=None, culture=None, market_published=None, market_status=None, market_displayed=None, market_channel=None, market_sort=None, market_ew=None, selection_status=None, selection_channel=None, selection_published=None) -> web.Response:
    """Gets one or more specific markets

    Retrieves one or more specific markets. Markets with Live at the end are always In-Play markets. However, not ALL In-Play markets have Live at the end of the market name.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param event_id: The event ID to retrieve information for.
    :type event_id: str
    :param ids: A comma-separated list of selectionIds
    :type ids: List[str]
    :param include_all_descendants: Include every descendant in the below heirarchy
    :type include_all_descendants: bool
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param include_empty: When declared as false it should exclude markets and events that have no selections / markets
    :type include_empty: bool
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param market_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type market_published: str
    :param market_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type market_status: str
    :param market_displayed: Specify whether to return displayed entities or not
    :type market_displayed: str
    :param market_channel: Specify a channel filter and only results from that channel will be returned
    :type market_channel: str
    :param market_sort: Filter by market sort (e.g. MR (match result) -- (Outright)).
    :type market_sort: str
    :param market_ew: Specify whether to return markets with each way betting or those without
    :type market_ew: str
    :param selection_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type selection_status: str
    :param selection_channel: Specify a channel filter and only results from that channel will be returned
    :type selection_channel: str
    :param selection_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type selection_published: str

    """
    return web.Response(status=200)


async def get_markets_by_group_id(request: web.Request, api_key, competition_id, market_sort, market_group_id, fields=None, include=None, exclude=None) -> web.Response:
    """Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId

    Retrieves a list of events/markets/selections where markets within said event match selected sort/groupId

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param competition_id: The competition id to retrieve information for.
    :type competition_id: str
    :param market_sort: Filter by market sort (e.g. MR (match result) -- (Outright)).
    :type market_sort: str
    :param market_group_id: Filter by marketGroupId (e.g. OB_MG1276585).
    :type market_group_id: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]

    """
    return web.Response(status=200)


async def get_selections(request: web.Request, api_key, event_id, market_id, ids=None, fields=None, include=None, exclude=None, culture=None, selection_status=None, selection_channel=None, selection_published=None) -> web.Response:
    """Gets one or more selections for a market

    Retrieves one or more selections for a market

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param event_id: The event ID to retrieve information for.
    :type event_id: str
    :param market_id: The market id to retrieve information for
    :type market_id: str
    :param ids: A comma-separated list of selectionIds
    :type ids: List[str]
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param selection_status: Specify a status to filter results by. This is currently A (active) or S (suspended)
    :type selection_status: str
    :param selection_channel: Specify a channel filter and only results from that channel will be returned
    :type selection_channel: str
    :param selection_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type selection_published: str

    """
    return web.Response(status=200)


async def get_sports(request: web.Request, api_key, sort=None, offset=None, is_published=None, limit=None, fields=None, include=None, exclude=None, culture=None) -> web.Response:
    """Gets a list of all sports

    Gets a list of all sports

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param sort: The field to order the response by, followed by the order. For example: name,desc
    :type sort: str
    :param offset: Skip over a number of elements by specifying a start value for the query
    :type offset: int
    :param is_published: Specify whether only active entities should be returned, according to the William Hill definition of active
    :type is_published: str
    :param limit: Specify the number of results to return
    :type limit: int
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str

    """
    return web.Response(status=200)


async def get_top_bets(request: web.Request, api_key, sport_ids=None, competition_ids=None, limit=None, fields=None, include=None, exclude=None, param_top_bet_event_id=None, sort_name=None, culture=None, locale=None) -> web.Response:
    """Retrieves a weighted list of Selections.

    Retrieves a weighted list of Selections.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param sport_ids: A comma-separated list of sportsIds for which to retrieve topBets for
    :type sport_ids: List[str]
    :param competition_ids: A comma-separated list of competitionIds for which to retrieve topBets for
    :type competition_ids: List[str]
    :param limit: Specify the number of results to return
    :type limit: int
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]
    :param param_top_bet_event_id: The event ID to retrieve top bet information for. Multiple events up to 5 may be used
    :type param_top_bet_event_id: str
    :param sort_name: The market sort code used to further filter event results. Please note this can only be used with event id(s).
    :type sort_name: str
    :param culture: Code used to return responses in language other than English, acceptable values are en-GB|de-DE|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type culture: str
    :param locale: Code used to select a set of top bets settings, default is \&quot;whapi\&quot; which allows events set in far future to be included, setting the value to \&quot;en-GB\&quot; will activate english sportsbook settings, mirroring top bets on the website, which restricts events returned to those taking place in next 36 hours. Acceptable values (not all heve their own settings - if none currently available for that locale - en-GB will be used) are de-DE|whapi|en-GB|es-ES|fr-FR|nn-NO|fi-FI|ru-RU|pt-PT|hu-HU|sl-SL|ga-IE|en-CA|sr-Latn|sv-SE|el&#x3D;GR|zh-CHS|it-IT|zh-CHT|cs-CZ|de-AT|ja-JP|pl-PL|da-DK|ro-RO|nl-NL|tr-TR
    :type locale: str

    """
    return web.Response(status=200)
