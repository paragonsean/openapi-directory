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
import java.math.BigDecimal;
import java.util.Arrays;
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
 * SkulistbyProductId
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SkulistbyProductId {
  public static final String SERIALIZED_NAME_ACTIVATE_IF_POSSIBLE = "ActivateIfPossible";
  @SerializedName(SERIALIZED_NAME_ACTIVATE_IF_POSSIBLE)
  private Boolean activateIfPossible;

  public static final String SERIALIZED_NAME_COMMERCIAL_CONDITION_ID = "CommercialConditionId";
  @SerializedName(SERIALIZED_NAME_COMMERCIAL_CONDITION_ID)
  private Integer commercialConditionId;

  public static final String SERIALIZED_NAME_CUBIC_WEIGHT = "CubicWeight";
  @SerializedName(SERIALIZED_NAME_CUBIC_WEIGHT)
  private BigDecimal cubicWeight;

  public static final String SERIALIZED_NAME_DATE_UPDATED = "DateUpdated";
  @SerializedName(SERIALIZED_NAME_DATE_UPDATED)
  private String dateUpdated;

  public static final String SERIALIZED_NAME_ESTIMATED_DATE_ARRIVAL = "EstimatedDateArrival";
  @SerializedName(SERIALIZED_NAME_ESTIMATED_DATE_ARRIVAL)
  private String estimatedDateArrival;

  public static final String SERIALIZED_NAME_FLAG_KIT_ITENS_SELL_APART = "FlagKitItensSellApart";
  @SerializedName(SERIALIZED_NAME_FLAG_KIT_ITENS_SELL_APART)
  private Boolean flagKitItensSellApart;

  public static final String SERIALIZED_NAME_HEIGHT = "Height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private BigDecimal height;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INTERNAL_NOTE = "InternalNote";
  @SerializedName(SERIALIZED_NAME_INTERNAL_NOTE)
  private String internalNote;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_DYNAMIC_KIT = "IsDynamicKit";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IS_DYNAMIC_KIT)
  private String isDynamicKit;

  public static final String SERIALIZED_NAME_IS_GIFT_CARD_RECHARGE = "IsGiftCardRecharge";
  @SerializedName(SERIALIZED_NAME_IS_GIFT_CARD_RECHARGE)
  private Boolean isGiftCardRecharge;

  public static final String SERIALIZED_NAME_IS_INVENTORIED = "IsInventoried";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IS_INVENTORIED)
  private Boolean isInventoried;

  public static final String SERIALIZED_NAME_IS_KIT = "IsKit";
  @SerializedName(SERIALIZED_NAME_IS_KIT)
  private Boolean isKit;

  public static final String SERIALIZED_NAME_IS_PERSISTED = "IsPersisted";
  @SerializedName(SERIALIZED_NAME_IS_PERSISTED)
  private Boolean isPersisted;

  public static final String SERIALIZED_NAME_IS_REMOVED = "IsRemoved";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IS_REMOVED)
  private Boolean isRemoved;

  public static final String SERIALIZED_NAME_IS_TRANSPORTED = "IsTransported";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_IS_TRANSPORTED)
  private Boolean isTransported;

  public static final String SERIALIZED_NAME_LENGTH = "Length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private BigDecimal length;

  public static final String SERIALIZED_NAME_MANUFACTURER_CODE = "ManufacturerCode";
  @SerializedName(SERIALIZED_NAME_MANUFACTURER_CODE)
  private String manufacturerCode;

  public static final String SERIALIZED_NAME_MEASUREMENT_UNIT = "MeasurementUnit";
  @SerializedName(SERIALIZED_NAME_MEASUREMENT_UNIT)
  private String measurementUnit;

  public static final String SERIALIZED_NAME_MODAL_ID = "ModalId";
  @SerializedName(SERIALIZED_NAME_MODAL_ID)
  private Integer modalId;

  public static final String SERIALIZED_NAME_MODAL_TYPE = "ModalType";
  @SerializedName(SERIALIZED_NAME_MODAL_TYPE)
  private String modalType;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_POSITION = "Position";
  @SerializedName(SERIALIZED_NAME_POSITION)
  private Integer position;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "ProductId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private Integer productId;

  public static final String SERIALIZED_NAME_REAL_HEIGHT = "RealHeight";
  @SerializedName(SERIALIZED_NAME_REAL_HEIGHT)
  private BigDecimal realHeight;

  public static final String SERIALIZED_NAME_REAL_LENGTH = "RealLength";
  @SerializedName(SERIALIZED_NAME_REAL_LENGTH)
  private BigDecimal realLength;

  public static final String SERIALIZED_NAME_REAL_WEIGHT_KG = "RealWeightKg";
  @SerializedName(SERIALIZED_NAME_REAL_WEIGHT_KG)
  private BigDecimal realWeightKg;

  public static final String SERIALIZED_NAME_REAL_WIDTH = "RealWidth";
  @SerializedName(SERIALIZED_NAME_REAL_WIDTH)
  private BigDecimal realWidth;

  public static final String SERIALIZED_NAME_REF_ID = "RefId";
  @SerializedName(SERIALIZED_NAME_REF_ID)
  private String refId;

  public static final String SERIALIZED_NAME_REFERENCE_STOCK_KEEPING_UNIT_ID = "ReferenceStockKeepingUnitId";
  @SerializedName(SERIALIZED_NAME_REFERENCE_STOCK_KEEPING_UNIT_ID)
  private String referenceStockKeepingUnitId;

  public static final String SERIALIZED_NAME_REWARD_VALUE = "RewardValue";
  @SerializedName(SERIALIZED_NAME_REWARD_VALUE)
  private BigDecimal rewardValue;

  public static final String SERIALIZED_NAME_UNIT_MULTIPLIER = "UnitMultiplier";
  @SerializedName(SERIALIZED_NAME_UNIT_MULTIPLIER)
  private BigDecimal unitMultiplier;

  public static final String SERIALIZED_NAME_WEIGHT_KG = "WeightKg";
  @SerializedName(SERIALIZED_NAME_WEIGHT_KG)
  private BigDecimal weightKg;

  public static final String SERIALIZED_NAME_WIDTH = "Width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private BigDecimal width;

  public static final String SERIALIZED_NAME_IS_KIT_OPTIMIZED = "isKitOptimized";
  @SerializedName(SERIALIZED_NAME_IS_KIT_OPTIMIZED)
  private Boolean isKitOptimized;

  public SkulistbyProductId() {
  }

  public SkulistbyProductId activateIfPossible(Boolean activateIfPossible) {
    this.activateIfPossible = activateIfPossible;
    return this;
  }

  /**
   * When set to &#x60;true&#x60;, this attribute will automatically update the SKU as active once associated with an image or an active component.
   * @return activateIfPossible
   */
  @javax.annotation.Nullable
  public Boolean getActivateIfPossible() {
    return activateIfPossible;
  }

  public void setActivateIfPossible(Boolean activateIfPossible) {
    this.activateIfPossible = activateIfPossible;
  }


  public SkulistbyProductId commercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
    return this;
  }

  /**
   * SKU Commercial Condition ID.
   * @return commercialConditionId
   */
  @javax.annotation.Nullable
  public Integer getCommercialConditionId() {
    return commercialConditionId;
  }

  public void setCommercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
  }


  public SkulistbyProductId cubicWeight(BigDecimal cubicWeight) {
    this.cubicWeight = cubicWeight;
    return this;
  }

  /**
   * [Cubic weight](https://help.vtex.com/en/tutorial/understanding-the-cubic-weight-factor--tutorials_128).
   * @return cubicWeight
   */
  @javax.annotation.Nullable
  public BigDecimal getCubicWeight() {
    return cubicWeight;
  }

  public void setCubicWeight(BigDecimal cubicWeight) {
    this.cubicWeight = cubicWeight;
  }


  public SkulistbyProductId dateUpdated(String dateUpdated) {
    this.dateUpdated = dateUpdated;
    return this;
  }

  /**
   * Date when the product was updated for the most recent time.
   * @return dateUpdated
   */
  @javax.annotation.Nullable
  public String getDateUpdated() {
    return dateUpdated;
  }

  public void setDateUpdated(String dateUpdated) {
    this.dateUpdated = dateUpdated;
  }


  public SkulistbyProductId estimatedDateArrival(String estimatedDateArrival) {
    this.estimatedDateArrival = estimatedDateArrival;
    return this;
  }

  /**
   * SKU estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the product is on pre-sale. You must take into consideration both the launch date and the freight calculation for the arrival date.
   * @return estimatedDateArrival
   */
  @javax.annotation.Nullable
  public String getEstimatedDateArrival() {
    return estimatedDateArrival;
  }

  public void setEstimatedDateArrival(String estimatedDateArrival) {
    this.estimatedDateArrival = estimatedDateArrival;
  }


  public SkulistbyProductId flagKitItensSellApart(Boolean flagKitItensSellApart) {
    this.flagKitItensSellApart = flagKitItensSellApart;
    return this;
  }

  /**
   * Defines if the SKU bundle items can be sold separately.
   * @return flagKitItensSellApart
   */
  @javax.annotation.Nullable
  public Boolean getFlagKitItensSellApart() {
    return flagKitItensSellApart;
  }

  public void setFlagKitItensSellApart(Boolean flagKitItensSellApart) {
    this.flagKitItensSellApart = flagKitItensSellApart;
  }


  public SkulistbyProductId height(BigDecimal height) {
    this.height = height;
    return this;
  }

  /**
   * SKU Height.
   * @return height
   */
  @javax.annotation.Nullable
  public BigDecimal getHeight() {
    return height;
  }

  public void setHeight(BigDecimal height) {
    this.height = height;
  }


  public SkulistbyProductId id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * SKU ID.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public SkulistbyProductId internalNote(String internalNote) {
    this.internalNote = internalNote;
    return this;
  }

  /**
   * Internal note.
   * @return internalNote
   */
  @javax.annotation.Nullable
  public String getInternalNote() {
    return internalNote;
  }

  public void setInternalNote(String internalNote) {
    this.internalNote = internalNote;
  }


  public SkulistbyProductId isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Defines if the SKU is active or not.
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  @Deprecated
  public SkulistbyProductId isDynamicKit(String isDynamicKit) {
    this.isDynamicKit = isDynamicKit;
    return this;
  }

  /**
   * Get isDynamicKit
   * @return isDynamicKit
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public String getIsDynamicKit() {
    return isDynamicKit;
  }

  @Deprecated
  public void setIsDynamicKit(String isDynamicKit) {
    this.isDynamicKit = isDynamicKit;
  }


  public SkulistbyProductId isGiftCardRecharge(Boolean isGiftCardRecharge) {
    this.isGiftCardRecharge = isGiftCardRecharge;
    return this;
  }

  /**
   * Defines if the purchase of the SKU will generate reward value for the customer.
   * @return isGiftCardRecharge
   */
  @javax.annotation.Nullable
  public Boolean getIsGiftCardRecharge() {
    return isGiftCardRecharge;
  }

  public void setIsGiftCardRecharge(Boolean isGiftCardRecharge) {
    this.isGiftCardRecharge = isGiftCardRecharge;
  }


  @Deprecated
  public SkulistbyProductId isInventoried(Boolean isInventoried) {
    this.isInventoried = isInventoried;
    return this;
  }

  /**
   * Get isInventoried
   * @return isInventoried
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getIsInventoried() {
    return isInventoried;
  }

  @Deprecated
  public void setIsInventoried(Boolean isInventoried) {
    this.isInventoried = isInventoried;
  }


  public SkulistbyProductId isKit(Boolean isKit) {
    this.isKit = isKit;
    return this;
  }

  /**
   * Flag to set whether the product SKU is made up of one or more SKUs, thereby becoming a bundle. Must be enabled if you are adding a bundle. Once activated, the flag cannot be reverted.
   * @return isKit
   */
  @javax.annotation.Nullable
  public Boolean getIsKit() {
    return isKit;
  }

  public void setIsKit(Boolean isKit) {
    this.isKit = isKit;
  }


  public SkulistbyProductId isPersisted(Boolean isPersisted) {
    this.isPersisted = isPersisted;
    return this;
  }

  /**
   * Defines if the SKU is persisted.
   * @return isPersisted
   */
  @javax.annotation.Nullable
  public Boolean getIsPersisted() {
    return isPersisted;
  }

  public void setIsPersisted(Boolean isPersisted) {
    this.isPersisted = isPersisted;
  }


  @Deprecated
  public SkulistbyProductId isRemoved(Boolean isRemoved) {
    this.isRemoved = isRemoved;
    return this;
  }

  /**
   * Defines if the SKU is removed.
   * @return isRemoved
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getIsRemoved() {
    return isRemoved;
  }

  @Deprecated
  public void setIsRemoved(Boolean isRemoved) {
    this.isRemoved = isRemoved;
  }


  @Deprecated
  public SkulistbyProductId isTransported(Boolean isTransported) {
    this.isTransported = isTransported;
    return this;
  }

  /**
   * Get isTransported
   * @return isTransported
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Boolean getIsTransported() {
    return isTransported;
  }

  @Deprecated
  public void setIsTransported(Boolean isTransported) {
    this.isTransported = isTransported;
  }


  public SkulistbyProductId length(BigDecimal length) {
    this.length = length;
    return this;
  }

  /**
   * SKU Length.
   * @return length
   */
  @javax.annotation.Nullable
  public BigDecimal getLength() {
    return length;
  }

  public void setLength(BigDecimal length) {
    this.length = length;
  }


  public SkulistbyProductId manufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
    return this;
  }

  /**
   * Product Supplier ID.
   * @return manufacturerCode
   */
  @javax.annotation.Nullable
  public String getManufacturerCode() {
    return manufacturerCode;
  }

  public void setManufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
  }


  public SkulistbyProductId measurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
    return this;
  }

  /**
   * Measurement unit.
   * @return measurementUnit
   */
  @javax.annotation.Nullable
  public String getMeasurementUnit() {
    return measurementUnit;
  }

  public void setMeasurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
  }


  public SkulistbyProductId modalId(Integer modalId) {
    this.modalId = modalId;
    return this;
  }

  /**
   * Delivery Method (Modal Type) ID.
   * @return modalId
   */
  @javax.annotation.Nullable
  public Integer getModalId() {
    return modalId;
  }

  public void setModalId(Integer modalId) {
    this.modalId = modalId;
  }


  public SkulistbyProductId modalType(String modalType) {
    this.modalType = modalType;
    return this;
  }

  /**
   * Links an unusual type of SKU to a carrier specialized in delivering it. This field should be filled in with the name of the modal (e.g. \&quot;Chemicals\&quot; or \&quot;Refrigerated products\&quot;). To learn more about this feature, read our articles [How the modal works](https://help.vtex.com/en/tutorial/how-does-the-modal-work--tutorials_125) and [Setting up modal for carriers](https://help.vtex.com/en/tutorial/configure-modal--3jhLqxuPhuiq24UoykCcqy).
   * @return modalType
   */
  @javax.annotation.Nullable
  public String getModalType() {
    return modalType;
  }

  public void setModalType(String modalType) {
    this.modalType = modalType;
  }


  public SkulistbyProductId name(String name) {
    this.name = name;
    return this;
  }

  /**
   * SKU Name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public SkulistbyProductId position(Integer position) {
    this.position = position;
    return this;
  }

  /**
   * SKU Position.
   * @return position
   */
  @javax.annotation.Nullable
  public Integer getPosition() {
    return position;
  }

  public void setPosition(Integer position) {
    this.position = position;
  }


  public SkulistbyProductId productId(Integer productId) {
    this.productId = productId;
    return this;
  }

  /**
   * Product ID.
   * @return productId
   */
  @javax.annotation.Nullable
  public Integer getProductId() {
    return productId;
  }

  public void setProductId(Integer productId) {
    this.productId = productId;
  }


  public SkulistbyProductId realHeight(BigDecimal realHeight) {
    this.realHeight = realHeight;
    return this;
  }

  /**
   * Real SKU Height.
   * @return realHeight
   */
  @javax.annotation.Nullable
  public BigDecimal getRealHeight() {
    return realHeight;
  }

  public void setRealHeight(BigDecimal realHeight) {
    this.realHeight = realHeight;
  }


  public SkulistbyProductId realLength(BigDecimal realLength) {
    this.realLength = realLength;
    return this;
  }

  /**
   * Real SKU Length.
   * @return realLength
   */
  @javax.annotation.Nullable
  public BigDecimal getRealLength() {
    return realLength;
  }

  public void setRealLength(BigDecimal realLength) {
    this.realLength = realLength;
  }


  public SkulistbyProductId realWeightKg(BigDecimal realWeightKg) {
    this.realWeightKg = realWeightKg;
    return this;
  }

  /**
   * Real Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
   * @return realWeightKg
   */
  @javax.annotation.Nullable
  public BigDecimal getRealWeightKg() {
    return realWeightKg;
  }

  public void setRealWeightKg(BigDecimal realWeightKg) {
    this.realWeightKg = realWeightKg;
  }


  public SkulistbyProductId realWidth(BigDecimal realWidth) {
    this.realWidth = realWidth;
    return this;
  }

  /**
   * Real SKU Width.
   * @return realWidth
   */
  @javax.annotation.Nullable
  public BigDecimal getRealWidth() {
    return realWidth;
  }

  public void setRealWidth(BigDecimal realWidth) {
    this.realWidth = realWidth;
  }


  public SkulistbyProductId refId(String refId) {
    this.refId = refId;
    return this;
  }

  /**
   * Product Reference ID.
   * @return refId
   */
  @javax.annotation.Nullable
  public String getRefId() {
    return refId;
  }

  public void setRefId(String refId) {
    this.refId = refId;
  }


  public SkulistbyProductId referenceStockKeepingUnitId(String referenceStockKeepingUnitId) {
    this.referenceStockKeepingUnitId = referenceStockKeepingUnitId;
    return this;
  }

  /**
   * SKU Reference ID.
   * @return referenceStockKeepingUnitId
   */
  @javax.annotation.Nullable
  public String getReferenceStockKeepingUnitId() {
    return referenceStockKeepingUnitId;
  }

  public void setReferenceStockKeepingUnitId(String referenceStockKeepingUnitId) {
    this.referenceStockKeepingUnitId = referenceStockKeepingUnitId;
  }


  public SkulistbyProductId rewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
    return this;
  }

  /**
   * Reward value related to the SKU.
   * @return rewardValue
   */
  @javax.annotation.Nullable
  public BigDecimal getRewardValue() {
    return rewardValue;
  }

  public void setRewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
  }


  public SkulistbyProductId unitMultiplier(BigDecimal unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
    return this;
  }

  /**
   * This is the multiple number of SKU. If the Multiplier is 5.0000, the product can be added in multiple quantities of 5, 10, 15, 20, onward.
   * @return unitMultiplier
   */
  @javax.annotation.Nullable
  public BigDecimal getUnitMultiplier() {
    return unitMultiplier;
  }

  public void setUnitMultiplier(BigDecimal unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
  }


  public SkulistbyProductId weightKg(BigDecimal weightKg) {
    this.weightKg = weightKg;
    return this;
  }

  /**
   * Weight of the SKU in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
   * @return weightKg
   */
  @javax.annotation.Nullable
  public BigDecimal getWeightKg() {
    return weightKg;
  }

  public void setWeightKg(BigDecimal weightKg) {
    this.weightKg = weightKg;
  }


  public SkulistbyProductId width(BigDecimal width) {
    this.width = width;
    return this;
  }

  /**
   * SKU Width.
   * @return width
   */
  @javax.annotation.Nullable
  public BigDecimal getWidth() {
    return width;
  }

  public void setWidth(BigDecimal width) {
    this.width = width;
  }


  public SkulistbyProductId isKitOptimized(Boolean isKitOptimized) {
    this.isKitOptimized = isKitOptimized;
    return this;
  }

  /**
   * Defines if the SKU is a Optimized bundle.
   * @return isKitOptimized
   */
  @javax.annotation.Nullable
  public Boolean getIsKitOptimized() {
    return isKitOptimized;
  }

  public void setIsKitOptimized(Boolean isKitOptimized) {
    this.isKitOptimized = isKitOptimized;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SkulistbyProductId skulistbyProductId = (SkulistbyProductId) o;
    return Objects.equals(this.activateIfPossible, skulistbyProductId.activateIfPossible) &&
        Objects.equals(this.commercialConditionId, skulistbyProductId.commercialConditionId) &&
        Objects.equals(this.cubicWeight, skulistbyProductId.cubicWeight) &&
        Objects.equals(this.dateUpdated, skulistbyProductId.dateUpdated) &&
        Objects.equals(this.estimatedDateArrival, skulistbyProductId.estimatedDateArrival) &&
        Objects.equals(this.flagKitItensSellApart, skulistbyProductId.flagKitItensSellApart) &&
        Objects.equals(this.height, skulistbyProductId.height) &&
        Objects.equals(this.id, skulistbyProductId.id) &&
        Objects.equals(this.internalNote, skulistbyProductId.internalNote) &&
        Objects.equals(this.isActive, skulistbyProductId.isActive) &&
        Objects.equals(this.isDynamicKit, skulistbyProductId.isDynamicKit) &&
        Objects.equals(this.isGiftCardRecharge, skulistbyProductId.isGiftCardRecharge) &&
        Objects.equals(this.isInventoried, skulistbyProductId.isInventoried) &&
        Objects.equals(this.isKit, skulistbyProductId.isKit) &&
        Objects.equals(this.isPersisted, skulistbyProductId.isPersisted) &&
        Objects.equals(this.isRemoved, skulistbyProductId.isRemoved) &&
        Objects.equals(this.isTransported, skulistbyProductId.isTransported) &&
        Objects.equals(this.length, skulistbyProductId.length) &&
        Objects.equals(this.manufacturerCode, skulistbyProductId.manufacturerCode) &&
        Objects.equals(this.measurementUnit, skulistbyProductId.measurementUnit) &&
        Objects.equals(this.modalId, skulistbyProductId.modalId) &&
        Objects.equals(this.modalType, skulistbyProductId.modalType) &&
        Objects.equals(this.name, skulistbyProductId.name) &&
        Objects.equals(this.position, skulistbyProductId.position) &&
        Objects.equals(this.productId, skulistbyProductId.productId) &&
        Objects.equals(this.realHeight, skulistbyProductId.realHeight) &&
        Objects.equals(this.realLength, skulistbyProductId.realLength) &&
        Objects.equals(this.realWeightKg, skulistbyProductId.realWeightKg) &&
        Objects.equals(this.realWidth, skulistbyProductId.realWidth) &&
        Objects.equals(this.refId, skulistbyProductId.refId) &&
        Objects.equals(this.referenceStockKeepingUnitId, skulistbyProductId.referenceStockKeepingUnitId) &&
        Objects.equals(this.rewardValue, skulistbyProductId.rewardValue) &&
        Objects.equals(this.unitMultiplier, skulistbyProductId.unitMultiplier) &&
        Objects.equals(this.weightKg, skulistbyProductId.weightKg) &&
        Objects.equals(this.width, skulistbyProductId.width) &&
        Objects.equals(this.isKitOptimized, skulistbyProductId.isKitOptimized);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(activateIfPossible, commercialConditionId, cubicWeight, dateUpdated, estimatedDateArrival, flagKitItensSellApart, height, id, internalNote, isActive, isDynamicKit, isGiftCardRecharge, isInventoried, isKit, isPersisted, isRemoved, isTransported, length, manufacturerCode, measurementUnit, modalId, modalType, name, position, productId, realHeight, realLength, realWeightKg, realWidth, refId, referenceStockKeepingUnitId, rewardValue, unitMultiplier, weightKg, width, isKitOptimized);
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
    sb.append("class SkulistbyProductId {\n");
    sb.append("    activateIfPossible: ").append(toIndentedString(activateIfPossible)).append("\n");
    sb.append("    commercialConditionId: ").append(toIndentedString(commercialConditionId)).append("\n");
    sb.append("    cubicWeight: ").append(toIndentedString(cubicWeight)).append("\n");
    sb.append("    dateUpdated: ").append(toIndentedString(dateUpdated)).append("\n");
    sb.append("    estimatedDateArrival: ").append(toIndentedString(estimatedDateArrival)).append("\n");
    sb.append("    flagKitItensSellApart: ").append(toIndentedString(flagKitItensSellApart)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    internalNote: ").append(toIndentedString(internalNote)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isDynamicKit: ").append(toIndentedString(isDynamicKit)).append("\n");
    sb.append("    isGiftCardRecharge: ").append(toIndentedString(isGiftCardRecharge)).append("\n");
    sb.append("    isInventoried: ").append(toIndentedString(isInventoried)).append("\n");
    sb.append("    isKit: ").append(toIndentedString(isKit)).append("\n");
    sb.append("    isPersisted: ").append(toIndentedString(isPersisted)).append("\n");
    sb.append("    isRemoved: ").append(toIndentedString(isRemoved)).append("\n");
    sb.append("    isTransported: ").append(toIndentedString(isTransported)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    manufacturerCode: ").append(toIndentedString(manufacturerCode)).append("\n");
    sb.append("    measurementUnit: ").append(toIndentedString(measurementUnit)).append("\n");
    sb.append("    modalId: ").append(toIndentedString(modalId)).append("\n");
    sb.append("    modalType: ").append(toIndentedString(modalType)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    position: ").append(toIndentedString(position)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    realHeight: ").append(toIndentedString(realHeight)).append("\n");
    sb.append("    realLength: ").append(toIndentedString(realLength)).append("\n");
    sb.append("    realWeightKg: ").append(toIndentedString(realWeightKg)).append("\n");
    sb.append("    realWidth: ").append(toIndentedString(realWidth)).append("\n");
    sb.append("    refId: ").append(toIndentedString(refId)).append("\n");
    sb.append("    referenceStockKeepingUnitId: ").append(toIndentedString(referenceStockKeepingUnitId)).append("\n");
    sb.append("    rewardValue: ").append(toIndentedString(rewardValue)).append("\n");
    sb.append("    unitMultiplier: ").append(toIndentedString(unitMultiplier)).append("\n");
    sb.append("    weightKg: ").append(toIndentedString(weightKg)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
    sb.append("    isKitOptimized: ").append(toIndentedString(isKitOptimized)).append("\n");
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
    openapiFields.add("ActivateIfPossible");
    openapiFields.add("CommercialConditionId");
    openapiFields.add("CubicWeight");
    openapiFields.add("DateUpdated");
    openapiFields.add("EstimatedDateArrival");
    openapiFields.add("FlagKitItensSellApart");
    openapiFields.add("Height");
    openapiFields.add("Id");
    openapiFields.add("InternalNote");
    openapiFields.add("IsActive");
    openapiFields.add("IsDynamicKit");
    openapiFields.add("IsGiftCardRecharge");
    openapiFields.add("IsInventoried");
    openapiFields.add("IsKit");
    openapiFields.add("IsPersisted");
    openapiFields.add("IsRemoved");
    openapiFields.add("IsTransported");
    openapiFields.add("Length");
    openapiFields.add("ManufacturerCode");
    openapiFields.add("MeasurementUnit");
    openapiFields.add("ModalId");
    openapiFields.add("ModalType");
    openapiFields.add("Name");
    openapiFields.add("Position");
    openapiFields.add("ProductId");
    openapiFields.add("RealHeight");
    openapiFields.add("RealLength");
    openapiFields.add("RealWeightKg");
    openapiFields.add("RealWidth");
    openapiFields.add("RefId");
    openapiFields.add("ReferenceStockKeepingUnitId");
    openapiFields.add("RewardValue");
    openapiFields.add("UnitMultiplier");
    openapiFields.add("WeightKg");
    openapiFields.add("Width");
    openapiFields.add("isKitOptimized");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SkulistbyProductId
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SkulistbyProductId.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SkulistbyProductId is not found in the empty JSON string", SkulistbyProductId.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SkulistbyProductId.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SkulistbyProductId` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("DateUpdated") != null && !jsonObj.get("DateUpdated").isJsonNull()) && !jsonObj.get("DateUpdated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DateUpdated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DateUpdated").toString()));
      }
      if ((jsonObj.get("EstimatedDateArrival") != null && !jsonObj.get("EstimatedDateArrival").isJsonNull()) && !jsonObj.get("EstimatedDateArrival").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `EstimatedDateArrival` to be a primitive type in the JSON string but got `%s`", jsonObj.get("EstimatedDateArrival").toString()));
      }
      if ((jsonObj.get("InternalNote") != null && !jsonObj.get("InternalNote").isJsonNull()) && !jsonObj.get("InternalNote").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `InternalNote` to be a primitive type in the JSON string but got `%s`", jsonObj.get("InternalNote").toString()));
      }
      if ((jsonObj.get("IsDynamicKit") != null && !jsonObj.get("IsDynamicKit").isJsonNull()) && !jsonObj.get("IsDynamicKit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `IsDynamicKit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("IsDynamicKit").toString()));
      }
      if ((jsonObj.get("ManufacturerCode") != null && !jsonObj.get("ManufacturerCode").isJsonNull()) && !jsonObj.get("ManufacturerCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ManufacturerCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ManufacturerCode").toString()));
      }
      if ((jsonObj.get("MeasurementUnit") != null && !jsonObj.get("MeasurementUnit").isJsonNull()) && !jsonObj.get("MeasurementUnit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MeasurementUnit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MeasurementUnit").toString()));
      }
      if ((jsonObj.get("ModalType") != null && !jsonObj.get("ModalType").isJsonNull()) && !jsonObj.get("ModalType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ModalType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ModalType").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("RefId") != null && !jsonObj.get("RefId").isJsonNull()) && !jsonObj.get("RefId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `RefId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("RefId").toString()));
      }
      if ((jsonObj.get("ReferenceStockKeepingUnitId") != null && !jsonObj.get("ReferenceStockKeepingUnitId").isJsonNull()) && !jsonObj.get("ReferenceStockKeepingUnitId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ReferenceStockKeepingUnitId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ReferenceStockKeepingUnitId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SkulistbyProductId.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SkulistbyProductId' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SkulistbyProductId> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SkulistbyProductId.class));

       return (TypeAdapter<T>) new TypeAdapter<SkulistbyProductId>() {
           @Override
           public void write(JsonWriter out, SkulistbyProductId value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SkulistbyProductId read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SkulistbyProductId given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SkulistbyProductId
   * @throws IOException if the JSON string is invalid with respect to SkulistbyProductId
   */
  public static SkulistbyProductId fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SkulistbyProductId.class);
  }

  /**
   * Convert an instance of SkulistbyProductId to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

