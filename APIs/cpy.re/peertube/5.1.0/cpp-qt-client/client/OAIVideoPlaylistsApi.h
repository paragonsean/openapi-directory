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

#ifndef OAI_OAIVideoPlaylistsApi_H
#define OAI_OAIVideoPlaylistsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddPlaylist_200_response.h"
#include "OAIAddVideoPlaylistVideo_200_response.h"
#include "OAIAddVideoPlaylistVideo_request.h"
#include "OAIHttpFileElement.h"
#include "OAIPutVideoPlaylistVideo_request.h"
#include "OAIReorderVideoPlaylist_request.h"
#include "OAIVideoListResponse.h"
#include "OAIVideoPlaylist.h"
#include "OAIVideoPlaylistPrivacySet.h"
#include "OAIVideoPlaylistTypeSet.h"
#include "OAI_api_v1_accounts__name__video_playlists_get_200_response.h"
#include "OAI_api_v1_users_me_video_playlists_videos_exist_get_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVideoPlaylistsApi : public QObject {
    Q_OBJECT

public:
    OAIVideoPlaylistsApi(const int timeOut = 0);
    ~OAIVideoPlaylistsApi();

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
    * @param[in]  display_name QString [required]
    * @param[in]  description QString [optional]
    * @param[in]  privacy OAIVideoPlaylistPrivacySet [optional]
    * @param[in]  thumbnailfile OAIHttpFileElement [optional]
    * @param[in]  video_channel_id qint32 [optional]
    */
    virtual void addPlaylist(const QString &display_name, const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIVideoPlaylistPrivacySet> &privacy = ::OpenAPI::OptionalParam<OAIVideoPlaylistPrivacySet>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &thumbnailfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<qint32> &video_channel_id = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  playlist_id qint32 [required]
    * @param[in]  oai_add_video_playlist_video_request OAIAddVideoPlaylistVideo_request [optional]
    */
    virtual void addVideoPlaylistVideo(const qint32 &playlist_id, const ::OpenAPI::OptionalParam<OAIAddVideoPlaylistVideo_request> &oai_add_video_playlist_video_request = ::OpenAPI::OptionalParam<OAIAddVideoPlaylistVideo_request>());

    /**
    * @param[in]  name QString [required]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  search QString [optional]
    * @param[in]  playlist_type OAIVideoPlaylistTypeSet [optional]
    */
    virtual void apiV1AccountsNameVideoPlaylistsGet(const QString &name, const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet> &playlist_type = ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet>());

    /**
    * @param[in]  video_ids QList<qint32> [required]
    */
    virtual void apiV1UsersMeVideoPlaylistsVideosExistGet(const QList<qint32> &video_ids);

    /**
    * @param[in]  channel_handle QString [required]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  playlist_type OAIVideoPlaylistTypeSet [optional]
    */
    virtual void apiV1VideoChannelsChannelHandleVideoPlaylistsGet(const QString &channel_handle, const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet> &playlist_type = ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet>());

    /**
    * @param[in]  playlist_id qint32 [required]
    */
    virtual void apiV1VideoPlaylistsPlaylistIdDelete(const qint32 &playlist_id);

    /**
    * @param[in]  playlist_id qint32 [required]
    */
    virtual void apiV1VideoPlaylistsPlaylistIdGet(const qint32 &playlist_id);

    /**
    * @param[in]  playlist_id qint32 [required]
    * @param[in]  description QString [optional]
    * @param[in]  display_name QString [optional]
    * @param[in]  privacy OAIVideoPlaylistPrivacySet [optional]
    * @param[in]  thumbnailfile OAIHttpFileElement [optional]
    * @param[in]  video_channel_id qint32 [optional]
    */
    virtual void apiV1VideoPlaylistsPlaylistIdPut(const qint32 &playlist_id, const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &display_name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIVideoPlaylistPrivacySet> &privacy = ::OpenAPI::OptionalParam<OAIVideoPlaylistPrivacySet>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &thumbnailfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<qint32> &video_channel_id = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  playlist_id qint32 [required]
    * @param[in]  playlist_element_id qint32 [required]
    */
    virtual void delVideoPlaylistVideo(const qint32 &playlist_id, const qint32 &playlist_element_id);


    virtual void getPlaylistPrivacyPolicies();

    /**
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  playlist_type OAIVideoPlaylistTypeSet [optional]
    */
    virtual void getPlaylists(const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet> &playlist_type = ::OpenAPI::OptionalParam<OAIVideoPlaylistTypeSet>());

    /**
    * @param[in]  playlist_id qint32 [required]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    */
    virtual void getVideoPlaylistVideos(const qint32 &playlist_id, const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  playlist_id qint32 [required]
    * @param[in]  playlist_element_id qint32 [required]
    * @param[in]  oai_put_video_playlist_video_request OAIPutVideoPlaylistVideo_request [optional]
    */
    virtual void putVideoPlaylistVideo(const qint32 &playlist_id, const qint32 &playlist_element_id, const ::OpenAPI::OptionalParam<OAIPutVideoPlaylistVideo_request> &oai_put_video_playlist_video_request = ::OpenAPI::OptionalParam<OAIPutVideoPlaylistVideo_request>());

    /**
    * @param[in]  playlist_id qint32 [required]
    * @param[in]  oai_reorder_video_playlist_request OAIReorderVideoPlaylist_request [optional]
    */
    virtual void reorderVideoPlaylist(const qint32 &playlist_id, const ::OpenAPI::OptionalParam<OAIReorderVideoPlaylist_request> &oai_reorder_video_playlist_request = ::OpenAPI::OptionalParam<OAIReorderVideoPlaylist_request>());


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

    void addPlaylistCallback(OAIHttpRequestWorker *worker);
    void addVideoPlaylistVideoCallback(OAIHttpRequestWorker *worker);
    void apiV1AccountsNameVideoPlaylistsGetCallback(OAIHttpRequestWorker *worker);
    void apiV1UsersMeVideoPlaylistsVideosExistGetCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoPlaylistsPlaylistIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoPlaylistsPlaylistIdGetCallback(OAIHttpRequestWorker *worker);
    void apiV1VideoPlaylistsPlaylistIdPutCallback(OAIHttpRequestWorker *worker);
    void delVideoPlaylistVideoCallback(OAIHttpRequestWorker *worker);
    void getPlaylistPrivacyPoliciesCallback(OAIHttpRequestWorker *worker);
    void getPlaylistsCallback(OAIHttpRequestWorker *worker);
    void getVideoPlaylistVideosCallback(OAIHttpRequestWorker *worker);
    void putVideoPlaylistVideoCallback(OAIHttpRequestWorker *worker);
    void reorderVideoPlaylistCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addPlaylistSignal(OAIAddPlaylist_200_response summary);
    void addVideoPlaylistVideoSignal(OAIAddVideoPlaylistVideo_200_response summary);
    void apiV1AccountsNameVideoPlaylistsGetSignal(OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void apiV1UsersMeVideoPlaylistsVideosExistGetSignal(OAI_api_v1_users_me_video_playlists_videos_exist_get_200_response summary);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignal(OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void apiV1VideoPlaylistsPlaylistIdDeleteSignal();
    void apiV1VideoPlaylistsPlaylistIdGetSignal(OAIVideoPlaylist summary);
    void apiV1VideoPlaylistsPlaylistIdPutSignal();
    void delVideoPlaylistVideoSignal();
    void getPlaylistPrivacyPoliciesSignal(QList<QString> summary);
    void getPlaylistsSignal(OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void getVideoPlaylistVideosSignal(OAIVideoListResponse summary);
    void putVideoPlaylistVideoSignal();
    void reorderVideoPlaylistSignal();


    void addPlaylistSignalFull(OAIHttpRequestWorker *worker, OAIAddPlaylist_200_response summary);
    void addVideoPlaylistVideoSignalFull(OAIHttpRequestWorker *worker, OAIAddVideoPlaylistVideo_200_response summary);
    void apiV1AccountsNameVideoPlaylistsGetSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void apiV1UsersMeVideoPlaylistsVideosExistGetSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_users_me_video_playlists_videos_exist_get_200_response summary);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void apiV1VideoPlaylistsPlaylistIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VideoPlaylistsPlaylistIdGetSignalFull(OAIHttpRequestWorker *worker, OAIVideoPlaylist summary);
    void apiV1VideoPlaylistsPlaylistIdPutSignalFull(OAIHttpRequestWorker *worker);
    void delVideoPlaylistVideoSignalFull(OAIHttpRequestWorker *worker);
    void getPlaylistPrivacyPoliciesSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void getPlaylistsSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_accounts__name__video_playlists_get_200_response summary);
    void getVideoPlaylistVideosSignalFull(OAIHttpRequestWorker *worker, OAIVideoListResponse summary);
    void putVideoPlaylistVideoSignalFull(OAIHttpRequestWorker *worker);
    void reorderVideoPlaylistSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use addPlaylistSignalError() instead")
    void addPlaylistSignalE(OAIAddPlaylist_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addPlaylistSignalError(OAIAddPlaylist_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addVideoPlaylistVideoSignalError() instead")
    void addVideoPlaylistVideoSignalE(OAIAddVideoPlaylistVideo_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addVideoPlaylistVideoSignalError(OAIAddVideoPlaylistVideo_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AccountsNameVideoPlaylistsGetSignalError() instead")
    void apiV1AccountsNameVideoPlaylistsGetSignalE(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AccountsNameVideoPlaylistsGetSignalError(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeVideoPlaylistsVideosExistGetSignalError() instead")
    void apiV1UsersMeVideoPlaylistsVideosExistGetSignalE(OAI_api_v1_users_me_video_playlists_videos_exist_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeVideoPlaylistsVideosExistGetSignalError(OAI_api_v1_users_me_video_playlists_videos_exist_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalError() instead")
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalE(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalError(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoPlaylistsPlaylistIdDeleteSignalError() instead")
    void apiV1VideoPlaylistsPlaylistIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoPlaylistsPlaylistIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoPlaylistsPlaylistIdGetSignalError() instead")
    void apiV1VideoPlaylistsPlaylistIdGetSignalE(OAIVideoPlaylist summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoPlaylistsPlaylistIdGetSignalError(OAIVideoPlaylist summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoPlaylistsPlaylistIdPutSignalError() instead")
    void apiV1VideoPlaylistsPlaylistIdPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoPlaylistsPlaylistIdPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delVideoPlaylistVideoSignalError() instead")
    void delVideoPlaylistVideoSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void delVideoPlaylistVideoSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlaylistPrivacyPoliciesSignalError() instead")
    void getPlaylistPrivacyPoliciesSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPlaylistPrivacyPoliciesSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlaylistsSignalError() instead")
    void getPlaylistsSignalE(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPlaylistsSignalError(OAI_api_v1_accounts__name__video_playlists_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoPlaylistVideosSignalError() instead")
    void getVideoPlaylistVideosSignalE(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoPlaylistVideosSignalError(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putVideoPlaylistVideoSignalError() instead")
    void putVideoPlaylistVideoSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void putVideoPlaylistVideoSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reorderVideoPlaylistSignalError() instead")
    void reorderVideoPlaylistSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void reorderVideoPlaylistSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addPlaylistSignalErrorFull() instead")
    void addPlaylistSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addPlaylistSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addVideoPlaylistVideoSignalErrorFull() instead")
    void addVideoPlaylistVideoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addVideoPlaylistVideoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AccountsNameVideoPlaylistsGetSignalErrorFull() instead")
    void apiV1AccountsNameVideoPlaylistsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AccountsNameVideoPlaylistsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeVideoPlaylistsVideosExistGetSignalErrorFull() instead")
    void apiV1UsersMeVideoPlaylistsVideosExistGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeVideoPlaylistsVideosExistGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalErrorFull() instead")
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoChannelsChannelHandleVideoPlaylistsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoPlaylistsPlaylistIdDeleteSignalErrorFull() instead")
    void apiV1VideoPlaylistsPlaylistIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoPlaylistsPlaylistIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoPlaylistsPlaylistIdGetSignalErrorFull() instead")
    void apiV1VideoPlaylistsPlaylistIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoPlaylistsPlaylistIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideoPlaylistsPlaylistIdPutSignalErrorFull() instead")
    void apiV1VideoPlaylistsPlaylistIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideoPlaylistsPlaylistIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delVideoPlaylistVideoSignalErrorFull() instead")
    void delVideoPlaylistVideoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void delVideoPlaylistVideoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlaylistPrivacyPoliciesSignalErrorFull() instead")
    void getPlaylistPrivacyPoliciesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPlaylistPrivacyPoliciesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPlaylistsSignalErrorFull() instead")
    void getPlaylistsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPlaylistsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoPlaylistVideosSignalErrorFull() instead")
    void getVideoPlaylistVideosSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoPlaylistVideosSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putVideoPlaylistVideoSignalErrorFull() instead")
    void putVideoPlaylistVideoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putVideoPlaylistVideoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reorderVideoPlaylistSignalErrorFull() instead")
    void reorderVideoPlaylistSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reorderVideoPlaylistSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
