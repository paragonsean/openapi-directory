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

#include "OAISkuSeller.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISkuSeller::OAISkuSeller(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISkuSeller::OAISkuSeller() {
    this->initializeModel();
}

OAISkuSeller::~OAISkuSeller() {}

void OAISkuSeller::initializeModel() {

    m_freight_commission_percentage_isSet = false;
    m_freight_commission_percentage_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_product_commission_percentage_isSet = false;
    m_product_commission_percentage_isValid = false;

    m_seller_id_isSet = false;
    m_seller_id_isValid = false;

    m_seller_stock_keeping_unit_id_isSet = false;
    m_seller_stock_keeping_unit_id_isValid = false;

    m_stock_keeping_unit_id_isSet = false;
    m_stock_keeping_unit_id_isValid = false;
}

void OAISkuSeller::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISkuSeller::fromJsonObject(QJsonObject json) {

    m_freight_commission_percentage_isValid = ::OpenAPI::fromJsonValue(m_freight_commission_percentage, json[QString("FreightCommissionPercentage")]);
    m_freight_commission_percentage_isSet = !json[QString("FreightCommissionPercentage")].isNull() && m_freight_commission_percentage_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_product_commission_percentage_isValid = ::OpenAPI::fromJsonValue(m_product_commission_percentage, json[QString("ProductCommissionPercentage")]);
    m_product_commission_percentage_isSet = !json[QString("ProductCommissionPercentage")].isNull() && m_product_commission_percentage_isValid;

    m_seller_id_isValid = ::OpenAPI::fromJsonValue(m_seller_id, json[QString("SellerId")]);
    m_seller_id_isSet = !json[QString("SellerId")].isNull() && m_seller_id_isValid;

    m_seller_stock_keeping_unit_id_isValid = ::OpenAPI::fromJsonValue(m_seller_stock_keeping_unit_id, json[QString("SellerStockKeepingUnitId")]);
    m_seller_stock_keeping_unit_id_isSet = !json[QString("SellerStockKeepingUnitId")].isNull() && m_seller_stock_keeping_unit_id_isValid;

    m_stock_keeping_unit_id_isValid = ::OpenAPI::fromJsonValue(m_stock_keeping_unit_id, json[QString("StockKeepingUnitId")]);
    m_stock_keeping_unit_id_isSet = !json[QString("StockKeepingUnitId")].isNull() && m_stock_keeping_unit_id_isValid;
}

QString OAISkuSeller::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISkuSeller::asJsonObject() const {
    QJsonObject obj;
    if (m_freight_commission_percentage_isSet) {
        obj.insert(QString("FreightCommissionPercentage"), ::OpenAPI::toJsonValue(m_freight_commission_percentage));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_product_commission_percentage_isSet) {
        obj.insert(QString("ProductCommissionPercentage"), ::OpenAPI::toJsonValue(m_product_commission_percentage));
    }
    if (m_seller_id_isSet) {
        obj.insert(QString("SellerId"), ::OpenAPI::toJsonValue(m_seller_id));
    }
    if (m_seller_stock_keeping_unit_id_isSet) {
        obj.insert(QString("SellerStockKeepingUnitId"), ::OpenAPI::toJsonValue(m_seller_stock_keeping_unit_id));
    }
    if (m_stock_keeping_unit_id_isSet) {
        obj.insert(QString("StockKeepingUnitId"), ::OpenAPI::toJsonValue(m_stock_keeping_unit_id));
    }
    return obj;
}

double OAISkuSeller::getFreightCommissionPercentage() const {
    return m_freight_commission_percentage;
}
void OAISkuSeller::setFreightCommissionPercentage(const double &freight_commission_percentage) {
    m_freight_commission_percentage = freight_commission_percentage;
    m_freight_commission_percentage_isSet = true;
}

bool OAISkuSeller::is_freight_commission_percentage_Set() const{
    return m_freight_commission_percentage_isSet;
}

bool OAISkuSeller::is_freight_commission_percentage_Valid() const{
    return m_freight_commission_percentage_isValid;
}

bool OAISkuSeller::isIsActive() const {
    return m_is_active;
}
void OAISkuSeller::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAISkuSeller::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAISkuSeller::is_is_active_Valid() const{
    return m_is_active_isValid;
}

double OAISkuSeller::getProductCommissionPercentage() const {
    return m_product_commission_percentage;
}
void OAISkuSeller::setProductCommissionPercentage(const double &product_commission_percentage) {
    m_product_commission_percentage = product_commission_percentage;
    m_product_commission_percentage_isSet = true;
}

bool OAISkuSeller::is_product_commission_percentage_Set() const{
    return m_product_commission_percentage_isSet;
}

bool OAISkuSeller::is_product_commission_percentage_Valid() const{
    return m_product_commission_percentage_isValid;
}

QString OAISkuSeller::getSellerId() const {
    return m_seller_id;
}
void OAISkuSeller::setSellerId(const QString &seller_id) {
    m_seller_id = seller_id;
    m_seller_id_isSet = true;
}

bool OAISkuSeller::is_seller_id_Set() const{
    return m_seller_id_isSet;
}

bool OAISkuSeller::is_seller_id_Valid() const{
    return m_seller_id_isValid;
}

QString OAISkuSeller::getSellerStockKeepingUnitId() const {
    return m_seller_stock_keeping_unit_id;
}
void OAISkuSeller::setSellerStockKeepingUnitId(const QString &seller_stock_keeping_unit_id) {
    m_seller_stock_keeping_unit_id = seller_stock_keeping_unit_id;
    m_seller_stock_keeping_unit_id_isSet = true;
}

bool OAISkuSeller::is_seller_stock_keeping_unit_id_Set() const{
    return m_seller_stock_keeping_unit_id_isSet;
}

bool OAISkuSeller::is_seller_stock_keeping_unit_id_Valid() const{
    return m_seller_stock_keeping_unit_id_isValid;
}

qint32 OAISkuSeller::getStockKeepingUnitId() const {
    return m_stock_keeping_unit_id;
}
void OAISkuSeller::setStockKeepingUnitId(const qint32 &stock_keeping_unit_id) {
    m_stock_keeping_unit_id = stock_keeping_unit_id;
    m_stock_keeping_unit_id_isSet = true;
}

bool OAISkuSeller::is_stock_keeping_unit_id_Set() const{
    return m_stock_keeping_unit_id_isSet;
}

bool OAISkuSeller::is_stock_keeping_unit_id_Valid() const{
    return m_stock_keeping_unit_id_isValid;
}

bool OAISkuSeller::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_freight_commission_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_commission_percentage_isSet) {
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

        if (m_stock_keeping_unit_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISkuSeller::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_freight_commission_percentage_isValid && m_is_active_isValid && m_product_commission_percentage_isValid && m_seller_id_isValid && m_seller_stock_keeping_unit_id_isValid && m_stock_keeping_unit_id_isValid && true;
}

} // namespace OpenAPI
