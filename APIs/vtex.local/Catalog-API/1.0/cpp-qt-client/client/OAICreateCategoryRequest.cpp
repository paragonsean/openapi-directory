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

#include "OAICreateCategoryRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateCategoryRequest::OAICreateCategoryRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateCategoryRequest::OAICreateCategoryRequest() {
    this->initializeModel();
}

OAICreateCategoryRequest::~OAICreateCategoryRequest() {}

void OAICreateCategoryRequest::initializeModel() {

    m_active_store_front_link_isSet = false;
    m_active_store_front_link_isValid = false;

    m_ad_words_remarketing_code_isSet = false;
    m_ad_words_remarketing_code_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_father_category_id_isSet = false;
    m_father_category_id_isValid = false;

    m_global_category_id_isSet = false;
    m_global_category_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_keywords_isSet = false;
    m_keywords_isValid = false;

    m_lomadee_campaign_code_isSet = false;
    m_lomadee_campaign_code_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_score_isSet = false;
    m_score_isValid = false;

    m_show_brand_filter_isSet = false;
    m_show_brand_filter_isValid = false;

    m_show_in_store_front_isSet = false;
    m_show_in_store_front_isValid = false;

    m_stock_keeping_unit_selection_mode_isSet = false;
    m_stock_keeping_unit_selection_mode_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAICreateCategoryRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateCategoryRequest::fromJsonObject(QJsonObject json) {

    m_active_store_front_link_isValid = ::OpenAPI::fromJsonValue(m_active_store_front_link, json[QString("ActiveStoreFrontLink")]);
    m_active_store_front_link_isSet = !json[QString("ActiveStoreFrontLink")].isNull() && m_active_store_front_link_isValid;

    m_ad_words_remarketing_code_isValid = ::OpenAPI::fromJsonValue(m_ad_words_remarketing_code, json[QString("AdWordsRemarketingCode")]);
    m_ad_words_remarketing_code_isSet = !json[QString("AdWordsRemarketingCode")].isNull() && m_ad_words_remarketing_code_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_father_category_id_isValid = ::OpenAPI::fromJsonValue(m_father_category_id, json[QString("FatherCategoryId")]);
    m_father_category_id_isSet = !json[QString("FatherCategoryId")].isNull() && m_father_category_id_isValid;

    m_global_category_id_isValid = ::OpenAPI::fromJsonValue(m_global_category_id, json[QString("GlobalCategoryId")]);
    m_global_category_id_isSet = !json[QString("GlobalCategoryId")].isNull() && m_global_category_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_keywords_isValid = ::OpenAPI::fromJsonValue(m_keywords, json[QString("Keywords")]);
    m_keywords_isSet = !json[QString("Keywords")].isNull() && m_keywords_isValid;

    m_lomadee_campaign_code_isValid = ::OpenAPI::fromJsonValue(m_lomadee_campaign_code, json[QString("LomadeeCampaignCode")]);
    m_lomadee_campaign_code_isSet = !json[QString("LomadeeCampaignCode")].isNull() && m_lomadee_campaign_code_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_score_isValid = ::OpenAPI::fromJsonValue(m_score, json[QString("Score")]);
    m_score_isSet = !json[QString("Score")].isNull() && m_score_isValid;

    m_show_brand_filter_isValid = ::OpenAPI::fromJsonValue(m_show_brand_filter, json[QString("ShowBrandFilter")]);
    m_show_brand_filter_isSet = !json[QString("ShowBrandFilter")].isNull() && m_show_brand_filter_isValid;

    m_show_in_store_front_isValid = ::OpenAPI::fromJsonValue(m_show_in_store_front, json[QString("ShowInStoreFront")]);
    m_show_in_store_front_isSet = !json[QString("ShowInStoreFront")].isNull() && m_show_in_store_front_isValid;

    m_stock_keeping_unit_selection_mode_isValid = ::OpenAPI::fromJsonValue(m_stock_keeping_unit_selection_mode, json[QString("StockKeepingUnitSelectionMode")]);
    m_stock_keeping_unit_selection_mode_isSet = !json[QString("StockKeepingUnitSelectionMode")].isNull() && m_stock_keeping_unit_selection_mode_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("Title")]);
    m_title_isSet = !json[QString("Title")].isNull() && m_title_isValid;
}

