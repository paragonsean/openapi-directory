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
 * OAICreateSeller_200_response.h
 *
 * 
 */

#ifndef OAICreateSeller_200_response_H
#define OAICreateSeller_200_response_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateSeller_200_response : public OAIObject {
public:
    OAICreateSeller_200_response();
    OAICreateSeller_200_response(QString json);
    ~OAICreateSeller_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getArchiveId() const;
    void setArchiveId(const qint32 &archive_id);
    bool is_archive_id_Set() const;
    bool is_archive_id_Valid() const;

    QString getCnpj() const;
    void setCnpj(const QString &cnpj);
    bool is_cnpj_Set() const;
    bool is_cnpj_Valid() const;

    QString getCscIdentification() const;
    void setCscIdentification(const QString &csc_identification);
    bool is_csc_identification_Set() const;
    bool is_csc_identification_Valid() const;

    QString getCatalogSystemEndpoint() const;
    void setCatalogSystemEndpoint(const QString &catalog_system_endpoint);
    bool is_catalog_system_endpoint_Set() const;
    bool is_catalog_system_endpoint_Valid() const;

    QString getCategoryCommissionPercentage() const;
    void setCategoryCommissionPercentage(const QString &category_commission_percentage);
    bool is_category_commission_percentage_Set() const;
    bool is_category_commission_percentage_Valid() const;

    QString getDeliveryPolicy() const;
    void setDeliveryPolicy(const QString &delivery_policy);
    bool is_delivery_policy_Set() const;
    bool is_delivery_policy_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getExchangeReturnPolicy() const;
    void setExchangeReturnPolicy(const QString &exchange_return_policy);
    bool is_exchange_return_policy_Set() const;
    bool is_exchange_return_policy_Valid() const;

    double getFreightCommissionPercentage() const;
    void setFreightCommissionPercentage(const double &freight_commission_percentage);
    bool is_freight_commission_percentage_Set() const;
    bool is_freight_commission_percentage_Valid() const;

    QString getFulfillmentEndpoint() const;
    void setFulfillmentEndpoint(const QString &fulfillment_endpoint);
    bool is_fulfillment_endpoint_Set() const;
    bool is_fulfillment_endpoint_Valid() const;

    qint32 getFulfillmentSellerId() const;
    void setFulfillmentSellerId(const qint32 &fulfillment_seller_id);
    bool is_fulfillment_seller_id_Set() const;
    bool is_fulfillment_seller_id_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsBetterScope() const;
    void setIsBetterScope(const bool &is_better_scope);
    bool is_is_better_scope_Set() const;
    bool is_is_better_scope_Valid() const;

    QString getMerchantName() const;
    void setMerchantName(const QString &merchant_name);
    bool is_merchant_name_Set() const;
    bool is_merchant_name_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    double getProductCommissionPercentage() const;
    void setProductCommissionPercentage(const double &product_commission_percentage);
    bool is_product_commission_percentage_Set() const;
    bool is_product_commission_percentage_Valid() const;

    QString getSecutityPrivacyPolicy() const;
    void setSecutityPrivacyPolicy(const QString &secutity_privacy_policy);
    bool is_secutity_privacy_policy_Set() const;
    bool is_secutity_privacy_policy_Valid() const;

    QString getSellerId() const;
    void setSellerId(const QString &seller_id);
    bool is_seller_id_Set() const;
    bool is_seller_id_Valid() const;

    qint32 getSellerType() const;
    void setSellerType(const qint32 &seller_type);
    bool is_seller_type_Set() const;
    bool is_seller_type_Valid() const;

    QString getTrustPolicy() const;
    void setTrustPolicy(const QString &trust_policy);
    bool is_trust_policy_Set() const;
    bool is_trust_policy_Valid() const;

    QString getUrlLogo() const;
    void setUrlLogo(const QString &url_logo);
    bool is_url_logo_Set() const;
    bool is_url_logo_Valid() const;

    bool isUseHybridPaymentOptions() const;
    void setUseHybridPaymentOptions(const bool &use_hybrid_payment_options);
    bool is_use_hybrid_payment_options_Set() const;
    bool is_use_hybrid_payment_options_Valid() const;

    QString getUserName() const;
    void setUserName(const QString &user_name);
    bool is_user_name_Set() const;
    bool is_user_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_archive_id;
    bool m_archive_id_isSet;
    bool m_archive_id_isValid;

    QString m_cnpj;
    bool m_cnpj_isSet;
    bool m_cnpj_isValid;

    QString m_csc_identification;
    bool m_csc_identification_isSet;
    bool m_csc_identification_isValid;

    QString m_catalog_system_endpoint;
    bool m_catalog_system_endpoint_isSet;
    bool m_catalog_system_endpoint_isValid;

    QString m_category_commission_percentage;
    bool m_category_commission_percentage_isSet;
    bool m_category_commission_percentage_isValid;

    QString m_delivery_policy;
    bool m_delivery_policy_isSet;
    bool m_delivery_policy_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_exchange_return_policy;
    bool m_exchange_return_policy_isSet;
    bool m_exchange_return_policy_isValid;

    double m_freight_commission_percentage;
    bool m_freight_commission_percentage_isSet;
    bool m_freight_commission_percentage_isValid;

    QString m_fulfillment_endpoint;
    bool m_fulfillment_endpoint_isSet;
    bool m_fulfillment_endpoint_isValid;

    qint32 m_fulfillment_seller_id;
    bool m_fulfillment_seller_id_isSet;
    bool m_fulfillment_seller_id_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_better_scope;
    bool m_is_better_scope_isSet;
    bool m_is_better_scope_isValid;

    QString m_merchant_name;
    bool m_merchant_name_isSet;
    bool m_merchant_name_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    double m_product_commission_percentage;
    bool m_product_commission_percentage_isSet;
    bool m_product_commission_percentage_isValid;

    QString m_secutity_privacy_policy;
    bool m_secutity_privacy_policy_isSet;
    bool m_secutity_privacy_policy_isValid;

    QString m_seller_id;
    bool m_seller_id_isSet;
    bool m_seller_id_isValid;

    qint32 m_seller_type;
    bool m_seller_type_isSet;
    bool m_seller_type_isValid;

    QString m_trust_policy;
    bool m_trust_policy_isSet;
    bool m_trust_policy_isValid;

    QString m_url_logo;
    bool m_url_logo_isSet;
    bool m_url_logo_isValid;

    bool m_use_hybrid_payment_options;
    bool m_use_hybrid_payment_options_isSet;
    bool m_use_hybrid_payment_options_isValid;

    QString m_user_name;
    bool m_user_name_isSet;
    bool m_user_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateSeller_200_response)

#endif // OAICreateSeller_200_response_H
