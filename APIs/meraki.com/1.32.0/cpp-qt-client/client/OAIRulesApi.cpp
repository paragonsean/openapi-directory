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

#include "OAIRulesApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIRulesApi::OAIRulesApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIRulesApi::~OAIRulesApi() {
}

void OAIRulesApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.meraki.com/api/v1"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("getNetworkApplianceTrafficShapingRules", defaultConf);
    _serverIndices.insert("getNetworkApplianceTrafficShapingRules", 0);
    _serverConfigs.insert("getNetworkWirelessSsidTrafficShapingRules", defaultConf);
    _serverIndices.insert("getNetworkWirelessSsidTrafficShapingRules", 0);
    _serverConfigs.insert("updateNetworkApplianceTrafficShapingRules", defaultConf);
    _serverIndices.insert("updateNetworkApplianceTrafficShapingRules", 0);
    _serverConfigs.insert("updateNetworkWirelessSsidTrafficShapingRules", defaultConf);
    _serverIndices.insert("updateNetworkWirelessSsidTrafficShapingRules", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIRulesApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIRulesApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIRulesApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIRulesApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIRulesApi::setUsername(const QString &username) {
    _username = username;
}

void OAIRulesApi::setPassword(const QString &password) {
    _password = password;
}


void OAIRulesApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIRulesApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIRulesApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIRulesApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIRulesApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIRulesApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIRulesApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIRulesApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIRulesApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIRulesApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIRulesApi::getParamStylePrefix(const QString &style) {
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

QString OAIRulesApi::getParamStyleSuffix(const QString &style) {
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

QString OAIRulesApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIRulesApi::getNetworkApplianceTrafficShapingRules(const QString &network_id) {
    QString fullPath = QString(_serverConfigs["getNetworkApplianceTrafficShapingRules"][_serverIndices.value("getNetworkApplianceTrafficShapingRules")].URL()+"/networks/{networkId}/appliance/trafficShaping/rules");
    
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIRulesApi::getNetworkApplianceTrafficShapingRulesCallback);
    connect(this, &OAIRulesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIRulesApi::getNetworkApplianceTrafficShapingRulesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNetworkApplianceTrafficShapingRulesSignal(output);
        Q_EMIT getNetworkApplianceTrafficShapingRulesSignalFull(worker, output);
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

        Q_EMIT getNetworkApplianceTrafficShapingRulesSignalE(output, error_type, error_str);
        Q_EMIT getNetworkApplianceTrafficShapingRulesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNetworkApplianceTrafficShapingRulesSignalError(output, error_type, error_str);
        Q_EMIT getNetworkApplianceTrafficShapingRulesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIRulesApi::getNetworkWirelessSsidTrafficShapingRules(const QString &network_id, const QString &number) {
    QString fullPath = QString(_serverConfigs["getNetworkWirelessSsidTrafficShapingRules"][_serverIndices.value("getNetworkWirelessSsidTrafficShapingRules")].URL()+"/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules");
    
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
    
    {
        QString numberPathParam("{");
        numberPathParam.append("number").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "number", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"number"+pathSuffix : pathPrefix;
        fullPath.replace(numberPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(number)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIRulesApi::getNetworkWirelessSsidTrafficShapingRulesCallback);
    connect(this, &OAIRulesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIRulesApi::getNetworkWirelessSsidTrafficShapingRulesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getNetworkWirelessSsidTrafficShapingRulesSignal(output);
        Q_EMIT getNetworkWirelessSsidTrafficShapingRulesSignalFull(worker, output);
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

        Q_EMIT getNetworkWirelessSsidTrafficShapingRulesSignalE(output, error_type, error_str);
        Q_EMIT getNetworkWirelessSsidTrafficShapingRulesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getNetworkWirelessSsidTrafficShapingRulesSignalError(output, error_type, error_str);
        Q_EMIT getNetworkWirelessSsidTrafficShapingRulesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIRulesApi::updateNetworkApplianceTrafficShapingRules(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkApplianceTrafficShapingRules_request> &oai_update_network_appliance_traffic_shaping_rules_request) {
    QString fullPath = QString(_serverConfigs["updateNetworkApplianceTrafficShapingRules"][_serverIndices.value("updateNetworkApplianceTrafficShapingRules")].URL()+"/networks/{networkId}/appliance/trafficShaping/rules");
    
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

    if (oai_update_network_appliance_traffic_shaping_rules_request.hasValue()){

        
        QByteArray output = oai_update_network_appliance_traffic_shaping_rules_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIRulesApi::updateNetworkApplianceTrafficShapingRulesCallback);
    connect(this, &OAIRulesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIRulesApi::updateNetworkApplianceTrafficShapingRulesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateNetworkApplianceTrafficShapingRulesSignal(output);
        Q_EMIT updateNetworkApplianceTrafficShapingRulesSignalFull(worker, output);
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

        Q_EMIT updateNetworkApplianceTrafficShapingRulesSignalE(output, error_type, error_str);
        Q_EMIT updateNetworkApplianceTrafficShapingRulesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateNetworkApplianceTrafficShapingRulesSignalError(output, error_type, error_str);
        Q_EMIT updateNetworkApplianceTrafficShapingRulesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIRulesApi::updateNetworkWirelessSsidTrafficShapingRules(const QString &network_id, const QString &number, const ::OpenAPI::OptionalParam<OAIUpdateNetworkWirelessSsidTrafficShapingRules_request> &oai_update_network_wireless_ssid_traffic_shaping_rules_request) {
    QString fullPath = QString(_serverConfigs["updateNetworkWirelessSsidTrafficShapingRules"][_serverIndices.value("updateNetworkWirelessSsidTrafficShapingRules")].URL()+"/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules");
    
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
    
    {
        QString numberPathParam("{");
        numberPathParam.append("number").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "number", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"number"+pathSuffix : pathPrefix;
        fullPath.replace(numberPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(number)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_update_network_wireless_ssid_traffic_shaping_rules_request.hasValue()){

        
        QByteArray output = oai_update_network_wireless_ssid_traffic_shaping_rules_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIRulesApi::updateNetworkWirelessSsidTrafficShapingRulesCallback);
    connect(this, &OAIRulesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIRulesApi::updateNetworkWirelessSsidTrafficShapingRulesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateNetworkWirelessSsidTrafficShapingRulesSignal(output);
        Q_EMIT updateNetworkWirelessSsidTrafficShapingRulesSignalFull(worker, output);
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

        Q_EMIT updateNetworkWirelessSsidTrafficShapingRulesSignalE(output, error_type, error_str);
        Q_EMIT updateNetworkWirelessSsidTrafficShapingRulesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateNetworkWirelessSsidTrafficShapingRulesSignalError(output, error_type, error_str);
        Q_EMIT updateNetworkWirelessSsidTrafficShapingRulesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIRulesApi::tokenAvailable(){

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
