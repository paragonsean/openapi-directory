/**
 * Vault API
 * Welcome to the Vault API 👋  When you're looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  ``` curl -X POST https://unify.apideck.com/vault/sessions     -H \"Content-Type: application/json\"     -H \"Authorization: Bearer <your-api-key>\"     -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"     -H \"X-APIDECK-APP-ID: <application-id>\"     -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}' ```  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.  This is being handled by the `/authorize` endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIConsumersApi_H
#define OAI_OAIConsumersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIBadRequestResponse.h"
#include "OAIConsumer.h"
#include "OAIConsumerRequestCountsInDateRangeResponse.h"
#include "OAICreateConsumerResponse.h"
#include "OAIDeleteConsumerResponse.h"
#include "OAIGetConsumerResponse.h"
#include "OAIGetConsumersResponse.h"
#include "OAINotFoundResponse.h"
#include "OAIPaymentRequiredResponse.h"
#include "OAIUnauthorizedResponse.h"
#include "OAIUnexpectedErrorResponse.h"
#include "OAIUnprocessableResponse.h"
#include "OAIUpdateConsumerRequest.h"
#include "OAIUpdateConsumerResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIConsumersApi : public QObject {
    Q_OBJECT

public:
    OAIConsumersApi(const int timeOut = 0);
    ~OAIConsumersApi();

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
    * @param[in]  x_apideck_app_id QString [required]
    * @param[in]  consumer_id QString [required]
    * @param[in]  start_datetime QString [required]
    * @param[in]  end_datetime QString [required]
    */
    virtual void consumerRequestCountsAll(const QString &x_apideck_app_id, const QString &consumer_id, const QString &start_datetime, const QString &end_datetime);

    /**
    * @param[in]  x_apideck_app_id QString [required]
    * @param[in]  oai_consumer OAIConsumer [required]
    */
    virtual void consumersAdd(const QString &x_apideck_app_id, const OAIConsumer &oai_consumer);

    /**
    * @param[in]  x_apideck_app_id QString [required]
    * @param[in]  cursor QString [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void consumersAll(const QString &x_apideck_app_id, const ::OpenAPI::OptionalParam<QString> &cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  x_apideck_app_id QString [required]
    * @param[in]  consumer_id QString [required]
    */
    virtual void consumersDelete(const QString &x_apideck_app_id, const QString &consumer_id);

    /**
    * @param[in]  x_apideck_app_id QString [required]
    * @param[in]  consumer_id QString [required]
    */
    virtual void consumersOne(const QString &x_apideck_app_id, const QString &consumer_id);

    /**
    * @param[in]  x_apideck_app_id QString [required]
    * @param[in]  consumer_id QString [required]
    * @param[in]  oai_update_consumer_request OAIUpdateConsumerRequest [required]
    */
    virtual void consumersUpdate(const QString &x_apideck_app_id, const QString &consumer_id, const OAIUpdateConsumerRequest &oai_update_consumer_request);


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

    void consumerRequestCountsAllCallback(OAIHttpRequestWorker *worker);
    void consumersAddCallback(OAIHttpRequestWorker *worker);
    void consumersAllCallback(OAIHttpRequestWorker *worker);
    void consumersDeleteCallback(OAIHttpRequestWorker *worker);
    void consumersOneCallback(OAIHttpRequestWorker *worker);
    void consumersUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void consumerRequestCountsAllSignal(OAIConsumerRequestCountsInDateRangeResponse summary);
    void consumersAddSignal(OAICreateConsumerResponse summary);
    void consumersAllSignal(OAIGetConsumersResponse summary);
    void consumersDeleteSignal(OAIDeleteConsumerResponse summary);
    void consumersOneSignal(OAIGetConsumerResponse summary);
    void consumersUpdateSignal(OAIUpdateConsumerResponse summary);


    void consumerRequestCountsAllSignalFull(OAIHttpRequestWorker *worker, OAIConsumerRequestCountsInDateRangeResponse summary);
    void consumersAddSignalFull(OAIHttpRequestWorker *worker, OAICreateConsumerResponse summary);
    void consumersAllSignalFull(OAIHttpRequestWorker *worker, OAIGetConsumersResponse summary);
    void consumersDeleteSignalFull(OAIHttpRequestWorker *worker, OAIDeleteConsumerResponse summary);
    void consumersOneSignalFull(OAIHttpRequestWorker *worker, OAIGetConsumerResponse summary);
    void consumersUpdateSignalFull(OAIHttpRequestWorker *worker, OAIUpdateConsumerResponse summary);

    Q_DECL_DEPRECATED_X("Use consumerRequestCountsAllSignalError() instead")
    void consumerRequestCountsAllSignalE(OAIConsumerRequestCountsInDateRangeResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerRequestCountsAllSignalError(OAIConsumerRequestCountsInDateRangeResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersAddSignalError() instead")
    void consumersAddSignalE(OAICreateConsumerResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersAddSignalError(OAICreateConsumerResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersAllSignalError() instead")
    void consumersAllSignalE(OAIGetConsumersResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersAllSignalError(OAIGetConsumersResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersDeleteSignalError() instead")
    void consumersDeleteSignalE(OAIDeleteConsumerResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersDeleteSignalError(OAIDeleteConsumerResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersOneSignalError() instead")
    void consumersOneSignalE(OAIGetConsumerResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersOneSignalError(OAIGetConsumerResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersUpdateSignalError() instead")
    void consumersUpdateSignalE(OAIUpdateConsumerResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersUpdateSignalError(OAIUpdateConsumerResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use consumerRequestCountsAllSignalErrorFull() instead")
    void consumerRequestCountsAllSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumerRequestCountsAllSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersAddSignalErrorFull() instead")
    void consumersAddSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersAddSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersAllSignalErrorFull() instead")
    void consumersAllSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersAllSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersDeleteSignalErrorFull() instead")
    void consumersDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersOneSignalErrorFull() instead")
    void consumersOneSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersOneSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use consumersUpdateSignalErrorFull() instead")
    void consumersUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void consumersUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
