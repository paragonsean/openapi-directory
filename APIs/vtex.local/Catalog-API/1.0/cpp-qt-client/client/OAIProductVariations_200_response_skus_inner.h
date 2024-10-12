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
 * OAIProductVariations_200_response_skus_inner.h
 *
 * Object containing information about a specific SKU.
 */

#ifndef OAIProductVariations_200_response_skus_inner_H
#define OAIProductVariations_200_response_skus_inner_H

#include <QJsonObject>

#include "OAIProductVariations_200_response_skus_inner_measures.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIProductVariations_200_response_skus_inner_measures;

class OAIProductVariations_200_response_skus_inner : public OAIObject {
public:
    OAIProductVariations_200_response_skus_inner();
    OAIProductVariations_200_response_skus_inner(QString json);
    ~OAIProductVariations_200_response_skus_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAvailable() const;
    void setAvailable(const bool &available);
    bool is_available_Set() const;
    bool is_available_Valid() const;

    qint32 getAvailablequantity() const;
    void setAvailablequantity(const qint32 &availablequantity);
    bool is_availablequantity_Set() const;
    bool is_availablequantity_Valid() const;

    qint32 getBestPrice() const;
    void setBestPrice(const qint32 &best_price);
    bool is_best_price_Set() const;
    bool is_best_price_Valid() const;

    QString getBestPriceFormated() const;
    void setBestPriceFormated(const QString &best_price_formated);
    bool is_best_price_formated_Set() const;
    bool is_best_price_formated_Valid() const;

    QString getCacheVersionUsedToCallCheckout() const;
    void setCacheVersionUsedToCallCheckout(const QString &cache_version_used_to_call_checkout);
    bool is_cache_version_used_to_call_checkout_Set() const;
    bool is_cache_version_used_to_call_checkout_Valid() const;

    QMap<QString, QString> getDimensions() const;
    void setDimensions(const QMap<QString, QString> &dimensions);
    bool is_dimensions_Set() const;
    bool is_dimensions_Valid() const;

    QString getImage() const;
    void setImage(const QString &image);
    bool is_image_Set() const;
    bool is_image_Valid() const;

    qint32 getInstallments() const;
    void setInstallments(const qint32 &installments);
    bool is_installments_Set() const;
    bool is_installments_Valid() const;

    qint32 getInstallmentsInsterestRate() const;
    void setInstallmentsInsterestRate(const qint32 &installments_insterest_rate);
    bool is_installments_insterest_rate_Set() const;
    bool is_installments_insterest_rate_Valid() const;

    qint32 getInstallmentsValue() const;
    void setInstallmentsValue(const qint32 &installments_value);
    bool is_installments_value_Set() const;
    bool is_installments_value_Valid() const;

    qint32 getListPrice() const;
    void setListPrice(const qint32 &list_price);
    bool is_list_price_Set() const;
    bool is_list_price_Valid() const;

    QString getListPriceFormated() const;
    void setListPriceFormated(const QString &list_price_formated);
    bool is_list_price_formated_Set() const;
    bool is_list_price_formated_Valid() const;

    OAIProductVariations_200_response_skus_inner_measures getMeasures() const;
    void setMeasures(const OAIProductVariations_200_response_skus_inner_measures &measures);
    bool is_measures_Set() const;
    bool is_measures_Valid() const;

    qint32 getRewardValue() const;
    void setRewardValue(const qint32 &reward_value);
    bool is_reward_value_Set() const;
    bool is_reward_value_Valid() const;

    QString getSellerId() const;
    void setSellerId(const QString &seller_id);
    bool is_seller_id_Set() const;
    bool is_seller_id_Valid() const;

    qint32 getSku() const;
    void setSku(const qint32 &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    QString getSkuname() const;
    void setSkuname(const QString &skuname);
    bool is_skuname_Set() const;
    bool is_skuname_Valid() const;

    qint32 getSpotPrice() const;
    void setSpotPrice(const qint32 &spot_price);
    bool is_spot_price_Set() const;
    bool is_spot_price_Valid() const;

    qint32 getTaxAsInt() const;
    void setTaxAsInt(const qint32 &tax_as_int);
    bool is_tax_as_int_Set() const;
    bool is_tax_as_int_Valid() const;

    QString getTaxFormated() const;
    void setTaxFormated(const QString &tax_formated);
    bool is_tax_formated_Set() const;
    bool is_tax_formated_Valid() const;

    double getUnitMultiplier() const;
    void setUnitMultiplier(const double &unit_multiplier);
    bool is_unit_multiplier_Set() const;
    bool is_unit_multiplier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_available;
    bool m_available_isSet;
    bool m_available_isValid;

    qint32 m_availablequantity;
    bool m_availablequantity_isSet;
    bool m_availablequantity_isValid;

    qint32 m_best_price;
    bool m_best_price_isSet;
    bool m_best_price_isValid;

    QString m_best_price_formated;
    bool m_best_price_formated_isSet;
    bool m_best_price_formated_isValid;

    QString m_cache_version_used_to_call_checkout;
    bool m_cache_version_used_to_call_checkout_isSet;
    bool m_cache_version_used_to_call_checkout_isValid;

    QMap<QString, QString> m_dimensions;
    bool m_dimensions_isSet;
    bool m_dimensions_isValid;

    QString m_image;
    bool m_image_isSet;
    bool m_image_isValid;

    qint32 m_installments;
    bool m_installments_isSet;
    bool m_installments_isValid;

    qint32 m_installments_insterest_rate;
    bool m_installments_insterest_rate_isSet;
    bool m_installments_insterest_rate_isValid;

    qint32 m_installments_value;
    bool m_installments_value_isSet;
    bool m_installments_value_isValid;

    qint32 m_list_price;
    bool m_list_price_isSet;
    bool m_list_price_isValid;

    QString m_list_price_formated;
    bool m_list_price_formated_isSet;
    bool m_list_price_formated_isValid;

    OAIProductVariations_200_response_skus_inner_measures m_measures;
    bool m_measures_isSet;
    bool m_measures_isValid;

    qint32 m_reward_value;
    bool m_reward_value_isSet;
    bool m_reward_value_isValid;

    QString m_seller_id;
    bool m_seller_id_isSet;
    bool m_seller_id_isValid;

    qint32 m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;

    QString m_skuname;
    bool m_skuname_isSet;
    bool m_skuname_isValid;

    qint32 m_spot_price;
    bool m_spot_price_isSet;
    bool m_spot_price_isValid;

    qint32 m_tax_as_int;
    bool m_tax_as_int_isSet;
    bool m_tax_as_int_isValid;

    QString m_tax_formated;
    bool m_tax_formated_isSet;
    bool m_tax_formated_isValid;

    double m_unit_multiplier;
    bool m_unit_multiplier_isSet;
    bool m_unit_multiplier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductVariations_200_response_skus_inner)

#endif // OAIProductVariations_200_response_skus_inner_H
