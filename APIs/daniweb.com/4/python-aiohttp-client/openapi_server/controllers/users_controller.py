from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_users import EndpointGetUsers
from openapi_server.models.endpoint_get_users_id import EndpointGetUsersID
from openapi_server.models.endpoint_get_users_id_groups import EndpointGetUsersIDGroups
from openapi_server.models.endpoint_get_users_id_groups_messages import EndpointGetUsersIDGroupsMessages
from openapi_server.models.endpoint_get_users_id_metadata import EndpointGetUsersIDMetadata
from openapi_server.models.endpoint_get_users_id_metadata_collections import EndpointGetUsersIDMetadataCollections
from openapi_server.models.endpoint_get_users_id_positions import EndpointGetUsersIDPositions
from openapi_server.models.endpoint_get_users_id_synergies import EndpointGetUsersIDSynergies
from openapi_server.models.endpoint_get_users_nearby import EndpointGetUsersNearby
from openapi_server.models.endpoint_patch_users import EndpointPatchUsers
from openapi_server.models.endpoint_patch_users_id_synergies import EndpointPatchUsersIDSynergies
from openapi_server.models.endpoint_post_users_id_messages import EndpointPostUsersIDMessages
from openapi_server.models.endpoint_post_users_id_metadata import EndpointPostUsersIDMetadata
from openapi_server.models.endpoint_post_users_invites import EndpointPostUsersInvites
from openapi_server.models.endpoint_post_users_metadata_filters import EndpointPostUsersMetadataFilters
from openapi_server.models.endpoint_post_users_searches import EndpointPostUsersSearches
from openapi_server import util


async def users_get(request: web.Request, filter=None, order_by=None, bubbled=None, offset=None, limit=None) -> web.Response:
    """users_get

    Fetch an array of users that you&#39;ve been matched with, connected with, skipped, or muted. You can only retrieve users existing within the current access token&#39;s bubble. This report may be limited to the last ~500-1000 users you&#39;ve communicated with within the access token&#39;s bubble. Matches are always ordered by synergy, and the order_by parameter is ignored. You can only retrieve bubbled users when retrieving matches, and the bubbled parameter is ignored otherwise. Your 100 best algorithmic matches are based on: Complementary data submitted to Profiles, CVs, and Metadata; Complementary data acquired from third-parties; Location information; Many behavioral data points, such as how responsive users are to connections; Degrees of separation (mutual connections); etc. You may connect with 3 of these algorithmic matches per day for free. However, new members are allowed a grace period of additional daily matches. Each time you choose to meet or mute one of your algorithmic matches, a new match is introduced.

    :param filter: 
    :type filter: str
    :param order_by: 
    :type order_by: str
    :param bubbled: 
    :type bubbled: bool
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def users_get_0(request: web.Request, ) -> web.Response:
    """users_get_0

    Retrieve the currently OAuth&#39;ed end-user, based on the access token being used, including private information and settings such as their email address.


    """
    return web.Response(status=200)


async def users_id_groups_get(request: web.Request, id) -> web.Response:
    """users_id_groups_get

    You can only retrieve groups that were created by users existing within the current access token&#39;s bubble.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def users_id_groups_messages_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """users_id_groups_messages_get

    Paginated transcript of group messages authored by an individual user who exists within the current access token&#39;s bubble. Messages are sorted oldest to newest.

    :param id: 
    :type id: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def users_id_messages_post(request: web.Request, id, bubbled=None, metadata_0_key=None, metadata_0_privacy=None, metadata_0_values=None, metadata_1_key=None, metadata_1_privacy=None, metadata_1_values=None, metadata_2_key=None, metadata_2_privacy=None, metadata_2_values=None, text_emoticons=None, text_raw=None) -> web.Response:
    """users_id_messages_post

    Initiate a conversation with a user who exists within the current access token&#39;s bubble by sending them an introductory message. If you aren&#39;t already in a conversation with them, this endpoint meets them first, and then sends the message. Note that if you aren&#39;t in an existing conversation, you still must meet the criteria to meet them, meaning the user must currently be free for you to meet. You will receive an error message unless it is currently free for you to meet the user. You can use the users/{:IDS}/synergies endpoint to first determine if the user isn&#39;t already in a conversation with you and is free for you to meet and, if they aren&#39;t, how to pay to meet them. If you don&#39;t specify a message, it defaults to your custom introductory message defined in your settings.

    :param id: 
    :type id: int
    :param bubbled: 
    :type bubbled: bool
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_privacy: 
    :type metadata_0_privacy: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_privacy: 
    :type metadata_1_privacy: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_privacy: 
    :type metadata_2_privacy: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]
    :param text_emoticons: 
    :type text_emoticons: bool
    :param text_raw: 
    :type text_raw: str

    """
    return web.Response(status=200)


