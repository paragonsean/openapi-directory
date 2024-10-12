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

#include "OAIGetSKUseller_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetSKUseller_200_response::OAIGetSKUseller_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetSKUseller_200_response::OAIGetSKUseller_200_response() {
    this->initializeModel();
}

OAIGetSKUseller_200_response::~OAIGetSKUseller_200_response() {}

void OAIGetSKUseller_200_response::initializeModel() {

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_persisted_isSet = false;
    m_is_persisted_isValid = false;

    m_is_removed_isSet = false;
    m_is_removed_isValid = false;

    m_requested_update_date_isSet = false;
    m_requested_update_date_isValid = false;

    m_seller_id_isSet = false;
    m_seller_id_isValid = false;

    m_seller_stock_keeping_unit_id_isSet = false;
    m_seller_stock_keeping_unit_id_isValid = false;

    m_sku_seller_id_isSet = false;
    m_sku_seller_id_isValid = false;

    m_stock_keeping_unit_id_isSet = false;
    m_stock_keeping_unit_id_isValid = false;

    m_update_date_isSet = false;
    m_update_date_isValid = false;
}

void OAIGetSKUseller_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetSKUseller_200_response::fromJsonObject(QJsonObject json) {

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_persisted_isValid = ::OpenAPI::fromJsonValue(m_is_persisted, json[QString("IsPersisted")]);
    m_is_persisted_isSet = !json[QString("IsPersisted")].isNull() && m_is_persisted_isValid;

    m_is_removed_isValid = ::OpenAPI::fromJsonValue(m_is_removed, json[QString("IsRemoved")]);
    m_is_removed_isSet = !json[QString("IsRemoved")].isNull() && m_is_removed_isValid;

    m_requested_update_date_isValid = ::OpenAPI::fromJsonValue(m_requested_update_date, json[QString("RequestedUpdateDate")]);
    m_requested_update_date_isSet = !json[QString("RequestedUpdateDate")].isNull() && m_requested_update_date_isValid;

    m_seller_id_isValid = ::OpenAPI::fromJsonValue(m_seller_id, json[QString("SellerId")]);
    m_seller_id_isSet = !json[QString("SellerId")].isNull() && m_seller_id_isValid;

    m_seller_stock_keeping_unit_id_isValid = ::OpenAPI::fromJsonValue(m_seller_stock_keeping_unit_id, json[QString("SellerStockKeepingUnitId")]);
    m_seller_stock_keeping_unit_id_isSet = !json[QString("SellerStockKeepingUnitId")].isNull() && m_seller_stock_keeping_unit_id_isValid;

    m_sku_seller_id_isValid = ::OpenAPI::fromJsonValue(m_sku_seller_id, json[QString("SkuSellerId")]);
    m_sku_seller_id_isSet = !json[QString("SkuSellerId")].isNull() && m_sku_seller_id_isValid;

    m_stock_keeping_unit_id_isValid = ::OpenAPI::fromJsonValue(m_stock_keeping_unit_id, json[QString("StockKeepingUnitId")]);
    m_stock_keeping_unit_id_isSet = !json[QString("StockKeepingUnitId")].isNull() && m_stock_keeping_unit_id_isValid;

    m_update_date_isValid = ::OpenAPI::fromJsonValue(m_update_date, json[QString("UpdateDate")]);
    m_update_date_isSet = !json[QString("UpdateDate")].isNull() && m_update_date_isValid;
}

QString OAIGetSKUseller_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetSKUseller_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_persisted_isSet) {
        obj.insert(QString("IsPersisted"), ::OpenAPI::toJsonValue(m_is_persisted));
    }
    if (m_is_removed_isSet) {
        obj.insert(QString("IsRemoved"), ::OpenAPI::toJsonValue(m_is_removed));
    }
    if (m_requested_update_date_isSet) {
        obj.insert(QString("RequestedUpdateDate"), ::OpenAPI::toJsonValue(m_requested_update_date));
    }
    if (m_seller_id_isSet) {
        obj.insert(QString("SellerId"), ::OpenAPI::toJsonValue(m_seller_id));
    }
    if (m_seller_stock_keeping_unit_id_isSet) {
        obj.insert(QString("SellerStockKeepingUnitId"), ::OpenAPI::toJsonValue(m_seller_stock_keeping_unit_id));
    }
    if (m_sku_seller_id_isSet) {
        obj.insert(QString("SkuSellerId"), ::OpenAPI::toJsonValue(m_sku_seller_id));
    }
    if (m_stock_keeping_unit_id_isSet) {
        obj.insert(QString("StockKeepingUnitId"), ::OpenAPI::toJsonValue(m_stock_keeping_unit_id));
    }
    if (m_update_date_isSet) {
        obj.insert(QString("UpdateDate"), ::OpenAPI::toJsonValue(m_update_date));
    }
    return obj;
}

