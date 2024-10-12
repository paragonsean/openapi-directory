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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
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
 * ApiCatalogPvtStockkeepingunitSkuIdPutRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApiCatalogPvtStockkeepingunitSkuIdPutRequest {
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
  private Integer packagedWeightKg;

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
  private List<String> videos = new ArrayList<>();

  public static final String SERIALIZED_NAME_WEIGHT_KG = "WeightKg";
  @SerializedName(SERIALIZED_NAME_WEIGHT_KG)
  private BigDecimal weightKg;

  public static final String SERIALIZED_NAME_WIDTH = "Width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private BigDecimal width;

  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest() {
  }

  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest activateIfPossible(Boolean activateIfPossible) {
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


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest commercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
    return this;
  }

  /**
   * Used to define SKU specific promotions or installment rules. In case of no specific condition, use &#x60;1&#x60; (default value). This field does not accept &#x60;0&#x60;. Find out more by reading [Registering a commercial condition](https://help.vtex.com/tutorial/registering-a-commercial-condition--tutorials_445).
   * @return commercialConditionId
   */
  @javax.annotation.Nullable
  public Integer getCommercialConditionId() {
    return commercialConditionId;
  }

  public void setCommercialConditionId(Integer commercialConditionId) {
    this.commercialConditionId = commercialConditionId;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest creationDate(String creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * Date and time of the SKU&#39;s creation.
   * @return creationDate
   */
  @javax.annotation.Nullable
  public String getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(String creationDate) {
    this.creationDate = creationDate;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest cubicWeight(BigDecimal cubicWeight) {
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


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest estimatedDateArrival(String estimatedDateArrival) {
    this.estimatedDateArrival = estimatedDateArrival;
    return this;
  }

  /**
   * To add the product as pre-sale, enter the product estimated arrival date in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. You must take into consideration both the launch date and the freight calculation for the arrival date.
   * @return estimatedDateArrival
   */
  @javax.annotation.Nullable
  public String getEstimatedDateArrival() {
    return estimatedDateArrival;
  }

  public void setEstimatedDateArrival(String estimatedDateArrival) {
    this.estimatedDateArrival = estimatedDateArrival;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest height(BigDecimal height) {
    this.height = height;
    return this;
  }

  /**
   * SKU real height.
   * @return height
   */
  @javax.annotation.Nullable
  public BigDecimal getHeight() {
    return height;
  }

  public void setHeight(BigDecimal height) {
    this.height = height;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Shows if the SKU is active (&#x60;true&#x60;) or not (&#x60;false&#x60;).
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest isKit(Boolean isKit) {
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


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest kitItensSellApart(Boolean kitItensSellApart) {
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


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest length(BigDecimal length) {
    this.length = length;
    return this;
  }

  /**
   * SKU real length.
   * @return length
   */
  @javax.annotation.Nullable
  public BigDecimal getLength() {
    return length;
  }

  public void setLength(BigDecimal length) {
    this.length = length;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest manufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
    return this;
  }

  /**
   * Provided by the manufacturers to identify their product. This field should be filled in if the product has a specific manufacturer’s code.
   * @return manufacturerCode
   */
  @javax.annotation.Nullable
  public String getManufacturerCode() {
    return manufacturerCode;
  }

  public void setManufacturerCode(String manufacturerCode) {
    this.manufacturerCode = manufacturerCode;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest measurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
    return this;
  }

  /**
   * Used only in cases when you need to convert the unit of measure for sale. If a product is sold in boxes for example, but customers want to buy per square meter (m²). In common cases, use &#x60;&#39;un&#39;&#x60;.
   * @return measurementUnit
   */
  @javax.annotation.Nullable
  public String getMeasurementUnit() {
    return measurementUnit;
  }

  public void setMeasurementUnit(String measurementUnit) {
    this.measurementUnit = measurementUnit;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest modalType(String modalType) {
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


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * SKU name, meaning the variation of the previously added product. For example: **Product** - _Fridge_, **SKU** - _110V_.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest packagedHeight(BigDecimal packagedHeight) {
    this.packagedHeight = packagedHeight;
    return this;
  }

  /**
   * Height used for shipping calculation.
   * @return packagedHeight
   */
  @javax.annotation.Nonnull
  public BigDecimal getPackagedHeight() {
    return packagedHeight;
  }

  public void setPackagedHeight(BigDecimal packagedHeight) {
    this.packagedHeight = packagedHeight;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest packagedLength(BigDecimal packagedLength) {
    this.packagedLength = packagedLength;
    return this;
  }

  /**
   * Length used for shipping calculation.
   * @return packagedLength
   */
  @javax.annotation.Nonnull
  public BigDecimal getPackagedLength() {
    return packagedLength;
  }

  public void setPackagedLength(BigDecimal packagedLength) {
    this.packagedLength = packagedLength;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest packagedWeightKg(Integer packagedWeightKg) {
    this.packagedWeightKg = packagedWeightKg;
    return this;
  }

  /**
   * Weight used for shipping calculation, in the measurement [configured in the store](https://help.vtex.com/en/tutorial/filling-in-system-settings--tutorials_269), which by default is in grams.
   * @return packagedWeightKg
   */
  @javax.annotation.Nonnull
  public Integer getPackagedWeightKg() {
    return packagedWeightKg;
  }

  public void setPackagedWeightKg(Integer packagedWeightKg) {
    this.packagedWeightKg = packagedWeightKg;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest packagedWidth(BigDecimal packagedWidth) {
    this.packagedWidth = packagedWidth;
    return this;
  }

  /**
   * Width used for shipping calculation.
   * @return packagedWidth
   */
  @javax.annotation.Nonnull
  public BigDecimal getPackagedWidth() {
    return packagedWidth;
  }

  public void setPackagedWidth(BigDecimal packagedWidth) {
    this.packagedWidth = packagedWidth;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest productId(Integer productId) {
    this.productId = productId;
    return this;
  }

  /**
   * ID of the Product associated with this SKU.
   * @return productId
   */
  @javax.annotation.Nonnull
  public Integer getProductId() {
    return productId;
  }

  public void setProductId(Integer productId) {
    this.productId = productId;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest refId(String refId) {
    this.refId = refId;
    return this;
  }

  /**
   * Reference code used internally for organizational purposes. Must be unique. It is not required only if EAN code already exists. If not, this field must be provided.
   * @return refId
   */
  @javax.annotation.Nullable
  public String getRefId() {
    return refId;
  }

  public void setRefId(String refId) {
    this.refId = refId;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest rewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
    return this;
  }

  /**
   * Credit that the customer receives when finalizing an order of one specific SKU unit. By filling this field out with &#x60;1&#x60;, the customer gets U$ 1 credit on the site.
   * @return rewardValue
   */
  @javax.annotation.Nullable
  public BigDecimal getRewardValue() {
    return rewardValue;
  }

  public void setRewardValue(BigDecimal rewardValue) {
    this.rewardValue = rewardValue;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest unitMultiplier(BigDecimal unitMultiplier) {
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


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest videos(List<String> videos) {
    this.videos = videos;
    return this;
  }

  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest addVideosItem(String videosItem) {
    if (this.videos == null) {
      this.videos = new ArrayList<>();
    }
    this.videos.add(videosItem);
    return this;
  }

  /**
   * Videos URLs
   * @return videos
   */
  @javax.annotation.Nullable
  public List<String> getVideos() {
    return videos;
  }

  public void setVideos(List<String> videos) {
    this.videos = videos;
  }


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest weightKg(BigDecimal weightKg) {
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


  public ApiCatalogPvtStockkeepingunitSkuIdPutRequest width(BigDecimal width) {
    this.width = width;
    return this;
  }

  /**
   * SKU real width.
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
    ApiCatalogPvtStockkeepingunitSkuIdPutRequest apiCatalogPvtStockkeepingunitSkuIdPutRequest = (ApiCatalogPvtStockkeepingunitSkuIdPutRequest) o;
    return Objects.equals(this.activateIfPossible, apiCatalogPvtStockkeepingunitSkuIdPutRequest.activateIfPossible) &&
        Objects.equals(this.commercialConditionId, apiCatalogPvtStockkeepingunitSkuIdPutRequest.commercialConditionId) &&
        Objects.equals(this.creationDate, apiCatalogPvtStockkeepingunitSkuIdPutRequest.creationDate) &&
        Objects.equals(this.cubicWeight, apiCatalogPvtStockkeepingunitSkuIdPutRequest.cubicWeight) &&
        Objects.equals(this.estimatedDateArrival, apiCatalogPvtStockkeepingunitSkuIdPutRequest.estimatedDateArrival) &&
        Objects.equals(this.height, apiCatalogPvtStockkeepingunitSkuIdPutRequest.height) &&
        Objects.equals(this.isActive, apiCatalogPvtStockkeepingunitSkuIdPutRequest.isActive) &&
        Objects.equals(this.isKit, apiCatalogPvtStockkeepingunitSkuIdPutRequest.isKit) &&
        Objects.equals(this.kitItensSellApart, apiCatalogPvtStockkeepingunitSkuIdPutRequest.kitItensSellApart) &&
        Objects.equals(this.length, apiCatalogPvtStockkeepingunitSkuIdPutRequest.length) &&
        Objects.equals(this.manufacturerCode, apiCatalogPvtStockkeepingunitSkuIdPutRequest.manufacturerCode) &&
        Objects.equals(this.measurementUnit, apiCatalogPvtStockkeepingunitSkuIdPutRequest.measurementUnit) &&
        Objects.equals(this.modalType, apiCatalogPvtStockkeepingunitSkuIdPutRequest.modalType) &&
        Objects.equals(this.name, apiCatalogPvtStockkeepingunitSkuIdPutRequest.name) &&
        Objects.equals(this.packagedHeight, apiCatalogPvtStockkeepingunitSkuIdPutRequest.packagedHeight) &&
        Objects.equals(this.packagedLength, apiCatalogPvtStockkeepingunitSkuIdPutRequest.packagedLength) &&
        Objects.equals(this.packagedWeightKg, apiCatalogPvtStockkeepingunitSkuIdPutRequest.packagedWeightKg) &&
        Objects.equals(this.packagedWidth, apiCatalogPvtStockkeepingunitSkuIdPutRequest.packagedWidth) &&
        Objects.equals(this.productId, apiCatalogPvtStockkeepingunitSkuIdPutRequest.productId) &&
        Objects.equals(this.refId, apiCatalogPvtStockkeepingunitSkuIdPutRequest.refId) &&
        Objects.equals(this.rewardValue, apiCatalogPvtStockkeepingunitSkuIdPutRequest.rewardValue) &&
        Objects.equals(this.unitMultiplier, apiCatalogPvtStockkeepingunitSkuIdPutRequest.unitMultiplier) &&
        Objects.equals(this.videos, apiCatalogPvtStockkeepingunitSkuIdPutRequest.videos) &&
        Objects.equals(this.weightKg, apiCatalogPvtStockkeepingunitSkuIdPutRequest.weightKg) &&
        Objects.equals(this.width, apiCatalogPvtStockkeepingunitSkuIdPutRequest.width);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(activateIfPossible, commercialConditionId, creationDate, cubicWeight, estimatedDateArrival, height, isActive, isKit, kitItensSellApart, length, manufacturerCode, measurementUnit, modalType, name, packagedHeight, packagedLength, packagedWeightKg, packagedWidth, productId, refId, rewardValue, unitMultiplier, videos, weightKg, width);
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
    sb.append("class ApiCatalogPvtStockkeepingunitSkuIdPutRequest {\n");
    sb.append("    activateIfPossible: ").append(toIndentedString(activateIfPossible)).append("\n");
    sb.append("    commercialConditionId: ").append(toIndentedString(commercialConditionId)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    cubicWeight: ").append(toIndentedString(cubicWeight)).append("\n");
    sb.append("    estimatedDateArrival: ").append(toIndentedString(estimatedDateArrival)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
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
    openapiRequiredFields.add("Name");
    openapiRequiredFields.add("PackagedHeight");
    openapiRequiredFields.add("PackagedLength");
    openapiRequiredFields.add("PackagedWeightKg");
    openapiRequiredFields.add("PackagedWidth");
    openapiRequiredFields.add("ProductId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApiCatalogPvtStockkeepingunitSkuIdPutRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApiCatalogPvtStockkeepingunitSkuIdPutRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApiCatalogPvtStockkeepingunitSkuIdPutRequest is not found in the empty JSON string", ApiCatalogPvtStockkeepingunitSkuIdPutRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApiCatalogPvtStockkeepingunitSkuIdPutRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApiCatalogPvtStockkeepingunitSkuIdPutRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ApiCatalogPvtStockkeepingunitSkuIdPutRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
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
      if (!jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("RefId") != null && !jsonObj.get("RefId").isJsonNull()) && !jsonObj.get("RefId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `RefId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("RefId").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("Videos") != null && !jsonObj.get("Videos").isJsonNull() && !jsonObj.get("Videos").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `Videos` to be an array in the JSON string but got `%s`", jsonObj.get("Videos").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApiCatalogPvtStockkeepingunitSkuIdPutRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApiCatalogPvtStockkeepingunitSkuIdPutRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApiCatalogPvtStockkeepingunitSkuIdPutRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApiCatalogPvtStockkeepingunitSkuIdPutRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<ApiCatalogPvtStockkeepingunitSkuIdPutRequest>() {
           @Override
           public void write(JsonWriter out, ApiCatalogPvtStockkeepingunitSkuIdPutRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApiCatalogPvtStockkeepingunitSkuIdPutRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApiCatalogPvtStockkeepingunitSkuIdPutRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApiCatalogPvtStockkeepingunitSkuIdPutRequest
   * @throws IOException if the JSON string is invalid with respect to ApiCatalogPvtStockkeepingunitSkuIdPutRequest
   */
  public static ApiCatalogPvtStockkeepingunitSkuIdPutRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApiCatalogPvtStockkeepingunitSkuIdPutRequest.class);
  }

  /**
   * Convert an instance of ApiCatalogPvtStockkeepingunitSkuIdPutRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

