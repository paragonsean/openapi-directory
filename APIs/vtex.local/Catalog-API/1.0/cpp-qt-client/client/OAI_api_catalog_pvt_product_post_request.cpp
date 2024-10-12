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

#include "OAI_api_catalog_pvt_product_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_catalog_pvt_product_post_request::OAI_api_catalog_pvt_product_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_catalog_pvt_product_post_request::OAI_api_catalog_pvt_product_post_request() {
    this->initializeModel();
}

OAI_api_catalog_pvt_product_post_request::~OAI_api_catalog_pvt_product_post_request() {}

void OAI_api_catalog_pvt_product_post_request::initializeModel() {

    m_ad_words_remarketing_code_isSet = false;
    m_ad_words_remarketing_code_isValid = false;

    m_brand_id_isSet = false;
    m_brand_id_isValid = false;

    m_brand_name_isSet = false;
    m_brand_name_isValid = false;

    m_category_id_isSet = false;
    m_category_id_isValid = false;

    m_category_path_isSet = false;
    m_category_path_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_description_short_isSet = false;
    m_description_short_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_visible_isSet = false;
    m_is_visible_isValid = false;

    m_key_words_isSet = false;
    m_key_words_isValid = false;

    m_link_id_isSet = false;
    m_link_id_isValid = false;

    m_lomadee_campaign_code_isSet = false;
    m_lomadee_campaign_code_isValid = false;

    m_meta_tag_description_isSet = false;
    m_meta_tag_description_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_ref_id_isSet = false;
    m_ref_id_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_score_isSet = false;
    m_score_isValid = false;

    m_show_without_stock_isSet = false;
    m_show_without_stock_isValid = false;

    m_supplier_id_isSet = false;
    m_supplier_id_isValid = false;

    m_tax_code_isSet = false;
    m_tax_code_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAI_api_catalog_pvt_product_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_catalog_pvt_product_post_request::fromJsonObject(QJsonObject json) {

    m_ad_words_remarketing_code_isValid = ::OpenAPI::fromJsonValue(m_ad_words_remarketing_code, json[QString("AdWordsRemarketingCode")]);
    m_ad_words_remarketing_code_isSet = !json[QString("AdWordsRemarketingCode")].isNull() && m_ad_words_remarketing_code_isValid;

    m_brand_id_isValid = ::OpenAPI::fromJsonValue(m_brand_id, json[QString("BrandId")]);
    m_brand_id_isSet = !json[QString("BrandId")].isNull() && m_brand_id_isValid;

    m_brand_name_isValid = ::OpenAPI::fromJsonValue(m_brand_name, json[QString("BrandName")]);
    m_brand_name_isSet = !json[QString("BrandName")].isNull() && m_brand_name_isValid;

    m_category_id_isValid = ::OpenAPI::fromJsonValue(m_category_id, json[QString("CategoryId")]);
    m_category_id_isSet = !json[QString("CategoryId")].isNull() && m_category_id_isValid;

    m_category_path_isValid = ::OpenAPI::fromJsonValue(m_category_path, json[QString("CategoryPath")]);
    m_category_path_isSet = !json[QString("CategoryPath")].isNull() && m_category_path_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_description_short_isValid = ::OpenAPI::fromJsonValue(m_description_short, json[QString("DescriptionShort")]);
    m_description_short_isSet = !json[QString("DescriptionShort")].isNull() && m_description_short_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_visible_isValid = ::OpenAPI::fromJsonValue(m_is_visible, json[QString("IsVisible")]);
    m_is_visible_isSet = !json[QString("IsVisible")].isNull() && m_is_visible_isValid;

    m_key_words_isValid = ::OpenAPI::fromJsonValue(m_key_words, json[QString("KeyWords")]);
    m_key_words_isSet = !json[QString("KeyWords")].isNull() && m_key_words_isValid;

    m_link_id_isValid = ::OpenAPI::fromJsonValue(m_link_id, json[QString("LinkId")]);
    m_link_id_isSet = !json[QString("LinkId")].isNull() && m_link_id_isValid;

    m_lomadee_campaign_code_isValid = ::OpenAPI::fromJsonValue(m_lomadee_campaign_code, json[QString("LomadeeCampaignCode")]);
    m_lomadee_campaign_code_isSet = !json[QString("LomadeeCampaignCode")].isNull() && m_lomadee_campaign_code_isValid;

    m_meta_tag_description_isValid = ::OpenAPI::fromJsonValue(m_meta_tag_description, json[QString("MetaTagDescription")]);
    m_meta_tag_description_isSet = !json[QString("MetaTagDescription")].isNull() && m_meta_tag_description_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_ref_id_isValid = ::OpenAPI::fromJsonValue(m_ref_id, json[QString("RefId")]);
    m_ref_id_isSet = !json[QString("RefId")].isNull() && m_ref_id_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("ReleaseDate")]);
    m_release_date_isSet = !json[QString("ReleaseDate")].isNull() && m_release_date_isValid;

    m_score_isValid = ::OpenAPI::fromJsonValue(m_score, json[QString("Score")]);
    m_score_isSet = !json[QString("Score")].isNull() && m_score_isValid;

    m_show_without_stock_isValid = ::OpenAPI::fromJsonValue(m_show_without_stock, json[QString("ShowWithoutStock")]);
    m_show_without_stock_isSet = !json[QString("ShowWithoutStock")].isNull() && m_show_without_stock_isValid;

    m_supplier_id_isValid = ::OpenAPI::fromJsonValue(m_supplier_id, json[QString("SupplierId")]);
    m_supplier_id_isSet = !json[QString("SupplierId")].isNull() && m_supplier_id_isValid;

    m_tax_code_isValid = ::OpenAPI::fromJsonValue(m_tax_code, json[QString("TaxCode")]);
    m_tax_code_isSet = !json[QString("TaxCode")].isNull() && m_tax_code_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("Title")]);
    m_title_isSet = !json[QString("Title")].isNull() && m_title_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_catalog_pvt_product_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_ad_words_remarketing_code_isSet) {
        obj.insert(QString("AdWordsRemarketingCode"), ::OpenAPI::toJsonValue(m_ad_words_remarketing_code));
    }
    if (m_brand_id_isSet) {
        obj.insert(QString("BrandId"), ::OpenAPI::toJsonValue(m_brand_id));
    }
    if (m_brand_name_isSet) {
        obj.insert(QString("BrandName"), ::OpenAPI::toJsonValue(m_brand_name));
    }
    if (m_category_id_isSet) {
        obj.insert(QString("CategoryId"), ::OpenAPI::toJsonValue(m_category_id));
    }
    if (m_category_path_isSet) {
        obj.insert(QString("CategoryPath"), ::OpenAPI::toJsonValue(m_category_path));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_description_short_isSet) {
        obj.insert(QString("DescriptionShort"), ::OpenAPI::toJsonValue(m_description_short));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_visible_isSet) {
        obj.insert(QString("IsVisible"), ::OpenAPI::toJsonValue(m_is_visible));
    }
    if (m_key_words_isSet) {
        obj.insert(QString("KeyWords"), ::OpenAPI::toJsonValue(m_key_words));
    }
    if (m_link_id_isSet) {
        obj.insert(QString("LinkId"), ::OpenAPI::toJsonValue(m_link_id));
    }
    if (m_lomadee_campaign_code_isSet) {
        obj.insert(QString("LomadeeCampaignCode"), ::OpenAPI::toJsonValue(m_lomadee_campaign_code));
    }
    if (m_meta_tag_description_isSet) {
        obj.insert(QString("MetaTagDescription"), ::OpenAPI::toJsonValue(m_meta_tag_description));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_ref_id_isSet) {
        obj.insert(QString("RefId"), ::OpenAPI::toJsonValue(m_ref_id));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("ReleaseDate"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_score_isSet) {
        obj.insert(QString("Score"), ::OpenAPI::toJsonValue(m_score));
    }
    if (m_show_without_stock_isSet) {
        obj.insert(QString("ShowWithoutStock"), ::OpenAPI::toJsonValue(m_show_without_stock));
    }
    if (m_supplier_id_isSet) {
        obj.insert(QString("SupplierId"), ::OpenAPI::toJsonValue(m_supplier_id));
    }
    if (m_tax_code_isSet) {
        obj.insert(QString("TaxCode"), ::OpenAPI::toJsonValue(m_tax_code));
    }
    if (m_title_isSet) {
        obj.insert(QString("Title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAI_api_catalog_pvt_product_post_request::getAdWordsRemarketingCode() const {
    return m_ad_words_remarketing_code;
}
void OAI_api_catalog_pvt_product_post_request::setAdWordsRemarketingCode(const QString &ad_words_remarketing_code) {
    m_ad_words_remarketing_code = ad_words_remarketing_code;
    m_ad_words_remarketing_code_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_ad_words_remarketing_code_Set() const{
    return m_ad_words_remarketing_code_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_ad_words_remarketing_code_Valid() const{
    return m_ad_words_remarketing_code_isValid;
}

qint32 OAI_api_catalog_pvt_product_post_request::getBrandId() const {
    return m_brand_id;
}
void OAI_api_catalog_pvt_product_post_request::setBrandId(const qint32 &brand_id) {
    m_brand_id = brand_id;
    m_brand_id_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_brand_id_Set() const{
    return m_brand_id_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_brand_id_Valid() const{
    return m_brand_id_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getBrandName() const {
    return m_brand_name;
}
void OAI_api_catalog_pvt_product_post_request::setBrandName(const QString &brand_name) {
    m_brand_name = brand_name;
    m_brand_name_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_brand_name_Set() const{
    return m_brand_name_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_brand_name_Valid() const{
    return m_brand_name_isValid;
}

qint32 OAI_api_catalog_pvt_product_post_request::getCategoryId() const {
    return m_category_id;
}
void OAI_api_catalog_pvt_product_post_request::setCategoryId(const qint32 &category_id) {
    m_category_id = category_id;
    m_category_id_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_category_id_Set() const{
    return m_category_id_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_category_id_Valid() const{
    return m_category_id_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getCategoryPath() const {
    return m_category_path;
}
void OAI_api_catalog_pvt_product_post_request::setCategoryPath(const QString &category_path) {
    m_category_path = category_path;
    m_category_path_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_category_path_Set() const{
    return m_category_path_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_category_path_Valid() const{
    return m_category_path_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getDescription() const {
    return m_description;
}
void OAI_api_catalog_pvt_product_post_request::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_description_Set() const{
    return m_description_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_description_Valid() const{
    return m_description_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getDescriptionShort() const {
    return m_description_short;
}
void OAI_api_catalog_pvt_product_post_request::setDescriptionShort(const QString &description_short) {
    m_description_short = description_short;
    m_description_short_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_description_short_Set() const{
    return m_description_short_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_description_short_Valid() const{
    return m_description_short_isValid;
}

qint32 OAI_api_catalog_pvt_product_post_request::getId() const {
    return m_id;
}
void OAI_api_catalog_pvt_product_post_request::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_id_Valid() const{
    return m_id_isValid;
}

bool OAI_api_catalog_pvt_product_post_request::isIsActive() const {
    return m_is_active;
}
void OAI_api_catalog_pvt_product_post_request::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAI_api_catalog_pvt_product_post_request::isIsVisible() const {
    return m_is_visible;
}
void OAI_api_catalog_pvt_product_post_request::setIsVisible(const bool &is_visible) {
    m_is_visible = is_visible;
    m_is_visible_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_is_visible_Set() const{
    return m_is_visible_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_is_visible_Valid() const{
    return m_is_visible_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getKeyWords() const {
    return m_key_words;
}
void OAI_api_catalog_pvt_product_post_request::setKeyWords(const QString &key_words) {
    m_key_words = key_words;
    m_key_words_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_key_words_Set() const{
    return m_key_words_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_key_words_Valid() const{
    return m_key_words_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getLinkId() const {
    return m_link_id;
}
void OAI_api_catalog_pvt_product_post_request::setLinkId(const QString &link_id) {
    m_link_id = link_id;
    m_link_id_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_link_id_Set() const{
    return m_link_id_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_link_id_Valid() const{
    return m_link_id_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getLomadeeCampaignCode() const {
    return m_lomadee_campaign_code;
}
void OAI_api_catalog_pvt_product_post_request::setLomadeeCampaignCode(const QString &lomadee_campaign_code) {
    m_lomadee_campaign_code = lomadee_campaign_code;
    m_lomadee_campaign_code_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_lomadee_campaign_code_Set() const{
    return m_lomadee_campaign_code_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_lomadee_campaign_code_Valid() const{
    return m_lomadee_campaign_code_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getMetaTagDescription() const {
    return m_meta_tag_description;
}
void OAI_api_catalog_pvt_product_post_request::setMetaTagDescription(const QString &meta_tag_description) {
    m_meta_tag_description = meta_tag_description;
    m_meta_tag_description_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_meta_tag_description_Set() const{
    return m_meta_tag_description_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_meta_tag_description_Valid() const{
    return m_meta_tag_description_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getName() const {
    return m_name;
}
void OAI_api_catalog_pvt_product_post_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getRefId() const {
    return m_ref_id;
}
void OAI_api_catalog_pvt_product_post_request::setRefId(const QString &ref_id) {
    m_ref_id = ref_id;
    m_ref_id_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_ref_id_Set() const{
    return m_ref_id_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_ref_id_Valid() const{
    return m_ref_id_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getReleaseDate() const {
    return m_release_date;
}
void OAI_api_catalog_pvt_product_post_request::setReleaseDate(const QString &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_release_date_Valid() const{
    return m_release_date_isValid;
}

qint32 OAI_api_catalog_pvt_product_post_request::getScore() const {
    return m_score;
}
void OAI_api_catalog_pvt_product_post_request::setScore(const qint32 &score) {
    m_score = score;
    m_score_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_score_Set() const{
    return m_score_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_score_Valid() const{
    return m_score_isValid;
}

bool OAI_api_catalog_pvt_product_post_request::isShowWithoutStock() const {
    return m_show_without_stock;
}
void OAI_api_catalog_pvt_product_post_request::setShowWithoutStock(const bool &show_without_stock) {
    m_show_without_stock = show_without_stock;
    m_show_without_stock_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_show_without_stock_Set() const{
    return m_show_without_stock_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_show_without_stock_Valid() const{
    return m_show_without_stock_isValid;
}

qint32 OAI_api_catalog_pvt_product_post_request::getSupplierId() const {
    return m_supplier_id;
}
void OAI_api_catalog_pvt_product_post_request::setSupplierId(const qint32 &supplier_id) {
    m_supplier_id = supplier_id;
    m_supplier_id_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_supplier_id_Set() const{
    return m_supplier_id_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_supplier_id_Valid() const{
    return m_supplier_id_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getTaxCode() const {
    return m_tax_code;
}
void OAI_api_catalog_pvt_product_post_request::setTaxCode(const QString &tax_code) {
    m_tax_code = tax_code;
    m_tax_code_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_tax_code_Set() const{
    return m_tax_code_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_tax_code_Valid() const{
    return m_tax_code_isValid;
}

QString OAI_api_catalog_pvt_product_post_request::getTitle() const {
    return m_title;
}
void OAI_api_catalog_pvt_product_post_request::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAI_api_catalog_pvt_product_post_request::is_title_Set() const{
    return m_title_isSet;
}

bool OAI_api_catalog_pvt_product_post_request::is_title_Valid() const{
    return m_title_isValid;
}

bool OAI_api_catalog_pvt_product_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ad_words_remarketing_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_brand_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_brand_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_category_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_short_isSet) {
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

        if (m_is_visible_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_words_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lomadee_campaign_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta_tag_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ref_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_without_stock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supplier_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_code_isSet) {
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

bool OAI_api_catalog_pvt_product_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
