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

#include "OAIConnectionsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIConnectionsApi::OAIConnectionsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIConnectionsApi::~OAIConnectionsApi() {
}

void OAIConnectionsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://unify.apideck.com"),
    "Production server",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("connectionSettingsAll", defaultConf);
    _serverIndices.insert("connectionSettingsAll", 0);
    _serverConfigs.insert("connectionSettingsUpdate", defaultConf);
    _serverIndices.insert("connectionSettingsUpdate", 0);
    _serverConfigs.insert("connectionsAdd", defaultConf);
    _serverIndices.insert("connectionsAdd", 0);
    _serverConfigs.insert("connectionsAll", defaultConf);
    _serverIndices.insert("connectionsAll", 0);
    _serverConfigs.insert("connectionsAuthorize", defaultConf);
    _serverIndices.insert("connectionsAuthorize", 0);
    _serverConfigs.insert("connectionsCallback", defaultConf);
    _serverIndices.insert("connectionsCallback", 0);
    _serverConfigs.insert("connectionsDelete", defaultConf);
    _serverIndices.insert("connectionsDelete", 0);
    _serverConfigs.insert("connectionsImport", defaultConf);
    _serverIndices.insert("connectionsImport", 0);
    _serverConfigs.insert("connectionsOne", defaultConf);
    _serverIndices.insert("connectionsOne", 0);
    _serverConfigs.insert("connectionsRevoke", defaultConf);
    _serverIndices.insert("connectionsRevoke", 0);
    _serverConfigs.insert("connectionsToken", defaultConf);
    _serverIndices.insert("connectionsToken", 0);
    _serverConfigs.insert("connectionsUpdate", defaultConf);
    _serverIndices.insert("connectionsUpdate", 0);
    _serverConfigs.insert("customFieldsAll", defaultConf);
    _serverIndices.insert("customFieldsAll", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIConnectionsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIConnectionsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIConnectionsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIConnectionsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIConnectionsApi::setUsername(const QString &username) {
    _username = username;
}

void OAIConnectionsApi::setPassword(const QString &password) {
    _password = password;
}


void OAIConnectionsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIConnectionsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIConnectionsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAIConnectionsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIConnectionsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIConnectionsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIConnectionsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIConnectionsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIConnectionsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIConnectionsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIConnectionsApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAIConnectionsApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAIConnectionsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAIConnectionsApi::connectionSettingsAll(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &unified_api, const QString &service_id, const QString &resource) {
    QString fullPath = QString(_serverConfigs["connectionSettingsAll"][_serverIndices.value("connectionSettingsAll")].URL()+"/vault/connections/{unified_api}/{service_id}/{resource}/config");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString resourcePathParam("{");
        resourcePathParam.append("resource").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "resource", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"resource"+pathSuffix : pathPrefix;
        fullPath.replace(resourcePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(resource)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionSettingsAllCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionSettingsAllCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetConnectionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionSettingsAllSignal(output);
        Q_EMIT connectionSettingsAllSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionSettingsAllSignalE(output, error_type, error_str);
        Q_EMIT connectionSettingsAllSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionSettingsAllSignalError(output, error_type, error_str);
        Q_EMIT connectionSettingsAllSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionSettingsUpdate(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &service_id, const QString &unified_api, const QString &resource, const OAIConnection &oai_connection) {
    QString fullPath = QString(_serverConfigs["connectionSettingsUpdate"][_serverIndices.value("connectionSettingsUpdate")].URL()+"/vault/connections/{unified_api}/{service_id}/{resource}/config");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    
    {
        QString resourcePathParam("{");
        resourcePathParam.append("resource").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "resource", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"resource"+pathSuffix : pathPrefix;
        fullPath.replace(resourcePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(resource)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PATCH");

    {

        
        QByteArray output = oai_connection.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionSettingsUpdateCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionSettingsUpdateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateConnectionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionSettingsUpdateSignal(output);
        Q_EMIT connectionSettingsUpdateSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionSettingsUpdateSignalE(output, error_type, error_str);
        Q_EMIT connectionSettingsUpdateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionSettingsUpdateSignalError(output, error_type, error_str);
        Q_EMIT connectionSettingsUpdateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsAdd(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &service_id, const QString &unified_api, const OAIConnection &oai_connection) {
    QString fullPath = QString(_serverConfigs["connectionsAdd"][_serverIndices.value("connectionsAdd")].URL()+"/vault/connections/{unified_api}/{service_id}");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_connection.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsAddCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsAddCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateConnectionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsAddSignal(output);
        Q_EMIT connectionsAddSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsAddSignalE(output, error_type, error_str);
        Q_EMIT connectionsAddSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsAddSignalError(output, error_type, error_str);
        Q_EMIT connectionsAddSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsAll(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const ::OpenAPI::OptionalParam<QString> &api, const ::OpenAPI::OptionalParam<bool> &configured) {
    QString fullPath = QString(_serverConfigs["connectionsAll"][_serverIndices.value("connectionsAll")].URL()+"/vault/connections");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (api.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "api", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("api")).append(querySuffix).append(QUrl::toPercentEncoding(api.stringValue()));
    }
    if (configured.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "configured", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("configured")).append(querySuffix).append(QUrl::toPercentEncoding(configured.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsAllCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsAllCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetConnectionsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsAllSignal(output);
        Q_EMIT connectionsAllSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsAllSignalE(output, error_type, error_str);
        Q_EMIT connectionsAllSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsAllSignalError(output, error_type, error_str);
        Q_EMIT connectionsAllSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsAuthorize(const QString &service_id, const QString &application_id, const QString &state, const QString &redirect_uri, const ::OpenAPI::OptionalParam<QList<QString>> &scope) {
    QString fullPath = QString(_serverConfigs["connectionsAuthorize"][_serverIndices.value("connectionsAuthorize")].URL()+"/vault/authorize/{service_id}/{application_id}");
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString application_idPathParam("{");
        application_idPathParam.append("application_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "application_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"application_id"+pathSuffix : pathPrefix;
        fullPath.replace(application_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(application_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "state", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("state")).append(querySuffix).append(QUrl::toPercentEncoding(state));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "redirect_uri", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("redirect_uri")).append(querySuffix).append(QUrl::toPercentEncoding(redirect_uri));
    }
    if (scope.hasValue())
    {
        queryStyle = "spaceDelimited";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "scope", false);
        if (scope.value().size() > 0) {
            if (QString("ssv").indexOf("multi") == 0) {
                for (QString t : scope.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("scope=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("ssv").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("scope").append(querySuffix);
                qint32 count = 0;
                for (QString t : scope.value()) {
                    if (count > 0) {
                        fullPath.append((false)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("ssv").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("scope").append(querySuffix);
                qint32 count = 0;
                for (QString t : scope.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("ssv").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("scope").append(querySuffix);
                qint32 count = 0;
                for (QString t : scope.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("ssv").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("scope").append(querySuffix);
                qint32 count = 0;
                for (QString t : scope.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("ssv").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("scope").append(querySuffix);
                qint32 count = 0;
                for (QString t : scope.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsAuthorizeCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsAuthorizeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUnexpectedErrorResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsAuthorizeSignal(output);
        Q_EMIT connectionsAuthorizeSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsAuthorizeSignalE(output, error_type, error_str);
        Q_EMIT connectionsAuthorizeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsAuthorizeSignalError(output, error_type, error_str);
        Q_EMIT connectionsAuthorizeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsCallback(const QString &state, const QString &code) {
    QString fullPath = QString(_serverConfigs["connectionsCallback"][_serverIndices.value("connectionsCallback")].URL()+"/vault/callback");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "state", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("state")).append(querySuffix).append(QUrl::toPercentEncoding(state));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "code", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("code")).append(querySuffix).append(QUrl::toPercentEncoding(code));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsCallbackCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsCallbackCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUnexpectedErrorResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsCallbackSignal(output);
        Q_EMIT connectionsCallbackSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsCallbackSignalE(output, error_type, error_str);
        Q_EMIT connectionsCallbackSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsCallbackSignalError(output, error_type, error_str);
        Q_EMIT connectionsCallbackSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsDelete(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &service_id, const QString &unified_api) {
    QString fullPath = QString(_serverConfigs["connectionsDelete"][_serverIndices.value("connectionsDelete")].URL()+"/vault/connections/{unified_api}/{service_id}");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsDeleteCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsDeleteSignal();
        Q_EMIT connectionsDeleteSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsDeleteSignalE(error_type, error_str);
        Q_EMIT connectionsDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsDeleteSignalError(error_type, error_str);
        Q_EMIT connectionsDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsImport(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &service_id, const QString &unified_api, const OAIConnectionImportData &oai_connection_import_data) {
    QString fullPath = QString(_serverConfigs["connectionsImport"][_serverIndices.value("connectionsImport")].URL()+"/vault/connections/{unified_api}/{service_id}/import");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_connection_import_data.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsImportCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsImportCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateConnectionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsImportSignal(output);
        Q_EMIT connectionsImportSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsImportSignalE(output, error_type, error_str);
        Q_EMIT connectionsImportSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsImportSignalError(output, error_type, error_str);
        Q_EMIT connectionsImportSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsOne(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &service_id, const QString &unified_api) {
    QString fullPath = QString(_serverConfigs["connectionsOne"][_serverIndices.value("connectionsOne")].URL()+"/vault/connections/{unified_api}/{service_id}");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsOneCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsOneCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetConnectionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsOneSignal(output);
        Q_EMIT connectionsOneSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsOneSignalE(output, error_type, error_str);
        Q_EMIT connectionsOneSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsOneSignalError(output, error_type, error_str);
        Q_EMIT connectionsOneSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsRevoke(const QString &service_id, const QString &application_id, const QString &state, const QString &redirect_uri) {
    QString fullPath = QString(_serverConfigs["connectionsRevoke"][_serverIndices.value("connectionsRevoke")].URL()+"/vault/revoke/{service_id}/{application_id}");
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString application_idPathParam("{");
        application_idPathParam.append("application_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "application_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"application_id"+pathSuffix : pathPrefix;
        fullPath.replace(application_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(application_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "state", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("state")).append(querySuffix).append(QUrl::toPercentEncoding(state));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "redirect_uri", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("redirect_uri")).append(querySuffix).append(QUrl::toPercentEncoding(redirect_uri));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsRevokeCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsRevokeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUnexpectedErrorResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsRevokeSignal(output);
        Q_EMIT connectionsRevokeSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsRevokeSignalE(output, error_type, error_str);
        Q_EMIT connectionsRevokeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsRevokeSignalError(output, error_type, error_str);
        Q_EMIT connectionsRevokeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsToken(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &service_id, const QString &unified_api, const ::OpenAPI::OptionalParam<OAIObject> &body) {
    QString fullPath = QString(_serverConfigs["connectionsToken"][_serverIndices.value("connectionsToken")].URL()+"/vault/connections/{unified_api}/{service_id}/token");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (body.hasValue()){

        
        QByteArray output = body.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsTokenCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsTokenCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetConnectionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsTokenSignal(output);
        Q_EMIT connectionsTokenSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsTokenSignalE(output, error_type, error_str);
        Q_EMIT connectionsTokenSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsTokenSignalError(output, error_type, error_str);
        Q_EMIT connectionsTokenSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::connectionsUpdate(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &service_id, const QString &unified_api, const OAIConnection &oai_connection) {
    QString fullPath = QString(_serverConfigs["connectionsUpdate"][_serverIndices.value("connectionsUpdate")].URL()+"/vault/connections/{unified_api}/{service_id}");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PATCH");

    {

        
        QByteArray output = oai_connection.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::connectionsUpdateCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::connectionsUpdateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateConnectionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connectionsUpdateSignal(output);
        Q_EMIT connectionsUpdateSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT connectionsUpdateSignalE(output, error_type, error_str);
        Q_EMIT connectionsUpdateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connectionsUpdateSignalError(output, error_type, error_str);
        Q_EMIT connectionsUpdateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::customFieldsAll(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &unified_api, const QString &service_id, const QString &resource) {
    QString fullPath = QString(_serverConfigs["customFieldsAll"][_serverIndices.value("customFieldsAll")].URL()+"/vault/connections/{unified_api}/{service_id}/{resource}/custom-fields");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    
    {
        QString unified_apiPathParam("{");
        unified_apiPathParam.append("unified_api").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "unified_api", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"unified_api"+pathSuffix : pathPrefix;
        fullPath.replace(unified_apiPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(unified_api)));
    }
    
    {
        QString service_idPathParam("{");
        service_idPathParam.append("service_id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "service_id", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"service_id"+pathSuffix : pathPrefix;
        fullPath.replace(service_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(service_id)));
    }
    
    {
        QString resourcePathParam("{");
        resourcePathParam.append("resource").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "resource", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"resource"+pathSuffix : pathPrefix;
        fullPath.replace(resourcePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(resource)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(x_apideck_consumer_id).isEmpty()) {
            input.headers.insert("x-apideck-consumer-id", ::OpenAPI::toStringValue(x_apideck_consumer_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_app_id).isEmpty()) {
            input.headers.insert("x-apideck-app-id", ::OpenAPI::toStringValue(x_apideck_app_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConnectionsApi::customFieldsAllCallback);
    connect(this, &OAIConnectionsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConnectionsApi::customFieldsAllCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetCustomFieldsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT customFieldsAllSignal(output);
        Q_EMIT customFieldsAllSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT customFieldsAllSignalE(output, error_type, error_str);
        Q_EMIT customFieldsAllSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT customFieldsAllSignalError(output, error_type, error_str);
        Q_EMIT customFieldsAllSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConnectionsApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
