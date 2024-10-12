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

#include "OAIUpdateSellerRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateSellerRequest::OAIUpdateSellerRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateSellerRequest::OAIUpdateSellerRequest() {
    this->initializeModel();
}

OAIUpdateSellerRequest::~OAIUpdateSellerRequest() {}

void OAIUpdateSellerRequest::initializeModel() {

    m_archive_id_isSet = false;
    m_archive_id_isValid = false;

    m_cnpj_isSet = false;
    m_cnpj_isValid = false;

    m_csc_identification_isSet = false;
    m_csc_identification_isValid = false;

    m_catalog_system_endpoint_isSet = false;
    m_catalog_system_endpoint_isValid = false;

    m_category_commission_percentage_isSet = false;
    m_category_commission_percentage_isValid = false;

    m_delivery_policy_isSet = false;
    m_delivery_policy_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_exchange_return_policy_isSet = false;
    m_exchange_return_policy_isValid = false;

    m_freight_commission_percentage_isSet = false;
    m_freight_commission_percentage_isValid = false;

    m_fulfillment_endpoint_isSet = false;
    m_fulfillment_endpoint_isValid = false;

    m_fulfillment_seller_id_isSet = false;
    m_fulfillment_seller_id_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_better_scope_isSet = false;
    m_is_better_scope_isValid = false;

    m_merchant_name_isSet = false;
    m_merchant_name_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_product_commission_percentage_isSet = false;
    m_product_commission_percentage_isValid = false;

    m_secutity_privacy_policy_isSet = false;
    m_secutity_privacy_policy_isValid = false;

    m_seller_id_isSet = false;
    m_seller_id_isValid = false;

    m_seller_type_isSet = false;
    m_seller_type_isValid = false;

    m_trust_policy_isSet = false;
    m_trust_policy_isValid = false;

    m_url_logo_isSet = false;
    m_url_logo_isValid = false;

    m_use_hybrid_payment_options_isSet = false;
    m_use_hybrid_payment_options_isValid = false;

    m_user_name_isSet = false;
    m_user_name_isValid = false;
}

void OAIUpdateSellerRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateSellerRequest::fromJsonObject(QJsonObject json) {

    m_archive_id_isValid = ::OpenAPI::fromJsonValue(m_archive_id, json[QString("ArchiveId")]);
    m_archive_id_isSet = !json[QString("ArchiveId")].isNull() && m_archive_id_isValid;

    m_cnpj_isValid = ::OpenAPI::fromJsonValue(m_cnpj, json[QString("CNPJ")]);
    m_cnpj_isSet = !json[QString("CNPJ")].isNull() && m_cnpj_isValid;

    m_csc_identification_isValid = ::OpenAPI::fromJsonValue(m_csc_identification, json[QString("CSCIdentification")]);
    m_csc_identification_isSet = !json[QString("CSCIdentification")].isNull() && m_csc_identification_isValid;

    m_catalog_system_endpoint_isValid = ::OpenAPI::fromJsonValue(m_catalog_system_endpoint, json[QString("CatalogSystemEndpoint")]);
    m_catalog_system_endpoint_isSet = !json[QString("CatalogSystemEndpoint")].isNull() && m_catalog_system_endpoint_isValid;

    m_category_commission_percentage_isValid = ::OpenAPI::fromJsonValue(m_category_commission_percentage, json[QString("CategoryCommissionPercentage")]);
    m_category_commission_percentage_isSet = !json[QString("CategoryCommissionPercentage")].isNull() && m_category_commission_percentage_isValid;

    m_delivery_policy_isValid = ::OpenAPI::fromJsonValue(m_delivery_policy, json[QString("DeliveryPolicy")]);
    m_delivery_policy_isSet = !json[QString("DeliveryPolicy")].isNull() && m_delivery_policy_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("Email")]);
    m_email_isSet = !json[QString("Email")].isNull() && m_email_isValid;

    m_exchange_return_policy_isValid = ::OpenAPI::fromJsonValue(m_exchange_return_policy, json[QString("ExchangeReturnPolicy")]);
    m_exchange_return_policy_isSet = !json[QString("ExchangeReturnPolicy")].isNull() && m_exchange_return_policy_isValid;

    m_freight_commission_percentage_isValid = ::OpenAPI::fromJsonValue(m_freight_commission_percentage, json[QString("FreightCommissionPercentage")]);
    m_freight_commission_percentage_isSet = !json[QString("FreightCommissionPercentage")].isNull() && m_freight_commission_percentage_isValid;

    m_fulfillment_endpoint_isValid = ::OpenAPI::fromJsonValue(m_fulfillment_endpoint, json[QString("FulfillmentEndpoint")]);
    m_fulfillment_endpoint_isSet = !json[QString("FulfillmentEndpoint")].isNull() && m_fulfillment_endpoint_isValid;

    m_fulfillment_seller_id_isValid = ::OpenAPI::fromJsonValue(m_fulfillment_seller_id, json[QString("FulfillmentSellerId")]);
    m_fulfillment_seller_id_isSet = !json[QString("FulfillmentSellerId")].isNull() && m_fulfillment_seller_id_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("IsActive")]);
    m_is_active_isSet = !json[QString("IsActive")].isNull() && m_is_active_isValid;

    m_is_better_scope_isValid = ::OpenAPI::fromJsonValue(m_is_better_scope, json[QString("IsBetterScope")]);
    m_is_better_scope_isSet = !json[QString("IsBetterScope")].isNull() && m_is_better_scope_isValid;

    m_merchant_name_isValid = ::OpenAPI::fromJsonValue(m_merchant_name, json[QString("MerchantName")]);
    m_merchant_name_isSet = !json[QString("MerchantName")].isNull() && m_merchant_name_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("Password")]);
    m_password_isSet = !json[QString("Password")].isNull() && m_password_isValid;

    m_product_commission_percentage_isValid = ::OpenAPI::fromJsonValue(m_product_commission_percentage, json[QString("ProductCommissionPercentage")]);
    m_product_commission_percentage_isSet = !json[QString("ProductCommissionPercentage")].isNull() && m_product_commission_percentage_isValid;

    m_secutity_privacy_policy_isValid = ::OpenAPI::fromJsonValue(m_secutity_privacy_policy, json[QString("SecutityPrivacyPolicy")]);
    m_secutity_privacy_policy_isSet = !json[QString("SecutityPrivacyPolicy")].isNull() && m_secutity_privacy_policy_isValid;

    m_seller_id_isValid = ::OpenAPI::fromJsonValue(m_seller_id, json[QString("SellerId")]);
    m_seller_id_isSet = !json[QString("SellerId")].isNull() && m_seller_id_isValid;

    m_seller_type_isValid = ::OpenAPI::fromJsonValue(m_seller_type, json[QString("SellerType")]);
    m_seller_type_isSet = !json[QString("SellerType")].isNull() && m_seller_type_isValid;

    m_trust_policy_isValid = ::OpenAPI::fromJsonValue(m_trust_policy, json[QString("TrustPolicy")]);
    m_trust_policy_isSet = !json[QString("TrustPolicy")].isNull() && m_trust_policy_isValid;

    m_url_logo_isValid = ::OpenAPI::fromJsonValue(m_url_logo, json[QString("UrlLogo")]);
    m_url_logo_isSet = !json[QString("UrlLogo")].isNull() && m_url_logo_isValid;

    m_use_hybrid_payment_options_isValid = ::OpenAPI::fromJsonValue(m_use_hybrid_payment_options, json[QString("UseHybridPaymentOptions")]);
    m_use_hybrid_payment_options_isSet = !json[QString("UseHybridPaymentOptions")].isNull() && m_use_hybrid_payment_options_isValid;

    m_user_name_isValid = ::OpenAPI::fromJsonValue(m_user_name, json[QString("UserName")]);
    m_user_name_isSet = !json[QString("UserName")].isNull() && m_user_name_isValid;
}

