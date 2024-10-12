# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto import BaseItemDto
from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.channel_mapping_options_dto import ChannelMappingOptionsDto
from openapi_server.models.channel_type import ChannelType
from openapi_server.models.get_programs_dto import GetProgramsDto
from openapi_server.models.guide_info import GuideInfo
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.listings_provider_info import ListingsProviderInfo
from openapi_server.models.live_tv_info import LiveTvInfo
from openapi_server.models.name_id_pair import NameIdPair
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.recording_status import RecordingStatus
from openapi_server.models.series_timer_info_dto import SeriesTimerInfoDto
from openapi_server.models.series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult
from openapi_server.models.set_channel_mapping_dto import SetChannelMappingDto
from openapi_server.models.sort_order import SortOrder
from openapi_server.models.timer_info_dto import TimerInfoDto
from openapi_server.models.timer_info_dto_query_result import TimerInfoDtoQueryResult
from openapi_server.models.tuner_channel_mapping import TunerChannelMapping
from openapi_server.models.tuner_host_info import TunerHostInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_listing_provider(client):
    """Test case for add_listing_provider

    Adds a listings provider.
    """
    body = {"Path":"Path","NewsCategories":["NewsCategories","NewsCategories"],"ZipCode":"ZipCode","ChannelMappings":[{"Value":"Value","Name":"Name"},{"Value":"Value","Name":"Name"}],"ListingsId":"ListingsId","EnableAllTuners":True,"EnabledTuners":["EnabledTuners","EnabledTuners"],"MovieCategories":["MovieCategories","MovieCategories"],"Type":"Type","MoviePrefix":"MoviePrefix","Username":"Username","KidsCategories":["KidsCategories","KidsCategories"],"UserAgent":"UserAgent","Country":"Country","PreferredLanguage":"PreferredLanguage","SportsCategories":["SportsCategories","SportsCategories"],"Id":"Id","Password":"Password"}
    params = [('pw', 'pw_example'),
                    ('validateListings', False),
                    ('validateLogin', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/ListingProviders',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_tuner_host(client):
    """Test case for add_tuner_host

    Adds a tuner host.
    """
    body = {"AllowHWTranscoding":True,"Type":"Type","EnableStreamLooping":True,"FriendlyName":"FriendlyName","DeviceId":"DeviceId","TunerCount":0,"ImportFavoritesOnly":True,"UserAgent":"UserAgent","Id":"Id","Source":"Source","Url":"Url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/TunerHosts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_series_timer(client):
    """Test case for cancel_series_timer

    Cancels a live tv series timer.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/LiveTv/SeriesTimers/{timer_id}'.format(timer_id='timer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_timer(client):
    """Test case for cancel_timer

    Cancels a live tv timer.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/LiveTv/Timers/{timer_id}'.format(timer_id='timer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_series_timer(client):
    """Test case for create_series_timer

    Creates a live tv series timer.
    """
    body = {"KeepUntil":"UntilDeleted","PrePaddingSeconds":1,"KeepUpTo":0,"SkipEpisodesInLibrary":True,"RecordNewOnly":True,"RecordAnyChannel":True,"ParentThumbImageTag":"ParentThumbImageTag","ChannelId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ExternalProgramId":"ExternalProgramId","ChannelPrimaryImageTag":"ChannelPrimaryImageTag","Name":"Name","IsPostPaddingRequired":True,"StartDate":"2000-01-23T04:56:07.000+00:00","ParentBackdropItemId":"ParentBackdropItemId","ServerId":"ServerId","Days":["Sunday","Sunday"],"DayPattern":"Daily","ParentPrimaryImageTag":"ParentPrimaryImageTag","IsPrePaddingRequired":True,"Priority":5,"ExternalId":"ExternalId","RecordAnyTime":True,"ExternalChannelId":"ExternalChannelId","Overview":"Overview","PostPaddingSeconds":6,"ParentPrimaryImageItemId":"ParentPrimaryImageItemId","ProgramId":"ProgramId","EndDate":"2000-01-23T04:56:07.000+00:00","ImageTags":{"key":"ImageTags"},"ParentThumbItemId":"ParentThumbItemId","Type":"Type","ChannelName":"ChannelName","ParentBackdropImageTags":["ParentBackdropImageTags","ParentBackdropImageTags"],"ServiceName":"ServiceName","Id":"Id"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/SeriesTimers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_timer(client):
    """Test case for create_timer

    Creates a live tv timer.
    """
    body = {"KeepUntil":"UntilDeleted","PrePaddingSeconds":6,"RunTimeTicks":5,"ChannelId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ExternalProgramId":"ExternalProgramId","ChannelPrimaryImageTag":"ChannelPrimaryImageTag","Name":"Name","IsPostPaddingRequired":True,"StartDate":"2000-01-23T04:56:07.000+00:00","ProgramInfo":{"SeasonName":"SeasonName","PremiereDate":"2000-01-23T04:56:07.000+00:00","AirTime":"AirTime","CriticRating":7.386282,"Studios":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"Aperture":2.3021358869347655,"CameraMake":"CameraMake","ChannelPrimaryImageTag":"ChannelPrimaryImageTag","ExtraType":"ExtraType","ParentBackdropItemId":"ParentBackdropItemId","Etag":"Etag","ExposureTime":1.4894159098541704,"ParentLogoImageTag":"ParentLogoImageTag","IsoType":"Dvd","MediaType":"MediaType","Tags":["Tags","Tags"],"ImageBlurHashes":{"Art":{"key":"Art"},"Banner":{"key":"Banner"},"Thumb":{"key":"Thumb"},"BoxRear":{"key":"BoxRear"},"Chapter":{"key":"Chapter"},"Box":{"key":"Box"},"Profile":{"key":"Profile"},"Logo":{"key":"Logo"},"Disc":{"key":"Disc"},"Primary":{"key":"Primary"},"Screenshot":{"key":"Screenshot"},"Backdrop":{"key":"Backdrop"},"Menu":{"key":"Menu"}},"Status":"Status","IndexNumberEnd":4,"ArtistItems":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"MediaSources":[{"EncoderPath":"EncoderPath","RequiredHttpHeaders":{"key":"RequiredHttpHeaders"},"RunTimeTicks":7,"MediaStreams":[{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5},{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5}],"Size":3,"Video3DFormat":"HalfSideBySide","BufferMs":3,"Timestamp":"None","Name":"Name","RequiresOpening":True,"SupportsDirectStream":True,"VideoType":"VideoFile","RequiresClosing":True,"Container":"Container","LiveStreamId":"LiveStreamId","RequiresLooping":True,"DefaultSubtitleStreamIndex":1,"GenPtsInput":True,"IsInfiniteStream":True,"Path":"Path","IsRemote":True,"EncoderProtocol":"File","IgnoreIndex":True,"SupportsDirectPlay":True,"TranscodingSubProtocol":"TranscodingSubProtocol","AnalyzeDurationMs":9,"Formats":["Formats","Formats"],"Bitrate":6,"OpenToken":"OpenToken","SupportsProbing":True,"MediaAttachments":[{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"},{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"}],"Type":"Default","ReadAtNativeFramerate":True,"ETag":"ETag","TranscodingContainer":"TranscodingContainer","IgnoreDts":True,"TranscodingUrl":"TranscodingUrl","Id":"Id","SupportsTranscoding":True,"DefaultAudioStreamIndex":6},{"EncoderPath":"EncoderPath","RequiredHttpHeaders":{"key":"RequiredHttpHeaders"},"RunTimeTicks":7,"MediaStreams":[{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5},{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5}],"Size":3,"Video3DFormat":"HalfSideBySide","BufferMs":3,"Timestamp":"None","Name":"Name","RequiresOpening":True,"SupportsDirectStream":True,"VideoType":"VideoFile","RequiresClosing":True,"Container":"Container","LiveStreamId":"LiveStreamId","RequiresLooping":True,"DefaultSubtitleStreamIndex":1,"GenPtsInput":True,"IsInfiniteStream":True,"Path":"Path","IsRemote":True,"EncoderProtocol":"File","IgnoreIndex":True,"SupportsDirectPlay":True,"TranscodingSubProtocol":"TranscodingSubProtocol","AnalyzeDurationMs":9,"Formats":["Formats","Formats"],"Bitrate":6,"OpenToken":"OpenToken","SupportsProbing":True,"MediaAttachments":[{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"},{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"}],"Type":"Default","ReadAtNativeFramerate":True,"ETag":"ETag","TranscodingContainer":"TranscodingContainer","IgnoreDts":True,"TranscodingUrl":"TranscodingUrl","Id":"Id","SupportsTranscoding":True,"DefaultAudioStreamIndex":6}],"GenreItems":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"OfficialRating":"OfficialRating","ProgramCount":6,"ProgramId":"ProgramId","Longitude":6.683562403749608,"FocalLength":6.84685269835264,"LockData":True,"IsNews":True,"ShutterSpeed":7.260521264802104,"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","IsFolder":True,"SeriesTimerId":"SeriesTimerId","SeriesId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","MediaStreams":[{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5},{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5}],"IsPlaceHolder":True,"CanDownload":True,"IsMovie":True,"SeriesCount":4,"DateLastMediaAdded":"2000-01-23T04:56:07.000+00:00","ParentArtImageTag":"ParentArtImageTag","PlayAccess":"Full","SeriesStudio":"SeriesStudio","IsLive":True,"Width":8,"ExternalUrls":[{"Url":"Url","Name":"Name"},{"Url":"Url","Name":"Name"}],"RecursiveItemCount":4,"ParentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Path":"Path","MusicVideoCount":7,"ScreenshotImageTags":["ScreenshotImageTags","ScreenshotImageTags"],"EpisodeCount":1,"IsSeries":True,"ProductionLocations":["ProductionLocations","ProductionLocations"],"ParentPrimaryImageItemId":"ParentPrimaryImageItemId","EndDate":"2000-01-23T04:56:07.000+00:00","ParentThumbItemId":"ParentThumbItemId","SeriesPrimaryImageTag":"SeriesPrimaryImageTag","PreferredMetadataLanguage":"PreferredMetadataLanguage","Type":"Type","BackdropImageTags":["BackdropImageTags","BackdropImageTags"],"ParentBackdropImageTags":["ParentBackdropImageTags","ParentBackdropImageTags"],"AirsBeforeEpisodeNumber":6,"ChildCount":3,"Audio":"Mono","Artists":["Artists","Artists"],"ChannelType":"TV","RunTimeTicks":1,"AlbumPrimaryImageTag":"AlbumPrimaryImageTag","CumulativeRunTimeTicks":1,"SourceType":"SourceType","CanDelete":True,"Album":"Album","DisplayPreferencesId":"DisplayPreferencesId","PlaylistItemId":"PlaylistItemId","Latitude":9.965781217890562,"SortName":"SortName","ArtistCount":7,"Name":"Name","StartDate":"2000-01-23T04:56:07.000+00:00","Container":"Container","ProductionYear":0,"SeriesName":"SeriesName","ParentArtItemId":"ParentArtItemId","AlbumId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","LocalTrailerCount":9,"SupportsSync":True,"CompletionPercentage":4.145608029883936,"IndexNumber":1,"Genres":["Genres","Genres"],"LockedFields":["Cast","Cast"],"SeasonId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ParentPrimaryImageTag":"ParentPrimaryImageTag","ProviderIds":{"key":"ProviderIds"},"RemoteTrailers":[{"Url":"Url","Name":"Name"},{"Url":"Url","Name":"Name"}],"MediaSourceCount":8,"CustomRating":"CustomRating","AirsAfterSeasonNumber":0,"AirDays":["Sunday","Sunday"],"ParentLogoItemId":"ParentLogoItemId","PartCount":3,"ChannelName":"ChannelName","EpisodeTitle":"EpisodeTitle","IsoSpeedRating":5,"CommunityRating":2.027123,"Software":"Software","Chapters":[{"StartPositionTicks":9,"ImageTag":"ImageTag","ImageDateModified":"2000-01-23T04:56:07.000+00:00","ImagePath":"ImagePath","Name":"Name"},{"StartPositionTicks":9,"ImageTag":"ImageTag","ImageDateModified":"2000-01-23T04:56:07.000+00:00","ImagePath":"ImagePath","Name":"Name"}],"SongCount":9,"Taglines":["Taglines","Taglines"],"AirsBeforeSeasonNumber":1,"CameraModel":"CameraModel","PreferredMetadataCountryCode":"PreferredMetadataCountryCode","ChannelNumber":"ChannelNumber","UserData":{"Played":True,"UnplayedItemCount":6,"PlayedPercentage":5.507386964179881,"PlayCount":0,"Rating":4.86315908102884,"PlaybackPositionTicks":7,"LastPlayedDate":"2000-01-23T04:56:07.000+00:00","Likes":True,"IsFavorite":True,"ItemId":"ItemId","Key":"Key"},"TimerId":"TimerId","DateCreated":"2000-01-23T04:56:07.000+00:00","HasSubtitles":True,"ParentThumbImageTag":"ParentThumbImageTag","IsSports":True,"ChannelId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ParentIndexNumber":5,"AlbumArtists":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"ServerId":"ServerId","Number":"Number","AlbumCount":5,"IsRepeat":True,"CollectionType":"CollectionType","Height":7,"PrimaryImageAspectRatio":4.078845849666752,"IsKids":True,"DisplayOrder":"DisplayOrder","IsHD":True,"EnableMediaSourceDisplay":True,"SeriesThumbImageTag":"SeriesThumbImageTag","MovieCount":3,"People":[{"Role":"Role","Type":"Type","PrimaryImageTag":"PrimaryImageTag","Id":"Id","ImageBlurHashes":{"Art":{"key":"Art"},"Banner":{"key":"Banner"},"Thumb":{"key":"Thumb"},"BoxRear":{"key":"BoxRear"},"Chapter":{"key":"Chapter"},"Box":{"key":"Box"},"Profile":{"key":"Profile"},"Logo":{"key":"Logo"},"Disc":{"key":"Disc"},"Primary":{"key":"Primary"},"Screenshot":{"key":"Screenshot"},"Backdrop":{"key":"Backdrop"},"Menu":{"key":"Menu"}},"Name":"Name"},{"Role":"Role","Type":"Type","PrimaryImageTag":"PrimaryImageTag","Id":"Id","ImageBlurHashes":{"Art":{"key":"Art"},"Banner":{"key":"Banner"},"Thumb":{"key":"Thumb"},"BoxRear":{"key":"BoxRear"},"Chapter":{"key":"Chapter"},"Box":{"key":"Box"},"Profile":{"key":"Profile"},"Logo":{"key":"Logo"},"Disc":{"key":"Disc"},"Primary":{"key":"Primary"},"Screenshot":{"key":"Screenshot"},"Backdrop":{"key":"Backdrop"},"Menu":{"key":"Menu"}},"Name":"Name"}],"Overview":"Overview","SpecialFeatureCount":0,"ImageOrientation":"TopLeft","AlbumArtist":"AlbumArtist","ImageTags":{"key":"ImageTags"},"AspectRatio":"AspectRatio","TrailerCount":9,"OriginalTitle":"OriginalTitle","ForcedSortName":"ForcedSortName","IsPremiere":True,"LocationType":"FileSystem","Altitude":5.637376656633329},"ParentBackdropItemId":"ParentBackdropItemId","ServerId":"ServerId","Status":"New","IsPrePaddingRequired":True,"Priority":1,"ExternalId":"ExternalId","ExternalSeriesTimerId":"ExternalSeriesTimerId","ExternalChannelId":"ExternalChannelId","Overview":"Overview","PostPaddingSeconds":0,"ProgramId":"ProgramId","EndDate":"2000-01-23T04:56:07.000+00:00","Type":"Type","ChannelName":"ChannelName","ParentBackdropImageTags":["ParentBackdropImageTags","ParentBackdropImageTags"],"ServiceName":"ServiceName","Id":"Id","SeriesTimerId":"SeriesTimerId"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/Timers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_listing_provider(client):
    """Test case for delete_listing_provider

    Delete listing provider.
    """
    params = [('id', 'id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/LiveTv/ListingProviders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_recording(client):
    """Test case for delete_recording

    Deletes a live tv recording.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/LiveTv/Recordings/{recording_id}'.format(recording_id='recording_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tuner_host(client):
    """Test case for delete_tuner_host

    Deletes a tuner host.
    """
    params = [('id', 'id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/LiveTv/TunerHosts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discover_tuners(client):
    """Test case for discover_tuners

    Discover tuners.
    """
    params = [('newDevicesOnly', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Tuners/Discover',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discvover_tuners(client):
    """Test case for discvover_tuners

    Discover tuners.
    """
    params = [('newDevicesOnly', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Tuners/Discvover',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel(client):
    """Test case for get_channel

    Gets a live tv channel.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_mapping_options(client):
    """Test case for get_channel_mapping_options

    Get channel mapping options.
    """
    params = [('providerId', 'provider_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/ChannelMappingOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_listing_provider(client):
    """Test case for get_default_listing_provider

    Gets default listings provider info.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/ListingProviders/Default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_timer(client):
    """Test case for get_default_timer

    Gets the default values for a new timer.
    """
    params = [('programId', 'program_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Timers/Defaults',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_guide_info(client):
    """Test case for get_guide_info

    Get guid info.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/GuideInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lineups(client):
    """Test case for get_lineups

    Gets available lineups.
    """
    params = [('id', 'id_example'),
                    ('type', 'type_example'),
                    ('location', 'location_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/ListingProviders/Lineups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_recording_file(client):
    """Test case for get_live_recording_file

    Gets a live tv recording stream.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/LiveRecordings/{recording_id}/stream'.format(recording_id='recording_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_stream_file(client):
    """Test case for get_live_stream_file

    Gets a live tv channel stream.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/LiveStreamFiles/{stream_id}/stream.{container}'.format(stream_id='stream_id_example', container='container_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_tv_channels(client):
    """Test case for get_live_tv_channels

    Gets available live tv channels.
    """
    params = [('type', openapi_server.ChannelType()),
                    ('userId', 'user_id_example'),
                    ('startIndex', 56),
                    ('isMovie', True),
                    ('isSeries', True),
                    ('isNews', True),
                    ('isKids', True),
                    ('isSports', True),
                    ('limit', 56),
                    ('isFavorite', True),
                    ('isLiked', True),
                    ('isDisliked', True),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableUserData', True),
                    ('sortBy', ['sort_by_example']),
                    ('sortOrder', openapi_server.SortOrder()),
                    ('enableFavoriteSorting', False),
                    ('addCurrentProgram', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_tv_info(client):
    """Test case for get_live_tv_info

    Gets available live tv services.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_live_tv_programs(client):
    """Test case for get_live_tv_programs

    Gets available live tv epgs.
    """
    params = [('channelIds', ['channel_ids_example']),
                    ('userId', 'user_id_example'),
                    ('minStartDate', '2013-10-20T19:20:30+01:00'),
                    ('hasAired', True),
                    ('isAiring', True),
                    ('maxStartDate', '2013-10-20T19:20:30+01:00'),
                    ('minEndDate', '2013-10-20T19:20:30+01:00'),
                    ('maxEndDate', '2013-10-20T19:20:30+01:00'),
                    ('isMovie', True),
                    ('isSeries', True),
                    ('isNews', True),
                    ('isKids', True),
                    ('isSports', True),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('sortBy', 'sort_by_example'),
                    ('sortOrder', 'sort_order_example'),
                    ('genres', ['genres_example']),
                    ('genreIds', ['genre_ids_example']),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('enableUserData', True),
                    ('seriesTimerId', 'series_timer_id_example'),
                    ('librarySeriesId', 'library_series_id_example'),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableTotalRecordCount', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Programs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_program(client):
    """Test case for get_program

    Gets a live tv program.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Programs/{program_id}'.format(program_id='program_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_programs(client):
    """Test case for get_programs

    Gets available live tv epgs.
    """
    body = {"EnableUserData":True,"SortBy":"SortBy","EnableTotalRecordCount":True,"LibrarySeriesId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","IsAiring":True,"IsSports":True,"ImageTypeLimit":0,"MaxStartDate":"2000-01-23T04:56:07.000+00:00","EnableImageTypes":["Primary","Primary"],"IsMovie":True,"MinStartDate":"2000-01-23T04:56:07.000+00:00","MinEndDate":"2000-01-23T04:56:07.000+00:00","Genres":["Genres","Genres"],"HasAired":True,"IsKids":True,"StartIndex":1,"GenreIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"IsSeries":True,"SortOrder":"SortOrder","ChannelIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"Fields":["AirTime","AirTime"],"MaxEndDate":"2000-01-23T04:56:07.000+00:00","IsNews":True,"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","EnableImages":True,"Limit":6,"SeriesTimerId":"SeriesTimerId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/Programs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recommended_programs(client):
    """Test case for get_recommended_programs

    Gets recommended live tv epgs.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('isAiring', True),
                    ('hasAired', True),
                    ('isSeries', True),
                    ('isMovie', True),
                    ('isNews', True),
                    ('isKids', True),
                    ('isSports', True),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('genreIds', ['genre_ids_example']),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableUserData', True),
                    ('enableTotalRecordCount', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Programs/Recommended',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recording(client):
    """Test case for get_recording

    Gets a live tv recording.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Recordings/{recording_id}'.format(recording_id='recording_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recording_folders(client):
    """Test case for get_recording_folders

    Gets recording folders.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Recordings/Folders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recording_group(client):
    """Test case for get_recording_group

    Get recording group.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Recordings/Groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recording_groups(client):
    """Test case for get_recording_groups

    Gets live tv recording groups.
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Recordings/Groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recordings(client):
    """Test case for get_recordings

    Gets live tv recordings.
    """
    params = [('channelId', 'channel_id_example'),
                    ('userId', 'user_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('status', openapi_server.RecordingStatus()),
                    ('isInProgress', True),
                    ('seriesTimerId', 'series_timer_id_example'),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableUserData', True),
                    ('isMovie', True),
                    ('isSeries', True),
                    ('isKids', True),
                    ('isSports', True),
                    ('isNews', True),
                    ('isLibraryItem', True),
                    ('enableTotalRecordCount', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Recordings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recordings_series(client):
    """Test case for get_recordings_series

    Gets live tv recording series.
    """
    params = [('channelId', 'channel_id_example'),
                    ('userId', 'user_id_example'),
                    ('groupId', 'group_id_example'),
                    ('startIndex', 56),
                    ('limit', 56),
                    ('status', openapi_server.RecordingStatus()),
                    ('isInProgress', True),
                    ('seriesTimerId', 'series_timer_id_example'),
                    ('enableImages', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()]),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableUserData', True),
                    ('enableTotalRecordCount', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Recordings/Series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schedules_direct_countries(client):
    """Test case for get_schedules_direct_countries

    Gets available countries.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/ListingProviders/SchedulesDirect/Countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_timer(client):
    """Test case for get_series_timer

    Gets a live tv series timer.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/SeriesTimers/{timer_id}'.format(timer_id='timer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_series_timers(client):
    """Test case for get_series_timers

    Gets live tv series timers.
    """
    params = [('sortBy', 'sort_by_example'),
                    ('sortOrder', openapi_server.SortOrder())]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/SeriesTimers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_timer(client):
    """Test case for get_timer

    Gets a timer.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Timers/{timer_id}'.format(timer_id='timer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_timers(client):
    """Test case for get_timers

    Gets the live tv timers.
    """
    params = [('channelId', 'channel_id_example'),
                    ('seriesTimerId', 'series_timer_id_example'),
                    ('isActive', True),
                    ('isScheduled', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/Timers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tuner_host_types(client):
    """Test case for get_tuner_host_types

    Get tuner host types.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/LiveTv/TunerHosts/Types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_tuner(client):
    """Test case for reset_tuner

    Resets a tv tuner.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/Tuners/{tuner_id}/Reset'.format(tuner_id='tuner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_channel_mapping(client):
    """Test case for set_channel_mapping

    Set channel mappings.
    """
    body = {"ProviderId":"ProviderId","ProviderChannelId":"ProviderChannelId","TunerChannelId":"TunerChannelId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/ChannelMappings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_series_timer(client):
    """Test case for update_series_timer

    Updates a live tv series timer.
    """
    body = {"KeepUntil":"UntilDeleted","PrePaddingSeconds":1,"KeepUpTo":0,"SkipEpisodesInLibrary":True,"RecordNewOnly":True,"RecordAnyChannel":True,"ParentThumbImageTag":"ParentThumbImageTag","ChannelId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ExternalProgramId":"ExternalProgramId","ChannelPrimaryImageTag":"ChannelPrimaryImageTag","Name":"Name","IsPostPaddingRequired":True,"StartDate":"2000-01-23T04:56:07.000+00:00","ParentBackdropItemId":"ParentBackdropItemId","ServerId":"ServerId","Days":["Sunday","Sunday"],"DayPattern":"Daily","ParentPrimaryImageTag":"ParentPrimaryImageTag","IsPrePaddingRequired":True,"Priority":5,"ExternalId":"ExternalId","RecordAnyTime":True,"ExternalChannelId":"ExternalChannelId","Overview":"Overview","PostPaddingSeconds":6,"ParentPrimaryImageItemId":"ParentPrimaryImageItemId","ProgramId":"ProgramId","EndDate":"2000-01-23T04:56:07.000+00:00","ImageTags":{"key":"ImageTags"},"ParentThumbItemId":"ParentThumbItemId","Type":"Type","ChannelName":"ChannelName","ParentBackdropImageTags":["ParentBackdropImageTags","ParentBackdropImageTags"],"ServiceName":"ServiceName","Id":"Id"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/SeriesTimers/{timer_id}'.format(timer_id='timer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_timer(client):
    """Test case for update_timer

    Updates a live tv timer.
    """
    body = {"KeepUntil":"UntilDeleted","PrePaddingSeconds":6,"RunTimeTicks":5,"ChannelId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ExternalProgramId":"ExternalProgramId","ChannelPrimaryImageTag":"ChannelPrimaryImageTag","Name":"Name","IsPostPaddingRequired":True,"StartDate":"2000-01-23T04:56:07.000+00:00","ProgramInfo":{"SeasonName":"SeasonName","PremiereDate":"2000-01-23T04:56:07.000+00:00","AirTime":"AirTime","CriticRating":7.386282,"Studios":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"Aperture":2.3021358869347655,"CameraMake":"CameraMake","ChannelPrimaryImageTag":"ChannelPrimaryImageTag","ExtraType":"ExtraType","ParentBackdropItemId":"ParentBackdropItemId","Etag":"Etag","ExposureTime":1.4894159098541704,"ParentLogoImageTag":"ParentLogoImageTag","IsoType":"Dvd","MediaType":"MediaType","Tags":["Tags","Tags"],"ImageBlurHashes":{"Art":{"key":"Art"},"Banner":{"key":"Banner"},"Thumb":{"key":"Thumb"},"BoxRear":{"key":"BoxRear"},"Chapter":{"key":"Chapter"},"Box":{"key":"Box"},"Profile":{"key":"Profile"},"Logo":{"key":"Logo"},"Disc":{"key":"Disc"},"Primary":{"key":"Primary"},"Screenshot":{"key":"Screenshot"},"Backdrop":{"key":"Backdrop"},"Menu":{"key":"Menu"}},"Status":"Status","IndexNumberEnd":4,"ArtistItems":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"MediaSources":[{"EncoderPath":"EncoderPath","RequiredHttpHeaders":{"key":"RequiredHttpHeaders"},"RunTimeTicks":7,"MediaStreams":[{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5},{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5}],"Size":3,"Video3DFormat":"HalfSideBySide","BufferMs":3,"Timestamp":"None","Name":"Name","RequiresOpening":True,"SupportsDirectStream":True,"VideoType":"VideoFile","RequiresClosing":True,"Container":"Container","LiveStreamId":"LiveStreamId","RequiresLooping":True,"DefaultSubtitleStreamIndex":1,"GenPtsInput":True,"IsInfiniteStream":True,"Path":"Path","IsRemote":True,"EncoderProtocol":"File","IgnoreIndex":True,"SupportsDirectPlay":True,"TranscodingSubProtocol":"TranscodingSubProtocol","AnalyzeDurationMs":9,"Formats":["Formats","Formats"],"Bitrate":6,"OpenToken":"OpenToken","SupportsProbing":True,"MediaAttachments":[{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"},{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"}],"Type":"Default","ReadAtNativeFramerate":True,"ETag":"ETag","TranscodingContainer":"TranscodingContainer","IgnoreDts":True,"TranscodingUrl":"TranscodingUrl","Id":"Id","SupportsTranscoding":True,"DefaultAudioStreamIndex":6},{"EncoderPath":"EncoderPath","RequiredHttpHeaders":{"key":"RequiredHttpHeaders"},"RunTimeTicks":7,"MediaStreams":[{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5},{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5}],"Size":3,"Video3DFormat":"HalfSideBySide","BufferMs":3,"Timestamp":"None","Name":"Name","RequiresOpening":True,"SupportsDirectStream":True,"VideoType":"VideoFile","RequiresClosing":True,"Container":"Container","LiveStreamId":"LiveStreamId","RequiresLooping":True,"DefaultSubtitleStreamIndex":1,"GenPtsInput":True,"IsInfiniteStream":True,"Path":"Path","IsRemote":True,"EncoderProtocol":"File","IgnoreIndex":True,"SupportsDirectPlay":True,"TranscodingSubProtocol":"TranscodingSubProtocol","AnalyzeDurationMs":9,"Formats":["Formats","Formats"],"Bitrate":6,"OpenToken":"OpenToken","SupportsProbing":True,"MediaAttachments":[{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"},{"CodecTag":"CodecTag","Comment":"Comment","DeliveryUrl":"DeliveryUrl","Codec":"Codec","FileName":"FileName","Index":2,"MimeType":"MimeType"}],"Type":"Default","ReadAtNativeFramerate":True,"ETag":"ETag","TranscodingContainer":"TranscodingContainer","IgnoreDts":True,"TranscodingUrl":"TranscodingUrl","Id":"Id","SupportsTranscoding":True,"DefaultAudioStreamIndex":6}],"GenreItems":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"OfficialRating":"OfficialRating","ProgramCount":6,"ProgramId":"ProgramId","Longitude":6.683562403749608,"FocalLength":6.84685269835264,"LockData":True,"IsNews":True,"ShutterSpeed":7.260521264802104,"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","IsFolder":True,"SeriesTimerId":"SeriesTimerId","SeriesId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","MediaStreams":[{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5},{"VideoRange":"VideoRange","CodecTimeBase":"CodecTimeBase","ColorSpace":"ColorSpace","Index":3,"ColorRange":"ColorRange","localizedForced":"localizedForced","BitDepth":6,"Channels":6,"Profile":"Profile","SupportsExternalStream":True,"DeliveryUrl":"DeliveryUrl","localizedDefault":"localizedDefault","Codec":"Codec","ColorPrimaries":"ColorPrimaries","SampleRate":0,"IsTextSubtitleStream":True,"Language":"Language","IsAnamorphic":True,"Height":3,"NalLengthSize":"NalLengthSize","PixelFormat":"PixelFormat","RefFrames":6,"IsAVC":True,"Width":8,"TimeBase":"TimeBase","ColorTransfer":"ColorTransfer","CodecTag":"CodecTag","IsDefault":True,"Path":"Path","Comment":"Comment","DeliveryMethod":"Encode","IsExternalUrl":True,"DisplayTitle":"DisplayTitle","IsForced":True,"ChannelLayout":"ChannelLayout","PacketLength":0,"localizedUndefined":"localizedUndefined","Title":"Title","RealFrameRate":7.05877,"AspectRatio":"AspectRatio","AverageFrameRate":6.778325,"Score":4,"Type":"Audio","IsExternal":True,"IsInterlaced":True,"Level":7.143538047012306,"BitRate":5}],"IsPlaceHolder":True,"CanDownload":True,"IsMovie":True,"SeriesCount":4,"DateLastMediaAdded":"2000-01-23T04:56:07.000+00:00","ParentArtImageTag":"ParentArtImageTag","PlayAccess":"Full","SeriesStudio":"SeriesStudio","IsLive":True,"Width":8,"ExternalUrls":[{"Url":"Url","Name":"Name"},{"Url":"Url","Name":"Name"}],"RecursiveItemCount":4,"ParentId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Path":"Path","MusicVideoCount":7,"ScreenshotImageTags":["ScreenshotImageTags","ScreenshotImageTags"],"EpisodeCount":1,"IsSeries":True,"ProductionLocations":["ProductionLocations","ProductionLocations"],"ParentPrimaryImageItemId":"ParentPrimaryImageItemId","EndDate":"2000-01-23T04:56:07.000+00:00","ParentThumbItemId":"ParentThumbItemId","SeriesPrimaryImageTag":"SeriesPrimaryImageTag","PreferredMetadataLanguage":"PreferredMetadataLanguage","Type":"Type","BackdropImageTags":["BackdropImageTags","BackdropImageTags"],"ParentBackdropImageTags":["ParentBackdropImageTags","ParentBackdropImageTags"],"AirsBeforeEpisodeNumber":6,"ChildCount":3,"Audio":"Mono","Artists":["Artists","Artists"],"ChannelType":"TV","RunTimeTicks":1,"AlbumPrimaryImageTag":"AlbumPrimaryImageTag","CumulativeRunTimeTicks":1,"SourceType":"SourceType","CanDelete":True,"Album":"Album","DisplayPreferencesId":"DisplayPreferencesId","PlaylistItemId":"PlaylistItemId","Latitude":9.965781217890562,"SortName":"SortName","ArtistCount":7,"Name":"Name","StartDate":"2000-01-23T04:56:07.000+00:00","Container":"Container","ProductionYear":0,"SeriesName":"SeriesName","ParentArtItemId":"ParentArtItemId","AlbumId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","LocalTrailerCount":9,"SupportsSync":True,"CompletionPercentage":4.145608029883936,"IndexNumber":1,"Genres":["Genres","Genres"],"LockedFields":["Cast","Cast"],"SeasonId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ParentPrimaryImageTag":"ParentPrimaryImageTag","ProviderIds":{"key":"ProviderIds"},"RemoteTrailers":[{"Url":"Url","Name":"Name"},{"Url":"Url","Name":"Name"}],"MediaSourceCount":8,"CustomRating":"CustomRating","AirsAfterSeasonNumber":0,"AirDays":["Sunday","Sunday"],"ParentLogoItemId":"ParentLogoItemId","PartCount":3,"ChannelName":"ChannelName","EpisodeTitle":"EpisodeTitle","IsoSpeedRating":5,"CommunityRating":2.027123,"Software":"Software","Chapters":[{"StartPositionTicks":9,"ImageTag":"ImageTag","ImageDateModified":"2000-01-23T04:56:07.000+00:00","ImagePath":"ImagePath","Name":"Name"},{"StartPositionTicks":9,"ImageTag":"ImageTag","ImageDateModified":"2000-01-23T04:56:07.000+00:00","ImagePath":"ImagePath","Name":"Name"}],"SongCount":9,"Taglines":["Taglines","Taglines"],"AirsBeforeSeasonNumber":1,"CameraModel":"CameraModel","PreferredMetadataCountryCode":"PreferredMetadataCountryCode","ChannelNumber":"ChannelNumber","UserData":{"Played":True,"UnplayedItemCount":6,"PlayedPercentage":5.507386964179881,"PlayCount":0,"Rating":4.86315908102884,"PlaybackPositionTicks":7,"LastPlayedDate":"2000-01-23T04:56:07.000+00:00","Likes":True,"IsFavorite":True,"ItemId":"ItemId","Key":"Key"},"TimerId":"TimerId","DateCreated":"2000-01-23T04:56:07.000+00:00","HasSubtitles":True,"ParentThumbImageTag":"ParentThumbImageTag","IsSports":True,"ChannelId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ParentIndexNumber":5,"AlbumArtists":[{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"},{"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Name":"Name"}],"ServerId":"ServerId","Number":"Number","AlbumCount":5,"IsRepeat":True,"CollectionType":"CollectionType","Height":7,"PrimaryImageAspectRatio":4.078845849666752,"IsKids":True,"DisplayOrder":"DisplayOrder","IsHD":True,"EnableMediaSourceDisplay":True,"SeriesThumbImageTag":"SeriesThumbImageTag","MovieCount":3,"People":[{"Role":"Role","Type":"Type","PrimaryImageTag":"PrimaryImageTag","Id":"Id","ImageBlurHashes":{"Art":{"key":"Art"},"Banner":{"key":"Banner"},"Thumb":{"key":"Thumb"},"BoxRear":{"key":"BoxRear"},"Chapter":{"key":"Chapter"},"Box":{"key":"Box"},"Profile":{"key":"Profile"},"Logo":{"key":"Logo"},"Disc":{"key":"Disc"},"Primary":{"key":"Primary"},"Screenshot":{"key":"Screenshot"},"Backdrop":{"key":"Backdrop"},"Menu":{"key":"Menu"}},"Name":"Name"},{"Role":"Role","Type":"Type","PrimaryImageTag":"PrimaryImageTag","Id":"Id","ImageBlurHashes":{"Art":{"key":"Art"},"Banner":{"key":"Banner"},"Thumb":{"key":"Thumb"},"BoxRear":{"key":"BoxRear"},"Chapter":{"key":"Chapter"},"Box":{"key":"Box"},"Profile":{"key":"Profile"},"Logo":{"key":"Logo"},"Disc":{"key":"Disc"},"Primary":{"key":"Primary"},"Screenshot":{"key":"Screenshot"},"Backdrop":{"key":"Backdrop"},"Menu":{"key":"Menu"}},"Name":"Name"}],"Overview":"Overview","SpecialFeatureCount":0,"ImageOrientation":"TopLeft","AlbumArtist":"AlbumArtist","ImageTags":{"key":"ImageTags"},"AspectRatio":"AspectRatio","TrailerCount":9,"OriginalTitle":"OriginalTitle","ForcedSortName":"ForcedSortName","IsPremiere":True,"LocationType":"FileSystem","Altitude":5.637376656633329},"ParentBackdropItemId":"ParentBackdropItemId","ServerId":"ServerId","Status":"New","IsPrePaddingRequired":True,"Priority":1,"ExternalId":"ExternalId","ExternalSeriesTimerId":"ExternalSeriesTimerId","ExternalChannelId":"ExternalChannelId","Overview":"Overview","PostPaddingSeconds":0,"ProgramId":"ProgramId","EndDate":"2000-01-23T04:56:07.000+00:00","Type":"Type","ChannelName":"ChannelName","ParentBackdropImageTags":["ParentBackdropImageTags","ParentBackdropImageTags"],"ServiceName":"ServiceName","Id":"Id","SeriesTimerId":"SeriesTimerId"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/LiveTv/Timers/{timer_id}'.format(timer_id='timer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

