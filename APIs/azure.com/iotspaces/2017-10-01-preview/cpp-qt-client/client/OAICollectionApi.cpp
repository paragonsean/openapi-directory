/**
 * IoTSpacesClient
 * Use this API to manage the IoTSpaces service instances in your Azure subscription.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICollectionApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAICollectionApi::OAICollectionApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAICollectionApi::~OAICollectionApi() {
}

void OAICollectionApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://management.azure.com/"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("ioTSpacesList", defaultConf);
    _serverIndices.insert("ioTSpacesList", 0);
    _serverConfigs.insert("ioTSpacesListByResourceGroup", defaultConf);
    _serverIndices.insert("ioTSpacesListByResourceGroup", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAICollectionApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAICollectionApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAICollectionApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAICollectionApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAICollectionApi::setUsername(const QString &username) {
    _username = username;
}

void OAICollectionApi::setPassword(const QString &password) {
    _password = password;
}


void OAICollectionApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAICollectionApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAICollectionApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAICollectionApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAICollectionApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAICollectionApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAICollectionApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAICollectionApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAICollectionApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAICollectionApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAICollectionApi::getParamStylePrefix(const QString &style) {
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

QString OAICollectionApi::getParamStyleSuffix(const QString &style) {
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

QString OAICollectionApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAICollectionApi::ioTSpacesList(const QString &api_version, const QString &subscription_id) {
    QString fullPath = QString(_serverConfigs["ioTSpacesList"][_serverIndices.value("ioTSpacesList")].URL()+"/subscriptions/{subscriptionId}/providers/Microsoft.IoTSpaces/Graph");
    
    
    {
        QString subscription_idPathParam("{");
        subscription_idPathParam.append("subscriptionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subscriptionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subscriptionId"+pathSuffix : pathPrefix;
        fullPath.replace(subscription_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(subscription_id)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "api-version", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("api-version")).append(querySuffix).append(QUrl::toPercentEncoding(api_version));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICollectionApi::ioTSpacesListCallback);
    connect(this, &OAICollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 1;
    _implicitFlow.link();
    _passwordFlow.unlink();
    _authFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    scope.append("user_impersonation");
    auto token = _implicitFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICollectionApi::ioTSpacesListCallback);
    connect(this, &OAICollectionApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;



    worker->execute(&input);
}

void OAICollectionApi::ioTSpacesListCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIIoTSpacesDescriptionListResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT ioTSpacesListSignal(output);
        Q_EMIT ioTSpacesListSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_implicitFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("user_impersonation");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.microsoftonline.com/common/oauth2/authorize");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _implicitFlow.setVariables(authorizationUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId");
        Q_EMIT _implicitFlow.authenticationNeeded();


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

        Q_EMIT ioTSpacesListSignalE(output, error_type, error_str);
        Q_EMIT ioTSpacesListSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT ioTSpacesListSignalError(output, error_type, error_str);
        Q_EMIT ioTSpacesListSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICollectionApi::ioTSpacesListByResourceGroup(const QString &api_version, const QString &subscription_id, const QString &resource_group_name) {
    QString fullPath = QString(_serverConfigs["ioTSpacesListByResourceGroup"][_serverIndices.value("ioTSpacesListByResourceGroup")].URL()+"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTSpaces/Graph");
    
    
    {
        QString subscription_idPathParam("{");
        subscription_idPathParam.append("subscriptionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subscriptionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subscriptionId"+pathSuffix : pathPrefix;
        fullPath.replace(subscription_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(subscription_id)));
    }
    
    {
        QString resource_group_namePathParam("{");
        resource_group_namePathParam.append("resourceGroupName").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "resourceGroupName", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"resourceGroupName"+pathSuffix : pathPrefix;
        fullPath.replace(resource_group_namePathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(resource_group_name)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "api-version", false);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("api-version")).append(querySuffix).append(QUrl::toPercentEncoding(api_version));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICollectionApi::ioTSpacesListByResourceGroupCallback);
    connect(this, &OAICollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });
    _OauthMethod = 1;
    _implicitFlow.link();
    _passwordFlow.unlink();
    _authFlow.unlink();
    _credentialFlow.unlink();
    QStringList scope;
    scope.append("user_impersonation");
    auto token = _implicitFlow.getToken(scope.join(" "));
    if(token.isValid())
        input.headers.insert("Authorization", "Bearer " + token.getToken());

    _latestWorker = new OAIHttpRequestWorker(this, _manager);
    _latestWorker->setTimeOut(_timeOut);
    _latestWorker->setWorkingDirectory(_workingDirectory);

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICollectionApi::ioTSpacesListByResourceGroupCallback);
    connect(this, &OAICollectionApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;



    worker->execute(&input);
}

void OAICollectionApi::ioTSpacesListByResourceGroupCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIIoTSpacesDescriptionListResult output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT ioTSpacesListByResourceGroupSignal(output);
        Q_EMIT ioTSpacesListByResourceGroupSignalFull(worker, output);
    } else if(worker->error_type == QNetworkReply::AuthenticationRequiredError){
        connect(&_implicitFlow, SIGNAL(tokenReceived()), this, SLOT(tokenAvailable()));
        QStringList scope;
        scope.append("user_impersonation");
        QString scopeStr = scope.join(" ");
        QString authorizationUrl("https://login.microsoftonline.com/common/oauth2/authorize");
        //TODO get clientID and Secret and state in the config? https://swagger.io/docs/specification/authentication/oauth2/ states that you should do as you like
        _implicitFlow.setVariables(authorizationUrl, scopeStr, "state" , "http://127.0.0.1:9999", "clientId");
        Q_EMIT _implicitFlow.authenticationNeeded();


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

        Q_EMIT ioTSpacesListByResourceGroupSignalE(output, error_type, error_str);
        Q_EMIT ioTSpacesListByResourceGroupSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT ioTSpacesListByResourceGroupSignalError(output, error_type, error_str);
        Q_EMIT ioTSpacesListByResourceGroupSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICollectionApi::tokenAvailable(){

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
