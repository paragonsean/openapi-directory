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

#include "OAIRequest_body_7.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRequest_body_7::OAIRequest_body_7(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRequest_body_7::OAIRequest_body_7() {
    this->initializeModel();
}

OAIRequest_body_7::~OAIRequest_body_7() {}

void OAIRequest_body_7::initializeModel() {

    m_category_id_isSet = false;
    m_category_id_isValid = false;

    m_default_value_isSet = false;
    m_default_value_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_field_group_id_isSet = false;
    m_field_group_id_isValid = false;

    m_field_type_id_isSet = false;
    m_field_type_id_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_filter_isSet = false;
    m_is_filter_isValid = false;

    m_is_on_product_details_isSet = false;
    m_is_on_product_details_isValid = false;

    m_is_required_isSet = false;
    m_is_required_isValid = false;

    m_is_side_menu_link_active_isSet = false;
    m_is_side_menu_link_active_isValid = false;

    m_is_stock_keeping_unit_isSet = false;
    m_is_stock_keeping_unit_isValid = false;

    m_is_top_menu_link_active_isSet = false;
    m_is_top_menu_link_active_isValid = false;

    m_is_wizard_isSet = false;
    m_is_wizard_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;
}

void OAIRequest_body_7::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRequest_body_7::fromJsonObject(QJsonObject json) {

    m_category_id_isValid = ::OpenAPI::fromJsonValue(m_category_id, json[QString("CategoryId")]);
    m_category_id_isSet = !json[QString("CategoryId")].isNull() && m_category_id_isValid;

    m_default_value_isValid = ::OpenAPI::fromJsonValue(m_default_value, json[QString("DefaultValue")]);
    m_default_value_isSet = !json[QString("DefaultValue")].isNull() && m_default_value_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_field_group_id_isValid = ::OpenAPI::fromJsonValue(m_field_group_id, json[QString("FieldGroupId")]);
    m_field_group_id_isSet = !json[QString("FieldGroupId")].isNull() && m_field_group_id_isValid;

    m_field_type_id_isValid = ::OpenAPI::fromJsonValue(m_field_type_id, json[QString("FieldTypeId")]);
    m_field_type_id_isSet = !json[QString("FieldTypeId")].isNull() && m_field_type_id_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_filter_isValid = ::OpenAPI::fromJsonValue(m_is_filter, json[QString("IsFilter")]);
    m_is_filter_isSet = !json[QString("IsFilter")].isNull() && m_is_filter_isValid;

    m_is_on_product_details_isValid = ::OpenAPI::fromJsonValue(m_is_on_product_details, json[QString("IsOnProductDetails")]);
    m_is_on_product_details_isSet = !json[QString("IsOnProductDetails")].isNull() && m_is_on_product_details_isValid;

    m_is_required_isValid = ::OpenAPI::fromJsonValue(m_is_required, json[QString("IsRequired")]);
    m_is_required_isSet = !json[QString("IsRequired")].isNull() && m_is_required_isValid;

    m_is_side_menu_link_active_isValid = ::OpenAPI::fromJsonValue(m_is_side_menu_link_active, json[QString("IsSideMenuLinkActive")]);
    m_is_side_menu_link_active_isSet = !json[QString("IsSideMenuLinkActive")].isNull() && m_is_side_menu_link_active_isValid;

    m_is_stock_keeping_unit_isValid = ::OpenAPI::fromJsonValue(m_is_stock_keeping_unit, json[QString("IsStockKeepingUnit")]);
    m_is_stock_keeping_unit_isSet = !json[QString("IsStockKeepingUnit")].isNull() && m_is_stock_keeping_unit_isValid;

    m_is_top_menu_link_active_isValid = ::OpenAPI::fromJsonValue(m_is_top_menu_link_active, json[QString("IsTopMenuLinkActive")]);
    m_is_top_menu_link_active_isSet = !json[QString("IsTopMenuLinkActive")].isNull() && m_is_top_menu_link_active_isValid;

    m_is_wizard_isValid = ::OpenAPI::fromJsonValue(m_is_wizard, json[QString("IsWizard")]);
    m_is_wizard_isSet = !json[QString("IsWizard")].isNull() && m_is_wizard_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("Position")]);
    m_position_isSet = !json[QString("Position")].isNull() && m_position_isValid;
}

