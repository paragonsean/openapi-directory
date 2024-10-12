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

#include "OAIGetGiftList_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetGiftList_200_response::OAIGetGiftList_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetGiftList_200_response::OAIGetGiftList_200_response() {
    this->initializeModel();
}

OAIGetGiftList_200_response::~OAIGetGiftList_200_response() {}

void OAIGetGiftList_200_response::initializeModel() {

    m_is_public_isSet = false;
    m_is_public_isValid = false;

    m_address_isSet = false;
    m_address_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_event_city_isSet = false;
    m_event_city_isValid = false;

    m_event_date_isSet = false;
    m_event_date_isValid = false;

    m_event_location_isSet = false;
    m_event_location_isValid = false;

    m_event_state_isSet = false;
    m_event_state_isValid = false;

    m_file_id_isSet = false;
    m_file_id_isValid = false;

    m_file_url_isSet = false;
    m_file_url_isValid = false;

    m_gift_card_id_isSet = false;
    m_gift_card_id_isValid = false;

    m_gift_card_recharge_sku_id_isSet = false;
    m_gift_card_recharge_sku_id_isValid = false;

    m_gift_list_id_isSet = false;
    m_gift_list_id_isValid = false;

    m_gift_list_members_isSet = false;
    m_gift_list_members_isValid = false;

    m_gift_list_sku_ids_isSet = false;
    m_gift_list_sku_ids_isValid = false;

    m_gift_list_type_id_isSet = false;
    m_gift_list_type_id_isValid = false;

    m_gift_list_type_name_isSet = false;
    m_gift_list_type_name_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_address_ok_isSet = false;
    m_is_address_ok_isValid = false;

    m_member_names_isSet = false;
    m_member_names_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_profile_system_user_address_name_isSet = false;
    m_profile_system_user_address_name_isValid = false;

    m_profile_system_user_id_isSet = false;
    m_profile_system_user_id_isValid = false;

    m_ships_to_owner_isSet = false;
    m_ships_to_owner_isValid = false;

    m_telemarketing_id_isSet = false;
    m_telemarketing_id_isValid = false;

    m_telemarketing_observation_isSet = false;
    m_telemarketing_observation_isValid = false;

    m_url_folder_isSet = false;
    m_url_folder_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIGetGiftList_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetGiftList_200_response::fromJsonObject(QJsonObject json) {

    m_is_public_isValid = ::OpenAPI::fromJsonValue(m_is_public, json[QString("IsPublic")]);
    m_is_public_isSet = !json[QString("IsPublic")].isNull() && m_is_public_isValid;

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("dateCreated")]);
    m_date_created_isSet = !json[QString("dateCreated")].isNull() && m_date_created_isValid;

    m_event_city_isValid = ::OpenAPI::fromJsonValue(m_event_city, json[QString("eventCity")]);
    m_event_city_isSet = !json[QString("eventCity")].isNull() && m_event_city_isValid;

    m_event_date_isValid = ::OpenAPI::fromJsonValue(m_event_date, json[QString("eventDate")]);
    m_event_date_isSet = !json[QString("eventDate")].isNull() && m_event_date_isValid;

    m_event_location_isValid = ::OpenAPI::fromJsonValue(m_event_location, json[QString("eventLocation")]);
    m_event_location_isSet = !json[QString("eventLocation")].isNull() && m_event_location_isValid;

    m_event_state_isValid = ::OpenAPI::fromJsonValue(m_event_state, json[QString("eventState")]);
    m_event_state_isSet = !json[QString("eventState")].isNull() && m_event_state_isValid;

    m_file_id_isValid = ::OpenAPI::fromJsonValue(m_file_id, json[QString("fileId")]);
    m_file_id_isSet = !json[QString("fileId")].isNull() && m_file_id_isValid;

    m_file_url_isValid = ::OpenAPI::fromJsonValue(m_file_url, json[QString("fileUrl")]);
    m_file_url_isSet = !json[QString("fileUrl")].isNull() && m_file_url_isValid;

    m_gift_card_id_isValid = ::OpenAPI::fromJsonValue(m_gift_card_id, json[QString("giftCardId")]);
    m_gift_card_id_isSet = !json[QString("giftCardId")].isNull() && m_gift_card_id_isValid;

    m_gift_card_recharge_sku_id_isValid = ::OpenAPI::fromJsonValue(m_gift_card_recharge_sku_id, json[QString("giftCardRechargeSkuId")]);
    m_gift_card_recharge_sku_id_isSet = !json[QString("giftCardRechargeSkuId")].isNull() && m_gift_card_recharge_sku_id_isValid;

    m_gift_list_id_isValid = ::OpenAPI::fromJsonValue(m_gift_list_id, json[QString("giftListId")]);
    m_gift_list_id_isSet = !json[QString("giftListId")].isNull() && m_gift_list_id_isValid;

    m_gift_list_members_isValid = ::OpenAPI::fromJsonValue(m_gift_list_members, json[QString("giftListMembers")]);
    m_gift_list_members_isSet = !json[QString("giftListMembers")].isNull() && m_gift_list_members_isValid;

    m_gift_list_sku_ids_isValid = ::OpenAPI::fromJsonValue(m_gift_list_sku_ids, json[QString("giftListSkuIds")]);
    m_gift_list_sku_ids_isSet = !json[QString("giftListSkuIds")].isNull() && m_gift_list_sku_ids_isValid;

    m_gift_list_type_id_isValid = ::OpenAPI::fromJsonValue(m_gift_list_type_id, json[QString("giftListTypeId")]);
    m_gift_list_type_id_isSet = !json[QString("giftListTypeId")].isNull() && m_gift_list_type_id_isValid;

    m_gift_list_type_name_isValid = ::OpenAPI::fromJsonValue(m_gift_list_type_name, json[QString("giftListTypeName")]);
    m_gift_list_type_name_isSet = !json[QString("giftListTypeName")].isNull() && m_gift_list_type_name_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("isActive")]);
    m_is_active_isSet = !json[QString("isActive")].isNull() && m_is_active_isValid;

    m_is_address_ok_isValid = ::OpenAPI::fromJsonValue(m_is_address_ok, json[QString("isAddressOk")]);
    m_is_address_ok_isSet = !json[QString("isAddressOk")].isNull() && m_is_address_ok_isValid;

    m_member_names_isValid = ::OpenAPI::fromJsonValue(m_member_names, json[QString("memberNames")]);
    m_member_names_isSet = !json[QString("memberNames")].isNull() && m_member_names_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_profile_system_user_address_name_isValid = ::OpenAPI::fromJsonValue(m_profile_system_user_address_name, json[QString("profileSystemUserAddressName")]);
    m_profile_system_user_address_name_isSet = !json[QString("profileSystemUserAddressName")].isNull() && m_profile_system_user_address_name_isValid;

    m_profile_system_user_id_isValid = ::OpenAPI::fromJsonValue(m_profile_system_user_id, json[QString("profileSystemUserId")]);
    m_profile_system_user_id_isSet = !json[QString("profileSystemUserId")].isNull() && m_profile_system_user_id_isValid;

    m_ships_to_owner_isValid = ::OpenAPI::fromJsonValue(m_ships_to_owner, json[QString("shipsToOwner")]);
    m_ships_to_owner_isSet = !json[QString("shipsToOwner")].isNull() && m_ships_to_owner_isValid;

    m_telemarketing_id_isValid = ::OpenAPI::fromJsonValue(m_telemarketing_id, json[QString("telemarketingId")]);
    m_telemarketing_id_isSet = !json[QString("telemarketingId")].isNull() && m_telemarketing_id_isValid;

    m_telemarketing_observation_isValid = ::OpenAPI::fromJsonValue(m_telemarketing_observation, json[QString("telemarketingObservation")]);
    m_telemarketing_observation_isSet = !json[QString("telemarketingObservation")].isNull() && m_telemarketing_observation_isValid;

    m_url_folder_isValid = ::OpenAPI::fromJsonValue(m_url_folder, json[QString("urlFolder")]);
    m_url_folder_isSet = !json[QString("urlFolder")].isNull() && m_url_folder_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("userId")]);
    m_user_id_isSet = !json[QString("userId")].isNull() && m_user_id_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIGetGiftList_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetGiftList_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_is_public_isSet) {
        obj.insert(QString("IsPublic"), ::OpenAPI::toJsonValue(m_is_public));
    }
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("dateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_event_city_isSet) {
        obj.insert(QString("eventCity"), ::OpenAPI::toJsonValue(m_event_city));
    }
    if (m_event_date_isSet) {
        obj.insert(QString("eventDate"), ::OpenAPI::toJsonValue(m_event_date));
    }
    if (m_event_location_isSet) {
        obj.insert(QString("eventLocation"), ::OpenAPI::toJsonValue(m_event_location));
    }
    if (m_event_state_isSet) {
        obj.insert(QString("eventState"), ::OpenAPI::toJsonValue(m_event_state));
    }
    if (m_file_id_isSet) {
        obj.insert(QString("fileId"), ::OpenAPI::toJsonValue(m_file_id));
    }
    if (m_file_url_isSet) {
        obj.insert(QString("fileUrl"), ::OpenAPI::toJsonValue(m_file_url));
    }
    if (m_gift_card_id_isSet) {
        obj.insert(QString("giftCardId"), ::OpenAPI::toJsonValue(m_gift_card_id));
    }
    if (m_gift_card_recharge_sku_id_isSet) {
        obj.insert(QString("giftCardRechargeSkuId"), ::OpenAPI::toJsonValue(m_gift_card_recharge_sku_id));
    }
    if (m_gift_list_id_isSet) {
        obj.insert(QString("giftListId"), ::OpenAPI::toJsonValue(m_gift_list_id));
    }
    if (m_gift_list_members.size() > 0) {
        obj.insert(QString("giftListMembers"), ::OpenAPI::toJsonValue(m_gift_list_members));
    }
    if (m_gift_list_sku_ids.size() > 0) {
        obj.insert(QString("giftListSkuIds"), ::OpenAPI::toJsonValue(m_gift_list_sku_ids));
    }
    if (m_gift_list_type_id_isSet) {
        obj.insert(QString("giftListTypeId"), ::OpenAPI::toJsonValue(m_gift_list_type_id));
    }
    if (m_gift_list_type_name_isSet) {
        obj.insert(QString("giftListTypeName"), ::OpenAPI::toJsonValue(m_gift_list_type_name));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("isActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_address_ok_isSet) {
        obj.insert(QString("isAddressOk"), ::OpenAPI::toJsonValue(m_is_address_ok));
    }
    if (m_member_names_isSet) {
        obj.insert(QString("memberNames"), ::OpenAPI::toJsonValue(m_member_names));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_profile_system_user_address_name_isSet) {
        obj.insert(QString("profileSystemUserAddressName"), ::OpenAPI::toJsonValue(m_profile_system_user_address_name));
    }
    if (m_profile_system_user_id_isSet) {
        obj.insert(QString("profileSystemUserId"), ::OpenAPI::toJsonValue(m_profile_system_user_id));
    }
    if (m_ships_to_owner_isSet) {
        obj.insert(QString("shipsToOwner"), ::OpenAPI::toJsonValue(m_ships_to_owner));
    }
    if (m_telemarketing_id_isSet) {
        obj.insert(QString("telemarketingId"), ::OpenAPI::toJsonValue(m_telemarketing_id));
    }
    if (m_telemarketing_observation_isSet) {
        obj.insert(QString("telemarketingObservation"), ::OpenAPI::toJsonValue(m_telemarketing_observation));
    }
    if (m_url_folder_isSet) {
        obj.insert(QString("urlFolder"), ::OpenAPI::toJsonValue(m_url_folder));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("userId"), ::OpenAPI::toJsonValue(m_user_id));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

bool OAIGetGiftList_200_response::isIsPublic() const {
    return m_is_public;
}
void OAIGetGiftList_200_response::setIsPublic(const bool &is_public) {
    m_is_public = is_public;
    m_is_public_isSet = true;
}

bool OAIGetGiftList_200_response::is_is_public_Set() const{
    return m_is_public_isSet;
}

bool OAIGetGiftList_200_response::is_is_public_Valid() const{
    return m_is_public_isValid;
}

QString OAIGetGiftList_200_response::getAddress() const {
    return m_address;
}
void OAIGetGiftList_200_response::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIGetGiftList_200_response::is_address_Set() const{
    return m_address_isSet;
}

bool OAIGetGiftList_200_response::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIGetGiftList_200_response::getDateCreated() const {
    return m_date_created;
}
void OAIGetGiftList_200_response::setDateCreated(const QString &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAIGetGiftList_200_response::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAIGetGiftList_200_response::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QString OAIGetGiftList_200_response::getEventCity() const {
    return m_event_city;
}
void OAIGetGiftList_200_response::setEventCity(const QString &event_city) {
    m_event_city = event_city;
    m_event_city_isSet = true;
}

bool OAIGetGiftList_200_response::is_event_city_Set() const{
    return m_event_city_isSet;
}

bool OAIGetGiftList_200_response::is_event_city_Valid() const{
    return m_event_city_isValid;
}

QString OAIGetGiftList_200_response::getEventDate() const {
    return m_event_date;
}
void OAIGetGiftList_200_response::setEventDate(const QString &event_date) {
    m_event_date = event_date;
    m_event_date_isSet = true;
}

bool OAIGetGiftList_200_response::is_event_date_Set() const{
    return m_event_date_isSet;
}

bool OAIGetGiftList_200_response::is_event_date_Valid() const{
    return m_event_date_isValid;
}

QString OAIGetGiftList_200_response::getEventLocation() const {
    return m_event_location;
}
void OAIGetGiftList_200_response::setEventLocation(const QString &event_location) {
    m_event_location = event_location;
    m_event_location_isSet = true;
}

bool OAIGetGiftList_200_response::is_event_location_Set() const{
    return m_event_location_isSet;
}

bool OAIGetGiftList_200_response::is_event_location_Valid() const{
    return m_event_location_isValid;
}

QString OAIGetGiftList_200_response::getEventState() const {
    return m_event_state;
}
void OAIGetGiftList_200_response::setEventState(const QString &event_state) {
    m_event_state = event_state;
    m_event_state_isSet = true;
}

bool OAIGetGiftList_200_response::is_event_state_Set() const{
    return m_event_state_isSet;
}

bool OAIGetGiftList_200_response::is_event_state_Valid() const{
    return m_event_state_isValid;
}

qint32 OAIGetGiftList_200_response::getFileId() const {
    return m_file_id;
}
void OAIGetGiftList_200_response::setFileId(const qint32 &file_id) {
    m_file_id = file_id;
    m_file_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_file_id_Set() const{
    return m_file_id_isSet;
}

bool OAIGetGiftList_200_response::is_file_id_Valid() const{
    return m_file_id_isValid;
}

QString OAIGetGiftList_200_response::getFileUrl() const {
    return m_file_url;
}
void OAIGetGiftList_200_response::setFileUrl(const QString &file_url) {
    m_file_url = file_url;
    m_file_url_isSet = true;
}

bool OAIGetGiftList_200_response::is_file_url_Set() const{
    return m_file_url_isSet;
}

bool OAIGetGiftList_200_response::is_file_url_Valid() const{
    return m_file_url_isValid;
}

qint32 OAIGetGiftList_200_response::getGiftCardId() const {
    return m_gift_card_id;
}
void OAIGetGiftList_200_response::setGiftCardId(const qint32 &gift_card_id) {
    m_gift_card_id = gift_card_id;
    m_gift_card_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_gift_card_id_Set() const{
    return m_gift_card_id_isSet;
}

bool OAIGetGiftList_200_response::is_gift_card_id_Valid() const{
    return m_gift_card_id_isValid;
}

qint32 OAIGetGiftList_200_response::getGiftCardRechargeSkuId() const {
    return m_gift_card_recharge_sku_id;
}
void OAIGetGiftList_200_response::setGiftCardRechargeSkuId(const qint32 &gift_card_recharge_sku_id) {
    m_gift_card_recharge_sku_id = gift_card_recharge_sku_id;
    m_gift_card_recharge_sku_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_gift_card_recharge_sku_id_Set() const{
    return m_gift_card_recharge_sku_id_isSet;
}

bool OAIGetGiftList_200_response::is_gift_card_recharge_sku_id_Valid() const{
    return m_gift_card_recharge_sku_id_isValid;
}

qint32 OAIGetGiftList_200_response::getGiftListId() const {
    return m_gift_list_id;
}
void OAIGetGiftList_200_response::setGiftListId(const qint32 &gift_list_id) {
    m_gift_list_id = gift_list_id;
    m_gift_list_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_gift_list_id_Set() const{
    return m_gift_list_id_isSet;
}

bool OAIGetGiftList_200_response::is_gift_list_id_Valid() const{
    return m_gift_list_id_isValid;
}

QList<OAIGiftListMembers_inner> OAIGetGiftList_200_response::getGiftListMembers() const {
    return m_gift_list_members;
}
void OAIGetGiftList_200_response::setGiftListMembers(const QList<OAIGiftListMembers_inner> &gift_list_members) {
    m_gift_list_members = gift_list_members;
    m_gift_list_members_isSet = true;
}

bool OAIGetGiftList_200_response::is_gift_list_members_Set() const{
    return m_gift_list_members_isSet;
}

bool OAIGetGiftList_200_response::is_gift_list_members_Valid() const{
    return m_gift_list_members_isValid;
}

QList<QString> OAIGetGiftList_200_response::getGiftListSkuIds() const {
    return m_gift_list_sku_ids;
}
void OAIGetGiftList_200_response::setGiftListSkuIds(const QList<QString> &gift_list_sku_ids) {
    m_gift_list_sku_ids = gift_list_sku_ids;
    m_gift_list_sku_ids_isSet = true;
}

bool OAIGetGiftList_200_response::is_gift_list_sku_ids_Set() const{
    return m_gift_list_sku_ids_isSet;
}

bool OAIGetGiftList_200_response::is_gift_list_sku_ids_Valid() const{
    return m_gift_list_sku_ids_isValid;
}

qint32 OAIGetGiftList_200_response::getGiftListTypeId() const {
    return m_gift_list_type_id;
}
void OAIGetGiftList_200_response::setGiftListTypeId(const qint32 &gift_list_type_id) {
    m_gift_list_type_id = gift_list_type_id;
    m_gift_list_type_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_gift_list_type_id_Set() const{
    return m_gift_list_type_id_isSet;
}

bool OAIGetGiftList_200_response::is_gift_list_type_id_Valid() const{
    return m_gift_list_type_id_isValid;
}

QString OAIGetGiftList_200_response::getGiftListTypeName() const {
    return m_gift_list_type_name;
}
void OAIGetGiftList_200_response::setGiftListTypeName(const QString &gift_list_type_name) {
    m_gift_list_type_name = gift_list_type_name;
    m_gift_list_type_name_isSet = true;
}

bool OAIGetGiftList_200_response::is_gift_list_type_name_Set() const{
    return m_gift_list_type_name_isSet;
}

bool OAIGetGiftList_200_response::is_gift_list_type_name_Valid() const{
    return m_gift_list_type_name_isValid;
}

bool OAIGetGiftList_200_response::isIsActive() const {
    return m_is_active;
}
void OAIGetGiftList_200_response::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIGetGiftList_200_response::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIGetGiftList_200_response::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAIGetGiftList_200_response::isIsAddressOk() const {
    return m_is_address_ok;
}
void OAIGetGiftList_200_response::setIsAddressOk(const bool &is_address_ok) {
    m_is_address_ok = is_address_ok;
    m_is_address_ok_isSet = true;
}

bool OAIGetGiftList_200_response::is_is_address_ok_Set() const{
    return m_is_address_ok_isSet;
}

bool OAIGetGiftList_200_response::is_is_address_ok_Valid() const{
    return m_is_address_ok_isValid;
}

QString OAIGetGiftList_200_response::getMemberNames() const {
    return m_member_names;
}
void OAIGetGiftList_200_response::setMemberNames(const QString &member_names) {
    m_member_names = member_names;
    m_member_names_isSet = true;
}

bool OAIGetGiftList_200_response::is_member_names_Set() const{
    return m_member_names_isSet;
}

bool OAIGetGiftList_200_response::is_member_names_Valid() const{
    return m_member_names_isValid;
}

QString OAIGetGiftList_200_response::getMessage() const {
    return m_message;
}
void OAIGetGiftList_200_response::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIGetGiftList_200_response::is_message_Set() const{
    return m_message_isSet;
}

bool OAIGetGiftList_200_response::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIGetGiftList_200_response::getName() const {
    return m_name;
}
void OAIGetGiftList_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetGiftList_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetGiftList_200_response::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGetGiftList_200_response::getProfileSystemUserAddressName() const {
    return m_profile_system_user_address_name;
}
void OAIGetGiftList_200_response::setProfileSystemUserAddressName(const QString &profile_system_user_address_name) {
    m_profile_system_user_address_name = profile_system_user_address_name;
    m_profile_system_user_address_name_isSet = true;
}

bool OAIGetGiftList_200_response::is_profile_system_user_address_name_Set() const{
    return m_profile_system_user_address_name_isSet;
}

bool OAIGetGiftList_200_response::is_profile_system_user_address_name_Valid() const{
    return m_profile_system_user_address_name_isValid;
}

QString OAIGetGiftList_200_response::getProfileSystemUserId() const {
    return m_profile_system_user_id;
}
void OAIGetGiftList_200_response::setProfileSystemUserId(const QString &profile_system_user_id) {
    m_profile_system_user_id = profile_system_user_id;
    m_profile_system_user_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_profile_system_user_id_Set() const{
    return m_profile_system_user_id_isSet;
}

bool OAIGetGiftList_200_response::is_profile_system_user_id_Valid() const{
    return m_profile_system_user_id_isValid;
}

bool OAIGetGiftList_200_response::isShipsToOwner() const {
    return m_ships_to_owner;
}
void OAIGetGiftList_200_response::setShipsToOwner(const bool &ships_to_owner) {
    m_ships_to_owner = ships_to_owner;
    m_ships_to_owner_isSet = true;
}

bool OAIGetGiftList_200_response::is_ships_to_owner_Set() const{
    return m_ships_to_owner_isSet;
}

bool OAIGetGiftList_200_response::is_ships_to_owner_Valid() const{
    return m_ships_to_owner_isValid;
}

qint32 OAIGetGiftList_200_response::getTelemarketingId() const {
    return m_telemarketing_id;
}
void OAIGetGiftList_200_response::setTelemarketingId(const qint32 &telemarketing_id) {
    m_telemarketing_id = telemarketing_id;
    m_telemarketing_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_telemarketing_id_Set() const{
    return m_telemarketing_id_isSet;
}

bool OAIGetGiftList_200_response::is_telemarketing_id_Valid() const{
    return m_telemarketing_id_isValid;
}

QString OAIGetGiftList_200_response::getTelemarketingObservation() const {
    return m_telemarketing_observation;
}
void OAIGetGiftList_200_response::setTelemarketingObservation(const QString &telemarketing_observation) {
    m_telemarketing_observation = telemarketing_observation;
    m_telemarketing_observation_isSet = true;
}

bool OAIGetGiftList_200_response::is_telemarketing_observation_Set() const{
    return m_telemarketing_observation_isSet;
}

bool OAIGetGiftList_200_response::is_telemarketing_observation_Valid() const{
    return m_telemarketing_observation_isValid;
}

QString OAIGetGiftList_200_response::getUrlFolder() const {
    return m_url_folder;
}
void OAIGetGiftList_200_response::setUrlFolder(const QString &url_folder) {
    m_url_folder = url_folder;
    m_url_folder_isSet = true;
}

bool OAIGetGiftList_200_response::is_url_folder_Set() const{
    return m_url_folder_isSet;
}

bool OAIGetGiftList_200_response::is_url_folder_Valid() const{
    return m_url_folder_isValid;
}

QString OAIGetGiftList_200_response::getUserId() const {
    return m_user_id;
}
void OAIGetGiftList_200_response::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIGetGiftList_200_response::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIGetGiftList_200_response::is_user_id_Valid() const{
    return m_user_id_isValid;
}

qint32 OAIGetGiftList_200_response::getVersion() const {
    return m_version;
}
void OAIGetGiftList_200_response::setVersion(const qint32 &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIGetGiftList_200_response::is_version_Set() const{
    return m_version_isSet;
}

bool OAIGetGiftList_200_response::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIGetGiftList_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_public_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_card_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_card_recharge_sku_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_list_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_list_members.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_list_sku_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_list_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_list_type_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_address_ok_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_member_names_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_system_user_address_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_system_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ships_to_owner_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_telemarketing_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_telemarketing_observation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_folder_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetGiftList_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
