/**
 * Enode API
 * Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)  Download [Postman Collection](/Postman-Enode-v1.4.0.json)  The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.  The API has a RESTful architecture and utilizes OAuth2 authorization.  We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io   ## Registration for API access In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.  # Authorization Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.  > The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.  ### Preparation: Configure your OAuth client  Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)  To configure your chosen OAuth client, you will need these details: - Your `client_id` - Your `client_secret` - Authorization URL: `https://link.test.enode.io/oauth2/auth` - Token URL: `https://link.test.enode.io/oauth2/token`  ```javascript // Node.js + openid-client example const enodeIssuer = await Issuer.discover('https://link.test.enode.io'); const client = new enodeIssuer.Client({   client_id: 'xyz',   client_secret: 'shhhhh',   redirect_uris: ['http://localhost:5000/callback'],   response_types: ['code'], }); ```   ### Preparation: Obtain a client access token via OAuth Client Credentials Grant Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.  ```javascript // Node.js + openid-client example const clientAccessToken = await client.grant({grant_type: \"client_credentials\"}); ```  This access token belongs to your client and is used for administrative actions, such as the next step.  This token should be cached by your server and reused until it expires, at which point your server should request a new one.    ### Step 1. Generate an Enode Link session for your User and launch the OAuth flow  When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.  Example Request: ``` POST /users/{userId}/link HTTP/1.1 Authorization: Bearer {access_token} {   \"forceLanguage\": \"nb-NO\",   \"vendor\": \"Tesla\", } ```  Example Response: ``` {     \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\", } ```  The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.  Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details: - Redirect URI - The URI to which your user should be redirected when the Oauth flow completes - Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer)) - State - The value of `linkState` from the request above  To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.  ```javascript // Node.js + openid-client + express example  // Construct an OAuth authorization URL const authorizationUrl = client.authorizationUrl({   scope: \"offline_access all\",   state: linkState });  // Redirect user to authorization URL res.redirect(authorizationUrl); ```   ### Step 2. User grants consent In the Link UI webapp the user will follow 3 steps:  1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box. 2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in. 3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.   ### Step 3. OAuth flow concludes with a callback When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.  Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.  Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).  ```javascript // Node.js + openid-client + express example  // Fetch linkState from user session const linkState = get(req, 'session.linkState');  // Parse relevant parameters from request URL const params = client.callbackParams(req);  // Exchange authorization code for access and refresh tokens // In this example, openid-client does the linkState validation check for us const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState}) ```  With the access token in hand, you can now access resources on behalf of the user.   # Errors And Problems ## OAuth Authorization Request  When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:  |error                      |error_description| |---------------------------|-----------------| |invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.| |unauthorized_client        |The client is not authorized to request an authorization code using this method.| |access_denied              |The resource owner or authorization server denied the request.| |unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.| |invalid_scope              |The requested scope is invalid, unknown, or malformed.| |server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.| |temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|  Example: ``` https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request. ```   ## Errors when accessing a User's resources  When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:  |HTTP Status Code           |Explanation      | |---------------------------|-----------------| |400 Bad Request            |The request payload has failed schema validation / parsing |401 Unauthorized           |Authentication details are missing or invalid |403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource |404 Not Found              |A non-existent resource is requested |429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request   In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.  Example: ``` HTTP/1.1 400 Bad Request Content-Type: application/problem+json {   \"type\": \"https://docs.enode.io/problems/payload-validation-error\",   \"title\": \"Payload validation failed\",   \"detail\": \"\\\"authorizationRequest.scope\\\" is required\", } ```  
 *
 * The version of the OpenAPI document: 1.3.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStatisticsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIStatisticsApi::OAIStatisticsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIStatisticsApi::~OAIStatisticsApi() {
}

void OAIStatisticsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.test.enode.io/"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("getStatisticsCharging", defaultConf);
    _serverIndices.insert("getStatisticsCharging", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIStatisticsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIStatisticsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIStatisticsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIStatisticsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIStatisticsApi::setUsername(const QString &username) {
    _username = username;
}

void OAIStatisticsApi::setPassword(const QString &password) {
    _password = password;
}


void OAIStatisticsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIStatisticsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIStatisticsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIStatisticsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIStatisticsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIStatisticsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIStatisticsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIStatisticsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIStatisticsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIStatisticsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIStatisticsApi::getParamStylePrefix(const QString &style) {
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

QString OAIStatisticsApi::getParamStyleSuffix(const QString &style) {
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

QString OAIStatisticsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIStatisticsApi::getStatisticsCharging(const QDate &start_date, const ::OpenAPI::OptionalParam<QString> &resolution, const ::OpenAPI::OptionalParam<QDate> &end_date, const ::OpenAPI::OptionalParam<QString> &vehicle_id, const ::OpenAPI::OptionalParam<QString> &charging_location_id) {
    QString fullPath = QString(_serverConfigs["getStatisticsCharging"][_serverIndices.value("getStatisticsCharging")].URL()+"/statistics/charging");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (resolution.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "resolution", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("resolution")).append(querySuffix).append(QUrl::toPercentEncoding(resolution.stringValue()));
    }
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "startDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("startDate")).append(querySuffix).append(QUrl::toPercentEncoding(start_date));
    }
    if (end_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "endDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("endDate")).append(querySuffix).append(QUrl::toPercentEncoding(end_date.stringValue()));
    }
    if (vehicle_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "vehicleId", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("vehicleId")).append(querySuffix).append(QUrl::toPercentEncoding(vehicle_id.stringValue()));
    }
    if (charging_location_id.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "chargingLocationId", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("chargingLocationId")).append(querySuffix).append(QUrl::toPercentEncoding(charging_location_id.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIStatisticsApi::getStatisticsChargingCallback);
    connect(this, &OAIStatisticsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 2;
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    _passwordFlow.unlink();
    _authFlow.link();
    QStringList scope;
    auto token = _authFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIStatisticsApi::getStatisticsChargingCallback);
    connect(this, &OAIStatisticsApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;




    worker->execute(&input);
}

void OAIStatisticsApi::getStatisticsChargingCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIGetStatisticsCharging_200_response_inner> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIGetStatisticsCharging_200_response_inner val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getStatisticsChargingSignal(output);
        Q_EMIT getStatisticsChargingSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_authFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://link.test.enode.io/oauth2/auth");
        QString tokenUrl("https://link.test.enode.io/oauth2/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _authFlow.setVariables(authorizationUrl, tokenUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId", "clientSecret");
        Q_EMIT _authFlow.authenticationNeeded();



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

        Q_EMIT getStatisticsChargingSignalE(output, error_type, error_str);
        Q_EMIT getStatisticsChargingSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getStatisticsChargingSignalError(output, error_type, error_str);
        Q_EMIT getStatisticsChargingSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIStatisticsApi::tokenAvailable(){

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
