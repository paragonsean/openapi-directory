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

#ifndef OAI_OAIUsersApi_H
#define OAI_OAIUsersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddUser.h"
#include "OAIAddUserResponse.h"
#include "OAIConfirmTwoFactorRequest_request.h"
#include "OAIDisableTwoFactor_request.h"
#include "OAIGetUser_200_response.h"
#include "OAIRequestTwoFactorResponse.h"
#include "OAIResendEmailToVerifyUser_request.h"
#include "OAIUpdateUser.h"
#include "OAIUser.h"
#include "OAIVerifyUser_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUsersApi : public QObject {
    Q_OBJECT

public:
    OAIUsersApi(const int timeOut = 0);
    ~OAIUsersApi();

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
    * @param[in]  oai_add_user OAIAddUser [required]
    */
    virtual void addUser(const OAIAddUser &oai_add_user);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_confirm_two_factor_request_request OAIConfirmTwoFactorRequest_request [optional]
    */
    virtual void confirmTwoFactorRequest(const qint32 &id, const ::OpenAPI::OptionalParam<OAIConfirmTwoFactorRequest_request> &oai_confirm_two_factor_request_request = ::OpenAPI::OptionalParam<OAIConfirmTwoFactorRequest_request>());

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void delUser(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_disable_two_factor_request OAIDisableTwoFactor_request [optional]
    */
    virtual void disableTwoFactor(const qint32 &id, const ::OpenAPI::OptionalParam<OAIDisableTwoFactor_request> &oai_disable_two_factor_request = ::OpenAPI::OptionalParam<OAIDisableTwoFactor_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  with_stats bool [optional]
    */
    virtual void getUser(const qint32 &id, const ::OpenAPI::OptionalParam<bool> &with_stats = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  search QString [optional]
    * @param[in]  blocked bool [optional]
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void getUsers(const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &blocked = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_update_user OAIUpdateUser [required]
    */
    virtual void putUser(const qint32 &id, const OAIUpdateUser &oai_update_user);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_disable_two_factor_request OAIDisableTwoFactor_request [optional]
    */
    virtual void requestTwoFactor(const qint32 &id, const ::OpenAPI::OptionalParam<OAIDisableTwoFactor_request> &oai_disable_two_factor_request = ::OpenAPI::OptionalParam<OAIDisableTwoFactor_request>());

    /**
    * @param[in]  oai_resend_email_to_verify_user_request OAIResendEmailToVerifyUser_request [optional]
    */
    virtual void resendEmailToVerifyUser(const ::OpenAPI::OptionalParam<OAIResendEmailToVerifyUser_request> &oai_resend_email_to_verify_user_request = ::OpenAPI::OptionalParam<OAIResendEmailToVerifyUser_request>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oai_verify_user_request OAIVerifyUser_request [optional]
    */
    virtual void verifyUser(const qint32 &id, const ::OpenAPI::OptionalParam<OAIVerifyUser_request> &oai_verify_user_request = ::OpenAPI::OptionalParam<OAIVerifyUser_request>());


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

    void addUserCallback(OAIHttpRequestWorker *worker);
    void confirmTwoFactorRequestCallback(OAIHttpRequestWorker *worker);
    void delUserCallback(OAIHttpRequestWorker *worker);
    void disableTwoFactorCallback(OAIHttpRequestWorker *worker);
    void getUserCallback(OAIHttpRequestWorker *worker);
    void getUsersCallback(OAIHttpRequestWorker *worker);
    void putUserCallback(OAIHttpRequestWorker *worker);
    void requestTwoFactorCallback(OAIHttpRequestWorker *worker);
    void resendEmailToVerifyUserCallback(OAIHttpRequestWorker *worker);
    void verifyUserCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addUserSignal(OAIAddUserResponse summary);
    void confirmTwoFactorRequestSignal();
    void delUserSignal();
    void disableTwoFactorSignal();
    void getUserSignal(OAIGetUser_200_response summary);
    void getUsersSignal(QList<OAIUser> summary);
    void putUserSignal();
    void requestTwoFactorSignal(QList<OAIRequestTwoFactorResponse> summary);
    void resendEmailToVerifyUserSignal();
    void verifyUserSignal();


    void addUserSignalFull(OAIHttpRequestWorker *worker, OAIAddUserResponse summary);
    void confirmTwoFactorRequestSignalFull(OAIHttpRequestWorker *worker);
    void delUserSignalFull(OAIHttpRequestWorker *worker);
    void disableTwoFactorSignalFull(OAIHttpRequestWorker *worker);
    void getUserSignalFull(OAIHttpRequestWorker *worker, OAIGetUser_200_response summary);
    void getUsersSignalFull(OAIHttpRequestWorker *worker, QList<OAIUser> summary);
    void putUserSignalFull(OAIHttpRequestWorker *worker);
    void requestTwoFactorSignalFull(OAIHttpRequestWorker *worker, QList<OAIRequestTwoFactorResponse> summary);
    void resendEmailToVerifyUserSignalFull(OAIHttpRequestWorker *worker);
    void verifyUserSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use addUserSignalError() instead")
    void addUserSignalE(OAIAddUserResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addUserSignalError(OAIAddUserResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use confirmTwoFactorRequestSignalError() instead")
    void confirmTwoFactorRequestSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void confirmTwoFactorRequestSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delUserSignalError() instead")
    void delUserSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void delUserSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disableTwoFactorSignalError() instead")
    void disableTwoFactorSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void disableTwoFactorSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUserSignalError() instead")
    void getUserSignalE(OAIGetUser_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUserSignalError(OAIGetUser_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersSignalError() instead")
    void getUsersSignalE(QList<OAIUser> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersSignalError(QList<OAIUser> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putUserSignalError() instead")
    void putUserSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void putUserSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestTwoFactorSignalError() instead")
    void requestTwoFactorSignalE(QList<OAIRequestTwoFactorResponse> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestTwoFactorSignalError(QList<OAIRequestTwoFactorResponse> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendEmailToVerifyUserSignalError() instead")
    void resendEmailToVerifyUserSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void resendEmailToVerifyUserSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyUserSignalError() instead")
    void verifyUserSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void verifyUserSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addUserSignalErrorFull() instead")
    void addUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use confirmTwoFactorRequestSignalErrorFull() instead")
    void confirmTwoFactorRequestSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void confirmTwoFactorRequestSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use delUserSignalErrorFull() instead")
    void delUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void delUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disableTwoFactorSignalErrorFull() instead")
    void disableTwoFactorSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void disableTwoFactorSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUserSignalErrorFull() instead")
    void getUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersSignalErrorFull() instead")
    void getUsersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use putUserSignalErrorFull() instead")
    void putUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void putUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestTwoFactorSignalErrorFull() instead")
    void requestTwoFactorSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestTwoFactorSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendEmailToVerifyUserSignalErrorFull() instead")
    void resendEmailToVerifyUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resendEmailToVerifyUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyUserSignalErrorFull() instead")
    void verifyUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void verifyUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
