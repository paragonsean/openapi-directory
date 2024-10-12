/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Abuse from './model/Abuse';
import AbuseMessage from './model/AbuseMessage';
import AbuseStateConstant from './model/AbuseStateConstant';
import AbuseStateSet from './model/AbuseStateSet';
import Account from './model/Account';
import AccountSummary from './model/AccountSummary';
import Actor from './model/Actor';
import ActorImage from './model/ActorImage';
import ActorInfo from './model/ActorInfo';
import AddIntroOptions from './model/AddIntroOptions';
import AddPlaylist200Response from './model/AddPlaylist200Response';
import AddPlaylist200ResponseVideoPlaylist from './model/AddPlaylist200ResponseVideoPlaylist';
import AddPluginRequest from './model/AddPluginRequest';
import AddPluginRequestOneOf from './model/AddPluginRequestOneOf';
import AddPluginRequestOneOf1 from './model/AddPluginRequestOneOf1';
import AddUser from './model/AddUser';
import AddUserResponse from './model/AddUserResponse';
import AddUserResponseUser from './model/AddUserResponseUser';
import AddVideoChannel200Response from './model/AddVideoChannel200Response';
import AddVideoChannelSync200Response from './model/AddVideoChannelSync200Response';
import AddVideoPlaylistVideo200Response from './model/AddVideoPlaylistVideo200Response';
import AddVideoPlaylistVideo200ResponseVideoPlaylistElement from './model/AddVideoPlaylistVideo200ResponseVideoPlaylistElement';
import AddVideoPlaylistVideoRequest from './model/AddVideoPlaylistVideoRequest';
import AddVideoPlaylistVideoRequestVideoId from './model/AddVideoPlaylistVideoRequestVideoId';
import ApiV1AbusesAbuseIdMessagesGet200Response from './model/ApiV1AbusesAbuseIdMessagesGet200Response';
import ApiV1AbusesAbuseIdMessagesPostRequest from './model/ApiV1AbusesAbuseIdMessagesPostRequest';
import ApiV1AbusesAbuseIdPutRequest from './model/ApiV1AbusesAbuseIdPutRequest';
import ApiV1AbusesPost200Response from './model/ApiV1AbusesPost200Response';
import ApiV1AbusesPost200ResponseAbuse from './model/ApiV1AbusesPost200ResponseAbuse';
import ApiV1AbusesPostRequest from './model/ApiV1AbusesPostRequest';
import ApiV1AbusesPostRequestAccount from './model/ApiV1AbusesPostRequestAccount';
import ApiV1AbusesPostRequestComment from './model/ApiV1AbusesPostRequestComment';
import ApiV1AbusesPostRequestVideo from './model/ApiV1AbusesPostRequestVideo';
import ApiV1AccountsNameVideoPlaylistsGet200Response from './model/ApiV1AccountsNameVideoPlaylistsGet200Response';
import ApiV1CustomPagesHomepageInstancePutRequest from './model/ApiV1CustomPagesHomepageInstancePutRequest';
import ApiV1PluginsNpmNameSettingsPutRequest from './model/ApiV1PluginsNpmNameSettingsPutRequest';
import ApiV1ServerBlocklistAccountsPostRequest from './model/ApiV1ServerBlocklistAccountsPostRequest';
import ApiV1ServerBlocklistServersPostRequest from './model/ApiV1ServerBlocklistServersPostRequest';
import ApiV1ServerFollowingPostRequest from './model/ApiV1ServerFollowingPostRequest';
import ApiV1ServerRedundancyHostPutRequest from './model/ApiV1ServerRedundancyHostPutRequest';
import ApiV1UsersMeAvatarPickPost200Response from './model/ApiV1UsersMeAvatarPickPost200Response';
import ApiV1UsersMeNotificationSettingsPutRequest from './model/ApiV1UsersMeNotificationSettingsPutRequest';
import ApiV1UsersMeNotificationsReadPostRequest from './model/ApiV1UsersMeNotificationsReadPostRequest';
import ApiV1UsersMeSubscriptionsPostRequest from './model/ApiV1UsersMeSubscriptionsPostRequest';
import ApiV1UsersMeVideoPlaylistsVideosExistGet200Response from './model/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response';
import ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner from './model/ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner';
import ApiV1UsersMeVideoQuotaUsedGet200Response from './model/ApiV1UsersMeVideoQuotaUsedGet200Response';
import ApiV1VideoChannelsChannelHandleBannerPickPost200Response from './model/ApiV1VideoChannelsChannelHandleBannerPickPost200Response';
import ApiV1VideosIdCommentThreadsPostRequest from './model/ApiV1VideosIdCommentThreadsPostRequest';
import ApiV1VideosIdRatePutRequest from './model/ApiV1VideosIdRatePutRequest';
import ApiV1VideosLiveIdSessionsGet200Response from './model/ApiV1VideosLiveIdSessionsGet200Response';
import BlockStatus from './model/BlockStatus';
import BlockStatusAccountsValue from './model/BlockStatusAccountsValue';
import BlockStatusHostsValue from './model/BlockStatusHostsValue';
import CommentThreadPostResponse from './model/CommentThreadPostResponse';
import CommentThreadResponse from './model/CommentThreadResponse';
import ConfirmTwoFactorRequestRequest from './model/ConfirmTwoFactorRequestRequest';
import CreateVideoTranscodingRequest from './model/CreateVideoTranscodingRequest';
import CustomHomepage from './model/CustomHomepage';
import CutOptions from './model/CutOptions';
import DisableTwoFactorRequest from './model/DisableTwoFactorRequest';
import FileRedundancyInformation from './model/FileRedundancyInformation';
import Follow from './model/Follow';
import GetAbuses200Response from './model/GetAbuses200Response';
import GetAccountFollowers200Response from './model/GetAccountFollowers200Response';
import GetAccountVideosCategoryOneOfParameter from './model/GetAccountVideosCategoryOneOfParameter';
import GetAccountVideosLanguageOneOfParameter from './model/GetAccountVideosLanguageOneOfParameter';
import GetAccountVideosLicenceOneOfParameter from './model/GetAccountVideosLicenceOneOfParameter';
import GetAccountVideosTagsAllOfParameter from './model/GetAccountVideosTagsAllOfParameter';
import GetAccountVideosTagsOneOfParameter from './model/GetAccountVideosTagsOneOfParameter';
import GetJobs200Response from './model/GetJobs200Response';
import GetLiveIdIdParameter from './model/GetLiveIdIdParameter';
import GetMeVideoRating from './model/GetMeVideoRating';
import GetOAuthToken200Response from './model/GetOAuthToken200Response';
import GetUser200Response from './model/GetUser200Response';
import GetVideoBlocks200Response from './model/GetVideoBlocks200Response';
import GetVideoCaptions200Response from './model/GetVideoCaptions200Response';
import ImportVideosInChannelCreate from './model/ImportVideosInChannelCreate';
import Job from './model/Job';
import ListRegistrations200Response from './model/ListRegistrations200Response';
import LiveVideoLatencyMode from './model/LiveVideoLatencyMode';
import LiveVideoReplaySettings from './model/LiveVideoReplaySettings';
import LiveVideoResponse from './model/LiveVideoResponse';
import LiveVideoSessionResponse from './model/LiveVideoSessionResponse';
import LiveVideoSessionResponseReplayVideo from './model/LiveVideoSessionResponseReplayVideo';
import LiveVideoUpdate from './model/LiveVideoUpdate';
import MRSSGroupContent from './model/MRSSGroupContent';
import MRSSPeerLink from './model/MRSSPeerLink';
import NSFWPolicy from './model/NSFWPolicy';
import Notification from './model/Notification';
import NotificationActorFollow from './model/NotificationActorFollow';
import NotificationActorFollowFollowing from './model/NotificationActorFollowFollowing';
import NotificationComment from './model/NotificationComment';
import NotificationListResponse from './model/NotificationListResponse';
import NotificationVideo from './model/NotificationVideo';
import NotificationVideoAbuse from './model/NotificationVideoAbuse';
import NotificationVideoImport from './model/NotificationVideoImport';
import OAuthClient from './model/OAuthClient';
import PlaybackMetricCreate from './model/PlaybackMetricCreate';
import PlaylistElement from './model/PlaylistElement';
import Plugin from './model/Plugin';
import PluginResponse from './model/PluginResponse';
import PutMirroredVideoRequest from './model/PutMirroredVideoRequest';
import PutVideoPlaylistVideoRequest from './model/PutVideoPlaylistVideoRequest';
import RegisterUser from './model/RegisterUser';
import RegisterUserChannel from './model/RegisterUserChannel';
import ReorderVideoPlaylistRequest from './model/ReorderVideoPlaylistRequest';
import RequestTwoFactorResponse from './model/RequestTwoFactorResponse';
import RequestTwoFactorResponseOtpRequest from './model/RequestTwoFactorResponseOtpRequest';
import ResendEmailToVerifyRegistrationRequest from './model/ResendEmailToVerifyRegistrationRequest';
import ResendEmailToVerifyUserRequest from './model/ResendEmailToVerifyUserRequest';
import SendClientLog from './model/SendClientLog';
import ServerConfig from './model/ServerConfig';
import ServerConfigAbout from './model/ServerConfigAbout';
import ServerConfigAboutInstance from './model/ServerConfigAboutInstance';
import ServerConfigAutoBlacklist from './model/ServerConfigAutoBlacklist';
import ServerConfigAutoBlacklistVideos from './model/ServerConfigAutoBlacklistVideos';
import ServerConfigAutoBlacklistVideosOfUsers from './model/ServerConfigAutoBlacklistVideosOfUsers';
import ServerConfigAvatar from './model/ServerConfigAvatar';
import ServerConfigAvatarFile from './model/ServerConfigAvatarFile';
import ServerConfigAvatarFileSize from './model/ServerConfigAvatarFileSize';
import ServerConfigCustom from './model/ServerConfigCustom';
import ServerConfigCustomAdmin from './model/ServerConfigCustomAdmin';
import ServerConfigCustomCache from './model/ServerConfigCustomCache';
import ServerConfigCustomCacheCaptions from './model/ServerConfigCustomCacheCaptions';
import ServerConfigCustomFollowers from './model/ServerConfigCustomFollowers';
import ServerConfigCustomFollowersInstance from './model/ServerConfigCustomFollowersInstance';
import ServerConfigCustomImport from './model/ServerConfigCustomImport';
import ServerConfigCustomInstance from './model/ServerConfigCustomInstance';
import ServerConfigCustomServices from './model/ServerConfigCustomServices';
import ServerConfigCustomServicesTwitter from './model/ServerConfigCustomServicesTwitter';
import ServerConfigCustomSignup from './model/ServerConfigCustomSignup';
import ServerConfigCustomTheme from './model/ServerConfigCustomTheme';
import ServerConfigCustomTranscoding from './model/ServerConfigCustomTranscoding';
import ServerConfigCustomTranscodingHls from './model/ServerConfigCustomTranscodingHls';
import ServerConfigCustomTranscodingResolutions from './model/ServerConfigCustomTranscodingResolutions';
import ServerConfigCustomTranscodingWebtorrent from './model/ServerConfigCustomTranscodingWebtorrent';
import ServerConfigCustomUser from './model/ServerConfigCustomUser';
import ServerConfigFollowings from './model/ServerConfigFollowings';
import ServerConfigFollowingsInstance from './model/ServerConfigFollowingsInstance';
import ServerConfigFollowingsInstanceAutoFollowIndex from './model/ServerConfigFollowingsInstanceAutoFollowIndex';
import ServerConfigImport from './model/ServerConfigImport';
import ServerConfigImportVideos from './model/ServerConfigImportVideos';
import ServerConfigInstance from './model/ServerConfigInstance';
import ServerConfigInstanceCustomizations from './model/ServerConfigInstanceCustomizations';
import ServerConfigPlugin from './model/ServerConfigPlugin';
import ServerConfigSearch from './model/ServerConfigSearch';
import ServerConfigSearchRemoteUri from './model/ServerConfigSearchRemoteUri';
import ServerConfigSignup from './model/ServerConfigSignup';
import ServerConfigTranscoding from './model/ServerConfigTranscoding';
import ServerConfigTrending from './model/ServerConfigTrending';
import ServerConfigTrendingVideos from './model/ServerConfigTrendingVideos';
import ServerConfigUser from './model/ServerConfigUser';
import ServerConfigVideo from './model/ServerConfigVideo';
import ServerConfigVideoCaption from './model/ServerConfigVideoCaption';
import ServerConfigVideoFile from './model/ServerConfigVideoFile';
import ServerConfigVideoImage from './model/ServerConfigVideoImage';
import ServerStats from './model/ServerStats';
import ServerStatsVideosRedundancyInner from './model/ServerStatsVideosRedundancyInner';
import UninstallPluginRequest from './model/UninstallPluginRequest';
import UpdateMe from './model/UpdateMe';
import UpdateUser from './model/UpdateUser';
import User from './model/User';
import UserAdminFlags from './model/UserAdminFlags';
import UserRegistration from './model/UserRegistration';
import UserRegistrationAcceptOrReject from './model/UserRegistrationAcceptOrReject';
import UserRegistrationRequest from './model/UserRegistrationRequest';
import UserRegistrationState from './model/UserRegistrationState';
import UserRegistrationUser from './model/UserRegistrationUser';
import UserRole from './model/UserRole';
import UserViewingVideo from './model/UserViewingVideo';
import UserWithStats from './model/UserWithStats';
import VerifyRegistrationEmailRequest from './model/VerifyRegistrationEmailRequest';
import VerifyUserRequest from './model/VerifyUserRequest';
import Video from './model/Video';
import VideoBlacklist from './model/VideoBlacklist';
import VideoCaption from './model/VideoCaption';
import VideoChannel from './model/VideoChannel';
import VideoChannelAllOfOwnerAccount from './model/VideoChannelAllOfOwnerAccount';
import VideoChannelCreate from './model/VideoChannelCreate';
import VideoChannelEdit from './model/VideoChannelEdit';
import VideoChannelList from './model/VideoChannelList';
import VideoChannelListDataInner from './model/VideoChannelListDataInner';
import VideoChannelSummary from './model/VideoChannelSummary';
import VideoChannelSync from './model/VideoChannelSync';
import VideoChannelSyncCreate from './model/VideoChannelSyncCreate';
import VideoChannelSyncList from './model/VideoChannelSyncList';
import VideoChannelSyncState from './model/VideoChannelSyncState';
import VideoChannelUpdate from './model/VideoChannelUpdate';
import VideoComment from './model/VideoComment';
import VideoCommentThreadTree from './model/VideoCommentThreadTree';
import VideoCommentsForXMLInner from './model/VideoCommentsForXMLInner';
import VideoConstantNumberCategory from './model/VideoConstantNumberCategory';
import VideoConstantNumberLicence from './model/VideoConstantNumberLicence';
import VideoConstantStringLanguage from './model/VideoConstantStringLanguage';
import VideoDetails from './model/VideoDetails';
import VideoFile from './model/VideoFile';
import VideoImport from './model/VideoImport';
import VideoImportStateConstant from './model/VideoImportStateConstant';
import VideoImportsList from './model/VideoImportsList';
import VideoInfo from './model/VideoInfo';
import VideoListResponse from './model/VideoListResponse';
import VideoPlaylist from './model/VideoPlaylist';
import VideoPlaylistPrivacyConstant from './model/VideoPlaylistPrivacyConstant';
import VideoPlaylistPrivacySet from './model/VideoPlaylistPrivacySet';
import VideoPlaylistTypeConstant from './model/VideoPlaylistTypeConstant';
import VideoPlaylistTypeSet from './model/VideoPlaylistTypeSet';
import VideoPrivacyConstant from './model/VideoPrivacyConstant';
import VideoPrivacySet from './model/VideoPrivacySet';
import VideoRating from './model/VideoRating';
import VideoRedundancy from './model/VideoRedundancy';
import VideoRedundancyRedundancies from './model/VideoRedundancyRedundancies';
import VideoResolutionConstant from './model/VideoResolutionConstant';
import VideoScheduledUpdate from './model/VideoScheduledUpdate';
import VideoSource from './model/VideoSource';
import VideoStateConstant from './model/VideoStateConstant';
import VideoStatsOverall from './model/VideoStatsOverall';
import VideoStatsOverallCountriesInner from './model/VideoStatsOverallCountriesInner';
import VideoStatsRetention from './model/VideoStatsRetention';
import VideoStatsRetentionDataInner from './model/VideoStatsRetentionDataInner';
import VideoStatsTimeserie from './model/VideoStatsTimeserie';
import VideoStatsTimeserieDataInner from './model/VideoStatsTimeserieDataInner';
import VideoStreamingPlaylists from './model/VideoStreamingPlaylists';
import VideoStreamingPlaylistsHLS from './model/VideoStreamingPlaylistsHLS';
import VideoStreamingPlaylistsHLSRedundanciesInner from './model/VideoStreamingPlaylistsHLSRedundanciesInner';
import VideoTokenResponse from './model/VideoTokenResponse';
import VideoTokenResponseFiles from './model/VideoTokenResponseFiles';
import VideoUploadRequestCommon from './model/VideoUploadRequestCommon';
import VideoUploadRequestResumable from './model/VideoUploadRequestResumable';
import VideoUploadResponse from './model/VideoUploadResponse';
import VideoUploadResponseVideo from './model/VideoUploadResponseVideo';
import VideoUserHistory from './model/VideoUserHistory';
import VideosForXMLInner from './model/VideosForXMLInner';
import VideosForXMLInnerEnclosure from './model/VideosForXMLInnerEnclosure';
import VideosForXMLInnerMediaCommunity from './model/VideosForXMLInnerMediaCommunity';
import VideosForXMLInnerMediaCommunityMediaStatistics from './model/VideosForXMLInnerMediaCommunityMediaStatistics';
import VideosForXMLInnerMediaEmbed from './model/VideosForXMLInnerMediaEmbed';
import VideosForXMLInnerMediaGroupInner from './model/VideosForXMLInnerMediaGroupInner';
import VideosForXMLInnerMediaPlayer from './model/VideosForXMLInnerMediaPlayer';
import VideosForXMLInnerMediaThumbnail from './model/VideosForXMLInnerMediaThumbnail';
import AbusesApi from './api/AbusesApi';
import AccountBlocksApi from './api/AccountBlocksApi';
import AccountsApi from './api/AccountsApi';
import ChannelsSyncApi from './api/ChannelsSyncApi';
import ConfigApi from './api/ConfigApi';
import HomepageApi from './api/HomepageApi';
import InstanceFollowsApi from './api/InstanceFollowsApi';
import InstanceRedundancyApi from './api/InstanceRedundancyApi';
import JobApi from './api/JobApi';
import LiveVideosApi from './api/LiveVideosApi';
import LogsApi from './api/LogsApi';
import MyHistoryApi from './api/MyHistoryApi';
import MyNotificationsApi from './api/MyNotificationsApi';
import MySubscriptionsApi from './api/MySubscriptionsApi';
import MyUserApi from './api/MyUserApi';
import PluginsApi from './api/PluginsApi';
import RegisterApi from './api/RegisterApi';
import SearchApi from './api/SearchApi';
import ServerBlocksApi from './api/ServerBlocksApi';
import SessionApi from './api/SessionApi';
import StaticVideoFilesApi from './api/StaticVideoFilesApi';
import StatsApi from './api/StatsApi';
import UsersApi from './api/UsersApi';
import VideoApi from './api/VideoApi';
import VideoBlocksApi from './api/VideoBlocksApi';
import VideoCaptionsApi from './api/VideoCaptionsApi';
import VideoChannelsApi from './api/VideoChannelsApi';
import VideoCommentsApi from './api/VideoCommentsApi';
import VideoFeedsApi from './api/VideoFeedsApi';
import VideoFilesApi from './api/VideoFilesApi';
import VideoImportsApi from './api/VideoImportsApi';
import VideoMirroringApi from './api/VideoMirroringApi';
import VideoOwnershipChangeApi from './api/VideoOwnershipChangeApi';
import VideoPlaylistsApi from './api/VideoPlaylistsApi';
import VideoRatesApi from './api/VideoRatesApi';
import VideoStatsApi from './api/VideoStatsApi';
import VideoTranscodingApi from './api/VideoTranscodingApi';
import VideoUploadApi from './api/VideoUploadApi';
import VideosApi from './api/VideosApi';


