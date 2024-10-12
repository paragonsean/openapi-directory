/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPayeeInvitationApi_H
#define OAI_OAIPayeeInvitationApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreatePayeeV3_request.h"
#include "OAICreatePayeesCSVResponseV3.h"
#include "OAICreatePayeesCSVResponseV4.h"
#include "OAICreatePayeesRequestV3.h"
#include "OAICreatePayeesRequestV4.h"
#include "OAIInline_response_400.h"
#include "OAIInline_response_401.h"
#include "OAIInline_response_403.h"
#include "OAIInline_response_404.h"
#include "OAIInline_response_409.h"
#include "OAIInvitePayeeRequestV3.h"
#include "OAIInvitePayeeRequestV4.h"
#include "OAIPagedPayeeInvitationStatusResponseV3.h"
#include "OAIPagedPayeeInvitationStatusResponseV4.h"
#include "OAIQueryBatchResponseV3.h"
#include "OAIQueryBatchResponseV4.h"
#include "OAIV4CreatePayee_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPayeeInvitationApi : public QObject {
    Q_OBJECT

public:
    OAIPayeeInvitationApi(const int timeOut = 0);
    ~OAIPayeeInvitationApi();

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
    * @param[in]  oai_create_payees_request_v3 OAICreatePayeesRequestV3 [optional]
    */
    Q_DECL_DEPRECATED virtual void createPayeeV3(const ::OpenAPI::OptionalParam<OAICreatePayeesRequestV3> &oai_create_payees_request_v3 = ::OpenAPI::OptionalParam<OAICreatePayeesRequestV3>());

    /**
    * @param[in]  payor_id QString [required]
    * @param[in]  payee_id QString [optional]
    * @param[in]  invitation_status QString [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    Q_DECL_DEPRECATED virtual void getPayeesInvitationStatusV3(const QString &payor_id, const ::OpenAPI::OptionalParam<QString> &payee_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &invitation_status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  payor_id QString [required]
    * @param[in]  payee_id QString [optional]
    * @param[in]  invitation_status QString [optional]
    * @param[in]  page qint32 [optional]
    * @param[in]  page_size qint32 [optional]
    */
    virtual void getPayeesInvitationStatusV4(const QString &payor_id, const ::OpenAPI::OptionalParam<QString> &payee_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &invitation_status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  batch_id QString [required]
    */
    Q_DECL_DEPRECATED virtual void queryBatchStatusV3(const QString &batch_id);

    /**
    * @param[in]  batch_id QString [required]
    */
    virtual void queryBatchStatusV4(const QString &batch_id);

    /**
    * @param[in]  payee_id QString [required]
    * @param[in]  oai_invite_payee_request_v3 OAIInvitePayeeRequestV3 [required]
    */
    Q_DECL_DEPRECATED virtual void resendPayeeInviteV3(const QString &payee_id, const OAIInvitePayeeRequestV3 &oai_invite_payee_request_v3);

    /**
    * @param[in]  payee_id QString [required]
    * @param[in]  oai_invite_payee_request_v4 OAIInvitePayeeRequestV4 [required]
    */
    virtual void resendPayeeInviteV4(const QString &payee_id, const OAIInvitePayeeRequestV4 &oai_invite_payee_request_v4);

    /**
    * @param[in]  oai_create_payees_request_v4 OAICreatePayeesRequestV4 [optional]
    */
    virtual void v4CreatePayee(const ::OpenAPI::OptionalParam<OAICreatePayeesRequestV4> &oai_create_payees_request_v4 = ::OpenAPI::OptionalParam<OAICreatePayeesRequestV4>());


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

    void createPayeeV3Callback(OAIHttpRequestWorker *worker);
    void getPayeesInvitationStatusV3Callback(OAIHttpRequestWorker *worker);
    void getPayeesInvitationStatusV4Callback(OAIHttpRequestWorker *worker);
    void queryBatchStatusV3Callback(OAIHttpRequestWorker *worker);
    void queryBatchStatusV4Callback(OAIHttpRequestWorker *worker);
    void resendPayeeInviteV3Callback(OAIHttpRequestWorker *worker);
    void resendPayeeInviteV4Callback(OAIHttpRequestWorker *worker);
    void v4CreatePayeeCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createPayeeV3Signal(OAICreatePayeesCSVResponseV3 summary);
    void getPayeesInvitationStatusV3Signal(OAIPagedPayeeInvitationStatusResponseV3 summary);
    void getPayeesInvitationStatusV4Signal(OAIPagedPayeeInvitationStatusResponseV4 summary);
    void queryBatchStatusV3Signal(OAIQueryBatchResponseV3 summary);
    void queryBatchStatusV4Signal(OAIQueryBatchResponseV4 summary);
    void resendPayeeInviteV3Signal();
    void resendPayeeInviteV4Signal();
    void v4CreatePayeeSignal(OAICreatePayeesCSVResponseV4 summary);


    void createPayeeV3SignalFull(OAIHttpRequestWorker *worker, OAICreatePayeesCSVResponseV3 summary);
    void getPayeesInvitationStatusV3SignalFull(OAIHttpRequestWorker *worker, OAIPagedPayeeInvitationStatusResponseV3 summary);
    void getPayeesInvitationStatusV4SignalFull(OAIHttpRequestWorker *worker, OAIPagedPayeeInvitationStatusResponseV4 summary);
    void queryBatchStatusV3SignalFull(OAIHttpRequestWorker *worker, OAIQueryBatchResponseV3 summary);
    void queryBatchStatusV4SignalFull(OAIHttpRequestWorker *worker, OAIQueryBatchResponseV4 summary);
    void resendPayeeInviteV3SignalFull(OAIHttpRequestWorker *worker);
    void resendPayeeInviteV4SignalFull(OAIHttpRequestWorker *worker);
    void v4CreatePayeeSignalFull(OAIHttpRequestWorker *worker, OAICreatePayeesCSVResponseV4 summary);

    Q_DECL_DEPRECATED_X("Use createPayeeV3SignalError() instead")
    void createPayeeV3SignalE(OAICreatePayeesCSVResponseV3 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createPayeeV3SignalError(OAICreatePayeesCSVResponseV3 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPayeesInvitationStatusV3SignalError() instead")
    void getPayeesInvitationStatusV3SignalE(OAIPagedPayeeInvitationStatusResponseV3 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPayeesInvitationStatusV3SignalError(OAIPagedPayeeInvitationStatusResponseV3 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPayeesInvitationStatusV4SignalError() instead")
    void getPayeesInvitationStatusV4SignalE(OAIPagedPayeeInvitationStatusResponseV4 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPayeesInvitationStatusV4SignalError(OAIPagedPayeeInvitationStatusResponseV4 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryBatchStatusV3SignalError() instead")
    void queryBatchStatusV3SignalE(OAIQueryBatchResponseV3 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void queryBatchStatusV3SignalError(OAIQueryBatchResponseV3 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryBatchStatusV4SignalError() instead")
    void queryBatchStatusV4SignalE(OAIQueryBatchResponseV4 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void queryBatchStatusV4SignalError(OAIQueryBatchResponseV4 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendPayeeInviteV3SignalError() instead")
    void resendPayeeInviteV3SignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void resendPayeeInviteV3SignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendPayeeInviteV4SignalError() instead")
    void resendPayeeInviteV4SignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void resendPayeeInviteV4SignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4CreatePayeeSignalError() instead")
    void v4CreatePayeeSignalE(OAICreatePayeesCSVResponseV4 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void v4CreatePayeeSignalError(OAICreatePayeesCSVResponseV4 summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createPayeeV3SignalErrorFull() instead")
    void createPayeeV3SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createPayeeV3SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPayeesInvitationStatusV3SignalErrorFull() instead")
    void getPayeesInvitationStatusV3SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPayeesInvitationStatusV3SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPayeesInvitationStatusV4SignalErrorFull() instead")
    void getPayeesInvitationStatusV4SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPayeesInvitationStatusV4SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryBatchStatusV3SignalErrorFull() instead")
    void queryBatchStatusV3SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void queryBatchStatusV3SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryBatchStatusV4SignalErrorFull() instead")
    void queryBatchStatusV4SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void queryBatchStatusV4SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendPayeeInviteV3SignalErrorFull() instead")
    void resendPayeeInviteV3SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resendPayeeInviteV3SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resendPayeeInviteV4SignalErrorFull() instead")
    void resendPayeeInviteV4SignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resendPayeeInviteV4SignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v4CreatePayeeSignalErrorFull() instead")
    void v4CreatePayeeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v4CreatePayeeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
