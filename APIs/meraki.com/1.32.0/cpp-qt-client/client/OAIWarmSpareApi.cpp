/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWarmSpareApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIWarmSpareApi::OAIWarmSpareApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIWarmSpareApi::~OAIWarmSpareApi() {
}

void OAIWarmSpareApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.meraki.com/api/v1"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("getDeviceSwitchWarmSpare", defaultConf);
    _serverIndices.insert("getDeviceSwitchWarmSpare", 0);
    _serverConfigs.insert("getNetworkApplianceWarmSpare", defaultConf);
    _serverIndices.insert("getNetworkApplianceWarmSpare", 0);
    _serverConfigs.insert("swapNetworkApplianceWarmSpare", defaultConf);
    _serverIndices.insert("swapNetworkApplianceWarmSpare", 0);
    _serverConfigs.insert("updateDeviceSwitchWarmSpare", defaultConf);
    _serverIndices.insert("updateDeviceSwitchWarmSpare", 0);
    _serverConfigs.insert("updateNetworkApplianceWarmSpare", defaultConf);
    _serverIndices.insert("updateNetworkApplianceWarmSpare", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIWarmSpareApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIWarmSpareApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIWarmSpareApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIWarmSpareApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIWarmSpareApi::setUsername(const QString &username) {
    _username = username;
}

void OAIWarmSpareApi::setPassword(const QString &password) {
    _password = password;
}


void OAIWarmSpareApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIWarmSpareApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIWarmSpareApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIWarmSpareApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIWarmSpareApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIWarmSpareApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIWarmSpareApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIWarmSpareApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIWarmSpareApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIWarmSpareApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIWarmSpareApi::getParamStylePrefix(const QString &style) {
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

QString OAIWarmSpareApi::getParamStyleSuffix(const QString &style) {
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

QString OAIWarmSpareApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIWarmSpareApi::getDeviceSwitchWarmSpare(const QString &serial) {
    QString fullPath = QString(_serverConfigs["getDeviceSwitchWarmSpare"][_serverIndices.value("getDeviceSwitchWarmSpare")].URL()+"/devices/{serial}/switch/warmSpare");
    
    if (_apiKeys.contains("meraki_api_key")) {
        addHeaders("meraki_api_key",_apiKeys.find("meraki_api_key").value());
    }
    
    
    {
        QString serialPathParam("{");
        serialPathParam.append("serial").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "serial", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"serial"+pathSuffix : pathPrefix;
        fullPath.replace(serialPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(serial)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWarmSpareApi::getDeviceSwitchWarmSpareCallback);
    connect(this, &OAIWarmSpareApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWarmSpareApi::getDeviceSwitchWarmSpareCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getDeviceSwitchWarmSpareSignal(output);
        Q_EMIT getDeviceSwitchWarmSpareSignalFull(worker, output);
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

        Q_EMIT getDeviceSwitchWarmSpareSignalE(output, error_type, error_str);
        Q_EMIT getDeviceSwitchWarmSpareSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getDeviceSwitchWarmSpareSignalError(output, error_type, error_str);
        Q_EMIT getDeviceSwitchWarmSpareSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWarmSpareApi::getNetworkApplianceWarmSpare(const QString &network_id) {
    QString fullPath = QString(_serverConfigs["getNetworkApplianceWarmSpare"][_serverIndices.value("getNetworkApplianceWarmSpare")].URL()+"/networks/{networkId}/appliance/warmSpare");
    
    if (_apiKeys.contains("meraki_api_key")) {
        addHeaders("meraki_api_key",_apiKeys.find("meraki_api_key").value());
    }
    
    
    {
        QString network_idPathParam("{");
        network_idPathParam.append("networkId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "networkId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"networkId"+pathSuffix : pathPrefix;
        fullPath.replace(network_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(network_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWarmSpareApi::getNetworkApplianceWarmSpareCallback);
    connect(this, &OAIWarmSpareApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWarmSpareApi::getNetworkApplianceWarmSpareCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNetworkApplianceWarmSpareSignal(output);
        Q_EMIT getNetworkApplianceWarmSpareSignalFull(worker, output);
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

        Q_EMIT getNetworkApplianceWarmSpareSignalE(output, error_type, error_str);
        Q_EMIT getNetworkApplianceWarmSpareSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNetworkApplianceWarmSpareSignalError(output, error_type, error_str);
        Q_EMIT getNetworkApplianceWarmSpareSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWarmSpareApi::swapNetworkApplianceWarmSpare(const QString &network_id) {
    QString fullPath = QString(_serverConfigs["swapNetworkApplianceWarmSpare"][_serverIndices.value("swapNetworkApplianceWarmSpare")].URL()+"/networks/{networkId}/appliance/warmSpare/swap");
    
    if (_apiKeys.contains("meraki_api_key")) {
        addHeaders("meraki_api_key",_apiKeys.find("meraki_api_key").value());
    }
    
    
    {
        QString network_idPathParam("{");
        network_idPathParam.append("networkId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "networkId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"networkId"+pathSuffix : pathPrefix;
        fullPath.replace(network_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(network_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWarmSpareApi::swapNetworkApplianceWarmSpareCallback);
    connect(this, &OAIWarmSpareApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWarmSpareApi::swapNetworkApplianceWarmSpareCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT swapNetworkApplianceWarmSpareSignal(output);
        Q_EMIT swapNetworkApplianceWarmSpareSignalFull(worker, output);
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

        Q_EMIT swapNetworkApplianceWarmSpareSignalE(output, error_type, error_str);
        Q_EMIT swapNetworkApplianceWarmSpareSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT swapNetworkApplianceWarmSpareSignalError(output, error_type, error_str);
        Q_EMIT swapNetworkApplianceWarmSpareSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWarmSpareApi::updateDeviceSwitchWarmSpare(const QString &serial, const OAIUpdateDeviceSwitchWarmSpare_request &oai_update_device_switch_warm_spare_request) {
    QString fullPath = QString(_serverConfigs["updateDeviceSwitchWarmSpare"][_serverIndices.value("updateDeviceSwitchWarmSpare")].URL()+"/devices/{serial}/switch/warmSpare");
    
    if (_apiKeys.contains("meraki_api_key")) {
        addHeaders("meraki_api_key",_apiKeys.find("meraki_api_key").value());
    }
    
    
    {
        QString serialPathParam("{");
        serialPathParam.append("serial").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "serial", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"serial"+pathSuffix : pathPrefix;
        fullPath.replace(serialPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(serial)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_update_device_switch_warm_spare_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWarmSpareApi::updateDeviceSwitchWarmSpareCallback);
    connect(this, &OAIWarmSpareApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWarmSpareApi::updateDeviceSwitchWarmSpareCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateDeviceSwitchWarmSpareSignal(output);
        Q_EMIT updateDeviceSwitchWarmSpareSignalFull(worker, output);
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

        Q_EMIT updateDeviceSwitchWarmSpareSignalE(output, error_type, error_str);
        Q_EMIT updateDeviceSwitchWarmSpareSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateDeviceSwitchWarmSpareSignalError(output, error_type, error_str);
        Q_EMIT updateDeviceSwitchWarmSpareSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWarmSpareApi::updateNetworkApplianceWarmSpare(const QString &network_id, const OAIUpdateNetworkApplianceWarmSpare_request &oai_update_network_appliance_warm_spare_request) {
    QString fullPath = QString(_serverConfigs["updateNetworkApplianceWarmSpare"][_serverIndices.value("updateNetworkApplianceWarmSpare")].URL()+"/networks/{networkId}/appliance/warmSpare");
    
    if (_apiKeys.contains("meraki_api_key")) {
        addHeaders("meraki_api_key",_apiKeys.find("meraki_api_key").value());
    }
    
    
    {
        QString network_idPathParam("{");
        network_idPathParam.append("networkId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "networkId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"networkId"+pathSuffix : pathPrefix;
        fullPath.replace(network_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(network_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_update_network_appliance_warm_spare_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWarmSpareApi::updateNetworkApplianceWarmSpareCallback);
    connect(this, &OAIWarmSpareApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWarmSpareApi::updateNetworkApplianceWarmSpareCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateNetworkApplianceWarmSpareSignal(output);
        Q_EMIT updateNetworkApplianceWarmSpareSignalFull(worker, output);
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

        Q_EMIT updateNetworkApplianceWarmSpareSignalE(output, error_type, error_str);
        Q_EMIT updateNetworkApplianceWarmSpareSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateNetworkApplianceWarmSpareSignalError(output, error_type, error_str);
        Q_EMIT updateNetworkApplianceWarmSpareSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWarmSpareApi::tokenAvailable(){

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