QString OAIUpdateSellerRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateSellerRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_archive_id_isSet) {
        obj.insert(QString("ArchiveId"), ::OpenAPI::toJsonValue(m_archive_id));
    }
    if (m_cnpj_isSet) {
        obj.insert(QString("CNPJ"), ::OpenAPI::toJsonValue(m_cnpj));
    }
    if (m_csc_identification_isSet) {
        obj.insert(QString("CSCIdentification"), ::OpenAPI::toJsonValue(m_csc_identification));
    }
    if (m_catalog_system_endpoint_isSet) {
        obj.insert(QString("CatalogSystemEndpoint"), ::OpenAPI::toJsonValue(m_catalog_system_endpoint));
    }
    if (m_category_commission_percentage_isSet) {
        obj.insert(QString("CategoryCommissionPercentage"), ::OpenAPI::toJsonValue(m_category_commission_percentage));
    }
    if (m_delivery_policy_isSet) {
        obj.insert(QString("DeliveryPolicy"), ::OpenAPI::toJsonValue(m_delivery_policy));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_email_isSet) {
        obj.insert(QString("Email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_exchange_return_policy_isSet) {
        obj.insert(QString("ExchangeReturnPolicy"), ::OpenAPI::toJsonValue(m_exchange_return_policy));
    }
    if (m_freight_commission_percentage_isSet) {
        obj.insert(QString("FreightCommissionPercentage"), ::OpenAPI::toJsonValue(m_freight_commission_percentage));
    }
    if (m_fulfillment_endpoint_isSet) {
        obj.insert(QString("FulfillmentEndpoint"), ::OpenAPI::toJsonValue(m_fulfillment_endpoint));
    }
    if (m_fulfillment_seller_id_isSet) {
        obj.insert(QString("FulfillmentSellerId"), ::OpenAPI::toJsonValue(m_fulfillment_seller_id));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("IsActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_better_scope_isSet) {
        obj.insert(QString("IsBetterScope"), ::OpenAPI::toJsonValue(m_is_better_scope));
    }
    if (m_merchant_name_isSet) {
        obj.insert(QString("MerchantName"), ::OpenAPI::toJsonValue(m_merchant_name));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_password_isSet) {
        obj.insert(QString("Password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_product_commission_percentage_isSet) {
        obj.insert(QString("ProductCommissionPercentage"), ::OpenAPI::toJsonValue(m_product_commission_percentage));
    }
    if (m_secutity_privacy_policy_isSet) {
        obj.insert(QString("SecutityPrivacyPolicy"), ::OpenAPI::toJsonValue(m_secutity_privacy_policy));
    }
    if (m_seller_id_isSet) {
        obj.insert(QString("SellerId"), ::OpenAPI::toJsonValue(m_seller_id));
    }
    if (m_seller_type_isSet) {
        obj.insert(QString("SellerType"), ::OpenAPI::toJsonValue(m_seller_type));
    }
    if (m_trust_policy_isSet) {
        obj.insert(QString("TrustPolicy"), ::OpenAPI::toJsonValue(m_trust_policy));
    }
    if (m_url_logo_isSet) {
        obj.insert(QString("UrlLogo"), ::OpenAPI::toJsonValue(m_url_logo));
    }
    if (m_use_hybrid_payment_options_isSet) {
        obj.insert(QString("UseHybridPaymentOptions"), ::OpenAPI::toJsonValue(m_use_hybrid_payment_options));
    }
    if (m_user_name_isSet) {
        obj.insert(QString("UserName"), ::OpenAPI::toJsonValue(m_user_name));
    }
    return obj;
}

qint32 OAIUpdateSellerRequest::getArchiveId() const {
    return m_archive_id;
}
void OAIUpdateSellerRequest::setArchiveId(const qint32 &archive_id) {
    m_archive_id = archive_id;
    m_archive_id_isSet = true;
}

bool OAIUpdateSellerRequest::is_archive_id_Set() const{
    return m_archive_id_isSet;
}

bool OAIUpdateSellerRequest::is_archive_id_Valid() const{
    return m_archive_id_isValid;
}

QString OAIUpdateSellerRequest::getCnpj() const {
    return m_cnpj;
}
void OAIUpdateSellerRequest::setCnpj(const QString &cnpj) {
    m_cnpj = cnpj;
    m_cnpj_isSet = true;
}

bool OAIUpdateSellerRequest::is_cnpj_Set() const{
    return m_cnpj_isSet;
}

bool OAIUpdateSellerRequest::is_cnpj_Valid() const{
    return m_cnpj_isValid;
}

QString OAIUpdateSellerRequest::getCscIdentification() const {
    return m_csc_identification;
}
void OAIUpdateSellerRequest::setCscIdentification(const QString &csc_identification) {
    m_csc_identification = csc_identification;
    m_csc_identification_isSet = true;
}

bool OAIUpdateSellerRequest::is_csc_identification_Set() const{
    return m_csc_identification_isSet;
}

bool OAIUpdateSellerRequest::is_csc_identification_Valid() const{
    return m_csc_identification_isValid;
}

QString OAIUpdateSellerRequest::getCatalogSystemEndpoint() const {
    return m_catalog_system_endpoint;
}
void OAIUpdateSellerRequest::setCatalogSystemEndpoint(const QString &catalog_system_endpoint) {
    m_catalog_system_endpoint = catalog_system_endpoint;
    m_catalog_system_endpoint_isSet = true;
}

bool OAIUpdateSellerRequest::is_catalog_system_endpoint_Set() const{
    return m_catalog_system_endpoint_isSet;
}

bool OAIUpdateSellerRequest::is_catalog_system_endpoint_Valid() const{
    return m_catalog_system_endpoint_isValid;
}

QString OAIUpdateSellerRequest::getCategoryCommissionPercentage() const {
    return m_category_commission_percentage;
}
void OAIUpdateSellerRequest::setCategoryCommissionPercentage(const QString &category_commission_percentage) {
    m_category_commission_percentage = category_commission_percentage;
    m_category_commission_percentage_isSet = true;
}

bool OAIUpdateSellerRequest::is_category_commission_percentage_Set() const{
    return m_category_commission_percentage_isSet;
}

bool OAIUpdateSellerRequest::is_category_commission_percentage_Valid() const{
    return m_category_commission_percentage_isValid;
}

QString OAIUpdateSellerRequest::getDeliveryPolicy() const {
    return m_delivery_policy;
}
void OAIUpdateSellerRequest::setDeliveryPolicy(const QString &delivery_policy) {
    m_delivery_policy = delivery_policy;
    m_delivery_policy_isSet = true;
}

bool OAIUpdateSellerRequest::is_delivery_policy_Set() const{
    return m_delivery_policy_isSet;
}

bool OAIUpdateSellerRequest::is_delivery_policy_Valid() const{
    return m_delivery_policy_isValid;
}

QString OAIUpdateSellerRequest::getDescription() const {
    return m_description;
}
void OAIUpdateSellerRequest::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIUpdateSellerRequest::is_description_Set() const{
    return m_description_isSet;
}

bool OAIUpdateSellerRequest::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIUpdateSellerRequest::getEmail() const {
    return m_email;
}
void OAIUpdateSellerRequest::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUpdateSellerRequest::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUpdateSellerRequest::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIUpdateSellerRequest::getExchangeReturnPolicy() const {
    return m_exchange_return_policy;
}
void OAIUpdateSellerRequest::setExchangeReturnPolicy(const QString &exchange_return_policy) {
    m_exchange_return_policy = exchange_return_policy;
    m_exchange_return_policy_isSet = true;
}

bool OAIUpdateSellerRequest::is_exchange_return_policy_Set() const{
    return m_exchange_return_policy_isSet;
}

bool OAIUpdateSellerRequest::is_exchange_return_policy_Valid() const{
    return m_exchange_return_policy_isValid;
}

double OAIUpdateSellerRequest::getFreightCommissionPercentage() const {
    return m_freight_commission_percentage;
}
void OAIUpdateSellerRequest::setFreightCommissionPercentage(const double &freight_commission_percentage) {
    m_freight_commission_percentage = freight_commission_percentage;
    m_freight_commission_percentage_isSet = true;
}

bool OAIUpdateSellerRequest::is_freight_commission_percentage_Set() const{
    return m_freight_commission_percentage_isSet;
}

bool OAIUpdateSellerRequest::is_freight_commission_percentage_Valid() const{
    return m_freight_commission_percentage_isValid;
}

QString OAIUpdateSellerRequest::getFulfillmentEndpoint() const {
    return m_fulfillment_endpoint;
}
void OAIUpdateSellerRequest::setFulfillmentEndpoint(const QString &fulfillment_endpoint) {
    m_fulfillment_endpoint = fulfillment_endpoint;
    m_fulfillment_endpoint_isSet = true;
}

bool OAIUpdateSellerRequest::is_fulfillment_endpoint_Set() const{
    return m_fulfillment_endpoint_isSet;
}

bool OAIUpdateSellerRequest::is_fulfillment_endpoint_Valid() const{
    return m_fulfillment_endpoint_isValid;
}

qint32 OAIUpdateSellerRequest::getFulfillmentSellerId() const {
    return m_fulfillment_seller_id;
}
void OAIUpdateSellerRequest::setFulfillmentSellerId(const qint32 &fulfillment_seller_id) {
    m_fulfillment_seller_id = fulfillment_seller_id;
    m_fulfillment_seller_id_isSet = true;
}

bool OAIUpdateSellerRequest::is_fulfillment_seller_id_Set() const{
    return m_fulfillment_seller_id_isSet;
}

bool OAIUpdateSellerRequest::is_fulfillment_seller_id_Valid() const{
    return m_fulfillment_seller_id_isValid;
}

bool OAIUpdateSellerRequest::isIsActive() const {
    return m_is_active;
}
void OAIUpdateSellerRequest::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIUpdateSellerRequest::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIUpdateSellerRequest::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAIUpdateSellerRequest::isIsBetterScope() const {
    return m_is_better_scope;
}
void OAIUpdateSellerRequest::setIsBetterScope(const bool &is_better_scope) {
    m_is_better_scope = is_better_scope;
    m_is_better_scope_isSet = true;
}

bool OAIUpdateSellerRequest::is_is_better_scope_Set() const{
    return m_is_better_scope_isSet;
}

bool OAIUpdateSellerRequest::is_is_better_scope_Valid() const{
    return m_is_better_scope_isValid;
}

QString OAIUpdateSellerRequest::getMerchantName() const {
    return m_merchant_name;
}
void OAIUpdateSellerRequest::setMerchantName(const QString &merchant_name) {
    m_merchant_name = merchant_name;
    m_merchant_name_isSet = true;
}

bool OAIUpdateSellerRequest::is_merchant_name_Set() const{
    return m_merchant_name_isSet;
}

bool OAIUpdateSellerRequest::is_merchant_name_Valid() const{
    return m_merchant_name_isValid;
}

QString OAIUpdateSellerRequest::getName() const {
    return m_name;
}
void OAIUpdateSellerRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateSellerRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateSellerRequest::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIUpdateSellerRequest::getPassword() const {
    return m_password;
}
void OAIUpdateSellerRequest::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIUpdateSellerRequest::is_password_Set() const{
    return m_password_isSet;
}

bool OAIUpdateSellerRequest::is_password_Valid() const{
    return m_password_isValid;
}

double OAIUpdateSellerRequest::getProductCommissionPercentage() const {
    return m_product_commission_percentage;
}
void OAIUpdateSellerRequest::setProductCommissionPercentage(const double &product_commission_percentage) {
    m_product_commission_percentage = product_commission_percentage;
    m_product_commission_percentage_isSet = true;
}

bool OAIUpdateSellerRequest::is_product_commission_percentage_Set() const{
    return m_product_commission_percentage_isSet;
}

bool OAIUpdateSellerRequest::is_product_commission_percentage_Valid() const{
    return m_product_commission_percentage_isValid;
}

QString OAIUpdateSellerRequest::getSecutityPrivacyPolicy() const {
    return m_secutity_privacy_policy;
}
void OAIUpdateSellerRequest::setSecutityPrivacyPolicy(const QString &secutity_privacy_policy) {
    m_secutity_privacy_policy = secutity_privacy_policy;
    m_secutity_privacy_policy_isSet = true;
}

bool OAIUpdateSellerRequest::is_secutity_privacy_policy_Set() const{
    return m_secutity_privacy_policy_isSet;
}

bool OAIUpdateSellerRequest::is_secutity_privacy_policy_Valid() const{
    return m_secutity_privacy_policy_isValid;
}

QString OAIUpdateSellerRequest::getSellerId() const {
    return m_seller_id;
}
void OAIUpdateSellerRequest::setSellerId(const QString &seller_id) {
    m_seller_id = seller_id;
    m_seller_id_isSet = true;
}

bool OAIUpdateSellerRequest::is_seller_id_Set() const{
    return m_seller_id_isSet;
}

bool OAIUpdateSellerRequest::is_seller_id_Valid() const{
    return m_seller_id_isValid;
}

qint32 OAIUpdateSellerRequest::getSellerType() const {
    return m_seller_type;
}
void OAIUpdateSellerRequest::setSellerType(const qint32 &seller_type) {
    m_seller_type = seller_type;
    m_seller_type_isSet = true;
}

bool OAIUpdateSellerRequest::is_seller_type_Set() const{
    return m_seller_type_isSet;
}

bool OAIUpdateSellerRequest::is_seller_type_Valid() const{
    return m_seller_type_isValid;
}

QString OAIUpdateSellerRequest::getTrustPolicy() const {
    return m_trust_policy;
}
void OAIUpdateSellerRequest::setTrustPolicy(const QString &trust_policy) {
    m_trust_policy = trust_policy;
    m_trust_policy_isSet = true;
}

bool OAIUpdateSellerRequest::is_trust_policy_Set() const{
    return m_trust_policy_isSet;
}

bool OAIUpdateSellerRequest::is_trust_policy_Valid() const{
    return m_trust_policy_isValid;
}

QString OAIUpdateSellerRequest::getUrlLogo() const {
    return m_url_logo;
}
void OAIUpdateSellerRequest::setUrlLogo(const QString &url_logo) {
    m_url_logo = url_logo;
    m_url_logo_isSet = true;
}

bool OAIUpdateSellerRequest::is_url_logo_Set() const{
    return m_url_logo_isSet;
}

bool OAIUpdateSellerRequest::is_url_logo_Valid() const{
    return m_url_logo_isValid;
}

bool OAIUpdateSellerRequest::isUseHybridPaymentOptions() const {
    return m_use_hybrid_payment_options;
}
void OAIUpdateSellerRequest::setUseHybridPaymentOptions(const bool &use_hybrid_payment_options) {
    m_use_hybrid_payment_options = use_hybrid_payment_options;
    m_use_hybrid_payment_options_isSet = true;
}

bool OAIUpdateSellerRequest::is_use_hybrid_payment_options_Set() const{
    return m_use_hybrid_payment_options_isSet;
}

bool OAIUpdateSellerRequest::is_use_hybrid_payment_options_Valid() const{
    return m_use_hybrid_payment_options_isValid;
}

QString OAIUpdateSellerRequest::getUserName() const {
    return m_user_name;
}
void OAIUpdateSellerRequest::setUserName(const QString &user_name) {
    m_user_name = user_name;
    m_user_name_isSet = true;
}

bool OAIUpdateSellerRequest::is_user_name_Set() const{
    return m_user_name_isSet;
}

bool OAIUpdateSellerRequest::is_user_name_Valid() const{
    return m_user_name_isValid;
}

bool OAIUpdateSellerRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_archive_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cnpj_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_csc_identification_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_catalog_system_endpoint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_category_commission_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_policy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exchange_return_policy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_freight_commission_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fulfillment_endpoint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fulfillment_seller_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_better_scope_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_commission_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secutity_privacy_policy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trust_policy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_logo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_hybrid_payment_options_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateSellerRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_archive_id_isValid && m_cnpj_isValid && m_csc_identification_isValid && m_catalog_system_endpoint_isValid && m_delivery_policy_isValid && m_description_isValid && m_email_isValid && m_exchange_return_policy_isValid && m_freight_commission_percentage_isValid && m_fulfillment_endpoint_isValid && m_fulfillment_seller_id_isValid && m_is_active_isValid && m_is_better_scope_isValid && m_name_isValid && m_password_isValid && m_product_commission_percentage_isValid && m_secutity_privacy_policy_isValid && m_seller_id_isValid && m_seller_type_isValid && m_url_logo_isValid && m_use_hybrid_payment_options_isValid && m_user_name_isValid && true;
}

} // namespace OpenAPI
