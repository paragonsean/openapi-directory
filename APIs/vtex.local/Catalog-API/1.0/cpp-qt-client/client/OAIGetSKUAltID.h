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
 * OAIGetSKUAltID.h
 *
 * 
 */

#ifndef OAIGetSKUAltID_H
#define OAIGetSKUAltID_H

#include <QJsonObject>

#include "OAIAlternateIds.h"
#include "OAIAttachment.h"
#include "OAIDimension.h"
#include "OAIImage.h"
#include "OAIProductSpecification.h"
#include "OAIRealDimension.h"
#include "OAISkuSeller.h"
#include "OAISkuSpecification.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAlternateIds;
class OAIAttachment;
class OAIDimension;
class OAIImage;
class OAIProductSpecification;
class OAIRealDimension;
class OAISkuSeller;
class OAISkuSpecification;

class OAIGetSKUAltID : public OAIObject {
public:
    OAIGetSKUAltID();
    OAIGetSKUAltID(QString json);
    ~OAIGetSKUAltID() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAlternateIdValues() const;
    void setAlternateIdValues(const QList<QString> &alternate_id_values);
    bool is_alternate_id_values_Set() const;
    bool is_alternate_id_values_Valid() const;

    OAIAlternateIds getAlternateIds() const;
    void setAlternateIds(const OAIAlternateIds &alternate_ids);
    bool is_alternate_ids_Set() const;
    bool is_alternate_ids_Valid() const;

    QList<OAIAttachment> getAttachments() const;
    void setAttachments(const QList<OAIAttachment> &attachments);
    bool is_attachments_Set() const;
    bool is_attachments_Valid() const;

    QString getBrandId() const;
    void setBrandId(const QString &brand_id);
    bool is_brand_id_Set() const;
    bool is_brand_id_Valid() const;

    QString getBrandName() const;
    void setBrandName(const QString &brand_name);
    bool is_brand_name_Set() const;
    bool is_brand_name_Valid() const;

    QString getCscIdentification() const;
    void setCscIdentification(const QString &csc_identification);
    bool is_csc_identification_Set() const;
    bool is_csc_identification_Valid() const;

