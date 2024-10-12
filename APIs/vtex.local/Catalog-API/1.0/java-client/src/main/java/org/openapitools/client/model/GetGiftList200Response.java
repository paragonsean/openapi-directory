/*
 * Catalog API
 *   > Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.    Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.      ## Index    - [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).  - [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).  - [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).  - [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.  - [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) -  Here you can consult, create, or update an SKU unique identification code (barcode).  - [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.  - [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).  - [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).  - [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Here you can associate or disassociate an Attachment to an SKU Service.  - [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.  - [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.  - [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).  - [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Here you can can consult, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).  - [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).  - [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).  - [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).  - [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).  - [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).  - [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).  - [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).  - [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).  - [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items.   - [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Here you can consult, create, or update a Specification Field Value.   - [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - You can consult, create, or update a Specification Value.  - [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Here you can consult, create, or update a Specification Group.  - [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - You can consult or delete a Non Structured Specification.  - [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Here you can consult Sales Channel.  - [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).  - [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Here you can consult, create, or update a Supplier.  - [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).  - [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Here you can consult Product Indexed information.  - [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Here you can consult commercial conditions registered in the store.      ## Common parameters    | Parameter name              | Description                                                                             |  |---------------------------|-----------------------------------------------------------------------------------------|  | `{{accountName}}`         | Store account name                                                                      |  | `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |  | `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |  | `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.GiftListMembersInner;
import org.openapitools.jackson.nullable.JsonNullable;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * Object with information about the Gift List.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetGiftList200Response {
  public static final String SERIALIZED_NAME_IS_PUBLIC = "IsPublic";
  @SerializedName(SERIALIZED_NAME_IS_PUBLIC)
  private Boolean isPublic;

  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_DATE_CREATED = "dateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private String dateCreated;

  public static final String SERIALIZED_NAME_EVENT_CITY = "eventCity";
  @SerializedName(SERIALIZED_NAME_EVENT_CITY)
  private String eventCity;

  public static final String SERIALIZED_NAME_EVENT_DATE = "eventDate";
  @SerializedName(SERIALIZED_NAME_EVENT_DATE)
  private String eventDate;

  public static final String SERIALIZED_NAME_EVENT_LOCATION = "eventLocation";
  @SerializedName(SERIALIZED_NAME_EVENT_LOCATION)
  private String eventLocation;

  public static final String SERIALIZED_NAME_EVENT_STATE = "eventState";
  @SerializedName(SERIALIZED_NAME_EVENT_STATE)
  private String eventState;

  public static final String SERIALIZED_NAME_FILE_ID = "fileId";
  @SerializedName(SERIALIZED_NAME_FILE_ID)
  private Integer fileId;

  public static final String SERIALIZED_NAME_FILE_URL = "fileUrl";
  @SerializedName(SERIALIZED_NAME_FILE_URL)
  private String fileUrl;

  public static final String SERIALIZED_NAME_GIFT_CARD_ID = "giftCardId";
  @SerializedName(SERIALIZED_NAME_GIFT_CARD_ID)
  private Integer giftCardId;

  public static final String SERIALIZED_NAME_GIFT_CARD_RECHARGE_SKU_ID = "giftCardRechargeSkuId";
  @SerializedName(SERIALIZED_NAME_GIFT_CARD_RECHARGE_SKU_ID)
  private Integer giftCardRechargeSkuId;

  public static final String SERIALIZED_NAME_GIFT_LIST_ID = "giftListId";
  @SerializedName(SERIALIZED_NAME_GIFT_LIST_ID)
  private Integer giftListId;

  public static final String SERIALIZED_NAME_GIFT_LIST_MEMBERS = "giftListMembers";
  @SerializedName(SERIALIZED_NAME_GIFT_LIST_MEMBERS)
  private List<GiftListMembersInner> giftListMembers = new ArrayList<>();

  public static final String SERIALIZED_NAME_GIFT_LIST_SKU_IDS = "giftListSkuIds";
  @SerializedName(SERIALIZED_NAME_GIFT_LIST_SKU_IDS)
  private List<String> giftListSkuIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_GIFT_LIST_TYPE_ID = "giftListTypeId";
  @SerializedName(SERIALIZED_NAME_GIFT_LIST_TYPE_ID)
  private Integer giftListTypeId;

  public static final String SERIALIZED_NAME_GIFT_LIST_TYPE_NAME = "giftListTypeName";
  @SerializedName(SERIALIZED_NAME_GIFT_LIST_TYPE_NAME)
  private String giftListTypeName;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "isActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_ADDRESS_OK = "isAddressOk";
  @SerializedName(SERIALIZED_NAME_IS_ADDRESS_OK)
  private Boolean isAddressOk;

  public static final String SERIALIZED_NAME_MEMBER_NAMES = "memberNames";
  @SerializedName(SERIALIZED_NAME_MEMBER_NAMES)
  private String memberNames;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROFILE_SYSTEM_USER_ADDRESS_NAME = "profileSystemUserAddressName";
  @SerializedName(SERIALIZED_NAME_PROFILE_SYSTEM_USER_ADDRESS_NAME)
  private String profileSystemUserAddressName;

  public static final String SERIALIZED_NAME_PROFILE_SYSTEM_USER_ID = "profileSystemUserId";
  @SerializedName(SERIALIZED_NAME_PROFILE_SYSTEM_USER_ID)
  private String profileSystemUserId;

  public static final String SERIALIZED_NAME_SHIPS_TO_OWNER = "shipsToOwner";
  @SerializedName(SERIALIZED_NAME_SHIPS_TO_OWNER)
  private Boolean shipsToOwner;

  public static final String SERIALIZED_NAME_TELEMARKETING_ID = "telemarketingId";
  @SerializedName(SERIALIZED_NAME_TELEMARKETING_ID)
  private Integer telemarketingId;

  public static final String SERIALIZED_NAME_TELEMARKETING_OBSERVATION = "telemarketingObservation";
  @SerializedName(SERIALIZED_NAME_TELEMARKETING_OBSERVATION)
  private String telemarketingObservation;

  public static final String SERIALIZED_NAME_URL_FOLDER = "urlFolder";
  @SerializedName(SERIALIZED_NAME_URL_FOLDER)
  private String urlFolder;

  public static final String SERIALIZED_NAME_USER_ID = "userId";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private Integer version;

  public GetGiftList200Response() {
  }

  public GetGiftList200Response isPublic(Boolean isPublic) {
    this.isPublic = isPublic;
    return this;
  }

  /**
   * Defines if the gift list is public.
   * @return isPublic
   */
  @javax.annotation.Nullable
  public Boolean getIsPublic() {
    return isPublic;
  }

  public void setIsPublic(Boolean isPublic) {
    this.isPublic = isPublic;
  }


  public GetGiftList200Response address(String address) {
    this.address = address;
    return this;
  }

  /**
   * Address of the gift list.
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public GetGiftList200Response dateCreated(String dateCreated) {
    this.dateCreated = dateCreated;
    return this;
  }

  /**
   * Date when the gift list was created.
   * @return dateCreated
   */
  @javax.annotation.Nullable
  public String getDateCreated() {
    return dateCreated;
  }

  public void setDateCreated(String dateCreated) {
    this.dateCreated = dateCreated;
  }


  public GetGiftList200Response eventCity(String eventCity) {
    this.eventCity = eventCity;
    return this;
  }

  /**
   * City of the event associated with the Gift List.
   * @return eventCity
   */
  @javax.annotation.Nullable
  public String getEventCity() {
    return eventCity;
  }

  public void setEventCity(String eventCity) {
    this.eventCity = eventCity;
  }


  public GetGiftList200Response eventDate(String eventDate) {
    this.eventDate = eventDate;
    return this;
  }

  /**
   * Date of the event associated with the Gift List.
   * @return eventDate
   */
  @javax.annotation.Nullable
  public String getEventDate() {
    return eventDate;
  }

  public void setEventDate(String eventDate) {
    this.eventDate = eventDate;
  }


  public GetGiftList200Response eventLocation(String eventLocation) {
    this.eventLocation = eventLocation;
    return this;
  }

  /**
   * Location of the event associated with the Gift List.
   * @return eventLocation
   */
  @javax.annotation.Nullable
  public String getEventLocation() {
    return eventLocation;
  }

  public void setEventLocation(String eventLocation) {
    this.eventLocation = eventLocation;
  }


  public GetGiftList200Response eventState(String eventState) {
    this.eventState = eventState;
    return this;
  }

  /**
   * State of the event associated with the Gift List.
   * @return eventState
   */
  @javax.annotation.Nullable
  public String getEventState() {
    return eventState;
  }

  public void setEventState(String eventState) {
    this.eventState = eventState;
  }


  public GetGiftList200Response fileId(Integer fileId) {
    this.fileId = fileId;
    return this;
  }

  /**
   * File ID.
   * @return fileId
   */
  @javax.annotation.Nullable
  public Integer getFileId() {
    return fileId;
  }

  public void setFileId(Integer fileId) {
    this.fileId = fileId;
  }


  public GetGiftList200Response fileUrl(String fileUrl) {
    this.fileUrl = fileUrl;
    return this;
  }

  /**
   * File URL.
   * @return fileUrl
   */
  @javax.annotation.Nullable
  public String getFileUrl() {
    return fileUrl;
  }

  public void setFileUrl(String fileUrl) {
    this.fileUrl = fileUrl;
  }


  public GetGiftList200Response giftCardId(Integer giftCardId) {
    this.giftCardId = giftCardId;
    return this;
  }

  /**
   * Gift Card ID.
   * @return giftCardId
   */
  @javax.annotation.Nullable
  public Integer getGiftCardId() {
    return giftCardId;
  }

  public void setGiftCardId(Integer giftCardId) {
    this.giftCardId = giftCardId;
  }


  public GetGiftList200Response giftCardRechargeSkuId(Integer giftCardRechargeSkuId) {
    this.giftCardRechargeSkuId = giftCardRechargeSkuId;
    return this;
  }

  /**
   * ID of the SKU that recharges the gift card.
   * @return giftCardRechargeSkuId
   */
  @javax.annotation.Nullable
  public Integer getGiftCardRechargeSkuId() {
    return giftCardRechargeSkuId;
  }

  public void setGiftCardRechargeSkuId(Integer giftCardRechargeSkuId) {
    this.giftCardRechargeSkuId = giftCardRechargeSkuId;
  }


  public GetGiftList200Response giftListId(Integer giftListId) {
    this.giftListId = giftListId;
    return this;
  }

  /**
   * Gift List ID.
   * @return giftListId
   */
  @javax.annotation.Nullable
  public Integer getGiftListId() {
    return giftListId;
  }

  public void setGiftListId(Integer giftListId) {
    this.giftListId = giftListId;
  }


  public GetGiftList200Response giftListMembers(List<GiftListMembersInner> giftListMembers) {
    this.giftListMembers = giftListMembers;
    return this;
  }

  public GetGiftList200Response addGiftListMembersItem(GiftListMembersInner giftListMembersItem) {
    if (this.giftListMembers == null) {
      this.giftListMembers = new ArrayList<>();
    }
    this.giftListMembers.add(giftListMembersItem);
    return this;
  }

  /**
   * Array of members of the gift list.
   * @return giftListMembers
   */
  @javax.annotation.Nullable
  public List<GiftListMembersInner> getGiftListMembers() {
    return giftListMembers;
  }

  public void setGiftListMembers(List<GiftListMembersInner> giftListMembers) {
    this.giftListMembers = giftListMembers;
  }


  public GetGiftList200Response giftListSkuIds(List<String> giftListSkuIds) {
    this.giftListSkuIds = giftListSkuIds;
    return this;
  }

  public GetGiftList200Response addGiftListSkuIdsItem(String giftListSkuIdsItem) {
    if (this.giftListSkuIds == null) {
      this.giftListSkuIds = new ArrayList<>();
    }
    this.giftListSkuIds.add(giftListSkuIdsItem);
    return this;
  }

  /**
   * Array with the IDs of SKUs that are part of the gift list.
   * @return giftListSkuIds
   */
  @javax.annotation.Nullable
  public List<String> getGiftListSkuIds() {
    return giftListSkuIds;
  }

  public void setGiftListSkuIds(List<String> giftListSkuIds) {
    this.giftListSkuIds = giftListSkuIds;
  }


  public GetGiftList200Response giftListTypeId(Integer giftListTypeId) {
    this.giftListTypeId = giftListTypeId;
    return this;
  }

  /**
   * Gift List Type ID.
   * @return giftListTypeId
   */
  @javax.annotation.Nullable
  public Integer getGiftListTypeId() {
    return giftListTypeId;
  }

  public void setGiftListTypeId(Integer giftListTypeId) {
    this.giftListTypeId = giftListTypeId;
  }


  public GetGiftList200Response giftListTypeName(String giftListTypeName) {
    this.giftListTypeName = giftListTypeName;
    return this;
  }

  /**
   * Gift List Type name.
   * @return giftListTypeName
   */
  @javax.annotation.Nullable
  public String getGiftListTypeName() {
    return giftListTypeName;
  }

  public void setGiftListTypeName(String giftListTypeName) {
    this.giftListTypeName = giftListTypeName;
  }


  public GetGiftList200Response isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Defines if the gift list is active.
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public GetGiftList200Response isAddressOk(Boolean isAddressOk) {
    this.isAddressOk = isAddressOk;
    return this;
  }

  /**
   * Validates the address of the gift list.
   * @return isAddressOk
   */
  @javax.annotation.Nullable
  public Boolean getIsAddressOk() {
    return isAddressOk;
  }

  public void setIsAddressOk(Boolean isAddressOk) {
    this.isAddressOk = isAddressOk;
  }


  public GetGiftList200Response memberNames(String memberNames) {
    this.memberNames = memberNames;
    return this;
  }

  /**
   * Name of the members of the gift list.
   * @return memberNames
   */
  @javax.annotation.Nullable
  public String getMemberNames() {
    return memberNames;
  }

  public void setMemberNames(String memberNames) {
    this.memberNames = memberNames;
  }


  public GetGiftList200Response message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Gift List message.
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public GetGiftList200Response name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Gift List name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public GetGiftList200Response profileSystemUserAddressName(String profileSystemUserAddressName) {
    this.profileSystemUserAddressName = profileSystemUserAddressName;
    return this;
  }

  /**
   * Name of the user&#39;s address.
   * @return profileSystemUserAddressName
   */
  @javax.annotation.Nullable
  public String getProfileSystemUserAddressName() {
    return profileSystemUserAddressName;
  }

  public void setProfileSystemUserAddressName(String profileSystemUserAddressName) {
    this.profileSystemUserAddressName = profileSystemUserAddressName;
  }


  public GetGiftList200Response profileSystemUserId(String profileSystemUserId) {
    this.profileSystemUserId = profileSystemUserId;
    return this;
  }

  /**
   * User ID on Profile System.
   * @return profileSystemUserId
   */
  @javax.annotation.Nullable
  public String getProfileSystemUserId() {
    return profileSystemUserId;
  }

  public void setProfileSystemUserId(String profileSystemUserId) {
    this.profileSystemUserId = profileSystemUserId;
  }


  public GetGiftList200Response shipsToOwner(Boolean shipsToOwner) {
    this.shipsToOwner = shipsToOwner;
    return this;
  }

  /**
   * Defines if items purchased from the gift list will be shipped to the owner of the gift list.
   * @return shipsToOwner
   */
  @javax.annotation.Nullable
  public Boolean getShipsToOwner() {
    return shipsToOwner;
  }

  public void setShipsToOwner(Boolean shipsToOwner) {
    this.shipsToOwner = shipsToOwner;
  }


  public GetGiftList200Response telemarketingId(Integer telemarketingId) {
    this.telemarketingId = telemarketingId;
    return this;
  }

  /**
   * Telemarketing ID.
   * @return telemarketingId
   */
  @javax.annotation.Nullable
  public Integer getTelemarketingId() {
    return telemarketingId;
  }

  public void setTelemarketingId(Integer telemarketingId) {
    this.telemarketingId = telemarketingId;
  }


  public GetGiftList200Response telemarketingObservation(String telemarketingObservation) {
    this.telemarketingObservation = telemarketingObservation;
    return this;
  }

  /**
   * Telemarketing observation.
   * @return telemarketingObservation
   */
  @javax.annotation.Nullable
  public String getTelemarketingObservation() {
    return telemarketingObservation;
  }

  public void setTelemarketingObservation(String telemarketingObservation) {
    this.telemarketingObservation = telemarketingObservation;
  }


  public GetGiftList200Response urlFolder(String urlFolder) {
    this.urlFolder = urlFolder;
    return this;
  }

  /**
   * Slug of the gift list that will be part of its URL.
   * @return urlFolder
   */
  @javax.annotation.Nullable
  public String getUrlFolder() {
    return urlFolder;
  }

  public void setUrlFolder(String urlFolder) {
    this.urlFolder = urlFolder;
  }


  public GetGiftList200Response userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * User ID.
   * @return userId
   */
  @javax.annotation.Nullable
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }


  public GetGiftList200Response version(Integer version) {
    this.version = version;
    return this;
  }

  /**
   * Version of the gift list.
   * @return version
   */
  @javax.annotation.Nullable
  public Integer getVersion() {
    return version;
  }

  public void setVersion(Integer version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetGiftList200Response getGiftList200Response = (GetGiftList200Response) o;
    return Objects.equals(this.isPublic, getGiftList200Response.isPublic) &&
        Objects.equals(this.address, getGiftList200Response.address) &&
        Objects.equals(this.dateCreated, getGiftList200Response.dateCreated) &&
        Objects.equals(this.eventCity, getGiftList200Response.eventCity) &&
        Objects.equals(this.eventDate, getGiftList200Response.eventDate) &&
        Objects.equals(this.eventLocation, getGiftList200Response.eventLocation) &&
        Objects.equals(this.eventState, getGiftList200Response.eventState) &&
        Objects.equals(this.fileId, getGiftList200Response.fileId) &&
        Objects.equals(this.fileUrl, getGiftList200Response.fileUrl) &&
        Objects.equals(this.giftCardId, getGiftList200Response.giftCardId) &&
        Objects.equals(this.giftCardRechargeSkuId, getGiftList200Response.giftCardRechargeSkuId) &&
        Objects.equals(this.giftListId, getGiftList200Response.giftListId) &&
        Objects.equals(this.giftListMembers, getGiftList200Response.giftListMembers) &&
        Objects.equals(this.giftListSkuIds, getGiftList200Response.giftListSkuIds) &&
        Objects.equals(this.giftListTypeId, getGiftList200Response.giftListTypeId) &&
        Objects.equals(this.giftListTypeName, getGiftList200Response.giftListTypeName) &&
        Objects.equals(this.isActive, getGiftList200Response.isActive) &&
        Objects.equals(this.isAddressOk, getGiftList200Response.isAddressOk) &&
        Objects.equals(this.memberNames, getGiftList200Response.memberNames) &&
        Objects.equals(this.message, getGiftList200Response.message) &&
        Objects.equals(this.name, getGiftList200Response.name) &&
        Objects.equals(this.profileSystemUserAddressName, getGiftList200Response.profileSystemUserAddressName) &&
        Objects.equals(this.profileSystemUserId, getGiftList200Response.profileSystemUserId) &&
        Objects.equals(this.shipsToOwner, getGiftList200Response.shipsToOwner) &&
        Objects.equals(this.telemarketingId, getGiftList200Response.telemarketingId) &&
        Objects.equals(this.telemarketingObservation, getGiftList200Response.telemarketingObservation) &&
        Objects.equals(this.urlFolder, getGiftList200Response.urlFolder) &&
        Objects.equals(this.userId, getGiftList200Response.userId) &&
        Objects.equals(this.version, getGiftList200Response.version);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(isPublic, address, dateCreated, eventCity, eventDate, eventLocation, eventState, fileId, fileUrl, giftCardId, giftCardRechargeSkuId, giftListId, giftListMembers, giftListSkuIds, giftListTypeId, giftListTypeName, isActive, isAddressOk, memberNames, message, name, profileSystemUserAddressName, profileSystemUserId, shipsToOwner, telemarketingId, telemarketingObservation, urlFolder, userId, version);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetGiftList200Response {\n");
    sb.append("    isPublic: ").append(toIndentedString(isPublic)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    eventCity: ").append(toIndentedString(eventCity)).append("\n");
    sb.append("    eventDate: ").append(toIndentedString(eventDate)).append("\n");
    sb.append("    eventLocation: ").append(toIndentedString(eventLocation)).append("\n");
    sb.append("    eventState: ").append(toIndentedString(eventState)).append("\n");
    sb.append("    fileId: ").append(toIndentedString(fileId)).append("\n");
    sb.append("    fileUrl: ").append(toIndentedString(fileUrl)).append("\n");
    sb.append("    giftCardId: ").append(toIndentedString(giftCardId)).append("\n");
    sb.append("    giftCardRechargeSkuId: ").append(toIndentedString(giftCardRechargeSkuId)).append("\n");
    sb.append("    giftListId: ").append(toIndentedString(giftListId)).append("\n");
    sb.append("    giftListMembers: ").append(toIndentedString(giftListMembers)).append("\n");
    sb.append("    giftListSkuIds: ").append(toIndentedString(giftListSkuIds)).append("\n");
    sb.append("    giftListTypeId: ").append(toIndentedString(giftListTypeId)).append("\n");
    sb.append("    giftListTypeName: ").append(toIndentedString(giftListTypeName)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isAddressOk: ").append(toIndentedString(isAddressOk)).append("\n");
    sb.append("    memberNames: ").append(toIndentedString(memberNames)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    profileSystemUserAddressName: ").append(toIndentedString(profileSystemUserAddressName)).append("\n");
    sb.append("    profileSystemUserId: ").append(toIndentedString(profileSystemUserId)).append("\n");
    sb.append("    shipsToOwner: ").append(toIndentedString(shipsToOwner)).append("\n");
    sb.append("    telemarketingId: ").append(toIndentedString(telemarketingId)).append("\n");
    sb.append("    telemarketingObservation: ").append(toIndentedString(telemarketingObservation)).append("\n");
    sb.append("    urlFolder: ").append(toIndentedString(urlFolder)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("IsPublic");
    openapiFields.add("address");
    openapiFields.add("dateCreated");
    openapiFields.add("eventCity");
    openapiFields.add("eventDate");
    openapiFields.add("eventLocation");
    openapiFields.add("eventState");
    openapiFields.add("fileId");
    openapiFields.add("fileUrl");
    openapiFields.add("giftCardId");
    openapiFields.add("giftCardRechargeSkuId");
    openapiFields.add("giftListId");
    openapiFields.add("giftListMembers");
    openapiFields.add("giftListSkuIds");
    openapiFields.add("giftListTypeId");
    openapiFields.add("giftListTypeName");
    openapiFields.add("isActive");
    openapiFields.add("isAddressOk");
    openapiFields.add("memberNames");
    openapiFields.add("message");
    openapiFields.add("name");
    openapiFields.add("profileSystemUserAddressName");
    openapiFields.add("profileSystemUserId");
    openapiFields.add("shipsToOwner");
    openapiFields.add("telemarketingId");
    openapiFields.add("telemarketingObservation");
    openapiFields.add("urlFolder");
    openapiFields.add("userId");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetGiftList200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetGiftList200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetGiftList200Response is not found in the empty JSON string", GetGiftList200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetGiftList200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetGiftList200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) && !jsonObj.get("address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("dateCreated") != null && !jsonObj.get("dateCreated").isJsonNull()) && !jsonObj.get("dateCreated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dateCreated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dateCreated").toString()));
      }
      if ((jsonObj.get("eventCity") != null && !jsonObj.get("eventCity").isJsonNull()) && !jsonObj.get("eventCity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eventCity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eventCity").toString()));
      }
      if ((jsonObj.get("eventDate") != null && !jsonObj.get("eventDate").isJsonNull()) && !jsonObj.get("eventDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eventDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eventDate").toString()));
      }
      if ((jsonObj.get("eventLocation") != null && !jsonObj.get("eventLocation").isJsonNull()) && !jsonObj.get("eventLocation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eventLocation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eventLocation").toString()));
      }
      if ((jsonObj.get("eventState") != null && !jsonObj.get("eventState").isJsonNull()) && !jsonObj.get("eventState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eventState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eventState").toString()));
      }
      if ((jsonObj.get("fileUrl") != null && !jsonObj.get("fileUrl").isJsonNull()) && !jsonObj.get("fileUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileUrl").toString()));
      }
      if (jsonObj.get("giftListMembers") != null && !jsonObj.get("giftListMembers").isJsonNull()) {
        JsonArray jsonArraygiftListMembers = jsonObj.getAsJsonArray("giftListMembers");
        if (jsonArraygiftListMembers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("giftListMembers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `giftListMembers` to be an array in the JSON string but got `%s`", jsonObj.get("giftListMembers").toString()));
          }

          // validate the optional field `giftListMembers` (array)
          for (int i = 0; i < jsonArraygiftListMembers.size(); i++) {
            GiftListMembersInner.validateJsonElement(jsonArraygiftListMembers.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("giftListSkuIds") != null && !jsonObj.get("giftListSkuIds").isJsonNull() && !jsonObj.get("giftListSkuIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftListSkuIds` to be an array in the JSON string but got `%s`", jsonObj.get("giftListSkuIds").toString()));
      }
      if ((jsonObj.get("giftListTypeName") != null && !jsonObj.get("giftListTypeName").isJsonNull()) && !jsonObj.get("giftListTypeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `giftListTypeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("giftListTypeName").toString()));
      }
      if ((jsonObj.get("memberNames") != null && !jsonObj.get("memberNames").isJsonNull()) && !jsonObj.get("memberNames").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `memberNames` to be a primitive type in the JSON string but got `%s`", jsonObj.get("memberNames").toString()));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("profileSystemUserAddressName") != null && !jsonObj.get("profileSystemUserAddressName").isJsonNull()) && !jsonObj.get("profileSystemUserAddressName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profileSystemUserAddressName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profileSystemUserAddressName").toString()));
      }
      if ((jsonObj.get("profileSystemUserId") != null && !jsonObj.get("profileSystemUserId").isJsonNull()) && !jsonObj.get("profileSystemUserId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profileSystemUserId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profileSystemUserId").toString()));
      }
      if ((jsonObj.get("telemarketingObservation") != null && !jsonObj.get("telemarketingObservation").isJsonNull()) && !jsonObj.get("telemarketingObservation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `telemarketingObservation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("telemarketingObservation").toString()));
      }
      if ((jsonObj.get("urlFolder") != null && !jsonObj.get("urlFolder").isJsonNull()) && !jsonObj.get("urlFolder").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `urlFolder` to be a primitive type in the JSON string but got `%s`", jsonObj.get("urlFolder").toString()));
      }
      if ((jsonObj.get("userId") != null && !jsonObj.get("userId").isJsonNull()) && !jsonObj.get("userId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetGiftList200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetGiftList200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetGiftList200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetGiftList200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetGiftList200Response>() {
           @Override
           public void write(JsonWriter out, GetGiftList200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetGiftList200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetGiftList200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetGiftList200Response
   * @throws IOException if the JSON string is invalid with respect to GetGiftList200Response
   */
  public static GetGiftList200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetGiftList200Response.class);
  }

  /**
   * Convert an instance of GetGiftList200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