QString OAIRequest_body_7::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRequest_body_7::asJsonObject() const {
    QJsonObject obj;
    if (m_category_id_isSet) {
        obj.insert(QString("CategoryId"), ::OpenAPI::toJsonValue(m_category_id));
    }
    if (m_default_value_isSet) {
        obj.insert(QString("DefaultValue"), ::OpenAPI::toJsonValue(m_default_value));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_field_group_id_isSet) {
        obj.insert(QString("FieldGroupId"), ::OpenAPI::toJsonValue(m_field_group_id));
    }
    if (m_field_type_id_isSet) {
        obj.insert(QString("FieldTypeId"), ::OpenAPI::toJsonValue(m_field_type_id));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_filter_isSet) {
        obj.insert(QString("IsFilter"), ::OpenAPI::toJsonValue(m_is_filter));
    }
    if (m_is_on_product_details_isSet) {
        obj.insert(QString("IsOnProductDetails"), ::OpenAPI::toJsonValue(m_is_on_product_details));
    }
    if (m_is_required_isSet) {
        obj.insert(QString("IsRequired"), ::OpenAPI::toJsonValue(m_is_required));
    }
    if (m_is_side_menu_link_active_isSet) {
        obj.insert(QString("IsSideMenuLinkActive"), ::OpenAPI::toJsonValue(m_is_side_menu_link_active));
    }
    if (m_is_stock_keeping_unit_isSet) {
        obj.insert(QString("IsStockKeepingUnit"), ::OpenAPI::toJsonValue(m_is_stock_keeping_unit));
    }
    if (m_is_top_menu_link_active_isSet) {
        obj.insert(QString("IsTopMenuLinkActive"), ::OpenAPI::toJsonValue(m_is_top_menu_link_active));
    }
    if (m_is_wizard_isSet) {
        obj.insert(QString("IsWizard"), ::OpenAPI::toJsonValue(m_is_wizard));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_position_isSet) {
        obj.insert(QString("Position"), ::OpenAPI::toJsonValue(m_position));
    }
    return obj;
}

qint32 OAIRequest_body_7::getCategoryId() const {
    return m_category_id;
}
void OAIRequest_body_7::setCategoryId(const qint32 &category_id) {
    m_category_id = category_id;
    m_category_id_isSet = true;
}

bool OAIRequest_body_7::is_category_id_Set() const{
    return m_category_id_isSet;
}

bool OAIRequest_body_7::is_category_id_Valid() const{
    return m_category_id_isValid;
}

QString OAIRequest_body_7::getDefaultValue() const {
    return m_default_value;
}
void OAIRequest_body_7::setDefaultValue(const QString &default_value) {
    m_default_value = default_value;
    m_default_value_isSet = true;
}

bool OAIRequest_body_7::is_default_value_Set() const{
    return m_default_value_isSet;
}

bool OAIRequest_body_7::is_default_value_Valid() const{
    return m_default_value_isValid;
}

QString OAIRequest_body_7::getDescription() const {
    return m_description;
}
void OAIRequest_body_7::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIRequest_body_7::is_description_Set() const{
    return m_description_isSet;
}

bool OAIRequest_body_7::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIRequest_body_7::getFieldGroupId() const {
    return m_field_group_id;
}
void OAIRequest_body_7::setFieldGroupId(const qint32 &field_group_id) {
    m_field_group_id = field_group_id;
    m_field_group_id_isSet = true;
}

bool OAIRequest_body_7::is_field_group_id_Set() const{
    return m_field_group_id_isSet;
}

bool OAIRequest_body_7::is_field_group_id_Valid() const{
    return m_field_group_id_isValid;
}

qint32 OAIRequest_body_7::getFieldTypeId() const {
    return m_field_type_id;
}
void OAIRequest_body_7::setFieldTypeId(const qint32 &field_type_id) {
    m_field_type_id = field_type_id;
    m_field_type_id_isSet = true;
}

bool OAIRequest_body_7::is_field_type_id_Set() const{
    return m_field_type_id_isSet;
}

bool OAIRequest_body_7::is_field_type_id_Valid() const{
    return m_field_type_id_isValid;
}

bool OAIRequest_body_7::isIsActive() const {
    return m_is_active;
}
void OAIRequest_body_7::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIRequest_body_7::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIRequest_body_7::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAIRequest_body_7::isIsFilter() const {
    return m_is_filter;
}
void OAIRequest_body_7::setIsFilter(const bool &is_filter) {
    m_is_filter = is_filter;
    m_is_filter_isSet = true;
}

bool OAIRequest_body_7::is_is_filter_Set() const{
    return m_is_filter_isSet;
}

bool OAIRequest_body_7::is_is_filter_Valid() const{
    return m_is_filter_isValid;
}

