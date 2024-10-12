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
 * OAIGetGiftList_200_response.h
 *
 * Object with information about the Gift List.
 */

#ifndef OAIGetGiftList_200_response_H
#define OAIGetGiftList_200_response_H

#include <QJsonObject>

#include "OAIGiftListMembers_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGiftListMembers_inner;

class OAIGetGiftList_200_response : public OAIObject {
public:
    OAIGetGiftList_200_response();
    OAIGetGiftList_200_response(QString json);
    ~OAIGetGiftList_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsPublic() const;
    void setIsPublic(const bool &is_public);
    bool is_is_public_Set() const;
    bool is_is_public_Valid() const;

    QString getAddress() const;
    void setAddress(const QString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QString getDateCreated() const;
    void setDateCreated(const QString &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QString getEventCity() const;
    void setEventCity(const QString &event_city);
    bool is_event_city_Set() const;
    bool is_event_city_Valid() const;

    QString getEventDate() const;
    void setEventDate(const QString &event_date);
    bool is_event_date_Set() const;
    bool is_event_date_Valid() const;

    QString getEventLocation() const;
    void setEventLocation(const QString &event_location);
    bool is_event_location_Set() const;
    bool is_event_location_Valid() const;

    QString getEventState() const;
    void setEventState(const QString &event_state);
    bool is_event_state_Set() const;
    bool is_event_state_Valid() const;

    qint32 getFileId() const;
    void setFileId(const qint32 &file_id);
    bool is_file_id_Set() const;
    bool is_file_id_Valid() const;

    QString getFileUrl() const;
    void setFileUrl(const QString &file_url);
    bool is_file_url_Set() const;
    bool is_file_url_Valid() const;

    qint32 getGiftCardId() const;
    void setGiftCardId(const qint32 &gift_card_id);
    bool is_gift_card_id_Set() const;
    bool is_gift_card_id_Valid() const;

    qint32 getGiftCardRechargeSkuId() const;
    void setGiftCardRechargeSkuId(const qint32 &gift_card_recharge_sku_id);
    bool is_gift_card_recharge_sku_id_Set() const;
    bool is_gift_card_recharge_sku_id_Valid() const;

    qint32 getGiftListId() const;
    void setGiftListId(const qint32 &gift_list_id);
    bool is_gift_list_id_Set() const;
    bool is_gift_list_id_Valid() const;

    QList<OAIGiftListMembers_inner> getGiftListMembers() const;
    void setGiftListMembers(const QList<OAIGiftListMembers_inner> &gift_list_members);
    bool is_gift_list_members_Set() const;
    bool is_gift_list_members_Valid() const;

    QList<QString> getGiftListSkuIds() const;
    void setGiftListSkuIds(const QList<QString> &gift_list_sku_ids);
    bool is_gift_list_sku_ids_Set() const;
    bool is_gift_list_sku_ids_Valid() const;

    qint32 getGiftListTypeId() const;
    void setGiftListTypeId(const qint32 &gift_list_type_id);
    bool is_gift_list_type_id_Set() const;
    bool is_gift_list_type_id_Valid() const;

    QString getGiftListTypeName() const;
    void setGiftListTypeName(const QString &gift_list_type_name);
    bool is_gift_list_type_name_Set() const;
    bool is_gift_list_type_name_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsAddressOk() const;
    void setIsAddressOk(const bool &is_address_ok);
    bool is_is_address_ok_Set() const;
    bool is_is_address_ok_Valid() const;

    QString getMemberNames() const;
    void setMemberNames(const QString &member_names);
    bool is_member_names_Set() const;
    bool is_member_names_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getProfileSystemUserAddressName() const;
    void setProfileSystemUserAddressName(const QString &profile_system_user_address_name);
    bool is_profile_system_user_address_name_Set() const;
    bool is_profile_system_user_address_name_Valid() const;

    QString getProfileSystemUserId() const;
    void setProfileSystemUserId(const QString &profile_system_user_id);
    bool is_profile_system_user_id_Set() const;
    bool is_profile_system_user_id_Valid() const;

    bool isShipsToOwner() const;
    void setShipsToOwner(const bool &ships_to_owner);
    bool is_ships_to_owner_Set() const;
    bool is_ships_to_owner_Valid() const;

    qint32 getTelemarketingId() const;
    void setTelemarketingId(const qint32 &telemarketing_id);
    bool is_telemarketing_id_Set() const;
    bool is_telemarketing_id_Valid() const;

    QString getTelemarketingObservation() const;
    void setTelemarketingObservation(const QString &telemarketing_observation);
    bool is_telemarketing_observation_Set() const;
    bool is_telemarketing_observation_Valid() const;

    QString getUrlFolder() const;
    void setUrlFolder(const QString &url_folder);
    bool is_url_folder_Set() const;
    bool is_url_folder_Valid() const;

    QString getUserId() const;
    void setUserId(const QString &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    qint32 getVersion() const;
    void setVersion(const qint32 &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_is_public;
    bool m_is_public_isSet;
    bool m_is_public_isValid;

    QString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QString m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QString m_event_city;
    bool m_event_city_isSet;
    bool m_event_city_isValid;

    QString m_event_date;
    bool m_event_date_isSet;
    bool m_event_date_isValid;

    QString m_event_location;
    bool m_event_location_isSet;
    bool m_event_location_isValid;

    QString m_event_state;
    bool m_event_state_isSet;
    bool m_event_state_isValid;

    qint32 m_file_id;
    bool m_file_id_isSet;
    bool m_file_id_isValid;

    QString m_file_url;
    bool m_file_url_isSet;
    bool m_file_url_isValid;

    qint32 m_gift_card_id;
    bool m_gift_card_id_isSet;
    bool m_gift_card_id_isValid;

    qint32 m_gift_card_recharge_sku_id;
    bool m_gift_card_recharge_sku_id_isSet;
    bool m_gift_card_recharge_sku_id_isValid;

    qint32 m_gift_list_id;
    bool m_gift_list_id_isSet;
    bool m_gift_list_id_isValid;

    QList<OAIGiftListMembers_inner> m_gift_list_members;
    bool m_gift_list_members_isSet;
    bool m_gift_list_members_isValid;

    QList<QString> m_gift_list_sku_ids;
    bool m_gift_list_sku_ids_isSet;
    bool m_gift_list_sku_ids_isValid;

    qint32 m_gift_list_type_id;
    bool m_gift_list_type_id_isSet;
    bool m_gift_list_type_id_isValid;

    QString m_gift_list_type_name;
    bool m_gift_list_type_name_isSet;
    bool m_gift_list_type_name_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_address_ok;
    bool m_is_address_ok_isSet;
    bool m_is_address_ok_isValid;

    QString m_member_names;
    bool m_member_names_isSet;
    bool m_member_names_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_profile_system_user_address_name;
    bool m_profile_system_user_address_name_isSet;
    bool m_profile_system_user_address_name_isValid;

    QString m_profile_system_user_id;
    bool m_profile_system_user_id_isSet;
    bool m_profile_system_user_id_isValid;

    bool m_ships_to_owner;
    bool m_ships_to_owner_isSet;
    bool m_ships_to_owner_isValid;

    qint32 m_telemarketing_id;
    bool m_telemarketing_id_isSet;
    bool m_telemarketing_id_isValid;

    QString m_telemarketing_observation;
    bool m_telemarketing_observation_isSet;
    bool m_telemarketing_observation_isValid;

    QString m_url_folder;
    bool m_url_folder_isSet;
    bool m_url_folder_isValid;

    QString m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;

    qint32 m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetGiftList_200_response)

#endif // OAIGetGiftList_200_response_H
