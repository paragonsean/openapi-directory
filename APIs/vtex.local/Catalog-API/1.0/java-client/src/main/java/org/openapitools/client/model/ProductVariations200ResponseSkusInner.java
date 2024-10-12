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
import java.util.HashMap;
import java.util.Map;
import org.openapitools.client.model.ProductVariations200ResponseSkusInnerMeasures;
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
 * Object containing information about a specific SKU.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProductVariations200ResponseSkusInner {
  public static final String SERIALIZED_NAME_AVAILABLE = "available";
  @SerializedName(SERIALIZED_NAME_AVAILABLE)
  private Boolean available;

  public static final String SERIALIZED_NAME_AVAILABLEQUANTITY = "availablequantity";
  @SerializedName(SERIALIZED_NAME_AVAILABLEQUANTITY)
  private Integer availablequantity;

  public static final String SERIALIZED_NAME_BEST_PRICE = "bestPrice";
  @SerializedName(SERIALIZED_NAME_BEST_PRICE)
  private Integer bestPrice;

  public static final String SERIALIZED_NAME_BEST_PRICE_FORMATED = "bestPriceFormated";
  @SerializedName(SERIALIZED_NAME_BEST_PRICE_FORMATED)
  private String bestPriceFormated;

  public static final String SERIALIZED_NAME_CACHE_VERSION_USED_TO_CALL_CHECKOUT = "cacheVersionUsedToCallCheckout";
  @SerializedName(SERIALIZED_NAME_CACHE_VERSION_USED_TO_CALL_CHECKOUT)
  private String cacheVersionUsedToCallCheckout;

  public static final String SERIALIZED_NAME_DIMENSIONS = "dimensions";
  @SerializedName(SERIALIZED_NAME_DIMENSIONS)
  private Map<String, String> dimensions = new HashMap<>();

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_INSTALLMENTS = "installments";
  @SerializedName(SERIALIZED_NAME_INSTALLMENTS)
  private Integer installments;

  public static final String SERIALIZED_NAME_INSTALLMENTS_INSTEREST_RATE = "installmentsInsterestRate";
  @SerializedName(SERIALIZED_NAME_INSTALLMENTS_INSTEREST_RATE)
  private Integer installmentsInsterestRate;

  public static final String SERIALIZED_NAME_INSTALLMENTS_VALUE = "installmentsValue";
  @SerializedName(SERIALIZED_NAME_INSTALLMENTS_VALUE)
  private Integer installmentsValue;

  public static final String SERIALIZED_NAME_LIST_PRICE = "listPrice";
  @SerializedName(SERIALIZED_NAME_LIST_PRICE)
  private Integer listPrice;

  public static final String SERIALIZED_NAME_LIST_PRICE_FORMATED = "listPriceFormated";
  @SerializedName(SERIALIZED_NAME_LIST_PRICE_FORMATED)
  private String listPriceFormated;

  public static final String SERIALIZED_NAME_MEASURES = "measures";
  @SerializedName(SERIALIZED_NAME_MEASURES)
  private ProductVariations200ResponseSkusInnerMeasures measures;

  public static final String SERIALIZED_NAME_REWARD_VALUE = "rewardValue";
  @SerializedName(SERIALIZED_NAME_REWARD_VALUE)
  private Integer rewardValue;

  public static final String SERIALIZED_NAME_SELLER_ID = "sellerId";
  @SerializedName(SERIALIZED_NAME_SELLER_ID)
  private String sellerId;

  public static final String SERIALIZED_NAME_SKU = "sku";
  @SerializedName(SERIALIZED_NAME_SKU)
  private Integer sku;

  public static final String SERIALIZED_NAME_SKUNAME = "skuname";
  @SerializedName(SERIALIZED_NAME_SKUNAME)
  private String skuname;

  public static final String SERIALIZED_NAME_SPOT_PRICE = "spotPrice";
  @SerializedName(SERIALIZED_NAME_SPOT_PRICE)
  private Integer spotPrice;

  public static final String SERIALIZED_NAME_TAX_AS_INT = "taxAsInt";
  @SerializedName(SERIALIZED_NAME_TAX_AS_INT)
  private Integer taxAsInt;

  public static final String SERIALIZED_NAME_TAX_FORMATED = "taxFormated";
  @SerializedName(SERIALIZED_NAME_TAX_FORMATED)
  private String taxFormated;

  public static final String SERIALIZED_NAME_UNIT_MULTIPLIER = "unitMultiplier";
  @SerializedName(SERIALIZED_NAME_UNIT_MULTIPLIER)
  private BigDecimal unitMultiplier;

  public ProductVariations200ResponseSkusInner() {
  }

  public ProductVariations200ResponseSkusInner available(Boolean available) {
    this.available = available;
    return this;
  }

  /**
   * Defines if the SKU is available (&#x60;true&#x60;) or not (&#x60;false&#x60;).
   * @return available
   */
  @javax.annotation.Nullable
  public Boolean getAvailable() {
    return available;
  }

  public void setAvailable(Boolean available) {
    this.available = available;
  }


  public ProductVariations200ResponseSkusInner availablequantity(Integer availablequantity) {
    this.availablequantity = availablequantity;
    return this;
  }

  /**
   * Available quantity of the SKU in stock.
   * @return availablequantity
   */
  @javax.annotation.Nullable
  public Integer getAvailablequantity() {
    return availablequantity;
  }

  public void setAvailablequantity(Integer availablequantity) {
    this.availablequantity = availablequantity;
  }


  public ProductVariations200ResponseSkusInner bestPrice(Integer bestPrice) {
    this.bestPrice = bestPrice;
    return this;
  }

  /**
   * Best price.
   * @return bestPrice
   */
  @javax.annotation.Nullable
  public Integer getBestPrice() {
    return bestPrice;
  }

  public void setBestPrice(Integer bestPrice) {
    this.bestPrice = bestPrice;
  }


  public ProductVariations200ResponseSkusInner bestPriceFormated(String bestPriceFormated) {
    this.bestPriceFormated = bestPriceFormated;
    return this;
  }

  /**
   * Best price formatted according to the valid currency.
   * @return bestPriceFormated
   */
  @javax.annotation.Nullable
  public String getBestPriceFormated() {
    return bestPriceFormated;
  }

  public void setBestPriceFormated(String bestPriceFormated) {
    this.bestPriceFormated = bestPriceFormated;
  }


  public ProductVariations200ResponseSkusInner cacheVersionUsedToCallCheckout(String cacheVersionUsedToCallCheckout) {
    this.cacheVersionUsedToCallCheckout = cacheVersionUsedToCallCheckout;
    return this;
  }

  /**
   * Cache version used to call Checkout.
   * @return cacheVersionUsedToCallCheckout
   */
  @javax.annotation.Nullable
  public String getCacheVersionUsedToCallCheckout() {
    return cacheVersionUsedToCallCheckout;
  }

  public void setCacheVersionUsedToCallCheckout(String cacheVersionUsedToCallCheckout) {
    this.cacheVersionUsedToCallCheckout = cacheVersionUsedToCallCheckout;
  }


  public ProductVariations200ResponseSkusInner dimensions(Map<String, String> dimensions) {
    this.dimensions = dimensions;
    return this;
  }

  public ProductVariations200ResponseSkusInner putDimensionsItem(String key, String dimensionsItem) {
    if (this.dimensions == null) {
      this.dimensions = new HashMap<>();
    }
    this.dimensions.put(key, dimensionsItem);
    return this;
  }

  /**
   * Lists SKU specifications and their respective values.
   * @return dimensions
   */
  @javax.annotation.Nullable
  public Map<String, String> getDimensions() {
    return dimensions;
  }

  public void setDimensions(Map<String, String> dimensions) {
    this.dimensions = dimensions;
  }


  public ProductVariations200ResponseSkusInner image(String image) {
    this.image = image;
    return this;
  }

  /**
   * SKU image URL.
   * @return image
   */
  @javax.annotation.Nullable
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public ProductVariations200ResponseSkusInner installments(Integer installments) {
    this.installments = installments;
    return this;
  }

  /**
   * Number of installments.
   * @return installments
   */
  @javax.annotation.Nullable
  public Integer getInstallments() {
    return installments;
  }

  public void setInstallments(Integer installments) {
    this.installments = installments;
  }


  public ProductVariations200ResponseSkusInner installmentsInsterestRate(Integer installmentsInsterestRate) {
    this.installmentsInsterestRate = installmentsInsterestRate;
    return this;
  }

  /**
   * Interest rate of installments.
   * @return installmentsInsterestRate
   */
  @javax.annotation.Nullable
  public Integer getInstallmentsInsterestRate() {
    return installmentsInsterestRate;
  }

  public void setInstallmentsInsterestRate(Integer installmentsInsterestRate) {
    this.installmentsInsterestRate = installmentsInsterestRate;
  }


  public ProductVariations200ResponseSkusInner installmentsValue(Integer installmentsValue) {
    this.installmentsValue = installmentsValue;
    return this;
  }

  /**
   * Value of installments.
   * @return installmentsValue
   */
  @javax.annotation.Nullable
  public Integer getInstallmentsValue() {
    return installmentsValue;
  }

  public void setInstallmentsValue(Integer installmentsValue) {
    this.installmentsValue = installmentsValue;
  }


  public ProductVariations200ResponseSkusInner listPrice(Integer listPrice) {
    this.listPrice = listPrice;
    return this;
  }

  /**
   * List price.
   * @return listPrice
   */
  @javax.annotation.Nullable
  public Integer getListPrice() {
    return listPrice;
  }

  public void setListPrice(Integer listPrice) {
    this.listPrice = listPrice;
  }


  public ProductVariations200ResponseSkusInner listPriceFormated(String listPriceFormated) {
    this.listPriceFormated = listPriceFormated;
    return this;
  }

  /**
   * List price formatted according to the valid currency.
   * @return listPriceFormated
   */
  @javax.annotation.Nullable
  public String getListPriceFormated() {
    return listPriceFormated;
  }

  public void setListPriceFormated(String listPriceFormated) {
    this.listPriceFormated = listPriceFormated;
  }


  public ProductVariations200ResponseSkusInner measures(ProductVariations200ResponseSkusInnerMeasures measures) {
    this.measures = measures;
    return this;
  }

  /**
   * Get measures
   * @return measures
   */
  @javax.annotation.Nullable
  public ProductVariations200ResponseSkusInnerMeasures getMeasures() {
    return measures;
  }

  public void setMeasures(ProductVariations200ResponseSkusInnerMeasures measures) {
    this.measures = measures;
  }


  public ProductVariations200ResponseSkusInner rewardValue(Integer rewardValue) {
    this.rewardValue = rewardValue;
    return this;
  }

  /**
   * SKU reward value for rewards program.
   * @return rewardValue
   */
  @javax.annotation.Nullable
  public Integer getRewardValue() {
    return rewardValue;
  }

  public void setRewardValue(Integer rewardValue) {
    this.rewardValue = rewardValue;
  }


  public ProductVariations200ResponseSkusInner sellerId(String sellerId) {
    this.sellerId = sellerId;
    return this;
  }

  /**
   * Seller ID.
   * @return sellerId
   */
  @javax.annotation.Nullable
  public String getSellerId() {
    return sellerId;
  }

  public void setSellerId(String sellerId) {
    this.sellerId = sellerId;
  }


  public ProductVariations200ResponseSkusInner sku(Integer sku) {
    this.sku = sku;
    return this;
  }

  /**
   * SKU ID.
   * @return sku
   */
  @javax.annotation.Nullable
  public Integer getSku() {
    return sku;
  }

  public void setSku(Integer sku) {
    this.sku = sku;
  }


  public ProductVariations200ResponseSkusInner skuname(String skuname) {
    this.skuname = skuname;
    return this;
  }

  /**
   * SKU Name.
   * @return skuname
   */
  @javax.annotation.Nullable
  public String getSkuname() {
    return skuname;
  }

  public void setSkuname(String skuname) {
    this.skuname = skuname;
  }


  public ProductVariations200ResponseSkusInner spotPrice(Integer spotPrice) {
    this.spotPrice = spotPrice;
    return this;
  }

  /**
   * Spot price.
   * @return spotPrice
   */
  @javax.annotation.Nullable
  public Integer getSpotPrice() {
    return spotPrice;
  }

  public void setSpotPrice(Integer spotPrice) {
    this.spotPrice = spotPrice;
  }


  public ProductVariations200ResponseSkusInner taxAsInt(Integer taxAsInt) {
    this.taxAsInt = taxAsInt;
    return this;
  }

  /**
   * Tax value.
   * @return taxAsInt
   */
  @javax.annotation.Nullable
  public Integer getTaxAsInt() {
    return taxAsInt;
  }

  public void setTaxAsInt(Integer taxAsInt) {
    this.taxAsInt = taxAsInt;
  }


  public ProductVariations200ResponseSkusInner taxFormated(String taxFormated) {
    this.taxFormated = taxFormated;
    return this;
  }

  /**
   * Tax value formatted according to the valid currency.
   * @return taxFormated
   */
  @javax.annotation.Nullable
  public String getTaxFormated() {
    return taxFormated;
  }

  public void setTaxFormated(String taxFormated) {
    this.taxFormated = taxFormated;
  }


  public ProductVariations200ResponseSkusInner unitMultiplier(BigDecimal unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
    return this;
  }

  /**
   * SKU Unit Multiplier.
   * @return unitMultiplier
   */
  @javax.annotation.Nullable
  public BigDecimal getUnitMultiplier() {
    return unitMultiplier;
  }

  public void setUnitMultiplier(BigDecimal unitMultiplier) {
    this.unitMultiplier = unitMultiplier;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProductVariations200ResponseSkusInner productVariations200ResponseSkusInner = (ProductVariations200ResponseSkusInner) o;
    return Objects.equals(this.available, productVariations200ResponseSkusInner.available) &&
        Objects.equals(this.availablequantity, productVariations200ResponseSkusInner.availablequantity) &&
        Objects.equals(this.bestPrice, productVariations200ResponseSkusInner.bestPrice) &&
        Objects.equals(this.bestPriceFormated, productVariations200ResponseSkusInner.bestPriceFormated) &&
        Objects.equals(this.cacheVersionUsedToCallCheckout, productVariations200ResponseSkusInner.cacheVersionUsedToCallCheckout) &&
        Objects.equals(this.dimensions, productVariations200ResponseSkusInner.dimensions) &&
        Objects.equals(this.image, productVariations200ResponseSkusInner.image) &&
        Objects.equals(this.installments, productVariations200ResponseSkusInner.installments) &&
        Objects.equals(this.installmentsInsterestRate, productVariations200ResponseSkusInner.installmentsInsterestRate) &&
        Objects.equals(this.installmentsValue, productVariations200ResponseSkusInner.installmentsValue) &&
        Objects.equals(this.listPrice, productVariations200ResponseSkusInner.listPrice) &&
        Objects.equals(this.listPriceFormated, productVariations200ResponseSkusInner.listPriceFormated) &&
        Objects.equals(this.measures, productVariations200ResponseSkusInner.measures) &&
        Objects.equals(this.rewardValue, productVariations200ResponseSkusInner.rewardValue) &&
        Objects.equals(this.sellerId, productVariations200ResponseSkusInner.sellerId) &&
        Objects.equals(this.sku, productVariations200ResponseSkusInner.sku) &&
        Objects.equals(this.skuname, productVariations200ResponseSkusInner.skuname) &&
        Objects.equals(this.spotPrice, productVariations200ResponseSkusInner.spotPrice) &&
        Objects.equals(this.taxAsInt, productVariations200ResponseSkusInner.taxAsInt) &&
        Objects.equals(this.taxFormated, productVariations200ResponseSkusInner.taxFormated) &&
        Objects.equals(this.unitMultiplier, productVariations200ResponseSkusInner.unitMultiplier);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(available, availablequantity, bestPrice, bestPriceFormated, cacheVersionUsedToCallCheckout, dimensions, image, installments, installmentsInsterestRate, installmentsValue, listPrice, listPriceFormated, measures, rewardValue, sellerId, sku, skuname, spotPrice, taxAsInt, taxFormated, unitMultiplier);
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
    sb.append("class ProductVariations200ResponseSkusInner {\n");
    sb.append("    available: ").append(toIndentedString(available)).append("\n");
    sb.append("    availablequantity: ").append(toIndentedString(availablequantity)).append("\n");
    sb.append("    bestPrice: ").append(toIndentedString(bestPrice)).append("\n");
    sb.append("    bestPriceFormated: ").append(toIndentedString(bestPriceFormated)).append("\n");
    sb.append("    cacheVersionUsedToCallCheckout: ").append(toIndentedString(cacheVersionUsedToCallCheckout)).append("\n");
    sb.append("    dimensions: ").append(toIndentedString(dimensions)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    installments: ").append(toIndentedString(installments)).append("\n");
    sb.append("    installmentsInsterestRate: ").append(toIndentedString(installmentsInsterestRate)).append("\n");
    sb.append("    installmentsValue: ").append(toIndentedString(installmentsValue)).append("\n");
    sb.append("    listPrice: ").append(toIndentedString(listPrice)).append("\n");
    sb.append("    listPriceFormated: ").append(toIndentedString(listPriceFormated)).append("\n");
    sb.append("    measures: ").append(toIndentedString(measures)).append("\n");
    sb.append("    rewardValue: ").append(toIndentedString(rewardValue)).append("\n");
    sb.append("    sellerId: ").append(toIndentedString(sellerId)).append("\n");
    sb.append("    sku: ").append(toIndentedString(sku)).append("\n");
    sb.append("    skuname: ").append(toIndentedString(skuname)).append("\n");
    sb.append("    spotPrice: ").append(toIndentedString(spotPrice)).append("\n");
    sb.append("    taxAsInt: ").append(toIndentedString(taxAsInt)).append("\n");
    sb.append("    taxFormated: ").append(toIndentedString(taxFormated)).append("\n");
    sb.append("    unitMultiplier: ").append(toIndentedString(unitMultiplier)).append("\n");
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
    openapiFields.add("available");
    openapiFields.add("availablequantity");
    openapiFields.add("bestPrice");
    openapiFields.add("bestPriceFormated");
    openapiFields.add("cacheVersionUsedToCallCheckout");
    openapiFields.add("dimensions");
    openapiFields.add("image");
    openapiFields.add("installments");
    openapiFields.add("installmentsInsterestRate");
    openapiFields.add("installmentsValue");
    openapiFields.add("listPrice");
    openapiFields.add("listPriceFormated");
    openapiFields.add("measures");
    openapiFields.add("rewardValue");
    openapiFields.add("sellerId");
    openapiFields.add("sku");
    openapiFields.add("skuname");
    openapiFields.add("spotPrice");
    openapiFields.add("taxAsInt");
    openapiFields.add("taxFormated");
    openapiFields.add("unitMultiplier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProductVariations200ResponseSkusInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProductVariations200ResponseSkusInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProductVariations200ResponseSkusInner is not found in the empty JSON string", ProductVariations200ResponseSkusInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProductVariations200ResponseSkusInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProductVariations200ResponseSkusInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("bestPriceFormated") != null && !jsonObj.get("bestPriceFormated").isJsonNull()) && !jsonObj.get("bestPriceFormated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bestPriceFormated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bestPriceFormated").toString()));
      }
      if ((jsonObj.get("cacheVersionUsedToCallCheckout") != null && !jsonObj.get("cacheVersionUsedToCallCheckout").isJsonNull()) && !jsonObj.get("cacheVersionUsedToCallCheckout").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cacheVersionUsedToCallCheckout` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cacheVersionUsedToCallCheckout").toString()));
      }
      if ((jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) && !jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if ((jsonObj.get("listPriceFormated") != null && !jsonObj.get("listPriceFormated").isJsonNull()) && !jsonObj.get("listPriceFormated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `listPriceFormated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("listPriceFormated").toString()));
      }
      // validate the optional field `measures`
      if (jsonObj.get("measures") != null && !jsonObj.get("measures").isJsonNull()) {
        ProductVariations200ResponseSkusInnerMeasures.validateJsonElement(jsonObj.get("measures"));
      }
      if ((jsonObj.get("sellerId") != null && !jsonObj.get("sellerId").isJsonNull()) && !jsonObj.get("sellerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sellerId").toString()));
      }
      if ((jsonObj.get("skuname") != null && !jsonObj.get("skuname").isJsonNull()) && !jsonObj.get("skuname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `skuname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("skuname").toString()));
      }
      if ((jsonObj.get("taxFormated") != null && !jsonObj.get("taxFormated").isJsonNull()) && !jsonObj.get("taxFormated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `taxFormated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("taxFormated").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProductVariations200ResponseSkusInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProductVariations200ResponseSkusInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProductVariations200ResponseSkusInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProductVariations200ResponseSkusInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ProductVariations200ResponseSkusInner>() {
           @Override
           public void write(JsonWriter out, ProductVariations200ResponseSkusInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProductVariations200ResponseSkusInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProductVariations200ResponseSkusInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProductVariations200ResponseSkusInner
   * @throws IOException if the JSON string is invalid with respect to ProductVariations200ResponseSkusInner
   */
  public static ProductVariations200ResponseSkusInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProductVariations200ResponseSkusInner.class);
  }

  /**
   * Convert an instance of ProductVariations200ResponseSkusInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

