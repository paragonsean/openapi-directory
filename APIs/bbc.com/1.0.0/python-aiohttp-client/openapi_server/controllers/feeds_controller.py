from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.nitro import Nitro
from openapi_server import util


async def list_availability(request: web.Request, sort=None, sort_direction=None, availability=None, descendants_of=None, media_set=None, page=None, page_size=None, territory=None, debug=None) -> web.Response:
    """Discover details of on-demand availability for programmes and their versions

    Discover details of on-demand availability for programmes and their versions

    :param sort: Sorts: * scheduled_start: sort chronologically by scheduled start time/date, ascending 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param availability: filter for subset of availabilities
    :type availability: List[str]
    :param descendants_of: filter for subset of availabilities that have PID as ancestor
    :type descendants_of: List[str]
    :param media_set: filter for subset of availabilities with media set
    :type media_set: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param territory: filter for availabilities in given territory
    :type territory: List[str]
    :param debug: Turn on debug information (undocumented)
    :type debug: bool

    """
    return web.Response(status=200)


async def list_broadcasts(request: web.Request, sort=None, sort_direction=None, mixin=None, authority=None, descendants_of=None, end_from=None, end_to=None, format=None, genre=None, id=None, item=None, page=None, page_size=None, people=None, pid=None, q=None, schedule_day=None, schedule_day_from=None, schedule_day_to=None, service_master_brand=None, sid=None, start_from=None, start_to=None, version=None) -> web.Response:
    """Build schedules and find metadata for TV and radio broadcasts

    Fetch metadata about linear Broadcasts and Services, allowing the generation of Television and Radio schedules and other datasets for broadcast items. Use /schedules instead of this feed as it is more efficient. Broadcasts will be deprecated in the future.

    :param sort: Sorts: * start_date: sort chronologically by scheduled start time/date, ascending 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param mixin: Mixins: * titles: return ancestor programme titles 
    :type mixin: List[str]
    :param authority: filter for subset of broadcasts that have given authority
    :type authority: List[str]
    :param descendants_of: filter for subset of broadcasts that are descendants of the given programme PID
    :type descendants_of: List[str]
    :param end_from: filter for subset of broadcasts that end on or later than the specified datetime
    :type end_from: str
    :param end_to: filter for subset of broadcasts that end on or earlier than the specified datetime
    :type end_to: str
    :param format: filter for subset of broadcasts that are classified in the given format ID
    :type format: List[str]
    :param genre: filter for subset of broadcasts that are classified in the given genre ID
    :type genre: List[str]
    :param id: filter for subset of broadcasts that have given identifier
    :type id: List[str]
    :param item: filter for subset of broadcasts with the given item performed on it
    :type item: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param people: filter for subset of broadcasts that have given contributor
    :type people: str
    :param pid: filter for subset of broadcasts having given PID
    :type pid: List[str]
    :param q: filter for subset of broadcasts matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param schedule_day: filter for subset of broadcasts that start on the specified day (BBC time)
    :type schedule_day: str
    :param schedule_day_from: filter for subset of broadcasts that start on or after the specified day (BBC time)
    :type schedule_day_from: str
    :param schedule_day_to: filter for subset of broadcasts that start on or before the specified day (BBC time)
    :type schedule_day_to: str
    :param service_master_brand: filter for subset of broadcasts with given service master brand
    :type service_master_brand: List[str]
    :param sid: filter for subset of broadcasts that are on the specified linear service
    :type sid: List[str]
    :param start_from: filter for subset of broadcasts that start on or later than the specified datetime
    :type start_from: str
    :param start_to: filter for subset of broadcasts that start on or earlier than the specified datetime
    :type start_to: str
    :param version: filter for subset of broadcasts with given PID as their parent version
    :type version: List[str]

    """
    end_from = util.deserialize_datetime(end_from)
    end_to = util.deserialize_datetime(end_to)
    schedule_day = util.deserialize_date(schedule_day)
    schedule_day_from = util.deserialize_date(schedule_day_from)
    schedule_day_to = util.deserialize_date(schedule_day_to)
    start_from = util.deserialize_datetime(start_from)
    start_to = util.deserialize_datetime(start_to)
    return web.Response(status=200)


