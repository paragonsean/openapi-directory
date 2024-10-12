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

#include "OAI_api_catalog_pvt_attachments_get_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_catalog_pvt_attachments_get_200_response::OAI_api_catalog_pvt_attachments_get_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_catalog_pvt_attachments_get_200_response::OAI_api_catalog_pvt_attachments_get_200_response() {
    this->initializeModel();
}

OAI_api_catalog_pvt_attachments_get_200_response::~OAI_api_catalog_pvt_attachments_get_200_response() {}

void OAI_api_catalog_pvt_attachments_get_200_response::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_page_isSet = false;
    m_page_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_total_page_isSet = false;
    m_total_page_isValid = false;

    m_total_rows_isSet = false;
    m_total_rows_isValid = false;
}

void OAI_api_catalog_pvt_attachments_get_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_catalog_pvt_attachments_get_200_response::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("Data")]);
    m_data_isSet = !json[QString("Data")].isNull() && m_data_isValid;

    m_page_isValid = ::OpenAPI::fromJsonValue(m_page, json[QString("Page")]);
    m_page_isSet = !json[QString("Page")].isNull() && m_page_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("Size")]);
    m_size_isSet = !json[QString("Size")].isNull() && m_size_isValid;

    m_total_page_isValid = ::OpenAPI::fromJsonValue(m_total_page, json[QString("TotalPage")]);
    m_total_page_isSet = !json[QString("TotalPage")].isNull() && m_total_page_isValid;

    m_total_rows_isValid = ::OpenAPI::fromJsonValue(m_total_rows, json[QString("TotalRows")]);
    m_total_rows_isSet = !json[QString("TotalRows")].isNull() && m_total_rows_isValid;
}

QString OAI_api_catalog_pvt_attachments_get_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_catalog_pvt_attachments_get_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_data.size() > 0) {
        obj.insert(QString("Data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_page_isSet) {
        obj.insert(QString("Page"), ::OpenAPI::toJsonValue(m_page));
    }
    if (m_size_isSet) {
        obj.insert(QString("Size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_total_page_isSet) {
        obj.insert(QString("TotalPage"), ::OpenAPI::toJsonValue(m_total_page));
    }
    if (m_total_rows_isSet) {
        obj.insert(QString("TotalRows"), ::OpenAPI::toJsonValue(m_total_rows));
    }
    return obj;
}

QList<OAIAttachmentResponse> OAI_api_catalog_pvt_attachments_get_200_response::getData() const {
    return m_data;
}
void OAI_api_catalog_pvt_attachments_get_200_response::setData(const QList<OAIAttachmentResponse> &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_data_Set() const{
    return m_data_isSet;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_data_Valid() const{
    return m_data_isValid;
}

qint32 OAI_api_catalog_pvt_attachments_get_200_response::getPage() const {
    return m_page;
}
void OAI_api_catalog_pvt_attachments_get_200_response::setPage(const qint32 &page) {
    m_page = page;
    m_page_isSet = true;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_page_Set() const{
    return m_page_isSet;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_page_Valid() const{
    return m_page_isValid;
}

qint32 OAI_api_catalog_pvt_attachments_get_200_response::getSize() const {
    return m_size;
}
void OAI_api_catalog_pvt_attachments_get_200_response::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_size_Set() const{
    return m_size_isSet;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_size_Valid() const{
    return m_size_isValid;
}

qint32 OAI_api_catalog_pvt_attachments_get_200_response::getTotalPage() const {
    return m_total_page;
}
void OAI_api_catalog_pvt_attachments_get_200_response::setTotalPage(const qint32 &total_page) {
    m_total_page = total_page;
    m_total_page_isSet = true;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_total_page_Set() const{
    return m_total_page_isSet;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_total_page_Valid() const{
    return m_total_page_isValid;
}

qint32 OAI_api_catalog_pvt_attachments_get_200_response::getTotalRows() const {
    return m_total_rows;
}
void OAI_api_catalog_pvt_attachments_get_200_response::setTotalRows(const qint32 &total_rows) {
    m_total_rows = total_rows;
    m_total_rows_isSet = true;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_total_rows_Set() const{
    return m_total_rows_isSet;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::is_total_rows_Valid() const{
    return m_total_rows_isValid;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_rows_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_api_catalog_pvt_attachments_get_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
