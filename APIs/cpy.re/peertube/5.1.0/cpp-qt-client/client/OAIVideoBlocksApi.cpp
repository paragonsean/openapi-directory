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

#include "OAIVideoBlocksApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIVideoBlocksApi::OAIVideoBlocksApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIVideoBlocksApi::~OAIVideoBlocksApi() {
}

void OAIVideoBlocksApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://peertube2.cpy.re"),
    "Live Test Server (live data - latest nightly version)",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://peertube3.cpy.re"),
    "Live Test Server (live data - latest RC version)",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://peertube.cpy.re"),
    "Live Test Server (live data - stable version)",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("addVideoBlock", defaultConf);
    _serverIndices.insert("addVideoBlock", 0);
    _serverConfigs.insert("delVideoBlock", defaultConf);
    _serverIndices.insert("delVideoBlock", 0);
    _serverConfigs.insert("getVideoBlocks", defaultConf);
    _serverIndices.insert("getVideoBlocks", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIVideoBlocksApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIVideoBlocksApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIVideoBlocksApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIVideoBlocksApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIVideoBlocksApi::setUsername(const QString &username) {
    _username = username;
}

void OAIVideoBlocksApi::setPassword(const QString &password) {
    _password = password;
}


void OAIVideoBlocksApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIVideoBlocksApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIVideoBlocksApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIVideoBlocksApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIVideoBlocksApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIVideoBlocksApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIVideoBlocksApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIVideoBlocksApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIVideoBlocksApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIVideoBlocksApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIVideoBlocksApi::getParamStylePrefix(const QString &style) {
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

QString OAIVideoBlocksApi::getParamStyleSuffix(const QString &style) {
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

QString OAIVideoBlocksApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIVideoBlocksApi::addVideoBlock(const OAIGetLiveId_id_parameter &id) {
    QString fullPath = QString(_serverConfigs["addVideoBlock"][_serverIndices.value("addVideoBlock")].URL()+"/api/v1/videos/{id}/blacklist");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"id"+pathSuffix;
        QJsonObject parameter = id.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(idPathParam, QUrl::toPercentEncoding(paramString));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoBlocksApi::addVideoBlockCallback);
    connect(this, &OAIVideoBlocksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    scope.append("admin");
    scope.append("moderator");
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoBlocksApi::addVideoBlockCallback);
    connect(this, &OAIVideoBlocksApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoBlocksApi::addVideoBlockCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addVideoBlockSignal();
        Q_EMIT addVideoBlockSignalFull(worker);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("admin");
        scope.append("moderator");
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT addVideoBlockSignalE(error_type, error_str);
        Q_EMIT addVideoBlockSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addVideoBlockSignalError(error_type, error_str);
        Q_EMIT addVideoBlockSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoBlocksApi::delVideoBlock(const OAIGetLiveId_id_parameter &id) {
    QString fullPath = QString(_serverConfigs["delVideoBlock"][_serverIndices.value("delVideoBlock")].URL()+"/api/v1/videos/{id}/blacklist");
    
    
    {
        QString idPathParam("{");
        idPathParam.append("id").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "id", false);
        QString paramString = (pathStyle == "matrix" && false) ? pathPrefix : pathPrefix+"id"+pathSuffix;
        QJsonObject parameter = id.asJsonObject();
        qint32 count = 0;
        for(const QString& key : parameter.keys()) {
            if (count > 0) {
                pathDelimiter = (pathStyle == "matrix" && false) ? ";" : getParamStyleDelimiter(pathStyle, key, false);
                paramString.append(pathDelimiter);
            }
            QString assignOperator = (false) ? "=" : ",";
            switch(parameter.value(key).type()) {
                case QJsonValue::String:
                {
                    paramString.append(key+assignOperator+parameter.value(key).toString());
                    break;
                }
                case QJsonValue::Double:
                {
                    paramString.append(key+assignOperator+QString::number(parameter.value(key).toDouble()));
                    break;
                }
                case QJsonValue::Bool:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toBool()).toString());
                    break;
                }
                case QJsonValue::Array:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toArray()).toString());
                    break;
                }
                case QJsonValue::Object:
                {
                    paramString.append(key+assignOperator+QVariant(parameter.value(key).toObject()).toString());
                    break;
                }
                case QJsonValue::Null:
                case QJsonValue::Undefined:
                    break;
            }
            count++;
        }
        fullPath.replace(idPathParam, QUrl::toPercentEncoding(paramString));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoBlocksApi::delVideoBlockCallback);
    connect(this, &OAIVideoBlocksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    scope.append("admin");
    scope.append("moderator");
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoBlocksApi::delVideoBlockCallback);
    connect(this, &OAIVideoBlocksApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoBlocksApi::delVideoBlockCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT delVideoBlockSignal();
        Q_EMIT delVideoBlockSignalFull(worker);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("admin");
        scope.append("moderator");
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT delVideoBlockSignalE(error_type, error_str);
        Q_EMIT delVideoBlockSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT delVideoBlockSignalError(error_type, error_str);
        Q_EMIT delVideoBlockSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoBlocksApi::getVideoBlocks(const ::OpenAPI::OptionalParam<qint32> &type, const ::OpenAPI::OptionalParam<QString> &search, const ::OpenAPI::OptionalParam<qint32> &start, const ::OpenAPI::OptionalParam<qint32> &count, const ::OpenAPI::OptionalParam<QString> &sort) {
    QString fullPath = QString(_serverConfigs["getVideoBlocks"][_serverIndices.value("getVideoBlocks")].URL()+"/api/v1/videos/blacklist");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (type.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "type", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("type")).append(querySuffix).append(QUrl::toPercentEncoding(type.stringValue()));
    }
    if (search.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "search", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("search")).append(querySuffix).append(QUrl::toPercentEncoding(search.stringValue()));
    }
    if (start.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "start", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("start")).append(querySuffix).append(QUrl::toPercentEncoding(start.stringValue()));
    }
    if (count.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "count", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("count")).append(querySuffix).append(QUrl::toPercentEncoding(count.stringValue()));
    }
    if (sort.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sort", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sort")).append(querySuffix).append(QUrl::toPercentEncoding(sort.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoBlocksApi::getVideoBlocksCallback);
    connect(this, &OAIVideoBlocksApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });


    _OauthMethod = 4;
    _passwordFlow.link();
    _authFlow.unlink();
    _implicitFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    scope.append("admin");
    scope.append("moderator");
    auto token = _passwordFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIVideoBlocksApi::getVideoBlocksCallback);
    connect(this, &OAIVideoBlocksApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;
    

    worker->execute(&input);
}

void OAIVideoBlocksApi::getVideoBlocksCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetVideoBlocks_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getVideoBlocksSignal(output);
        Q_EMIT getVideoBlocksSignalFull(worker, output);


    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_passwordFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("admin");
        scope.append("moderator");
        QString scopeStr = scope.join(" ");
        QString tokenUrl("/api/v1/users/token");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _passwordFlow.setVariables(tokenUrl , scopeStr ,"clientId", "clientSecret", "username", "password");
        Q_EMIT _passwordFlow.authenticationNeeded();
        
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

        Q_EMIT getVideoBlocksSignalE(output, error_type, error_str);
        Q_EMIT getVideoBlocksSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getVideoBlocksSignalError(output, error_type, error_str);
        Q_EMIT getVideoBlocksSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIVideoBlocksApi::tokenAvailable(){

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
