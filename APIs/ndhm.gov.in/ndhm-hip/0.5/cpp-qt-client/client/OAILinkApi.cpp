/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILinkApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAILinkApi::OAILinkApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAILinkApi::~OAILinkApi() {
}

void OAILinkApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://dev.ndhm.gov.in/gateway"),
    "Sandbox",
    QMap<QString, OAIServerVariable>()));
    serverConf.append(OAIServerConfiguration(
    QUrl("https://your-hrp-server.com"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("v05LinksLinkConfirmPost", serverConf);
    _serverIndices.insert("v05LinksLinkConfirmPost", 0);
    serverConf.append(OAIServerConfiguration(
    QUrl("https://your-hrp-server.com"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("v05LinksLinkInitPost", serverConf);
    _serverIndices.insert("v05LinksLinkInitPost", 0);
    serverConf.append(OAIServerConfiguration(
    QUrl("https://your-hrp-server.com"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("v05LinksLinkOnAddContextsPost", serverConf);
    _serverIndices.insert("v05LinksLinkOnAddContextsPost", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAILinkApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAILinkApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAILinkApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAILinkApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAILinkApi::setUsername(const QString &username) {
    _username = username;
}

void OAILinkApi::setPassword(const QString &password) {
    _password = password;
}


void OAILinkApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAILinkApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAILinkApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAILinkApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAILinkApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAILinkApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAILinkApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAILinkApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAILinkApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAILinkApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAILinkApi::getParamStylePrefix(const QString &style) {
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

QString OAILinkApi::getParamStyleSuffix(const QString &style) {
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

QString OAILinkApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAILinkApi::v05LinksLinkConfirmPost(const QString &authorization, const QString &x_hip_id, const OAILinkConfirmationRequest &oai_link_confirmation_request) {
    QString fullPath = QString(_serverConfigs["v05LinksLinkConfirmPost"][_serverIndices.value("v05LinksLinkConfirmPost")].URL()+"/v0.5/links/link/confirm");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_link_confirmation_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(authorization).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_hip_id).isEmpty()) {
            input.headers.insert("X-HIP-ID", ::OpenAPI::toStringValue(x_hip_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILinkApi::v05LinksLinkConfirmPostCallback);
    connect(this, &OAILinkApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILinkApi::v05LinksLinkConfirmPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v05LinksLinkConfirmPostSignal();
        Q_EMIT v05LinksLinkConfirmPostSignalFull(worker);
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

        Q_EMIT v05LinksLinkConfirmPostSignalE(error_type, error_str);
        Q_EMIT v05LinksLinkConfirmPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v05LinksLinkConfirmPostSignalError(error_type, error_str);
        Q_EMIT v05LinksLinkConfirmPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILinkApi::v05LinksLinkInitPost(const QString &authorization, const QString &x_hip_id, const OAIPatientLinkReferenceRequest &oai_patient_link_reference_request) {
    QString fullPath = QString(_serverConfigs["v05LinksLinkInitPost"][_serverIndices.value("v05LinksLinkInitPost")].URL()+"/v0.5/links/link/init");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_patient_link_reference_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(authorization).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_hip_id).isEmpty()) {
            input.headers.insert("X-HIP-ID", ::OpenAPI::toStringValue(x_hip_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILinkApi::v05LinksLinkInitPostCallback);
    connect(this, &OAILinkApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILinkApi::v05LinksLinkInitPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v05LinksLinkInitPostSignal();
        Q_EMIT v05LinksLinkInitPostSignalFull(worker);
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

        Q_EMIT v05LinksLinkInitPostSignalE(error_type, error_str);
        Q_EMIT v05LinksLinkInitPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v05LinksLinkInitPostSignalError(error_type, error_str);
        Q_EMIT v05LinksLinkInitPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILinkApi::v05LinksLinkOnAddContextsPost(const QString &authorization, const QString &x_hip_id, const OAIPatientCareContextLinkResponse &oai_patient_care_context_link_response) {
    QString fullPath = QString(_serverConfigs["v05LinksLinkOnAddContextsPost"][_serverIndices.value("v05LinksLinkOnAddContextsPost")].URL()+"/v0.5/links/link/on-add-contexts");
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_patient_care_context_link_response.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(authorization).isEmpty()) {
            input.headers.insert("Authorization", ::OpenAPI::toStringValue(authorization));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(x_hip_id).isEmpty()) {
            input.headers.insert("X-HIP-ID", ::OpenAPI::toStringValue(x_hip_id));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILinkApi::v05LinksLinkOnAddContextsPostCallback);
    connect(this, &OAILinkApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILinkApi::v05LinksLinkOnAddContextsPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT v05LinksLinkOnAddContextsPostSignal();
        Q_EMIT v05LinksLinkOnAddContextsPostSignalFull(worker);
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

        Q_EMIT v05LinksLinkOnAddContextsPostSignalE(error_type, error_str);
        Q_EMIT v05LinksLinkOnAddContextsPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT v05LinksLinkOnAddContextsPostSignalError(error_type, error_str);
        Q_EMIT v05LinksLinkOnAddContextsPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILinkApi::tokenAvailable(){

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
