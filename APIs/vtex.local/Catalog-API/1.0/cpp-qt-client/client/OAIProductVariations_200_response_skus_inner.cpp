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

#include "OAIProductVariations_200_response_skus_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductVariations_200_response_skus_inner::OAIProductVariations_200_response_skus_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductVariations_200_response_skus_inner::OAIProductVariations_200_response_skus_inner() {
    this->initializeModel();
}

OAIProductVariations_200_response_skus_inner::~OAIProductVariations_200_response_skus_inner() {}

void OAIProductVariations_200_response_skus_inner::initializeModel() {

    m_available_isSet = false;
    m_available_isValid = false;

    m_availablequantity_isSet = false;
    m_availablequantity_isValid = false;

    m_best_price_isSet = false;
    m_best_price_isValid = false;

    m_best_price_formated_isSet = false;
    m_best_price_formated_isValid = false;

    m_cache_version_used_to_call_checkout_isSet = false;
    m_cache_version_used_to_call_checkout_isValid = false;

    m_dimensions_isSet = false;
    m_dimensions_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_installments_isSet = false;
    m_installments_isValid = false;

    m_installments_insterest_rate_isSet = false;
    m_installments_insterest_rate_isValid = false;

    m_installments_value_isSet = false;
    m_installments_value_isValid = false;

    m_list_price_isSet = false;
    m_list_price_isValid = false;

    m_list_price_formated_isSet = false;
    m_list_price_formated_isValid = false;

    m_measures_isSet = false;
    m_measures_isValid = false;

    m_reward_value_isSet = false;
    m_reward_value_isValid = false;

    m_seller_id_isSet = false;
    m_seller_id_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_skuname_isSet = false;
    m_skuname_isValid = false;

    m_spot_price_isSet = false;
    m_spot_price_isValid = false;

    m_tax_as_int_isSet = false;
    m_tax_as_int_isValid = false;

    m_tax_formated_isSet = false;
    m_tax_formated_isValid = false;

    m_unit_multiplier_isSet = false;
    m_unit_multiplier_isValid = false;
}

void OAIProductVariations_200_response_skus_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductVariations_200_response_skus_inner::fromJsonObject(QJsonObject json) {

    m_available_isValid = ::OpenAPI::fromJsonValue(m_available, json[QString("available")]);
    m_available_isSet = !json[QString("available")].isNull() && m_available_isValid;

    m_availablequantity_isValid = ::OpenAPI::fromJsonValue(m_availablequantity, json[QString("availablequantity")]);
    m_availablequantity_isSet = !json[QString("availablequantity")].isNull() && m_availablequantity_isValid;

    m_best_price_isValid = ::OpenAPI::fromJsonValue(m_best_price, json[QString("bestPrice")]);
    m_best_price_isSet = !json[QString("bestPrice")].isNull() && m_best_price_isValid;

    m_best_price_formated_isValid = ::OpenAPI::fromJsonValue(m_best_price_formated, json[QString("bestPriceFormated")]);
    m_best_price_formated_isSet = !json[QString("bestPriceFormated")].isNull() && m_best_price_formated_isValid;

    m_cache_version_used_to_call_checkout_isValid = ::OpenAPI::fromJsonValue(m_cache_version_used_to_call_checkout, json[QString("cacheVersionUsedToCallCheckout")]);
    m_cache_version_used_to_call_checkout_isSet = !json[QString("cacheVersionUsedToCallCheckout")].isNull() && m_cache_version_used_to_call_checkout_isValid;

    m_dimensions_isValid = ::OpenAPI::fromJsonValue(m_dimensions, json[QString("dimensions")]);
    m_dimensions_isSet = !json[QString("dimensions")].isNull() && m_dimensions_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_installments_isValid = ::OpenAPI::fromJsonValue(m_installments, json[QString("installments")]);
    m_installments_isSet = !json[QString("installments")].isNull() && m_installments_isValid;

    m_installments_insterest_rate_isValid = ::OpenAPI::fromJsonValue(m_installments_insterest_rate, json[QString("installmentsInsterestRate")]);
    m_installments_insterest_rate_isSet = !json[QString("installmentsInsterestRate")].isNull() && m_installments_insterest_rate_isValid;

    m_installments_value_isValid = ::OpenAPI::fromJsonValue(m_installments_value, json[QString("installmentsValue")]);
    m_installments_value_isSet = !json[QString("installmentsValue")].isNull() && m_installments_value_isValid;

    m_list_price_isValid = ::OpenAPI::fromJsonValue(m_list_price, json[QString("listPrice")]);
    m_list_price_isSet = !json[QString("listPrice")].isNull() && m_list_price_isValid;

    m_list_price_formated_isValid = ::OpenAPI::fromJsonValue(m_list_price_formated, json[QString("listPriceFormated")]);
    m_list_price_formated_isSet = !json[QString("listPriceFormated")].isNull() && m_list_price_formated_isValid;

    m_measures_isValid = ::OpenAPI::fromJsonValue(m_measures, json[QString("measures")]);
    m_measures_isSet = !json[QString("measures")].isNull() && m_measures_isValid;

    m_reward_value_isValid = ::OpenAPI::fromJsonValue(m_reward_value, json[QString("rewardValue")]);
    m_reward_value_isSet = !json[QString("rewardValue")].isNull() && m_reward_value_isValid;

    m_seller_id_isValid = ::OpenAPI::fromJsonValue(m_seller_id, json[QString("sellerId")]);
    m_seller_id_isSet = !json[QString("sellerId")].isNull() && m_seller_id_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_skuname_isValid = ::OpenAPI::fromJsonValue(m_skuname, json[QString("skuname")]);
    m_skuname_isSet = !json[QString("skuname")].isNull() && m_skuname_isValid;

    m_spot_price_isValid = ::OpenAPI::fromJsonValue(m_spot_price, json[QString("spotPrice")]);
    m_spot_price_isSet = !json[QString("spotPrice")].isNull() && m_spot_price_isValid;

    m_tax_as_int_isValid = ::OpenAPI::fromJsonValue(m_tax_as_int, json[QString("taxAsInt")]);
    m_tax_as_int_isSet = !json[QString("taxAsInt")].isNull() && m_tax_as_int_isValid;

    m_tax_formated_isValid = ::OpenAPI::fromJsonValue(m_tax_formated, json[QString("taxFormated")]);
    m_tax_formated_isSet = !json[QString("taxFormated")].isNull() && m_tax_formated_isValid;

    m_unit_multiplier_isValid = ::OpenAPI::fromJsonValue(m_unit_multiplier, json[QString("unitMultiplier")]);
    m_unit_multiplier_isSet = !json[QString("unitMultiplier")].isNull() && m_unit_multiplier_isValid;
}

