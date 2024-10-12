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

#ifndef OAI_OAIRegisterApi_H
#define OAI_OAIRegisterApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIListRegistrations_200_response.h"
#include "OAIRegisterUser.h"
#include "OAIResendEmailToVerifyRegistration_request.h"
#include "OAIResendEmailToVerifyUser_request.h"
#include "OAIUserRegistration.h"
#include "OAIUserRegistrationAcceptOrReject.h"
#include "OAIUserRegistrationRequest.h"
#include "OAIVerifyRegistrationEmail_request.h"
#include "OAIVerifyUser_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRegisterApi : public QObject {
    Q_OBJECT

public:
    OAIRegisterApi(const int timeOut = 0);
    ~OAIRegisterApi();

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
    * @param[in]  registration_id qint32 [required]
    * @param[in]  oai_user_registration_accept_or_reject OAIUserRegistrationAcceptOrReject [optional]
    */
    virtual void acceptRegistration(const qint32 &registration_id, const ::OpenAPI::OptionalParam<OAIUserRegistrationAcceptOrReject> &oai_user_registration_accept_or_reject = ::OpenAPI::OptionalParam<OAIUserRegistrationAcceptOrReject>());

    /**
    * @param[in]  registration_id qint32 [required]
    */
    virtual void deleteRegistration(const qint32 &registration_id);

    /**
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  search QString [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void listRegistrations(const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_register_user OAIRegisterUser [required]
    */
    virtual void registerUser(const OAIRegisterUser &oai_register_user);

    /**
    * @param[in]  registration_id qint32 [required]
    * @param[in]  oai_user_registration_accept_or_reject OAIUserRegistrationAcceptOrReject [optional]
    */
    virtual void rejectRegistration(const qint32 &registration_id, const ::OpenAPI::OptionalParam<OAIUserRegistrationAcceptOrReject> &oai_user_registration_accept_or_reject = ::OpenAPI::OptionalParam<OAIUserRegistrationAcceptOrReject>());

    /**
    * @param[in]  oai_user_registration_request OAIUserRegistrationRequest [optional]
    */
    virtual void requestRegistration(const ::OpenAPI::OptionalParam<OAIUserRegistrationRequest> &oai_user_registration_request = ::OpenAPI::OptionalParam<OAIUserRegistrationRequest>());

    /**
    * @param[in]  oai_resend_email_to_verify_registration_request OAIResendEmailToVerifyRegistration_request [optional]
    */
    virtual void resendEmailToVerifyRegistration(const ::OpenAPI::OptionalParam<OAIResendEmailToVerifyRegistration_request> &oai_resend_email_to_verify_registration_request = ::OpenAPI::OptionalParam<OAIResendEmailToVerifyRegistration_request>());

    /**
    * @param[in]  oai_resend_email_to_verify_user_request OAIResendEmailToVerifyUser_request [optional]
    */
    virtual void resendEmailToVerifyUser(const ::OpenAPI::OptionalParam<OAIResendEmailToVerifyUser_request> &oai_resend_email_to_verify_user_request = ::OpenAPI::OptionalParam<OAIResendEmailToVerifyUser_request>());

    /**
    * @param[in]  registration_id qint32 [required]
    * @param[in]  oai_verify_registration_email_request OAIVerifyRegistrationEmail_request [optional]
    */
    virtual void verifyRegistrationEmail(const qint32 &registration_id, const ::OpenAPI::OptionalParam<OAIVerifyRegistrationEmail_request> &oai_verify_registration_email_request = ::OpenAPI::OptionalParam<OAIVerifyRegistrationEmail_request>());

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

    void acceptRegistrationCallback(OAIHttpRequestWorker *worker);
    void deleteRegistrationCallback(OAIHttpRequestWorker *worker);
    void listRegistrationsCallback(OAIHttpRequestWorker *worker);
    void registerUserCallback(OAIHttpRequestWorker *worker);
    void rejectRegistrationCallback(OAIHttpRequestWorker *worker);
    void requestRegistrationCallback(OAIHttpRequestWorker *worker);
    void resendEmailToVerifyRegistrationCallback(OAIHttpRequestWorker *worker);
    void resendEmailToVerifyUserCallback(OAIHttpRequestWorker *worker);
    void verifyRegistrationEmailCallback(OAIHttpRequestWorker *worker);
    void verifyUserCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void acceptRegistrationSignal();
    void deleteRegistrationSignal();
    void listRegistrationsSignal(OAIListRegistrations_200_response summary);
    void registerUserSignal();
    void rejectRegistrationSignal();
    void requestRegistrationSignal(OAIUserRegistration summary);
    void resendEmailToVerifyRegistrationSignal();
    void resendEmailToVerifyUserSignal();
    void verifyRegistrationEmailSignal();
    void verifyUserSignal();


    void acceptRegistrationSignalFull(OAIHttpRequestWorker *worker);
    void deleteRegistrationSignalFull(OAIHttpRequestWorker *worker);
    void listRegistrationsSignalFull(OAIHttpRequestWorker *worker, OAIListRegistrations_200_response summary);
    void registerUserSignalFull(OAIHttpRequestWorker *worker);
    void rejectRegistrationSignalFull(OAIHttpRequestWorker *worker);
    void requestRegistrationSignalFull(OAIHttpRequestWorker *worker, OAIUserRegistration summary);
    void resendEmailToVerifyRegistrationSignalFull(OAIHttpRequestWorker *worker);
    void resendEmailToVerifyUserSignalFull(OAIHttpRequestWorker *worker);
    void verifyRegistrationEmailSignalFull(OAIHttpRequestWorker *worker);
    void verifyUserSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use acceptRegistrationSignalError() instead")
    void acceptRegistrationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void acceptRegistrationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRegistrationSignalError() instead")
    void deleteRegistrationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRegistrationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRegistrationsSignalError() instead")
    void listRegistrationsSignalE(OAIListRegistrations_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRegistrationsSignalError(OAIListRegistrations_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use registerUserSignalError() instead")
    void registerUserSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void registerUserSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rejectRegistrationSignalError() instead")
    void rejectRegistrationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void rejectRegistrationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRegistrationSignalError() instead")
    void requestRegistrationSignalE(OAIUserRegistration summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRegistrationSignalError(OAIUserRegistration summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendEmailToVerifyRegistrationSignalError() instead")
    void resendEmailToVerifyRegistrationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void resendEmailToVerifyRegistrationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendEmailToVerifyUserSignalError() instead")
    void resendEmailToVerifyUserSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void resendEmailToVerifyUserSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyRegistrationEmailSignalError() instead")
    void verifyRegistrationEmailSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void verifyRegistrationEmailSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyUserSignalError() instead")
    void verifyUserSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void verifyUserSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use acceptRegistrationSignalErrorFull() instead")
    void acceptRegistrationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void acceptRegistrationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRegistrationSignalErrorFull() instead")
    void deleteRegistrationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRegistrationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRegistrationsSignalErrorFull() instead")
    void listRegistrationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRegistrationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use registerUserSignalErrorFull() instead")
    void registerUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void registerUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rejectRegistrationSignalErrorFull() instead")
    void rejectRegistrationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rejectRegistrationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRegistrationSignalErrorFull() instead")
    void requestRegistrationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRegistrationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendEmailToVerifyRegistrationSignalErrorFull() instead")
    void resendEmailToVerifyRegistrationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resendEmailToVerifyRegistrationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendEmailToVerifyUserSignalErrorFull() instead")
    void resendEmailToVerifyUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resendEmailToVerifyUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifyRegistrationEmailSignalErrorFull() instead")
    void verifyRegistrationEmailSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void verifyRegistrationEmailSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
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
