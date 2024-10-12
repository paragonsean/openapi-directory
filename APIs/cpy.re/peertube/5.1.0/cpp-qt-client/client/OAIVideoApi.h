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

#ifndef OAI_OAIVideoApi_H
#define OAI_OAIVideoApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetAccountVideos_categoryOneOf_parameter.h"
#include "OAIGetAccountVideos_languageOneOf_parameter.h"
#include "OAIGetAccountVideos_licenceOneOf_parameter.h"
#include "OAIGetAccountVideos_tagsAllOf_parameter.h"
#include "OAIGetAccountVideos_tagsOneOf_parameter.h"
#include "OAIGetLiveId_id_parameter.h"
#include "OAIHttpFileElement.h"
#include "OAILiveVideoLatencyMode.h"
#include "OAILiveVideoReplaySettings.h"
#include "OAILiveVideoResponse.h"
#include "OAILiveVideoUpdate.h"
#include "OAIUserViewingVideo.h"
#include "OAIVideoDetails.h"
#include "OAIVideoListResponse.h"
#include "OAIVideoPrivacySet.h"
#include "OAIVideoScheduledUpdate.h"
#include "OAIVideoSource.h"
#include "OAIVideoTokenResponse.h"
#include "OAIVideoUploadRequestResumable.h"
#include "OAIVideoUploadResponse.h"
#include <QString>
#include <QDateTime>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVideoApi : public QObject {
    Q_OBJECT

