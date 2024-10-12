/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIVideoChannelsApi_H
#define OAI_OAIVideoChannelsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddVideoChannel_200_response.h"
#include "OAIGetAccountFollowers_200_response.h"
#include "OAIGetAccountVideos_categoryOneOf_parameter.h"
#include "OAIGetAccountVideos_languageOneOf_parameter.h"
#include "OAIGetAccountVideos_licenceOneOf_parameter.h"
#include "OAIGetAccountVideos_tagsAllOf_parameter.h"
#include "OAIGetAccountVideos_tagsOneOf_parameter.h"
#include "OAIHttpFileElement.h"
#include "OAIImportVideosInChannelCreate.h"
#include "OAIVideoChannel.h"
#include "OAIVideoChannelCreate.h"
#include "OAIVideoChannelList.h"
#include "OAIVideoChannelSyncList.h"
#include "OAIVideoChannelUpdate.h"
#include "OAIVideoListResponse.h"
#include "OAIVideoPlaylistTypeSet.h"
#include "OAIVideoPrivacySet.h"
#include "OAI_api_v1_accounts__name__video_playlists_get_200_response.h"
#include "OAI_api_v1_users_me_avatar_pick_post_200_response.h"
#include "OAI_api_v1_video_channels__channelHandle__banner_pick_post_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVideoChannelsApi : public QObject {
    Q_OBJECT

