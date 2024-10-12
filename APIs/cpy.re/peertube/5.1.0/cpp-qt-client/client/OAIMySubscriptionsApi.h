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

#ifndef OAI_OAIMySubscriptionsApi_H
#define OAI_OAIMySubscriptionsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetAccountVideos_categoryOneOf_parameter.h"
#include "OAIGetAccountVideos_languageOneOf_parameter.h"
#include "OAIGetAccountVideos_licenceOneOf_parameter.h"
#include "OAIGetAccountVideos_tagsAllOf_parameter.h"
#include "OAIGetAccountVideos_tagsOneOf_parameter.h"
#include "OAIObject.h"
#include "OAIVideoChannel.h"
#include "OAIVideoChannelList.h"
#include "OAIVideoListResponse.h"
#include "OAIVideoPrivacySet.h"
#include "OAI_api_v1_users_me_subscriptions_post_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMySubscriptionsApi : public QObject {
    Q_OBJECT

public:
    OAIMySubscriptionsApi(const int timeOut = 0);
    ~OAIMySubscriptionsApi();

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
    * @param[in]  uris QList<QString> [required]
    */
    virtual void apiV1UsersMeSubscriptionsExistGet(const QList<QString> &uris);

    /**
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void apiV1UsersMeSubscriptionsGet(const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_api_v1_users_me_subscriptions_post_request OAI_api_v1_users_me_subscriptions_post_request [optional]
    */
    virtual void apiV1UsersMeSubscriptionsPost(const ::OpenAPI::OptionalParam<OAI_api_v1_users_me_subscriptions_post_request> &oai_api_v1_users_me_subscriptions_post_request = ::OpenAPI::OptionalParam<OAI_api_v1_users_me_subscriptions_post_request>());

    /**
    * @param[in]  subscription_handle QString [required]
    */
    virtual void apiV1UsersMeSubscriptionsSubscriptionHandleDelete(const QString &subscription_handle);

    /**
    * @param[in]  subscription_handle QString [required]
    */
    virtual void apiV1UsersMeSubscriptionsSubscriptionHandleGet(const QString &subscription_handle);

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
    virtual void apiV1UsersMeSubscriptionsVideosGet(const ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter> &category_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_categoryOneOf_parameter>(), const ::OpenAPI::OptionalParam<bool> &is_live = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter> &tags_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter> &tags_all_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_tagsAllOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter> &licence_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_licenceOneOf_parameter>(), const ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter> &language_one_of = ::OpenAPI::OptionalParam<OAIGetAccountVideos_languageOneOf_parameter>(), const ::OpenAPI::OptionalParam<QString> &nsfw = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &is_local = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &include = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAIVideoPrivacySet> &privacy_one_of = ::OpenAPI::OptionalParam<OAIVideoPrivacySet>(), const ::OpenAPI::OptionalParam<bool> &has_hls_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &has_webtorrent_files = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &skip_count = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &exclude_already_watched = ::OpenAPI::OptionalParam<bool>());


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

    void apiV1UsersMeSubscriptionsExistGetCallback(OAIHttpRequestWorker *worker);
    void apiV1UsersMeSubscriptionsGetCallback(OAIHttpRequestWorker *worker);
    void apiV1UsersMeSubscriptionsPostCallback(OAIHttpRequestWorker *worker);
    void apiV1UsersMeSubscriptionsSubscriptionHandleDeleteCallback(OAIHttpRequestWorker *worker);
    void apiV1UsersMeSubscriptionsSubscriptionHandleGetCallback(OAIHttpRequestWorker *worker);
    void apiV1UsersMeSubscriptionsVideosGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void apiV1UsersMeSubscriptionsExistGetSignal(OAIObject summary);
    void apiV1UsersMeSubscriptionsGetSignal(OAIVideoChannelList summary);
    void apiV1UsersMeSubscriptionsPostSignal();
    void apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignal();
    void apiV1UsersMeSubscriptionsSubscriptionHandleGetSignal(OAIVideoChannel summary);
    void apiV1UsersMeSubscriptionsVideosGetSignal(OAIVideoListResponse summary);


    void apiV1UsersMeSubscriptionsExistGetSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void apiV1UsersMeSubscriptionsGetSignalFull(OAIHttpRequestWorker *worker, OAIVideoChannelList summary);
    void apiV1UsersMeSubscriptionsPostSignalFull(OAIHttpRequestWorker *worker);
    void apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignalFull(OAIHttpRequestWorker *worker);
    void apiV1UsersMeSubscriptionsSubscriptionHandleGetSignalFull(OAIHttpRequestWorker *worker, OAIVideoChannel summary);
    void apiV1UsersMeSubscriptionsVideosGetSignalFull(OAIHttpRequestWorker *worker, OAIVideoListResponse summary);

    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsExistGetSignalError() instead")
    void apiV1UsersMeSubscriptionsExistGetSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsExistGetSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsGetSignalError() instead")
    void apiV1UsersMeSubscriptionsGetSignalE(OAIVideoChannelList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsGetSignalError(OAIVideoChannelList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsPostSignalError() instead")
    void apiV1UsersMeSubscriptionsPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignalError() instead")
    void apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsSubscriptionHandleGetSignalError() instead")
    void apiV1UsersMeSubscriptionsSubscriptionHandleGetSignalE(OAIVideoChannel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsSubscriptionHandleGetSignalError(OAIVideoChannel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsVideosGetSignalError() instead")
    void apiV1UsersMeSubscriptionsVideosGetSignalE(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsVideosGetSignalError(OAIVideoListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsExistGetSignalErrorFull() instead")
    void apiV1UsersMeSubscriptionsExistGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsExistGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsGetSignalErrorFull() instead")
    void apiV1UsersMeSubscriptionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsPostSignalErrorFull() instead")
    void apiV1UsersMeSubscriptionsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignalErrorFull() instead")
    void apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsSubscriptionHandleDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsSubscriptionHandleGetSignalErrorFull() instead")
    void apiV1UsersMeSubscriptionsSubscriptionHandleGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsSubscriptionHandleGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use apiV1UsersMeSubscriptionsVideosGetSignalErrorFull() instead")
    void apiV1UsersMeSubscriptionsVideosGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void apiV1UsersMeSubscriptionsVideosGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