bool OAIGetSKUseller_200_response::isIsActive() const {
    return m_is_active;
}
void OAIGetSKUseller_200_response::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIGetSKUseller_200_response::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIGetSKUseller_200_response::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAIGetSKUseller_200_response::isIsPersisted() const {
    return m_is_persisted;
}
void OAIGetSKUseller_200_response::setIsPersisted(const bool &is_persisted) {
    m_is_persisted = is_persisted;
    m_is_persisted_isSet = true;
}

bool OAIGetSKUseller_200_response::is_is_persisted_Set() const{
    return m_is_persisted_isSet;
}

bool OAIGetSKUseller_200_response::is_is_persisted_Valid() const{
    return m_is_persisted_isValid;
}

bool OAIGetSKUseller_200_response::isIsRemoved() const {
    return m_is_removed;
}
void OAIGetSKUseller_200_response::setIsRemoved(const bool &is_removed) {
    m_is_removed = is_removed;
    m_is_removed_isSet = true;
}

bool OAIGetSKUseller_200_response::is_is_removed_Set() const{
    return m_is_removed_isSet;
}

bool OAIGetSKUseller_200_response::is_is_removed_Valid() const{
    return m_is_removed_isValid;
}

QString OAIGetSKUseller_200_response::getRequestedUpdateDate() const {
    return m_requested_update_date;
}
void OAIGetSKUseller_200_response::setRequestedUpdateDate(const QString &requested_update_date) {
    m_requested_update_date = requested_update_date;
    m_requested_update_date_isSet = true;
}

bool OAIGetSKUseller_200_response::is_requested_update_date_Set() const{
    return m_requested_update_date_isSet;
}

bool OAIGetSKUseller_200_response::is_requested_update_date_Valid() const{
    return m_requested_update_date_isValid;
}

QString OAIGetSKUseller_200_response::getSellerId() const {
    return m_seller_id;
}
void OAIGetSKUseller_200_response::setSellerId(const QString &seller_id) {
    m_seller_id = seller_id;
    m_seller_id_isSet = true;
}

bool OAIGetSKUseller_200_response::is_seller_id_Set() const{
    return m_seller_id_isSet;
}

bool OAIGetSKUseller_200_response::is_seller_id_Valid() const{
    return m_seller_id_isValid;
}

QString OAIGetSKUseller_200_response::getSellerStockKeepingUnitId() const {
    return m_seller_stock_keeping_unit_id;
}
void OAIGetSKUseller_200_response::setSellerStockKeepingUnitId(const QString &seller_stock_keeping_unit_id) {
    m_seller_stock_keeping_unit_id = seller_stock_keeping_unit_id;
    m_seller_stock_keeping_unit_id_isSet = true;
}

bool OAIGetSKUseller_200_response::is_seller_stock_keeping_unit_id_Set() const{
    return m_seller_stock_keeping_unit_id_isSet;
}

bool OAIGetSKUseller_200_response::is_seller_stock_keeping_unit_id_Valid() const{
    return m_seller_stock_keeping_unit_id_isValid;
}

qint32 OAIGetSKUseller_200_response::getSkuSellerId() const {
    return m_sku_seller_id;
}
void OAIGetSKUseller_200_response::setSkuSellerId(const qint32 &sku_seller_id) {
    m_sku_seller_id = sku_seller_id;
    m_sku_seller_id_isSet = true;
}

bool OAIGetSKUseller_200_response::is_sku_seller_id_Set() const{
    return m_sku_seller_id_isSet;
}

bool OAIGetSKUseller_200_response::is_sku_seller_id_Valid() const{
    return m_sku_seller_id_isValid;
}

qint32 OAIGetSKUseller_200_response::getStockKeepingUnitId() const {
    return m_stock_keeping_unit_id;
}
void OAIGetSKUseller_200_response::setStockKeepingUnitId(const qint32 &stock_keeping_unit_id) {
    m_stock_keeping_unit_id = stock_keeping_unit_id;
    m_stock_keeping_unit_id_isSet = true;
}

bool OAIGetSKUseller_200_response::is_stock_keeping_unit_id_Set() const{
    return m_stock_keeping_unit_id_isSet;
}

bool OAIGetSKUseller_200_response::is_stock_keeping_unit_id_Valid() const{
    return m_stock_keeping_unit_id_isValid;
}

QString OAIGetSKUseller_200_response::getUpdateDate() const {
    return m_update_date;
}
void OAIGetSKUseller_200_response::setUpdateDate(const QString &update_date) {
    m_update_date = update_date;
    m_update_date_isSet = true;
}

bool OAIGetSKUseller_200_response::is_update_date_Set() const{
    return m_update_date_isSet;
}

bool OAIGetSKUseller_200_response::is_update_date_Valid() const{
    return m_update_date_isValid;
}

bool OAIGetSKUseller_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_persisted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_removed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requested_update_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_stock_keeping_unit_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_seller_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stock_keeping_unit_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetSKUseller_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_is_active_isValid && m_is_persisted_isValid && m_is_removed_isValid && m_requested_update_date_isValid && m_seller_id_isValid && m_seller_stock_keeping_unit_id_isValid && m_sku_seller_id_isValid && m_stock_keeping_unit_id_isValid && m_update_date_isValid && true;
}

} // namespace OpenAPI