    QList<QString> getCategories() const;
    void setCategories(const QList<QString> &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    QList<QString> getCategoriesFullPath() const;
    void setCategoriesFullPath(const QList<QString> &categories_full_path);
    bool is_categories_full_path_Set() const;
    bool is_categories_full_path_Valid() const;

    QList<QString> getCollections() const;
    void setCollections(const QList<QString> &collections);
    bool is_collections_Set() const;
    bool is_collections_Valid() const;

    qint32 getCommercialConditionId() const;
    void setCommercialConditionId(const qint32 &commercial_condition_id);
    bool is_commercial_condition_id_Set() const;
    bool is_commercial_condition_id_Valid() const;

    QString getComplementName() const;
    void setComplementName(const QString &complement_name);
    bool is_complement_name_Set() const;
    bool is_complement_name_Valid() const;

    QString getDetailUrl() const;
    void setDetailUrl(const QString &detail_url);
    bool is_detail_url_Set() const;
    bool is_detail_url_Valid() const;

    OAIDimension getDimension() const;
    void setDimension(const OAIDimension &dimension);
    bool is_dimension_Set() const;
    bool is_dimension_Valid() const;

    QString getEstimatedDateArrival() const;
    void setEstimatedDateArrival(const QString &estimated_date_arrival);
    bool is_estimated_date_arrival_Set() const;
    bool is_estimated_date_arrival_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getImageUrl() const;
    void setImageUrl(const QString &image_url);
    bool is_image_url_Set() const;
    bool is_image_url_Valid() const;

    QList<OAIImage> getImages() const;
    void setImages(const QList<OAIImage> &images);
    bool is_images_Set() const;
    bool is_images_Valid() const;

    QString getInformationSource() const;
    void setInformationSource(const QString &information_source);
    bool is_information_source_Set() const;
    bool is_information_source_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsDirectCategoryActive() const;
    void setIsDirectCategoryActive(const bool &is_direct_category_active);
    bool is_is_direct_category_active_Set() const;
    bool is_is_direct_category_active_Valid() const;

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

    bool isIsProductActive() const;
    void setIsProductActive(const bool &is_product_active);
    bool is_is_product_active_Set() const;
    bool is_is_product_active_Valid() const;

    Q_DECL_DEPRECATED bool isIsTransported() const;
    Q_DECL_DEPRECATED void setIsTransported(const bool &is_transported);
    Q_DECL_DEPRECATED bool is_is_transported_Set() const;
    Q_DECL_DEPRECATED bool is_is_transported_Valid() const;

    QString getKeyWords() const;
    void setKeyWords(const QString &key_words);
    bool is_key_words_Set() const;
    bool is_key_words_Valid() const;

    QList<QString> getKitItems() const;
    void setKitItems(const QList<QString> &kit_items);
    bool is_kit_items_Set() const;
    bool is_kit_items_Valid() const;

    QString getManufacturerCode() const;
    void setManufacturerCode(const QString &manufacturer_code);
    bool is_manufacturer_code_Set() const;
    bool is_manufacturer_code_Valid() const;

    QString getMeasurementUnit() const;
    void setMeasurementUnit(const QString &measurement_unit);
    bool is_measurement_unit_Set() const;
    bool is_measurement_unit_Valid() const;

    QString getModalType() const;
    void setModalType(const QString &modal_type);
    bool is_modal_type_Set() const;
    bool is_modal_type_Valid() const;

    QString getNameComplete() const;
    void setNameComplete(const QString &name_complete);
    bool is_name_complete_Set() const;
    bool is_name_complete_Valid() const;

    QMap<QString, QMap<QString, qint32>> getPositionsInClusters() const;
    void setPositionsInClusters(const QMap<QString, QMap<QString, qint32>> &positions_in_clusters);
    bool is_positions_in_clusters_Set() const;
    bool is_positions_in_clusters_Valid() const;

    QMap<QString, QMap<QString, QString>> getProductCategories() const;
    void setProductCategories(const QMap<QString, QMap<QString, QString>> &product_categories);
    bool is_product_categories_Set() const;
    bool is_product_categories_Valid() const;

    QString getProductCategoryIds() const;
    void setProductCategoryIds(const QString &product_category_ids);
    bool is_product_category_ids_Set() const;
    bool is_product_category_ids_Valid() const;

    QMap<QString, QMap<QString, QString>> getProductClusterHighlights() const;
    void setProductClusterHighlights(const QMap<QString, QMap<QString, QString>> &product_cluster_highlights);
    bool is_product_cluster_highlights_Set() const;
    bool is_product_cluster_highlights_Valid() const;

    QMap<QString, QMap<QString, QString>> getProductClusterNames() const;
    void setProductClusterNames(const QMap<QString, QMap<QString, QString>> &product_cluster_names);
    bool is_product_cluster_names_Set() const;
    bool is_product_cluster_names_Valid() const;

    QString getProductClustersIds() const;
    void setProductClustersIds(const QString &product_clusters_ids);
    bool is_product_clusters_ids_Set() const;
    bool is_product_clusters_ids_Valid() const;

    QString getProductDescription() const;
    void setProductDescription(const QString &product_description);
    bool is_product_description_Set() const;
    bool is_product_description_Valid() const;

    qint32 getProductFinalScore() const;
    void setProductFinalScore(const qint32 &product_final_score);
    bool is_product_final_score_Set() const;
    bool is_product_final_score_Valid() const;

    qint32 getProductGlobalCategoryId() const;
    void setProductGlobalCategoryId(const qint32 &product_global_category_id);
    bool is_product_global_category_id_Set() const;
    bool is_product_global_category_id_Valid() const;

    qint32 getProductId() const;
    void setProductId(const qint32 &product_id);
    bool is_product_id_Set() const;
    bool is_product_id_Valid() const;

    bool isProductIsVisible() const;
    void setProductIsVisible(const bool &product_is_visible);
    bool is_product_is_visible_Set() const;
    bool is_product_is_visible_Valid() const;

    QString getProductName() const;
    void setProductName(const QString &product_name);
    bool is_product_name_Set() const;
    bool is_product_name_Valid() const;

    QString getProductRefId() const;
    void setProductRefId(const QString &product_ref_id);
    bool is_product_ref_id_Set() const;
    bool is_product_ref_id_Valid() const;

    QList<OAIProductSpecification> getProductSpecifications() const;
    void setProductSpecifications(const QList<OAIProductSpecification> &product_specifications);
    bool is_product_specifications_Set() const;
    bool is_product_specifications_Valid() const;

    OAIRealDimension getRealDimension() const;
    void setRealDimension(const OAIRealDimension &real_dimension);
    bool is_real_dimension_Set() const;
    bool is_real_dimension_Valid() const;

    QString getReleaseDate() const;
    void setReleaseDate(const QString &release_date);
    bool is_release_date_Set() const;
    bool is_release_date_Valid() const;

    double getRewardValue() const;
    void setRewardValue(const double &reward_value);
    bool is_reward_value_Set() const;
    bool is_reward_value_Valid() const;

    QList<qint32> getSalesChannels() const;
    void setSalesChannels(const QList<qint32> &sales_channels);
    bool is_sales_channels_Set() const;
    bool is_sales_channels_Valid() const;

    QList<QString> getServices() const;
    void setServices(const QList<QString> &services);
    bool is_services_Set() const;
    bool is_services_Valid() const;

    bool isShowIfNotAvailable() const;
    void setShowIfNotAvailable(const bool &show_if_not_available);
    bool is_show_if_not_available_Set() const;
    bool is_show_if_not_available_Valid() const;

    QString getSkuName() const;
    void setSkuName(const QString &sku_name);
    bool is_sku_name_Set() const;
    bool is_sku_name_Valid() const;

    QList<OAISkuSeller> getSkuSellers() const;
    void setSkuSellers(const QList<OAISkuSeller> &sku_sellers);
    bool is_sku_sellers_Set() const;
    bool is_sku_sellers_Valid() const;

    QList<OAISkuSpecification> getSkuSpecifications() const;
    void setSkuSpecifications(const QList<OAISkuSpecification> &sku_specifications);
    bool is_sku_specifications_Set() const;
    bool is_sku_specifications_Valid() const;

    QString getTaxCode() const;
    void setTaxCode(const QString &tax_code);
    bool is_tax_code_Set() const;
    bool is_tax_code_Valid() const;

    double getUnitMultiplier() const;
    void setUnitMultiplier(const double &unit_multiplier);
    bool is_unit_multiplier_Set() const;
    bool is_unit_multiplier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_alternate_id_values;
    bool m_alternate_id_values_isSet;
    bool m_alternate_id_values_isValid;

    OAIAlternateIds m_alternate_ids;
    bool m_alternate_ids_isSet;
    bool m_alternate_ids_isValid;

    QList<OAIAttachment> m_attachments;
    bool m_attachments_isSet;
    bool m_attachments_isValid;

    QString m_brand_id;
    bool m_brand_id_isSet;
    bool m_brand_id_isValid;

    QString m_brand_name;
    bool m_brand_name_isSet;
    bool m_brand_name_isValid;

    QString m_csc_identification;
    bool m_csc_identification_isSet;
    bool m_csc_identification_isValid;

    QList<QString> m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    QList<QString> m_categories_full_path;
    bool m_categories_full_path_isSet;
    bool m_categories_full_path_isValid;

    QList<QString> m_collections;
    bool m_collections_isSet;
    bool m_collections_isValid;

    qint32 m_commercial_condition_id;
    bool m_commercial_condition_id_isSet;
    bool m_commercial_condition_id_isValid;

    QString m_complement_name;
    bool m_complement_name_isSet;
    bool m_complement_name_isValid;

    QString m_detail_url;
    bool m_detail_url_isSet;
    bool m_detail_url_isValid;

    OAIDimension m_dimension;
    bool m_dimension_isSet;
    bool m_dimension_isValid;

    QString m_estimated_date_arrival;
    bool m_estimated_date_arrival_isSet;
    bool m_estimated_date_arrival_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_image_url;
    bool m_image_url_isSet;
    bool m_image_url_isValid;

    QList<OAIImage> m_images;
    bool m_images_isSet;
    bool m_images_isValid;

    QString m_information_source;
    bool m_information_source_isSet;
    bool m_information_source_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_direct_category_active;
    bool m_is_direct_category_active_isSet;
    bool m_is_direct_category_active_isValid;

    bool m_is_gift_card_recharge;
    bool m_is_gift_card_recharge_isSet;
    bool m_is_gift_card_recharge_isValid;

    bool m_is_inventoried;
    bool m_is_inventoried_isSet;
    bool m_is_inventoried_isValid;

    bool m_is_kit;
    bool m_is_kit_isSet;
    bool m_is_kit_isValid;

    bool m_is_product_active;
    bool m_is_product_active_isSet;
    bool m_is_product_active_isValid;

    bool m_is_transported;
    bool m_is_transported_isSet;
    bool m_is_transported_isValid;

    QString m_key_words;
    bool m_key_words_isSet;
    bool m_key_words_isValid;

    QList<QString> m_kit_items;
    bool m_kit_items_isSet;
    bool m_kit_items_isValid;

    QString m_manufacturer_code;
    bool m_manufacturer_code_isSet;
    bool m_manufacturer_code_isValid;

    QString m_measurement_unit;
    bool m_measurement_unit_isSet;
    bool m_measurement_unit_isValid;

    QString m_modal_type;
    bool m_modal_type_isSet;
    bool m_modal_type_isValid;

    QString m_name_complete;
    bool m_name_complete_isSet;
    bool m_name_complete_isValid;

    QMap<QString, QMap<QString, qint32>> m_positions_in_clusters;
    bool m_positions_in_clusters_isSet;
    bool m_positions_in_clusters_isValid;

    QMap<QString, QMap<QString, QString>> m_product_categories;
    bool m_product_categories_isSet;
    bool m_product_categories_isValid;

    QString m_product_category_ids;
    bool m_product_category_ids_isSet;
    bool m_product_category_ids_isValid;

    QMap<QString, QMap<QString, QString>> m_product_cluster_highlights;
    bool m_product_cluster_highlights_isSet;
    bool m_product_cluster_highlights_isValid;

    QMap<QString, QMap<QString, QString>> m_product_cluster_names;
    bool m_product_cluster_names_isSet;
    bool m_product_cluster_names_isValid;

    QString m_product_clusters_ids;
    bool m_product_clusters_ids_isSet;
    bool m_product_clusters_ids_isValid;

    QString m_product_description;
    bool m_product_description_isSet;
    bool m_product_description_isValid;

    qint32 m_product_final_score;
    bool m_product_final_score_isSet;
    bool m_product_final_score_isValid;

    qint32 m_product_global_category_id;
    bool m_product_global_category_id_isSet;
    bool m_product_global_category_id_isValid;

    qint32 m_product_id;
    bool m_product_id_isSet;
    bool m_product_id_isValid;

    bool m_product_is_visible;
    bool m_product_is_visible_isSet;
    bool m_product_is_visible_isValid;

    QString m_product_name;
    bool m_product_name_isSet;
    bool m_product_name_isValid;

    QString m_product_ref_id;
    bool m_product_ref_id_isSet;
    bool m_product_ref_id_isValid;

    QList<OAIProductSpecification> m_product_specifications;
    bool m_product_specifications_isSet;
    bool m_product_specifications_isValid;

    OAIRealDimension m_real_dimension;
    bool m_real_dimension_isSet;
    bool m_real_dimension_isValid;

    QString m_release_date;
    bool m_release_date_isSet;
    bool m_release_date_isValid;

    double m_reward_value;
    bool m_reward_value_isSet;
    bool m_reward_value_isValid;

    QList<qint32> m_sales_channels;
    bool m_sales_channels_isSet;
    bool m_sales_channels_isValid;

    QList<QString> m_services;
    bool m_services_isSet;
    bool m_services_isValid;

    bool m_show_if_not_available;
    bool m_show_if_not_available_isSet;
    bool m_show_if_not_available_isValid;

    QString m_sku_name;
    bool m_sku_name_isSet;
    bool m_sku_name_isValid;

    QList<OAISkuSeller> m_sku_sellers;
    bool m_sku_sellers_isSet;
    bool m_sku_sellers_isValid;

    QList<OAISkuSpecification> m_sku_specifications;
    bool m_sku_specifications_isSet;
    bool m_sku_specifications_isValid;

    QString m_tax_code;
    bool m_tax_code_isSet;
    bool m_tax_code_isValid;

    double m_unit_multiplier;
    bool m_unit_multiplier_isSet;
    bool m_unit_multiplier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetSKUAltID)

#endif // OAIGetSKUAltID_H
