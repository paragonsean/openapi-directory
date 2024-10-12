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
 * ApiCatalogPvtStockkeepingunitGet200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiCatalogPvtStockkeepingunitGet200Response {
  public static final String SERIALIZED_NAME_ACTIVATE_IF_POSSIBLE = "ActivateIfPossible";
  @SerializedName(SERIALIZED_NAME_ACTIVATE_IF_POSSIBLE)
  private Boolean activateIfPossible;

  public static final String SERIALIZED_NAME_COMMERCIAL_CONDITION_ID = "CommercialConditionId";
  @SerializedName(SERIALIZED_NAME_COMMERCIAL_CONDITION_ID)
  private Integer commercialConditionId;

  public static final String SERIALIZED_NAME_CREATION_DATE = "CreationDate";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private String creationDate;

  public static final String SERIALIZED_NAME_CUBIC_WEIGHT = "CubicWeight";
  @SerializedName(SERIALIZED_NAME_CUBIC_WEIGHT)
  private BigDecimal cubicWeight;

  public static final String SERIALIZED_NAME_ESTIMATED_DATE_ARRIVAL = "EstimatedDateArrival";
  @SerializedName(SERIALIZED_NAME_ESTIMATED_DATE_ARRIVAL)
  private String estimatedDateArrival;

  public static final String SERIALIZED_NAME_HEIGHT = "Height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private BigDecimal height;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_KIT = "IsKit";
  @SerializedName(SERIALIZED_NAME_IS_KIT)
  private Boolean isKit;

  public static final String SERIALIZED_NAME_KIT_ITENS_SELL_APART = "KitItensSellApart";
  @SerializedName(SERIALIZED_NAME_KIT_ITENS_SELL_APART)
  private Boolean kitItensSellApart;

  public static final String SERIALIZED_NAME_LENGTH = "Length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private BigDecimal length;

  public static final String SERIALIZED_NAME_MANUFACTURER_CODE = "ManufacturerCode";
  @SerializedName(SERIALIZED_NAME_MANUFACTURER_CODE)
  private String manufacturerCode;

  public static final String SERIALIZED_NAME_MEASUREMENT_UNIT = "MeasurementUnit";
  @SerializedName(SERIALIZED_NAME_MEASUREMENT_UNIT)
  private String measurementUnit;

  public static final String SERIALIZED_NAME_MODAL_TYPE = "ModalType";
  @SerializedName(SERIALIZED_NAME_MODAL_TYPE)
  private String modalType;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PACKAGED_HEIGHT = "PackagedHeight";
  @SerializedName(SERIALIZED_NAME_PACKAGED_HEIGHT)
  private BigDecimal packagedHeight;

  public static final String SERIALIZED_NAME_PACKAGED_LENGTH = "PackagedLength";
  @SerializedName(SERIALIZED_NAME_PACKAGED_LENGTH)
  private BigDecimal packagedLength;

  public static final String SERIALIZED_NAME_PACKAGED_WEIGHT_KG = "PackagedWeightKg";
  @SerializedName(SERIALIZED_NAME_PACKAGED_WEIGHT_KG)
  private BigDecimal packagedWeightKg;

  public static final String SERIALIZED_NAME_PACKAGED_WIDTH = "PackagedWidth";
  @SerializedName(SERIALIZED_NAME_PACKAGED_WIDTH)
  private BigDecimal packagedWidth;

  public static final String SERIALIZED_NAME_PRODUCT_ID = "ProductId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_ID)
  private Integer productId;

  public static final String SERIALIZED_NAME_REF_ID = "RefId";
  @SerializedName(SERIALIZED_NAME_REF_ID)
  private String refId;

  public static final String SERIALIZED_NAME_REWARD_VALUE = "RewardValue";
  @SerializedName(SERIALIZED_NAME_REWARD_VALUE)
  private BigDecimal rewardValue;

  public static final String SERIALIZED_NAME_UNIT_MULTIPLIER = "UnitMultiplier";
  @SerializedName(SERIALIZED_NAME_UNIT_MULTIPLIER)
  private BigDecimal unitMultiplier;

  public static final String SERIALIZED_NAME_VIDEOS = "Videos";
  @SerializedName(SERIALIZED_NAME_VIDEOS)
  private String videos;

  public static final String SERIALIZED_NAME_WEIGHT_KG = "WeightKg";
  @SerializedName(SERIALIZED_NAME_WEIGHT_KG)
  private BigDecimal weightKg;

  public static final String SERIALIZED_NAME_WIDTH = "Width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private BigDecimal width;

  public ApiCatalogPvtStockkeepingunitGet200Response() {
  }

  public ApiCatalogPvtStockkeepingunitGet200Response activateIfPossible(Boolean activateIfPossible) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response commercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
    return this;
  }

  /**
   * Commercial Condition ID.
   * @return commercialConditionId
   */
  @javax.annotation.Nullable
  public Integer getCommercialConditionId() {
    return commercialConditionId;
  }

  public void setCommercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response creationDate(String creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * SKU Creation Date.
   * @return creationDate
   */
  @javax.annotation.Nullable
  public String getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(String creationDate) {
    this.creationDate = creationDate;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response cubicWeight(BigDecimal cubicWeight) {
    this.cubicWeight = cubicWeight;
    return this;
  }

  /**
   * [Cubic Weight](https://help.vtex.com/en/tutorial/understanding-the-cubic-weight-factor--tutorials_128).
   * @return cubicWeight
   */
  @javax.annotation.Nullable
  public BigDecimal getCubicWeight() {
    return cubicWeight;
  }

  public void setCubicWeight(BigDecimal cubicWeight) {
    this.cubicWeight = cubicWeight;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response estimatedDateArrival(String estimatedDateArrival) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response height(BigDecimal height) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response id(Integer id) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Defines if the SKU is active (&#x60;true&#x60;) or not (&#x60;false&#x60;).
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response isKit(Boolean isKit) {
    this.isKit = isKit;
    return this;
  }

  /**
   * Shows if the SKU is a Kit (&#x60;true&#x60;) or not (&#x60;false&#x60;).
   * @return isKit
   */
  @javax.annotation.Nullable
  public Boolean getIsKit() {
    return isKit;
  }

  public void setIsKit(Boolean isKit) {
    this.isKit = isKit;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response kitItensSellApart(Boolean kitItensSellApart) {
    this.kitItensSellApart = kitItensSellApart;
    return this;
  }

  /**
   * Defines if Kit components can be sold apart.
   * @return kitItensSellApart
   */
  @javax.annotation.Nullable
  public Boolean getKitItensSellApart() {
    return kitItensSellApart;
  }

  public void setKitItensSellApart(Boolean kitItensSellApart) {
    this.kitItensSellApart = kitItensSellApart;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response length(BigDecimal length) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response manufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
    return this;
  }

  /**
   * Manufacturer Code.
   * @return manufacturerCode
   */
  @javax.annotation.Nullable
  public String getManufacturerCode() {
    return manufacturerCode;
  }

  public void setManufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response measurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
    return this;
  }

  /**
   * Measurement Unit.
   * @return measurementUnit
   */
  @javax.annotation.Nullable
  public String getMeasurementUnit() {
    return measurementUnit;
  }

  public void setMeasurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response modalType(String modalType) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response name(String name) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response packagedHeight(BigDecimal packagedHeight) {
    this.packagedHeight = packagedHeight;
    return this;
  }

  /**
   * Packaged Height.
   * @return packagedHeight
   */
  @javax.annotation.Nullable
  public BigDecimal getPackagedHeight() {
    return packagedHeight;
  }

  public void setPackagedHeight(BigDecimal packagedHeight) {
    this.packagedHeight = packagedHeight;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response packagedLength(BigDecimal packagedLength) {
    this.packagedLength = packagedLength;
    return this;
  }

  /**
   * Packaged Length.
   * @return packagedLength
   */
  @javax.annotation.Nullable
  public BigDecimal getPackagedLength() {
    return packagedLength;
  }

  public void setPackagedLength(BigDecimal packagedLength) {
    this.packagedLength = packagedLength;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response packagedWeightKg(BigDecimal packagedWeightKg) {
    this.packagedWeightKg = packagedWeightKg;
    return this;
  }

  /**
   * Packaged Weight, in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
   * @return packagedWeightKg
   */
  @javax.annotation.Nullable
  public BigDecimal getPackagedWeightKg() {
    return packagedWeightKg;
  }

  public void setPackagedWeightKg(BigDecimal packagedWeightKg) {
    this.packagedWeightKg = packagedWeightKg;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response packagedWidth(BigDecimal packagedWidth) {
    this.packagedWidth = packagedWidth;
    return this;
  }

  /**
   * Packaged Width.
   * @return packagedWidth
   */
  @javax.annotation.Nullable
  public BigDecimal getPackagedWidth() {
    return packagedWidth;
  }

  public void setPackagedWidth(BigDecimal packagedWidth) {
    this.packagedWidth = packagedWidth;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response productId(Integer productId) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response refId(String refId) {
    this.refId = refId;
    return this;
  }

  /**
   * SKU RefId.
   * @return refId
   */
  @javax.annotation.Nullable
  public String getRefId() {
    return refId;
  }

  public void setRefId(String refId) {
    this.refId = refId;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response rewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
    return this;
  }

  /**
   * Defines the value of the reward for clients who purchase the SKU.
   * @return rewardValue
   */
  @javax.annotation.Nullable
  public BigDecimal getRewardValue() {
    return rewardValue;
  }

  public void setRewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response unitMultiplier(BigDecimal unitMultiplier) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response videos(String videos) {
    this.videos = videos;
    return this;
  }

  /**
   * Video URLs.
   * @return videos
   */
  @javax.annotation.Nullable
  public String getVideos() {
    return videos;
  }

  public void setVideos(String videos) {
    this.videos = videos;
  }


  public ApiCatalogPvtStockkeepingunitGet200Response weightKg(BigDecimal weightKg) {
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


  public ApiCatalogPvtStockkeepingunitGet200Response width(BigDecimal width) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApiCatalogPvtStockkeepingunitGet200Response apiCatalogPvtStockkeepingunitGet200Response = (ApiCatalogPvtStockkeepingunitGet200Response) o;
    return Objects.equals(this.activateIfPossible, apiCatalogPvtStockkeepingunitGet200Response.activateIfPossible) &&
        Objects.equals(this.commercialConditionId, apiCatalogPvtStockkeepingunitGet200Response.commercialConditionId) &&
        Objects.equals(this.creationDate, apiCatalogPvtStockkeepingunitGet200Response.creationDate) &&
        Objects.equals(this.cubicWeight, apiCatalogPvtStockkeepingunitGet200Response.cubicWeight) &&
        Objects.equals(this.estimatedDateArrival, apiCatalogPvtStockkeepingunitGet200Response.estimatedDateArrival) &&
        Objects.equals(this.height, apiCatalogPvtStockkeepingunitGet200Response.height) &&
        Objects.equals(this.id, apiCatalogPvtStockkeepingunitGet200Response.id) &&
        Objects.equals(this.isActive, apiCatalogPvtStockkeepingunitGet200Response.isActive) &&
        Objects.equals(this.isKit, apiCatalogPvtStockkeepingunitGet200Response.isKit) &&
        Objects.equals(this.kitItensSellApart, apiCatalogPvtStockkeepingunitGet200Response.kitItensSellApart) &&
        Objects.equals(this.length, apiCatalogPvtStockkeepingunitGet200Response.length) &&
        Objects.equals(this.manufacturerCode, apiCatalogPvtStockkeepingunitGet200Response.manufacturerCode) &&
        Objects.equals(this.measurementUnit, apiCatalogPvtStockkeepingunitGet200Response.measurementUnit) &&
        Objects.equals(this.modalType, apiCatalogPvtStockkeepingunitGet200Response.modalType) &&
        Objects.equals(this.name, apiCatalogPvtStockkeepingunitGet200Response.name) &&
        Objects.equals(this.packagedHeight, apiCatalogPvtStockkeepingunitGet200Response.packagedHeight) &&
        Objects.equals(this.packagedLength, apiCatalogPvtStockkeepingunitGet200Response.packagedLength) &&
        Objects.equals(this.packagedWeightKg, apiCatalogPvtStockkeepingunitGet200Response.packagedWeightKg) &&
        Objects.equals(this.packagedWidth, apiCatalogPvtStockkeepingunitGet200Response.packagedWidth) &&
        Objects.equals(this.productId, apiCatalogPvtStockkeepingunitGet200Response.productId) &&
        Objects.equals(this.refId, apiCatalogPvtStockkeepingunitGet200Response.refId) &&
        Objects.equals(this.rewardValue, apiCatalogPvtStockkeepingunitGet200Response.rewardValue) &&
        Objects.equals(this.unitMultiplier, apiCatalogPvtStockkeepingunitGet200Response.unitMultiplier) &&
        Objects.equals(this.videos, apiCatalogPvtStockkeepingunitGet200Response.videos) &&
        Objects.equals(this.weightKg, apiCatalogPvtStockkeepingunitGet200Response.weightKg) &&
        Objects.equals(this.width, apiCatalogPvtStockkeepingunitGet200Response.width);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(activateIfPossible, commercialConditionId, creationDate, cubicWeight, estimatedDateArrival, height, id, isActive, isKit, kitItensSellApart, length, manufacturerCode, measurementUnit, modalType, name, packagedHeight, packagedLength, packagedWeightKg, packagedWidth, productId, refId, rewardValue, unitMultiplier, videos, weightKg, width);
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
    sb.append("class ApiCatalogPvtStockkeepingunitGet200Response {\n");
    sb.append("    activateIfPossible: ").append(toIndentedString(activateIfPossible)).append("\n");
    sb.append("    commercialConditionId: ").append(toIndentedString(commercialConditionId)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    cubicWeight: ").append(toIndentedString(cubicWeight)).append("\n");
    sb.append("    estimatedDateArrival: ").append(toIndentedString(estimatedDateArrival)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isKit: ").append(toIndentedString(isKit)).append("\n");
    sb.append("    kitItensSellApart: ").append(toIndentedString(kitItensSellApart)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    manufacturerCode: ").append(toIndentedString(manufacturerCode)).append("\n");
    sb.append("    measurementUnit: ").append(toIndentedString(measurementUnit)).append("\n");
    sb.append("    modalType: ").append(toIndentedString(modalType)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    packagedHeight: ").append(toIndentedString(packagedHeight)).append("\n");
    sb.append("    packagedLength: ").append(toIndentedString(packagedLength)).append("\n");
    sb.append("    packagedWeightKg: ").append(toIndentedString(packagedWeightKg)).append("\n");
    sb.append("    packagedWidth: ").append(toIndentedString(packagedWidth)).append("\n");
    sb.append("    productId: ").append(toIndentedString(productId)).append("\n");
    sb.append("    refId: ").append(toIndentedString(refId)).append("\n");
    sb.append("    rewardValue: ").append(toIndentedString(rewardValue)).append("\n");
    sb.append("    unitMultiplier: ").append(toIndentedString(unitMultiplier)).append("\n");
    sb.append("    videos: ").append(toIndentedString(videos)).append("\n");
    sb.append("    weightKg: ").append(toIndentedString(weightKg)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
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
    openapiFields.add("CreationDate");
    openapiFields.add("CubicWeight");
    openapiFields.add("EstimatedDateArrival");
    openapiFields.add("Height");
    openapiFields.add("Id");
    openapiFields.add("IsActive");
    openapiFields.add("IsKit");
    openapiFields.add("KitItensSellApart");
    openapiFields.add("Length");
    openapiFields.add("ManufacturerCode");
    openapiFields.add("MeasurementUnit");
    openapiFields.add("ModalType");
    openapiFields.add("Name");
    openapiFields.add("PackagedHeight");
    openapiFields.add("PackagedLength");
    openapiFields.add("PackagedWeightKg");
    openapiFields.add("PackagedWidth");
    openapiFields.add("ProductId");
    openapiFields.add("RefId");
    openapiFields.add("RewardValue");
    openapiFields.add("UnitMultiplier");
    openapiFields.add("Videos");
    openapiFields.add("WeightKg");
    openapiFields.add("Width");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiCatalogPvtStockkeepingunitGet200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiCatalogPvtStockkeepingunitGet200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiCatalogPvtStockkeepingunitGet200Response is not found in the empty JSON string", ApiCatalogPvtStockkeepingunitGet200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiCatalogPvtStockkeepingunitGet200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiCatalogPvtStockkeepingunitGet200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("CreationDate") != null && !jsonObj.get("CreationDate").isJsonNull()) && !jsonObj.get("CreationDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CreationDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CreationDate").toString()));
      }
      if ((jsonObj.get("EstimatedDateArrival") != null && !jsonObj.get("EstimatedDateArrival").isJsonNull()) && !jsonObj.get("EstimatedDateArrival").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `EstimatedDateArrival` to be a primitive type in the JSON string but got `%s`", jsonObj.get("EstimatedDateArrival").toString()));
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
      if ((jsonObj.get("Videos") != null && !jsonObj.get("Videos").isJsonNull()) && !jsonObj.get("Videos").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Videos` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Videos").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiCatalogPvtStockkeepingunitGet200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiCatalogPvtStockkeepingunitGet200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiCatalogPvtStockkeepingunitGet200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiCatalogPvtStockkeepingunitGet200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiCatalogPvtStockkeepingunitGet200Response>() {
           @Override
           public void write(JsonWriter out, ApiCatalogPvtStockkeepingunitGet200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiCatalogPvtStockkeepingunitGet200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiCatalogPvtStockkeepingunitGet200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiCatalogPvtStockkeepingunitGet200Response
   * @throws IOException if the JSON string is invalid with respect to ApiCatalogPvtStockkeepingunitGet200Response
   */
  public static ApiCatalogPvtStockkeepingunitGet200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiCatalogPvtStockkeepingunitGet200Response.class);
  }

  /**
   * Convert an instance of ApiCatalogPvtStockkeepingunitGet200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

