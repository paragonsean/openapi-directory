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

#ifndef OAI_OAIAbusesApi_H
#define OAI_OAIAbusesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAbuseStateSet.h"
#include "OAIGetAbuses_200_response.h"
#include "OAI_api_v1_abuses__abuseId__messages_get_200_response.h"
#include "OAI_api_v1_abuses__abuseId__messages_post_request.h"
#include "OAI_api_v1_abuses__abuseId__put_request.h"
#include "OAI_api_v1_abuses_post_200_response.h"
#include "OAI_api_v1_abuses_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAbusesApi : public QObject {
    Q_OBJECT

public:
    OAIAbusesApi(const int timeOut = 0);
    ~OAIAbusesApi();

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
    * @param[in]  abuse_id qint32 [required]
    */
    virtual void apiV1AbusesAbuseIdDelete(const qint32 &abuse_id);

    /**
    * @param[in]  abuse_id qint32 [required]
    * @param[in]  abuse_message_id qint32 [required]
    */
    virtual void apiV1AbusesAbuseIdMessagesAbuseMessageIdDelete(const qint32 &abuse_id, const qint32 &abuse_message_id);

    /**
    * @param[in]  abuse_id qint32 [required]
    */
    virtual void apiV1AbusesAbuseIdMessagesGet(const qint32 &abuse_id);

    /**
    * @param[in]  abuse_id qint32 [required]
    * @param[in]  oai_api_v1_abuses__abuse_id__messages_post_request OAI_api_v1_abuses__abuseId__messages_post_request [required]
    */
    virtual void apiV1AbusesAbuseIdMessagesPost(const qint32 &abuse_id, const OAI_api_v1_abuses__abuseId__messages_post_request &oai_api_v1_abuses__abuse_id__messages_post_request);

    /**
    * @param[in]  abuse_id qint32 [required]
    * @param[in]  oai_api_v1_abuses__abuse_id__put_request OAI_api_v1_abuses__abuseId__put_request [optional]
    */
    virtual void apiV1AbusesAbuseIdPut(const qint32 &abuse_id, const ::OpenAPI::OptionalParam<OAI_api_v1_abuses__abuseId__put_request> &oai_api_v1_abuses__abuse_id__put_request = ::OpenAPI::OptionalParam<OAI_api_v1_abuses__abuseId__put_request>());

    /**
    * @param[in]  oai_api_v1_abuses_post_request OAI_api_v1_abuses_post_request [required]
    */
    virtual void apiV1AbusesPost(const OAI_api_v1_abuses_post_request &oai_api_v1_abuses_post_request);

    /**
    * @param[in]  id qint32 [optional]
    * @param[in]  predefined_reason QList<QString> [optional]
    * @param[in]  search QString [optional]
    * @param[in]  state OAIAbuseStateSet [optional]
    * @param[in]  search_reporter QString [optional]
    * @param[in]  search_reportee QString [optional]
    * @param[in]  search_video QString [optional]
    * @param[in]  search_video_channel QString [optional]
    * @param[in]  video_is QString [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getAbuses(const ::OpenAPI::OptionalParam<qint32> &id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QList<QString>> &predefined_reason = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIAbuseStateSet> &state = ::OpenAPI::OptionalParam<OAIAbuseStateSet>(), const ::OpenAPI::OptionalParam<QString> &search_reporter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search_reportee = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search_video = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &search_video_channel = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &video_is = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id qint32 [optional]
    * @param[in]  state OAIAbuseStateSet [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    */
    virtual void getMyAbuses(const ::OpenAPI::OptionalParam<qint32> &id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIAbuseStateSet> &state = ::OpenAPI::OptionalParam<OAIAbuseStateSet>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>());


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

    void apiV1AbusesAbuseIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteCallback(OAIHttpRequestWorker *worker);
    void apiV1AbusesAbuseIdMessagesGetCallback(OAIHttpRequestWorker *worker);
    void apiV1AbusesAbuseIdMessagesPostCallback(OAIHttpRequestWorker *worker);
    void apiV1AbusesAbuseIdPutCallback(OAIHttpRequestWorker *worker);
    void apiV1AbusesPostCallback(OAIHttpRequestWorker *worker);
    void getAbusesCallback(OAIHttpRequestWorker *worker);
    void getMyAbusesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiV1AbusesAbuseIdDeleteSignal();
    void apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignal();
    void apiV1AbusesAbuseIdMessagesGetSignal(OAI_api_v1_abuses__abuseId__messages_get_200_response summary);
    void apiV1AbusesAbuseIdMessagesPostSignal();
    void apiV1AbusesAbuseIdPutSignal();
    void apiV1AbusesPostSignal(OAI_api_v1_abuses_post_200_response summary);
    void getAbusesSignal(OAIGetAbuses_200_response summary);
    void getMyAbusesSignal(OAIGetAbuses_200_response summary);


    void apiV1AbusesAbuseIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiV1AbusesAbuseIdMessagesGetSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_abuses__abuseId__messages_get_200_response summary);
    void apiV1AbusesAbuseIdMessagesPostSignalFull(OAIHttpRequestWorker *worker);
    void apiV1AbusesAbuseIdPutSignalFull(OAIHttpRequestWorker *worker);
    void apiV1AbusesPostSignalFull(OAIHttpRequestWorker *worker, OAI_api_v1_abuses_post_200_response summary);
    void getAbusesSignalFull(OAIHttpRequestWorker *worker, OAIGetAbuses_200_response summary);
    void getMyAbusesSignalFull(OAIHttpRequestWorker *worker, OAIGetAbuses_200_response summary);

    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdDeleteSignalError() instead")
    void apiV1AbusesAbuseIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignalError() instead")
    void apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdMessagesGetSignalError() instead")
    void apiV1AbusesAbuseIdMessagesGetSignalE(OAI_api_v1_abuses__abuseId__messages_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdMessagesGetSignalError(OAI_api_v1_abuses__abuseId__messages_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdMessagesPostSignalError() instead")
    void apiV1AbusesAbuseIdMessagesPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdMessagesPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdPutSignalError() instead")
    void apiV1AbusesAbuseIdPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesPostSignalError() instead")
    void apiV1AbusesPostSignalE(OAI_api_v1_abuses_post_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesPostSignalError(OAI_api_v1_abuses_post_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAbusesSignalError() instead")
    void getAbusesSignalE(OAIGetAbuses_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAbusesSignalError(OAIGetAbuses_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMyAbusesSignalError() instead")
    void getMyAbusesSignalE(OAIGetAbuses_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMyAbusesSignalError(OAIGetAbuses_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdDeleteSignalErrorFull() instead")
    void apiV1AbusesAbuseIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignalErrorFull() instead")
    void apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdMessagesAbuseMessageIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdMessagesGetSignalErrorFull() instead")
    void apiV1AbusesAbuseIdMessagesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdMessagesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdMessagesPostSignalErrorFull() instead")
    void apiV1AbusesAbuseIdMessagesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdMessagesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesAbuseIdPutSignalErrorFull() instead")
    void apiV1AbusesAbuseIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesAbuseIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1AbusesPostSignalErrorFull() instead")
    void apiV1AbusesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1AbusesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAbusesSignalErrorFull() instead")
    void getAbusesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAbusesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMyAbusesSignalErrorFull() instead")
    void getMyAbusesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMyAbusesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
