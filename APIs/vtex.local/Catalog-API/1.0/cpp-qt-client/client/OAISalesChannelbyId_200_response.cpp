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

#include "OAISalesChannelbyId_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISalesChannelbyId_200_response::OAISalesChannelbyId_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISalesChannelbyId_200_response::OAISalesChannelbyId_200_response() {
    this->initializeModel();
}

OAISalesChannelbyId_200_response::~OAISalesChannelbyId_200_response() {}

void OAISalesChannelbyId_200_response::initializeModel() {

    m_condition_rule_isSet = false;
    m_condition_rule_isValid = false;

    m_country_code_isSet = false;
    m_country_code_isValid = false;

    m_culture_info_isSet = false;
    m_culture_info_isValid = false;

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_currency_decimal_digits_isSet = false;
    m_currency_decimal_digits_isValid = false;

    m_currency_format_info_isSet = false;
    m_currency_format_info_isValid = false;

    m_currency_locale_isSet = false;
    m_currency_locale_isValid = false;

    m_currency_symbol_isSet = false;
    m_currency_symbol_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_origin_isSet = false;
    m_origin_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_product_cluster_id_isSet = false;
    m_product_cluster_id_isValid = false;

    m_time_zone_isSet = false;
    m_time_zone_isValid = false;
}

void OAISalesChannelbyId_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISalesChannelbyId_200_response::fromJsonObject(QJsonObject json) {

    m_condition_rule_isValid = ::OpenAPI::fromJsonValue(m_condition_rule, json[QString("ConditionRule")]);
    m_condition_rule_isSet = !json[QString("ConditionRule")].isNull() && m_condition_rule_isValid;

    m_country_code_isValid = ::OpenAPI::fromJsonValue(m_country_code, json[QString("CountryCode")]);
    m_country_code_isSet = !json[QString("CountryCode")].isNull() && m_country_code_isValid;

    m_culture_info_isValid = ::OpenAPI::fromJsonValue(m_culture_info, json[QString("CultureInfo")]);
    m_culture_info_isSet = !json[QString("CultureInfo")].isNull() && m_culture_info_isValid;

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("CurrencyCode")]);
    m_currency_code_isSet = !json[QString("CurrencyCode")].isNull() && m_currency_code_isValid;

    m_currency_decimal_digits_isValid = ::OpenAPI::fromJsonValue(m_currency_decimal_digits, json[QString("CurrencyDecimalDigits")]);
    m_currency_decimal_digits_isSet = !json[QString("CurrencyDecimalDigits")].isNull() && m_currency_decimal_digits_isValid;

    m_currency_format_info_isValid = ::OpenAPI::fromJsonValue(m_currency_format_info, json[QString("CurrencyFormatInfo")]);
    m_currency_format_info_isSet = !json[QString("CurrencyFormatInfo")].isNull() && m_currency_format_info_isValid;

    m_currency_locale_isValid = ::OpenAPI::fromJsonValue(m_currency_locale, json[QString("CurrencyLocale")]);
    m_currency_locale_isSet = !json[QString("CurrencyLocale")].isNull() && m_currency_locale_isValid;

    m_currency_symbol_isValid = ::OpenAPI::fromJsonValue(m_currency_symbol, json[QString("CurrencySymbol")]);
    m_currency_symbol_isSet = !json[QString("CurrencySymbol")].isNull() && m_currency_symbol_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_origin_isValid = ::OpenAPI::fromJsonValue(m_origin, json[QString("Origin")]);
    m_origin_isSet = !json[QString("Origin")].isNull() && m_origin_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("Position")]);
    m_position_isSet = !json[QString("Position")].isNull() && m_position_isValid;

    m_product_cluster_id_isValid = ::OpenAPI::fromJsonValue(m_product_cluster_id, json[QString("ProductClusterId")]);
    m_product_cluster_id_isSet = !json[QString("ProductClusterId")].isNull() && m_product_cluster_id_isValid;

    m_time_zone_isValid = ::OpenAPI::fromJsonValue(m_time_zone, json[QString("TimeZone")]);
    m_time_zone_isSet = !json[QString("TimeZone")].isNull() && m_time_zone_isValid;
}

