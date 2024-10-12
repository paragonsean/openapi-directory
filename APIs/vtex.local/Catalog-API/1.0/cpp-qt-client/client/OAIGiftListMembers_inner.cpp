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

#include "OAIGiftListMembers_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGiftListMembers_inner::OAIGiftListMembers_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGiftListMembers_inner::OAIGiftListMembers_inner() {
    this->initializeModel();
}

OAIGiftListMembers_inner::~OAIGiftListMembers_inner() {}

void OAIGiftListMembers_inner::initializeModel() {

    m_client_id_isSet = false;
    m_client_id_isValid = false;

    m_gift_list_id_isSet = false;
    m_gift_list_id_isValid = false;

    m_gift_list_member_id_isSet = false;
    m_gift_list_member_id_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_admin_isSet = false;
    m_is_admin_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_surname_isSet = false;
    m_surname_isValid = false;

    m_text1_isSet = false;
    m_text1_isValid = false;

    m_text2_isSet = false;
    m_text2_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIGiftListMembers_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGiftListMembers_inner::fromJsonObject(QJsonObject json) {

    m_client_id_isValid = ::OpenAPI::fromJsonValue(m_client_id, json[QString("clientId")]);
    m_client_id_isSet = !json[QString("clientId")].isNull() && m_client_id_isValid;

    m_gift_list_id_isValid = ::OpenAPI::fromJsonValue(m_gift_list_id, json[QString("giftListId")]);
    m_gift_list_id_isSet = !json[QString("giftListId")].isNull() && m_gift_list_id_isValid;

    m_gift_list_member_id_isValid = ::OpenAPI::fromJsonValue(m_gift_list_member_id, json[QString("giftListMemberId")]);
    m_gift_list_member_id_isSet = !json[QString("giftListMemberId")].isNull() && m_gift_list_member_id_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("isActive")]);
    m_is_active_isSet = !json[QString("isActive")].isNull() && m_is_active_isValid;

    m_is_admin_isValid = ::OpenAPI::fromJsonValue(m_is_admin, json[QString("isAdmin")]);
    m_is_admin_isSet = !json[QString("isAdmin")].isNull() && m_is_admin_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_surname_isValid = ::OpenAPI::fromJsonValue(m_surname, json[QString("surname")]);
    m_surname_isSet = !json[QString("surname")].isNull() && m_surname_isValid;

    m_text1_isValid = ::OpenAPI::fromJsonValue(m_text1, json[QString("text1")]);
    m_text1_isSet = !json[QString("text1")].isNull() && m_text1_isValid;

    m_text2_isValid = ::OpenAPI::fromJsonValue(m_text2, json[QString("text2")]);
    m_text2_isSet = !json[QString("text2")].isNull() && m_text2_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("userId")]);
    m_user_id_isSet = !json[QString("userId")].isNull() && m_user_id_isValid;
}