public:
    OAIVideoChannelsApi(const int timeOut = 0);
    ~OAIVideoChannelsApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  oai_video_channel_create OAIVideoChannelCreate [optional]
    */
    virtual void addVideoChannel(const ::OpenAPI::OptionalParam<OAIVideoChannelCreate> &oai_video_channel_create = ::OpenAPI::OptionalParam<OAIVideoChannelCreate>());

    /**
    * @param[in]  name QString [required]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void apiV1AccountsNameVideoChannelSyncsGet(const QString &name, const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  name QString [required]
    * @param[in]  with_stats bool [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void apiV1AccountsNameVideoChannelsGet(const QString &name, const ::OpenAPI::OptionalParam<bool> &with_stats = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  channel_handle QString [required]
    */
    virtual void apiV1VideoChannelsChannelHandleAvatarDelete(const QString &channel_handle);

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  avatarfile OAIHttpFileElement [optional]
    */
    virtual void apiV1VideoChannelsChannelHandleAvatarPickPost(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &avatarfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>());

    /**
    * @param[in]  channel_handle QString [required]
    */
    virtual void apiV1VideoChannelsChannelHandleBannerDelete(const QString &channel_handle);

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  bannerfile OAIHttpFileElement [optional]
    */
    virtual void apiV1VideoChannelsChannelHandleBannerPickPost(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &bannerfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>());

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  oai_import_videos_in_channel_create OAIImportVideosInChannelCreate [optional]
    */
    virtual void apiV1VideoChannelsChannelHandleImportVideosPost(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIImportVideosInChannelCreate> &oai_import_videos_in_channel_create = ::OpenAPI::OptionalParam<OAIImportVideosInChannelCreate>());

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  playlist_type OAIVideoPlaylistTypeSet [optional]
    */
    virtual void apiV1VideoChannelsChannelHandleVideoPlaylistsGet(const QString &channel_handle, const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet> &playlist_type = ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet>());

    /**
    * @param[in]  channel_handle QString [required]
    */
    virtual void delVideoChannel(const QString &channel_handle);

    /**
    * @param[in]  channel_handle QString [required]
    */
    virtual void getVideoChannel(const QString &channel_handle);

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  search QString [optional]
    */
    virtual void getVideoChannelFollowers(const QString &channel_handle, const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  category_one_of OAIGetAccountVideos_categoryOneOf_parameter [optional]
    * @param[in]  is_live bool [optional]
    * @param[in]  tags_one_of OAIGetAccountVideos_tagsOneOf_parameter [optional]
    * @param[in]  tags_all_of OAIGetAccountVideos_tagsAllOf_parameter [optional]
    * @param[in]  licence_one_of OAIGetAccountVideos_licenceOneOf_parameter [optional]
    * @param[in]  language_one_of OAIGetAccountVideos_languageOneOf_parameter [optional]
    * @param[in]  nsfw QString [optional]
    * @param[in]  is_local bool [optional]
    * @param[in]  include qint32 [optional]
    * @param[in]  privacy_one_of OAIVideoPrivacySet [optional]
    * @param[in]  has_hls_files bool [optional]
    * @param[in]  has_webtorrent_files bool [optional]
    * @param[in]  skip_count QString [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  exclude_already_watched bool [optional]
    */
    virtual void getVideoChannelVideos(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter> &category_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter>(), const ::OpenAPI::OptionalParam<bool> &is_live = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter> &tags_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter> &tags_all_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter> &licence_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter> &language_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter>(), const ::OpenAPI::OptionalParam<QString> &nsfw = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &is_local = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &include = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy_one_of = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<bool> &has_hls_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &has_webtorrent_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &skip_count = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &exclude_already_watched = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getVideoChannels(const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  oai_video_channel_update OAIVideoChannelUpdate [optional]
    */
    virtual void putVideoChannel(const QString &channel_handle, const ::OpenAPI::OptionalParam<OAIVideoChannelUpdate> &oai_video_channel_update = ::OpenAPI::OptionalParam<OAIVideoChannelUpdate>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void addVideoChannelCallback(OAIHttpRequestWorker *worker);
    void apiV1AccountsNameVideoChannelSyncsGetCallback(OAIHttpRequestWorker *worker);
    void apiV1AccountsNameVideoChannelsGetCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleAvatarDeleteCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleAvatarPickPostCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleBannerDeleteCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleBannerPickPostCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleImportVideosPostCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetCallback(OAIHttpRequestWorker *worker);
    void delVideoChannelCallback(OAIHttpRequestWorker *worker);
    void getVideoChannelCallback(OAIHttpRequestWorker *worker);
    void getVideoChannelFollowersCallback(OAIHttpRequestWorker *worker);
    void getVideoChannelVideosCallback(OAIHttpRequestWorker *worker);
    void getVideoChannelsCallback(OAIHttpRequestWorker *worker);
    void putVideoChannelCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addVideoChannelSignal(OAIAddVideoChannel_200_response summary);
    void apiV1AccountsNameVideoChannelSyncsGetSignal(OAIVideoChannelSyncList summary);
    void apiV1AccountsNameVideoChannelsGetSignal(OAIVideoChannelList summary);
    void apiV1VideoChannelsChannelHandleAvatarDeleteSignal();
    void apiV1VideoChannelsChannelHandleAvatarPickPostSignal(OAI_api_v1_users_me_avatar_pick_post_200_response summary);
    void apiV1VideoChannelsChannelHandleBannerDeleteSignal();
    void apiV1VideoChannelsChannelHandleBannerPickPostSignal(OAI_api_v1_video_channels__channelHandle__banner_pick_post_200_response summary);
    void apiV1VideoChannelsChannelHandleImportVideosPostSignal();
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignal(OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void delVideoChannelSignal();
    void getVideoChannelSignal(OAIVideoChannel summary);
    void getVideoChannelFollowersSignal(OAIGetAccountFollowers_200_response summary);
    void getVideoChannelVideosSignal(OAIVideoListResponse summary);
    void getVideoChannelsSignal(OAIVideoChannelList summary);
    void putVideoChannelSignal();


    void addVideoChannelSignalFull(OAIHttpRequestWorker *worker, OAIAddVideoChannel_200_response summary);
    void apiV1AccountsNameVideoChannelSyncsGetSignalFull(OAIHttpRequestWorker *worker, OAIVideoChannelSyncList summary);
    void apiV1AccountsNameVideoChannelsGetSignalFull(OAIHttpRequestWorker *worker, OAIVideoChannelList summary);
    void apiV1VideoChannelsChannelHandleAvatarDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleAvatarPickPostSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_users_me_avatar_pick_post_200_response summary);
    void apiV1VideoChannelsChannelHandleBannerDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleBannerPickPostSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_video_channels__channelHandle__banner_pick_post_200_response summary);
    void apiV1VideoChannelsChannelHandleImportVideosPostSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void delVideoChannelSignalFull(OAIHttpRequestWorker *worker);
    void getVideoChannelSignalFull(OAIHttpRequestWorker *worker, OAIVideoChannel summary);
    void getVideoChannelFollowersSignalFull(OAIHttpRequestWorker *worker, OAIGetAccountFollowers_200_response summary);
    void getVideoChannelVideosSignalFull(OAIHttpRequestWorker *worker, OAIVideoListResponse summary);
    void getVideoChannelsSignalFull(OAIHttpRequestWorker *worker, OAIVideoChannelList summary);
    void putVideoChannelSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use addVideoChannelSignalError() instead")
    void addVideoChannelSignalE(OAIAddVideoChannel_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addVideoChannelSignalError(OAIAddVideoChannel_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AccountsNameVideoChannelSyncsGetSignalError() instead")
    void apiV1AccountsNameVideoChannelSyncsGetSignalE(OAIVideoChannelSyncList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AccountsNameVideoChannelSyncsGetSignalError(OAIVideoChannelSyncList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AccountsNameVideoChannelsGetSignalError() instead")
    void apiV1AccountsNameVideoChannelsGetSignalE(OAIVideoChannelList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AccountsNameVideoChannelsGetSignalError(OAIVideoChannelList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleAvatarDeleteSignalError() instead")
    void apiV1VideoChannelsChannelHandleAvatarDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleAvatarDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleAvatarPickPostSignalError() instead")
    void apiV1VideoChannelsChannelHandleAvatarPickPostSignalE(OAI_api_v1_users_me_avatar_pick_post_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleAvatarPickPostSignalError(OAI_api_v1_users_me_avatar_pick_post_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleBannerDeleteSignalError() instead")
    void apiV1VideoChannelsChannelHandleBannerDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleBannerDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleBannerPickPostSignalError() instead")
    void apiV1VideoChannelsChannelHandleBannerPickPostSignalE(OAI_api_v1_video_channels__channelHandle__banner_pick_post_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleBannerPickPostSignalError(OAI_api_v1_video_channels__channelHandle__banner_pick_post_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleImportVideosPostSignalError() instead")
    void apiV1VideoChannelsChannelHandleImportVideosPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleImportVideosPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalError() instead")
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalE(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalError(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delVideoChannelSignalError() instead")
    void delVideoChannelSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void delVideoChannelSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelSignalError() instead")
    void getVideoChannelSignalE(OAIVideoChannel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelSignalError(OAIVideoChannel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelFollowersSignalError() instead")
    void getVideoChannelFollowersSignalE(OAIGetAccountFollowers_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelFollowersSignalError(OAIGetAccountFollowers_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelVideosSignalError() instead")
    void getVideoChannelVideosSignalE(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelVideosSignalError(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelsSignalError() instead")
    void getVideoChannelsSignalE(OAIVideoChannelList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelsSignalError(OAIVideoChannelList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putVideoChannelSignalError() instead")
    void putVideoChannelSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void putVideoChannelSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addVideoChannelSignalErrorFull() instead")
    void addVideoChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addVideoChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AccountsNameVideoChannelSyncsGetSignalErrorFull() instead")
    void apiV1AccountsNameVideoChannelSyncsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AccountsNameVideoChannelSyncsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AccountsNameVideoChannelsGetSignalErrorFull() instead")
    void apiV1AccountsNameVideoChannelsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AccountsNameVideoChannelsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleAvatarDeleteSignalErrorFull() instead")
    void apiV1VideoChannelsChannelHandleAvatarDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleAvatarDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleAvatarPickPostSignalErrorFull() instead")
    void apiV1VideoChannelsChannelHandleAvatarPickPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleAvatarPickPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleBannerDeleteSignalErrorFull() instead")
    void apiV1VideoChannelsChannelHandleBannerDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleBannerDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleBannerPickPostSignalErrorFull() instead")
    void apiV1VideoChannelsChannelHandleBannerPickPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleBannerPickPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleImportVideosPostSignalErrorFull() instead")
    void apiV1VideoChannelsChannelHandleImportVideosPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleImportVideosPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalErrorFull() instead")
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delVideoChannelSignalErrorFull() instead")
    void delVideoChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void delVideoChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelSignalErrorFull() instead")
    void getVideoChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelFollowersSignalErrorFull() instead")
    void getVideoChannelFollowersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelFollowersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelVideosSignalErrorFull() instead")
    void getVideoChannelVideosSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelVideosSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelsSignalErrorFull() instead")
    void getVideoChannelsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putVideoChannelSignalErrorFull() instead")
    void putVideoChannelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putVideoChannelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
