/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIConfigurableProductsSkuOptionsIdApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIConfigurableProductsSkuOptionsIdApi::OAIConfigurableProductsSkuOptionsIdApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIConfigurableProductsSkuOptionsIdApi::~OAIConfigurableProductsSkuOptionsIdApi() {
}

void OAIConfigurableProductsSkuOptionsIdApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://example.com/rest/default"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("configurableProductOptionRepositoryV1DeleteByIdDelete", defaultConf);
    _serverIndices.insert("configurableProductOptionRepositoryV1DeleteByIdDelete", 0);
    _serverConfigs.insert("configurableProductOptionRepositoryV1GetGet", defaultConf);
    _serverIndices.insert("configurableProductOptionRepositoryV1GetGet", 0);
    _serverConfigs.insert("configurableProductOptionRepositoryV1SavePut", defaultConf);
    _serverIndices.insert("configurableProductOptionRepositoryV1SavePut", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIConfigurableProductsSkuOptionsIdApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIConfigurableProductsSkuOptionsIdApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIConfigurableProductsSkuOptionsIdApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIConfigurableProductsSkuOptionsIdApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIConfigurableProductsSkuOptionsIdApi::setUsername(const QString &username) {
    _username = username;
}

void OAIConfigurableProductsSkuOptionsIdApi::setPassword(const QString &password) {
    _password = password;
}


void OAIConfigurableProductsSkuOptionsIdApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIConfigurableProductsSkuOptionsIdApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIConfigurableProductsSkuOptionsIdApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIConfigurableProductsSkuOptionsIdApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIConfigurableProductsSkuOptionsIdApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIConfigurableProductsSkuOptionsIdApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIConfigurableProductsSkuOptionsIdApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIConfigurableProductsSkuOptionsIdApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIConfigurableProductsSkuOptionsIdApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIConfigurableProductsSkuOptionsIdApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIConfigurableProductsSkuOptionsIdApi::getParamStylePrefix(const QString &style) {
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

QString OAIConfigurableProductsSkuOptionsIdApi::getParamStyleSuffix(const QString &style) {
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

QString OAIConfigurableProductsSkuOptionsIdApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1DeleteByIdDelete(const QString &sku, const qint32 &id) {
    QString fullPath = QString(_serverConfigs["configurableProductOptionRepositoryV1DeleteByIdDelete"][_serverIndices.value("configurableProductOptionRepositoryV1DeleteByIdDelete")].URL()+"/V1/configurable-products/{sku}/options/{id}");
    
    
    {
        QString skuPathParam("{");
        skuPathParam.append("sku").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "sku", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"sku"+pathSuffix : pathPrefix;
        fullPath.replace(skuPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sku)));
    }
    
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
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1DeleteByIdDeleteCallback);
    connect(this, &OAIConfigurableProductsSkuOptionsIdApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1DeleteByIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    bool output;
    ::OpenAPI::fromStringValue(QString(worker->response), output);
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT configurableProductOptionRepositoryV1DeleteByIdDeleteSignal(output);
        Q_EMIT configurableProductOptionRepositoryV1DeleteByIdDeleteSignalFull(worker, output);
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

        Q_EMIT configurableProductOptionRepositoryV1DeleteByIdDeleteSignalE(output, error_type, error_str);
        Q_EMIT configurableProductOptionRepositoryV1DeleteByIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT configurableProductOptionRepositoryV1DeleteByIdDeleteSignalError(output, error_type, error_str);
        Q_EMIT configurableProductOptionRepositoryV1DeleteByIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1GetGet(const QString &sku, const qint32 &id) {
    QString fullPath = QString(_serverConfigs["configurableProductOptionRepositoryV1GetGet"][_serverIndices.value("configurableProductOptionRepositoryV1GetGet")].URL()+"/V1/configurable-products/{sku}/options/{id}");
    
    
    {
        QString skuPathParam("{");
        skuPathParam.append("sku").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "sku", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"sku"+pathSuffix : pathPrefix;
        fullPath.replace(skuPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sku)));
    }
    
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
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1GetGetCallback);
    connect(this, &OAIConfigurableProductsSkuOptionsIdApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1GetGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIConfigurable_product_data_option_interface output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT configurableProductOptionRepositoryV1GetGetSignal(output);
        Q_EMIT configurableProductOptionRepositoryV1GetGetSignalFull(worker, output);
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

        Q_EMIT configurableProductOptionRepositoryV1GetGetSignalE(output, error_type, error_str);
        Q_EMIT configurableProductOptionRepositoryV1GetGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT configurableProductOptionRepositoryV1GetGetSignalError(output, error_type, error_str);
        Q_EMIT configurableProductOptionRepositoryV1GetGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1SavePut(const QString &sku, const QString &id, const ::OpenAPI::OptionalParam<OAIConfigurableProductOptionRepositoryV1SavePost_request> &oai_configurable_product_option_repository_v1_save_post_request) {
    QString fullPath = QString(_serverConfigs["configurableProductOptionRepositoryV1SavePut"][_serverIndices.value("configurableProductOptionRepositoryV1SavePut")].URL()+"/V1/configurable-products/{sku}/options/{id}");
    
    
    {
        QString skuPathParam("{");
        skuPathParam.append("sku").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "sku", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"sku"+pathSuffix : pathPrefix;
        fullPath.replace(skuPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sku)));
    }
    
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
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"id"+pathSuffix : pathPrefix;
        fullPath.replace(idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_configurable_product_option_repository_v1_save_post_request.hasValue()){

        
        QByteArray output = oai_configurable_product_option_repository_v1_save_post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1SavePutCallback);
    connect(this, &OAIConfigurableProductsSkuOptionsIdApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIConfigurableProductsSkuOptionsIdApi::configurableProductOptionRepositoryV1SavePutCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    qint32 output;
    ::OpenAPI::fromStringValue(QString(worker->response), output);
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT configurableProductOptionRepositoryV1SavePutSignal(output);
        Q_EMIT configurableProductOptionRepositoryV1SavePutSignalFull(worker, output);
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

        Q_EMIT configurableProductOptionRepositoryV1SavePutSignalE(output, error_type, error_str);
        Q_EMIT configurableProductOptionRepositoryV1SavePutSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT configurableProductOptionRepositoryV1SavePutSignalError(output, error_type, error_str);
        Q_EMIT configurableProductOptionRepositoryV1SavePutSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIConfigurableProductsSkuOptionsIdApi::tokenAvailable(){

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
