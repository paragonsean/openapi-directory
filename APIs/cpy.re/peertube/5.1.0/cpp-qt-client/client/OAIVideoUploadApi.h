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

#ifndef OAI_OAIVideoUploadApi_H
#define OAI_OAIVideoUploadApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIHttpFileElement.h"
#include "OAIVideoPrivacySet.h"
#include "OAIVideoScheduledUpdate.h"
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

class OAIVideoUploadApi : public QObject {
    Q_OBJECT

public:
    OAIVideoUploadApi(const int timeOut = 0);
    ~OAIVideoUploadApi();

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
    * @param[in]  target_url QString [optional]
    * @param[in]  magnet_uri QString [optional]
    * @param[in]  torrentfile OAIHttpFileElement [optional]
    * @param[in]  category qint32 [optional]
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
    virtual void importVideo(const qint32 &channel_id, const QString &name, const ::OpenAPI::OptionalParam<QString> &target_url = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &magnet_uri = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &torrentfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<qint32> &category = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &comments_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &description = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &download_enabled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &language = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &licence = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &nsfw = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QDateTime> &originally_published_at = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &previewfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<OAIVideoScheduledUpdate> &schedule_update = ::OpenAPI::OptionalParam<OAIVideoScheduledUpdate>(), const ::OpenAPI::OptionalParam<QString> &support = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QSet<QString>> &tags = ::OpenAPI::OptionalParam<QSet<QString>>(), const ::OpenAPI::OptionalParam<OAIHttpFileElement> &thumbnailfile = ::OpenAPI::OptionalParam<OAIHttpFileElement>(), const ::OpenAPI::OptionalParam<bool> &wait_transcoding = ::OpenAPI::OptionalParam<bool>());

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
    * @param[in]  content_length double [required]
    */
    virtual void uploadResumableCancel(const QString &upload_id, const double &content_length);

    /**
    * @param[in]  x_upload_content_length double [required]
    * @param[in]  x_upload_content_type QString [required]
    * @param[in]  oai_video_upload_request_resumable OAIVideoUploadRequestResumable [optional]
    */
    virtual void uploadResumableInit(const double &x_upload_content_length, const QString &x_upload_content_type, const ::OpenAPI::OptionalParam<OAIVideoUploadRequestResumable> &oai_video_upload_request_resumable = ::OpenAPI::OptionalParam<OAIVideoUploadRequestResumable>());

    /**
    * @param[in]  upload_id QString [required]
    * @param[in]  content_range QString [required]
    * @param[in]  content_length double [required]
    * @param[in]  body OAIHttpFileElement [optional]
    */
    virtual void uploadResumable(const QString &upload_id, const QString &content_range, const double &content_length, const ::OpenAPI::OptionalParam<OAIHttpFileElement> &body = ::OpenAPI::OptionalParam<OAIHttpFileElement>());


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

    void importVideoCallback(OAIHttpRequestWorker *worker);
    void uploadLegacyCallback(OAIHttpRequestWorker *worker);
    void uploadResumableCancelCallback(OAIHttpRequestWorker *worker);
    void uploadResumableInitCallback(OAIHttpRequestWorker *worker);
    void uploadResumableCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void importVideoSignal(OAIVideoUploadResponse summary);
    void uploadLegacySignal(OAIVideoUploadResponse summary);
    void uploadResumableCancelSignal();
    void uploadResumableInitSignal();
    void uploadResumableSignal(OAIVideoUploadResponse summary);


    void importVideoSignalFull(OAIHttpRequestWorker *worker, OAIVideoUploadResponse summary);
    void uploadLegacySignalFull(OAIHttpRequestWorker *worker, OAIVideoUploadResponse summary);
    void uploadResumableCancelSignalFull(OAIHttpRequestWorker *worker);
    void uploadResumableInitSignalFull(OAIHttpRequestWorker *worker);
    void uploadResumableSignalFull(OAIHttpRequestWorker *worker, OAIVideoUploadResponse summary);

    Q_DECL_DEPRECATED_X("Use importVideoSignalError() instead")
    void importVideoSignalE(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void importVideoSignalError(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadLegacySignalError() instead")
    void uploadLegacySignalE(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadLegacySignalError(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableCancelSignalError() instead")
    void uploadResumableCancelSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableCancelSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableInitSignalError() instead")
    void uploadResumableInitSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableInitSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableSignalError() instead")
    void uploadResumableSignalE(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableSignalError(OAIVideoUploadResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use importVideoSignalErrorFull() instead")
    void importVideoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void importVideoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadLegacySignalErrorFull() instead")
    void uploadLegacySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadLegacySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableCancelSignalErrorFull() instead")
    void uploadResumableCancelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableCancelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableInitSignalErrorFull() instead")
    void uploadResumableInitSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableInitSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use uploadResumableSignalErrorFull() instead")
    void uploadResumableSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void uploadResumableSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