async def list_groups(request: web.Request, sort=None, sort_direction=None, mixin=None, for_descendants_of=None, for_programme=None, group=None, group_type=None, member=None, page=None, page_size=None, partner_id=None, partner_pid=None, pid=None, q=None, embargoed=None) -> web.Response:
    """Find metadata for curated groups: seasons, collections, galleries or franchises

    Long-lived curated collections of programmes and more, including Collections, Seasons, Franchises and Galleries

    :param sort: Sorts: * pid: sort alphabetically by PID 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param mixin: Mixins: * alternate_images: mixin to return the alternate images for a group * group_for: mixin to return links to programme entities that group belongs to * images: mixin to add image information for a group * related_links: mixin to return related links for the group 
    :type mixin: List[str]
    :param for_descendants_of: filter for groups related to given programme or its descendants
    :type for_descendants_of: str
    :param for_programme: filter for subset of groups directly related to a given programme
    :type for_programme: str
    :param group: filter for subset of groups which belong to the given group pid
    :type group: str
    :param group_type: filter for subset of groups that have the given group type
    :type group_type: List[str]
    :param member: filter for subset of groups which contain an entity with the given pid as a member
    :type member: str
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for groups by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for groups by partner PID
    :type partner_pid: List[str]
    :param pid: filter for subset of seasons, collections, galleries or franchises having given PID
    :type pid: List[str]
    :param q: filter for subset of groups matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param embargoed: Control return of embargoed items (undocumented)
    :type embargoed: str

    """
    return web.Response(status=200)


async def list_images(request: web.Request, sort=None, sort_direction=None, group=None, image_type=None, is_alternate_image_for=None, is_image_for=None, page=None, page_size=None, partner_id=None, partner_pid=None, pid=None, q=None, embargoed=None) -> web.Response:
    """Find metadata for images

    Find metadata for images, particularly those in galleries

    :param sort: Sorts: * group_position: sort numerically by position, ascending only * pid: sort alphabetically by PID 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param group: filter for images belonging to the given group (i.e. Gallery)
    :type group: str
    :param image_type: filter for images by type
    :type image_type: List[str]
    :param is_alternate_image_for: filter for alternate images by entity PID
    :type is_alternate_image_for: str
    :param is_image_for: filter for images by entity PID
    :type is_image_for: str
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for images by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for images by partner PID
    :type partner_pid: List[str]
    :param pid: filter for subset of images having given PID
    :type pid: List[str]
    :param q: filter for subset of images matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param embargoed: Control return of embargoed items (undocumented)
    :type embargoed: str

    """
    return web.Response(status=200)


async def list_items(request: web.Request, sort=None, sort_direction=None, mixin=None, authority=None, id=None, id_type=None, item_type=None, page=None, page_size=None, partner_id=None, partner_pid=None, people=None, pid=None, programme=None, q=None, segment_event=None) -> web.Response:
    """Look inside programmes to find segments: chapters, tracks and more

    Look inside programmes to find segments: chapters, tracks and more

    :param sort: Sorts: * pid: sort by pid, descending 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param mixin: Mixins: * contributions: mixin to return information about contributors to items * images: mixin to add image information for an item * offset: mixin to return programme segment offsets, works in conjunction with programme filter * play_event: mixin to return programme segment events, works in conjunction with programme or segment_event filters 
    :type mixin: List[str]
    :param authority: filter for subset of items that have an ID issued by the given authority
    :type authority: str
    :param id: filter for subset of items having given ID
    :type id: List[str]
    :param id_type: filter for subset of items that have given an ID of the given type
    :type id_type: str
    :param item_type: filter for specific type(s) of items
    :type item_type: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for items by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for items by partner PID
    :type partner_pid: List[str]
    :param people: filter for subset of items that have specified person involved
    :type people: str
    :param pid: filter for subset of items matching one of the given PIDs
    :type pid: List[str]
    :param programme: filter for subset of items that are part of the given programme
    :type programme: str
    :param q: filter for subset of items matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param segment_event: filter for item with the given segment_event
    :type segment_event: str

    """
    return web.Response(status=200)