QString OAIProductVariations_200_response_skus_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductVariations_200_response_skus_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_available_isSet) {
        obj.insert(QString("available"), ::OpenAPI::toJsonValue(m_available));
    }
    if (m_availablequantity_isSet) {
        obj.insert(QString("availablequantity"), ::OpenAPI::toJsonValue(m_availablequantity));
    }
    if (m_best_price_isSet) {
        obj.insert(QString("bestPrice"), ::OpenAPI::toJsonValue(m_best_price));
    }
    if (m_best_price_formated_isSet) {
        obj.insert(QString("bestPriceFormated"), ::OpenAPI::toJsonValue(m_best_price_formated));
    }
    if (m_cache_version_used_to_call_checkout_isSet) {
        obj.insert(QString("cacheVersionUsedToCallCheckout"), ::OpenAPI::toJsonValue(m_cache_version_used_to_call_checkout));
    }
    if (m_dimensions.size() > 0) {
        obj.insert(QString("dimensions"), ::OpenAPI::toJsonValue(m_dimensions));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_installments_isSet) {
        obj.insert(QString("installments"), ::OpenAPI::toJsonValue(m_installments));
    }
    if (m_installments_insterest_rate_isSet) {
        obj.insert(QString("installmentsInsterestRate"), ::OpenAPI::toJsonValue(m_installments_insterest_rate));
    }
    if (m_installments_value_isSet) {
        obj.insert(QString("installmentsValue"), ::OpenAPI::toJsonValue(m_installments_value));
    }
    if (m_list_price_isSet) {
        obj.insert(QString("listPrice"), ::OpenAPI::toJsonValue(m_list_price));
    }
    if (m_list_price_formated_isSet) {
        obj.insert(QString("listPriceFormated"), ::OpenAPI::toJsonValue(m_list_price_formated));
    }
    if (m_measures.isSet()) {
        obj.insert(QString("measures"), ::OpenAPI::toJsonValue(m_measures));
    }
    if (m_reward_value_isSet) {
        obj.insert(QString("rewardValue"), ::OpenAPI::toJsonValue(m_reward_value));
    }
    if (m_seller_id_isSet) {
        obj.insert(QString("sellerId"), ::OpenAPI::toJsonValue(m_seller_id));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_skuname_isSet) {
        obj.insert(QString("skuname"), ::OpenAPI::toJsonValue(m_skuname));
    }
    if (m_spot_price_isSet) {
        obj.insert(QString("spotPrice"), ::OpenAPI::toJsonValue(m_spot_price));
    }
    if (m_tax_as_int_isSet) {
        obj.insert(QString("taxAsInt"), ::OpenAPI::toJsonValue(m_tax_as_int));
    }
    if (m_tax_formated_isSet) {
        obj.insert(QString("taxFormated"), ::OpenAPI::toJsonValue(m_tax_formated));
    }
    if (m_unit_multiplier_isSet) {
        obj.insert(QString("unitMultiplier"), ::OpenAPI::toJsonValue(m_unit_multiplier));
    }
    return obj;
}

