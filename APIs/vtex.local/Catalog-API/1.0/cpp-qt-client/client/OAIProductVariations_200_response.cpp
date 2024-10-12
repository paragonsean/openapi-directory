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

#include "OAIProductVariations_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductVariations_200_response::OAIProductVariations_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductVariations_200_response::OAIProductVariations_200_response() {
    this->initializeModel();
}

OAIProductVariations_200_response::~OAIProductVariations_200_response() {}

void OAIProductVariations_200_response::initializeModel() {

    m_available_isSet = false;
    m_available_isValid = false;

    m_dimensions_isSet = false;
    m_dimensions_isValid = false;

    m_dimensions_input_type_isSet = false;
    m_dimensions_input_type_isValid = false;

    m_dimensions_map_isSet = false;
    m_dimensions_map_isValid = false;

    m_display_mode_isSet = false;
    m_display_mode_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_sales_channel_isSet = false;
    m_sales_channel_isValid = false;

    m_skus_isSet = false;
    m_skus_isValid = false;
}

void OAIProductVariations_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductVariations_200_response::fromJsonObject(QJsonObject json) {

    m_available_isValid = ::OpenAPI::fromJsonValue(m_available, json[QString("available")]);
    m_available_isSet = !json[QString("available")].isNull() && m_available_isValid;

    m_dimensions_isValid = ::OpenAPI::fromJsonValue(m_dimensions, json[QString("dimensions")]);
    m_dimensions_isSet = !json[QString("dimensions")].isNull() && m_dimensions_isValid;

    m_dimensions_input_type_isValid = ::OpenAPI::fromJsonValue(m_dimensions_input_type, json[QString("dimensionsInputType")]);
    m_dimensions_input_type_isSet = !json[QString("dimensionsInputType")].isNull() && m_dimensions_input_type_isValid;

    if(json["dimensionsMap"].isObject()){
        auto varmap = json["dimensionsMap"].toObject().toVariantMap();
        m_dimensions_map_isValid = true;
        if(varmap.count() > 0){
            for(auto val : varmap.keys()){
                QList<QJsonValue> item;
                auto jval = QJsonValue::fromVariant(varmap.value(val));
                m_dimensions_map_isValid &= ::OpenAPI::fromJsonValue(item, jval);
                m_dimensions_map_isSet &= !jval.isNull() && m_dimensions_map_isValid;
                m_dimensions_map.insert(m_dimensions_map.end(), val, item);
            }
        }
    }

    m_display_mode_isValid = ::OpenAPI::fromJsonValue(m_display_mode, json[QString("displayMode")]);
    m_display_mode_isSet = !json[QString("displayMode")].isNull() && m_display_mode_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("productId")]);
    m_product_id_isSet = !json[QString("productId")].isNull() && m_product_id_isValid;

    m_sales_channel_isValid = ::OpenAPI::fromJsonValue(m_sales_channel, json[QString("salesChannel")]);
    m_sales_channel_isSet = !json[QString("salesChannel")].isNull() && m_sales_channel_isValid;

    m_skus_isValid = ::OpenAPI::fromJsonValue(m_skus, json[QString("skus")]);
    m_skus_isSet = !json[QString("skus")].isNull() && m_skus_isValid;
}

QString OAIProductVariations_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductVariations_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_available_isSet) {
        obj.insert(QString("available"), ::OpenAPI::toJsonValue(m_available));
    }
    if (m_dimensions.size() > 0) {
        obj.insert(QString("dimensions"), ::OpenAPI::toJsonValue(m_dimensions));
    }
    if (m_dimensions_input_type.size() > 0) {
        obj.insert(QString("dimensionsInputType"), ::OpenAPI::toJsonValue(m_dimensions_input_type));
    }
    if (m_dimensions_map.size() > 0) {
        
        obj.insert(QString("dimensionsMap"), toJsonValue(m_dimensions_map));
    }
    if (m_display_mode_isSet) {
        obj.insert(QString("displayMode"), ::OpenAPI::toJsonValue(m_display_mode));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("productId"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_sales_channel_isSet) {
        obj.insert(QString("salesChannel"), ::OpenAPI::toJsonValue(m_sales_channel));
    }
    if (m_skus.size() > 0) {
        obj.insert(QString("skus"), ::OpenAPI::toJsonValue(m_skus));
    }
    return obj;
}