async def list_masterbrands(request: web.Request, sort=None, sort_direction=None, mixin=None, mid=None, page=None, page_size=None, partner_id=None, partner_pid=None, q=None) -> web.Response:
    """List all Master Brands

    List all Master Brands

    :param sort: Sorts: * mid: sort by mid, ascending 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param mixin: Mixins: * images: mixin to add image information for a masterbrand 
    :type mixin: List[str]
    :param mid: filter for subset of masterbrands that have given identifier
    :type mid: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for masterbrands by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for masterbrands by partner PID
    :type partner_pid: List[str]
    :param q: filter for subset of masterbrands matching supplied keyword/phrase (boolean operators permitted)
    :type q: str

    """
    return web.Response(status=200)


async def list_people(request: web.Request, authority=None, has_external_id=None, id=None, id_type=None, page=None, page_size=None, partner_id=None, partner_pid=None, pid=None, programme=None, q=None) -> web.Response:
    """Find the people behind and in programmes: cast, crew, guests and more

    The People feed allows you to search for the people and groups that contribute to programmes. This is the starting point for cast and crew credits, as well as finding contributors using external IDs (such as Wikipedia URLs)

    :param authority: filter for subset of people that have an ID issued by the given authority
    :type authority: str
    :param has_external_id: filter for people who have an external identifier
    :type has_external_id: List[str]
    :param id: filter for subset of people having given ID
    :type id: List[str]
    :param id_type: filter for subset of people that have given an ID of the given type
    :type id_type: str
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for people by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for people by partner PID
    :type partner_pid: List[str]
    :param pid: filter for subset of people having given PID
    :type pid: List[str]
    :param programme: filter for subset of people that have contributed to the given programme pid
    :type programme: str
    :param q: filter for subset of people matching supplied keyword/phrase (boolean operators permitted)
    :type q: str

    """
    return web.Response(status=200)


async def list_pips(request: web.Request, page=None, page_size=None, q=None) -> web.Response:
    """Look inside pips entities

    Look inside pips entities

    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param q: filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted)
    :type q: str

    """
    return web.Response(status=200)


async def list_programme_details(request: web.Request, page=None, page_size=None, partner_pid=None, pid=None) -> web.Response:
    """Exposes programme information for a single pid

    Exposes programme information for a single pid

    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_pid: Filter for programme information by partner PID
    :type partner_pid: str
    :param pid: Filter for programme information for the provided PID
    :type pid: str

    """
    return web.Response(status=200)


