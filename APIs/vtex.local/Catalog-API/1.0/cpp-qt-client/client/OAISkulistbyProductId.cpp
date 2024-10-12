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

#include "OAISkulistbyProductId.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISkulistbyProductId::OAISkulistbyProductId(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISkulistbyProductId::OAISkulistbyProductId() {
    this->initializeModel();
}

OAISkulistbyProductId::~OAISkulistbyProductId() {}

void OAISkulistbyProductId::initializeModel() {

    m_activate_if_possible_isSet = false;
    m_activate_if_possible_isValid = false;

    m_commercial_condition_id_isSet = false;
    m_commercial_condition_id_isValid = false;

    m_cubic_weight_isSet = false;
    m_cubic_weight_isValid = false;

    m_date_updated_isSet = false;
    m_date_updated_isValid = false;

    m_estimated_date_arrival_isSet = false;
    m_estimated_date_arrival_isValid = false;

    m_flag_kit_itens_sell_apart_isSet = false;
    m_flag_kit_itens_sell_apart_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_internal_note_isSet = false;
    m_internal_note_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_dynamic_kit_isSet = false;
    m_is_dynamic_kit_isValid = false;

    m_is_gift_card_recharge_isSet = false;
    m_is_gift_card_recharge_isValid = false;

    m_is_inventoried_isSet = false;
    m_is_inventoried_isValid = false;

    m_is_kit_isSet = false;
    m_is_kit_isValid = false;

    m_is_persisted_isSet = false;
    m_is_persisted_isValid = false;

    m_is_removed_isSet = false;
    m_is_removed_isValid = false;

    m_is_transported_isSet = false;
    m_is_transported_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_manufacturer_code_isSet = false;
    m_manufacturer_code_isValid = false;

    m_measurement_unit_isSet = false;
    m_measurement_unit_isValid = false;

    m_modal_id_isSet = false;
    m_modal_id_isValid = false;

    m_modal_type_isSet = false;
    m_modal_type_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_real_height_isSet = false;
    m_real_height_isValid = false;

    m_real_length_isSet = false;
    m_real_length_isValid = false;

    m_real_weight_kg_isSet = false;
    m_real_weight_kg_isValid = false;

    m_real_width_isSet = false;
    m_real_width_isValid = false;

    m_ref_id_isSet = false;
    m_ref_id_isValid = false;

    m_reference_stock_keeping_unit_id_isSet = false;
    m_reference_stock_keeping_unit_id_isValid = false;

    m_reward_value_isSet = false;
    m_reward_value_isValid = false;

    m_unit_multiplier_isSet = false;
    m_unit_multiplier_isValid = false;

    m_weight_kg_isSet = false;
    m_weight_kg_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;

    m_is_kit_optimized_isSet = false;
    m_is_kit_optimized_isValid = false;
}