QString OAIGiftListMembers_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGiftListMembers_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_client_id_isSet) {
        obj.insert(QString("clientId"), ::OpenAPI::toJsonValue(m_client_id));
    }
    if (m_gift_list_id_isSet) {
        obj.insert(QString("giftListId"), ::OpenAPI::toJsonValue(m_gift_list_id));
    }
    if (m_gift_list_member_id_isSet) {
        obj.insert(QString("giftListMemberId"), ::OpenAPI::toJsonValue(m_gift_list_member_id));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("isActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_admin_isSet) {
        obj.insert(QString("isAdmin"), ::OpenAPI::toJsonValue(m_is_admin));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_surname_isSet) {
        obj.insert(QString("surname"), ::OpenAPI::toJsonValue(m_surname));
    }
    if (m_text1_isSet) {
        obj.insert(QString("text1"), ::OpenAPI::toJsonValue(m_text1));
    }
    if (m_text2_isSet) {
        obj.insert(QString("text2"), ::OpenAPI::toJsonValue(m_text2));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("userId"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIGiftListMembers_inner::getClientId() const {
    return m_client_id;
}
void OAIGiftListMembers_inner::setClientId(const QString &client_id) {
    m_client_id = client_id;
    m_client_id_isSet = true;
}

bool OAIGiftListMembers_inner::is_client_id_Set() const{
    return m_client_id_isSet;
}

bool OAIGiftListMembers_inner::is_client_id_Valid() const{
    return m_client_id_isValid;
}

qint32 OAIGiftListMembers_inner::getGiftListId() const {
    return m_gift_list_id;
}
void OAIGiftListMembers_inner::setGiftListId(const qint32 &gift_list_id) {
    m_gift_list_id = gift_list_id;
    m_gift_list_id_isSet = true;
}

bool OAIGiftListMembers_inner::is_gift_list_id_Set() const{
    return m_gift_list_id_isSet;
}

bool OAIGiftListMembers_inner::is_gift_list_id_Valid() const{
    return m_gift_list_id_isValid;
}

qint32 OAIGiftListMembers_inner::getGiftListMemberId() const {
    return m_gift_list_member_id;
}
void OAIGiftListMembers_inner::setGiftListMemberId(const qint32 &gift_list_member_id) {
    m_gift_list_member_id = gift_list_member_id;
    m_gift_list_member_id_isSet = true;
}

bool OAIGiftListMembers_inner::is_gift_list_member_id_Set() const{
    return m_gift_list_member_id_isSet;
}

bool OAIGiftListMembers_inner::is_gift_list_member_id_Valid() const{
    return m_gift_list_member_id_isValid;
}

bool OAIGiftListMembers_inner::isIsActive() const {
    return m_is_active;
}
void OAIGiftListMembers_inner::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIGiftListMembers_inner::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIGiftListMembers_inner::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAIGiftListMembers_inner::isIsAdmin() const {
    return m_is_admin;
}
void OAIGiftListMembers_inner::setIsAdmin(const bool &is_admin) {
    m_is_admin = is_admin;
    m_is_admin_isSet = true;
}

bool OAIGiftListMembers_inner::is_is_admin_Set() const{
    return m_is_admin_isSet;
}

bool OAIGiftListMembers_inner::is_is_admin_Valid() const{
    return m_is_admin_isValid;
}

QString OAIGiftListMembers_inner::getName() const {
    return m_name;
}
void OAIGiftListMembers_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGiftListMembers_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGiftListMembers_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGiftListMembers_inner::getSurname() const {
    return m_surname;
}
void OAIGiftListMembers_inner::setSurname(const QString &surname) {
    m_surname = surname;
    m_surname_isSet = true;
}

bool OAIGiftListMembers_inner::is_surname_Set() const{
    return m_surname_isSet;
}

bool OAIGiftListMembers_inner::is_surname_Valid() const{
    return m_surname_isValid;
}

QString OAIGiftListMembers_inner::getText1() const {
    return m_text1;
}
void OAIGiftListMembers_inner::setText1(const QString &text1) {
    m_text1 = text1;
    m_text1_isSet = true;
}

bool OAIGiftListMembers_inner::is_text1_Set() const{
    return m_text1_isSet;
}

bool OAIGiftListMembers_inner::is_text1_Valid() const{
    return m_text1_isValid;
}

QString OAIGiftListMembers_inner::getText2() const {
    return m_text2;
}
void OAIGiftListMembers_inner::setText2(const QString &text2) {
    m_text2 = text2;
    m_text2_isSet = true;
}

bool OAIGiftListMembers_inner::is_text2_Set() const{
    return m_text2_isSet;
}

bool OAIGiftListMembers_inner::is_text2_Valid() const{
    return m_text2_isValid;
}

QString OAIGiftListMembers_inner::getTitle() const {
    return m_title;
}
void OAIGiftListMembers_inner::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIGiftListMembers_inner::is_title_Set() const{
    return m_title_isSet;
}

bool OAIGiftListMembers_inner::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIGiftListMembers_inner::getUserId() const {
    return m_user_id;
}
void OAIGiftListMembers_inner::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIGiftListMembers_inner::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIGiftListMembers_inner::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIGiftListMembers_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_list_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_list_member_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_admin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_surname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGiftListMembers_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