async def list_programmes(request: web.Request, sort=None, sort_direction=None, mixin=None, audio_described=None, availability=None, availability_entity_type=None, availability_from=None, availability_type=None, children_of=None, descendants_of=None, duration=None, entity_type=None, format=None, genre=None, group=None, initial_letter=None, initial_letter_end=None, initial_letter_start=None, initial_letter_strict=None, item=None, master_brand=None, media_set=None, media_type=None, page=None, page_size=None, partner_id=None, partner_pid=None, payment_type=None, people=None, pid=None, promoted_for=None, q=None, signed=None, tag_name=None, tag_scheme=None, tleo=None, version=None, embargoed=None) -> web.Response:
    """Start here for programmes metadata: Brands, Series, Episodes and Clips

    Fetch metadata about Programmes (brands, series, episodes, clips). By applying different filter restrictions this feed can be used in many ways, for example to retrieve all series belonging to a brand, all the episodes and/or clips for a specific series, or any TLEO objects for a masterbrand. Other filters permit restricting to specific formats and/or genres, and you can request specific versions (for example Signed or Audio-Described). Parameters may be combined in any way suitable for your application.

    :param sort: Sorts: * group_position: sort numerically by position in group, ascending * pid: sort alphabetically by PID, descending * position: sort numerically by position, ascending * promotion: sort by promotion rank, ascending * release_date: sort chronologically by release date, descending * relevance: sort by weighting of search term (use with q parameter) * scheduled_start: sort chronologically by scheduled start time/date, ascending * strict_title: sort alphabetically by title, ascending * title: sort by title librarian style (ignoring leading &#39;The&#39;, &#39;A&#39;, etc), ascending * tree: sort by root pid and then preorder tree sort. Requires entities to have release date. 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param mixin: Mixins: * alternate_images: mixin to return the alternate images for a programme * ancestor_titles: mixin to return ancestor programme titles * availability: mixin to return programme availability information * available_simulcasts: mixin to return information about programmes that are currently available as simulcasts * available_versions: mixin to return information about programmes that are currently available on demand * available_webcasts: mixin to return information about programmes that are currently available as webcasts * contributions: mixin to return information about contributors to a programme * duration: mixin to return original version duration in programme concept entities * genre_groupings: mixin to return list of genre groupings * genre_groups: mixin to return list of genre groups * images: mixin to add image information for a programme * is_embeddable: mixin to add embeddable information for a programme * previous_next: mixin to return the programmes which appear before and after a programme (as determined by the sort applied in the request) * programme_type: mixin to return the programme type * related_links: mixin to return information about related links to a programme * titles: mixin to return ancestor programme titles * versions_availability: mixin to return information about programmes that are currently available 
    :type mixin: List[str]
    :param audio_described: filter for subset of programmes that are audio-described
    :type audio_described: List[str]
    :param availability: filter for subset of programmes that have availability
    :type availability: List[str]
    :param availability_entity_type: additional filter when availability&#x3D;available
    :type availability_entity_type: List[str]
    :param availability_from: filter for subset of programmes that are available after or at the specified datetime
    :type availability_from: str
    :param availability_type: filter for a subset of programmes that are available for a given type
    :type availability_type: List[str]
    :param children_of: filter for subset of programmes that have PID as immediate parent
    :type children_of: List[str]
    :param descendants_of: filter for subset of programmes that have PID as ancestor
    :type descendants_of: List[str]
    :param duration: filter for subset of programmes that have given duration
    :type duration: List[str]
    :param entity_type: filter for subset of programmes that have given entity type
    :type entity_type: List[str]
    :param format: filter for subset of programmes with format
    :type format: List[str]
    :param genre: filter for subset of programmes with genre
    :type genre: List[str]
    :param group: filter for subset of programmes which belong to the given group pid
    :type group: str
    :param initial_letter: filter for subset of programmes with title beginning with initial letter librarian style (ignoring leading &#39;The&#39;, &#39;An&#39; (Welsh), etc) 0-9 a-z
    :type initial_letter: str
    :param initial_letter_end: Programmes with (librarian) titles whose initial letter is equal/before given letter. Use with initial_letter_start for a range
    :type initial_letter_end: str
    :param initial_letter_start: Programmes with (librarian) titles whose initial letter is equal/after given letter. Use with initial_letter_end for range.
    :type initial_letter_start: str
    :param initial_letter_strict: filter for subset of programmes with title beginning with initial letter
    :type initial_letter_strict: List[str]
    :param item: filter for subset of programmes with linked to versions which have the given item pids
    :type item: List[str]
    :param master_brand: filter for subset of programmes with master_brand
    :type master_brand: List[str]
    :param media_set: filter for subset of programmes with media set
    :type media_set: str
    :param media_type: filter for subset of programmes with media type
    :type media_type: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for programmes by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for programmes by partner PID
    :type partner_pid: List[str]
    :param payment_type: filter for a subset of programmes that are of the given payment_type
    :type payment_type: List[str]
    :param people: filter for subset of programmes with contributions by given people PID
    :type people: str
    :param pid: filter for subset of programmes having given PID
    :type pid: List[str]
    :param promoted_for: filter for subset of programmes which are promoted for given service
    :type promoted_for: str
    :param q: filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param signed: filter for subset of programmes that are signed
    :type signed: List[str]
    :param tag_name: filter for subset of programmes with tag
    :type tag_name: str
    :param tag_scheme: filter for subset of programmes with a tag
    :type tag_scheme: str
    :param tleo: filter for subset of programmes that are TLEOs
    :type tleo: List[str]
    :param version: filter for subset of programmes with given PID as one of their versions
    :type version: List[str]
    :param embargoed: Control return of embargoed items (undocumented)
    :type embargoed: str

    """
    availability_from = util.deserialize_datetime(availability_from)
    return web.Response(status=200)


