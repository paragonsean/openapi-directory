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
import java.util.Arrays;
import org.openapitools.client.model.CurrencyFormatInfo;
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
 * SalesChannelbyId200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SalesChannelbyId200Response {
  public static final String SERIALIZED_NAME_CONDITION_RULE = "ConditionRule";
  @SerializedName(SERIALIZED_NAME_CONDITION_RULE)
  private String conditionRule;

  public static final String SERIALIZED_NAME_COUNTRY_CODE = "CountryCode";
  @SerializedName(SERIALIZED_NAME_COUNTRY_CODE)
  private String countryCode;

  public static final String SERIALIZED_NAME_CULTURE_INFO = "CultureInfo";
  @SerializedName(SERIALIZED_NAME_CULTURE_INFO)
  private String cultureInfo;

  public static final String SERIALIZED_NAME_CURRENCY_CODE = "CurrencyCode";
  @SerializedName(SERIALIZED_NAME_CURRENCY_CODE)
  private String currencyCode;

  public static final String SERIALIZED_NAME_CURRENCY_DECIMAL_DIGITS = "CurrencyDecimalDigits";
  @SerializedName(SERIALIZED_NAME_CURRENCY_DECIMAL_DIGITS)
  private Integer currencyDecimalDigits;

  public static final String SERIALIZED_NAME_CURRENCY_FORMAT_INFO = "CurrencyFormatInfo";
  @SerializedName(SERIALIZED_NAME_CURRENCY_FORMAT_INFO)
  private CurrencyFormatInfo currencyFormatInfo;

  public static final String SERIALIZED_NAME_CURRENCY_LOCALE = "CurrencyLocale";
  @SerializedName(SERIALIZED_NAME_CURRENCY_LOCALE)
  private Integer currencyLocale;

  public static final String SERIALIZED_NAME_CURRENCY_SYMBOL = "CurrencySymbol";
  @SerializedName(SERIALIZED_NAME_CURRENCY_SYMBOL)
  private String currencySymbol;

  public static final String SERIALIZED_NAME_ID = "Id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ORIGIN = "Origin";
  @SerializedName(SERIALIZED_NAME_ORIGIN)
  private String origin;

  public static final String SERIALIZED_NAME_POSITION = "Position";
  @SerializedName(SERIALIZED_NAME_POSITION)
  private Integer position;

  public static final String SERIALIZED_NAME_PRODUCT_CLUSTER_ID = "ProductClusterId";
  @SerializedName(SERIALIZED_NAME_PRODUCT_CLUSTER_ID)
  private Integer productClusterId;

  public static final String SERIALIZED_NAME_TIME_ZONE = "TimeZone";
  @SerializedName(SERIALIZED_NAME_TIME_ZONE)
  private String timeZone;

  public SalesChannelbyId200Response() {
  }

  public SalesChannelbyId200Response conditionRule(String conditionRule) {
    this.conditionRule = conditionRule;
    return this;
  }

  /**
   * Defines what is the conditional rule to activate de Sales Channel.
   * @return conditionRule
   */
  @javax.annotation.Nullable
  public String getConditionRule() {
    return conditionRule;
  }

  public void setConditionRule(String conditionRule) {
    this.conditionRule = conditionRule;
  }


  public SalesChannelbyId200Response countryCode(String countryCode) {
    this.countryCode = countryCode;
    return this;
  }

  /**
   * Country Code in ISO 3166-1 alfa-3 Standard.
   * @return countryCode
   */
  @javax.annotation.Nullable
  public String getCountryCode() {
    return countryCode;
  }

  public void setCountryCode(String countryCode) {
    this.countryCode = countryCode;
  }


  public SalesChannelbyId200Response cultureInfo(String cultureInfo) {
    this.cultureInfo = cultureInfo;
    return this;
  }

  /**
   * Language Country code in LCIDstring Standard.
   * @return cultureInfo
   */
  @javax.annotation.Nullable
  public String getCultureInfo() {
    return cultureInfo;
  }

  public void setCultureInfo(String cultureInfo) {
    this.cultureInfo = cultureInfo;
  }


  public SalesChannelbyId200Response currencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
    return this;
  }

  /**
   * Currency Code in ISO 4217 standard.
   * @return currencyCode
   */
  @javax.annotation.Nullable
  public String getCurrencyCode() {
    return currencyCode;
  }

  public void setCurrencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
  }


  public SalesChannelbyId200Response currencyDecimalDigits(Integer currencyDecimalDigits) {
    this.currencyDecimalDigits = currencyDecimalDigits;
    return this;
  }

  /**
   * Quantity of Currency Decimal Digits.
   * @return currencyDecimalDigits
   */
  @javax.annotation.Nullable
  public Integer getCurrencyDecimalDigits() {
    return currencyDecimalDigits;
  }

  public void setCurrencyDecimalDigits(Integer currencyDecimalDigits) {
    this.currencyDecimalDigits = currencyDecimalDigits;
  }


  public SalesChannelbyId200Response currencyFormatInfo(CurrencyFormatInfo currencyFormatInfo) {
    this.currencyFormatInfo = currencyFormatInfo;
    return this;
  }

  /**
   * Get currencyFormatInfo
   * @return currencyFormatInfo
   */
  @javax.annotation.Nullable
  public CurrencyFormatInfo getCurrencyFormatInfo() {
    return currencyFormatInfo;
  }

  public void setCurrencyFormatInfo(CurrencyFormatInfo currencyFormatInfo) {
    this.currencyFormatInfo = currencyFormatInfo;
  }


  public SalesChannelbyId200Response currencyLocale(Integer currencyLocale) {
    this.currencyLocale = currencyLocale;
    return this;
  }

  /**
   * Currency Locale Code in LCID standard.
   * @return currencyLocale
   */
  @javax.annotation.Nullable
  public Integer getCurrencyLocale() {
    return currencyLocale;
  }

  public void setCurrencyLocale(Integer currencyLocale) {
    this.currencyLocale = currencyLocale;
  }


  public SalesChannelbyId200Response currencySymbol(String currencySymbol) {
    this.currencySymbol = currencySymbol;
    return this;
  }

  /**
   * Currency symbol.
   * @return currencySymbol
   */
  @javax.annotation.Nullable
  public String getCurrencySymbol() {
    return currencySymbol;
  }

  public void setCurrencySymbol(String currencySymbol) {
    this.currencySymbol = currencySymbol;
  }


  public SalesChannelbyId200Response id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Sales Channel unique identifier.
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public SalesChannelbyId200Response isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Defines if the Sales Channel is active (&#x60;true&#x60;) or not (&#x60;false&#x60;).
   * @return isActive
   */
  @javax.annotation.Nullable
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public SalesChannelbyId200Response name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Sales Channel name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public SalesChannelbyId200Response origin(String origin) {
    this.origin = origin;
    return this;
  }

  /**
   * Origin of products in the Sales Channel.
   * @return origin
   */
  @javax.annotation.Nullable
  public String getOrigin() {
    return origin;
  }

  public void setOrigin(String origin) {
    this.origin = origin;
  }


  public SalesChannelbyId200Response position(Integer position) {
    this.position = position;
    return this;
  }

  /**
   * Defines the position on index.
   * @return position
   */
  @javax.annotation.Nullable
  public Integer getPosition() {
    return position;
  }

  public void setPosition(Integer position) {
    this.position = position;
  }


  public SalesChannelbyId200Response productClusterId(Integer productClusterId) {
    this.productClusterId = productClusterId;
    return this;
  }

  /**
   * Product Cluster ID, if the Sales Channel has releated Product Cluster.
   * @return productClusterId
   */
  @javax.annotation.Nullable
  public Integer getProductClusterId() {
    return productClusterId;
  }

  public void setProductClusterId(Integer productClusterId) {
    this.productClusterId = productClusterId;
  }


  public SalesChannelbyId200Response timeZone(String timeZone) {
    this.timeZone = timeZone;
    return this;
  }

  /**
   * Name of Time Zone.
   * @return timeZone
   */
  @javax.annotation.Nullable
  public String getTimeZone() {
    return timeZone;
  }

  public void setTimeZone(String timeZone) {
    this.timeZone = timeZone;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SalesChannelbyId200Response salesChannelbyId200Response = (SalesChannelbyId200Response) o;
    return Objects.equals(this.conditionRule, salesChannelbyId200Response.conditionRule) &&
        Objects.equals(this.countryCode, salesChannelbyId200Response.countryCode) &&
        Objects.equals(this.cultureInfo, salesChannelbyId200Response.cultureInfo) &&
        Objects.equals(this.currencyCode, salesChannelbyId200Response.currencyCode) &&
        Objects.equals(this.currencyDecimalDigits, salesChannelbyId200Response.currencyDecimalDigits) &&
        Objects.equals(this.currencyFormatInfo, salesChannelbyId200Response.currencyFormatInfo) &&
        Objects.equals(this.currencyLocale, salesChannelbyId200Response.currencyLocale) &&
        Objects.equals(this.currencySymbol, salesChannelbyId200Response.currencySymbol) &&
        Objects.equals(this.id, salesChannelbyId200Response.id) &&
        Objects.equals(this.isActive, salesChannelbyId200Response.isActive) &&
        Objects.equals(this.name, salesChannelbyId200Response.name) &&
        Objects.equals(this.origin, salesChannelbyId200Response.origin) &&
        Objects.equals(this.position, salesChannelbyId200Response.position) &&
        Objects.equals(this.productClusterId, salesChannelbyId200Response.productClusterId) &&
        Objects.equals(this.timeZone, salesChannelbyId200Response.timeZone);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(conditionRule, countryCode, cultureInfo, currencyCode, currencyDecimalDigits, currencyFormatInfo, currencyLocale, currencySymbol, id, isActive, name, origin, position, productClusterId, timeZone);
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
    sb.append("class SalesChannelbyId200Response {\n");
    sb.append("    conditionRule: ").append(toIndentedString(conditionRule)).append("\n");
    sb.append("    countryCode: ").append(toIndentedString(countryCode)).append("\n");
    sb.append("    cultureInfo: ").append(toIndentedString(cultureInfo)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    currencyDecimalDigits: ").append(toIndentedString(currencyDecimalDigits)).append("\n");
    sb.append("    currencyFormatInfo: ").append(toIndentedString(currencyFormatInfo)).append("\n");
    sb.append("    currencyLocale: ").append(toIndentedString(currencyLocale)).append("\n");
    sb.append("    currencySymbol: ").append(toIndentedString(currencySymbol)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    origin: ").append(toIndentedString(origin)).append("\n");
    sb.append("    position: ").append(toIndentedString(position)).append("\n");
    sb.append("    productClusterId: ").append(toIndentedString(productClusterId)).append("\n");
    sb.append("    timeZone: ").append(toIndentedString(timeZone)).append("\n");
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
    openapiFields.add("ConditionRule");
    openapiFields.add("CountryCode");
    openapiFields.add("CultureInfo");
    openapiFields.add("CurrencyCode");
    openapiFields.add("CurrencyDecimalDigits");
    openapiFields.add("CurrencyFormatInfo");
    openapiFields.add("CurrencyLocale");
    openapiFields.add("CurrencySymbol");
    openapiFields.add("Id");
    openapiFields.add("IsActive");
    openapiFields.add("Name");
    openapiFields.add("Origin");
    openapiFields.add("Position");
    openapiFields.add("ProductClusterId");
    openapiFields.add("TimeZone");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SalesChannelbyId200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SalesChannelbyId200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SalesChannelbyId200Response is not found in the empty JSON string", SalesChannelbyId200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SalesChannelbyId200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SalesChannelbyId200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ConditionRule") != null && !jsonObj.get("ConditionRule").isJsonNull()) && !jsonObj.get("ConditionRule").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ConditionRule` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ConditionRule").toString()));
      }
      if ((jsonObj.get("CountryCode") != null && !jsonObj.get("CountryCode").isJsonNull()) && !jsonObj.get("CountryCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CountryCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CountryCode").toString()));
      }
      if ((jsonObj.get("CultureInfo") != null && !jsonObj.get("CultureInfo").isJsonNull()) && !jsonObj.get("CultureInfo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CultureInfo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CultureInfo").toString()));
      }
      if ((jsonObj.get("CurrencyCode") != null && !jsonObj.get("CurrencyCode").isJsonNull()) && !jsonObj.get("CurrencyCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CurrencyCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CurrencyCode").toString()));
      }
      // validate the optional field `CurrencyFormatInfo`
      if (jsonObj.get("CurrencyFormatInfo") != null && !jsonObj.get("CurrencyFormatInfo").isJsonNull()) {
        CurrencyFormatInfo.validateJsonElement(jsonObj.get("CurrencyFormatInfo"));
      }
      if ((jsonObj.get("CurrencySymbol") != null && !jsonObj.get("CurrencySymbol").isJsonNull()) && !jsonObj.get("CurrencySymbol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CurrencySymbol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CurrencySymbol").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Origin") != null && !jsonObj.get("Origin").isJsonNull()) && !jsonObj.get("Origin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Origin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Origin").toString()));
      }
      if ((jsonObj.get("TimeZone") != null && !jsonObj.get("TimeZone").isJsonNull()) && !jsonObj.get("TimeZone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TimeZone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TimeZone").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SalesChannelbyId200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SalesChannelbyId200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SalesChannelbyId200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SalesChannelbyId200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<SalesChannelbyId200Response>() {
           @Override
           public void write(JsonWriter out, SalesChannelbyId200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SalesChannelbyId200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SalesChannelbyId200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SalesChannelbyId200Response
   * @throws IOException if the JSON string is invalid with respect to SalesChannelbyId200Response
   */
  public static SalesChannelbyId200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SalesChannelbyId200Response.class);
  }

  /**
   * Convert an instance of SalesChannelbyId200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

