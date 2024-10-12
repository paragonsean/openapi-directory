/**
 * httpbin.org
 * A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>
 *
 * The version of the OpenAPI document: 0.9.2
 * Contact: me@kennethreitz.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIAuthApi::OAIAuthApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIAuthApi::~OAIAuthApi() {
}

void OAIAuthApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://httpbin.org"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("basicAuthUserPasswdGet", defaultConf);
    _serverIndices.insert("basicAuthUserPasswdGet", 0);
    _serverConfigs.insert("bearerGet", defaultConf);
    _serverIndices.insert("bearerGet", 0);
    _serverConfigs.insert("digestAuthQopUserPasswdAlgorithmGet", defaultConf);
    _serverIndices.insert("digestAuthQopUserPasswdAlgorithmGet", 0);
    _serverConfigs.insert("digestAuthQopUserPasswdAlgorithmStaleAfterGet", defaultConf);
    _serverIndices.insert("digestAuthQopUserPasswdAlgorithmStaleAfterGet", 0);
    _serverConfigs.insert("digestAuthQopUserPasswdGet", defaultConf);
    _serverIndices.insert("digestAuthQopUserPasswdGet", 0);
    _serverConfigs.insert("hiddenBasicAuthUserPasswdGet", defaultConf);
    _serverIndices.insert("hiddenBasicAuthUserPasswdGet", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIAuthApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIAuthApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIAuthApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIAuthApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIAuthApi::setUsername(const QString &username) {
    _username = username;
}

void OAIAuthApi::setPassword(const QString &password) {
    _password = password;
}


void OAIAuthApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIAuthApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIAuthApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIAuthApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIAuthApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIAuthApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIAuthApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIAuthApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIAuthApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIAuthApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIAuthApi::getParamStylePrefix(const QString &style) {
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

QString OAIAuthApi::getParamStyleSuffix(const QString &style) {
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

QString OAIAuthApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIAuthApi::basicAuthUserPasswdGet(const QString &user, const QString &passwd) {
    QString fullPath = QString(_serverConfigs["basicAuthUserPasswdGet"][_serverIndices.value("basicAuthUserPasswdGet")].URL()+"/basic-auth/{user}/{passwd}");
    
    
    {
        QString userPathParam("{");
        userPathParam.append("user").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user"+pathSuffix : pathPrefix;
        fullPath.replace(userPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user)));
    }
    
    {
        QString passwdPathParam("{");
        passwdPathParam.append("passwd").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "passwd", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"passwd"+pathSuffix : pathPrefix;
        fullPath.replace(passwdPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(passwd)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAuthApi::basicAuthUserPasswdGetCallback);
    connect(this, &OAIAuthApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAuthApi::basicAuthUserPasswdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT basicAuthUserPasswdGetSignal();
        Q_EMIT basicAuthUserPasswdGetSignalFull(worker);
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

        Q_EMIT basicAuthUserPasswdGetSignalE(error_type, error_str);
        Q_EMIT basicAuthUserPasswdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT basicAuthUserPasswdGetSignalError(error_type, error_str);
        Q_EMIT basicAuthUserPasswdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAuthApi::bearerGet(const ::OpenAPI::OptionalParam<QString> &authorization) {
    QString fullPath = QString(_serverConfigs["bearerGet"][_serverIndices.value("bearerGet")].URL()+"/bearer");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (authorization.hasValue())
    {
        if (!::OpenAPI::toStringValue(authorization.value()).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAuthApi::bearerGetCallback);
    connect(this, &OAIAuthApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAuthApi::bearerGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT bearerGetSignal();
        Q_EMIT bearerGetSignalFull(worker);
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

        Q_EMIT bearerGetSignalE(error_type, error_str);
        Q_EMIT bearerGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT bearerGetSignalError(error_type, error_str);
        Q_EMIT bearerGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAuthApi::digestAuthQopUserPasswdAlgorithmGet(const QString &qop, const QString &user, const QString &passwd, const QString &algorithm) {
    QString fullPath = QString(_serverConfigs["digestAuthQopUserPasswdAlgorithmGet"][_serverIndices.value("digestAuthQopUserPasswdAlgorithmGet")].URL()+"/digest-auth/{qop}/{user}/{passwd}/{algorithm}");
    
    
    {
        QString qopPathParam("{");
        qopPathParam.append("qop").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "qop", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"qop"+pathSuffix : pathPrefix;
        fullPath.replace(qopPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(qop)));
    }
    
    {
        QString userPathParam("{");
        userPathParam.append("user").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user"+pathSuffix : pathPrefix;
        fullPath.replace(userPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user)));
    }
    
    {
        QString passwdPathParam("{");
        passwdPathParam.append("passwd").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "passwd", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"passwd"+pathSuffix : pathPrefix;
        fullPath.replace(passwdPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(passwd)));
    }
    
    {
        QString algorithmPathParam("{");
        algorithmPathParam.append("algorithm").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "algorithm", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"algorithm"+pathSuffix : pathPrefix;
        fullPath.replace(algorithmPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(algorithm)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAuthApi::digestAuthQopUserPasswdAlgorithmGetCallback);
    connect(this, &OAIAuthApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAuthApi::digestAuthQopUserPasswdAlgorithmGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT digestAuthQopUserPasswdAlgorithmGetSignal();
        Q_EMIT digestAuthQopUserPasswdAlgorithmGetSignalFull(worker);
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

        Q_EMIT digestAuthQopUserPasswdAlgorithmGetSignalE(error_type, error_str);
        Q_EMIT digestAuthQopUserPasswdAlgorithmGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT digestAuthQopUserPasswdAlgorithmGetSignalError(error_type, error_str);
        Q_EMIT digestAuthQopUserPasswdAlgorithmGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAuthApi::digestAuthQopUserPasswdAlgorithmStaleAfterGet(const QString &qop, const QString &user, const QString &passwd, const QString &algorithm, const QString &stale_after) {
    QString fullPath = QString(_serverConfigs["digestAuthQopUserPasswdAlgorithmStaleAfterGet"][_serverIndices.value("digestAuthQopUserPasswdAlgorithmStaleAfterGet")].URL()+"/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}");
    
    
    {
        QString qopPathParam("{");
        qopPathParam.append("qop").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "qop", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"qop"+pathSuffix : pathPrefix;
        fullPath.replace(qopPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(qop)));
    }
    
    {
        QString userPathParam("{");
        userPathParam.append("user").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user"+pathSuffix : pathPrefix;
        fullPath.replace(userPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user)));
    }
    
    {
        QString passwdPathParam("{");
        passwdPathParam.append("passwd").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "passwd", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"passwd"+pathSuffix : pathPrefix;
        fullPath.replace(passwdPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(passwd)));
    }
    
    {
        QString algorithmPathParam("{");
        algorithmPathParam.append("algorithm").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "algorithm", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"algorithm"+pathSuffix : pathPrefix;
        fullPath.replace(algorithmPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(algorithm)));
    }
    
    {
        QString stale_afterPathParam("{");
        stale_afterPathParam.append("stale_after").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "stale_after", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"stale_after"+pathSuffix : pathPrefix;
        fullPath.replace(stale_afterPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(stale_after)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAuthApi::digestAuthQopUserPasswdAlgorithmStaleAfterGetCallback);
    connect(this, &OAIAuthApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAuthApi::digestAuthQopUserPasswdAlgorithmStaleAfterGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT digestAuthQopUserPasswdAlgorithmStaleAfterGetSignal();
        Q_EMIT digestAuthQopUserPasswdAlgorithmStaleAfterGetSignalFull(worker);
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

        Q_EMIT digestAuthQopUserPasswdAlgorithmStaleAfterGetSignalE(error_type, error_str);
        Q_EMIT digestAuthQopUserPasswdAlgorithmStaleAfterGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT digestAuthQopUserPasswdAlgorithmStaleAfterGetSignalError(error_type, error_str);
        Q_EMIT digestAuthQopUserPasswdAlgorithmStaleAfterGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAuthApi::digestAuthQopUserPasswdGet(const QString &qop, const QString &user, const QString &passwd) {
    QString fullPath = QString(_serverConfigs["digestAuthQopUserPasswdGet"][_serverIndices.value("digestAuthQopUserPasswdGet")].URL()+"/digest-auth/{qop}/{user}/{passwd}");
    
    
    {
        QString qopPathParam("{");
        qopPathParam.append("qop").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "qop", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"qop"+pathSuffix : pathPrefix;
        fullPath.replace(qopPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(qop)));
    }
    
    {
        QString userPathParam("{");
        userPathParam.append("user").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user"+pathSuffix : pathPrefix;
        fullPath.replace(userPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user)));
    }
    
    {
        QString passwdPathParam("{");
        passwdPathParam.append("passwd").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "passwd", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"passwd"+pathSuffix : pathPrefix;
        fullPath.replace(passwdPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(passwd)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAuthApi::digestAuthQopUserPasswdGetCallback);
    connect(this, &OAIAuthApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAuthApi::digestAuthQopUserPasswdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT digestAuthQopUserPasswdGetSignal();
        Q_EMIT digestAuthQopUserPasswdGetSignalFull(worker);
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

        Q_EMIT digestAuthQopUserPasswdGetSignalE(error_type, error_str);
        Q_EMIT digestAuthQopUserPasswdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT digestAuthQopUserPasswdGetSignalError(error_type, error_str);
        Q_EMIT digestAuthQopUserPasswdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAuthApi::hiddenBasicAuthUserPasswdGet(const QString &user, const QString &passwd) {
    QString fullPath = QString(_serverConfigs["hiddenBasicAuthUserPasswdGet"][_serverIndices.value("hiddenBasicAuthUserPasswdGet")].URL()+"/hidden-basic-auth/{user}/{passwd}");
    
    
    {
        QString userPathParam("{");
        userPathParam.append("user").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "user", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"user"+pathSuffix : pathPrefix;
        fullPath.replace(userPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(user)));
    }
    
    {
        QString passwdPathParam("{");
        passwdPathParam.append("passwd").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "passwd", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"passwd"+pathSuffix : pathPrefix;
        fullPath.replace(passwdPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(passwd)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAuthApi::hiddenBasicAuthUserPasswdGetCallback);
    connect(this, &OAIAuthApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAuthApi::hiddenBasicAuthUserPasswdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT hiddenBasicAuthUserPasswdGetSignal();
        Q_EMIT hiddenBasicAuthUserPasswdGetSignalFull(worker);
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

        Q_EMIT hiddenBasicAuthUserPasswdGetSignalE(error_type, error_str);
        Q_EMIT hiddenBasicAuthUserPasswdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT hiddenBasicAuthUserPasswdGetSignalError(error_type, error_str);
        Q_EMIT hiddenBasicAuthUserPasswdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAuthApi::tokenAvailable(){

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
