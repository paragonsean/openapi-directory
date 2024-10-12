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

/*
 * OAISkulistbyProductId.h
 *
 * 
 */

#ifndef OAISkulistbyProductId_H
#define OAISkulistbyProductId_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISkulistbyProductId : public OAIObject {
public:
    OAISkulistbyProductId();
    OAISkulistbyProductId(QString json);
    ~OAISkulistbyProductId() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isActivateIfPossible() const;
    void setActivateIfPossible(const bool &activate_if_possible);
    bool is_activate_if_possible_Set() const;
    bool is_activate_if_possible_Valid() const;

    qint32 getCommercialConditionId() const;
    void setCommercialConditionId(const qint32 &commercial_condition_id);
    bool is_commercial_condition_id_Set() const;
    bool is_commercial_condition_id_Valid() const;

    double getCubicWeight() const;
    void setCubicWeight(const double &cubic_weight);
    bool is_cubic_weight_Set() const;
    bool is_cubic_weight_Valid() const;

    QString getDateUpdated() const;
    void setDateUpdated(const QString &date_updated);
    bool is_date_updated_Set() const;
    bool is_date_updated_Valid() const;

    QString getEstimatedDateArrival() const;
    void setEstimatedDateArrival(const QString &estimated_date_arrival);
    bool is_estimated_date_arrival_Set() const;
    bool is_estimated_date_arrival_Valid() const;

    bool isFlagKitItensSellApart() const;
    void setFlagKitItensSellApart(const bool &flag_kit_itens_sell_apart);
    bool is_flag_kit_itens_sell_apart_Set() const;
    bool is_flag_kit_itens_sell_apart_Valid() const;

    double getHeight() const;
    void setHeight(const double &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getInternalNote() const;
    void setInternalNote(const QString &internal_note);
    bool is_internal_note_Set() const;
    bool is_internal_note_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    Q_DECL_DEPRECATED QString getIsDynamicKit() const;
    Q_DECL_DEPRECATED void setIsDynamicKit(const QString &is_dynamic_kit);
    Q_DECL_DEPRECATED bool is_is_dynamic_kit_Set() const;
    Q_DECL_DEPRECATED bool is_is_dynamic_kit_Valid() const;

    bool isIsGiftCardRecharge() const;
    void setIsGiftCardRecharge(const bool &is_gift_card_recharge);
    bool is_is_gift_card_recharge_Set() const;
    bool is_is_gift_card_recharge_Valid() const;

    Q_DECL_DEPRECATED bool isIsInventoried() const;
    Q_DECL_DEPRECATED void setIsInventoried(const bool &is_inventoried);
    Q_DECL_DEPRECATED bool is_is_inventoried_Set() const;
    Q_DECL_DEPRECATED bool is_is_inventoried_Valid() const;

    bool isIsKit() const;
    void setIsKit(const bool &is_kit);
    bool is_is_kit_Set() const;
    bool is_is_kit_Valid() const;

    bool isIsPersisted() const;
    void setIsPersisted(const bool &is_persisted);
    bool is_is_persisted_Set() const;
    bool is_is_persisted_Valid() const;

    Q_DECL_DEPRECATED bool isIsRemoved() const;
    Q_DECL_DEPRECATED void setIsRemoved(const bool &is_removed);
    Q_DECL_DEPRECATED bool is_is_removed_Set() const;
    Q_DECL_DEPRECATED bool is_is_removed_Valid() const;

    Q_DECL_DEPRECATED bool isIsTransported() const;
    Q_DECL_DEPRECATED void setIsTransported(const bool &is_transported);
    Q_DECL_DEPRECATED bool is_is_transported_Set() const;
    Q_DECL_DEPRECATED bool is_is_transported_Valid() const;

    double getLength() const;
    void setLength(const double &length);
    bool is_length_Set() const;
    bool is_length_Valid() const;

    QString getManufacturerCode() const;
    void setManufacturerCode(const QString &manufacturer_code);
    bool is_manufacturer_code_Set() const;
    bool is_manufacturer_code_Valid() const;

    QString getMeasurementUnit() const;
    void setMeasurementUnit(const QString &measurement_unit);
    bool is_measurement_unit_Set() const;
    bool is_measurement_unit_Valid() const;

    qint32 getModalId() const;
    void setModalId(const qint32 &modal_id);
    bool is_modal_id_Set() const;
    bool is_modal_id_Valid() const;

    QString getModalType() const;
    void setModalType(const QString &modal_type);
    bool is_modal_type_Set() const;
    bool is_modal_type_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPosition() const;
    void setPosition(const qint32 &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    qint32 getProductId() const;
    void setProductId(const qint32 &product_id);
    bool is_product_id_Set() const;
    bool is_product_id_Valid() const;

    double getRealHeight() const;
    void setRealHeight(const double &real_height);
    bool is_real_height_Set() const;
    bool is_real_height_Valid() const;

    double getRealLength() const;
    void setRealLength(const double &real_length);
    bool is_real_length_Set() const;
    bool is_real_length_Valid() const;

    double getRealWeightKg() const;
    void setRealWeightKg(const double &real_weight_kg);
    bool is_real_weight_kg_Set() const;
    bool is_real_weight_kg_Valid() const;

    double getRealWidth() const;
    void setRealWidth(const double &real_width);
    bool is_real_width_Set() const;
    bool is_real_width_Valid() const;

    QString getRefId() const;
    void setRefId(const QString &ref_id);
    bool is_ref_id_Set() const;
    bool is_ref_id_Valid() const;

    QString getReferenceStockKeepingUnitId() const;
    void setReferenceStockKeepingUnitId(const QString &reference_stock_keeping_unit_id);
    bool is_reference_stock_keeping_unit_id_Set() const;
    bool is_reference_stock_keeping_unit_id_Valid() const;

    double getRewardValue() const;
    void setRewardValue(const double &reward_value);
    bool is_reward_value_Set() const;
    bool is_reward_value_Valid() const;

    double getUnitMultiplier() const;
    void setUnitMultiplier(const double &unit_multiplier);
    bool is_unit_multiplier_Set() const;
    bool is_unit_multiplier_Valid() const;

    double getWeightKg() const;
    void setWeightKg(const double &weight_kg);
    bool is_weight_kg_Set() const;
    bool is_weight_kg_Valid() const;

    double getWidth() const;
    void setWidth(const double &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    bool isIsKitOptimized() const;
    void setIsKitOptimized(const bool &is_kit_optimized);
    bool is_is_kit_optimized_Set() const;
    bool is_is_kit_optimized_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_activate_if_possible;
    bool m_activate_if_possible_isSet;
    bool m_activate_if_possible_isValid;

    qint32 m_commercial_condition_id;
    bool m_commercial_condition_id_isSet;
    bool m_commercial_condition_id_isValid;

    double m_cubic_weight;
    bool m_cubic_weight_isSet;
    bool m_cubic_weight_isValid;

    QString m_date_updated;
    bool m_date_updated_isSet;
    bool m_date_updated_isValid;

    QString m_estimated_date_arrival;
    bool m_estimated_date_arrival_isSet;
    bool m_estimated_date_arrival_isValid;

    bool m_flag_kit_itens_sell_apart;
    bool m_flag_kit_itens_sell_apart_isSet;
    bool m_flag_kit_itens_sell_apart_isValid;

    double m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_internal_note;
    bool m_internal_note_isSet;
    bool m_internal_note_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    QString m_is_dynamic_kit;
    bool m_is_dynamic_kit_isSet;
    bool m_is_dynamic_kit_isValid;

    bool m_is_gift_card_recharge;
    bool m_is_gift_card_recharge_isSet;
    bool m_is_gift_card_recharge_isValid;

    bool m_is_inventoried;
    bool m_is_inventoried_isSet;
    bool m_is_inventoried_isValid;

    bool m_is_kit;
    bool m_is_kit_isSet;
    bool m_is_kit_isValid;

    bool m_is_persisted;
    bool m_is_persisted_isSet;
    bool m_is_persisted_isValid;

    bool m_is_removed;
    bool m_is_removed_isSet;
    bool m_is_removed_isValid;

    bool m_is_transported;
    bool m_is_transported_isSet;
    bool m_is_transported_isValid;

    double m_length;
    bool m_length_isSet;
    bool m_length_isValid;

    QString m_manufacturer_code;
    bool m_manufacturer_code_isSet;
    bool m_manufacturer_code_isValid;

    QString m_measurement_unit;
    bool m_measurement_unit_isSet;
    bool m_measurement_unit_isValid;

    qint32 m_modal_id;
    bool m_modal_id_isSet;
    bool m_modal_id_isValid;

    QString m_modal_type;
    bool m_modal_type_isSet;
    bool m_modal_type_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    qint32 m_product_id;
    bool m_product_id_isSet;
    bool m_product_id_isValid;

    double m_real_height;
    bool m_real_height_isSet;
    bool m_real_height_isValid;

    double m_real_length;
    bool m_real_length_isSet;
    bool m_real_length_isValid;

    double m_real_weight_kg;
    bool m_real_weight_kg_isSet;
    bool m_real_weight_kg_isValid;

    double m_real_width;
    bool m_real_width_isSet;
    bool m_real_width_isValid;

    QString m_ref_id;
    bool m_ref_id_isSet;
    bool m_ref_id_isValid;

    QString m_reference_stock_keeping_unit_id;
    bool m_reference_stock_keeping_unit_id_isSet;
    bool m_reference_stock_keeping_unit_id_isValid;

    double m_reward_value;
    bool m_reward_value_isSet;
    bool m_reward_value_isValid;

    double m_unit_multiplier;
    bool m_unit_multiplier_isSet;
    bool m_unit_multiplier_isValid;

    double m_weight_kg;
    bool m_weight_kg_isSet;
    bool m_weight_kg_isValid;

    double m_width;
    bool m_width_isSet;
    bool m_width_isValid;

    bool m_is_kit_optimized;
    bool m_is_kit_optimized_isSet;
    bool m_is_kit_optimized_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISkulistbyProductId)

#endif // OAISkulistbyProductId_H
