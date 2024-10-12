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

#include "OAIGetSKUandContext.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetSKUandContext::OAIGetSKUandContext(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetSKUandContext::OAIGetSKUandContext() {
    this->initializeModel();
}

OAIGetSKUandContext::~OAIGetSKUandContext() {}

void OAIGetSKUandContext::initializeModel() {

    m_alternate_id_values_isSet = false;
    m_alternate_id_values_isValid = false;

    m_alternate_ids_isSet = false;
    m_alternate_ids_isValid = false;

    m_attachments_isSet = false;
    m_attachments_isValid = false;

    m_brand_id_isSet = false;
    m_brand_id_isValid = false;

    m_brand_name_isSet = false;
    m_brand_name_isValid = false;

    m_csc_identification_isSet = false;
    m_csc_identification_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_collections_isSet = false;
    m_collections_isValid = false;

    m_commercial_condition_id_isSet = false;
    m_commercial_condition_id_isValid = false;

    m_complement_name_isSet = false;
    m_complement_name_isValid = false;

    m_detail_url_isSet = false;
    m_detail_url_isValid = false;

    m_dimension_isSet = false;
    m_dimension_isValid = false;

    m_estimated_date_arrival_isSet = false;
    m_estimated_date_arrival_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_url_isSet = false;
    m_image_url_isValid = false;

    m_images_isSet = false;
    m_images_isValid = false;

    m_information_source_isSet = false;
    m_information_source_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_gift_card_recharge_isSet = false;
    m_is_gift_card_recharge_isValid = false;

    m_is_inventoried_isSet = false;
    m_is_inventoried_isValid = false;

    m_is_kit_isSet = false;
    m_is_kit_isValid = false;

    m_is_product_active_isSet = false;
    m_is_product_active_isValid = false;

    m_is_transported_isSet = false;
    m_is_transported_isValid = false;

    m_key_words_isSet = false;
    m_key_words_isValid = false;

    m_kit_items_isSet = false;
    m_kit_items_isValid = false;

    m_manufacturer_code_isSet = false;
    m_manufacturer_code_isValid = false;

    m_measurement_unit_isSet = false;
    m_measurement_unit_isValid = false;

    m_modal_type_isSet = false;
    m_modal_type_isValid = false;

    m_name_complete_isSet = false;
    m_name_complete_isValid = false;

    m_product_categories_isSet = false;
    m_product_categories_isValid = false;

    m_product_category_ids_isSet = false;
    m_product_category_ids_isValid = false;

    m_product_clusters_ids_isSet = false;
    m_product_clusters_ids_isValid = false;

    m_product_description_isSet = false;
    m_product_description_isValid = false;

    m_product_final_score_isSet = false;
    m_product_final_score_isValid = false;

    m_product_global_category_id_isSet = false;
    m_product_global_category_id_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_product_is_visible_isSet = false;
    m_product_is_visible_isValid = false;

    m_product_name_isSet = false;
    m_product_name_isValid = false;

    m_product_ref_id_isSet = false;
    m_product_ref_id_isValid = false;

    m_product_specifications_isSet = false;
    m_product_specifications_isValid = false;

    m_real_dimension_isSet = false;
    m_real_dimension_isValid = false;

    m_release_date_isSet = false;
    m_release_date_isValid = false;

    m_reward_value_isSet = false;
    m_reward_value_isValid = false;

    m_sales_channels_isSet = false;
    m_sales_channels_isValid = false;

    m_services_isSet = false;
    m_services_isValid = false;

    m_show_if_not_available_isSet = false;
    m_show_if_not_available_isValid = false;

    m_sku_name_isSet = false;
    m_sku_name_isValid = false;

    m_sku_sellers_isSet = false;
    m_sku_sellers_isValid = false;

    m_sku_specifications_isSet = false;
    m_sku_specifications_isValid = false;

    m_tax_code_isSet = false;
    m_tax_code_isValid = false;

    m_unit_multiplier_isSet = false;
    m_unit_multiplier_isValid = false;
}