async def list_promotions(request: web.Request, mixin=None, context=None, page=None, page_size=None, partner_id=None, partner_pid=None, pid=None, promoted_by=None, promoted_for=None, q=None, status=None) -> web.Response:
    """Discover metadata for content promotions

    Details of short-term editorially curated \&quot;promotions\&quot;, for instance those programmes featured on iPlayer today

    :param mixin: Mixins: * related_links: mixin to return information about related links to a promotion 
    :type mixin: List[str]
    :param context: filter for subset of promotions belonging to a given context
    :type context: str
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for promotions by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for promotions by partner PID
    :type partner_pid: List[str]
    :param pid: filter for subset of promotions having given PID
    :type pid: List[str]
    :param promoted_by: filter for subset of promotions having given promoted by
    :type promoted_by: List[str]
    :param promoted_for: filter for subset of promotions having given promoted for
    :type promoted_for: List[str]
    :param q: filter for subset of promotions matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param status: filter for subset of promotions with status
    :type status: List[str]

    """
    return web.Response(status=200)


async def list_schedules(request: web.Request, sort=None, sort_direction=None, mixin=None, authority=None, descendants_of=None, end_from=None, end_to=None, format=None, genre=None, group=None, id=None, id_type=None, item=None, page=None, page_size=None, partner_id=None, partner_pid=None, people=None, pid=None, q=None, repeat=None, schedule_day=None, schedule_day_from=None, schedule_day_to=None, service_master_brand=None, sid=None, start_from=None, start_to=None, version=None) -> web.Response:
    """Build schedules and find metadata for TV and radio broadcasts and webcasts

    Dates, Times, Schedules: when and where are programmes being shown?

    :param sort: Sorts: * start_date: sort chronologically by scheduled start time/date, ascending 
    :type sort: str
    :param sort_direction: Sort direction
    :type sort_direction: str
    :param mixin: Mixins: * ancestor_titles: return ancestor programme titles * images: mixin to add image information for broadcasts and webcasts * titles: return ancestor programme titles 
    :type mixin: List[str]
    :param authority: filter for subset of broadcasts and webcasts that have given authority
    :type authority: List[str]
    :param descendants_of: filter for subset of broadcasts and webcasts that are descendants of the given programme PID
    :type descendants_of: List[str]
    :param end_from: filter for subset of broadcasts and webcasts that end on or later than the specified datetime
    :type end_from: str
    :param end_to: filter for subset of broadcasts and webcasts that end on or earlier than the specified datetime
    :type end_to: str
    :param format: filter for subset of broadcasts and webcasts that are classified in the given format ID
    :type format: List[str]
    :param genre: filter for subset of broadcasts and webcasts that are classified in the given genre ID
    :type genre: List[str]
    :param group: filter for subset of broadcasts and webcasts that have programmes in the given group
    :type group: str
    :param id: filter for subset of broadcasts and webcasts that have given identifier
    :type id: List[str]
    :param id_type: filter for subset of broadcasts and webcasts that have given id type
    :type id_type: List[str]
    :param item: filter for subset of broadcasts and webcasts with the given item performed on it
    :type item: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for broadcasts and webcasts by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for broadcasts and webcasts by partner PID
    :type partner_pid: List[str]
    :param people: filter for subset of broadcasts and webcasts that have given contributor
    :type people: str
    :param pid: filter for subset of broadcasts and webcasts having given PID
    :type pid: List[str]
    :param q: filter for subset of broadcasts and webcasts matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param repeat: filter to show either only repeats or non-repeats
    :type repeat: bool
    :param schedule_day: filter for subset of broadcasts and webcasts that start on the specified day (BBC time)
    :type schedule_day: str
    :param schedule_day_from: filter for subset of broadcasts and webcasts that start on or after the specified day (BBC time)
    :type schedule_day_from: str
    :param schedule_day_to: filter for subset of broadcasts and webcasts that start on or before the specified day (BBC time)
    :type schedule_day_to: str
    :param service_master_brand: filter for subset of broadcasts and webcasts with given service master brand
    :type service_master_brand: List[str]
    :param sid: filter for subset of broadcasts and webcasts that are on the specified linear service
    :type sid: List[str]
    :param start_from: filter for subset of broadcasts and webcasts that start on or later than the specified datetime
    :type start_from: str
    :param start_to: filter for subset of broadcasts and webcasts that start on or earlier than the specified datetime
    :type start_to: str
    :param version: filter for subset of broadcasts and webcasts with given PID as their parent version
    :type version: List[str]

    """
    end_from = util.deserialize_datetime(end_from)
    end_to = util.deserialize_datetime(end_to)
    schedule_day = util.deserialize_date(schedule_day)
    schedule_day_from = util.deserialize_date(schedule_day_from)
    schedule_day_to = util.deserialize_date(schedule_day_to)
    start_from = util.deserialize_datetime(start_from)
    start_to = util.deserialize_datetime(start_to)
    return web.Response(status=200)


