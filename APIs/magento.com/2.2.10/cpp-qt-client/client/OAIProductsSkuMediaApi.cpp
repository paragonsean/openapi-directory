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

#include "OAIProductsSkuMediaApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIProductsSkuMediaApi::OAIProductsSkuMediaApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIProductsSkuMediaApi::~OAIProductsSkuMediaApi() {
}

void OAIProductsSkuMediaApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://example.com/rest/default"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    _serverConfigs.insert("catalogProductAttributeMediaGalleryManagementV1CreatePost", defaultConf);
    _serverIndices.insert("catalogProductAttributeMediaGalleryManagementV1CreatePost", 0);
    _serverConfigs.insert("catalogProductAttributeMediaGalleryManagementV1GetListGet", defaultConf);
    _serverIndices.insert("catalogProductAttributeMediaGalleryManagementV1GetListGet", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIProductsSkuMediaApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIProductsSkuMediaApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIProductsSkuMediaApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIProductsSkuMediaApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIProductsSkuMediaApi::setUsername(const QString &username) {
    _username = username;
}

void OAIProductsSkuMediaApi::setPassword(const QString &password) {
    _password = password;
}


void OAIProductsSkuMediaApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIProductsSkuMediaApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIProductsSkuMediaApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIProductsSkuMediaApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIProductsSkuMediaApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIProductsSkuMediaApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIProductsSkuMediaApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIProductsSkuMediaApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIProductsSkuMediaApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIProductsSkuMediaApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIProductsSkuMediaApi::getParamStylePrefix(const QString &style) {
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

QString OAIProductsSkuMediaApi::getParamStyleSuffix(const QString &style) {
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

QString OAIProductsSkuMediaApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIProductsSkuMediaApi::catalogProductAttributeMediaGalleryManagementV1CreatePost(const QString &sku, const ::OpenAPI::OptionalParam<OAICatalogProductAttributeMediaGalleryManagementV1CreatePost_request> &oai_catalog_product_attribute_media_gallery_management_v1_create_post_request) {
    QString fullPath = QString(_serverConfigs["catalogProductAttributeMediaGalleryManagementV1CreatePost"][_serverIndices.value("catalogProductAttributeMediaGalleryManagementV1CreatePost")].URL()+"/V1/products/{sku}/media");
    
    
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
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_catalog_product_attribute_media_gallery_management_v1_create_post_request.hasValue()){

        
        QByteArray output = oai_catalog_product_attribute_media_gallery_management_v1_create_post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProductsSkuMediaApi::catalogProductAttributeMediaGalleryManagementV1CreatePostCallback);
    connect(this, &OAIProductsSkuMediaApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProductsSkuMediaApi::catalogProductAttributeMediaGalleryManagementV1CreatePostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    qint32 output;
    ::OpenAPI::fromStringValue(QString(worker->response), output);
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1CreatePostSignal(output);
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1CreatePostSignalFull(worker, output);
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

        Q_EMIT catalogProductAttributeMediaGalleryManagementV1CreatePostSignalE(output, error_type, error_str);
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1CreatePostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT catalogProductAttributeMediaGalleryManagementV1CreatePostSignalError(output, error_type, error_str);
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1CreatePostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProductsSkuMediaApi::catalogProductAttributeMediaGalleryManagementV1GetListGet(const QString &sku) {
    QString fullPath = QString(_serverConfigs["catalogProductAttributeMediaGalleryManagementV1GetListGet"][_serverIndices.value("catalogProductAttributeMediaGalleryManagementV1GetListGet")].URL()+"/V1/products/{sku}/media");
    
    
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
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIProductsSkuMediaApi::catalogProductAttributeMediaGalleryManagementV1GetListGetCallback);
    connect(this, &OAIProductsSkuMediaApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIProductsSkuMediaApi::catalogProductAttributeMediaGalleryManagementV1GetListGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAICatalog_data_product_attribute_media_gallery_entry_interface> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAICatalog_data_product_attribute_media_gallery_entry_interface val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1GetListGetSignal(output);
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1GetListGetSignalFull(worker, output);
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

        Q_EMIT catalogProductAttributeMediaGalleryManagementV1GetListGetSignalE(output, error_type, error_str);
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1GetListGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT catalogProductAttributeMediaGalleryManagementV1GetListGetSignalError(output, error_type, error_str);
        Q_EMIT catalogProductAttributeMediaGalleryManagementV1GetListGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIProductsSkuMediaApi::tokenAvailable(){

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