bool OAIProductVariations_200_response_skus_inner::isAvailable() const {
    return m_available;
}
void OAIProductVariations_200_response_skus_inner::setAvailable(const bool &available) {
    m_available = available;
    m_available_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_available_Set() const{
    return m_available_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_available_Valid() const{
    return m_available_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getAvailablequantity() const {
    return m_availablequantity;
}
void OAIProductVariations_200_response_skus_inner::setAvailablequantity(const qint32 &availablequantity) {
    m_availablequantity = availablequantity;
    m_availablequantity_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_availablequantity_Set() const{
    return m_availablequantity_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_availablequantity_Valid() const{
    return m_availablequantity_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getBestPrice() const {
    return m_best_price;
}
void OAIProductVariations_200_response_skus_inner::setBestPrice(const qint32 &best_price) {
    m_best_price = best_price;
    m_best_price_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_best_price_Set() const{
    return m_best_price_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_best_price_Valid() const{
    return m_best_price_isValid;
}

QString OAIProductVariations_200_response_skus_inner::getBestPriceFormated() const {
    return m_best_price_formated;
}
void OAIProductVariations_200_response_skus_inner::setBestPriceFormated(const QString &best_price_formated) {
    m_best_price_formated = best_price_formated;
    m_best_price_formated_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_best_price_formated_Set() const{
    return m_best_price_formated_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_best_price_formated_Valid() const{
    return m_best_price_formated_isValid;
}

QString OAIProductVariations_200_response_skus_inner::getCacheVersionUsedToCallCheckout() const {
    return m_cache_version_used_to_call_checkout;
}
void OAIProductVariations_200_response_skus_inner::setCacheVersionUsedToCallCheckout(const QString &cache_version_used_to_call_checkout) {
    m_cache_version_used_to_call_checkout = cache_version_used_to_call_checkout;
    m_cache_version_used_to_call_checkout_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_cache_version_used_to_call_checkout_Set() const{
    return m_cache_version_used_to_call_checkout_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_cache_version_used_to_call_checkout_Valid() const{
    return m_cache_version_used_to_call_checkout_isValid;
}

QMap<QString, QString> OAIProductVariations_200_response_skus_inner::getDimensions() const {
    return m_dimensions;
}
void OAIProductVariations_200_response_skus_inner::setDimensions(const QMap<QString, QString> &dimensions) {
    m_dimensions = dimensions;
    m_dimensions_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_dimensions_Set() const{
    return m_dimensions_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_dimensions_Valid() const{
    return m_dimensions_isValid;
}

QString OAIProductVariations_200_response_skus_inner::getImage() const {
    return m_image;
}
void OAIProductVariations_200_response_skus_inner::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_image_Set() const{
    return m_image_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_image_Valid() const{
    return m_image_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getInstallments() const {
    return m_installments;
}
void OAIProductVariations_200_response_skus_inner::setInstallments(const qint32 &installments) {
    m_installments = installments;
    m_installments_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_installments_Set() const{
    return m_installments_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_installments_Valid() const{
    return m_installments_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getInstallmentsInsterestRate() const {
    return m_installments_insterest_rate;
}
void OAIProductVariations_200_response_skus_inner::setInstallmentsInsterestRate(const qint32 &installments_insterest_rate) {
    m_installments_insterest_rate = installments_insterest_rate;
    m_installments_insterest_rate_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_installments_insterest_rate_Set() const{
    return m_installments_insterest_rate_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_installments_insterest_rate_Valid() const{
    return m_installments_insterest_rate_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getInstallmentsValue() const {
    return m_installments_value;
}
void OAIProductVariations_200_response_skus_inner::setInstallmentsValue(const qint32 &installments_value) {
    m_installments_value = installments_value;
    m_installments_value_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_installments_value_Set() const{
    return m_installments_value_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_installments_value_Valid() const{
    return m_installments_value_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getListPrice() const {
    return m_list_price;
}
void OAIProductVariations_200_response_skus_inner::setListPrice(const qint32 &list_price) {
    m_list_price = list_price;
    m_list_price_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_list_price_Set() const{
    return m_list_price_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_list_price_Valid() const{
    return m_list_price_isValid;
}

QString OAIProductVariations_200_response_skus_inner::getListPriceFormated() const {
    return m_list_price_formated;
}
void OAIProductVariations_200_response_skus_inner::setListPriceFormated(const QString &list_price_formated) {
    m_list_price_formated = list_price_formated;
    m_list_price_formated_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_list_price_formated_Set() const{
    return m_list_price_formated_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_list_price_formated_Valid() const{
    return m_list_price_formated_isValid;
}

OAIProductVariations_200_response_skus_inner_measures OAIProductVariations_200_response_skus_inner::getMeasures() const {
    return m_measures;
}
void OAIProductVariations_200_response_skus_inner::setMeasures(const OAIProductVariations_200_response_skus_inner_measures &measures) {
    m_measures = measures;
    m_measures_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_measures_Set() const{
    return m_measures_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_measures_Valid() const{
    return m_measures_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getRewardValue() const {
    return m_reward_value;
}
void OAIProductVariations_200_response_skus_inner::setRewardValue(const qint32 &reward_value) {
    m_reward_value = reward_value;
    m_reward_value_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_reward_value_Set() const{
    return m_reward_value_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_reward_value_Valid() const{
    return m_reward_value_isValid;
}

QString OAIProductVariations_200_response_skus_inner::getSellerId() const {
    return m_seller_id;
}
void OAIProductVariations_200_response_skus_inner::setSellerId(const QString &seller_id) {
    m_seller_id = seller_id;
    m_seller_id_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_seller_id_Set() const{
    return m_seller_id_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_seller_id_Valid() const{
    return m_seller_id_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getSku() const {
    return m_sku;
}
void OAIProductVariations_200_response_skus_inner::setSku(const qint32 &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_sku_Valid() const{
    return m_sku_isValid;
}

QString OAIProductVariations_200_response_skus_inner::getSkuname() const {
    return m_skuname;
}
void OAIProductVariations_200_response_skus_inner::setSkuname(const QString &skuname) {
    m_skuname = skuname;
    m_skuname_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_skuname_Set() const{
    return m_skuname_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_skuname_Valid() const{
    return m_skuname_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getSpotPrice() const {
    return m_spot_price;
}
void OAIProductVariations_200_response_skus_inner::setSpotPrice(const qint32 &spot_price) {
    m_spot_price = spot_price;
    m_spot_price_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_spot_price_Set() const{
    return m_spot_price_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_spot_price_Valid() const{
    return m_spot_price_isValid;
}

qint32 OAIProductVariations_200_response_skus_inner::getTaxAsInt() const {
    return m_tax_as_int;
}
void OAIProductVariations_200_response_skus_inner::setTaxAsInt(const qint32 &tax_as_int) {
    m_tax_as_int = tax_as_int;
    m_tax_as_int_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_tax_as_int_Set() const{
    return m_tax_as_int_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_tax_as_int_Valid() const{
    return m_tax_as_int_isValid;
}

QString OAIProductVariations_200_response_skus_inner::getTaxFormated() const {
    return m_tax_formated;
}
void OAIProductVariations_200_response_skus_inner::setTaxFormated(const QString &tax_formated) {
    m_tax_formated = tax_formated;
    m_tax_formated_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_tax_formated_Set() const{
    return m_tax_formated_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_tax_formated_Valid() const{
    return m_tax_formated_isValid;
}

double OAIProductVariations_200_response_skus_inner::getUnitMultiplier() const {
    return m_unit_multiplier;
}
void OAIProductVariations_200_response_skus_inner::setUnitMultiplier(const double &unit_multiplier) {
    m_unit_multiplier = unit_multiplier;
    m_unit_multiplier_isSet = true;
}

bool OAIProductVariations_200_response_skus_inner::is_unit_multiplier_Set() const{
    return m_unit_multiplier_isSet;
}

bool OAIProductVariations_200_response_skus_inner::is_unit_multiplier_Valid() const{
    return m_unit_multiplier_isValid;
}

bool OAIProductVariations_200_response_skus_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_availablequantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_best_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_best_price_formated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cache_version_used_to_call_checkout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dimensions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_installments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_installments_insterest_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_installments_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_list_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_list_price_formated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_measures.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_reward_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_skuname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spot_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_as_int_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_formated_isSet) {
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

bool OAIProductVariations_200_response_skus_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