async def users_id_metadata_collections_get(request: web.Request, id) -> web.Response:
    """users_id_metadata_collections_get

    Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token&#39;s bubble based on preknown metadata key/value pairs. Metadata will be grouped by key.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def users_id_metadata_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """users_id_metadata_get

    Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token&#39;s bubble based on preknown metadata key/value pairs.

    :param id: 
    :type id: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def users_id_metadata_post(request: web.Request, id, metadata_0_key=None, metadata_0_privacy=None, metadata_0_values=None, metadata_1_key=None, metadata_1_privacy=None, metadata_1_values=None, metadata_2_key=None, metadata_2_privacy=None, metadata_2_values=None) -> web.Response:
    """users_id_metadata_post

    Attach one-to-many key/value pairs of metadata to a user, so long as the user exists within the current access token&#39;s bubble. You can set one key at a time, with one or many values. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user; Bubbled metadata by anyone using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user; Private metadata by you, so long as you are using an access token existing within the current bubble.

    :param id: 
    :type id: int
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_privacy: 
    :type metadata_0_privacy: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_privacy: 
    :type metadata_1_privacy: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_privacy: 
    :type metadata_2_privacy: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]

    """
    return web.Response(status=200)


async def users_id_positions_get(request: web.Request, id, bubbled=None) -> web.Response:
    """users_id_positions_get

    Retrieve the CV of a user who exists within the current access token&#39;s bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. You can only record CV data to your own account. However, any app that you have OAuth&#39;ed against can do so. By default, you will receive CV data that all apps have recorded for the user. Optionally, you can choose to only receive data that the current access token&#39;s bubble has recorded.

    :param id: 
    :type id: int
    :param bubbled: 
    :type bubbled: bool

    """
    return web.Response(status=200)


async def users_id_synergies_get(request: web.Request, id) -> web.Response:
    """users_id_synergies_get

    Determine your match relationship with one or more users who exist within the current access token&#39;s bubble. Under some conditions, the price to meet the user will be $0. However, if this is not the case, the PayPal URL payment method will be provided along with the price to meet the user. The PayPal API can be leveraged to send payments programatically, provided the parameters passed in remain the same to ensure that the payment is correctly recorded. Once the payment has been recorded via PayPal IPN, the price to meet the user changes to $0. You can then call the users/{:ID}/meet endpoint to meet the user.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def users_id_synergies_patch(request: web.Request, id, relationship_muted=None, relationship_skipped=None) -> web.Response:
    """users_id_synergies_patch

    Skip, mute or unmute a user you&#39;ve been matched with. Skipped matches are only presented as algorithmic matches after all other candidates have been exhausted. You cannot be matched with or meet muted users. You can only skip, mute or unmute users existing within the same bubble.

    :param id: 
    :type id: int
    :param relationship_muted: 
    :type relationship_muted: bool
    :param relationship_skipped: 
    :type relationship_skipped: bool

    """
    return web.Response(status=200)


async def users_idget(request: web.Request, id) -> web.Response:
    """users_idget

    Fetch an array of users. You can only retrieve users existing within the current access token&#39;s bubble.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)