/**
* The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  &#x60;&#x60;&#x60; HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset&#x3D;utf-8  {   \&quot;detail\&quot;: \&quot;Video not found\&quot;,   \&quot;docs\&quot;: \&quot;https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\&quot;,   \&quot;status\&quot;: 404,   \&quot;title\&quot;: \&quot;Not Found\&quot;,   \&quot;type\&quot;: \&quot;about:blank\&quot; } &#x60;&#x60;&#x60;  We provide error &#x60;type&#x60; values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  &#x60;&#x60;&#x60; HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset&#x3D;utf-8  {   \&quot;detail\&quot;: \&quot;Cannot get this video regarding follow constraints\&quot;,   \&quot;docs\&quot;: \&quot;https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\&quot;,   \&quot;status\&quot;: 403,   \&quot;title\&quot;: \&quot;Forbidden\&quot;,   \&quot;type\&quot;: \&quot;https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\&quot; } &#x60;&#x60;&#x60;  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  &#x60;&#x60;&#x60; HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset&#x3D;utf-8  {   \&quot;detail\&quot;: \&quot;Incorrect request parameters: id\&quot;,   \&quot;docs\&quot;: \&quot;https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\&quot;,   \&quot;instance\&quot;: \&quot;/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\&quot;,   \&quot;invalid-params\&quot;: {     \&quot;id\&quot;: {       \&quot;location\&quot;: \&quot;params\&quot;,       \&quot;msg\&quot;: \&quot;Invalid value\&quot;,       \&quot;param\&quot;: \&quot;id\&quot;,       \&quot;value\&quot;: \&quot;9c9de5e8-0a1e-484a-b099-e80766180\&quot;     }   },   \&quot;status\&quot;: 400,   \&quot;title\&quot;: \&quot;Bad Request\&quot;,   \&quot;type\&quot;: \&quot;about:blank\&quot; } &#x60;&#x60;&#x60;  Where &#x60;id&#x60; is the name of the field concerned by the error, within the route definition. &#x60;invalid-params.&lt;field&gt;.location&#x60; can be either &#39;params&#39;, &#39;body&#39;, &#39;header&#39;, &#39;query&#39; or &#39;cookies&#39;, and &#x60;invalid-params.&lt;field&gt;.value&#x60; reports the value that didn&#39;t pass validation whose &#x60;invalid-params.&lt;field&gt;.msg&#x60; is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - &#x60;error&#x60;: superseded by &#x60;detail&#x60; - &#x60;code&#x60;: superseded by &#x60;type&#x60; (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube&#39;s API. Custom values can be set by administrators:  | Endpoint (prefix: &#x60;/api/v1&#x60;) | Calls         | Time frame   | |------------------------------|---------------|--------------| | &#x60;/_*&#x60;                         | 50            | 10 seconds   | | &#x60;POST /users/token&#x60;          | 15            | 5 minutes    | | &#x60;POST /users/register&#x60;       | 2&lt;sup&gt;*&lt;/sup&gt; | 5 minutes    | | &#x60;POST /users/ask-send-verify-email&#x60; | 3      | 5 minutes    |  Depending on the endpoint, &lt;sup&gt;*&lt;/sup&gt;failed requests are not taken into account. A service limit is announced by a &#x60;429 Too Many Requests&#x60; status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | &#x60;X-RateLimit-Limit&#x60;     | Number of max requests allowed in the current time period  | | &#x60;X-RateLimit-Remaining&#x60; | Number of remaining requests in the current time period    | | &#x60;X-RateLimit-Reset&#x60;     | Timestamp of end of current time period as UNIX timestamp  | | &#x60;Retry-After&#x60;           | Seconds to delay after the first &#x60;429&#x60; is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | &#x60;/api/_*&#x60;                    | | &#x60;/download/_*&#x60;               | | &#x60;/lazy-static/_*&#x60;            | | &#x60;/.well-known/webfinger&#x60;    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var PeerTube = require('index'); // See note below*.
* var xxxSvc = new PeerTube.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new PeerTube.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new PeerTube.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new PeerTube.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 5.1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Abuse model constructor.
     * @property {module:model/Abuse}
     */
    Abuse,

    /**
     * The AbuseMessage model constructor.
     * @property {module:model/AbuseMessage}
     */
    AbuseMessage,

    /**
     * The AbuseStateConstant model constructor.
     * @property {module:model/AbuseStateConstant}
     */
    AbuseStateConstant,

    /**
     * The AbuseStateSet model constructor.
     * @property {module:model/AbuseStateSet}
     */
    AbuseStateSet,

    /**
     * The Account model constructor.
     * @property {module:model/Account}
     */
    Account,

    /**
     * The AccountSummary model constructor.
     * @property {module:model/AccountSummary}
     */
    AccountSummary,

    /**
     * The Actor model constructor.
     * @property {module:model/Actor}
     */
    Actor,

    /**
     * The ActorImage model constructor.
     * @property {module:model/ActorImage}
     */
    ActorImage,

    /**
     * The ActorInfo model constructor.
     * @property {module:model/ActorInfo}
     */
    ActorInfo,

    /**
     * The AddIntroOptions model constructor.
     * @property {module:model/AddIntroOptions}
     */
    AddIntroOptions,

    /**
     * The AddPlaylist200Response model constructor.
     * @property {module:model/AddPlaylist200Response}
     */
    AddPlaylist200Response,

    /**
     * The AddPlaylist200ResponseVideoPlaylist model constructor.
     * @property {module:model/AddPlaylist200ResponseVideoPlaylist}
     */
    AddPlaylist200ResponseVideoPlaylist,

    /**
     * The AddPluginRequest model constructor.
     * @property {module:model/AddPluginRequest}
     */
    AddPluginRequest,

    /**
     * The AddPluginRequestOneOf model constructor.
     * @property {module:model/AddPluginRequestOneOf}
     */
    AddPluginRequestOneOf,

    /**
     * The AddPluginRequestOneOf1 model constructor.
     * @property {module:model/AddPluginRequestOneOf1}
     */
    AddPluginRequestOneOf1,

    /**
     * The AddUser model constructor.
     * @property {module:model/AddUser}
     */
    AddUser,

    /**
     * The AddUserResponse model constructor.
     * @property {module:model/AddUserResponse}
     */
    AddUserResponse,

    /**
     * The AddUserResponseUser model constructor.
     * @property {module:model/AddUserResponseUser}
     */
    AddUserResponseUser,

    /**
     * The AddVideoChannel200Response model constructor.
     * @property {module:model/AddVideoChannel200Response}
     */
    AddVideoChannel200Response,

    /**
     * The AddVideoChannelSync200Response model constructor.
     * @property {module:model/AddVideoChannelSync200Response}
     */
    AddVideoChannelSync200Response,

    /**
     * The AddVideoPlaylistVideo200Response model constructor.
     * @property {module:model/AddVideoPlaylistVideo200Response}
     */
    AddVideoPlaylistVideo200Response,

    /**
     * The AddVideoPlaylistVideo200ResponseVideoPlaylistElement model constructor.
     * @property {module:model/AddVideoPlaylistVideo200ResponseVideoPlaylistElement}
     */
    AddVideoPlaylistVideo200ResponseVideoPlaylistElement,

    /**
     * The AddVideoPlaylistVideoRequest model constructor.
     * @property {module:model/AddVideoPlaylistVideoRequest}
     */
    AddVideoPlaylistVideoRequest,

    /**
     * The AddVideoPlaylistVideoRequestVideoId model constructor.
     * @property {module:model/AddVideoPlaylistVideoRequestVideoId}
     */
    AddVideoPlaylistVideoRequestVideoId,

    /**
     * The ApiV1AbusesAbuseIdMessagesGet200Response model constructor.
     * @property {module:model/ApiV1AbusesAbuseIdMessagesGet200Response}
     */
    ApiV1AbusesAbuseIdMessagesGet200Response,

    /**
     * The ApiV1AbusesAbuseIdMessagesPostRequest model constructor.
     * @property {module:model/ApiV1AbusesAbuseIdMessagesPostRequest}
     */
    ApiV1AbusesAbuseIdMessagesPostRequest,

    /**
     * The ApiV1AbusesAbuseIdPutRequest model constructor.
     * @property {module:model/ApiV1AbusesAbuseIdPutRequest}
     */
    ApiV1AbusesAbuseIdPutRequest,

    /**
     * The ApiV1AbusesPost200Response model constructor.
     * @property {module:model/ApiV1AbusesPost200Response}
     */
    ApiV1AbusesPost200Response,

    /**
     * The ApiV1AbusesPost200ResponseAbuse model constructor.
     * @property {module:model/ApiV1AbusesPost200ResponseAbuse}
     */
    ApiV1AbusesPost200ResponseAbuse,

    /**
     * The ApiV1AbusesPostRequest model constructor.
     * @property {module:model/ApiV1AbusesPostRequest}
     */
    ApiV1AbusesPostRequest,

    /**
     * The ApiV1AbusesPostRequestAccount model constructor.
     * @property {module:model/ApiV1AbusesPostRequestAccount}
     */
    ApiV1AbusesPostRequestAccount,

    /**
     * The ApiV1AbusesPostRequestComment model constructor.
     * @property {module:model/ApiV1AbusesPostRequestComment}
     */
    ApiV1AbusesPostRequestComment,

    /**
     * The ApiV1AbusesPostRequestVideo model constructor.
     * @property {module:model/ApiV1AbusesPostRequestVideo}
     */
    ApiV1AbusesPostRequestVideo,

    /**
     * The ApiV1AccountsNameVideoPlaylistsGet200Response model constructor.
     * @property {module:model/ApiV1AccountsNameVideoPlaylistsGet200Response}
     */
    ApiV1AccountsNameVideoPlaylistsGet200Response,

    /**
     * The ApiV1CustomPagesHomepageInstancePutRequest model constructor.
     * @property {module:model/ApiV1CustomPagesHomepageInstancePutRequest}
     */
    ApiV1CustomPagesHomepageInstancePutRequest,

    /**
     * The ApiV1PluginsNpmNameSettingsPutRequest model constructor.
     * @property {module:model/ApiV1PluginsNpmNameSettingsPutRequest}
     */
    ApiV1PluginsNpmNameSettingsPutRequest,

    /**
     * The ApiV1ServerBlocklistAccountsPostRequest model constructor.
     * @property {module:model/ApiV1ServerBlocklistAccountsPostRequest}
     */
    ApiV1ServerBlocklistAccountsPostRequest,

    /**
     * The ApiV1ServerBlocklistServersPostRequest model constructor.
     * @property {module:model/ApiV1ServerBlocklistServersPostRequest}
     */
    ApiV1ServerBlocklistServersPostRequest,

    /**
     * The ApiV1ServerFollowingPostRequest model constructor.
     * @property {module:model/ApiV1ServerFollowingPostRequest}
     */
    ApiV1ServerFollowingPostRequest,

    /**
     * The ApiV1ServerRedundancyHostPutRequest model constructor.
     * @property {module:model/ApiV1ServerRedundancyHostPutRequest}
     */
    ApiV1ServerRedundancyHostPutRequest,

    /**
     * The ApiV1UsersMeAvatarPickPost200Response model constructor.
     * @property {module:model/ApiV1UsersMeAvatarPickPost200Response}
     */
    ApiV1UsersMeAvatarPickPost200Response,

    /**
     * The ApiV1UsersMeNotificationSettingsPutRequest model constructor.
     * @property {module:model/ApiV1UsersMeNotificationSettingsPutRequest}
     */
    ApiV1UsersMeNotificationSettingsPutRequest,

    /**
     * The ApiV1UsersMeNotificationsReadPostRequest model constructor.
     * @property {module:model/ApiV1UsersMeNotificationsReadPostRequest}
     */
    ApiV1UsersMeNotificationsReadPostRequest,

    /**
     * The ApiV1UsersMeSubscriptionsPostRequest model constructor.
     * @property {module:model/ApiV1UsersMeSubscriptionsPostRequest}
     */
    ApiV1UsersMeSubscriptionsPostRequest,

    /**
     * The ApiV1UsersMeVideoPlaylistsVideosExistGet200Response model constructor.
     * @property {module:model/ApiV1UsersMeVideoPlaylistsVideosExistGet200Response}
     */
    ApiV1UsersMeVideoPlaylistsVideosExistGet200Response,

    /**
     * The ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner model constructor.
     * @property {module:model/ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner}
     */
    ApiV1UsersMeVideoPlaylistsVideosExistGet200ResponseVideoIdInner,

    /**
     * The ApiV1UsersMeVideoQuotaUsedGet200Response model constructor.
     * @property {module:model/ApiV1UsersMeVideoQuotaUsedGet200Response}
     */
    ApiV1UsersMeVideoQuotaUsedGet200Response,

    /**
     * The ApiV1VideoChannelsChannelHandleBannerPickPost200Response model constructor.
     * @property {module:model/ApiV1VideoChannelsChannelHandleBannerPickPost200Response}
     */
    ApiV1VideoChannelsChannelHandleBannerPickPost200Response,

    /**
     * The ApiV1VideosIdCommentThreadsPostRequest model constructor.
     * @property {module:model/ApiV1VideosIdCommentThreadsPostRequest}
     */
    ApiV1VideosIdCommentThreadsPostRequest,

    /**
     * The ApiV1VideosIdRatePutRequest model constructor.
     * @property {module:model/ApiV1VideosIdRatePutRequest}
     */
    ApiV1VideosIdRatePutRequest,

    /**
     * The ApiV1VideosLiveIdSessionsGet200Response model constructor.
     * @property {module:model/ApiV1VideosLiveIdSessionsGet200Response}
     */
    ApiV1VideosLiveIdSessionsGet200Response,

    /**
     * The BlockStatus model constructor.
     * @property {module:model/BlockStatus}
     */
    BlockStatus,

    /**
     * The BlockStatusAccountsValue model constructor.
     * @property {module:model/BlockStatusAccountsValue}
     */
    BlockStatusAccountsValue,

    /**
     * The BlockStatusHostsValue model constructor.
     * @property {module:model/BlockStatusHostsValue}
     */
    BlockStatusHostsValue,

    /**
     * The CommentThreadPostResponse model constructor.
     * @property {module:model/CommentThreadPostResponse}
     */
    CommentThreadPostResponse,

    /**
     * The CommentThreadResponse model constructor.
     * @property {module:model/CommentThreadResponse}
     */
    CommentThreadResponse,

    /**
     * The ConfirmTwoFactorRequestRequest model constructor.
     * @property {module:model/ConfirmTwoFactorRequestRequest}
     */
    ConfirmTwoFactorRequestRequest,

    /**
     * The CreateVideoTranscodingRequest model constructor.
     * @property {module:model/CreateVideoTranscodingRequest}
     */
    CreateVideoTranscodingRequest,

    /**
     * The CustomHomepage model constructor.
     * @property {module:model/CustomHomepage}
     */
    CustomHomepage,

    /**
     * The CutOptions model constructor.
     * @property {module:model/CutOptions}
     */
    CutOptions,

    /**
     * The DisableTwoFactorRequest model constructor.
     * @property {module:model/DisableTwoFactorRequest}
     */
    DisableTwoFactorRequest,

    /**
     * The FileRedundancyInformation model constructor.
     * @property {module:model/FileRedundancyInformation}
     */
    FileRedundancyInformation,

    /**
     * The Follow model constructor.
     * @property {module:model/Follow}
     */
    Follow,

    /**
     * The GetAbuses200Response model constructor.
     * @property {module:model/GetAbuses200Response}
     */
    GetAbuses200Response,

    /**
     * The GetAccountFollowers200Response model constructor.
     * @property {module:model/GetAccountFollowers200Response}
     */
    GetAccountFollowers200Response,

    /**
     * The GetAccountVideosCategoryOneOfParameter model constructor.
     * @property {module:model/GetAccountVideosCategoryOneOfParameter}
     */
    GetAccountVideosCategoryOneOfParameter,

    /**
     * The GetAccountVideosLanguageOneOfParameter model constructor.
     * @property {module:model/GetAccountVideosLanguageOneOfParameter}
     */
    GetAccountVideosLanguageOneOfParameter,

    /**
     * The GetAccountVideosLicenceOneOfParameter model constructor.
     * @property {module:model/GetAccountVideosLicenceOneOfParameter}
     */
    GetAccountVideosLicenceOneOfParameter,

    /**
     * The GetAccountVideosTagsAllOfParameter model constructor.
     * @property {module:model/GetAccountVideosTagsAllOfParameter}
     */
    GetAccountVideosTagsAllOfParameter,

    /**
     * The GetAccountVideosTagsOneOfParameter model constructor.
     * @property {module:model/GetAccountVideosTagsOneOfParameter}
     */
    GetAccountVideosTagsOneOfParameter,

    /**
     * The GetJobs200Response model constructor.
     * @property {module:model/GetJobs200Response}
     */
    GetJobs200Response,

    /**
     * The GetLiveIdIdParameter model constructor.
     * @property {module:model/GetLiveIdIdParameter}
     */
    GetLiveIdIdParameter,

    /**
     * The GetMeVideoRating model constructor.
     * @property {module:model/GetMeVideoRating}
     */
    GetMeVideoRating,

    /**
     * The GetOAuthToken200Response model constructor.
     * @property {module:model/GetOAuthToken200Response}
     */
    GetOAuthToken200Response,

    /**
     * The GetUser200Response model constructor.
     * @property {module:model/GetUser200Response}
     */
    GetUser200Response,

    /**
     * The GetVideoBlocks200Response model constructor.
     * @property {module:model/GetVideoBlocks200Response}
     */
    GetVideoBlocks200Response,

    /**
     * The GetVideoCaptions200Response model constructor.
     * @property {module:model/GetVideoCaptions200Response}
     */
    GetVideoCaptions200Response,

    /**
     * The ImportVideosInChannelCreate model constructor.
     * @property {module:model/ImportVideosInChannelCreate}
     */
    ImportVideosInChannelCreate,

    /**
     * The Job model constructor.
     * @property {module:model/Job}
     */
    Job,

    /**
     * The ListRegistrations200Response model constructor.
     * @property {module:model/ListRegistrations200Response}
     */
    ListRegistrations200Response,

    /**
     * The LiveVideoLatencyMode model constructor.
     * @property {module:model/LiveVideoLatencyMode}
     */
    LiveVideoLatencyMode,

    /**
     * The LiveVideoReplaySettings model constructor.
     * @property {module:model/LiveVideoReplaySettings}
     */
    LiveVideoReplaySettings,

    /**
     * The LiveVideoResponse model constructor.
     * @property {module:model/LiveVideoResponse}
     */
    LiveVideoResponse,

    /**
     * The LiveVideoSessionResponse model constructor.
     * @property {module:model/LiveVideoSessionResponse}
     */
    LiveVideoSessionResponse,

    /**
     * The LiveVideoSessionResponseReplayVideo model constructor.
     * @property {module:model/LiveVideoSessionResponseReplayVideo}
     */
    LiveVideoSessionResponseReplayVideo,

    /**
     * The LiveVideoUpdate model constructor.
     * @property {module:model/LiveVideoUpdate}
     */
    LiveVideoUpdate,

    /**
     * The MRSSGroupContent model constructor.
     * @property {module:model/MRSSGroupContent}
     */
    MRSSGroupContent,

    /**
     * The MRSSPeerLink model constructor.
     * @property {module:model/MRSSPeerLink}
     */
    MRSSPeerLink,

    /**
     * The NSFWPolicy model constructor.
     * @property {module:model/NSFWPolicy}
     */
    NSFWPolicy,

    /**
     * The Notification model constructor.
     * @property {module:model/Notification}
     */
    Notification,

    /**
     * The NotificationActorFollow model constructor.
     * @property {module:model/NotificationActorFollow}
     */
    NotificationActorFollow,

    /**
     * The NotificationActorFollowFollowing model constructor.
     * @property {module:model/NotificationActorFollowFollowing}
     */
    NotificationActorFollowFollowing,

    /**
     * The NotificationComment model constructor.
     * @property {module:model/NotificationComment}
     */
    NotificationComment,

    /**
     * The NotificationListResponse model constructor.
     * @property {module:model/NotificationListResponse}
     */
    NotificationListResponse,

    /**
     * The NotificationVideo model constructor.
     * @property {module:model/NotificationVideo}
     */
    NotificationVideo,

    /**
     * The NotificationVideoAbuse model constructor.
     * @property {module:model/NotificationVideoAbuse}
     */
    NotificationVideoAbuse,

    /**
     * The NotificationVideoImport model constructor.
     * @property {module:model/NotificationVideoImport}
     */
    NotificationVideoImport,

    /**
     * The OAuthClient model constructor.
     * @property {module:model/OAuthClient}
     */
    OAuthClient,

    /**
     * The PlaybackMetricCreate model constructor.
     * @property {module:model/PlaybackMetricCreate}
     */
    PlaybackMetricCreate,

    /**
     * The PlaylistElement model constructor.
     * @property {module:model/PlaylistElement}
     */
    PlaylistElement,

    /**
     * The Plugin model constructor.
     * @property {module:model/Plugin}
     */
    Plugin,

    /**
     * The PluginResponse model constructor.
     * @property {module:model/PluginResponse}
     */
    PluginResponse,

    /**
     * The PutMirroredVideoRequest model constructor.
     * @property {module:model/PutMirroredVideoRequest}
     */
    PutMirroredVideoRequest,

    /**
     * The PutVideoPlaylistVideoRequest model constructor.
     * @property {module:model/PutVideoPlaylistVideoRequest}
     */
    PutVideoPlaylistVideoRequest,

    /**
     * The RegisterUser model constructor.
     * @property {module:model/RegisterUser}
     */
    RegisterUser,

    /**
     * The RegisterUserChannel model constructor.
     * @property {module:model/RegisterUserChannel}
     */
    RegisterUserChannel,

    /**
     * The ReorderVideoPlaylistRequest model constructor.
     * @property {module:model/ReorderVideoPlaylistRequest}
     */
    ReorderVideoPlaylistRequest,

    /**
     * The RequestTwoFactorResponse model constructor.
     * @property {module:model/RequestTwoFactorResponse}
     */
    RequestTwoFactorResponse,

    /**
     * The RequestTwoFactorResponseOtpRequest model constructor.
     * @property {module:model/RequestTwoFactorResponseOtpRequest}
     */
    RequestTwoFactorResponseOtpRequest,

    /**
     * The ResendEmailToVerifyRegistrationRequest model constructor.
     * @property {module:model/ResendEmailToVerifyRegistrationRequest}
     */
    ResendEmailToVerifyRegistrationRequest,

    /**
     * The ResendEmailToVerifyUserRequest model constructor.
     * @property {module:model/ResendEmailToVerifyUserRequest}
     */
    ResendEmailToVerifyUserRequest,

    /**
     * The SendClientLog model constructor.
     * @property {module:model/SendClientLog}
     */
    SendClientLog,

    /**
     * The ServerConfig model constructor.
     * @property {module:model/ServerConfig}
     */
    ServerConfig,

    /**
     * The ServerConfigAbout model constructor.
     * @property {module:model/ServerConfigAbout}
     */
    ServerConfigAbout,

    /**
     * The ServerConfigAboutInstance model constructor.
     * @property {module:model/ServerConfigAboutInstance}
     */
    ServerConfigAboutInstance,

    /**
     * The ServerConfigAutoBlacklist model constructor.
     * @property {module:model/ServerConfigAutoBlacklist}
     */
    ServerConfigAutoBlacklist,

    /**
     * The ServerConfigAutoBlacklistVideos model constructor.
     * @property {module:model/ServerConfigAutoBlacklistVideos}
     */
    ServerConfigAutoBlacklistVideos,

    /**
     * The ServerConfigAutoBlacklistVideosOfUsers model constructor.
     * @property {module:model/ServerConfigAutoBlacklistVideosOfUsers}
     */
    ServerConfigAutoBlacklistVideosOfUsers,

    /**
     * The ServerConfigAvatar model constructor.
     * @property {module:model/ServerConfigAvatar}
     */
    ServerConfigAvatar,

    /**
     * The ServerConfigAvatarFile model constructor.
     * @property {module:model/ServerConfigAvatarFile}
     */
    ServerConfigAvatarFile,

    /**
     * The ServerConfigAvatarFileSize model constructor.
     * @property {module:model/ServerConfigAvatarFileSize}
     */
    ServerConfigAvatarFileSize,

    /**
     * The ServerConfigCustom model constructor.
     * @property {module:model/ServerConfigCustom}
     */
    ServerConfigCustom,

    /**
     * The ServerConfigCustomAdmin model constructor.
     * @property {module:model/ServerConfigCustomAdmin}
     */
    ServerConfigCustomAdmin,

    /**
     * The ServerConfigCustomCache model constructor.
     * @property {module:model/ServerConfigCustomCache}
     */
    ServerConfigCustomCache,

    /**
     * The ServerConfigCustomCacheCaptions model constructor.
     * @property {module:model/ServerConfigCustomCacheCaptions}
     */
    ServerConfigCustomCacheCaptions,

    /**
     * The ServerConfigCustomFollowers model constructor.
     * @property {module:model/ServerConfigCustomFollowers}
     */
    ServerConfigCustomFollowers,

    /**
     * The ServerConfigCustomFollowersInstance model constructor.
     * @property {module:model/ServerConfigCustomFollowersInstance}
     */
    ServerConfigCustomFollowersInstance,

    /**
     * The ServerConfigCustomImport model constructor.
     * @property {module:model/ServerConfigCustomImport}
     */
    ServerConfigCustomImport,

    /**
     * The ServerConfigCustomInstance model constructor.
     * @property {module:model/ServerConfigCustomInstance}
     */
    ServerConfigCustomInstance,

    /**
     * The ServerConfigCustomServices model constructor.
     * @property {module:model/ServerConfigCustomServices}
     */
    ServerConfigCustomServices,

    /**
     * The ServerConfigCustomServicesTwitter model constructor.
     * @property {module:model/ServerConfigCustomServicesTwitter}
     */
    ServerConfigCustomServicesTwitter,

    /**
     * The ServerConfigCustomSignup model constructor.
     * @property {module:model/ServerConfigCustomSignup}
     */
    ServerConfigCustomSignup,

    /**
     * The ServerConfigCustomTheme model constructor.
     * @property {module:model/ServerConfigCustomTheme}
     */
    ServerConfigCustomTheme,

    /**
     * The ServerConfigCustomTranscoding model constructor.
     * @property {module:model/ServerConfigCustomTranscoding}
     */
    ServerConfigCustomTranscoding,

    /**
     * The ServerConfigCustomTranscodingHls model constructor.
     * @property {module:model/ServerConfigCustomTranscodingHls}
     */
    ServerConfigCustomTranscodingHls,

    /**
     * The ServerConfigCustomTranscodingResolutions model constructor.
     * @property {module:model/ServerConfigCustomTranscodingResolutions}
     */
    ServerConfigCustomTranscodingResolutions,

    /**
     * The ServerConfigCustomTranscodingWebtorrent model constructor.
     * @property {module:model/ServerConfigCustomTranscodingWebtorrent}
     */
    ServerConfigCustomTranscodingWebtorrent,

    /**
     * The ServerConfigCustomUser model constructor.
     * @property {module:model/ServerConfigCustomUser}
     */
    ServerConfigCustomUser,

    /**
     * The ServerConfigFollowings model constructor.
     * @property {module:model/ServerConfigFollowings}
     */
    ServerConfigFollowings,

    /**
     * The ServerConfigFollowingsInstance model constructor.
     * @property {module:model/ServerConfigFollowingsInstance}
     */
    ServerConfigFollowingsInstance,

    /**
     * The ServerConfigFollowingsInstanceAutoFollowIndex model constructor.
     * @property {module:model/ServerConfigFollowingsInstanceAutoFollowIndex}
     */
    ServerConfigFollowingsInstanceAutoFollowIndex,

    /**
     * The ServerConfigImport model constructor.
     * @property {module:model/ServerConfigImport}
     */
    ServerConfigImport,

    /**
     * The ServerConfigImportVideos model constructor.
     * @property {module:model/ServerConfigImportVideos}
     */
    ServerConfigImportVideos,

    /**
     * The ServerConfigInstance model constructor.
     * @property {module:model/ServerConfigInstance}
     */
    ServerConfigInstance,

    /**
     * The ServerConfigInstanceCustomizations model constructor.
     * @property {module:model/ServerConfigInstanceCustomizations}
     */
    ServerConfigInstanceCustomizations,

    /**
     * The ServerConfigPlugin model constructor.
     * @property {module:model/ServerConfigPlugin}
     */
    ServerConfigPlugin,

    /**
     * The ServerConfigSearch model constructor.
     * @property {module:model/ServerConfigSearch}
     */
    ServerConfigSearch,

    /**
     * The ServerConfigSearchRemoteUri model constructor.
     * @property {module:model/ServerConfigSearchRemoteUri}
     */
    ServerConfigSearchRemoteUri,

    /**
     * The ServerConfigSignup model constructor.
     * @property {module:model/ServerConfigSignup}
     */
    ServerConfigSignup,

    /**
     * The ServerConfigTranscoding model constructor.
     * @property {module:model/ServerConfigTranscoding}
     */
    ServerConfigTranscoding,

    /**
     * The ServerConfigTrending model constructor.
     * @property {module:model/ServerConfigTrending}
     */
    ServerConfigTrending,

    /**
     * The ServerConfigTrendingVideos model constructor.
     * @property {module:model/ServerConfigTrendingVideos}
     */
    ServerConfigTrendingVideos,

    /**
     * The ServerConfigUser model constructor.
     * @property {module:model/ServerConfigUser}
     */
    ServerConfigUser,

    /**
     * The ServerConfigVideo model constructor.
     * @property {module:model/ServerConfigVideo}
     */
    ServerConfigVideo,

    /**
     * The ServerConfigVideoCaption model constructor.
     * @property {module:model/ServerConfigVideoCaption}
     */
    ServerConfigVideoCaption,

    /**
     * The ServerConfigVideoFile model constructor.
     * @property {module:model/ServerConfigVideoFile}
     */
    ServerConfigVideoFile,

    /**
     * The ServerConfigVideoImage model constructor.
     * @property {module:model/ServerConfigVideoImage}
     */
    ServerConfigVideoImage,

    /**
     * The ServerStats model constructor.
     * @property {module:model/ServerStats}
     */
    ServerStats,

    /**
     * The ServerStatsVideosRedundancyInner model constructor.
     * @property {module:model/ServerStatsVideosRedundancyInner}
     */
    ServerStatsVideosRedundancyInner,

    /**
     * The UninstallPluginRequest model constructor.
     * @property {module:model/UninstallPluginRequest}
     */
    UninstallPluginRequest,

    /**
     * The UpdateMe model constructor.
     * @property {module:model/UpdateMe}
     */
    UpdateMe,

    /**
     * The UpdateUser model constructor.
     * @property {module:model/UpdateUser}
     */
    UpdateUser,

    /**
     * The User model constructor.
     * @property {module:model/User}
     */
    User,

    /**
     * The UserAdminFlags model constructor.
     * @property {module:model/UserAdminFlags}
     */
    UserAdminFlags,

    /**
     * The UserRegistration model constructor.
     * @property {module:model/UserRegistration}
     */
    UserRegistration,

    /**
     * The UserRegistrationAcceptOrReject model constructor.
     * @property {module:model/UserRegistrationAcceptOrReject}
     */
    UserRegistrationAcceptOrReject,

    /**
     * The UserRegistrationRequest model constructor.
     * @property {module:model/UserRegistrationRequest}
     */
    UserRegistrationRequest,

    /**
     * The UserRegistrationState model constructor.
     * @property {module:model/UserRegistrationState}
     */
    UserRegistrationState,

    /**
     * The UserRegistrationUser model constructor.
     * @property {module:model/UserRegistrationUser}
     */
    UserRegistrationUser,

    /**
     * The UserRole model constructor.
     * @property {module:model/UserRole}
     */
    UserRole,

    /**
     * The UserViewingVideo model constructor.
     * @property {module:model/UserViewingVideo}
     */
    UserViewingVideo,

    /**
     * The UserWithStats model constructor.
     * @property {module:model/UserWithStats}
     */
    UserWithStats,

    /**
     * The VerifyRegistrationEmailRequest model constructor.
     * @property {module:model/VerifyRegistrationEmailRequest}
     */
    VerifyRegistrationEmailRequest,

    /**
     * The VerifyUserRequest model constructor.
     * @property {module:model/VerifyUserRequest}
     */
    VerifyUserRequest,

    /**
     * The Video model constructor.
     * @property {module:model/Video}
     */
    Video,

    /**
     * The VideoBlacklist model constructor.
     * @property {module:model/VideoBlacklist}
     */
    VideoBlacklist,

    /**
     * The VideoCaption model constructor.
     * @property {module:model/VideoCaption}
     */
    VideoCaption,

    /**
     * The VideoChannel model constructor.
     * @property {module:model/VideoChannel}
     */
    VideoChannel,

    /**
     * The VideoChannelAllOfOwnerAccount model constructor.
     * @property {module:model/VideoChannelAllOfOwnerAccount}
     */
    VideoChannelAllOfOwnerAccount,

    /**
     * The VideoChannelCreate model constructor.
     * @property {module:model/VideoChannelCreate}
     */
    VideoChannelCreate,

    /**
     * The VideoChannelEdit model constructor.
     * @property {module:model/VideoChannelEdit}
     */
    VideoChannelEdit,

    /**
     * The VideoChannelList model constructor.
     * @property {module:model/VideoChannelList}
     */
    VideoChannelList,

    /**
     * The VideoChannelListDataInner model constructor.
     * @property {module:model/VideoChannelListDataInner}
     */
    VideoChannelListDataInner,

    /**
     * The VideoChannelSummary model constructor.
     * @property {module:model/VideoChannelSummary}
     */
    VideoChannelSummary,

    /**
     * The VideoChannelSync model constructor.
     * @property {module:model/VideoChannelSync}
     */
    VideoChannelSync,

    /**
     * The VideoChannelSyncCreate model constructor.
     * @property {module:model/VideoChannelSyncCreate}
     */
    VideoChannelSyncCreate,

    /**
     * The VideoChannelSyncList model constructor.
     * @property {module:model/VideoChannelSyncList}
     */
    VideoChannelSyncList,

    /**
     * The VideoChannelSyncState model constructor.
     * @property {module:model/VideoChannelSyncState}
     */
    VideoChannelSyncState,

    /**
     * The VideoChannelUpdate model constructor.
     * @property {module:model/VideoChannelUpdate}
     */
    VideoChannelUpdate,

    /**
     * The VideoComment model constructor.
     * @property {module:model/VideoComment}
     */
    VideoComment,

    /**
     * The VideoCommentThreadTree model constructor.
     * @property {module:model/VideoCommentThreadTree}
     */
    VideoCommentThreadTree,

    /**
     * The VideoCommentsForXMLInner model constructor.
     * @property {module:model/VideoCommentsForXMLInner}
     */
    VideoCommentsForXMLInner,

    /**
     * The VideoConstantNumberCategory model constructor.
     * @property {module:model/VideoConstantNumberCategory}
     */
    VideoConstantNumberCategory,

    /**
     * The VideoConstantNumberLicence model constructor.
     * @property {module:model/VideoConstantNumberLicence}
     */
    VideoConstantNumberLicence,

    /**
     * The VideoConstantStringLanguage model constructor.
     * @property {module:model/VideoConstantStringLanguage}
     */
    VideoConstantStringLanguage,

    /**
     * The VideoDetails model constructor.
     * @property {module:model/VideoDetails}
     */
    VideoDetails,

    /**
     * The VideoFile model constructor.
     * @property {module:model/VideoFile}
     */
    VideoFile,

    /**
     * The VideoImport model constructor.
     * @property {module:model/VideoImport}
     */
    VideoImport,

    /**
     * The VideoImportStateConstant model constructor.
     * @property {module:model/VideoImportStateConstant}
     */
    VideoImportStateConstant,

    /**
     * The VideoImportsList model constructor.
     * @property {module:model/VideoImportsList}
     */
    VideoImportsList,

    /**
     * The VideoInfo model constructor.
     * @property {module:model/VideoInfo}
     */
    VideoInfo,

    /**
     * The VideoListResponse model constructor.
     * @property {module:model/VideoListResponse}
     */
    VideoListResponse,

    /**
     * The VideoPlaylist model constructor.
     * @property {module:model/VideoPlaylist}
     */
    VideoPlaylist,

    /**
     * The VideoPlaylistPrivacyConstant model constructor.
     * @property {module:model/VideoPlaylistPrivacyConstant}
     */
    VideoPlaylistPrivacyConstant,

    /**
     * The VideoPlaylistPrivacySet model constructor.
     * @property {module:model/VideoPlaylistPrivacySet}
     */
    VideoPlaylistPrivacySet,

    /**
     * The VideoPlaylistTypeConstant model constructor.
     * @property {module:model/VideoPlaylistTypeConstant}
     */
    VideoPlaylistTypeConstant,

    /**
     * The VideoPlaylistTypeSet model constructor.
     * @property {module:model/VideoPlaylistTypeSet}
     */
    VideoPlaylistTypeSet,

    /**
     * The VideoPrivacyConstant model constructor.
     * @property {module:model/VideoPrivacyConstant}
     */
    VideoPrivacyConstant,

    /**
     * The VideoPrivacySet model constructor.
     * @property {module:model/VideoPrivacySet}
     */
    VideoPrivacySet,

    /**
     * The VideoRating model constructor.
     * @property {module:model/VideoRating}
     */
    VideoRating,

    /**
     * The VideoRedundancy model constructor.
     * @property {module:model/VideoRedundancy}
     */
    VideoRedundancy,

    /**
     * The VideoRedundancyRedundancies model constructor.
     * @property {module:model/VideoRedundancyRedundancies}
     */
    VideoRedundancyRedundancies,

    /**
     * The VideoResolutionConstant model constructor.
     * @property {module:model/VideoResolutionConstant}
     */
    VideoResolutionConstant,

    /**
     * The VideoScheduledUpdate model constructor.
     * @property {module:model/VideoScheduledUpdate}
     */
    VideoScheduledUpdate,

    /**
     * The VideoSource model constructor.
     * @property {module:model/VideoSource}
     */
    VideoSource,

    /**
     * The VideoStateConstant model constructor.
     * @property {module:model/VideoStateConstant}
     */
    VideoStateConstant,

    /**
     * The VideoStatsOverall model constructor.
     * @property {module:model/VideoStatsOverall}
     */
    VideoStatsOverall,

    /**
     * The VideoStatsOverallCountriesInner model constructor.
     * @property {module:model/VideoStatsOverallCountriesInner}
     */
    VideoStatsOverallCountriesInner,

    /**
     * The VideoStatsRetention model constructor.
     * @property {module:model/VideoStatsRetention}
     */
    VideoStatsRetention,

    /**
     * The VideoStatsRetentionDataInner model constructor.
     * @property {module:model/VideoStatsRetentionDataInner}
     */
    VideoStatsRetentionDataInner,

    /**
     * The VideoStatsTimeserie model constructor.
     * @property {module:model/VideoStatsTimeserie}
     */
    VideoStatsTimeserie,

    /**
     * The VideoStatsTimeserieDataInner model constructor.
     * @property {module:model/VideoStatsTimeserieDataInner}
     */
    VideoStatsTimeserieDataInner,

    /**
     * The VideoStreamingPlaylists model constructor.
     * @property {module:model/VideoStreamingPlaylists}
     */
    VideoStreamingPlaylists,

    /**
     * The VideoStreamingPlaylistsHLS model constructor.
     * @property {module:model/VideoStreamingPlaylistsHLS}
     */
    VideoStreamingPlaylistsHLS,

    /**
     * The VideoStreamingPlaylistsHLSRedundanciesInner model constructor.
     * @property {module:model/VideoStreamingPlaylistsHLSRedundanciesInner}
     */
    VideoStreamingPlaylistsHLSRedundanciesInner,

    /**
     * The VideoTokenResponse model constructor.
     * @property {module:model/VideoTokenResponse}
     */
    VideoTokenResponse,

    /**
     * The VideoTokenResponseFiles model constructor.
     * @property {module:model/VideoTokenResponseFiles}
     */
    VideoTokenResponseFiles,

    /**
     * The VideoUploadRequestCommon model constructor.
     * @property {module:model/VideoUploadRequestCommon}
     */
    VideoUploadRequestCommon,

    /**
     * The VideoUploadRequestResumable model constructor.
     * @property {module:model/VideoUploadRequestResumable}
     */
    VideoUploadRequestResumable,

    /**
     * The VideoUploadResponse model constructor.
     * @property {module:model/VideoUploadResponse}
     */
    VideoUploadResponse,

    /**
     * The VideoUploadResponseVideo model constructor.
     * @property {module:model/VideoUploadResponseVideo}
     */
    VideoUploadResponseVideo,

    /**
     * The VideoUserHistory model constructor.
     * @property {module:model/VideoUserHistory}
     */
    VideoUserHistory,

    /**
     * The VideosForXMLInner model constructor.
     * @property {module:model/VideosForXMLInner}
     */
    VideosForXMLInner,

    /**
     * The VideosForXMLInnerEnclosure model constructor.
     * @property {module:model/VideosForXMLInnerEnclosure}
     */
    VideosForXMLInnerEnclosure,

    /**
     * The VideosForXMLInnerMediaCommunity model constructor.
     * @property {module:model/VideosForXMLInnerMediaCommunity}
     */
    VideosForXMLInnerMediaCommunity,

    /**
     * The VideosForXMLInnerMediaCommunityMediaStatistics model constructor.
     * @property {module:model/VideosForXMLInnerMediaCommunityMediaStatistics}
     */
    VideosForXMLInnerMediaCommunityMediaStatistics,

    /**
     * The VideosForXMLInnerMediaEmbed model constructor.
     * @property {module:model/VideosForXMLInnerMediaEmbed}
     */
    VideosForXMLInnerMediaEmbed,

    /**
     * The VideosForXMLInnerMediaGroupInner model constructor.
     * @property {module:model/VideosForXMLInnerMediaGroupInner}
     */
    VideosForXMLInnerMediaGroupInner,

    /**
     * The VideosForXMLInnerMediaPlayer model constructor.
     * @property {module:model/VideosForXMLInnerMediaPlayer}
     */
    VideosForXMLInnerMediaPlayer,

    /**
     * The VideosForXMLInnerMediaThumbnail model constructor.
     * @property {module:model/VideosForXMLInnerMediaThumbnail}
     */
    VideosForXMLInnerMediaThumbnail,

    /**
    * The AbusesApi service constructor.
    * @property {module:api/AbusesApi}
    */
    AbusesApi,

    /**
    * The AccountBlocksApi service constructor.
    * @property {module:api/AccountBlocksApi}
    */
    AccountBlocksApi,

    /**
    * The AccountsApi service constructor.
    * @property {module:api/AccountsApi}
    */
    AccountsApi,

    /**
    * The ChannelsSyncApi service constructor.
    * @property {module:api/ChannelsSyncApi}
    */
    ChannelsSyncApi,

    /**
    * The ConfigApi service constructor.
    * @property {module:api/ConfigApi}
    */
    ConfigApi,

    /**
    * The HomepageApi service constructor.
    * @property {module:api/HomepageApi}
    */
    HomepageApi,

    /**
    * The InstanceFollowsApi service constructor.
    * @property {module:api/InstanceFollowsApi}
    */
    InstanceFollowsApi,

    /**
    * The InstanceRedundancyApi service constructor.
    * @property {module:api/InstanceRedundancyApi}
    */
    InstanceRedundancyApi,

    /**
    * The JobApi service constructor.
    * @property {module:api/JobApi}
    */
    JobApi,

    /**
    * The LiveVideosApi service constructor.
    * @property {module:api/LiveVideosApi}
    */
    LiveVideosApi,

    /**
    * The LogsApi service constructor.
    * @property {module:api/LogsApi}
    */
    LogsApi,

    /**
    * The MyHistoryApi service constructor.
    * @property {module:api/MyHistoryApi}
    */
    MyHistoryApi,

    /**
    * The MyNotificationsApi service constructor.
    * @property {module:api/MyNotificationsApi}
    */
    MyNotificationsApi,

    /**
    * The MySubscriptionsApi service constructor.
    * @property {module:api/MySubscriptionsApi}
    */
    MySubscriptionsApi,

    /**
    * The MyUserApi service constructor.
    * @property {module:api/MyUserApi}
    */
    MyUserApi,

    /**
    * The PluginsApi service constructor.
    * @property {module:api/PluginsApi}
    */
    PluginsApi,

    /**
    * The RegisterApi service constructor.
    * @property {module:api/RegisterApi}
    */
    RegisterApi,

    /**
    * The SearchApi service constructor.
    * @property {module:api/SearchApi}
    */
    SearchApi,

    /**
    * The ServerBlocksApi service constructor.
    * @property {module:api/ServerBlocksApi}
    */
    ServerBlocksApi,

    /**
    * The SessionApi service constructor.
    * @property {module:api/SessionApi}
    */
    SessionApi,

    /**
    * The StaticVideoFilesApi service constructor.
    * @property {module:api/StaticVideoFilesApi}
    */
    StaticVideoFilesApi,

    /**
    * The StatsApi service constructor.
    * @property {module:api/StatsApi}
    */
    StatsApi,

    /**
    * The UsersApi service constructor.
    * @property {module:api/UsersApi}
    */
    UsersApi,

    /**
    * The VideoApi service constructor.
    * @property {module:api/VideoApi}
    */
    VideoApi,

    /**
    * The VideoBlocksApi service constructor.
    * @property {module:api/VideoBlocksApi}
    */
    VideoBlocksApi,

    /**
    * The VideoCaptionsApi service constructor.
    * @property {module:api/VideoCaptionsApi}
    */
    VideoCaptionsApi,

    /**
    * The VideoChannelsApi service constructor.
    * @property {module:api/VideoChannelsApi}
    */
    VideoChannelsApi,

    /**
    * The VideoCommentsApi service constructor.
    * @property {module:api/VideoCommentsApi}
    */
    VideoCommentsApi,

    /**
    * The VideoFeedsApi service constructor.
    * @property {module:api/VideoFeedsApi}
    */
    VideoFeedsApi,

    /**
    * The VideoFilesApi service constructor.
    * @property {module:api/VideoFilesApi}
    */
    VideoFilesApi,

    /**
    * The VideoImportsApi service constructor.
    * @property {module:api/VideoImportsApi}
    */
    VideoImportsApi,

    /**
    * The VideoMirroringApi service constructor.
    * @property {module:api/VideoMirroringApi}
    */
    VideoMirroringApi,

    /**
    * The VideoOwnershipChangeApi service constructor.
    * @property {module:api/VideoOwnershipChangeApi}
    */
    VideoOwnershipChangeApi,

    /**
    * The VideoPlaylistsApi service constructor.
    * @property {module:api/VideoPlaylistsApi}
    */
    VideoPlaylistsApi,

    /**
    * The VideoRatesApi service constructor.
    * @property {module:api/VideoRatesApi}
    */
    VideoRatesApi,

    /**
    * The VideoStatsApi service constructor.
    * @property {module:api/VideoStatsApi}
    */
    VideoStatsApi,

    /**
    * The VideoTranscodingApi service constructor.
    * @property {module:api/VideoTranscodingApi}
    */
    VideoTranscodingApi,

    /**
    * The VideoUploadApi service constructor.
    * @property {module:api/VideoUploadApi}
    */
    VideoUploadApi,

    /**
    * The VideosApi service constructor.
    * @property {module:api/VideosApi}
    */
    VideosApi
};