void OAIGetSKUandContext::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetSKUandContext::fromJsonObject(QJsonObject json) {

    m_alternate_id_values_isValid = ::OpenAPI::fromJsonValue(m_alternate_id_values, json[QString("AlternateIdValues")]);
    m_alternate_id_values_isSet = !json[QString("AlternateIdValues")].isNull() && m_alternate_id_values_isValid;

    m_alternate_ids_isValid = ::OpenAPI::fromJsonValue(m_alternate_ids, json[QString("AlternateIds")]);
    m_alternate_ids_isSet = !json[QString("AlternateIds")].isNull() && m_alternate_ids_isValid;

    m_attachments_isValid = ::OpenAPI::fromJsonValue(m_attachments, json[QString("Attachments")]);
    m_attachments_isSet = !json[QString("Attachments")].isNull() && m_attachments_isValid;

    m_brand_id_isValid = ::OpenAPI::fromJsonValue(m_brand_id, json[QString("BrandId")]);
    m_brand_id_isSet = !json[QString("BrandId")].isNull() && m_brand_id_isValid;

    m_brand_name_isValid = ::OpenAPI::fromJsonValue(m_brand_name, json[QString("BrandName")]);
    m_brand_name_isSet = !json[QString("BrandName")].isNull() && m_brand_name_isValid;

    m_csc_identification_isValid = ::OpenAPI::fromJsonValue(m_csc_identification, json[QString("CSCIdentification")]);
    m_csc_identification_isSet = !json[QString("CSCIdentification")].isNull() && m_csc_identification_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("Categories")]);
    m_categories_isSet = !json[QString("Categories")].isNull() && m_categories_isValid;

    m_collections_isValid = ::OpenAPI::fromJsonValue(m_collections, json[QString("Collections")]);
    m_collections_isSet = !json[QString("Collections")].isNull() && m_collections_isValid;

    m_commercial_condition_id_isValid = ::OpenAPI::fromJsonValue(m_commercial_condition_id, json[QString("CommercialConditionId")]);
    m_commercial_condition_id_isSet = !json[QString("CommercialConditionId")].isNull() && m_commercial_condition_id_isValid;

    m_complement_name_isValid = ::OpenAPI::fromJsonValue(m_complement_name, json[QString("ComplementName")]);
    m_complement_name_isSet = !json[QString("ComplementName")].isNull() && m_complement_name_isValid;

    m_detail_url_isValid = ::OpenAPI::fromJsonValue(m_detail_url, json[QString("DetailUrl")]);
    m_detail_url_isSet = !json[QString("DetailUrl")].isNull() && m_detail_url_isValid;

    m_dimension_isValid = ::OpenAPI::fromJsonValue(m_dimension, json[QString("Dimension")]);
    m_dimension_isSet = !json[QString("Dimension")].isNull() && m_dimension_isValid;

    m_estimated_date_arrival_isValid = ::OpenAPI::fromJsonValue(m_estimated_date_arrival, json[QString("EstimatedDateArrival")]);
    m_estimated_date_arrival_isSet = !json[QString("EstimatedDateArrival")].isNull() && m_estimated_date_arrival_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_image_url_isValid = ::OpenAPI::fromJsonValue(m_image_url, json[QString("ImageUrl")]);
    m_image_url_isSet = !json[QString("ImageUrl")].isNull() && m_image_url_isValid;

    m_images_isValid = ::OpenAPI::fromJsonValue(m_images, json[QString("Images")]);
    m_images_isSet = !json[QString("Images")].isNull() && m_images_isValid;

    m_information_source_isValid = ::OpenAPI::fromJsonValue(m_information_source, json[QString("InformationSource")]);
    m_information_source_isSet = !json[QString("InformationSource")].isNull() && m_information_source_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_gift_card_recharge_isValid = ::OpenAPI::fromJsonValue(m_is_gift_card_recharge, json[QString("IsGiftCardRecharge")]);
    m_is_gift_card_recharge_isSet = !json[QString("IsGiftCardRecharge")].isNull() && m_is_gift_card_recharge_isValid;

    m_is_inventoried_isValid = ::OpenAPI::fromJsonValue(m_is_inventoried, json[QString("IsInventoried")]);
    m_is_inventoried_isSet = !json[QString("IsInventoried")].isNull() && m_is_inventoried_isValid;

    m_is_kit_isValid = ::OpenAPI::fromJsonValue(m_is_kit, json[QString("IsKit")]);
    m_is_kit_isSet = !json[QString("IsKit")].isNull() && m_is_kit_isValid;

    m_is_product_active_isValid = ::OpenAPI::fromJsonValue(m_is_product_active, json[QString("IsProductActive")]);
    m_is_product_active_isSet = !json[QString("IsProductActive")].isNull() && m_is_product_active_isValid;

    m_is_transported_isValid = ::OpenAPI::fromJsonValue(m_is_transported, json[QString("IsTransported")]);
    m_is_transported_isSet = !json[QString("IsTransported")].isNull() && m_is_transported_isValid;

    m_key_words_isValid = ::OpenAPI::fromJsonValue(m_key_words, json[QString("KeyWords")]);
    m_key_words_isSet = !json[QString("KeyWords")].isNull() && m_key_words_isValid;

    m_kit_items_isValid = ::OpenAPI::fromJsonValue(m_kit_items, json[QString("KitItems")]);
    m_kit_items_isSet = !json[QString("KitItems")].isNull() && m_kit_items_isValid;

    m_manufacturer_code_isValid = ::OpenAPI::fromJsonValue(m_manufacturer_code, json[QString("ManufacturerCode")]);
    m_manufacturer_code_isSet = !json[QString("ManufacturerCode")].isNull() && m_manufacturer_code_isValid;

    m_measurement_unit_isValid = ::OpenAPI::fromJsonValue(m_measurement_unit, json[QString("MeasurementUnit")]);
    m_measurement_unit_isSet = !json[QString("MeasurementUnit")].isNull() && m_measurement_unit_isValid;

    m_modal_type_isValid = ::OpenAPI::fromJsonValue(m_modal_type, json[QString("ModalType")]);
    m_modal_type_isSet = !json[QString("ModalType")].isNull() && m_modal_type_isValid;

    m_name_complete_isValid = ::OpenAPI::fromJsonValue(m_name_complete, json[QString("NameComplete")]);
    m_name_complete_isSet = !json[QString("NameComplete")].isNull() && m_name_complete_isValid;

    if(json["ProductCategories"].isObject()){
        auto varmap = json["ProductCategories"].toObject().toVariantMap();
        m_product_categories_isValid = true;
        if(varmap.count() > 0){
            for(auto val : varmap.keys()){
                QMap<QString, QString> item;
                auto jval = QJsonValue::fromVariant(varmap.value(val));
                m_product_categories_isValid &= ::OpenAPI::fromJsonValue(item, jval);
                m_product_categories_isSet &= !jval.isNull() && m_product_categories_isValid;
                m_product_categories.insert(m_product_categories.end(), val, item);
            }
        }
    }

    m_product_category_ids_isValid = ::OpenAPI::fromJsonValue(m_product_category_ids, json[QString("ProductCategoryIds")]);
    m_product_category_ids_isSet = !json[QString("ProductCategoryIds")].isNull() && m_product_category_ids_isValid;

    m_product_clusters_ids_isValid = ::OpenAPI::fromJsonValue(m_product_clusters_ids, json[QString("ProductClustersIds")]);
    m_product_clusters_ids_isSet = !json[QString("ProductClustersIds")].isNull() && m_product_clusters_ids_isValid;

    m_product_description_isValid = ::OpenAPI::fromJsonValue(m_product_description, json[QString("ProductDescription")]);
    m_product_description_isSet = !json[QString("ProductDescription")].isNull() && m_product_description_isValid;

    m_product_final_score_isValid = ::OpenAPI::fromJsonValue(m_product_final_score, json[QString("ProductFinalScore")]);
    m_product_final_score_isSet = !json[QString("ProductFinalScore")].isNull() && m_product_final_score_isValid;

    m_product_global_category_id_isValid = ::OpenAPI::fromJsonValue(m_product_global_category_id, json[QString("ProductGlobalCategoryId")]);
    m_product_global_category_id_isSet = !json[QString("ProductGlobalCategoryId")].isNull() && m_product_global_category_id_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("ProductId")]);
    m_product_id_isSet = !json[QString("ProductId")].isNull() && m_product_id_isValid;

    m_product_is_visible_isValid = ::OpenAPI::fromJsonValue(m_product_is_visible, json[QString("ProductIsVisible")]);
    m_product_is_visible_isSet = !json[QString("ProductIsVisible")].isNull() && m_product_is_visible_isValid;

    m_product_name_isValid = ::OpenAPI::fromJsonValue(m_product_name, json[QString("ProductName")]);
    m_product_name_isSet = !json[QString("ProductName")].isNull() && m_product_name_isValid;

    m_product_ref_id_isValid = ::OpenAPI::fromJsonValue(m_product_ref_id, json[QString("ProductRefId")]);
    m_product_ref_id_isSet = !json[QString("ProductRefId")].isNull() && m_product_ref_id_isValid;

    m_product_specifications_isValid = ::OpenAPI::fromJsonValue(m_product_specifications, json[QString("ProductSpecifications")]);
    m_product_specifications_isSet = !json[QString("ProductSpecifications")].isNull() && m_product_specifications_isValid;

    m_real_dimension_isValid = ::OpenAPI::fromJsonValue(m_real_dimension, json[QString("RealDimension")]);
    m_real_dimension_isSet = !json[QString("RealDimension")].isNull() && m_real_dimension_isValid;

    m_release_date_isValid = ::OpenAPI::fromJsonValue(m_release_date, json[QString("ReleaseDate")]);
    m_release_date_isSet = !json[QString("ReleaseDate")].isNull() && m_release_date_isValid;

    m_reward_value_isValid = ::OpenAPI::fromJsonValue(m_reward_value, json[QString("RewardValue")]);
    m_reward_value_isSet = !json[QString("RewardValue")].isNull() && m_reward_value_isValid;

    m_sales_channels_isValid = ::OpenAPI::fromJsonValue(m_sales_channels, json[QString("SalesChannels")]);
    m_sales_channels_isSet = !json[QString("SalesChannels")].isNull() && m_sales_channels_isValid;

    m_services_isValid = ::OpenAPI::fromJsonValue(m_services, json[QString("Services")]);
    m_services_isSet = !json[QString("Services")].isNull() && m_services_isValid;

    m_show_if_not_available_isValid = ::OpenAPI::fromJsonValue(m_show_if_not_available, json[QString("ShowIfNotAvailable")]);
    m_show_if_not_available_isSet = !json[QString("ShowIfNotAvailable")].isNull() && m_show_if_not_available_isValid;

    m_sku_name_isValid = ::OpenAPI::fromJsonValue(m_sku_name, json[QString("SkuName")]);
    m_sku_name_isSet = !json[QString("SkuName")].isNull() && m_sku_name_isValid;

    m_sku_sellers_isValid = ::OpenAPI::fromJsonValue(m_sku_sellers, json[QString("SkuSellers")]);
    m_sku_sellers_isSet = !json[QString("SkuSellers")].isNull() && m_sku_sellers_isValid;

    m_sku_specifications_isValid = ::OpenAPI::fromJsonValue(m_sku_specifications, json[QString("SkuSpecifications")]);
    m_sku_specifications_isSet = !json[QString("SkuSpecifications")].isNull() && m_sku_specifications_isValid;

    m_tax_code_isValid = ::OpenAPI::fromJsonValue(m_tax_code, json[QString("TaxCode")]);
    m_tax_code_isSet = !json[QString("TaxCode")].isNull() && m_tax_code_isValid;

    m_unit_multiplier_isValid = ::OpenAPI::fromJsonValue(m_unit_multiplier, json[QString("UnitMultiplier")]);
    m_unit_multiplier_isSet = !json[QString("UnitMultiplier")].isNull() && m_unit_multiplier_isValid;
}