QString OAISalesChannelbyId_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISalesChannelbyId_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_condition_rule_isSet) {
        obj.insert(QString("ConditionRule"), ::OpenAPI::toJsonValue(m_condition_rule));
    }
    if (m_country_code_isSet) {
        obj.insert(QString("CountryCode"), ::OpenAPI::toJsonValue(m_country_code));
    }
    if (m_culture_info_isSet) {
        obj.insert(QString("CultureInfo"), ::OpenAPI::toJsonValue(m_culture_info));
    }
    if (m_currency_code_isSet) {
        obj.insert(QString("CurrencyCode"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_currency_decimal_digits_isSet) {
        obj.insert(QString("CurrencyDecimalDigits"), ::OpenAPI::toJsonValue(m_currency_decimal_digits));
    }
    if (m_currency_format_info.isSet()) {
        obj.insert(QString("CurrencyFormatInfo"), ::OpenAPI::toJsonValue(m_currency_format_info));
    }
    if (m_currency_locale_isSet) {
        obj.insert(QString("CurrencyLocale"), ::OpenAPI::toJsonValue(m_currency_locale));
    }
    if (m_currency_symbol_isSet) {
        obj.insert(QString("CurrencySymbol"), ::OpenAPI::toJsonValue(m_currency_symbol));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_origin_isSet) {
        obj.insert(QString("Origin"), ::OpenAPI::toJsonValue(m_origin));
    }
    if (m_position_isSet) {
        obj.insert(QString("Position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_product_cluster_id_isSet) {
        obj.insert(QString("ProductClusterId"), ::OpenAPI::toJsonValue(m_product_cluster_id));
    }
    if (m_time_zone_isSet) {
        obj.insert(QString("TimeZone"), ::OpenAPI::toJsonValue(m_time_zone));
    }
    return obj;
}

QString OAISalesChannelbyId_200_response::getConditionRule() const {
    return m_condition_rule;
}
void OAISalesChannelbyId_200_response::setConditionRule(const QString &condition_rule) {
    m_condition_rule = condition_rule;
    m_condition_rule_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_condition_rule_Set() const{
    return m_condition_rule_isSet;
}

bool OAISalesChannelbyId_200_response::is_condition_rule_Valid() const{
    return m_condition_rule_isValid;
}

QString OAISalesChannelbyId_200_response::getCountryCode() const {
    return m_country_code;
}
void OAISalesChannelbyId_200_response::setCountryCode(const QString &country_code) {
    m_country_code = country_code;
    m_country_code_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_country_code_Set() const{
    return m_country_code_isSet;
}

bool OAISalesChannelbyId_200_response::is_country_code_Valid() const{
    return m_country_code_isValid;
}

QString OAISalesChannelbyId_200_response::getCultureInfo() const {
    return m_culture_info;
}
void OAISalesChannelbyId_200_response::setCultureInfo(const QString &culture_info) {
    m_culture_info = culture_info;
    m_culture_info_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_culture_info_Set() const{
    return m_culture_info_isSet;
}

bool OAISalesChannelbyId_200_response::is_culture_info_Valid() const{
    return m_culture_info_isValid;
}

QString OAISalesChannelbyId_200_response::getCurrencyCode() const {
    return m_currency_code;
}
void OAISalesChannelbyId_200_response::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAISalesChannelbyId_200_response::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

qint32 OAISalesChannelbyId_200_response::getCurrencyDecimalDigits() const {
    return m_currency_decimal_digits;
}
void OAISalesChannelbyId_200_response::setCurrencyDecimalDigits(const qint32 &currency_decimal_digits) {
    m_currency_decimal_digits = currency_decimal_digits;
    m_currency_decimal_digits_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_currency_decimal_digits_Set() const{
    return m_currency_decimal_digits_isSet;
}

bool OAISalesChannelbyId_200_response::is_currency_decimal_digits_Valid() const{
    return m_currency_decimal_digits_isValid;
}

OAICurrencyFormatInfo OAISalesChannelbyId_200_response::getCurrencyFormatInfo() const {
    return m_currency_format_info;
}
void OAISalesChannelbyId_200_response::setCurrencyFormatInfo(const OAICurrencyFormatInfo &currency_format_info) {
    m_currency_format_info = currency_format_info;
    m_currency_format_info_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_currency_format_info_Set() const{
    return m_currency_format_info_isSet;
}

bool OAISalesChannelbyId_200_response::is_currency_format_info_Valid() const{
    return m_currency_format_info_isValid;
}

qint32 OAISalesChannelbyId_200_response::getCurrencyLocale() const {
    return m_currency_locale;
}
void OAISalesChannelbyId_200_response::setCurrencyLocale(const qint32 &currency_locale) {
    m_currency_locale = currency_locale;
    m_currency_locale_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_currency_locale_Set() const{
    return m_currency_locale_isSet;
}

bool OAISalesChannelbyId_200_response::is_currency_locale_Valid() const{
    return m_currency_locale_isValid;
}

QString OAISalesChannelbyId_200_response::getCurrencySymbol() const {
    return m_currency_symbol;
}
void OAISalesChannelbyId_200_response::setCurrencySymbol(const QString &currency_symbol) {
    m_currency_symbol = currency_symbol;
    m_currency_symbol_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_currency_symbol_Set() const{
    return m_currency_symbol_isSet;
}

bool OAISalesChannelbyId_200_response::is_currency_symbol_Valid() const{
    return m_currency_symbol_isValid;
}

qint32 OAISalesChannelbyId_200_response::getId() const {
    return m_id;
}
void OAISalesChannelbyId_200_response::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAISalesChannelbyId_200_response::is_id_Valid() const{
    return m_id_isValid;
}

bool OAISalesChannelbyId_200_response::isIsActive() const {
    return m_is_active;
}
void OAISalesChannelbyId_200_response::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAISalesChannelbyId_200_response::is_is_active_Valid() const{
    return m_is_active_isValid;
}

QString OAISalesChannelbyId_200_response::getName() const {
    return m_name;
}
void OAISalesChannelbyId_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAISalesChannelbyId_200_response::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISalesChannelbyId_200_response::getOrigin() const {
    return m_origin;
}
void OAISalesChannelbyId_200_response::setOrigin(const QString &origin) {
    m_origin = origin;
    m_origin_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_origin_Set() const{
    return m_origin_isSet;
}

bool OAISalesChannelbyId_200_response::is_origin_Valid() const{
    return m_origin_isValid;
}

qint32 OAISalesChannelbyId_200_response::getPosition() const {
    return m_position;
}
void OAISalesChannelbyId_200_response::setPosition(const qint32 &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_position_Set() const{
    return m_position_isSet;
}

bool OAISalesChannelbyId_200_response::is_position_Valid() const{
    return m_position_isValid;
}

qint32 OAISalesChannelbyId_200_response::getProductClusterId() const {
    return m_product_cluster_id;
}
void OAISalesChannelbyId_200_response::setProductClusterId(const qint32 &product_cluster_id) {
    m_product_cluster_id = product_cluster_id;
    m_product_cluster_id_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_product_cluster_id_Set() const{
    return m_product_cluster_id_isSet;
}

bool OAISalesChannelbyId_200_response::is_product_cluster_id_Valid() const{
    return m_product_cluster_id_isValid;
}

QString OAISalesChannelbyId_200_response::getTimeZone() const {
    return m_time_zone;
}
void OAISalesChannelbyId_200_response::setTimeZone(const QString &time_zone) {
    m_time_zone = time_zone;
    m_time_zone_isSet = true;
}

bool OAISalesChannelbyId_200_response::is_time_zone_Set() const{
    return m_time_zone_isSet;
}

bool OAISalesChannelbyId_200_response::is_time_zone_Valid() const{
    return m_time_zone_isValid;
}

bool OAISalesChannelbyId_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_condition_rule_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_culture_info_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_decimal_digits_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_format_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_locale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_symbol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_origin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_cluster_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISalesChannelbyId_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
