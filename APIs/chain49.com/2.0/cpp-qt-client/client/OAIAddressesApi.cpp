/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddressesApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIAddressesApi::OAIAddressesApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIAddressesApi::~OAIAddressesApi() {
}

void OAIAddressesApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://api.chain49.com"),
    "Main",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://chain49.p.rapidapi.com"),
    "RapidAPI",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("getAddressV2", defaultConf);
    _serverIndices.insert("getAddressV2", 0);
    _serverConfigs.insert("getBalanceHistoryV2", defaultConf);
    _serverIndices.insert("getBalanceHistoryV2", 0);
    _serverConfigs.insert("getUTXOV2", defaultConf);
    _serverIndices.insert("getUTXOV2", 0);
    _serverConfigs.insert("getXpubV2", defaultConf);
    _serverIndices.insert("getXpubV2", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIAddressesApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIAddressesApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIAddressesApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIAddressesApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIAddressesApi::setUsername(const QString &username) {
    _username = username;
}

void OAIAddressesApi::setPassword(const QString &password) {
    _password = password;
}


void OAIAddressesApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIAddressesApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIAddressesApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIAddressesApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIAddressesApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIAddressesApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIAddressesApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIAddressesApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIAddressesApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIAddressesApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIAddressesApi::getParamStylePrefix(const QString &style) {
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

QString OAIAddressesApi::getParamStyleSuffix(const QString &style) {
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

QString OAIAddressesApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIAddressesApi::getAddressV2(const QString &blockchain, const QString &address, const ::OpenAPI::OptionalParam<qint32> &page, const ::OpenAPI::OptionalParam<qint32> &page_size, const ::OpenAPI::OptionalParam<qint32> &from_block, const ::OpenAPI::OptionalParam<qint32> &to_block, const ::OpenAPI::OptionalParam<QString> &details, const ::OpenAPI::OptionalParam<QString> &contract, const ::OpenAPI::OptionalParam<QString> &secondary) {
    QString fullPath = QString(_serverConfigs["getAddressV2"][_serverIndices.value("getAddressV2")].URL()+"/{blockchain}/v2/address/{address}");
    
    if (_apiKeys.contains("X-RapidAPI-Host")) {
        addHeaders("X-RapidAPI-Host",_apiKeys.find("X-RapidAPI-Host").value());
    }
    
    if (_apiKeys.contains("X-API-Key")) {
        addHeaders("X-API-Key",_apiKeys.find("X-API-Key").value());
    }
    
    if (_apiKeys.contains("X-RapidAPI-Key")) {
        addHeaders("X-RapidAPI-Key",_apiKeys.find("X-RapidAPI-Key").value());
    }
    
    
    {
        QString blockchainPathParam("{");
        blockchainPathParam.append("blockchain").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "blockchain", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"blockchain"+pathSuffix : pathPrefix;
        fullPath.replace(blockchainPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(blockchain)));
    }
    
    {
        QString addressPathParam("{");
        addressPathParam.append("address").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "address", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"address"+pathSuffix : pathPrefix;
        fullPath.replace(addressPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(address)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    if (page_size.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "pageSize", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("pageSize")).append(querySuffix).append(QUrl::toPercentEncoding(page_size.stringValue()));
    }
    if (from_block.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "fromBlock", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("fromBlock")).append(querySuffix).append(QUrl::toPercentEncoding(from_block.stringValue()));
    }
    if (to_block.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "toBlock", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("toBlock")).append(querySuffix).append(QUrl::toPercentEncoding(to_block.stringValue()));
    }
    if (details.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "details", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("details")).append(querySuffix).append(QUrl::toPercentEncoding(details.stringValue()));
    }
    if (contract.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "contract", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("contract")).append(querySuffix).append(QUrl::toPercentEncoding(contract.stringValue()));
    }
    if (secondary.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "secondary", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("secondary")).append(querySuffix).append(QUrl::toPercentEncoding(secondary.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAddressesApi::getAddressV2Callback);
    connect(this, &OAIAddressesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAddressesApi::getAddressV2Callback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getAddressV2Signal(output);
        Q_EMIT getAddressV2SignalFull(worker, output);
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

        Q_EMIT getAddressV2SignalE(output, error_type, error_str);
        Q_EMIT getAddressV2SignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getAddressV2SignalError(output, error_type, error_str);
        Q_EMIT getAddressV2SignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAddressesApi::getBalanceHistoryV2(const QString &blockchain, const QString &address_or_xpub, const ::OpenAPI::OptionalParam<QString> &from_date, const ::OpenAPI::OptionalParam<QString> &to_date, const ::OpenAPI::OptionalParam<QString> &fiatcurrency, const ::OpenAPI::OptionalParam<double> &group_by) {
    QString fullPath = QString(_serverConfigs["getBalanceHistoryV2"][_serverIndices.value("getBalanceHistoryV2")].URL()+"/{blockchain}/v2/balancehistory/{addressOrXpub}");
    
    if (_apiKeys.contains("X-RapidAPI-Host")) {
        addHeaders("X-RapidAPI-Host",_apiKeys.find("X-RapidAPI-Host").value());
    }
    
    if (_apiKeys.contains("X-API-Key")) {
        addHeaders("X-API-Key",_apiKeys.find("X-API-Key").value());
    }
    
    if (_apiKeys.contains("X-RapidAPI-Key")) {
        addHeaders("X-RapidAPI-Key",_apiKeys.find("X-RapidAPI-Key").value());
    }
    
    
    {
        QString blockchainPathParam("{");
        blockchainPathParam.append("blockchain").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "blockchain", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"blockchain"+pathSuffix : pathPrefix;
        fullPath.replace(blockchainPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(blockchain)));
    }
    
    {
        QString address_or_xpubPathParam("{");
        address_or_xpubPathParam.append("addressOrXpub").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "addressOrXpub", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"addressOrXpub"+pathSuffix : pathPrefix;
        fullPath.replace(address_or_xpubPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(address_or_xpub)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (from_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "fromDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("fromDate")).append(querySuffix).append(QUrl::toPercentEncoding(from_date.stringValue()));
    }
    if (to_date.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "toDate", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("toDate")).append(querySuffix).append(QUrl::toPercentEncoding(to_date.stringValue()));
    }
    if (fiatcurrency.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "fiatcurrency", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("fiatcurrency")).append(querySuffix).append(QUrl::toPercentEncoding(fiatcurrency.stringValue()));
    }
    if (group_by.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "groupBy", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("groupBy")).append(querySuffix).append(QUrl::toPercentEncoding(group_by.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAddressesApi::getBalanceHistoryV2Callback);
    connect(this, &OAIAddressesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAddressesApi::getBalanceHistoryV2Callback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAIGetBalanceHistoryV2_200_response_inner> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAIGetBalanceHistoryV2_200_response_inner val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getBalanceHistoryV2Signal(output);
        Q_EMIT getBalanceHistoryV2SignalFull(worker, output);
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

        Q_EMIT getBalanceHistoryV2SignalE(output, error_type, error_str);
        Q_EMIT getBalanceHistoryV2SignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getBalanceHistoryV2SignalError(output, error_type, error_str);
        Q_EMIT getBalanceHistoryV2SignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAddressesApi::getUTXOV2(const QString &blockchain, const QString &address_or_xpub, const ::OpenAPI::OptionalParam<bool> &confirmed) {
    QString fullPath = QString(_serverConfigs["getUTXOV2"][_serverIndices.value("getUTXOV2")].URL()+"/{blockchain}/v2/utxo/{addressOrXpub}");
    
    if (_apiKeys.contains("X-RapidAPI-Host")) {
        addHeaders("X-RapidAPI-Host",_apiKeys.find("X-RapidAPI-Host").value());
    }
    
    if (_apiKeys.contains("X-API-Key")) {
        addHeaders("X-API-Key",_apiKeys.find("X-API-Key").value());
    }
    
    if (_apiKeys.contains("X-RapidAPI-Key")) {
        addHeaders("X-RapidAPI-Key",_apiKeys.find("X-RapidAPI-Key").value());
    }
    
    
    {
        QString blockchainPathParam("{");
        blockchainPathParam.append("blockchain").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "blockchain", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"blockchain"+pathSuffix : pathPrefix;
        fullPath.replace(blockchainPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(blockchain)));
    }
    
    {
        QString address_or_xpubPathParam("{");
        address_or_xpubPathParam.append("addressOrXpub").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "addressOrXpub", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"addressOrXpub"+pathSuffix : pathPrefix;
        fullPath.replace(address_or_xpubPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(address_or_xpub)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (confirmed.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "confirmed", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("confirmed")).append(querySuffix).append(QUrl::toPercentEncoding(confirmed.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAddressesApi::getUTXOV2Callback);
    connect(this, &OAIAddressesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAddressesApi::getUTXOV2Callback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<QJsonValue> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        QJsonValue val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getUTXOV2Signal(output);
        Q_EMIT getUTXOV2SignalFull(worker, output);
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

        Q_EMIT getUTXOV2SignalE(output, error_type, error_str);
        Q_EMIT getUTXOV2SignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getUTXOV2SignalError(output, error_type, error_str);
        Q_EMIT getUTXOV2SignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAddressesApi::getXpubV2(const QString &blockchain, const QString &xpub, const ::OpenAPI::OptionalParam<qint32> &page, const ::OpenAPI::OptionalParam<qint32> &page_size, const ::OpenAPI::OptionalParam<qint32> &from_block, const ::OpenAPI::OptionalParam<qint32> &to_block, const ::OpenAPI::OptionalParam<QString> &details, const ::OpenAPI::OptionalParam<QString> &tokens, const ::OpenAPI::OptionalParam<QString> &secondary) {
    QString fullPath = QString(_serverConfigs["getXpubV2"][_serverIndices.value("getXpubV2")].URL()+"/{blockchain}/v2/xpub/{xpub}");
    
    if (_apiKeys.contains("X-RapidAPI-Host")) {
        addHeaders("X-RapidAPI-Host",_apiKeys.find("X-RapidAPI-Host").value());
    }
    
    if (_apiKeys.contains("X-API-Key")) {
        addHeaders("X-API-Key",_apiKeys.find("X-API-Key").value());
    }
    
    if (_apiKeys.contains("X-RapidAPI-Key")) {
        addHeaders("X-RapidAPI-Key",_apiKeys.find("X-RapidAPI-Key").value());
    }
    
    
    {
        QString blockchainPathParam("{");
        blockchainPathParam.append("blockchain").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "blockchain", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"blockchain"+pathSuffix : pathPrefix;
        fullPath.replace(blockchainPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(blockchain)));
    }
    
    {
        QString xpubPathParam("{");
        xpubPathParam.append("xpub").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "xpub", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"xpub"+pathSuffix : pathPrefix;
        fullPath.replace(xpubPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(xpub)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (page.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "page", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("page")).append(querySuffix).append(QUrl::toPercentEncoding(page.stringValue()));
    }
    if (page_size.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "pageSize", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("pageSize")).append(querySuffix).append(QUrl::toPercentEncoding(page_size.stringValue()));
    }
    if (from_block.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "fromBlock", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("fromBlock")).append(querySuffix).append(QUrl::toPercentEncoding(from_block.stringValue()));
    }
    if (to_block.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "toBlock", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("toBlock")).append(querySuffix).append(QUrl::toPercentEncoding(to_block.stringValue()));
    }
    if (details.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "details", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("details")).append(querySuffix).append(QUrl::toPercentEncoding(details.stringValue()));
    }
    if (tokens.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "tokens", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("tokens")).append(querySuffix).append(QUrl::toPercentEncoding(tokens.stringValue()));
    }
    if (secondary.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "secondary", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("secondary")).append(querySuffix).append(QUrl::toPercentEncoding(secondary.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIAddressesApi::getXpubV2Callback);
    connect(this, &OAIAddressesApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIAddressesApi::getXpubV2Callback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetXpubV2_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getXpubV2Signal(output);
        Q_EMIT getXpubV2SignalFull(worker, output);
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

        Q_EMIT getXpubV2SignalE(output, error_type, error_str);
        Q_EMIT getXpubV2SignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getXpubV2SignalError(output, error_type, error_str);
        Q_EMIT getXpubV2SignalErrorFull(worker, error_type, error_str);
    }
}

void OAIAddressesApi::tokenAvailable(){

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