QString OAIGetSKUandContext::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetSKUandContext::asJsonObject() const {
    QJsonObject obj;
    if (m_alternate_id_values.size() > 0) {
        obj.insert(QString("AlternateIdValues"), ::OpenAPI::toJsonValue(m_alternate_id_values));
    }
    if (m_alternate_ids.isSet()) {
        obj.insert(QString("AlternateIds"), ::OpenAPI::toJsonValue(m_alternate_ids));
    }
    if (m_attachments.size() > 0) {
        obj.insert(QString("Attachments"), ::OpenAPI::toJsonValue(m_attachments));
    }
    if (m_brand_id_isSet) {
        obj.insert(QString("BrandId"), ::OpenAPI::toJsonValue(m_brand_id));
    }
    if (m_brand_name_isSet) {
        obj.insert(QString("BrandName"), ::OpenAPI::toJsonValue(m_brand_name));
    }
    if (m_csc_identification_isSet) {
        obj.insert(QString("CSCIdentification"), ::OpenAPI::toJsonValue(m_csc_identification));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("Categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_collections.size() > 0) {
        obj.insert(QString("Collections"), ::OpenAPI::toJsonValue(m_collections));
    }
    if (m_commercial_condition_id_isSet) {
        obj.insert(QString("CommercialConditionId"), ::OpenAPI::toJsonValue(m_commercial_condition_id));
    }
    if (m_complement_name_isSet) {
        obj.insert(QString("ComplementName"), ::OpenAPI::toJsonValue(m_complement_name));
    }
    if (m_detail_url_isSet) {
        obj.insert(QString("DetailUrl"), ::OpenAPI::toJsonValue(m_detail_url));
    }
    if (m_dimension.isSet()) {
        obj.insert(QString("Dimension"), ::OpenAPI::toJsonValue(m_dimension));
    }
    if (m_estimated_date_arrival_isSet) {
        obj.insert(QString("EstimatedDateArrival"), ::OpenAPI::toJsonValue(m_estimated_date_arrival));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_url_isSet) {
        obj.insert(QString("ImageUrl"), ::OpenAPI::toJsonValue(m_image_url));
    }
    if (m_images.size() > 0) {
        obj.insert(QString("Images"), ::OpenAPI::toJsonValue(m_images));
    }
    if (m_information_source_isSet) {
        obj.insert(QString("InformationSource"), ::OpenAPI::toJsonValue(m_information_source));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_gift_card_recharge_isSet) {
        obj.insert(QString("IsGiftCardRecharge"), ::OpenAPI::toJsonValue(m_is_gift_card_recharge));
    }
    if (m_is_inventoried_isSet) {
        obj.insert(QString("IsInventoried"), ::OpenAPI::toJsonValue(m_is_inventoried));
    }
    if (m_is_kit_isSet) {
        obj.insert(QString("IsKit"), ::OpenAPI::toJsonValue(m_is_kit));
    }
    if (m_is_product_active_isSet) {
        obj.insert(QString("IsProductActive"), ::OpenAPI::toJsonValue(m_is_product_active));
    }
    if (m_is_transported_isSet) {
        obj.insert(QString("IsTransported"), ::OpenAPI::toJsonValue(m_is_transported));
    }
    if (m_key_words_isSet) {
        obj.insert(QString("KeyWords"), ::OpenAPI::toJsonValue(m_key_words));
    }
    if (m_kit_items.size() > 0) {
        obj.insert(QString("KitItems"), ::OpenAPI::toJsonValue(m_kit_items));
    }
    if (m_manufacturer_code_isSet) {
        obj.insert(QString("ManufacturerCode"), ::OpenAPI::toJsonValue(m_manufacturer_code));
    }
    if (m_measurement_unit_isSet) {
        obj.insert(QString("MeasurementUnit"), ::OpenAPI::toJsonValue(m_measurement_unit));
    }
    if (m_modal_type_isSet) {
        obj.insert(QString("ModalType"), ::OpenAPI::toJsonValue(m_modal_type));
    }
    if (m_name_complete_isSet) {
        obj.insert(QString("NameComplete"), ::OpenAPI::toJsonValue(m_name_complete));
    }
    if (m_product_categories.size() > 0) {
        
        obj.insert(QString("ProductCategories"), toJsonValue(m_product_categories));
    }
    if (m_product_category_ids_isSet) {
        obj.insert(QString("ProductCategoryIds"), ::OpenAPI::toJsonValue(m_product_category_ids));
    }
    if (m_product_clusters_ids_isSet) {
        obj.insert(QString("ProductClustersIds"), ::OpenAPI::toJsonValue(m_product_clusters_ids));
    }
    if (m_product_description_isSet) {
        obj.insert(QString("ProductDescription"), ::OpenAPI::toJsonValue(m_product_description));
    }
    if (m_product_final_score_isSet) {
        obj.insert(QString("ProductFinalScore"), ::OpenAPI::toJsonValue(m_product_final_score));
    }
    if (m_product_global_category_id_isSet) {
        obj.insert(QString("ProductGlobalCategoryId"), ::OpenAPI::toJsonValue(m_product_global_category_id));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("ProductId"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_product_is_visible_isSet) {
        obj.insert(QString("ProductIsVisible"), ::OpenAPI::toJsonValue(m_product_is_visible));
    }
    if (m_product_name_isSet) {
        obj.insert(QString("ProductName"), ::OpenAPI::toJsonValue(m_product_name));
    }
    if (m_product_ref_id_isSet) {
        obj.insert(QString("ProductRefId"), ::OpenAPI::toJsonValue(m_product_ref_id));
    }
    if (m_product_specifications.size() > 0) {
        obj.insert(QString("ProductSpecifications"), ::OpenAPI::toJsonValue(m_product_specifications));
    }
    if (m_real_dimension.isSet()) {
        obj.insert(QString("RealDimension"), ::OpenAPI::toJsonValue(m_real_dimension));
    }
    if (m_release_date_isSet) {
        obj.insert(QString("ReleaseDate"), ::OpenAPI::toJsonValue(m_release_date));
    }
    if (m_reward_value_isSet) {
        obj.insert(QString("RewardValue"), ::OpenAPI::toJsonValue(m_reward_value));
    }
    if (m_sales_channels.size() > 0) {
        obj.insert(QString("SalesChannels"), ::OpenAPI::toJsonValue(m_sales_channels));
    }
    if (m_services.size() > 0) {
        obj.insert(QString("Services"), ::OpenAPI::toJsonValue(m_services));
    }
    if (m_show_if_not_available_isSet) {
        obj.insert(QString("ShowIfNotAvailable"), ::OpenAPI::toJsonValue(m_show_if_not_available));
    }
    if (m_sku_name_isSet) {
        obj.insert(QString("SkuName"), ::OpenAPI::toJsonValue(m_sku_name));
    }
    if (m_sku_sellers.size() > 0) {
        obj.insert(QString("SkuSellers"), ::OpenAPI::toJsonValue(m_sku_sellers));
    }
    if (m_sku_specifications.size() > 0) {
        obj.insert(QString("SkuSpecifications"), ::OpenAPI::toJsonValue(m_sku_specifications));
    }
    if (m_tax_code_isSet) {
        obj.insert(QString("TaxCode"), ::OpenAPI::toJsonValue(m_tax_code));
    }
    if (m_unit_multiplier_isSet) {
        obj.insert(QString("UnitMultiplier"), ::OpenAPI::toJsonValue(m_unit_multiplier));
    }
    return obj;
}

QList<QString> OAIGetSKUandContext::getAlternateIdValues() const {
    return m_alternate_id_values;
}
void OAIGetSKUandContext::setAlternateIdValues(const QList<QString> &alternate_id_values) {
    m_alternate_id_values = alternate_id_values;
    m_alternate_id_values_isSet = true;
}

bool OAIGetSKUandContext::is_alternate_id_values_Set() const{
    return m_alternate_id_values_isSet;
}

bool OAIGetSKUandContext::is_alternate_id_values_Valid() const{
    return m_alternate_id_values_isValid;
}

OAIAlternateIds OAIGetSKUandContext::getAlternateIds() const {
    return m_alternate_ids;
}
void OAIGetSKUandContext::setAlternateIds(const OAIAlternateIds &alternate_ids) {
    m_alternate_ids = alternate_ids;
    m_alternate_ids_isSet = true;
}

bool OAIGetSKUandContext::is_alternate_ids_Set() const{
    return m_alternate_ids_isSet;
}

bool OAIGetSKUandContext::is_alternate_ids_Valid() const{
    return m_alternate_ids_isValid;
}

QList<OAIAttachment> OAIGetSKUandContext::getAttachments() const {
    return m_attachments;
}
void OAIGetSKUandContext::setAttachments(const QList<OAIAttachment> &attachments) {
    m_attachments = attachments;
    m_attachments_isSet = true;
}

bool OAIGetSKUandContext::is_attachments_Set() const{
    return m_attachments_isSet;
}

bool OAIGetSKUandContext::is_attachments_Valid() const{
    return m_attachments_isValid;
}

QString OAIGetSKUandContext::getBrandId() const {
    return m_brand_id;
}
void OAIGetSKUandContext::setBrandId(const QString &brand_id) {
    m_brand_id = brand_id;
    m_brand_id_isSet = true;
}

bool OAIGetSKUandContext::is_brand_id_Set() const{
    return m_brand_id_isSet;
}

bool OAIGetSKUandContext::is_brand_id_Valid() const{
    return m_brand_id_isValid;
}

QString OAIGetSKUandContext::getBrandName() const {
    return m_brand_name;
}
void OAIGetSKUandContext::setBrandName(const QString &brand_name) {
    m_brand_name = brand_name;
    m_brand_name_isSet = true;
}

bool OAIGetSKUandContext::is_brand_name_Set() const{
    return m_brand_name_isSet;
}

bool OAIGetSKUandContext::is_brand_name_Valid() const{
    return m_brand_name_isValid;
}

QString OAIGetSKUandContext::getCscIdentification() const {
    return m_csc_identification;
}
void OAIGetSKUandContext::setCscIdentification(const QString &csc_identification) {
    m_csc_identification = csc_identification;
    m_csc_identification_isSet = true;
}

bool OAIGetSKUandContext::is_csc_identification_Set() const{
    return m_csc_identification_isSet;
}

bool OAIGetSKUandContext::is_csc_identification_Valid() const{
    return m_csc_identification_isValid;
}

QList<QString> OAIGetSKUandContext::getCategories() const {
    return m_categories;
}
void OAIGetSKUandContext::setCategories(const QList<QString> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIGetSKUandContext::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIGetSKUandContext::is_categories_Valid() const{
    return m_categories_isValid;
}

QList<QString> OAIGetSKUandContext::getCollections() const {
    return m_collections;
}
void OAIGetSKUandContext::setCollections(const QList<QString> &collections) {
    m_collections = collections;
    m_collections_isSet = true;
}

bool OAIGetSKUandContext::is_collections_Set() const{
    return m_collections_isSet;
}

bool OAIGetSKUandContext::is_collections_Valid() const{
    return m_collections_isValid;
}

qint32 OAIGetSKUandContext::getCommercialConditionId() const {
    return m_commercial_condition_id;
}
void OAIGetSKUandContext::setCommercialConditionId(const qint32 &commercial_condition_id) {
    m_commercial_condition_id = commercial_condition_id;
    m_commercial_condition_id_isSet = true;
}

bool OAIGetSKUandContext::is_commercial_condition_id_Set() const{
    return m_commercial_condition_id_isSet;
}

bool OAIGetSKUandContext::is_commercial_condition_id_Valid() const{
    return m_commercial_condition_id_isValid;
}

QString OAIGetSKUandContext::getComplementName() const {
    return m_complement_name;
}
void OAIGetSKUandContext::setComplementName(const QString &complement_name) {
    m_complement_name = complement_name;
    m_complement_name_isSet = true;
}

bool OAIGetSKUandContext::is_complement_name_Set() const{
    return m_complement_name_isSet;
}

bool OAIGetSKUandContext::is_complement_name_Valid() const{
    return m_complement_name_isValid;
}

QString OAIGetSKUandContext::getDetailUrl() const {
    return m_detail_url;
}
void OAIGetSKUandContext::setDetailUrl(const QString &detail_url) {
    m_detail_url = detail_url;
    m_detail_url_isSet = true;
}

bool OAIGetSKUandContext::is_detail_url_Set() const{
    return m_detail_url_isSet;
}

bool OAIGetSKUandContext::is_detail_url_Valid() const{
    return m_detail_url_isValid;
}

OAIDimension OAIGetSKUandContext::getDimension() const {
    return m_dimension;
}
void OAIGetSKUandContext::setDimension(const OAIDimension &dimension) {
    m_dimension = dimension;
    m_dimension_isSet = true;
}

bool OAIGetSKUandContext::is_dimension_Set() const{
    return m_dimension_isSet;
}

bool OAIGetSKUandContext::is_dimension_Valid() const{
    return m_dimension_isValid;
}

QString OAIGetSKUandContext::getEstimatedDateArrival() const {
    return m_estimated_date_arrival;
}
void OAIGetSKUandContext::setEstimatedDateArrival(const QString &estimated_date_arrival) {
    m_estimated_date_arrival = estimated_date_arrival;
    m_estimated_date_arrival_isSet = true;
}

bool OAIGetSKUandContext::is_estimated_date_arrival_Set() const{
    return m_estimated_date_arrival_isSet;
}

bool OAIGetSKUandContext::is_estimated_date_arrival_Valid() const{
    return m_estimated_date_arrival_isValid;
}

qint32 OAIGetSKUandContext::getId() const {
    return m_id;
}
void OAIGetSKUandContext::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetSKUandContext::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetSKUandContext::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGetSKUandContext::getImageUrl() const {
    return m_image_url;
}
void OAIGetSKUandContext::setImageUrl(const QString &image_url) {
    m_image_url = image_url;
    m_image_url_isSet = true;
}

bool OAIGetSKUandContext::is_image_url_Set() const{
    return m_image_url_isSet;
}

bool OAIGetSKUandContext::is_image_url_Valid() const{
    return m_image_url_isValid;
}

QList<OAIImage> OAIGetSKUandContext::getImages() const {
    return m_images;
}
void OAIGetSKUandContext::setImages(const QList<OAIImage> &images) {
    m_images = images;
    m_images_isSet = true;
}

bool OAIGetSKUandContext::is_images_Set() const{
    return m_images_isSet;
}

bool OAIGetSKUandContext::is_images_Valid() const{
    return m_images_isValid;
}

QString OAIGetSKUandContext::getInformationSource() const {
    return m_information_source;
}
void OAIGetSKUandContext::setInformationSource(const QString &information_source) {
    m_information_source = information_source;
    m_information_source_isSet = true;
}

bool OAIGetSKUandContext::is_information_source_Set() const{
    return m_information_source_isSet;
}

bool OAIGetSKUandContext::is_information_source_Valid() const{
    return m_information_source_isValid;
}

bool OAIGetSKUandContext::isIsActive() const {
    return m_is_active;
}
void OAIGetSKUandContext::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIGetSKUandContext::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIGetSKUandContext::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAIGetSKUandContext::isIsGiftCardRecharge() const {
    return m_is_gift_card_recharge;
}
void OAIGetSKUandContext::setIsGiftCardRecharge(const bool &is_gift_card_recharge) {
    m_is_gift_card_recharge = is_gift_card_recharge;
    m_is_gift_card_recharge_isSet = true;
}

bool OAIGetSKUandContext::is_is_gift_card_recharge_Set() const{
    return m_is_gift_card_recharge_isSet;
}

bool OAIGetSKUandContext::is_is_gift_card_recharge_Valid() const{
    return m_is_gift_card_recharge_isValid;
}

bool OAIGetSKUandContext::isIsInventoried() const {
    return m_is_inventoried;
}
void OAIGetSKUandContext::setIsInventoried(const bool &is_inventoried) {
    m_is_inventoried = is_inventoried;
    m_is_inventoried_isSet = true;
}

bool OAIGetSKUandContext::is_is_inventoried_Set() const{
    return m_is_inventoried_isSet;
}

bool OAIGetSKUandContext::is_is_inventoried_Valid() const{
    return m_is_inventoried_isValid;
}

bool OAIGetSKUandContext::isIsKit() const {
    return m_is_kit;
}
void OAIGetSKUandContext::setIsKit(const bool &is_kit) {
    m_is_kit = is_kit;
    m_is_kit_isSet = true;
}

bool OAIGetSKUandContext::is_is_kit_Set() const{
    return m_is_kit_isSet;
}

bool OAIGetSKUandContext::is_is_kit_Valid() const{
    return m_is_kit_isValid;
}

bool OAIGetSKUandContext::isIsProductActive() const {
    return m_is_product_active;
}
void OAIGetSKUandContext::setIsProductActive(const bool &is_product_active) {
    m_is_product_active = is_product_active;
    m_is_product_active_isSet = true;
}

bool OAIGetSKUandContext::is_is_product_active_Set() const{
    return m_is_product_active_isSet;
}

bool OAIGetSKUandContext::is_is_product_active_Valid() const{
    return m_is_product_active_isValid;
}

bool OAIGetSKUandContext::isIsTransported() const {
    return m_is_transported;
}
void OAIGetSKUandContext::setIsTransported(const bool &is_transported) {
    m_is_transported = is_transported;
    m_is_transported_isSet = true;
}

bool OAIGetSKUandContext::is_is_transported_Set() const{
    return m_is_transported_isSet;
}

bool OAIGetSKUandContext::is_is_transported_Valid() const{
    return m_is_transported_isValid;
}

QString OAIGetSKUandContext::getKeyWords() const {
    return m_key_words;
}
void OAIGetSKUandContext::setKeyWords(const QString &key_words) {
    m_key_words = key_words;
    m_key_words_isSet = true;
}

bool OAIGetSKUandContext::is_key_words_Set() const{
    return m_key_words_isSet;
}

bool OAIGetSKUandContext::is_key_words_Valid() const{
    return m_key_words_isValid;
}

QList<QString> OAIGetSKUandContext::getKitItems() const {
    return m_kit_items;
}
void OAIGetSKUandContext::setKitItems(const QList<QString> &kit_items) {
    m_kit_items = kit_items;
    m_kit_items_isSet = true;
}

bool OAIGetSKUandContext::is_kit_items_Set() const{
    return m_kit_items_isSet;
}

bool OAIGetSKUandContext::is_kit_items_Valid() const{
    return m_kit_items_isValid;
}

QString OAIGetSKUandContext::getManufacturerCode() const {
    return m_manufacturer_code;
}
void OAIGetSKUandContext::setManufacturerCode(const QString &manufacturer_code) {
    m_manufacturer_code = manufacturer_code;
    m_manufacturer_code_isSet = true;
}

bool OAIGetSKUandContext::is_manufacturer_code_Set() const{
    return m_manufacturer_code_isSet;
}

bool OAIGetSKUandContext::is_manufacturer_code_Valid() const{
    return m_manufacturer_code_isValid;
}

QString OAIGetSKUandContext::getMeasurementUnit() const {
    return m_measurement_unit;
}
void OAIGetSKUandContext::setMeasurementUnit(const QString &measurement_unit) {
    m_measurement_unit = measurement_unit;
    m_measurement_unit_isSet = true;
}

bool OAIGetSKUandContext::is_measurement_unit_Set() const{
    return m_measurement_unit_isSet;
}

bool OAIGetSKUandContext::is_measurement_unit_Valid() const{
    return m_measurement_unit_isValid;
}

QString OAIGetSKUandContext::getModalType() const {
    return m_modal_type;
}
void OAIGetSKUandContext::setModalType(const QString &modal_type) {
    m_modal_type = modal_type;
    m_modal_type_isSet = true;
}

bool OAIGetSKUandContext::is_modal_type_Set() const{
    return m_modal_type_isSet;
}

bool OAIGetSKUandContext::is_modal_type_Valid() const{
    return m_modal_type_isValid;
}

QString OAIGetSKUandContext::getNameComplete() const {
    return m_name_complete;
}
void OAIGetSKUandContext::setNameComplete(const QString &name_complete) {
    m_name_complete = name_complete;
    m_name_complete_isSet = true;
}

bool OAIGetSKUandContext::is_name_complete_Set() const{
    return m_name_complete_isSet;
}

bool OAIGetSKUandContext::is_name_complete_Valid() const{
    return m_name_complete_isValid;
}

QMap<QString, QMap<QString, QString>> OAIGetSKUandContext::getProductCategories() const {
    return m_product_categories;
}
void OAIGetSKUandContext::setProductCategories(const QMap<QString, QMap<QString, QString>> &product_categories) {
    m_product_categories = product_categories;
    m_product_categories_isSet = true;
}

bool OAIGetSKUandContext::is_product_categories_Set() const{
    return m_product_categories_isSet;
}

bool OAIGetSKUandContext::is_product_categories_Valid() const{
    return m_product_categories_isValid;
}

QString OAIGetSKUandContext::getProductCategoryIds() const {
    return m_product_category_ids;
}
void OAIGetSKUandContext::setProductCategoryIds(const QString &product_category_ids) {
    m_product_category_ids = product_category_ids;
    m_product_category_ids_isSet = true;
}

bool OAIGetSKUandContext::is_product_category_ids_Set() const{
    return m_product_category_ids_isSet;
}

bool OAIGetSKUandContext::is_product_category_ids_Valid() const{
    return m_product_category_ids_isValid;
}

QString OAIGetSKUandContext::getProductClustersIds() const {
    return m_product_clusters_ids;
}
void OAIGetSKUandContext::setProductClustersIds(const QString &product_clusters_ids) {
    m_product_clusters_ids = product_clusters_ids;
    m_product_clusters_ids_isSet = true;
}

bool OAIGetSKUandContext::is_product_clusters_ids_Set() const{
    return m_product_clusters_ids_isSet;
}

bool OAIGetSKUandContext::is_product_clusters_ids_Valid() const{
    return m_product_clusters_ids_isValid;
}

QString OAIGetSKUandContext::getProductDescription() const {
    return m_product_description;
}
void OAIGetSKUandContext::setProductDescription(const QString &product_description) {
    m_product_description = product_description;
    m_product_description_isSet = true;
}

bool OAIGetSKUandContext::is_product_description_Set() const{
    return m_product_description_isSet;
}

bool OAIGetSKUandContext::is_product_description_Valid() const{
    return m_product_description_isValid;
}

qint32 OAIGetSKUandContext::getProductFinalScore() const {
    return m_product_final_score;
}
void OAIGetSKUandContext::setProductFinalScore(const qint32 &product_final_score) {
    m_product_final_score = product_final_score;
    m_product_final_score_isSet = true;
}

bool OAIGetSKUandContext::is_product_final_score_Set() const{
    return m_product_final_score_isSet;
}

bool OAIGetSKUandContext::is_product_final_score_Valid() const{
    return m_product_final_score_isValid;
}

qint32 OAIGetSKUandContext::getProductGlobalCategoryId() const {
    return m_product_global_category_id;
}
void OAIGetSKUandContext::setProductGlobalCategoryId(const qint32 &product_global_category_id) {
    m_product_global_category_id = product_global_category_id;
    m_product_global_category_id_isSet = true;
}

bool OAIGetSKUandContext::is_product_global_category_id_Set() const{
    return m_product_global_category_id_isSet;
}

bool OAIGetSKUandContext::is_product_global_category_id_Valid() const{
    return m_product_global_category_id_isValid;
}

qint32 OAIGetSKUandContext::getProductId() const {
    return m_product_id;
}
void OAIGetSKUandContext::setProductId(const qint32 &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIGetSKUandContext::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIGetSKUandContext::is_product_id_Valid() const{
    return m_product_id_isValid;
}

bool OAIGetSKUandContext::isProductIsVisible() const {
    return m_product_is_visible;
}
void OAIGetSKUandContext::setProductIsVisible(const bool &product_is_visible) {
    m_product_is_visible = product_is_visible;
    m_product_is_visible_isSet = true;
}

bool OAIGetSKUandContext::is_product_is_visible_Set() const{
    return m_product_is_visible_isSet;
}

bool OAIGetSKUandContext::is_product_is_visible_Valid() const{
    return m_product_is_visible_isValid;
}

QString OAIGetSKUandContext::getProductName() const {
    return m_product_name;
}
void OAIGetSKUandContext::setProductName(const QString &product_name) {
    m_product_name = product_name;
    m_product_name_isSet = true;
}

bool OAIGetSKUandContext::is_product_name_Set() const{
    return m_product_name_isSet;
}

bool OAIGetSKUandContext::is_product_name_Valid() const{
    return m_product_name_isValid;
}

QString OAIGetSKUandContext::getProductRefId() const {
    return m_product_ref_id;
}
void OAIGetSKUandContext::setProductRefId(const QString &product_ref_id) {
    m_product_ref_id = product_ref_id;
    m_product_ref_id_isSet = true;
}

bool OAIGetSKUandContext::is_product_ref_id_Set() const{
    return m_product_ref_id_isSet;
}

bool OAIGetSKUandContext::is_product_ref_id_Valid() const{
    return m_product_ref_id_isValid;
}

QList<OAIProductSpecification> OAIGetSKUandContext::getProductSpecifications() const {
    return m_product_specifications;
}
void OAIGetSKUandContext::setProductSpecifications(const QList<OAIProductSpecification> &product_specifications) {
    m_product_specifications = product_specifications;
    m_product_specifications_isSet = true;
}

bool OAIGetSKUandContext::is_product_specifications_Set() const{
    return m_product_specifications_isSet;
}

bool OAIGetSKUandContext::is_product_specifications_Valid() const{
    return m_product_specifications_isValid;
}

OAIRealDimension OAIGetSKUandContext::getRealDimension() const {
    return m_real_dimension;
}
void OAIGetSKUandContext::setRealDimension(const OAIRealDimension &real_dimension) {
    m_real_dimension = real_dimension;
    m_real_dimension_isSet = true;
}

bool OAIGetSKUandContext::is_real_dimension_Set() const{
    return m_real_dimension_isSet;
}

bool OAIGetSKUandContext::is_real_dimension_Valid() const{
    return m_real_dimension_isValid;
}

QString OAIGetSKUandContext::getReleaseDate() const {
    return m_release_date;
}
void OAIGetSKUandContext::setReleaseDate(const QString &release_date) {
    m_release_date = release_date;
    m_release_date_isSet = true;
}

bool OAIGetSKUandContext::is_release_date_Set() const{
    return m_release_date_isSet;
}

bool OAIGetSKUandContext::is_release_date_Valid() const{
    return m_release_date_isValid;
}

double OAIGetSKUandContext::getRewardValue() const {
    return m_reward_value;
}
void OAIGetSKUandContext::setRewardValue(const double &reward_value) {
    m_reward_value = reward_value;
    m_reward_value_isSet = true;
}

bool OAIGetSKUandContext::is_reward_value_Set() const{
    return m_reward_value_isSet;
}

bool OAIGetSKUandContext::is_reward_value_Valid() const{
    return m_reward_value_isValid;
}

QList<qint32> OAIGetSKUandContext::getSalesChannels() const {
    return m_sales_channels;
}
void OAIGetSKUandContext::setSalesChannels(const QList<qint32> &sales_channels) {
    m_sales_channels = sales_channels;
    m_sales_channels_isSet = true;
}

bool OAIGetSKUandContext::is_sales_channels_Set() const{
    return m_sales_channels_isSet;
}

bool OAIGetSKUandContext::is_sales_channels_Valid() const{
    return m_sales_channels_isValid;
}

QList<QString> OAIGetSKUandContext::getServices() const {
    return m_services;
}
void OAIGetSKUandContext::setServices(const QList<QString> &services) {
    m_services = services;
    m_services_isSet = true;
}

bool OAIGetSKUandContext::is_services_Set() const{
    return m_services_isSet;
}

bool OAIGetSKUandContext::is_services_Valid() const{
    return m_services_isValid;
}

bool OAIGetSKUandContext::isShowIfNotAvailable() const {
    return m_show_if_not_available;
}
void OAIGetSKUandContext::setShowIfNotAvailable(const bool &show_if_not_available) {
    m_show_if_not_available = show_if_not_available;
    m_show_if_not_available_isSet = true;
}

bool OAIGetSKUandContext::is_show_if_not_available_Set() const{
    return m_show_if_not_available_isSet;
}

bool OAIGetSKUandContext::is_show_if_not_available_Valid() const{
    return m_show_if_not_available_isValid;
}

QString OAIGetSKUandContext::getSkuName() const {
    return m_sku_name;
}
void OAIGetSKUandContext::setSkuName(const QString &sku_name) {
    m_sku_name = sku_name;
    m_sku_name_isSet = true;
}

bool OAIGetSKUandContext::is_sku_name_Set() const{
    return m_sku_name_isSet;
}

bool OAIGetSKUandContext::is_sku_name_Valid() const{
    return m_sku_name_isValid;
}

QList<OAISkuSeller> OAIGetSKUandContext::getSkuSellers() const {
    return m_sku_sellers;
}
void OAIGetSKUandContext::setSkuSellers(const QList<OAISkuSeller> &sku_sellers) {
    m_sku_sellers = sku_sellers;
    m_sku_sellers_isSet = true;
}

bool OAIGetSKUandContext::is_sku_sellers_Set() const{
    return m_sku_sellers_isSet;
}

bool OAIGetSKUandContext::is_sku_sellers_Valid() const{
    return m_sku_sellers_isValid;
}

QList<OAISkuSpecification> OAIGetSKUandContext::getSkuSpecifications() const {
    return m_sku_specifications;
}
void OAIGetSKUandContext::setSkuSpecifications(const QList<OAISkuSpecification> &sku_specifications) {
    m_sku_specifications = sku_specifications;
    m_sku_specifications_isSet = true;
}

bool OAIGetSKUandContext::is_sku_specifications_Set() const{
    return m_sku_specifications_isSet;
}

bool OAIGetSKUandContext::is_sku_specifications_Valid() const{
    return m_sku_specifications_isValid;
}

QString OAIGetSKUandContext::getTaxCode() const {
    return m_tax_code;
}
void OAIGetSKUandContext::setTaxCode(const QString &tax_code) {
    m_tax_code = tax_code;
    m_tax_code_isSet = true;
}

bool OAIGetSKUandContext::is_tax_code_Set() const{
    return m_tax_code_isSet;
}

bool OAIGetSKUandContext::is_tax_code_Valid() const{
    return m_tax_code_isValid;
}

double OAIGetSKUandContext::getUnitMultiplier() const {
    return m_unit_multiplier;
}
void OAIGetSKUandContext::setUnitMultiplier(const double &unit_multiplier) {
    m_unit_multiplier = unit_multiplier;
    m_unit_multiplier_isSet = true;
}

bool OAIGetSKUandContext::is_unit_multiplier_Set() const{
    return m_unit_multiplier_isSet;
}

bool OAIGetSKUandContext::is_unit_multiplier_Valid() const{
    return m_unit_multiplier_isValid;
}

bool OAIGetSKUandContext::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alternate_id_values.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_alternate_ids.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_attachments.size() > 0) {
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

        if (m_csc_identification_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_collections.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_commercial_condition_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_complement_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detail_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dimension.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_estimated_date_arrival_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_images.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_information_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_gift_card_recharge_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_inventoried_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_kit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_product_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_transported_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_words_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kit_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_manufacturer_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_measurement_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modal_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_complete_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_category_ids_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_clusters_ids_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_final_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_global_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_is_visible_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_ref_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_specifications.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_dimension.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reward_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_channels.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_services.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_if_not_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_sellers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_specifications.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_multiplier_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetSKUandContext::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_alternate_id_values_isValid && m_alternate_ids_isValid && m_attachments_isValid && m_brand_id_isValid && m_brand_name_isValid && m_csc_identification_isValid && m_categories_isValid && m_collections_isValid && m_commercial_condition_id_isValid && m_detail_url_isValid && m_dimension_isValid && m_estimated_date_arrival_isValid && m_id_isValid && m_image_url_isValid && m_images_isValid && m_information_source_isValid && m_is_active_isValid && m_is_gift_card_recharge_isValid && m_is_inventoried_isValid && m_is_kit_isValid && m_is_transported_isValid && m_kit_items_isValid && m_manufacturer_code_isValid && m_measurement_unit_isValid && m_modal_type_isValid && m_name_complete_isValid && m_product_categories_isValid && m_product_category_ids_isValid && m_product_clusters_ids_isValid && m_product_description_isValid && m_product_global_category_id_isValid && m_product_id_isValid && m_product_name_isValid && m_product_specifications_isValid && m_real_dimension_isValid && m_reward_value_isValid && m_sales_channels_isValid && m_services_isValid && m_sku_name_isValid && m_sku_sellers_isValid && m_sku_specifications_isValid && m_unit_multiplier_isValid && true;
}

} // namespace OpenAPI