QString OAICreateCategoryRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateCategoryRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_active_store_front_link_isSet) {
        obj.insert(QString("ActiveStoreFrontLink"), ::OpenAPI::toJsonValue(m_active_store_front_link));
    }
    if (m_ad_words_remarketing_code_isSet) {
        obj.insert(QString("AdWordsRemarketingCode"), ::OpenAPI::toJsonValue(m_ad_words_remarketing_code));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_father_category_id_isSet) {
        obj.insert(QString("FatherCategoryId"), ::OpenAPI::toJsonValue(m_father_category_id));
    }
    if (m_global_category_id_isSet) {
        obj.insert(QString("GlobalCategoryId"), ::OpenAPI::toJsonValue(m_global_category_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_keywords_isSet) {
        obj.insert(QString("Keywords"), ::OpenAPI::toJsonValue(m_keywords));
    }
    if (m_lomadee_campaign_code_isSet) {
        obj.insert(QString("LomadeeCampaignCode"), ::OpenAPI::toJsonValue(m_lomadee_campaign_code));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_score_isSet) {
        obj.insert(QString("Score"), ::OpenAPI::toJsonValue(m_score));
    }
    if (m_show_brand_filter_isSet) {
        obj.insert(QString("ShowBrandFilter"), ::OpenAPI::toJsonValue(m_show_brand_filter));
    }
    if (m_show_in_store_front_isSet) {
        obj.insert(QString("ShowInStoreFront"), ::OpenAPI::toJsonValue(m_show_in_store_front));
    }
    if (m_stock_keeping_unit_selection_mode_isSet) {
        obj.insert(QString("StockKeepingUnitSelectionMode"), ::OpenAPI::toJsonValue(m_stock_keeping_unit_selection_mode));
    }
    if (m_title_isSet) {
        obj.insert(QString("Title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

bool OAICreateCategoryRequest::isActiveStoreFrontLink() const {
    return m_active_store_front_link;
}
void OAICreateCategoryRequest::setActiveStoreFrontLink(const bool &active_store_front_link) {
    m_active_store_front_link = active_store_front_link;
    m_active_store_front_link_isSet = true;
}

bool OAICreateCategoryRequest::is_active_store_front_link_Set() const{
    return m_active_store_front_link_isSet;
}

bool OAICreateCategoryRequest::is_active_store_front_link_Valid() const{
    return m_active_store_front_link_isValid;
}

QString OAICreateCategoryRequest::getAdWordsRemarketingCode() const {
    return m_ad_words_remarketing_code;
}
void OAICreateCategoryRequest::setAdWordsRemarketingCode(const QString &ad_words_remarketing_code) {
    m_ad_words_remarketing_code = ad_words_remarketing_code;
    m_ad_words_remarketing_code_isSet = true;
}

bool OAICreateCategoryRequest::is_ad_words_remarketing_code_Set() const{
    return m_ad_words_remarketing_code_isSet;
}

bool OAICreateCategoryRequest::is_ad_words_remarketing_code_Valid() const{
    return m_ad_words_remarketing_code_isValid;
}

QString OAICreateCategoryRequest::getDescription() const {
    return m_description;
}
void OAICreateCategoryRequest::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICreateCategoryRequest::is_description_Set() const{
    return m_description_isSet;
}

bool OAICreateCategoryRequest::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAICreateCategoryRequest::getFatherCategoryId() const {
    return m_father_category_id;
}
void OAICreateCategoryRequest::setFatherCategoryId(const qint32 &father_category_id) {
    m_father_category_id = father_category_id;
    m_father_category_id_isSet = true;
}

bool OAICreateCategoryRequest::is_father_category_id_Set() const{
    return m_father_category_id_isSet;
}

bool OAICreateCategoryRequest::is_father_category_id_Valid() const{
    return m_father_category_id_isValid;
}

qint32 OAICreateCategoryRequest::getGlobalCategoryId() const {
    return m_global_category_id;
}
void OAICreateCategoryRequest::setGlobalCategoryId(const qint32 &global_category_id) {
    m_global_category_id = global_category_id;
    m_global_category_id_isSet = true;
}

bool OAICreateCategoryRequest::is_global_category_id_Set() const{
    return m_global_category_id_isSet;
}

bool OAICreateCategoryRequest::is_global_category_id_Valid() const{
    return m_global_category_id_isValid;
}

qint32 OAICreateCategoryRequest::getId() const {
    return m_id;
}
void OAICreateCategoryRequest::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICreateCategoryRequest::is_id_Set() const{
    return m_id_isSet;
}

bool OAICreateCategoryRequest::is_id_Valid() const{
    return m_id_isValid;
}

bool OAICreateCategoryRequest::isIsActive() const {
    return m_is_active;
}
void OAICreateCategoryRequest::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAICreateCategoryRequest::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAICreateCategoryRequest::is_is_active_Valid() const{
    return m_is_active_isValid;
}

QString OAICreateCategoryRequest::getKeywords() const {
    return m_keywords;
}
void OAICreateCategoryRequest::setKeywords(const QString &keywords) {
    m_keywords = keywords;
    m_keywords_isSet = true;
}

bool OAICreateCategoryRequest::is_keywords_Set() const{
    return m_keywords_isSet;
}

bool OAICreateCategoryRequest::is_keywords_Valid() const{
    return m_keywords_isValid;
}

QString OAICreateCategoryRequest::getLomadeeCampaignCode() const {
    return m_lomadee_campaign_code;
}
void OAICreateCategoryRequest::setLomadeeCampaignCode(const QString &lomadee_campaign_code) {
    m_lomadee_campaign_code = lomadee_campaign_code;
    m_lomadee_campaign_code_isSet = true;
}

bool OAICreateCategoryRequest::is_lomadee_campaign_code_Set() const{
    return m_lomadee_campaign_code_isSet;
}

bool OAICreateCategoryRequest::is_lomadee_campaign_code_Valid() const{
    return m_lomadee_campaign_code_isValid;
}

QString OAICreateCategoryRequest::getName() const {
    return m_name;
}
void OAICreateCategoryRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateCategoryRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateCategoryRequest::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAICreateCategoryRequest::getScore() const {
    return m_score;
}
void OAICreateCategoryRequest::setScore(const qint32 &score) {
    m_score = score;
    m_score_isSet = true;
}

bool OAICreateCategoryRequest::is_score_Set() const{
    return m_score_isSet;
}

bool OAICreateCategoryRequest::is_score_Valid() const{
    return m_score_isValid;
}

bool OAICreateCategoryRequest::isShowBrandFilter() const {
    return m_show_brand_filter;
}
void OAICreateCategoryRequest::setShowBrandFilter(const bool &show_brand_filter) {
    m_show_brand_filter = show_brand_filter;
    m_show_brand_filter_isSet = true;
}

bool OAICreateCategoryRequest::is_show_brand_filter_Set() const{
    return m_show_brand_filter_isSet;
}

bool OAICreateCategoryRequest::is_show_brand_filter_Valid() const{
    return m_show_brand_filter_isValid;
}

bool OAICreateCategoryRequest::isShowInStoreFront() const {
    return m_show_in_store_front;
}
void OAICreateCategoryRequest::setShowInStoreFront(const bool &show_in_store_front) {
    m_show_in_store_front = show_in_store_front;
    m_show_in_store_front_isSet = true;
}

bool OAICreateCategoryRequest::is_show_in_store_front_Set() const{
    return m_show_in_store_front_isSet;
}

bool OAICreateCategoryRequest::is_show_in_store_front_Valid() const{
    return m_show_in_store_front_isValid;
}

QString OAICreateCategoryRequest::getStockKeepingUnitSelectionMode() const {
    return m_stock_keeping_unit_selection_mode;
}
void OAICreateCategoryRequest::setStockKeepingUnitSelectionMode(const QString &stock_keeping_unit_selection_mode) {
    m_stock_keeping_unit_selection_mode = stock_keeping_unit_selection_mode;
    m_stock_keeping_unit_selection_mode_isSet = true;
}

bool OAICreateCategoryRequest::is_stock_keeping_unit_selection_mode_Set() const{
    return m_stock_keeping_unit_selection_mode_isSet;
}

bool OAICreateCategoryRequest::is_stock_keeping_unit_selection_mode_Valid() const{
    return m_stock_keeping_unit_selection_mode_isValid;
}

QString OAICreateCategoryRequest::getTitle() const {
    return m_title;
}
void OAICreateCategoryRequest::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAICreateCategoryRequest::is_title_Set() const{
    return m_title_isSet;
}

bool OAICreateCategoryRequest::is_title_Valid() const{
    return m_title_isValid;
}

bool OAICreateCategoryRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_store_front_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ad_words_remarketing_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_father_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_category_id_isSet) {
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

        if (m_keywords_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lomadee_campaign_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_brand_filter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_in_store_front_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stock_keeping_unit_selection_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateCategoryRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_active_store_front_link_isValid && m_ad_words_remarketing_code_isValid && m_description_isValid && m_father_category_id_isValid && m_global_category_id_isValid && m_is_active_isValid && m_keywords_isValid && m_lomadee_campaign_code_isValid && m_name_isValid && m_score_isValid && m_show_brand_filter_isValid && m_show_in_store_front_isValid && m_stock_keeping_unit_selection_mode_isValid && m_title_isValid && true;
}

} // namespace OpenAPI
