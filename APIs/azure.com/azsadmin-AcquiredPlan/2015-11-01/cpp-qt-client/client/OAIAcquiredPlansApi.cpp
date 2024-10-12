/**
 * SubscriptionsManagementClient
 * The Admin Subscriptions Management Client.
 *
 * The version of the OpenAPI document: 2015-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAcquiredPlansApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIAcquiredPlansApi::OAIAcquiredPlansApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIAcquiredPlansApi::~OAIAcquiredPlansApi() {
}

void OAIAcquiredPlansApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://adminmanagement.local.azurestack.external/"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("acquiredPlansCreate", defaultConf);
    _serverIndices.insert("acquiredPlansCreate", 0);
    _serverConfigs.insert("acquiredPlansDelete", defaultConf);
    _serverIndices.insert("acquiredPlansDelete", 0);
    _serverConfigs.insert("acquiredPlansGet", defaultConf);
    _serverIndices.insert("acquiredPlansGet", 0);
    _serverConfigs.insert("acquiredPlansList", defaultConf);
    _serverIndices.insert("acquiredPlansList", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIAcquiredPlansApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIAcquiredPlansApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIAcquiredPlansApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIAcquiredPlansApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIAcquiredPlansApi::setUsername(const QString &username) {
    _username = username;
}

void OAIAcquiredPlansApi::setPassword(const QString &password) {
    _password = password;
}


void OAIAcquiredPlansApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIAcquiredPlansApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIAcquiredPlansApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIAcquiredPlansApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIAcquiredPlansApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIAcquiredPlansApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIAcquiredPlansApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIAcquiredPlansApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIAcquiredPlansApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIAcquiredPlansApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIAcquiredPlansApi::getParamStylePrefix(const QString &style) {
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

QString OAIAcquiredPlansApi::getParamStyleSuffix(const QString &style) {
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

QString OAIAcquiredPlansApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIAcquiredPlansApi::acquiredPlansCreate(const QString &subscription_id, const QString &target_subscription_id, const QString &plan_acquisition_id, const QString &api_version, const OAIPlanAcquisition &new_acquired_plan) {
    QString fullPath = QString(_serverConfigs["acquiredPlansCreate"][_serverIndices.value("acquiredPlansCreate")].URL()+"/subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId}");
    
    
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
        QString target_subscription_idPathParam("{");
        target_subscription_idPathParam.append("targetSubscriptionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "targetSubscriptionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"targetSubscriptionId"+pathSuffix : pathPrefix;
        fullPath.replace(target_subscription_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(target_subscription_id)));
    }
    
    {
        QString plan_acquisition_idPathParam("{");
        plan_acquisition_idPathParam.append("planAcquisitionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "planAcquisitionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"planAcquisitionId"+pathSuffix : pathPrefix;
        fullPath.replace(plan_acquisition_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(plan_acquisition_id)));
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
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = new_acquired_plan.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansCreateCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, worker, &QObject::deleteLater);
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

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansCreateCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;



    worker->execute(&input);
}

void OAIAcquiredPlansApi::acquiredPlansCreateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPlanAcquisition output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT acquiredPlansCreateSignal(output);
        Q_EMIT acquiredPlansCreateSignalFull(worker, output);
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

        Q_EMIT acquiredPlansCreateSignalE(output, error_type, error_str);
        Q_EMIT acquiredPlansCreateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT acquiredPlansCreateSignalError(output, error_type, error_str);
        Q_EMIT acquiredPlansCreateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAcquiredPlansApi::acquiredPlansDelete(const QString &subscription_id, const QString &target_subscription_id, const QString &plan_acquisition_id, const QString &api_version) {
    QString fullPath = QString(_serverConfigs["acquiredPlansDelete"][_serverIndices.value("acquiredPlansDelete")].URL()+"/subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId}");
    
    
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
        QString target_subscription_idPathParam("{");
        target_subscription_idPathParam.append("targetSubscriptionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "targetSubscriptionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"targetSubscriptionId"+pathSuffix : pathPrefix;
        fullPath.replace(target_subscription_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(target_subscription_id)));
    }
    
    {
        QString plan_acquisition_idPathParam("{");
        plan_acquisition_idPathParam.append("planAcquisitionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "planAcquisitionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"planAcquisitionId"+pathSuffix : pathPrefix;
        fullPath.replace(plan_acquisition_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(plan_acquisition_id)));
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
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansDeleteCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, worker, &QObject::deleteLater);
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

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansDeleteCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;



    worker->execute(&input);
}

void OAIAcquiredPlansApi::acquiredPlansDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT acquiredPlansDeleteSignal();
        Q_EMIT acquiredPlansDeleteSignalFull(worker);
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

        Q_EMIT acquiredPlansDeleteSignalE(error_type, error_str);
        Q_EMIT acquiredPlansDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT acquiredPlansDeleteSignalError(error_type, error_str);
        Q_EMIT acquiredPlansDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAcquiredPlansApi::acquiredPlansGet(const QString &subscription_id, const QString &target_subscription_id, const QString &plan_acquisition_id, const QString &api_version) {
    QString fullPath = QString(_serverConfigs["acquiredPlansGet"][_serverIndices.value("acquiredPlansGet")].URL()+"/subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans/{planAcquisitionId}");
    
    
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
        QString target_subscription_idPathParam("{");
        target_subscription_idPathParam.append("targetSubscriptionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "targetSubscriptionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"targetSubscriptionId"+pathSuffix : pathPrefix;
        fullPath.replace(target_subscription_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(target_subscription_id)));
    }
    
    {
        QString plan_acquisition_idPathParam("{");
        plan_acquisition_idPathParam.append("planAcquisitionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "planAcquisitionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"planAcquisitionId"+pathSuffix : pathPrefix;
        fullPath.replace(plan_acquisition_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(plan_acquisition_id)));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansGetCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, worker, &QObject::deleteLater);
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

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansGetCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;



    worker->execute(&input);
}

void OAIAcquiredPlansApi::acquiredPlansGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPlanAcquisition output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT acquiredPlansGetSignal(output);
        Q_EMIT acquiredPlansGetSignalFull(worker, output);
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

        Q_EMIT acquiredPlansGetSignalE(output, error_type, error_str);
        Q_EMIT acquiredPlansGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT acquiredPlansGetSignalError(output, error_type, error_str);
        Q_EMIT acquiredPlansGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAcquiredPlansApi::acquiredPlansList(const QString &subscription_id, const QString &target_subscription_id, const QString &api_version) {
    QString fullPath = QString(_serverConfigs["acquiredPlansList"][_serverIndices.value("acquiredPlansList")].URL()+"/subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/subscriptions/{targetSubscriptionId}/acquiredPlans");
    
    
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
        QString target_subscription_idPathParam("{");
        target_subscription_idPathParam.append("targetSubscriptionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "targetSubscriptionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"targetSubscriptionId"+pathSuffix : pathPrefix;
        fullPath.replace(target_subscription_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(target_subscription_id)));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansListCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, worker, &QObject::deleteLater);
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

    connect(_latestWorker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAcquiredPlansApi::acquiredPlansListCallback);
    connect(this, &OAIAcquiredPlansApi::abortRequestsSignal, _latestWorker, &QObject::deleteLater);
    connect(_latestWorker, &QObject::destroyed, [this](){
        if(findChildren<OAIHttpRequestWorker*>().count() == 0){
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    _latestInput = input;
    _latestScope = scope;



    worker->execute(&input);
}

void OAIAcquiredPlansApi::acquiredPlansListCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIPlanAcquisitionList output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT acquiredPlansListSignal(output);
        Q_EMIT acquiredPlansListSignalFull(worker, output);
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

        Q_EMIT acquiredPlansListSignalE(output, error_type, error_str);
        Q_EMIT acquiredPlansListSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT acquiredPlansListSignalError(output, error_type, error_str);
        Q_EMIT acquiredPlansListSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAcquiredPlansApi::tokenAvailable(){

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