void OAISkulistbyProductId::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISkulistbyProductId::fromJsonObject(QJsonObject json) {

    m_activate_if_possible_isValid = ::OpenAPI::fromJsonValue(m_activate_if_possible, json[QString("ActivateIfPossible")]);
    m_activate_if_possible_isSet = !json[QString("ActivateIfPossible")].isNull() && m_activate_if_possible_isValid;

    m_commercial_condition_id_isValid = ::OpenAPI::fromJsonValue(m_commercial_condition_id, json[QString("CommercialConditionId")]);
    m_commercial_condition_id_isSet = !json[QString("CommercialConditionId")].isNull() && m_commercial_condition_id_isValid;

    m_cubic_weight_isValid = ::OpenAPI::fromJsonValue(m_cubic_weight, json[QString("CubicWeight")]);
    m_cubic_weight_isSet = !json[QString("CubicWeight")].isNull() && m_cubic_weight_isValid;

    m_date_updated_isValid = ::OpenAPI::fromJsonValue(m_date_updated, json[QString("DateUpdated")]);
    m_date_updated_isSet = !json[QString("DateUpdated")].isNull() && m_date_updated_isValid;

    m_estimated_date_arrival_isValid = ::OpenAPI::fromJsonValue(m_estimated_date_arrival, json[QString("EstimatedDateArrival")]);
    m_estimated_date_arrival_isSet = !json[QString("EstimatedDateArrival")].isNull() && m_estimated_date_arrival_isValid;

    m_flag_kit_itens_sell_apart_isValid = ::OpenAPI::fromJsonValue(m_flag_kit_itens_sell_apart, json[QString("FlagKitItensSellApart")]);
    m_flag_kit_itens_sell_apart_isSet = !json[QString("FlagKitItensSellApart")].isNull() && m_flag_kit_itens_sell_apart_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("Height")]);
    m_height_isSet = !json[QString("Height")].isNull() && m_height_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_internal_note_isValid = ::OpenAPI::fromJsonValue(m_internal_note, json[QString("InternalNote")]);
    m_internal_note_isSet = !json[QString("InternalNote")].isNull() && m_internal_note_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_dynamic_kit_isValid = ::OpenAPI::fromJsonValue(m_is_dynamic_kit, json[QString("IsDynamicKit")]);
    m_is_dynamic_kit_isSet = !json[QString("IsDynamicKit")].isNull() && m_is_dynamic_kit_isValid;

    m_is_gift_card_recharge_isValid = ::OpenAPI::fromJsonValue(m_is_gift_card_recharge, json[QString("IsGiftCardRecharge")]);
    m_is_gift_card_recharge_isSet = !json[QString("IsGiftCardRecharge")].isNull() && m_is_gift_card_recharge_isValid;

    m_is_inventoried_isValid = ::OpenAPI::fromJsonValue(m_is_inventoried, json[QString("IsInventoried")]);
    m_is_inventoried_isSet = !json[QString("IsInventoried")].isNull() && m_is_inventoried_isValid;

    m_is_kit_isValid = ::OpenAPI::fromJsonValue(m_is_kit, json[QString("IsKit")]);
    m_is_kit_isSet = !json[QString("IsKit")].isNull() && m_is_kit_isValid;

    m_is_persisted_isValid = ::OpenAPI::fromJsonValue(m_is_persisted, json[QString("IsPersisted")]);
    m_is_persisted_isSet = !json[QString("IsPersisted")].isNull() && m_is_persisted_isValid;

    m_is_removed_isValid = ::OpenAPI::fromJsonValue(m_is_removed, json[QString("IsRemoved")]);
    m_is_removed_isSet = !json[QString("IsRemoved")].isNull() && m_is_removed_isValid;

    m_is_transported_isValid = ::OpenAPI::fromJsonValue(m_is_transported, json[QString("IsTransported")]);
    m_is_transported_isSet = !json[QString("IsTransported")].isNull() && m_is_transported_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("Length")]);
    m_length_isSet = !json[QString("Length")].isNull() && m_length_isValid;

    m_manufacturer_code_isValid = ::OpenAPI::fromJsonValue(m_manufacturer_code, json[QString("ManufacturerCode")]);
    m_manufacturer_code_isSet = !json[QString("ManufacturerCode")].isNull() && m_manufacturer_code_isValid;

    m_measurement_unit_isValid = ::OpenAPI::fromJsonValue(m_measurement_unit, json[QString("MeasurementUnit")]);
    m_measurement_unit_isSet = !json[QString("MeasurementUnit")].isNull() && m_measurement_unit_isValid;

    m_modal_id_isValid = ::OpenAPI::fromJsonValue(m_modal_id, json[QString("ModalId")]);
    m_modal_id_isSet = !json[QString("ModalId")].isNull() && m_modal_id_isValid;

    m_modal_type_isValid = ::OpenAPI::fromJsonValue(m_modal_type, json[QString("ModalType")]);
    m_modal_type_isSet = !json[QString("ModalType")].isNull() && m_modal_type_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("Position")]);
    m_position_isSet = !json[QString("Position")].isNull() && m_position_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("ProductId")]);
    m_product_id_isSet = !json[QString("ProductId")].isNull() && m_product_id_isValid;

    m_real_height_isValid = ::OpenAPI::fromJsonValue(m_real_height, json[QString("RealHeight")]);
    m_real_height_isSet = !json[QString("RealHeight")].isNull() && m_real_height_isValid;

    m_real_length_isValid = ::OpenAPI::fromJsonValue(m_real_length, json[QString("RealLength")]);
    m_real_length_isSet = !json[QString("RealLength")].isNull() && m_real_length_isValid;

    m_real_weight_kg_isValid = ::OpenAPI::fromJsonValue(m_real_weight_kg, json[QString("RealWeightKg")]);
    m_real_weight_kg_isSet = !json[QString("RealWeightKg")].isNull() && m_real_weight_kg_isValid;

    m_real_width_isValid = ::OpenAPI::fromJsonValue(m_real_width, json[QString("RealWidth")]);
    m_real_width_isSet = !json[QString("RealWidth")].isNull() && m_real_width_isValid;

    m_ref_id_isValid = ::OpenAPI::fromJsonValue(m_ref_id, json[QString("RefId")]);
    m_ref_id_isSet = !json[QString("RefId")].isNull() && m_ref_id_isValid;

    m_reference_stock_keeping_unit_id_isValid = ::OpenAPI::fromJsonValue(m_reference_stock_keeping_unit_id, json[QString("ReferenceStockKeepingUnitId")]);
    m_reference_stock_keeping_unit_id_isSet = !json[QString("ReferenceStockKeepingUnitId")].isNull() && m_reference_stock_keeping_unit_id_isValid;

    m_reward_value_isValid = ::OpenAPI::fromJsonValue(m_reward_value, json[QString("RewardValue")]);
    m_reward_value_isSet = !json[QString("RewardValue")].isNull() && m_reward_value_isValid;

    m_unit_multiplier_isValid = ::OpenAPI::fromJsonValue(m_unit_multiplier, json[QString("UnitMultiplier")]);
    m_unit_multiplier_isSet = !json[QString("UnitMultiplier")].isNull() && m_unit_multiplier_isValid;

    m_weight_kg_isValid = ::OpenAPI::fromJsonValue(m_weight_kg, json[QString("WeightKg")]);
    m_weight_kg_isSet = !json[QString("WeightKg")].isNull() && m_weight_kg_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("Width")]);
    m_width_isSet = !json[QString("Width")].isNull() && m_width_isValid;

    m_is_kit_optimized_isValid = ::OpenAPI::fromJsonValue(m_is_kit_optimized, json[QString("isKitOptimized")]);
    m_is_kit_optimized_isSet = !json[QString("isKitOptimized")].isNull() && m_is_kit_optimized_isValid;
}