public:
    OAIVideoApi(const int timeOut = 0);
    ~OAIVideoApi();

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
    * @param[in]  channel_id qint32 [required]
    * @param[in]  name QString [required]
    * @param[in]  category qint32 [optional]
    * @param[in]  comments_enabled bool [optional]
    * @param[in]  description QString [optional]
    * @param[in]  download_enabled bool [optional]
    * @param[in]  language QString [optional]
    * @param[in]  latency_mode OAILiveVideoLatencyMode [optional]
    * @param[in]  licence qint32 [optional]
    * @param[in]  nsfw bool [optional]
    * @param[in]  permanent_live bool [optional]
    * @param[in]  previewfile OAIHttpFileElement [optional]
    * @param[in]  privacy OAIVideoPrivacySet [optional]
    * @param[in]  replay_settings OAILiveVideoReplaySettings [optional]
    * @param[in]  save_replay bool [optional]
    * @param[in]  support QString [optional]
    * @param[in]  tags QList<QString> [optional]
    * @param[in]  thumbnailfile OAIHttpFileElement [optional]
    */
    virtual void addLive(const qint32 &channel_id, const QString &name, const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &comments_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &download_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAILiveVideoLatencyMode> &latency_mode = ::OpenAPI::OptionalParam<OAILiveVideoLatencyMode>(), const ::OpenAPI::OptionalParam<qint32> &licence = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &nsfw = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &permanent_live = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &previewfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<OAILiveVideoReplaySettings> &replay_settings = ::OpenAPI::OptionalParam<OAILiveVideoReplaySettings>(), const ::OpenAPI::OptionalParam<bool> &save_replay = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &support = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &tags = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &thumbnailfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>());

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    * @param[in]  oai_user_viewing_video OAIUserViewingVideo [required]
    */
    virtual void addView(const OAIGetLiveId_id_parameter &id, const OAIUserViewingVideo &oai_user_viewing_video);

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    */
    virtual void apiV1VideosIdStudioEditPost(const OAIGetLiveId_id_parameter &id);

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    * @param[in]  oai_user_viewing_video OAIUserViewingVideo [required]
    */
    Q_DECL_DEPRECATED virtual void apiV1VideosIdWatchingPut(const OAIGetLiveId_id_parameter &id, const OAIUserViewingVideo &oai_user_viewing_video);

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    */
    virtual void delVideo(const OAIGetLiveId_id_parameter &id);

    /**
    * @param[in]  name QString [required]
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
    virtual void getAccountVideos(const QString &name, const ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter> &category_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter>(), const ::OpenAPI::OptionalParam<bool> &is_live = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter> &tags_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter> &tags_all_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter> &licence_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter> &language_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter>(), const ::OpenAPI::OptionalParam<QString> &nsfw = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &is_local = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &include = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy_one_of = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<bool> &has_hls_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &has_webtorrent_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &skip_count = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &exclude_already_watched = ::OpenAPI::OptionalParam<bool>());


    virtual void getCategories();


    virtual void getLanguages();


    virtual void getLicences();

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    */
    virtual void getLiveId(const OAIGetLiveId_id_parameter &id);

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    */
    virtual void getVideo(const OAIGetLiveId_id_parameter &id);

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
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    */
    virtual void getVideoDesc(const OAIGetLiveId_id_parameter &id);


    virtual void getVideoPrivacyPolicies();

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    */
    virtual void getVideoSource(const OAIGetLiveId_id_parameter &id);

    /**
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
    virtual void getVideos(const ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter> &category_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter>(), const ::OpenAPI::OptionalParam<bool> &is_live = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter> &tags_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter> &tags_all_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter> &licence_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter> &language_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter>(), const ::OpenAPI::OptionalParam<QString> &nsfw = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &is_local = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &include = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy_one_of = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<bool> &has_hls_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &has_webtorrent_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &skip_count = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &exclude_already_watched = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    * @param[in]  category qint32 [optional]
    * @param[in]  comments_enabled bool [optional]
    * @param[in]  description QString [optional]
    * @param[in]  download_enabled bool [optional]
    * @param[in]  language QString [optional]
    * @param[in]  licence qint32 [optional]
    * @param[in]  name QString [optional]
    * @param[in]  nsfw bool [optional]
    * @param[in]  originally_published_at QDateTime [optional]
    * @param[in]  previewfile OAIHttpFileElement [optional]
    * @param[in]  privacy OAIVideoPrivacySet [optional]
    * @param[in]  schedule_update OAIVideoScheduledUpdate [optional]
    * @param[in]  support QString [optional]
    * @param[in]  tags QList<QString> [optional]
    * @param[in]  thumbnailfile OAIHttpFileElement [optional]
    * @param[in]  wait_transcoding QString [optional]
    */
    virtual void putVideo(const OAIGetLiveId_id_parameter &id, const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &comments_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &download_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &licence = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &nsfw = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QDateTime> &originally_published_at = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &previewfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<OAIVideoScheduledUpdate> &schedule_update = ::OpenAPI::OptionalParam<OAIVideoScheduledUpdate>(), const ::OpenAPI::OptionalParam<QString> &support = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &tags = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &thumbnailfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<QString> &wait_transcoding = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    */
    virtual void requestVideoToken(const OAIGetLiveId_id_parameter &id);

    /**
    * @param[in]  id OAIGetLiveId_id_parameter [required]
    * @param[in]  oai_live_video_update OAILiveVideoUpdate [optional]
    */
    virtual void updateLiveId(const OAIGetLiveId_id_parameter &id, const ::OpenAPI::OptionalParam<OAILiveVideoUpdate> &oai_live_video_update = ::OpenAPI::OptionalParam<OAILiveVideoUpdate>());

    /**
    * @param[in]  name QString [required]
    * @param[in]  videofile OAIHttpFileElement [required]
    * @param[in]  category qint32 [optional]
    * @param[in]  channel_id qint32 [optional]
    * @param[in]  comments_enabled bool [optional]
    * @param[in]  description QString [optional]
    * @param[in]  download_enabled bool [optional]
    * @param[in]  language QString [optional]
    * @param[in]  licence qint32 [optional]
    * @param[in]  nsfw bool [optional]
    * @param[in]  originally_published_at QDateTime [optional]
    * @param[in]  previewfile OAIHttpFileElement [optional]
    * @param[in]  privacy OAIVideoPrivacySet [optional]
    * @param[in]  schedule_update OAIVideoScheduledUpdate [optional]
    * @param[in]  support QString [optional]
    * @param[in]  tags QSet<QString> [optional]
    * @param[in]  thumbnailfile OAIHttpFileElement [optional]
    * @param[in]  wait_transcoding bool [optional]
    */
    virtual void uploadLegacy(const QString &name, const OAIHttpFileElement &videofile, const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &channel_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &comments_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &download_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &licence = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &nsfw = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QDateTime> &originally_published_at = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &previewfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<OAIVideoScheduledUpdate> &schedule_update = ::OpenAPI::OptionalParam<OAIVideoScheduledUpdate>(), const ::OpenAPI::OptionalParam<QString> &support = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QSet<QString>> &tags = ::OpenAPI::OptionalParam<QSet<QString>>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &thumbnailfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<bool> &wait_transcoding = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  upload_id QString [required]
    * @param[in]  content_range QString [required]
    * @param[in]  content_length double [required]
    * @param[in]  body OAIHttpFileElement [optional]
    */
    virtual void uploadResumable(const QString &upload_id, const QString &content_range, const double &content_length, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &body = ::OpenAPI::OptionalParam<OAIHttpFileElement>());

    /**
    * @param[in]  upload_id QString [required]
    * @param[in]  content_length double [required]
    */
    virtual void uploadResumableCancel(const QString &upload_id, const double &content_length);

    /**
    * @param[in]  x_upload_content_length double [required]
    * @param[in]  x_upload_content_type QString [required]
    * @param[in]  oai_video_upload_request_resumable OAIVideoUploadRequestResumable [optional]
    */
    virtual void uploadResumableInit(const double &x_upload_content_length, const QString &x_upload_content_type, const ::OpenAPI::OptionalParam<OAIVideoUploadRequestResumable> &oai_video_upload_request_resumable = ::OpenAPI::OptionalParam<OAIVideoUploadRequestResumable>());


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

    void addLiveCallback(OAIHttpRequestWorker *worker);
    void addViewCallback(OAIHttpRequestWorker *worker);
    void apiV1VideosIdStudioEditPostCallback(OAIHttpRequestWorker *worker);
    void apiV1VideosIdWatchingPutCallback(OAIHttpRequestWorker *worker);
    void delVideoCallback(OAIHttpRequestWorker *worker);
    void getAccountVideosCallback(OAIHttpRequestWorker *worker);
    void getCategoriesCallback(OAIHttpRequestWorker *worker);
    void getLanguagesCallback(OAIHttpRequestWorker *worker);
    void getLicencesCallback(OAIHttpRequestWorker *worker);
    void getLiveIdCallback(OAIHttpRequestWorker *worker);
    void getVideoCallback(OAIHttpRequestWorker *worker);
    void getVideoChannelVideosCallback(OAIHttpRequestWorker *worker);
    void getVideoDescCallback(OAIHttpRequestWorker *worker);
    void getVideoPrivacyPoliciesCallback(OAIHttpRequestWorker *worker);
    void getVideoSourceCallback(OAIHttpRequestWorker *worker);
    void getVideosCallback(OAIHttpRequestWorker *worker);
    void putVideoCallback(OAIHttpRequestWorker *worker);
    void requestVideoTokenCallback(OAIHttpRequestWorker *worker);
    void updateLiveIdCallback(OAIHttpRequestWorker *worker);
    void uploadLegacyCallback(OAIHttpRequestWorker *worker);
    void uploadResumableCallback(OAIHttpRequestWorker *worker);
    void uploadResumableCancelCallback(OAIHttpRequestWorker *worker);
    void uploadResumableInitCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addLiveSignal(OAIVideoUploadResponse summary);
    void addViewSignal();
    void apiV1VideosIdStudioEditPostSignal();
    void apiV1VideosIdWatchingPutSignal();
    void delVideoSignal();
    void getAccountVideosSignal(OAIVideoListResponse summary);
    void getCategoriesSignal(QList<QString> summary);
    void getLanguagesSignal(QList<QString> summary);
    void getLicencesSignal(QList<QString> summary);
    void getLiveIdSignal(OAILiveVideoResponse summary);
    void getVideoSignal(OAIVideoDetails summary);
    void getVideoChannelVideosSignal(OAIVideoListResponse summary);
    void getVideoDescSignal(QString summary);
    void getVideoPrivacyPoliciesSignal(QList<QString> summary);
    void getVideoSourceSignal(OAIVideoSource summary);
    void getVideosSignal(OAIVideoListResponse summary);
    void putVideoSignal();
    void requestVideoTokenSignal(OAIVideoTokenResponse summary);
    void updateLiveIdSignal();
    void uploadLegacySignal(OAIVideoUploadResponse summary);
    void uploadResumableSignal(OAIVideoUploadResponse summary);
    void uploadResumableCancelSignal();
    void uploadResumableInitSignal();


    void addLiveSignalFull(OAIHttpRequestWorker *worker, OAIVideoUploadResponse summary);
    void addViewSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VideosIdStudioEditPostSignalFull(OAIHttpRequestWorker *worker);
    void apiV1VideosIdWatchingPutSignalFull(OAIHttpRequestWorker *worker);
    void delVideoSignalFull(OAIHttpRequestWorker *worker);
    void getAccountVideosSignalFull(OAIHttpRequestWorker *worker, OAIVideoListResponse summary);
    void getCategoriesSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void getLanguagesSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void getLicencesSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void getLiveIdSignalFull(OAIHttpRequestWorker *worker, OAILiveVideoResponse summary);
    void getVideoSignalFull(OAIHttpRequestWorker *worker, OAIVideoDetails summary);
    void getVideoChannelVideosSignalFull(OAIHttpRequestWorker *worker, OAIVideoListResponse summary);
    void getVideoDescSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void getVideoPrivacyPoliciesSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void getVideoSourceSignalFull(OAIHttpRequestWorker *worker, OAIVideoSource summary);
    void getVideosSignalFull(OAIHttpRequestWorker *worker, OAIVideoListResponse summary);
    void putVideoSignalFull(OAIHttpRequestWorker *worker);
    void requestVideoTokenSignalFull(OAIHttpRequestWorker *worker, OAIVideoTokenResponse summary);
    void updateLiveIdSignalFull(OAIHttpRequestWorker *worker);
    void uploadLegacySignalFull(OAIHttpRequestWorker *worker, OAIVideoUploadResponse summary);
    void uploadResumableSignalFull(OAIHttpRequestWorker *worker, OAIVideoUploadResponse summary);
    void uploadResumableCancelSignalFull(OAIHttpRequestWorker *worker);
    void uploadResumableInitSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use addLiveSignalError() instead")
    void addLiveSignalE(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addLiveSignalError(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addViewSignalError() instead")
    void addViewSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void addViewSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideosIdStudioEditPostSignalError() instead")
    void apiV1VideosIdStudioEditPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideosIdStudioEditPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideosIdWatchingPutSignalError() instead")
    void apiV1VideosIdWatchingPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideosIdWatchingPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delVideoSignalError() instead")
    void delVideoSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void delVideoSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountVideosSignalError() instead")
    void getAccountVideosSignalE(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountVideosSignalError(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCategoriesSignalError() instead")
    void getCategoriesSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getCategoriesSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLanguagesSignalError() instead")
    void getLanguagesSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLanguagesSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLicencesSignalError() instead")
    void getLicencesSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLicencesSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLiveIdSignalError() instead")
    void getLiveIdSignalE(OAILiveVideoResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLiveIdSignalError(OAILiveVideoResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoSignalError() instead")
    void getVideoSignalE(OAIVideoDetails summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoSignalError(OAIVideoDetails summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelVideosSignalError() instead")
    void getVideoChannelVideosSignalE(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelVideosSignalError(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoDescSignalError() instead")
    void getVideoDescSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoDescSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoPrivacyPoliciesSignalError() instead")
    void getVideoPrivacyPoliciesSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoPrivacyPoliciesSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoSourceSignalError() instead")
    void getVideoSourceSignalE(OAIVideoSource summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoSourceSignalError(OAIVideoSource summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideosSignalError() instead")
    void getVideosSignalE(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideosSignalError(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putVideoSignalError() instead")
    void putVideoSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void putVideoSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestVideoTokenSignalError() instead")
    void requestVideoTokenSignalE(OAIVideoTokenResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestVideoTokenSignalError(OAIVideoTokenResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLiveIdSignalError() instead")
    void updateLiveIdSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void updateLiveIdSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadLegacySignalError() instead")
    void uploadLegacySignalE(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadLegacySignalError(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableSignalError() instead")
    void uploadResumableSignalE(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableSignalError(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableCancelSignalError() instead")
    void uploadResumableCancelSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableCancelSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableInitSignalError() instead")
    void uploadResumableInitSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableInitSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addLiveSignalErrorFull() instead")
    void addLiveSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addLiveSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addViewSignalErrorFull() instead")
    void addViewSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addViewSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideosIdStudioEditPostSignalErrorFull() instead")
    void apiV1VideosIdStudioEditPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideosIdStudioEditPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1VideosIdWatchingPutSignalErrorFull() instead")
    void apiV1VideosIdWatchingPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1VideosIdWatchingPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delVideoSignalErrorFull() instead")
    void delVideoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void delVideoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountVideosSignalErrorFull() instead")
    void getAccountVideosSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountVideosSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCategoriesSignalErrorFull() instead")
    void getCategoriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCategoriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLanguagesSignalErrorFull() instead")
    void getLanguagesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLanguagesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLicencesSignalErrorFull() instead")
    void getLicencesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLicencesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLiveIdSignalErrorFull() instead")
    void getLiveIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLiveIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoSignalErrorFull() instead")
    void getVideoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoChannelVideosSignalErrorFull() instead")
    void getVideoChannelVideosSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoChannelVideosSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoDescSignalErrorFull() instead")
    void getVideoDescSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoDescSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoPrivacyPoliciesSignalErrorFull() instead")
    void getVideoPrivacyPoliciesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoPrivacyPoliciesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideoSourceSignalErrorFull() instead")
    void getVideoSourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideoSourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getVideosSignalErrorFull() instead")
    void getVideosSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVideosSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putVideoSignalErrorFull() instead")
    void putVideoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putVideoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestVideoTokenSignalErrorFull() instead")
    void requestVideoTokenSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestVideoTokenSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLiveIdSignalErrorFull() instead")
    void updateLiveIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLiveIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadLegacySignalErrorFull() instead")
    void uploadLegacySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadLegacySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableSignalErrorFull() instead")
    void uploadResumableSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableCancelSignalErrorFull() instead")
    void uploadResumableCancelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableCancelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableInitSignalErrorFull() instead")
    void uploadResumableInitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableInitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
