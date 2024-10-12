from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def call_phone_number_auth_post(request: web.Request, body=None) -> web.Response:
    """Call phone number auth.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def check_for_update_get(request: web.Request, is_testflight=None) -> web.Response:
    """Clubhouse uses this to check for updates when app is not installed from App Store (eg TestFlight)

    

    :param is_testflight: 
    :type is_testflight: int

    """
    return web.Response(status=200)


async def check_waitlist_status_post(request: web.Request, ) -> web.Response:
    """checks waitlist status.

    


    """
    return web.Response(status=200)


async def complete_phone_number_auth_post(request: web.Request, body=None) -> web.Response:
    """Call phone number auth.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def create_channel_post(request: web.Request, body=None) -> web.Response:
    """creates a channel

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def follow_post(request: web.Request, body=None) -> web.Response:
    """follows a user

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_actionable_notifications_get(request: web.Request, ) -> web.Response:
    """get actionable notifications (the bell again)

    


    """
    return web.Response(status=200)


async def get_all_topics_get(request: web.Request, ) -> web.Response:
    """gets all topics.

    


    """
    return web.Response(status=200)


async def get_channels_get(request: web.Request, ) -> web.Response:
    """get all channels

    


    """
    return web.Response(status=200)


async def get_club_post(request: web.Request, body=None) -> web.Response:
    """gets club by id

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_clubs_for_topic_post(request: web.Request, body=None) -> web.Response:
    """looks up clubs by topic.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_create_channel_targets_post(request: web.Request, body=None) -> web.Response:
    """is fetched when you tap Create Room

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_events_get(request: web.Request, is_filtered=None, page_size=None, page=None) -> web.Response:
    """the Upcoming for You page

    

    :param is_filtered: 
    :type is_filtered: bool
    :param page_size: 
    :type page_size: int
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def get_following_post(request: web.Request, body=None) -> web.Response:
    """get a list of the users and clubs that this user is following. Returned users have bios truncated to ~80 characters.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_notifications_get(request: web.Request, page_size=None, page=None) -> web.Response:
    """get notifications (the bell icon)

    

    :param page_size: 
    :type page_size: int
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def get_online_friends_post(request: web.Request, body=None) -> web.Response:
    """gets online friends on the app homepage.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_profile_post(request: web.Request, body=None) -> web.Response:
    """looks up user profile by ID.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_release_notes_post(request: web.Request, ) -> web.Response:
    """gets release notes.

    


    """
    return web.Response(status=200)


async def get_settings_get(request: web.Request, ) -> web.Response:
    """get notification settings

    


    """
    return web.Response(status=200)


async def get_suggested_club_invites_post(request: web.Request, body=None) -> web.Response:
    """find users to invite to clubs based on phone number

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_suggested_follows_all_get(request: web.Request, in_onboarding=None, page_size=None, page=None) -> web.Response:
    """gets suggested follows during signup

    

    :param in_onboarding: 
    :type in_onboarding: bool
    :param page_size: 
    :type page_size: int
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def get_suggested_follows_friends_only_post(request: web.Request, body=None) -> web.Response:
    """find people to follow by uploading contacts during signup

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_suggested_follows_similar_post(request: web.Request, body=None) -> web.Response:
    """find similar users. (The Sparkles button on Clubhouse&#39;s profile page)

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_suggested_invites_post(request: web.Request, body=None) -> web.Response:
    """find users to invite based on phone number.

    (also see https://zerforschung.org/posts/clubhouse-telefonnummern-en/ for @zerforschung&#39;s analysis of the privacy implications of this API)

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_suggested_speakers_post(request: web.Request, body=None) -> web.Response:
    """gets suggested users when you start a private room

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_topic_post(request: web.Request, body=None) -> web.Response:
    """looks up topic by ID.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_users_for_topic_get(request: web.Request, topic_id=None, page_size=None, page=None) -> web.Response:
    """looks up users by topic.

    

    :param topic_id: 
    :type topic_id: int
    :param page_size: 
    :type page_size: int
    :param page: 
    :type page: int

    """
    return web.Response(status=200)


async def get_welcome_channel_get(request: web.Request, ) -> web.Response:
    """called during signup

    


    """
    return web.Response(status=200)


async def invite_from_waitlist_post(request: web.Request, body=None) -> web.Response:
    """wave to another user on the waitlist to give them access

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def invite_to_app_post(request: web.Request, body=None) -> web.Response:
    """invite a user to the app, using one of your invites

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def join_channel_post(request: web.Request, body=None) -> web.Response:
    """join a channel.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def leave_channel_post(request: web.Request, body=None) -> web.Response:
    """leave a channel.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def me_post(request: web.Request, body=None) -> web.Response:
    """gets user

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def record_action_trails_post(request: web.Request, body=None) -> web.Response:
    """analytics

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def refresh_token_post(request: web.Request, body=None) -> web.Response:
    """gets an access_token from a refresh_token.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def resend_phone_number_auth_post(request: web.Request, body=None) -> web.Response:
    """Resend phone number auth.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def search_clubs_post(request: web.Request, body=None) -> web.Response:
    """search clubs.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def search_users_post(request: web.Request, body=None) -> web.Response:
    """search for users

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def start_phone_number_auth_post(request: web.Request, body=None) -> web.Response:
    """Starts phone number auth.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def update_notifications_post(request: web.Request, body=None) -> web.Response:
    """updates notification during signup.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def update_username_post(request: web.Request, body=None) -> web.Response:
    """edits username.

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)
