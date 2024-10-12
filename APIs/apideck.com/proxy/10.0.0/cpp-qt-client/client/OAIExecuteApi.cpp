/**
 * Proxy API
 * Welcome to the Proxy API.  You can use this API to access all Proxy API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                               | Type   | Required | Description | | ---------------------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | | Authorization                      | String | Yes      | Bearer API KEY | | x-apideck-app-id                   | String | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys. | | x-apideck-consumer-id              | String | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app.                       | | x-apideck-downstream-url           | String | Yes      | Downstream URL to forward the request too | | x-apideck-downstream-authorization | String | No       | Downstream authorization header. This will skip the Vault token injection. | | x-apideck-downstream-method        | String | No       | Downstream method. If not provided the upstream method will be inherited, depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | | x-apideck-service-id               | String | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.                                   |  ## Authorization  You can interact with the API through the authorization methods below.  ### apiKey  To use API you have to sign up and get your own API key. Unify API accounts have sandbox mode and live mode API keys. To change modes just use the appropriate key to get a live or test object. You can find your API keys on the unify settings of your Apideck app. Your Apideck application_id can also be found on the same page.  Authenticate your API requests by including your test or live secret API key in the request header.  - Bearer authorization header: Authorization: Bearer <your-apideck-api-key> - Application id header: x-apideck-app-id: <your-apideck-app-id>   You should use the public keys on the SDKs and the secret keys to authenticate API requests.  **Do not share or include your secret API keys on client side code.** Your API keys carry significant privileges. Please ensure to keep them 100% secure and be sure to not share your secret API keys in areas that are publicly accessible like GitHub.  Learn how to set the Authorization header inside Postman https://learning.postman.com/docs/postman/sending-api-requests/authorization/#api-key  Go to Unify to grab your API KEY https://app.apideck.com/unify/api-keys  | Security Scheme Type      | HTTP   | | ------------------------- | ------ | | HTTP Authorization Scheme | bearer |  ### applicationId  The ID of your Unify application  | Security Scheme Type  | API Key          | | --------------------- | ---------------- | | Header parameter name | x-apideck-app-id |  ## Static IP  Some of the APIs you want to use can require a static IP. Apideck's static IP feature allows you to the Proxy API with a fixed IP avoiding the need for you to set up your own infrastructure. This feature is currently available to all Apideck customers. To use this feature, the API Vendor will need to whitelist the associated static IP addresses. The provided static IP addresses are fixed to their specified region and shared by all customers who use this feature.  - EU Central 1: **18.197.244.247** - Other: upcoming    More info about our data security can be found at [https://compliance.apideck.com/](https://compliance.apideck.com/)  ## Limitations  ### Timeout  The request timeout is set at 30 seconds.  ### Response Size  The Proxy API has no response size limit. For responses larger than 2MB, the Proxy API will redirect to a temporary URL. In this case the usual Apideck response headers will be returned in the redirect response. Most HTTP clients will handle this redirect automatically.  ``` GET /proxy < 301 Moved Permanently < x-apideck-request-id: {{requestId}} < Location: {{temporaryUrl}}  GET {{temporaryUrl}} < {{responseBody}} ```  ## SDKs and API Clients  Upcoming. [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created. | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body. | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource. | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue. | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request. | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource. | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later. | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue. |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExecuteApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIExecuteApi::OAIExecuteApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIExecuteApi::~OAIExecuteApi() {
}

void OAIExecuteApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://unify.apideck.com"),
    "Production server",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("deleteProxy", defaultConf);
    _serverIndices.insert("deleteProxy", 0);
    _serverConfigs.insert("getProxy", defaultConf);
    _serverIndices.insert("getProxy", 0);
    _serverConfigs.insert("optionsProxy", defaultConf);
    _serverIndices.insert("optionsProxy", 0);
    _serverConfigs.insert("patchProxy", defaultConf);
    _serverIndices.insert("patchProxy", 0);
    _serverConfigs.insert("postProxy", defaultConf);
    _serverIndices.insert("postProxy", 0);
    _serverConfigs.insert("putProxy", defaultConf);
    _serverIndices.insert("putProxy", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIExecuteApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIExecuteApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIExecuteApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIExecuteApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIExecuteApi::setUsername(const QString &username) {
    _username = username;
}

void OAIExecuteApi::setPassword(const QString &password) {
    _password = password;
}


void OAIExecuteApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIExecuteApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIExecuteApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIExecuteApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIExecuteApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIExecuteApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIExecuteApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIExecuteApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIExecuteApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIExecuteApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIExecuteApi::getParamStylePrefix(const QString &style) {
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

QString OAIExecuteApi::getParamStyleSuffix(const QString &style) {
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

QString OAIExecuteApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIExecuteApi::deleteProxy(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &x_apideck_service_id, const QString &x_apideck_downstream_url, const ::OpenAPI::OptionalParam<QString> &x_apideck_downstream_authorization) {
    QString fullPath = QString(_serverConfigs["deleteProxy"][_serverIndices.value("deleteProxy")].URL()+"/proxy");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
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
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_service_id).isEmpty()) {
            input.headers.insert("x-apideck-service-id", ::OpenAPI::toStringValue(x_apideck_service_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_url).isEmpty()) {
            input.headers.insert("x-apideck-downstream-url", ::OpenAPI::toStringValue(x_apideck_downstream_url));
        }
        }
    if (x_apideck_downstream_authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()).isEmpty()) {
            input.headers.insert("x-apideck-downstream-authorization", ::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIExecuteApi::deleteProxyCallback);
    connect(this, &OAIExecuteApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIExecuteApi::deleteProxyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteProxySignal(output);
        Q_EMIT deleteProxySignalFull(worker, output);
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

        Q_EMIT deleteProxySignalE(output, error_type, error_str);
        Q_EMIT deleteProxySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteProxySignalError(output, error_type, error_str);
        Q_EMIT deleteProxySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIExecuteApi::getProxy(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &x_apideck_service_id, const QString &x_apideck_downstream_url, const ::OpenAPI::OptionalParam<QString> &x_apideck_downstream_authorization) {
    QString fullPath = QString(_serverConfigs["getProxy"][_serverIndices.value("getProxy")].URL()+"/proxy");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
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
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_service_id).isEmpty()) {
            input.headers.insert("x-apideck-service-id", ::OpenAPI::toStringValue(x_apideck_service_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_url).isEmpty()) {
            input.headers.insert("x-apideck-downstream-url", ::OpenAPI::toStringValue(x_apideck_downstream_url));
        }
        }
    if (x_apideck_downstream_authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()).isEmpty()) {
            input.headers.insert("x-apideck-downstream-authorization", ::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIExecuteApi::getProxyCallback);
    connect(this, &OAIExecuteApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIExecuteApi::getProxyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getProxySignal(output);
        Q_EMIT getProxySignalFull(worker, output);
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

        Q_EMIT getProxySignalE(output, error_type, error_str);
        Q_EMIT getProxySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getProxySignalError(output, error_type, error_str);
        Q_EMIT getProxySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIExecuteApi::optionsProxy(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &x_apideck_service_id, const QString &x_apideck_downstream_url, const ::OpenAPI::OptionalParam<QString> &x_apideck_downstream_authorization) {
    QString fullPath = QString(_serverConfigs["optionsProxy"][_serverIndices.value("optionsProxy")].URL()+"/proxy");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "OPTIONS");


    
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
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_service_id).isEmpty()) {
            input.headers.insert("x-apideck-service-id", ::OpenAPI::toStringValue(x_apideck_service_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_url).isEmpty()) {
            input.headers.insert("x-apideck-downstream-url", ::OpenAPI::toStringValue(x_apideck_downstream_url));
        }
        }
    if (x_apideck_downstream_authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()).isEmpty()) {
            input.headers.insert("x-apideck-downstream-authorization", ::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIExecuteApi::optionsProxyCallback);
    connect(this, &OAIExecuteApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIExecuteApi::optionsProxyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT optionsProxySignal(output);
        Q_EMIT optionsProxySignalFull(worker, output);
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

        Q_EMIT optionsProxySignalE(output, error_type, error_str);
        Q_EMIT optionsProxySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT optionsProxySignalError(output, error_type, error_str);
        Q_EMIT optionsProxySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIExecuteApi::patchProxy(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &x_apideck_service_id, const QString &x_apideck_downstream_url, const ::OpenAPI::OptionalParam<QString> &x_apideck_downstream_authorization, const ::OpenAPI::OptionalParam<OAIPostProxy_request> &oai_post_proxy_request) {
    QString fullPath = QString(_serverConfigs["patchProxy"][_serverIndices.value("patchProxy")].URL()+"/proxy");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PATCH");

    if (oai_post_proxy_request.hasValue()){

        
        QByteArray output = oai_post_proxy_request.value().asJson().toUtf8();
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
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_service_id).isEmpty()) {
            input.headers.insert("x-apideck-service-id", ::OpenAPI::toStringValue(x_apideck_service_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_url).isEmpty()) {
            input.headers.insert("x-apideck-downstream-url", ::OpenAPI::toStringValue(x_apideck_downstream_url));
        }
        }
    if (x_apideck_downstream_authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()).isEmpty()) {
            input.headers.insert("x-apideck-downstream-authorization", ::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIExecuteApi::patchProxyCallback);
    connect(this, &OAIExecuteApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIExecuteApi::patchProxyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT patchProxySignal(output);
        Q_EMIT patchProxySignalFull(worker, output);
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

        Q_EMIT patchProxySignalE(output, error_type, error_str);
        Q_EMIT patchProxySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT patchProxySignalError(output, error_type, error_str);
        Q_EMIT patchProxySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIExecuteApi::postProxy(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &x_apideck_service_id, const QString &x_apideck_downstream_url, const ::OpenAPI::OptionalParam<QString> &x_apideck_downstream_authorization, const ::OpenAPI::OptionalParam<OAIPostProxy_request> &oai_post_proxy_request) {
    QString fullPath = QString(_serverConfigs["postProxy"][_serverIndices.value("postProxy")].URL()+"/proxy");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_post_proxy_request.hasValue()){

        
        QByteArray output = oai_post_proxy_request.value().asJson().toUtf8();
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
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_service_id).isEmpty()) {
            input.headers.insert("x-apideck-service-id", ::OpenAPI::toStringValue(x_apideck_service_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_url).isEmpty()) {
            input.headers.insert("x-apideck-downstream-url", ::OpenAPI::toStringValue(x_apideck_downstream_url));
        }
        }
    if (x_apideck_downstream_authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()).isEmpty()) {
            input.headers.insert("x-apideck-downstream-authorization", ::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIExecuteApi::postProxyCallback);
    connect(this, &OAIExecuteApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIExecuteApi::postProxyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT postProxySignal(output);
        Q_EMIT postProxySignalFull(worker, output);
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

        Q_EMIT postProxySignalE(output, error_type, error_str);
        Q_EMIT postProxySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT postProxySignalError(output, error_type, error_str);
        Q_EMIT postProxySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIExecuteApi::putProxy(const QString &x_apideck_consumer_id, const QString &x_apideck_app_id, const QString &x_apideck_service_id, const QString &x_apideck_downstream_url, const ::OpenAPI::OptionalParam<QString> &x_apideck_downstream_authorization, const ::OpenAPI::OptionalParam<OAIPutProxy_request> &oai_put_proxy_request) {
    QString fullPath = QString(_serverConfigs["putProxy"][_serverIndices.value("putProxy")].URL()+"/proxy");
    
    if (_apiKeys.contains("apiKey")) {
        addHeaders("apiKey",_apiKeys.find("apiKey").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_put_proxy_request.hasValue()){

        
        QByteArray output = oai_put_proxy_request.value().asJson().toUtf8();
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
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_service_id).isEmpty()) {
            input.headers.insert("x-apideck-service-id", ::OpenAPI::toStringValue(x_apideck_service_id));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_url).isEmpty()) {
            input.headers.insert("x-apideck-downstream-url", ::OpenAPI::toStringValue(x_apideck_downstream_url));
        }
        }
    if (x_apideck_downstream_authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()).isEmpty()) {
            input.headers.insert("x-apideck-downstream-authorization", ::OpenAPI::toStringValue(x_apideck_downstream_authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIExecuteApi::putProxyCallback);
    connect(this, &OAIExecuteApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIExecuteApi::putProxyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putProxySignal(output);
        Q_EMIT putProxySignalFull(worker, output);
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

        Q_EMIT putProxySignalE(output, error_type, error_str);
        Q_EMIT putProxySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putProxySignalError(output, error_type, error_str);
        Q_EMIT putProxySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIExecuteApi::tokenAvailable(){

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
