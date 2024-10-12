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

#include "OAI_api_catalog_pvt_collection_post_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_catalog_pvt_collection_post_200_response::OAI_api_catalog_pvt_collection_post_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_catalog_pvt_collection_post_200_response::OAI_api_catalog_pvt_collection_post_200_response() {
    this->initializeModel();
}

OAI_api_catalog_pvt_collection_post_200_response::~OAI_api_catalog_pvt_collection_post_200_response() {}

void OAI_api_catalog_pvt_collection_post_200_response::initializeModel() {

    m_date_from_isSet = false;
    m_date_from_isValid = false;

    m_date_to_isSet = false;
    m_date_to_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_highlight_isSet = false;
    m_highlight_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_searchable_isSet = false;
    m_searchable_isValid = false;

    m_total_products_isSet = false;
    m_total_products_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAI_api_catalog_pvt_collection_post_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_catalog_pvt_collection_post_200_response::fromJsonObject(QJsonObject json) {

    m_date_from_isValid = ::OpenAPI::fromJsonValue(m_date_from, json[QString("DateFrom")]);
    m_date_from_isSet = !json[QString("DateFrom")].isNull() && m_date_from_isValid;

    m_date_to_isValid = ::OpenAPI::fromJsonValue(m_date_to, json[QString("DateTo")]);
    m_date_to_isSet = !json[QString("DateTo")].isNull() && m_date_to_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_highlight_isValid = ::OpenAPI::fromJsonValue(m_highlight, json[QString("Highlight")]);
    m_highlight_isSet = !json[QString("Highlight")].isNull() && m_highlight_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_searchable_isValid = ::OpenAPI::fromJsonValue(m_searchable, json[QString("Searchable")]);
    m_searchable_isSet = !json[QString("Searchable")].isNull() && m_searchable_isValid;

    m_total_products_isValid = ::OpenAPI::fromJsonValue(m_total_products, json[QString("TotalProducts")]);
    m_total_products_isSet = !json[QString("TotalProducts")].isNull() && m_total_products_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;
}

QString OAI_api_catalog_pvt_collection_post_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_catalog_pvt_collection_post_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_date_from_isSet) {
        obj.insert(QString("DateFrom"), ::OpenAPI::toJsonValue(m_date_from));
    }
    if (m_date_to_isSet) {
        obj.insert(QString("DateTo"), ::OpenAPI::toJsonValue(m_date_to));
    }
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_highlight_isSet) {
        obj.insert(QString("Highlight"), ::OpenAPI::toJsonValue(m_highlight));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_searchable_isSet) {
        obj.insert(QString("Searchable"), ::OpenAPI::toJsonValue(m_searchable));
    }
    if (m_total_products_isSet) {
        obj.insert(QString("TotalProducts"), ::OpenAPI::toJsonValue(m_total_products));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAI_api_catalog_pvt_collection_post_200_response::getDateFrom() const {
    return m_date_from;
}
void OAI_api_catalog_pvt_collection_post_200_response::setDateFrom(const QString &date_from) {
    m_date_from = date_from;
    m_date_from_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_date_from_Set() const{
    return m_date_from_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_date_from_Valid() const{
    return m_date_from_isValid;
}

QString OAI_api_catalog_pvt_collection_post_200_response::getDateTo() const {
    return m_date_to;
}
void OAI_api_catalog_pvt_collection_post_200_response::setDateTo(const QString &date_to) {
    m_date_to = date_to;
    m_date_to_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_date_to_Set() const{
    return m_date_to_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_date_to_Valid() const{
    return m_date_to_isValid;
}

QString OAI_api_catalog_pvt_collection_post_200_response::getDescription() const {
    return m_description;
}
void OAI_api_catalog_pvt_collection_post_200_response::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_description_Set() const{
    return m_description_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_description_Valid() const{
    return m_description_isValid;
}

bool OAI_api_catalog_pvt_collection_post_200_response::isHighlight() const {
    return m_highlight;
}
void OAI_api_catalog_pvt_collection_post_200_response::setHighlight(const bool &highlight) {
    m_highlight = highlight;
    m_highlight_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_highlight_Set() const{
    return m_highlight_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_highlight_Valid() const{
    return m_highlight_isValid;
}

qint32 OAI_api_catalog_pvt_collection_post_200_response::getId() const {
    return m_id;
}
void OAI_api_catalog_pvt_collection_post_200_response::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_id_Valid() const{
    return m_id_isValid;
}

QString OAI_api_catalog_pvt_collection_post_200_response::getName() const {
    return m_name;
}
void OAI_api_catalog_pvt_collection_post_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_name_Valid() const{
    return m_name_isValid;
}

bool OAI_api_catalog_pvt_collection_post_200_response::isSearchable() const {
    return m_searchable;
}
void OAI_api_catalog_pvt_collection_post_200_response::setSearchable(const bool &searchable) {
    m_searchable = searchable;
    m_searchable_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_searchable_Set() const{
    return m_searchable_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_searchable_Valid() const{
    return m_searchable_isValid;
}

qint32 OAI_api_catalog_pvt_collection_post_200_response::getTotalProducts() const {
    return m_total_products;
}
void OAI_api_catalog_pvt_collection_post_200_response::setTotalProducts(const qint32 &total_products) {
    m_total_products = total_products;
    m_total_products_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_total_products_Set() const{
    return m_total_products_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_total_products_Valid() const{
    return m_total_products_isValid;
}

QString OAI_api_catalog_pvt_collection_post_200_response::getType() const {
    return m_type;
}
void OAI_api_catalog_pvt_collection_post_200_response::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_type_Set() const{
    return m_type_isSet;
}

bool OAI_api_catalog_pvt_collection_post_200_response::is_type_Valid() const{
    return m_type_isValid;
}

bool OAI_api_catalog_pvt_collection_post_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_date_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_highlight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_searchable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_products_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_api_catalog_pvt_collection_post_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