async def list_services(request: web.Request, end_from=None, end_to=None, mid=None, page=None, page_size=None, partner_id=None, partner_pid=None, q=None, service_type=None, sid=None, start_from=None, start_to=None) -> web.Response:
    """Information about the linear services used for broadcast transmissions

    The services feed exposes the linear broadcast \&quot;services\&quot; from PIPs. These are the actual services which broadcast programmes (eg bbc_one_oxford is the service for BBC One in Oxford).

    :param end_from: Return services that end on or later than the specified datetime
    :type end_from: str
    :param end_to: filter for subset of broadcasts that end on or earlier than the specified datetime
    :type end_to: str
    :param mid: filter for services by masterbrand MID
    :type mid: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for services by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for services by partner PID
    :type partner_pid: List[str]
    :param q: filter for subset of services matching supplied keyword/phrase (boolean operators permitted)
    :type q: str
    :param service_type: filter for specified type of linear services
    :type service_type: List[str]
    :param sid: filter for specified linear service
    :type sid: List[str]
    :param start_from: Return services that start on or later than the specified datetime
    :type start_from: str
    :param start_to: Return services that start earlier than the specified datetime
    :type start_to: str

    """
    end_from = util.deserialize_datetime(end_from)
    end_to = util.deserialize_datetime(end_to)
    start_from = util.deserialize_datetime(start_from)
    start_to = util.deserialize_datetime(start_to)
    return web.Response(status=200)


async def list_versions(request: web.Request, availability=None, descendants_of=None, media_set=None, page=None, page_size=None, partner_id=None, partner_pid=None, payment_type=None, pid=None, embargoed=None) -> web.Response:
    """Metadata on editorial programme versions: original, signed, audio-described, etc

    The versions feed exposes editorial \&quot;Versions\&quot; of programmes. These are concepts used to capture different presentations of an overall programme: for example, versions of a programme may include one with sign language, one with audio description, one edited for content and more. Versions are also important to understand for broadcasts: a linear broadcast or an ondemand is always of a specific version, not merely of a programme.

    :param availability: filter for subset of versions that have availability
    :type availability: List[str]
    :param descendants_of: filter for subset of versions having given programme PID
    :type descendants_of: List[str]
    :param media_set: filter for subset of versions with availability in the given media set
    :type media_set: List[str]
    :param page: which page of results to return
    :type page: int
    :param page_size: number of results in each page
    :type page_size: int
    :param partner_id: filter for versions by partner ID
    :type partner_id: List[str]
    :param partner_pid: filter for versions by partner PID
    :type partner_pid: List[str]
    :param payment_type: filter for a subset of versions that are of the given payment_type
    :type payment_type: List[str]
    :param pid: filter for subset of versions having given PID
    :type pid: List[str]
    :param embargoed: Control return of embargoed items (undocumented)
    :type embargoed: str

    """
    return web.Response(status=200)
