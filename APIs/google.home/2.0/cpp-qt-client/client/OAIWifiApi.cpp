/**
 * Google Home
 * # Google Home Local API This is an unofficial documentation of the local API used by the Home app to communicate with GH devices. [GitHub Repo](https://github.com/rithvikvibhu/GHLocalApi)  [![GitHub stars](https://img.shields.io/github/stars/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/stargazers) [![GitHub license](https://img.shields.io/github/license/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/blob/master/LICENSE.md)  ## Getting Started  Requests must be made over HTTPS, port 8443, so the base URL for these endpoints is: `https://<google-home-ip>:8443/setup/`  Get the IP of Google Home from the Google Home app (Device Settings -> End of the list) or from your router.  GET requests are simple, in the browser kind.   POST requests need to set the header (when there's a body): `content-type: application/json`  ## Authentication  Since June 2019, most requests (with exceptions like `/setup/eureka_info`) need a local authorization token.  There are 3 kinds of tokens involved here:  ### Local Authorization Token This token must be sent in all requests in the header `cast-local-authorization-token`. It is short-lived (~1 day) and may change unexpectedly (with a sync, change in homegraph, etc.) ##### Get this token - With access to an android device, [get this token directly by either method](https://gist.github.com/rithvikvibhu/1a0f4937af957ef6a78453e3be482c1f). - Without a device, or to integrate it with a script, use an access token to get the homegraph and extract the token. To get an access token, read the next section. Check the example section for more info.  ### Access Token This is a standard google oauth2 access token. It is in the form `ya29.***`. This gives access to the Google Home Foyer API. These expire in an hour. Use this to get the homegraph (and then the local authorization token above). ##### Get this token To get this access token, either a Google account username/password or a Google Master Token is needed. More info in the gist. Use the script [from this gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d).  ### Master Token This is in the form `aas_et/_***` and can be used to request access tokens. ##### Get this token The same [script in the gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d) that gets the access token can also get the master token. Needs Google account creds.  ## Example  Here's the whole flow from just a pair of username/password to using the local API.  Prerequisites: - [grpcurl](https://github.com/fullstorydev/grpcurl) - [Proto files](https://drive.google.com/drive/folders/1RvnN3y-G23pd2SWHmfV_7sef8QU5GNF4?usp=sharing) (preserve folder structure)  ### 1. Get an access token with the script - Download get_tokens.py - Fill in username and password ```sh python3 get_tokens.py # Note down the access token printed. ```  ### 2. Use the access token and get home graph - This prints the json and uses jq to parse and filter out the fields deviceName and localAuthToken - This will give a list of all devices and their local auth tokens ```sh ./grpcurl -H 'authorization: Bearer ya29.a0Af****' \\  -import-path /path/to/protos \\  -proto /path/to/protos/google/internal/home/foyer/v1.proto \\  googlehomefoyer-pa.googleapis.com:443 \\  google.internal.home.foyer.v1.StructuresService/GetHomeGraph | jq '.home.devices[] | {deviceName, localAuthToken}' # Note down the local auth token for the device you want. ```  ### 3. Make the call to the local device using the local auth token ```sh curl -H \"cast-local-authorization-token: LOCAL_AUTH_TOKEN\" --verbose --insecure https://192.168.0.18:8443/setup/bluetooth/status ```
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWifiApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIWifiApi::OAIWifiApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIWifiApi::~OAIWifiApi() {
}

void OAIWifiApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://example.com/setup"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("connecttoWiFiNetwork", defaultConf);
    _serverIndices.insert("connecttoWiFiNetwork", 0);
    _serverConfigs.insert("forgetWiFiNetwork", defaultConf);
    _serverIndices.insert("forgetWiFiNetwork", 0);
    _serverConfigs.insert("getSavedNetworks", defaultConf);
    _serverIndices.insert("getSavedNetworks", 0);
    _serverConfigs.insert("getWiFiScanResults", defaultConf);
    _serverIndices.insert("getWiFiScanResults", 0);
    _serverConfigs.insert("scanforNetworks", defaultConf);
    _serverIndices.insert("scanforNetworks", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIWifiApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIWifiApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIWifiApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIWifiApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIWifiApi::setUsername(const QString &username) {
    _username = username;
}

void OAIWifiApi::setPassword(const QString &password) {
    _password = password;
}


void OAIWifiApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIWifiApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIWifiApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIWifiApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIWifiApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIWifiApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIWifiApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIWifiApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIWifiApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIWifiApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIWifiApi::getParamStylePrefix(const QString &style) {
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

QString OAIWifiApi::getParamStyleSuffix(const QString &style) {
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

QString OAIWifiApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIWifiApi::connecttoWiFiNetwork(const OAIConnecttoWi_FiNetworkRequest &oai_connectto_wi_fi_network_request) {
    QString fullPath = QString(_serverConfigs["connecttoWiFiNetwork"][_serverIndices.value("connecttoWiFiNetwork")].URL()+"/connect_wifi");
    
    if (_apiKeys.contains("cast-local-authorization-token")) {
        addHeaders("cast-local-authorization-token",_apiKeys.find("cast-local-authorization-token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_connectto_wi_fi_network_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWifiApi::connecttoWiFiNetworkCallback);
    connect(this, &OAIWifiApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWifiApi::connecttoWiFiNetworkCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT connecttoWiFiNetworkSignal();
        Q_EMIT connecttoWiFiNetworkSignalFull(worker);
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

        Q_EMIT connecttoWiFiNetworkSignalE(error_type, error_str);
        Q_EMIT connecttoWiFiNetworkSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT connecttoWiFiNetworkSignalError(error_type, error_str);
        Q_EMIT connecttoWiFiNetworkSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWifiApi::forgetWiFiNetwork(const OAIForgetWi_FiNetworkRequest &oai_forget_wi_fi_network_request) {
    QString fullPath = QString(_serverConfigs["forgetWiFiNetwork"][_serverIndices.value("forgetWiFiNetwork")].URL()+"/forget_wifi");
    
    if (_apiKeys.contains("cast-local-authorization-token")) {
        addHeaders("cast-local-authorization-token",_apiKeys.find("cast-local-authorization-token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_forget_wi_fi_network_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWifiApi::forgetWiFiNetworkCallback);
    connect(this, &OAIWifiApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWifiApi::forgetWiFiNetworkCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT forgetWiFiNetworkSignal(output);
        Q_EMIT forgetWiFiNetworkSignalFull(worker, output);
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

        Q_EMIT forgetWiFiNetworkSignalE(output, error_type, error_str);
        Q_EMIT forgetWiFiNetworkSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT forgetWiFiNetworkSignalError(output, error_type, error_str);
        Q_EMIT forgetWiFiNetworkSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWifiApi::getSavedNetworks() {
    QString fullPath = QString(_serverConfigs["getSavedNetworks"][_serverIndices.value("getSavedNetworks")].URL()+"/configured_networks");
    
    if (_apiKeys.contains("cast-local-authorization-token")) {
        addHeaders("cast-local-authorization-token",_apiKeys.find("cast-local-authorization-token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWifiApi::getSavedNetworksCallback);
    connect(this, &OAIWifiApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWifiApi::getSavedNetworksCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIExample113> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIExample113 val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getSavedNetworksSignal(output);
        Q_EMIT getSavedNetworksSignalFull(worker, output);
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

        Q_EMIT getSavedNetworksSignalE(output, error_type, error_str);
        Q_EMIT getSavedNetworksSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getSavedNetworksSignalError(output, error_type, error_str);
        Q_EMIT getSavedNetworksSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWifiApi::getWiFiScanResults() {
    QString fullPath = QString(_serverConfigs["getWiFiScanResults"][_serverIndices.value("getWiFiScanResults")].URL()+"/scan_results");
    
    if (_apiKeys.contains("cast-local-authorization-token")) {
        addHeaders("cast-local-authorization-token",_apiKeys.find("cast-local-authorization-token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWifiApi::getWiFiScanResultsCallback);
    connect(this, &OAIWifiApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWifiApi::getWiFiScanResultsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIExample114> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIExample114 val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getWiFiScanResultsSignal(output);
        Q_EMIT getWiFiScanResultsSignalFull(worker, output);
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

        Q_EMIT getWiFiScanResultsSignalE(output, error_type, error_str);
        Q_EMIT getWiFiScanResultsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getWiFiScanResultsSignalError(output, error_type, error_str);
        Q_EMIT getWiFiScanResultsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWifiApi::scanforNetworks() {
    QString fullPath = QString(_serverConfigs["scanforNetworks"][_serverIndices.value("scanforNetworks")].URL()+"/scan_wifi");
    
    if (_apiKeys.contains("cast-local-authorization-token")) {
        addHeaders("cast-local-authorization-token",_apiKeys.find("cast-local-authorization-token").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIWifiApi::scanforNetworksCallback);
    connect(this, &OAIWifiApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIWifiApi::scanforNetworksCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT scanforNetworksSignal(output);
        Q_EMIT scanforNetworksSignalFull(worker, output);
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

        Q_EMIT scanforNetworksSignalE(output, error_type, error_str);
        Q_EMIT scanforNetworksSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT scanforNetworksSignalError(output, error_type, error_str);
        Q_EMIT scanforNetworksSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIWifiApi::tokenAvailable(){

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
