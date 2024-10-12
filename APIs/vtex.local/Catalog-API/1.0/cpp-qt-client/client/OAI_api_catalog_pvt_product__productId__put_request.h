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
 * OAI_api_catalog_pvt_product__productId__put_request.h
 *
 * 
 */

#ifndef OAI_api_catalog_pvt_product__productId__put_request_H
#define OAI_api_catalog_pvt_product__productId__put_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_api_catalog_pvt_product__productId__put_request : public OAIObject {
public:
    OAI_api_catalog_pvt_product__productId__put_request();
    OAI_api_catalog_pvt_product__productId__put_request(QString json);
    ~OAI_api_catalog_pvt_product__productId__put_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    Q_DECL_DEPRECATED QString getAdWordsRemarketingCode() const;
    Q_DECL_DEPRECATED void setAdWordsRemarketingCode(const QString &ad_words_remarketing_code);
    Q_DECL_DEPRECATED bool is_ad_words_remarketing_code_Set() const;
    Q_DECL_DEPRECATED bool is_ad_words_remarketing_code_Valid() const;

    qint32 getBrandId() const;
    void setBrandId(const qint32 &brand_id);
    bool is_brand_id_Set() const;
    bool is_brand_id_Valid() const;

    qint32 getCategoryId() const;
    void setCategoryId(const qint32 &category_id);
    bool is_category_id_Set() const;
    bool is_category_id_Valid() const;

    qint32 getDepartmentId() const;
    void setDepartmentId(const qint32 &department_id);
    bool is_department_id_Set() const;
    bool is_department_id_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getDescriptionShort() const;
    void setDescriptionShort(const QString &description_short);
    bool is_description_short_Set() const;
    bool is_description_short_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsVisible() const;
    void setIsVisible(const bool &is_visible);
    bool is_is_visible_Set() const;
    bool is_is_visible_Valid() const;

    QString getKeyWords() const;
    void setKeyWords(const QString &key_words);
    bool is_key_words_Set() const;
    bool is_key_words_Valid() const;

    QString getLinkId() const;
    void setLinkId(const QString &link_id);
    bool is_link_id_Set() const;
    bool is_link_id_Valid() const;

    Q_DECL_DEPRECATED QString getLomadeeCampaignCode() const;
    Q_DECL_DEPRECATED void setLomadeeCampaignCode(const QString &lomadee_campaign_code);
    Q_DECL_DEPRECATED bool is_lomadee_campaign_code_Set() const;
    Q_DECL_DEPRECATED bool is_lomadee_campaign_code_Valid() const;

    QString getMetaTagDescription() const;
    void setMetaTagDescription(const QString &meta_tag_description);
    bool is_meta_tag_description_Set() const;
    bool is_meta_tag_description_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getRefId() const;
    void setRefId(const QString &ref_id);
    bool is_ref_id_Set() const;
    bool is_ref_id_Valid() const;

    QString getReleaseDate() const;
    void setReleaseDate(const QString &release_date);
    bool is_release_date_Set() const;
    bool is_release_date_Valid() const;

    qint32 getScore() const;
    void setScore(const qint32 &score);
    bool is_score_Set() const;
    bool is_score_Valid() const;

    bool isShowWithoutStock() const;
    void setShowWithoutStock(const bool &show_without_stock);
    bool is_show_without_stock_Set() const;
    bool is_show_without_stock_Valid() const;

    Q_DECL_DEPRECATED qint32 getSupplierId() const;
    Q_DECL_DEPRECATED void setSupplierId(const qint32 &supplier_id);
    Q_DECL_DEPRECATED bool is_supplier_id_Set() const;
    Q_DECL_DEPRECATED bool is_supplier_id_Valid() const;

    QString getTaxCode() const;
    void setTaxCode(const QString &tax_code);
    bool is_tax_code_Set() const;
    bool is_tax_code_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_ad_words_remarketing_code;
    bool m_ad_words_remarketing_code_isSet;
    bool m_ad_words_remarketing_code_isValid;

    qint32 m_brand_id;
    bool m_brand_id_isSet;
    bool m_brand_id_isValid;

    qint32 m_category_id;
    bool m_category_id_isSet;
    bool m_category_id_isValid;

    qint32 m_department_id;
    bool m_department_id_isSet;
    bool m_department_id_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_description_short;
    bool m_description_short_isSet;
    bool m_description_short_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_visible;
    bool m_is_visible_isSet;
    bool m_is_visible_isValid;

    QString m_key_words;
    bool m_key_words_isSet;
    bool m_key_words_isValid;

    QString m_link_id;
    bool m_link_id_isSet;
    bool m_link_id_isValid;

    QString m_lomadee_campaign_code;
    bool m_lomadee_campaign_code_isSet;
    bool m_lomadee_campaign_code_isValid;

    QString m_meta_tag_description;
    bool m_meta_tag_description_isSet;
    bool m_meta_tag_description_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_ref_id;
    bool m_ref_id_isSet;
    bool m_ref_id_isValid;

    QString m_release_date;
    bool m_release_date_isSet;
    bool m_release_date_isValid;

    qint32 m_score;
    bool m_score_isSet;
    bool m_score_isValid;

    bool m_show_without_stock;
    bool m_show_without_stock_isSet;
    bool m_show_without_stock_isValid;

    qint32 m_supplier_id;
    bool m_supplier_id_isSet;
    bool m_supplier_id_isValid;

    QString m_tax_code;
    bool m_tax_code_isSet;
    bool m_tax_code_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_api_catalog_pvt_product__productId__put_request)

#endif // OAI_api_catalog_pvt_product__productId__put_request_H