bool OAIRequest_body_7::isIsOnProductDetails() const {
    return m_is_on_product_details;
}
void OAIRequest_body_7::setIsOnProductDetails(const bool &is_on_product_details) {
    m_is_on_product_details = is_on_product_details;
    m_is_on_product_details_isSet = true;
}

bool OAIRequest_body_7::is_is_on_product_details_Set() const{
    return m_is_on_product_details_isSet;
}

bool OAIRequest_body_7::is_is_on_product_details_Valid() const{
    return m_is_on_product_details_isValid;
}

bool OAIRequest_body_7::isIsRequired() const {
    return m_is_required;
}
void OAIRequest_body_7::setIsRequired(const bool &is_required) {
    m_is_required = is_required;
    m_is_required_isSet = true;
}

bool OAIRequest_body_7::is_is_required_Set() const{
    return m_is_required_isSet;
}

bool OAIRequest_body_7::is_is_required_Valid() const{
    return m_is_required_isValid;
}

bool OAIRequest_body_7::isIsSideMenuLinkActive() const {
    return m_is_side_menu_link_active;
}
void OAIRequest_body_7::setIsSideMenuLinkActive(const bool &is_side_menu_link_active) {
    m_is_side_menu_link_active = is_side_menu_link_active;
    m_is_side_menu_link_active_isSet = true;
}

bool OAIRequest_body_7::is_is_side_menu_link_active_Set() const{
    return m_is_side_menu_link_active_isSet;
}

bool OAIRequest_body_7::is_is_side_menu_link_active_Valid() const{
    return m_is_side_menu_link_active_isValid;
}

bool OAIRequest_body_7::isIsStockKeepingUnit() const {
    return m_is_stock_keeping_unit;
}
void OAIRequest_body_7::setIsStockKeepingUnit(const bool &is_stock_keeping_unit) {
    m_is_stock_keeping_unit = is_stock_keeping_unit;
    m_is_stock_keeping_unit_isSet = true;
}

bool OAIRequest_body_7::is_is_stock_keeping_unit_Set() const{
    return m_is_stock_keeping_unit_isSet;
}

bool OAIRequest_body_7::is_is_stock_keeping_unit_Valid() const{
    return m_is_stock_keeping_unit_isValid;
}

bool OAIRequest_body_7::isIsTopMenuLinkActive() const {
    return m_is_top_menu_link_active;
}
void OAIRequest_body_7::setIsTopMenuLinkActive(const bool &is_top_menu_link_active) {
    m_is_top_menu_link_active = is_top_menu_link_active;
    m_is_top_menu_link_active_isSet = true;
}

bool OAIRequest_body_7::is_is_top_menu_link_active_Set() const{
    return m_is_top_menu_link_active_isSet;
}

bool OAIRequest_body_7::is_is_top_menu_link_active_Valid() const{
    return m_is_top_menu_link_active_isValid;
}

bool OAIRequest_body_7::isIsWizard() const {
    return m_is_wizard;
}
void OAIRequest_body_7::setIsWizard(const bool &is_wizard) {
    m_is_wizard = is_wizard;
    m_is_wizard_isSet = true;
}

bool OAIRequest_body_7::is_is_wizard_Set() const{
    return m_is_wizard_isSet;
}

bool OAIRequest_body_7::is_is_wizard_Valid() const{
    return m_is_wizard_isValid;
}

QString OAIRequest_body_7::getName() const {
    return m_name;
}
void OAIRequest_body_7::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIRequest_body_7::is_name_Set() const{
    return m_name_isSet;
}

bool OAIRequest_body_7::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIRequest_body_7::getPosition() const {
    return m_position;
}
void OAIRequest_body_7::setPosition(const qint32 &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIRequest_body_7::is_position_Set() const{
    return m_position_isSet;
}

bool OAIRequest_body_7::is_position_Valid() const{
    return m_position_isValid;
}

bool OAIRequest_body_7::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_default_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_field_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_field_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_filter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_on_product_details_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_required_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_side_menu_link_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_stock_keeping_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_top_menu_link_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_wizard_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRequest_body_7::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_category_id_isValid && m_default_value_isValid && m_description_isValid && m_field_group_id_isValid && m_field_type_id_isValid && m_is_active_isValid && m_is_filter_isValid && m_is_on_product_details_isValid && m_is_required_isValid && m_is_side_menu_link_active_isValid && m_is_stock_keeping_unit_isValid && m_is_top_menu_link_active_isValid && m_is_wizard_isValid && m_name_isValid && m_position_isValid && true;
}

} // namespace OpenAPI