QString OAISkulistbyProductId::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISkulistbyProductId::asJsonObject() const {
    QJsonObject obj;
    if (m_activate_if_possible_isSet) {
        obj.insert(QString("ActivateIfPossible"), ::OpenAPI::toJsonValue(m_activate_if_possible));
    }
    if (m_commercial_condition_id_isSet) {
        obj.insert(QString("CommercialConditionId"), ::OpenAPI::toJsonValue(m_commercial_condition_id));
    }
    if (m_cubic_weight_isSet) {
        obj.insert(QString("CubicWeight"), ::OpenAPI::toJsonValue(m_cubic_weight));
    }
    if (m_date_updated_isSet) {
        obj.insert(QString("DateUpdated"), ::OpenAPI::toJsonValue(m_date_updated));
    }
    if (m_estimated_date_arrival_isSet) {
        obj.insert(QString("EstimatedDateArrival"), ::OpenAPI::toJsonValue(m_estimated_date_arrival));
    }
    if (m_flag_kit_itens_sell_apart_isSet) {
        obj.insert(QString("FlagKitItensSellApart"), ::OpenAPI::toJsonValue(m_flag_kit_itens_sell_apart));
    }
    if (m_height_isSet) {
        obj.insert(QString("Height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_internal_note_isSet) {
        obj.insert(QString("InternalNote"), ::OpenAPI::toJsonValue(m_internal_note));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_dynamic_kit_isSet) {
        obj.insert(QString("IsDynamicKit"), ::OpenAPI::toJsonValue(m_is_dynamic_kit));
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
    if (m_is_persisted_isSet) {
        obj.insert(QString("IsPersisted"), ::OpenAPI::toJsonValue(m_is_persisted));
    }
    if (m_is_removed_isSet) {
        obj.insert(QString("IsRemoved"), ::OpenAPI::toJsonValue(m_is_removed));
    }
    if (m_is_transported_isSet) {
        obj.insert(QString("IsTransported"), ::OpenAPI::toJsonValue(m_is_transported));
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
    if (m_modal_id_isSet) {
        obj.insert(QString("ModalId"), ::OpenAPI::toJsonValue(m_modal_id));
    }
    if (m_modal_type_isSet) {
        obj.insert(QString("ModalType"), ::OpenAPI::toJsonValue(m_modal_type));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_position_isSet) {
        obj.insert(QString("Position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("ProductId"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_real_height_isSet) {
        obj.insert(QString("RealHeight"), ::OpenAPI::toJsonValue(m_real_height));
    }
    if (m_real_length_isSet) {
        obj.insert(QString("RealLength"), ::OpenAPI::toJsonValue(m_real_length));
    }
    if (m_real_weight_kg_isSet) {
        obj.insert(QString("RealWeightKg"), ::OpenAPI::toJsonValue(m_real_weight_kg));
    }
    if (m_real_width_isSet) {
        obj.insert(QString("RealWidth"), ::OpenAPI::toJsonValue(m_real_width));
    }
    if (m_ref_id_isSet) {
        obj.insert(QString("RefId"), ::OpenAPI::toJsonValue(m_ref_id));
    }
    if (m_reference_stock_keeping_unit_id_isSet) {
        obj.insert(QString("ReferenceStockKeepingUnitId"), ::OpenAPI::toJsonValue(m_reference_stock_keeping_unit_id));
    }
    if (m_reward_value_isSet) {
        obj.insert(QString("RewardValue"), ::OpenAPI::toJsonValue(m_reward_value));
    }
    if (m_unit_multiplier_isSet) {
        obj.insert(QString("UnitMultiplier"), ::OpenAPI::toJsonValue(m_unit_multiplier));
    }
    if (m_weight_kg_isSet) {
        obj.insert(QString("WeightKg"), ::OpenAPI::toJsonValue(m_weight_kg));
    }
    if (m_width_isSet) {
        obj.insert(QString("Width"), ::OpenAPI::toJsonValue(m_width));
    }
    if (m_is_kit_optimized_isSet) {
        obj.insert(QString("isKitOptimized"), ::OpenAPI::toJsonValue(m_is_kit_optimized));
    }
    return obj;
}

bool OAISkulistbyProductId::isActivateIfPossible() const {
    return m_activate_if_possible;
}
void OAISkulistbyProductId::setActivateIfPossible(const bool &activate_if_possible) {
    m_activate_if_possible = activate_if_possible;
    m_activate_if_possible_isSet = true;
}

bool OAISkulistbyProductId::is_activate_if_possible_Set() const{
    return m_activate_if_possible_isSet;
}

bool OAISkulistbyProductId::is_activate_if_possible_Valid() const{
    return m_activate_if_possible_isValid;
}

qint32 OAISkulistbyProductId::getCommercialConditionId() const {
    return m_commercial_condition_id;
}
void OAISkulistbyProductId::setCommercialConditionId(const qint32 &commercial_condition_id) {
    m_commercial_condition_id = commercial_condition_id;
    m_commercial_condition_id_isSet = true;
}

bool OAISkulistbyProductId::is_commercial_condition_id_Set() const{
    return m_commercial_condition_id_isSet;
}

bool OAISkulistbyProductId::is_commercial_condition_id_Valid() const{
    return m_commercial_condition_id_isValid;
}

double OAISkulistbyProductId::getCubicWeight() const {
    return m_cubic_weight;
}
void OAISkulistbyProductId::setCubicWeight(const double &cubic_weight) {
    m_cubic_weight = cubic_weight;
    m_cubic_weight_isSet = true;
}

bool OAISkulistbyProductId::is_cubic_weight_Set() const{
    return m_cubic_weight_isSet;
}

bool OAISkulistbyProductId::is_cubic_weight_Valid() const{
    return m_cubic_weight_isValid;
}

QString OAISkulistbyProductId::getDateUpdated() const {
    return m_date_updated;
}
void OAISkulistbyProductId::setDateUpdated(const QString &date_updated) {
    m_date_updated = date_updated;
    m_date_updated_isSet = true;
}

bool OAISkulistbyProductId::is_date_updated_Set() const{
    return m_date_updated_isSet;
}

bool OAISkulistbyProductId::is_date_updated_Valid() const{
    return m_date_updated_isValid;
}

QString OAISkulistbyProductId::getEstimatedDateArrival() const {
    return m_estimated_date_arrival;
}
void OAISkulistbyProductId::setEstimatedDateArrival(const QString &estimated_date_arrival) {
    m_estimated_date_arrival = estimated_date_arrival;
    m_estimated_date_arrival_isSet = true;
}

bool OAISkulistbyProductId::is_estimated_date_arrival_Set() const{
    return m_estimated_date_arrival_isSet;
}

bool OAISkulistbyProductId::is_estimated_date_arrival_Valid() const{
    return m_estimated_date_arrival_isValid;
}

bool OAISkulistbyProductId::isFlagKitItensSellApart() const {
    return m_flag_kit_itens_sell_apart;
}
void OAISkulistbyProductId::setFlagKitItensSellApart(const bool &flag_kit_itens_sell_apart) {
    m_flag_kit_itens_sell_apart = flag_kit_itens_sell_apart;
    m_flag_kit_itens_sell_apart_isSet = true;
}

bool OAISkulistbyProductId::is_flag_kit_itens_sell_apart_Set() const{
    return m_flag_kit_itens_sell_apart_isSet;
}

bool OAISkulistbyProductId::is_flag_kit_itens_sell_apart_Valid() const{
    return m_flag_kit_itens_sell_apart_isValid;
}

double OAISkulistbyProductId::getHeight() const {
    return m_height;
}
void OAISkulistbyProductId::setHeight(const double &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAISkulistbyProductId::is_height_Set() const{
    return m_height_isSet;
}

bool OAISkulistbyProductId::is_height_Valid() const{
    return m_height_isValid;
}

qint32 OAISkulistbyProductId::getId() const {
    return m_id;
}
void OAISkulistbyProductId::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISkulistbyProductId::is_id_Set() const{
    return m_id_isSet;
}

bool OAISkulistbyProductId::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISkulistbyProductId::getInternalNote() const {
    return m_internal_note;
}
void OAISkulistbyProductId::setInternalNote(const QString &internal_note) {
    m_internal_note = internal_note;
    m_internal_note_isSet = true;
}

bool OAISkulistbyProductId::is_internal_note_Set() const{
    return m_internal_note_isSet;
}

bool OAISkulistbyProductId::is_internal_note_Valid() const{
    return m_internal_note_isValid;
}

bool OAISkulistbyProductId::isIsActive() const {
    return m_is_active;
}
void OAISkulistbyProductId::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAISkulistbyProductId::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAISkulistbyProductId::is_is_active_Valid() const{
    return m_is_active_isValid;
}

QString OAISkulistbyProductId::getIsDynamicKit() const {
    return m_is_dynamic_kit;
}
void OAISkulistbyProductId::setIsDynamicKit(const QString &is_dynamic_kit) {
    m_is_dynamic_kit = is_dynamic_kit;
    m_is_dynamic_kit_isSet = true;
}

bool OAISkulistbyProductId::is_is_dynamic_kit_Set() const{
    return m_is_dynamic_kit_isSet;
}

bool OAISkulistbyProductId::is_is_dynamic_kit_Valid() const{
    return m_is_dynamic_kit_isValid;
}

bool OAISkulistbyProductId::isIsGiftCardRecharge() const {
    return m_is_gift_card_recharge;
}
void OAISkulistbyProductId::setIsGiftCardRecharge(const bool &is_gift_card_recharge) {
    m_is_gift_card_recharge = is_gift_card_recharge;
    m_is_gift_card_recharge_isSet = true;
}

bool OAISkulistbyProductId::is_is_gift_card_recharge_Set() const{
    return m_is_gift_card_recharge_isSet;
}

bool OAISkulistbyProductId::is_is_gift_card_recharge_Valid() const{
    return m_is_gift_card_recharge_isValid;
}

bool OAISkulistbyProductId::isIsInventoried() const {
    return m_is_inventoried;
}
void OAISkulistbyProductId::setIsInventoried(const bool &is_inventoried) {
    m_is_inventoried = is_inventoried;
    m_is_inventoried_isSet = true;
}

bool OAISkulistbyProductId::is_is_inventoried_Set() const{
    return m_is_inventoried_isSet;
}

bool OAISkulistbyProductId::is_is_inventoried_Valid() const{
    return m_is_inventoried_isValid;
}

bool OAISkulistbyProductId::isIsKit() const {
    return m_is_kit;
}
void OAISkulistbyProductId::setIsKit(const bool &is_kit) {
    m_is_kit = is_kit;
    m_is_kit_isSet = true;
}

bool OAISkulistbyProductId::is_is_kit_Set() const{
    return m_is_kit_isSet;
}

bool OAISkulistbyProductId::is_is_kit_Valid() const{
    return m_is_kit_isValid;
}

bool OAISkulistbyProductId::isIsPersisted() const {
    return m_is_persisted;
}
void OAISkulistbyProductId::setIsPersisted(const bool &is_persisted) {
    m_is_persisted = is_persisted;
    m_is_persisted_isSet = true;
}

bool OAISkulistbyProductId::is_is_persisted_Set() const{
    return m_is_persisted_isSet;
}

bool OAISkulistbyProductId::is_is_persisted_Valid() const{
    return m_is_persisted_isValid;
}

bool OAISkulistbyProductId::isIsRemoved() const {
    return m_is_removed;
}
void OAISkulistbyProductId::setIsRemoved(const bool &is_removed) {
    m_is_removed = is_removed;
    m_is_removed_isSet = true;
}

bool OAISkulistbyProductId::is_is_removed_Set() const{
    return m_is_removed_isSet;
}

bool OAISkulistbyProductId::is_is_removed_Valid() const{
    return m_is_removed_isValid;
}

bool OAISkulistbyProductId::isIsTransported() const {
    return m_is_transported;
}
void OAISkulistbyProductId::setIsTransported(const bool &is_transported) {
    m_is_transported = is_transported;
    m_is_transported_isSet = true;
}

bool OAISkulistbyProductId::is_is_transported_Set() const{
    return m_is_transported_isSet;
}

bool OAISkulistbyProductId::is_is_transported_Valid() const{
    return m_is_transported_isValid;
}

double OAISkulistbyProductId::getLength() const {
    return m_length;
}
void OAISkulistbyProductId::setLength(const double &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAISkulistbyProductId::is_length_Set() const{
    return m_length_isSet;
}

bool OAISkulistbyProductId::is_length_Valid() const{
    return m_length_isValid;
}

QString OAISkulistbyProductId::getManufacturerCode() const {
    return m_manufacturer_code;
}
void OAISkulistbyProductId::setManufacturerCode(const QString &manufacturer_code) {
    m_manufacturer_code = manufacturer_code;
    m_manufacturer_code_isSet = true;
}

bool OAISkulistbyProductId::is_manufacturer_code_Set() const{
    return m_manufacturer_code_isSet;
}

bool OAISkulistbyProductId::is_manufacturer_code_Valid() const{
    return m_manufacturer_code_isValid;
}

QString OAISkulistbyProductId::getMeasurementUnit() const {
    return m_measurement_unit;
}
void OAISkulistbyProductId::setMeasurementUnit(const QString &measurement_unit) {
    m_measurement_unit = measurement_unit;
    m_measurement_unit_isSet = true;
}

bool OAISkulistbyProductId::is_measurement_unit_Set() const{
    return m_measurement_unit_isSet;
}

bool OAISkulistbyProductId::is_measurement_unit_Valid() const{
    return m_measurement_unit_isValid;
}

qint32 OAISkulistbyProductId::getModalId() const {
    return m_modal_id;
}
void OAISkulistbyProductId::setModalId(const qint32 &modal_id) {
    m_modal_id = modal_id;
    m_modal_id_isSet = true;
}

bool OAISkulistbyProductId::is_modal_id_Set() const{
    return m_modal_id_isSet;
}

bool OAISkulistbyProductId::is_modal_id_Valid() const{
    return m_modal_id_isValid;
}

QString OAISkulistbyProductId::getModalType() const {
    return m_modal_type;
}
void OAISkulistbyProductId::setModalType(const QString &modal_type) {
    m_modal_type = modal_type;
    m_modal_type_isSet = true;
}

bool OAISkulistbyProductId::is_modal_type_Set() const{
    return m_modal_type_isSet;
}

bool OAISkulistbyProductId::is_modal_type_Valid() const{
    return m_modal_type_isValid;
}

QString OAISkulistbyProductId::getName() const {
    return m_name;
}
void OAISkulistbyProductId::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISkulistbyProductId::is_name_Set() const{
    return m_name_isSet;
}

bool OAISkulistbyProductId::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAISkulistbyProductId::getPosition() const {
    return m_position;
}
void OAISkulistbyProductId::setPosition(const qint32 &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAISkulistbyProductId::is_position_Set() const{
    return m_position_isSet;
}

bool OAISkulistbyProductId::is_position_Valid() const{
    return m_position_isValid;
}

qint32 OAISkulistbyProductId::getProductId() const {
    return m_product_id;
}
void OAISkulistbyProductId::setProductId(const qint32 &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAISkulistbyProductId::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAISkulistbyProductId::is_product_id_Valid() const{
    return m_product_id_isValid;
}

double OAISkulistbyProductId::getRealHeight() const {
    return m_real_height;
}
void OAISkulistbyProductId::setRealHeight(const double &real_height) {
    m_real_height = real_height;
    m_real_height_isSet = true;
}

bool OAISkulistbyProductId::is_real_height_Set() const{
    return m_real_height_isSet;
}

bool OAISkulistbyProductId::is_real_height_Valid() const{
    return m_real_height_isValid;
}

double OAISkulistbyProductId::getRealLength() const {
    return m_real_length;
}
void OAISkulistbyProductId::setRealLength(const double &real_length) {
    m_real_length = real_length;
    m_real_length_isSet = true;
}

bool OAISkulistbyProductId::is_real_length_Set() const{
    return m_real_length_isSet;
}

bool OAISkulistbyProductId::is_real_length_Valid() const{
    return m_real_length_isValid;
}

double OAISkulistbyProductId::getRealWeightKg() const {
    return m_real_weight_kg;
}
void OAISkulistbyProductId::setRealWeightKg(const double &real_weight_kg) {
    m_real_weight_kg = real_weight_kg;
    m_real_weight_kg_isSet = true;
}

bool OAISkulistbyProductId::is_real_weight_kg_Set() const{
    return m_real_weight_kg_isSet;
}

bool OAISkulistbyProductId::is_real_weight_kg_Valid() const{
    return m_real_weight_kg_isValid;
}

double OAISkulistbyProductId::getRealWidth() const {
    return m_real_width;
}
void OAISkulistbyProductId::setRealWidth(const double &real_width) {
    m_real_width = real_width;
    m_real_width_isSet = true;
}

bool OAISkulistbyProductId::is_real_width_Set() const{
    return m_real_width_isSet;
}

bool OAISkulistbyProductId::is_real_width_Valid() const{
    return m_real_width_isValid;
}

QString OAISkulistbyProductId::getRefId() const {
    return m_ref_id;
}
void OAISkulistbyProductId::setRefId(const QString &ref_id) {
    m_ref_id = ref_id;
    m_ref_id_isSet = true;
}

bool OAISkulistbyProductId::is_ref_id_Set() const{
    return m_ref_id_isSet;
}

bool OAISkulistbyProductId::is_ref_id_Valid() const{
    return m_ref_id_isValid;
}

QString OAISkulistbyProductId::getReferenceStockKeepingUnitId() const {
    return m_reference_stock_keeping_unit_id;
}
void OAISkulistbyProductId::setReferenceStockKeepingUnitId(const QString &reference_stock_keeping_unit_id) {
    m_reference_stock_keeping_unit_id = reference_stock_keeping_unit_id;
    m_reference_stock_keeping_unit_id_isSet = true;
}

bool OAISkulistbyProductId::is_reference_stock_keeping_unit_id_Set() const{
    return m_reference_stock_keeping_unit_id_isSet;
}

bool OAISkulistbyProductId::is_reference_stock_keeping_unit_id_Valid() const{
    return m_reference_stock_keeping_unit_id_isValid;
}

double OAISkulistbyProductId::getRewardValue() const {
    return m_reward_value;
}
void OAISkulistbyProductId::setRewardValue(const double &reward_value) {
    m_reward_value = reward_value;
    m_reward_value_isSet = true;
}

bool OAISkulistbyProductId::is_reward_value_Set() const{
    return m_reward_value_isSet;
}

bool OAISkulistbyProductId::is_reward_value_Valid() const{
    return m_reward_value_isValid;
}

double OAISkulistbyProductId::getUnitMultiplier() const {
    return m_unit_multiplier;
}
void OAISkulistbyProductId::setUnitMultiplier(const double &unit_multiplier) {
    m_unit_multiplier = unit_multiplier;
    m_unit_multiplier_isSet = true;
}

bool OAISkulistbyProductId::is_unit_multiplier_Set() const{
    return m_unit_multiplier_isSet;
}

bool OAISkulistbyProductId::is_unit_multiplier_Valid() const{
    return m_unit_multiplier_isValid;
}

double OAISkulistbyProductId::getWeightKg() const {
    return m_weight_kg;
}
void OAISkulistbyProductId::setWeightKg(const double &weight_kg) {
    m_weight_kg = weight_kg;
    m_weight_kg_isSet = true;
}

bool OAISkulistbyProductId::is_weight_kg_Set() const{
    return m_weight_kg_isSet;
}

bool OAISkulistbyProductId::is_weight_kg_Valid() const{
    return m_weight_kg_isValid;
}

double OAISkulistbyProductId::getWidth() const {
    return m_width;
}
void OAISkulistbyProductId::setWidth(const double &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAISkulistbyProductId::is_width_Set() const{
    return m_width_isSet;
}

bool OAISkulistbyProductId::is_width_Valid() const{
    return m_width_isValid;
}

bool OAISkulistbyProductId::isIsKitOptimized() const {
    return m_is_kit_optimized;
}
void OAISkulistbyProductId::setIsKitOptimized(const bool &is_kit_optimized) {
    m_is_kit_optimized = is_kit_optimized;
    m_is_kit_optimized_isSet = true;
}

bool OAISkulistbyProductId::is_is_kit_optimized_Set() const{
    return m_is_kit_optimized_isSet;
}

bool OAISkulistbyProductId::is_is_kit_optimized_Valid() const{
    return m_is_kit_optimized_isValid;
}

bool OAISkulistbyProductId::isSet() const {
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

        if (m_cubic_weight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_estimated_date_arrival_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flag_kit_itens_sell_apart_isSet) {
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

        if (m_internal_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_dynamic_kit_isSet) {
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

        if (m_is_persisted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_removed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_transported_isSet) {
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

        if (m_modal_id_isSet) {
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

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_weight_kg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ref_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_stock_keeping_unit_id_isSet) {
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

        if (m_weight_kg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_kit_optimized_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISkulistbyProductId::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