async def users_invites_post(request: web.Request, csv=None, emails=None) -> web.Response:
    """users_invites_post

    Invite users to into your current access token&#39;s bubble by having Dazah send out email invitations on your behalf. The invitation sends users to begin the OAuth flow for the current application (based on the settings specified in the application&#39;s profile), and therefore they will be redirected to the application upon signing up / logging in. Upon doing so, if they aren&#39;t already, they will automatically be connected with you as well. If your current access token does not escape the bubble, the invitation will specify you wish to connect within the application&#39;s name. If your current access token escapes the bubble, the invitation will specify you wish to connect within Dazah. Submit either a list of emails, or a LinkedIn or Outlook CSV file. You can retrieve your LinkedIn CSV file by exporting your LinkedIn Connections at https://www.linkedin.com/people/export-settings. You can retrieve your Outlook CSV file by using the Outlook Import and Export Wizard. This endpoint buckets the invitations into four categories: Existing invites are existing users who are already connected with you within the current bubble, and are therefore not emailed; Discovered invites are existing Dazah users who are available to be connected with within the current bubble, and are therefore not emailed. Now that they have been discovered, the users/{:ID}/meet API endpoint may be used to connect with them; Invalid invites are existing Dazah users who are unavailable to be connected with, because they have deactivated accounts, are muting you, etc., and are therefore not emailed; Emailed invites are queued to receive an invitation within approximately 1 hour. Note that if you are attempting to invite an existing Dazah user who does not currently exist within your current access token&#39;s bubble, they will fall within the Discovered bucket if your current access token escapes the bubble, but will be emailed an invitation to join the application if your current access token does not escape the bubble.

    :param csv: 
    :type csv: str
    :param emails: 
    :type emails: List[str]

    """
    return web.Response(status=200)


