/**
 * Catalog API
 *   > Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.    Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.      ## Index    - [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).  - [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).  - [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).  - [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.  - [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).  - [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.  - [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).  - [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).  - [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.  - [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.  - [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.  - [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).  - [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).  - [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).  - [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).  - [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).  - [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).  - [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).  - [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).  - [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).  - [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items.   - [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value.   - [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.  - [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.  - [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.  - [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.  - [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.  - [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).  - [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.  - [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.      ## Common parameters    | Parameter name              | Description                                                                             |  |---------------------------|-----------------------------------------------------------------------------------------|  | `{{accountName}}`         | Store account name                                                                      |  | `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |  | `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |  | `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILegacySubcollectionApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAILegacySubcollectionApi::OAILegacySubcollectionApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAILegacySubcollectionApi::~OAILegacySubcollectionApi() {
}

void OAILegacySubcollectionApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://vtex.local"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://{accountName}.{environment}.com.br"),
    "VTEX server url",
    QMap<QString, OAIServerVariable>{ 
    {"accountName", OAIServerVariable("Name of the VTEX account. Used as part of the URL.","{accountName}",
    QSet<QString>{ {"{accountName}"} })},
    
    {"environment", OAIServerVariable("Environment to use. Used as part of the URL.","{environment}",
    QSet<QString>{ {"{environment}"} })}, }));
    
    _serverConfigs.insert("apiCatalogPvtCollectionCollectionIdPositionPost", defaultConf);
    _serverIndices.insert("apiCatalogPvtCollectionCollectionIdPositionPost", 0);
    _serverConfigs.insert("apiCatalogPvtCollectionCollectionIdSubcollectionGet", defaultConf);
    _serverIndices.insert("apiCatalogPvtCollectionCollectionIdSubcollectionGet", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionPost", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionPost", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdBrandPost", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdBrandPost", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdCategoryPost", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdCategoryPost", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdDelete", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdDelete", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdGet", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdGet", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdPut", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdPut", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost", 0);
    _serverConfigs.insert("apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete", defaultConf);
    _serverIndices.insert("apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAILegacySubcollectionApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAILegacySubcollectionApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAILegacySubcollectionApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAILegacySubcollectionApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAILegacySubcollectionApi::setUsername(const QString &username) {
    _username = username;
}

void OAILegacySubcollectionApi::setPassword(const QString &password) {
    _password = password;
}


void OAILegacySubcollectionApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAILegacySubcollectionApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAILegacySubcollectionApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAILegacySubcollectionApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAILegacySubcollectionApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAILegacySubcollectionApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAILegacySubcollectionApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAILegacySubcollectionApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAILegacySubcollectionApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAILegacySubcollectionApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAILegacySubcollectionApi::getParamStylePrefix(const QString &style) {
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

QString OAILegacySubcollectionApi::getParamStyleSuffix(const QString &style) {
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

QString OAILegacySubcollectionApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAILegacySubcollectionApi::apiCatalogPvtCollectionCollectionIdPositionPost(const QString &content_type, const QString &accept, const qint32 &collection_id, const ::OpenAPI::OptionalParam<OAI_api_catalog_pvt_collection__collectionId__position_post_request> &oai_api_catalog_pvt_collection__collection_id__position_post_request) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtCollectionCollectionIdPositionPost"][_serverIndices.value("apiCatalogPvtCollectionCollectionIdPositionPost")].URL()+"/api/catalog/pvt/collection/{collectionId}/position");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString collection_idPathParam("{");
        collection_idPathParam.append("collectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "collectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"collectionId"+pathSuffix : pathPrefix;
        fullPath.replace(collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_api_catalog_pvt_collection__collection_id__position_post_request.hasValue()){

        
        QByteArray output = oai_api_catalog_pvt_collection__collection_id__position_post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtCollectionCollectionIdPositionPostCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtCollectionCollectionIdPositionPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtCollectionCollectionIdPositionPostSignal();
        Q_EMIT apiCatalogPvtCollectionCollectionIdPositionPostSignalFull(worker);
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

        Q_EMIT apiCatalogPvtCollectionCollectionIdPositionPostSignalE(error_type, error_str);
        Q_EMIT apiCatalogPvtCollectionCollectionIdPositionPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtCollectionCollectionIdPositionPostSignalError(error_type, error_str);
        Q_EMIT apiCatalogPvtCollectionCollectionIdPositionPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtCollectionCollectionIdSubcollectionGet(const QString &content_type, const QString &accept, const qint32 &collection_id) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtCollectionCollectionIdSubcollectionGet"][_serverIndices.value("apiCatalogPvtCollectionCollectionIdSubcollectionGet")].URL()+"/api/catalog/pvt/collection/{collectionId}/subcollection");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString collection_idPathParam("{");
        collection_idPathParam.append("collectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "collectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"collectionId"+pathSuffix : pathPrefix;
        fullPath.replace(collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtCollectionCollectionIdSubcollectionGetCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtCollectionCollectionIdSubcollectionGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QList<OAI_api_catalog_pvt_collection__collectionId__subcollection_get_200_response_inner> output;
    QString json(worker->response);
    QByteArray array(json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonArray jsonArray = doc.array();
    for (QJsonValue obj : jsonArray) {
        OAI_api_catalog_pvt_collection__collectionId__subcollection_get_200_response_inner val;
        ::OpenAPI::fromJsonValue(val, obj);
        output.append(val);
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtCollectionCollectionIdSubcollectionGetSignal(output);
        Q_EMIT apiCatalogPvtCollectionCollectionIdSubcollectionGetSignalFull(worker, output);
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

        Q_EMIT apiCatalogPvtCollectionCollectionIdSubcollectionGetSignalE(output, error_type, error_str);
        Q_EMIT apiCatalogPvtCollectionCollectionIdSubcollectionGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtCollectionCollectionIdSubcollectionGetSignalError(output, error_type, error_str);
        Q_EMIT apiCatalogPvtCollectionCollectionIdSubcollectionGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionPost(const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<OAI_api_catalog_pvt_subcollection_post_request> &oai_api_catalog_pvt_subcollection_post_request) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionPost"][_serverIndices.value("apiCatalogPvtSubcollectionPost")].URL()+"/api/catalog/pvt/subcollection");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_api_catalog_pvt_subcollection_post_request.hasValue()){

        
        QByteArray output = oai_api_catalog_pvt_subcollection_post_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionPostCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_catalog_pvt_subcollection_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionPostSignal(output);
        Q_EMIT apiCatalogPvtSubcollectionPostSignalFull(worker, output);
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

        Q_EMIT apiCatalogPvtSubcollectionPostSignalE(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionPostSignalError(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(const QString &content_type, const QString &accept, const qint32 &sub_collection_id, const qint32 &brand_id) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}/brand/{brandId}");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    
    {
        QString brand_idPathParam("{");
        brand_idPathParam.append("brandId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "brandId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"brandId"+pathSuffix : pathPrefix;
        fullPath.replace(brand_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(brand_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteSignal();
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteSignalFull(worker);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteSignalE(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteSignalError(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(const QString &content_type, const QString &accept, const qint32 &sub_collection_id, const qint32 &category_id) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}/brand/{categoryId}");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    
    {
        QString category_idPathParam("{");
        category_idPathParam.append("categoryId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "categoryId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"categoryId"+pathSuffix : pathPrefix;
        fullPath.replace(category_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(category_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteSignal();
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteSignalFull(worker);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteSignalE(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteSignalError(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandPost(const QString &content_type, const QString &accept, const qint32 &sub_collection_id, const ::OpenAPI::OptionalParam<OAIRequest_body_10> &oai_request_body_10) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdBrandPost"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdBrandPost")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}/brand");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_request_body_10.hasValue()){

        
        QByteArray output = oai_request_body_10.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandPostCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdBrandPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_catalog_pvt_subcollection__subCollectionId__brand_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandPostSignal(output);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandPostSignalFull(worker, output);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandPostSignalE(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandPostSignalError(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdBrandPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(const QString &content_type, const QString &accept, const qint32 &sub_collection_id, const ::OpenAPI::OptionalParam<OAIRequest_body_11> &oai_request_body_11) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdCategoryPost"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdCategoryPost")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}/category");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_request_body_11.hasValue()){

        
        QByteArray output = oai_request_body_11.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdCategoryPostCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdCategoryPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_catalog_pvt_subcollection__subCollectionId__category_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdCategoryPostSignal(output);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdCategoryPostSignalFull(worker, output);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdCategoryPostSignalE(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdCategoryPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdCategoryPostSignalError(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdCategoryPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdDelete(const QString &content_type, const QString &accept, const qint32 &sub_collection_id) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdDelete"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdDelete")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdDeleteCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdDeleteSignal();
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdDeleteSignalFull(worker);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdDeleteSignalE(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdDeleteSignalError(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdGet(const QString &content_type, const QString &accept, const qint32 &sub_collection_id) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdGet"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdGet")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdGetCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdGetCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_catalog_pvt_subcollection_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdGetSignal(output);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdGetSignalFull(worker, output);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdGetSignalE(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdGetSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdGetSignalError(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdGetSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdPut(const QString &content_type, const QString &accept, const qint32 &sub_collection_id, const ::OpenAPI::OptionalParam<OAI_api_catalog_pvt_subcollection__subCollectionId__put_request> &oai_api_catalog_pvt_subcollection__sub_collection_id__put_request) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdPut"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdPut")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    if (oai_api_catalog_pvt_subcollection__sub_collection_id__put_request.hasValue()){

        
        QByteArray output = oai_api_catalog_pvt_subcollection__sub_collection_id__put_request.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdPutCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdPutCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_catalog_pvt_subcollection_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdPutSignal(output);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdPutSignalFull(worker, output);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdPutSignalE(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdPutSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdPutSignalError(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdPutSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(const QString &content_type, const QString &accept, const qint32 &sub_collection_id, const ::OpenAPI::OptionalParam<OAIRequest_body_12> &oai_request_body_12) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_request_body_12.hasValue()){

        
        QByteArray output = oai_request_body_12.value().asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAI_api_catalog_pvt_subcollection__subCollectionId__stockkeepingunit_post_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostSignal(output);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostSignalFull(worker, output);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostSignalE(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostSignalError(output, error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPostSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(const QString &content_type, const QString &accept, const qint32 &sub_collection_id, const qint32 &sku_id) {
    QString fullPath = QString(_serverConfigs["apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete"][_serverIndices.value("apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete")].URL()+"/api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit/{skuId}");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
    {
        QString sub_collection_idPathParam("{");
        sub_collection_idPathParam.append("subCollectionId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "subCollectionId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"subCollectionId"+pathSuffix : pathPrefix;
        fullPath.replace(sub_collection_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sub_collection_id)));
    }
    
    {
        QString sku_idPathParam("{");
        sku_idPathParam.append("skuId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "skuId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"skuId"+pathSuffix : pathPrefix;
        fullPath.replace(sku_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(sku_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteCallback);
    connect(this, &OAILegacySubcollectionApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAILegacySubcollectionApi::apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteSignal();
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteSignalFull(worker);
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

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteSignalE(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteSignalError(error_type, error_str);
        Q_EMIT apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDeleteSignalErrorFull(worker, error_type, error_str);
    }
}

void OAILegacySubcollectionApi::tokenAvailable(){

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