bool OAIProductVariations_200_response::isAvailable() const {
    return m_available;
}
void OAIProductVariations_200_response::setAvailable(const bool &available) {
    m_available = available;
    m_available_isSet = true;
}

bool OAIProductVariations_200_response::is_available_Set() const{
    return m_available_isSet;
}

bool OAIProductVariations_200_response::is_available_Valid() const{
    return m_available_isValid;
}

QList<QString> OAIProductVariations_200_response::getDimensions() const {
    return m_dimensions;
}
void OAIProductVariations_200_response::setDimensions(const QList<QString> &dimensions) {
    m_dimensions = dimensions;
    m_dimensions_isSet = true;
}

bool OAIProductVariations_200_response::is_dimensions_Set() const{
    return m_dimensions_isSet;
}

bool OAIProductVariations_200_response::is_dimensions_Valid() const{
    return m_dimensions_isValid;
}

QMap<QString, QString> OAIProductVariations_200_response::getDimensionsInputType() const {
    return m_dimensions_input_type;
}
void OAIProductVariations_200_response::setDimensionsInputType(const QMap<QString, QString> &dimensions_input_type) {
    m_dimensions_input_type = dimensions_input_type;
    m_dimensions_input_type_isSet = true;
}

bool OAIProductVariations_200_response::is_dimensions_input_type_Set() const{
    return m_dimensions_input_type_isSet;
}

bool OAIProductVariations_200_response::is_dimensions_input_type_Valid() const{
    return m_dimensions_input_type_isValid;
}

QMap<QString, QList<QJsonValue>> OAIProductVariations_200_response::getDimensionsMap() const {
    return m_dimensions_map;
}
void OAIProductVariations_200_response::setDimensionsMap(const QMap<QString, QList<QJsonValue>> &dimensions_map) {
    m_dimensions_map = dimensions_map;
    m_dimensions_map_isSet = true;
}

bool OAIProductVariations_200_response::is_dimensions_map_Set() const{
    return m_dimensions_map_isSet;
}

bool OAIProductVariations_200_response::is_dimensions_map_Valid() const{
    return m_dimensions_map_isValid;
}

QString OAIProductVariations_200_response::getDisplayMode() const {
    return m_display_mode;
}
void OAIProductVariations_200_response::setDisplayMode(const QString &display_mode) {
    m_display_mode = display_mode;
    m_display_mode_isSet = true;
}

bool OAIProductVariations_200_response::is_display_mode_Set() const{
    return m_display_mode_isSet;
}

bool OAIProductVariations_200_response::is_display_mode_Valid() const{
    return m_display_mode_isValid;
}

QString OAIProductVariations_200_response::getName() const {
    return m_name;
}
void OAIProductVariations_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProductVariations_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProductVariations_200_response::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIProductVariations_200_response::getProductId() const {
    return m_product_id;
}
void OAIProductVariations_200_response::setProductId(const qint32 &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIProductVariations_200_response::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIProductVariations_200_response::is_product_id_Valid() const{
    return m_product_id_isValid;
}

QString OAIProductVariations_200_response::getSalesChannel() const {
    return m_sales_channel;
}
void OAIProductVariations_200_response::setSalesChannel(const QString &sales_channel) {
    m_sales_channel = sales_channel;
    m_sales_channel_isSet = true;
}

bool OAIProductVariations_200_response::is_sales_channel_Set() const{
    return m_sales_channel_isSet;
}

bool OAIProductVariations_200_response::is_sales_channel_Valid() const{
    return m_sales_channel_isValid;
}

QList<OAIProductVariations_200_response_skus_inner> OAIProductVariations_200_response::getSkus() const {
    return m_skus;
}
void OAIProductVariations_200_response::setSkus(const QList<OAIProductVariations_200_response_skus_inner> &skus) {
    m_skus = skus;
    m_skus_isSet = true;
}

bool OAIProductVariations_200_response::is_skus_Set() const{
    return m_skus_isSet;
}

bool OAIProductVariations_200_response::is_skus_Valid() const{
    return m_skus_isValid;
}

bool OAIProductVariations_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dimensions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dimensions_input_type.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dimensions_map.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_channel_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_skus.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductVariations_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