async def users_metadata_filters_post(request: web.Request, limit=None, metadata_0_key=None, metadata_0_values=None, metadata_1_key=None, metadata_1_values=None, metadata_2_key=None, metadata_2_values=None, offset=None) -> web.Response:
    """users_metadata_filters_post

    Paginated listing of users filtered by arbitrary metadata criteria. Users must match on all key/value pairs passed in. Users may only match on one value of an array passed in. However, users are sorted based on how many distinct values they match on (most matches first).

    :param limit: 
    :type limit: int
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_values: 
    :type metadata_0_values: List[str]
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_values: 
    :type metadata_1_values: List[str]
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_values: 
    :type metadata_2_values: List[str]
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def users_nearby_get(request: web.Request, latitude=None, longitude=None, offset=None, limit=None) -> web.Response:
    """users_nearby_get

    Fetch an array of users that are geographically close to a set of coordinates. You can only retrieve users existing within the current access token&#39;s bubble.

    :param latitude: 
    :type latitude: float
    :param longitude: 
    :type longitude: float
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def users_patch(request: web.Request, company=None, company_size=None, first_name=None, goals=None, headline=None, industry=None, introduction=None, job_position=None, last_name=None, location_importance=None, match_tags=None, pitch=None, tags=None, targeted_industry=None, url=None) -> web.Response:
    """users_patch

    Update the OAuth&#39;ed end user&#39;s account profile. At this time, for anti-spam reasons, restrictions preclude the ability to update email address and some other settings via the API.

    :param company: 
    :type company: str
    :param company_size: 
    :type company_size: str
    :param first_name: 
    :type first_name: str
    :param goals: 
    :type goals: List[str]
    :param headline: 
    :type headline: str
    :param industry: 
    :type industry: str
    :param introduction: 
    :type introduction: str
    :param job_position: 
    :type job_position: str
    :param last_name: 
    :type last_name: str
    :param location_importance: 
    :type location_importance: str
    :param match_tags: 
    :type match_tags: List[str]
    :param pitch: 
    :type pitch: str
    :param tags: 
    :type tags: List[str]
    :param targeted_industry: 
    :type targeted_industry: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def users_searches_post(request: web.Request, active_within_x_days=None, audience_ids=None, bubbled=None, exclude_connections=None, exclude_matches=None, exclude_muted=None, exclude_skipped=None, geo_latitude=None, geo_longitude=None, geo_miles_away=None, group_id=None, limit=None, location_city_query=None, location_city_weight=None, location_country_query=None, location_country_weight=None, location_region_query=None, location_region_weight=None, metadata_0_key=None, metadata_0_query=None, metadata_0_weight=None, metadata_1_key=None, metadata_1_query=None, metadata_1_weight=None, metadata_2_key=None, metadata_2_query=None, metadata_2_weight=None, offset=None, position_organization_query=None, position_organization_weight=None, position_role_query=None, position_role_weight=None, position_summary_query=None, position_summary_weight=None, profile_first_name_query=None, profile_first_name_weight=None, profile_goals_query=None, profile_goals_weight=None, profile_headline_query=None, profile_headline_weight=None, profile_industry_query=None, profile_industry_weight=None, profile_last_name_query=None, profile_last_name_weight=None, profile_pitch_query=None, profile_pitch_weight=None) -> web.Response:
    """users_searches_post

    Filter and perform a weighted search against user profile fields, CV fields, and metadata by specifying a string to search on for each individual field. By default, results are filtered such that all words in the string must exist, unless you seprate the words with OR. To perform a weighted search (as opposed to filtering), specify the weight (from 0-100) the search algorithm should assign to the field. You can optionally exclude users who you are already in or not in conversations with, exclude users who you previously skipped, or exclude users who you are muting. By doing so, you can effectively customize your own matching algorithm. You can specify geo coordinates to only find users a certain distance away from a specific location, or only find users within a certain distance from the OAuth&#39;ed end-user&#39;s last known location. If your app utilizes multiple audience segments, you can specify which audiences you would like to search. You can also limit users to just those who have been recently active. You can also choose to only receive users originating from the current access token&#39;s bubble. Only users existing within the current access token&#39;s bubble will be matched, and you can only search within a group created by a bubbled user.

    :param active_within_x_days: 
    :type active_within_x_days: int
    :param audience_ids: 
    :type audience_ids: List[int]
    :param bubbled: 
    :type bubbled: bool
    :param exclude_connections: 
    :type exclude_connections: bool
    :param exclude_matches: 
    :type exclude_matches: bool
    :param exclude_muted: 
    :type exclude_muted: bool
    :param exclude_skipped: 
    :type exclude_skipped: bool
    :param geo_latitude: 
    :type geo_latitude: float
    :param geo_longitude: 
    :type geo_longitude: float
    :param geo_miles_away: 
    :type geo_miles_away: float
    :param group_id: 
    :type group_id: int
    :param limit: 
    :type limit: int
    :param location_city_query: 
    :type location_city_query: str
    :param location_city_weight: 
    :type location_city_weight: int
    :param location_country_query: 
    :type location_country_query: str
    :param location_country_weight: 
    :type location_country_weight: int
    :param location_region_query: 
    :type location_region_query: str
    :param location_region_weight: 
    :type location_region_weight: int
    :param metadata_0_key: 
    :type metadata_0_key: str
    :param metadata_0_query: 
    :type metadata_0_query: str
    :param metadata_0_weight: 
    :type metadata_0_weight: int
    :param metadata_1_key: 
    :type metadata_1_key: str
    :param metadata_1_query: 
    :type metadata_1_query: str
    :param metadata_1_weight: 
    :type metadata_1_weight: int
    :param metadata_2_key: 
    :type metadata_2_key: str
    :param metadata_2_query: 
    :type metadata_2_query: str
    :param metadata_2_weight: 
    :type metadata_2_weight: int
    :param offset: 
    :type offset: int
    :param position_organization_query: 
    :type position_organization_query: str
    :param position_organization_weight: 
    :type position_organization_weight: int
    :param position_role_query: 
    :type position_role_query: str
    :param position_role_weight: 
    :type position_role_weight: int
    :param position_summary_query: 
    :type position_summary_query: str
    :param position_summary_weight: 
    :type position_summary_weight: int
    :param profile_first_name_query: 
    :type profile_first_name_query: str
    :param profile_first_name_weight: 
    :type profile_first_name_weight: int
    :param profile_goals_query: 
    :type profile_goals_query: str
    :param profile_goals_weight: 
    :type profile_goals_weight: str
    :param profile_headline_query: 
    :type profile_headline_query: str
    :param profile_headline_weight: 
    :type profile_headline_weight: int
    :param profile_industry_query: 
    :type profile_industry_query: str
    :param profile_industry_weight: 
    :type profile_industry_weight: int
    :param profile_last_name_query: 
    :type profile_last_name_query: str
    :param profile_last_name_weight: 
    :type profile_last_name_weight: int
    :param profile_pitch_query: 
    :type profile_pitch_query: str
    :param profile_pitch_weight: 
    :type profile_pitch_weight: int

    """
    return web.Response(status=200)
