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

#include "OAI_api_catalog_pvt_stockkeepingunit_post_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_catalog_pvt_stockkeepingunit_post_200_response::OAI_api_catalog_pvt_stockkeepingunit_post_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_catalog_pvt_stockkeepingunit_post_200_response::OAI_api_catalog_pvt_stockkeepingunit_post_200_response() {
    this->initializeModel();
}

OAI_api_catalog_pvt_stockkeepingunit_post_200_response::~OAI_api_catalog_pvt_stockkeepingunit_post_200_response() {}

void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::initializeModel() {

    m_activate_if_possible_isSet = false;
    m_activate_if_possible_isValid = false;

    m_commercial_condition_id_isSet = false;
    m_commercial_condition_id_isValid = false;

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_cubic_weight_isSet = false;
    m_cubic_weight_isValid = false;

    m_ean_isSet = false;
    m_ean_isValid = false;

    m_estimated_date_arrival_isSet = false;
    m_estimated_date_arrival_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_kit_isSet = false;
    m_is_kit_isValid = false;

    m_kit_itens_sell_apart_isSet = false;
    m_kit_itens_sell_apart_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_manufacturer_code_isSet = false;
    m_manufacturer_code_isValid = false;

    m_measurement_unit_isSet = false;
    m_measurement_unit_isValid = false;

    m_modal_type_isSet = false;
    m_modal_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_packaged_height_isSet = false;
    m_packaged_height_isValid = false;

    m_packaged_length_isSet = false;
    m_packaged_length_isValid = false;

    m_packaged_weight_kg_isSet = false;
    m_packaged_weight_kg_isValid = false;

    m_packaged_width_isSet = false;
    m_packaged_width_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_ref_id_isSet = false;
    m_ref_id_isValid = false;

    m_reward_value_isSet = false;
    m_reward_value_isValid = false;

    m_unit_multiplier_isSet = false;
    m_unit_multiplier_isValid = false;

    m_videos_isSet = false;
    m_videos_isValid = false;

    m_weight_kg_isSet = false;
    m_weight_kg_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::fromJsonObject(QJsonObject json) {

    m_activate_if_possible_isValid = ::OpenAPI::fromJsonValue(m_activate_if_possible, json[QString("ActivateIfPossible")]);
    m_activate_if_possible_isSet = !json[QString("ActivateIfPossible")].isNull() && m_activate_if_possible_isValid;

    m_commercial_condition_id_isValid = ::OpenAPI::fromJsonValue(m_commercial_condition_id, json[QString("CommercialConditionId")]);
    m_commercial_condition_id_isSet = !json[QString("CommercialConditionId")].isNull() && m_commercial_condition_id_isValid;

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("CreationDate")]);
    m_creation_date_isSet = !json[QString("CreationDate")].isNull() && m_creation_date_isValid;

    m_cubic_weight_isValid = ::OpenAPI::fromJsonValue(m_cubic_weight, json[QString("CubicWeight")]);
    m_cubic_weight_isSet = !json[QString("CubicWeight")].isNull() && m_cubic_weight_isValid;

    m_ean_isValid = ::OpenAPI::fromJsonValue(m_ean, json[QString("Ean")]);
    m_ean_isSet = !json[QString("Ean")].isNull() && m_ean_isValid;

    m_estimated_date_arrival_isValid = ::OpenAPI::fromJsonValue(m_estimated_date_arrival, json[QString("EstimatedDateArrival")]);
    m_estimated_date_arrival_isSet = !json[QString("EstimatedDateArrival")].isNull() && m_estimated_date_arrival_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("Height")]);
    m_height_isSet = !json[QString("Height")].isNull() && m_height_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_kit_isValid = ::OpenAPI::fromJsonValue(m_is_kit, json[QString("IsKit")]);
    m_is_kit_isSet = !json[QString("IsKit")].isNull() && m_is_kit_isValid;

    m_kit_itens_sell_apart_isValid = ::OpenAPI::fromJsonValue(m_kit_itens_sell_apart, json[QString("KitItensSellApart")]);
    m_kit_itens_sell_apart_isSet = !json[QString("KitItensSellApart")].isNull() && m_kit_itens_sell_apart_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("Length")]);
    m_length_isSet = !json[QString("Length")].isNull() && m_length_isValid;

    m_manufacturer_code_isValid = ::OpenAPI::fromJsonValue(m_manufacturer_code, json[QString("ManufacturerCode")]);
    m_manufacturer_code_isSet = !json[QString("ManufacturerCode")].isNull() && m_manufacturer_code_isValid;

    m_measurement_unit_isValid = ::OpenAPI::fromJsonValue(m_measurement_unit, json[QString("MeasurementUnit")]);
    m_measurement_unit_isSet = !json[QString("MeasurementUnit")].isNull() && m_measurement_unit_isValid;

    m_modal_type_isValid = ::OpenAPI::fromJsonValue(m_modal_type, json[QString("ModalType")]);
    m_modal_type_isSet = !json[QString("ModalType")].isNull() && m_modal_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_packaged_height_isValid = ::OpenAPI::fromJsonValue(m_packaged_height, json[QString("PackagedHeight")]);
    m_packaged_height_isSet = !json[QString("PackagedHeight")].isNull() && m_packaged_height_isValid;

    m_packaged_length_isValid = ::OpenAPI::fromJsonValue(m_packaged_length, json[QString("PackagedLength")]);
    m_packaged_length_isSet = !json[QString("PackagedLength")].isNull() && m_packaged_length_isValid;

    m_packaged_weight_kg_isValid = ::OpenAPI::fromJsonValue(m_packaged_weight_kg, json[QString("PackagedWeightKg")]);
    m_packaged_weight_kg_isSet = !json[QString("PackagedWeightKg")].isNull() && m_packaged_weight_kg_isValid;

    m_packaged_width_isValid = ::OpenAPI::fromJsonValue(m_packaged_width, json[QString("PackagedWidth")]);
    m_packaged_width_isSet = !json[QString("PackagedWidth")].isNull() && m_packaged_width_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("ProductId")]);
    m_product_id_isSet = !json[QString("ProductId")].isNull() && m_product_id_isValid;

    m_ref_id_isValid = ::OpenAPI::fromJsonValue(m_ref_id, json[QString("RefId")]);
    m_ref_id_isSet = !json[QString("RefId")].isNull() && m_ref_id_isValid;

    m_reward_value_isValid = ::OpenAPI::fromJsonValue(m_reward_value, json[QString("RewardValue")]);
    m_reward_value_isSet = !json[QString("RewardValue")].isNull() && m_reward_value_isValid;

    m_unit_multiplier_isValid = ::OpenAPI::fromJsonValue(m_unit_multiplier, json[QString("UnitMultiplier")]);
    m_unit_multiplier_isSet = !json[QString("UnitMultiplier")].isNull() && m_unit_multiplier_isValid;

    m_videos_isValid = ::OpenAPI::fromJsonValue(m_videos, json[QString("Videos")]);
    m_videos_isSet = !json[QString("Videos")].isNull() && m_videos_isValid;

    m_weight_kg_isValid = ::OpenAPI::fromJsonValue(m_weight_kg, json[QString("WeightKg")]);
    m_weight_kg_isSet = !json[QString("WeightKg")].isNull() && m_weight_kg_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("Width")]);
    m_width_isSet = !json[QString("Width")].isNull() && m_width_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_catalog_pvt_stockkeepingunit_post_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_activate_if_possible_isSet) {
        obj.insert(QString("ActivateIfPossible"), ::OpenAPI::toJsonValue(m_activate_if_possible));
    }
    if (m_commercial_condition_id_isSet) {
        obj.insert(QString("CommercialConditionId"), ::OpenAPI::toJsonValue(m_commercial_condition_id));
    }
    if (m_creation_date_isSet) {
        obj.insert(QString("CreationDate"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_cubic_weight_isSet) {
        obj.insert(QString("CubicWeight"), ::OpenAPI::toJsonValue(m_cubic_weight));
    }
    if (m_ean_isSet) {
        obj.insert(QString("Ean"), ::OpenAPI::toJsonValue(m_ean));
    }
    if (m_estimated_date_arrival_isSet) {
        obj.insert(QString("EstimatedDateArrival"), ::OpenAPI::toJsonValue(m_estimated_date_arrival));
    }
    if (m_height_isSet) {
        obj.insert(QString("Height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_kit_isSet) {
        obj.insert(QString("IsKit"), ::OpenAPI::toJsonValue(m_is_kit));
    }
    if (m_kit_itens_sell_apart_isSet) {
        obj.insert(QString("KitItensSellApart"), ::OpenAPI::toJsonValue(m_kit_itens_sell_apart));
    }
    if (m_length_isSet) {
        obj.insert(QString("Length"), ::OpenAPI::toJsonValue(m_length));
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
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_packaged_height_isSet) {
        obj.insert(QString("PackagedHeight"), ::OpenAPI::toJsonValue(m_packaged_height));
    }
    if (m_packaged_length_isSet) {
        obj.insert(QString("PackagedLength"), ::OpenAPI::toJsonValue(m_packaged_length));
    }
    if (m_packaged_weight_kg_isSet) {
        obj.insert(QString("PackagedWeightKg"), ::OpenAPI::toJsonValue(m_packaged_weight_kg));
    }
    if (m_packaged_width_isSet) {
        obj.insert(QString("PackagedWidth"), ::OpenAPI::toJsonValue(m_packaged_width));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("ProductId"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_ref_id_isSet) {
        obj.insert(QString("RefId"), ::OpenAPI::toJsonValue(m_ref_id));
    }
    if (m_reward_value_isSet) {
        obj.insert(QString("RewardValue"), ::OpenAPI::toJsonValue(m_reward_value));
    }
    if (m_unit_multiplier_isSet) {
        obj.insert(QString("UnitMultiplier"), ::OpenAPI::toJsonValue(m_unit_multiplier));
    }
    if (m_videos.size() > 0) {
        obj.insert(QString("Videos"), ::OpenAPI::toJsonValue(m_videos));
    }
    if (m_weight_kg_isSet) {
        obj.insert(QString("WeightKg"), ::OpenAPI::toJsonValue(m_weight_kg));
    }
    if (m_width_isSet) {
        obj.insert(QString("Width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::isActivateIfPossible() const {
    return m_activate_if_possible;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setActivateIfPossible(const bool &activate_if_possible) {
    m_activate_if_possible = activate_if_possible;
    m_activate_if_possible_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_activate_if_possible_Set() const{
    return m_activate_if_possible_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_activate_if_possible_Valid() const{
    return m_activate_if_possible_isValid;
}

qint32 OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getCommercialConditionId() const {
    return m_commercial_condition_id;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setCommercialConditionId(const qint32 &commercial_condition_id) {
    m_commercial_condition_id = commercial_condition_id;
    m_commercial_condition_id_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_commercial_condition_id_Set() const{
    return m_commercial_condition_id_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_commercial_condition_id_Valid() const{
    return m_commercial_condition_id_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getCreationDate() const {
    return m_creation_date;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setCreationDate(const QString &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getCubicWeight() const {
    return m_cubic_weight;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setCubicWeight(const double &cubic_weight) {
    m_cubic_weight = cubic_weight;
    m_cubic_weight_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_cubic_weight_Set() const{
    return m_cubic_weight_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_cubic_weight_Valid() const{
    return m_cubic_weight_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getEan() const {
    return m_ean;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setEan(const QString &ean) {
    m_ean = ean;
    m_ean_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_ean_Set() const{
    return m_ean_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_ean_Valid() const{
    return m_ean_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getEstimatedDateArrival() const {
    return m_estimated_date_arrival;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setEstimatedDateArrival(const QString &estimated_date_arrival) {
    m_estimated_date_arrival = estimated_date_arrival;
    m_estimated_date_arrival_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_estimated_date_arrival_Set() const{
    return m_estimated_date_arrival_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_estimated_date_arrival_Valid() const{
    return m_estimated_date_arrival_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getHeight() const {
    return m_height;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setHeight(const double &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_height_Set() const{
    return m_height_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_height_Valid() const{
    return m_height_isValid;
}

qint32 OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getId() const {
    return m_id;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_id_Valid() const{
    return m_id_isValid;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::isIsActive() const {
    return m_is_active;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::isIsKit() const {
    return m_is_kit;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setIsKit(const bool &is_kit) {
    m_is_kit = is_kit;
    m_is_kit_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_is_kit_Set() const{
    return m_is_kit_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_is_kit_Valid() const{
    return m_is_kit_isValid;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::isKitItensSellApart() const {
    return m_kit_itens_sell_apart;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setKitItensSellApart(const bool &kit_itens_sell_apart) {
    m_kit_itens_sell_apart = kit_itens_sell_apart;
    m_kit_itens_sell_apart_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_kit_itens_sell_apart_Set() const{
    return m_kit_itens_sell_apart_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_kit_itens_sell_apart_Valid() const{
    return m_kit_itens_sell_apart_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getLength() const {
    return m_length;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setLength(const double &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_length_Set() const{
    return m_length_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_length_Valid() const{
    return m_length_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getManufacturerCode() const {
    return m_manufacturer_code;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setManufacturerCode(const QString &manufacturer_code) {
    m_manufacturer_code = manufacturer_code;
    m_manufacturer_code_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_manufacturer_code_Set() const{
    return m_manufacturer_code_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_manufacturer_code_Valid() const{
    return m_manufacturer_code_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getMeasurementUnit() const {
    return m_measurement_unit;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setMeasurementUnit(const QString &measurement_unit) {
    m_measurement_unit = measurement_unit;
    m_measurement_unit_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_measurement_unit_Set() const{
    return m_measurement_unit_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_measurement_unit_Valid() const{
    return m_measurement_unit_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getModalType() const {
    return m_modal_type;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setModalType(const QString &modal_type) {
    m_modal_type = modal_type;
    m_modal_type_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_modal_type_Set() const{
    return m_modal_type_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_modal_type_Valid() const{
    return m_modal_type_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getName() const {
    return m_name;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_name_Valid() const{
    return m_name_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getPackagedHeight() const {
    return m_packaged_height;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setPackagedHeight(const double &packaged_height) {
    m_packaged_height = packaged_height;
    m_packaged_height_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_height_Set() const{
    return m_packaged_height_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_height_Valid() const{
    return m_packaged_height_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getPackagedLength() const {
    return m_packaged_length;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setPackagedLength(const double &packaged_length) {
    m_packaged_length = packaged_length;
    m_packaged_length_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_length_Set() const{
    return m_packaged_length_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_length_Valid() const{
    return m_packaged_length_isValid;
}

qint32 OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getPackagedWeightKg() const {
    return m_packaged_weight_kg;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setPackagedWeightKg(const qint32 &packaged_weight_kg) {
    m_packaged_weight_kg = packaged_weight_kg;
    m_packaged_weight_kg_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_weight_kg_Set() const{
    return m_packaged_weight_kg_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_weight_kg_Valid() const{
    return m_packaged_weight_kg_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getPackagedWidth() const {
    return m_packaged_width;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setPackagedWidth(const double &packaged_width) {
    m_packaged_width = packaged_width;
    m_packaged_width_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_width_Set() const{
    return m_packaged_width_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_packaged_width_Valid() const{
    return m_packaged_width_isValid;
}

qint32 OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getProductId() const {
    return m_product_id;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setProductId(const qint32 &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_product_id_Valid() const{
    return m_product_id_isValid;
}

QString OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getRefId() const {
    return m_ref_id;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setRefId(const QString &ref_id) {
    m_ref_id = ref_id;
    m_ref_id_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_ref_id_Set() const{
    return m_ref_id_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_ref_id_Valid() const{
    return m_ref_id_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getRewardValue() const {
    return m_reward_value;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setRewardValue(const double &reward_value) {
    m_reward_value = reward_value;
    m_reward_value_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_reward_value_Set() const{
    return m_reward_value_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_reward_value_Valid() const{
    return m_reward_value_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getUnitMultiplier() const {
    return m_unit_multiplier;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setUnitMultiplier(const double &unit_multiplier) {
    m_unit_multiplier = unit_multiplier;
    m_unit_multiplier_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_unit_multiplier_Set() const{
    return m_unit_multiplier_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_unit_multiplier_Valid() const{
    return m_unit_multiplier_isValid;
}

QList<QString> OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getVideos() const {
    return m_videos;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setVideos(const QList<QString> &videos) {
    m_videos = videos;
    m_videos_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_videos_Set() const{
    return m_videos_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_videos_Valid() const{
    return m_videos_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getWeightKg() const {
    return m_weight_kg;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setWeightKg(const double &weight_kg) {
    m_weight_kg = weight_kg;
    m_weight_kg_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_weight_kg_Set() const{
    return m_weight_kg_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_weight_kg_Valid() const{
    return m_weight_kg_isValid;
}

double OAI_api_catalog_pvt_stockkeepingunit_post_200_response::getWidth() const {
    return m_width;
}
void OAI_api_catalog_pvt_stockkeepingunit_post_200_response::setWidth(const double &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_width_Set() const{
    return m_width_isSet;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::is_width_Valid() const{
    return m_width_isValid;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_activate_if_possible_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_commercial_condition_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cubic_weight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ean_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_estimated_date_arrival_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
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

        if (m_is_kit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kit_itens_sell_apart_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
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

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_packaged_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_packaged_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_packaged_weight_kg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_packaged_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ref_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reward_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_multiplier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_videos.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_weight_kg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_api_catalog_pvt_stockkeepingunit_post_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
