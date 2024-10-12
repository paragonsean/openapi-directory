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
 * GetSKUseller200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:15.452014-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetSKUseller200Response {
  public static final String SERIALIZED_NAME_IS_ACTIVE = "IsActive";
  @SerializedName(SERIALIZED_NAME_IS_ACTIVE)
  private Boolean isActive;

  public static final String SERIALIZED_NAME_IS_PERSISTED = "IsPersisted";
  @SerializedName(SERIALIZED_NAME_IS_PERSISTED)
  private Boolean isPersisted;

  public static final String SERIALIZED_NAME_IS_REMOVED = "IsRemoved";
  @SerializedName(SERIALIZED_NAME_IS_REMOVED)
  private Boolean isRemoved;

  public static final String SERIALIZED_NAME_REQUESTED_UPDATE_DATE = "RequestedUpdateDate";
  @SerializedName(SERIALIZED_NAME_REQUESTED_UPDATE_DATE)
  private String requestedUpdateDate;

  public static final String SERIALIZED_NAME_SELLER_ID = "SellerId";
  @SerializedName(SERIALIZED_NAME_SELLER_ID)
  private String sellerId;

  public static final String SERIALIZED_NAME_SELLER_STOCK_KEEPING_UNIT_ID = "SellerStockKeepingUnitId";
  @SerializedName(SERIALIZED_NAME_SELLER_STOCK_KEEPING_UNIT_ID)
  private String sellerStockKeepingUnitId;

  public static final String SERIALIZED_NAME_SKU_SELLER_ID = "SkuSellerId";
  @SerializedName(SERIALIZED_NAME_SKU_SELLER_ID)
  private Integer skuSellerId;

  public static final String SERIALIZED_NAME_STOCK_KEEPING_UNIT_ID = "StockKeepingUnitId";
  @SerializedName(SERIALIZED_NAME_STOCK_KEEPING_UNIT_ID)
  private Integer stockKeepingUnitId;

  public static final String SERIALIZED_NAME_UPDATE_DATE = "UpdateDate";
  @SerializedName(SERIALIZED_NAME_UPDATE_DATE)
  private String updateDate;

  public GetSKUseller200Response() {
  }

  public GetSKUseller200Response isActive(Boolean isActive) {
    this.isActive = isActive;
    return this;
  }

  /**
   * Defines if the SKU binding is active.
   * @return isActive
   */
  @javax.annotation.Nonnull
  public Boolean getIsActive() {
    return isActive;
  }

  public void setIsActive(Boolean isActive) {
    this.isActive = isActive;
  }


  public GetSKUseller200Response isPersisted(Boolean isPersisted) {
    this.isPersisted = isPersisted;
    return this;
  }

  /**
   * Defines if the seller is persisted.
   * @return isPersisted
   */
  @javax.annotation.Nonnull
  public Boolean getIsPersisted() {
    return isPersisted;
  }

  public void setIsPersisted(Boolean isPersisted) {
    this.isPersisted = isPersisted;
  }


  public GetSKUseller200Response isRemoved(Boolean isRemoved) {
    this.isRemoved = isRemoved;
    return this;
  }

  /**
   * Defines if the seller is removed.
   * @return isRemoved
   */
  @javax.annotation.Nonnull
  public Boolean getIsRemoved() {
    return isRemoved;
  }

  public void setIsRemoved(Boolean isRemoved) {
    this.isRemoved = isRemoved;
  }


  public GetSKUseller200Response requestedUpdateDate(String requestedUpdateDate) {
    this.requestedUpdateDate = requestedUpdateDate;
    return this;
  }

  /**
   * Date when an SKU binding update was requested for the last time, in UTC format.
   * @return requestedUpdateDate
   */
  @javax.annotation.Nullable
  public String getRequestedUpdateDate() {
    return requestedUpdateDate;
  }

  public void setRequestedUpdateDate(String requestedUpdateDate) {
    this.requestedUpdateDate = requestedUpdateDate;
  }


  public GetSKUseller200Response sellerId(String sellerId) {
    this.sellerId = sellerId;
    return this;
  }

  /**
   * ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
   * @return sellerId
   */
  @javax.annotation.Nonnull
  public String getSellerId() {
    return sellerId;
  }

  public void setSellerId(String sellerId) {
    this.sellerId = sellerId;
  }


  public GetSKUseller200Response sellerStockKeepingUnitId(String sellerStockKeepingUnitId) {
    this.sellerStockKeepingUnitId = sellerStockKeepingUnitId;
    return this;
  }

  /**
   * SKU seller ID.
   * @return sellerStockKeepingUnitId
   */
  @javax.annotation.Nonnull
  public String getSellerStockKeepingUnitId() {
    return sellerStockKeepingUnitId;
  }

  public void setSellerStockKeepingUnitId(String sellerStockKeepingUnitId) {
    this.sellerStockKeepingUnitId = sellerStockKeepingUnitId;
  }


  public GetSKUseller200Response skuSellerId(Integer skuSellerId) {
    this.skuSellerId = skuSellerId;
    return this;
  }

  /**
   * SKU ID in the seller&#39;s store.
   * @return skuSellerId
   */
  @javax.annotation.Nonnull
  public Integer getSkuSellerId() {
    return skuSellerId;
  }

  public void setSkuSellerId(Integer skuSellerId) {
    this.skuSellerId = skuSellerId;
  }


  public GetSKUseller200Response stockKeepingUnitId(Integer stockKeepingUnitId) {
    this.stockKeepingUnitId = stockKeepingUnitId;
    return this;
  }

  /**
   * SKU ID in the VTEX marketplace.
   * @return stockKeepingUnitId
   */
  @javax.annotation.Nonnull
  public Integer getStockKeepingUnitId() {
    return stockKeepingUnitId;
  }

  public void setStockKeepingUnitId(Integer stockKeepingUnitId) {
    this.stockKeepingUnitId = stockKeepingUnitId;
  }


  public GetSKUseller200Response updateDate(String updateDate) {
    this.updateDate = updateDate;
    return this;
  }

  /**
   * Date when the SKU binding was updated for the last time, in UTC format.
   * @return updateDate
   */
  @javax.annotation.Nonnull
  public String getUpdateDate() {
    return updateDate;
  }

  public void setUpdateDate(String updateDate) {
    this.updateDate = updateDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetSKUseller200Response getSKUseller200Response = (GetSKUseller200Response) o;
    return Objects.equals(this.isActive, getSKUseller200Response.isActive) &&
        Objects.equals(this.isPersisted, getSKUseller200Response.isPersisted) &&
        Objects.equals(this.isRemoved, getSKUseller200Response.isRemoved) &&
        Objects.equals(this.requestedUpdateDate, getSKUseller200Response.requestedUpdateDate) &&
        Objects.equals(this.sellerId, getSKUseller200Response.sellerId) &&
        Objects.equals(this.sellerStockKeepingUnitId, getSKUseller200Response.sellerStockKeepingUnitId) &&
        Objects.equals(this.skuSellerId, getSKUseller200Response.skuSellerId) &&
        Objects.equals(this.stockKeepingUnitId, getSKUseller200Response.stockKeepingUnitId) &&
        Objects.equals(this.updateDate, getSKUseller200Response.updateDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isActive, isPersisted, isRemoved, requestedUpdateDate, sellerId, sellerStockKeepingUnitId, skuSellerId, stockKeepingUnitId, updateDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetSKUseller200Response {\n");
    sb.append("    isActive: ").append(toIndentedString(isActive)).append("\n");
    sb.append("    isPersisted: ").append(toIndentedString(isPersisted)).append("\n");
    sb.append("    isRemoved: ").append(toIndentedString(isRemoved)).append("\n");
    sb.append("    requestedUpdateDate: ").append(toIndentedString(requestedUpdateDate)).append("\n");
    sb.append("    sellerId: ").append(toIndentedString(sellerId)).append("\n");
    sb.append("    sellerStockKeepingUnitId: ").append(toIndentedString(sellerStockKeepingUnitId)).append("\n");
    sb.append("    skuSellerId: ").append(toIndentedString(skuSellerId)).append("\n");
    sb.append("    stockKeepingUnitId: ").append(toIndentedString(stockKeepingUnitId)).append("\n");
    sb.append("    updateDate: ").append(toIndentedString(updateDate)).append("\n");
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
    openapiFields.add("IsActive");
    openapiFields.add("IsPersisted");
    openapiFields.add("IsRemoved");
    openapiFields.add("RequestedUpdateDate");
    openapiFields.add("SellerId");
    openapiFields.add("SellerStockKeepingUnitId");
    openapiFields.add("SkuSellerId");
    openapiFields.add("StockKeepingUnitId");
    openapiFields.add("UpdateDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("IsActive");
    openapiRequiredFields.add("IsPersisted");
    openapiRequiredFields.add("IsRemoved");
    openapiRequiredFields.add("RequestedUpdateDate");
    openapiRequiredFields.add("SellerId");
    openapiRequiredFields.add("SellerStockKeepingUnitId");
    openapiRequiredFields.add("SkuSellerId");
    openapiRequiredFields.add("StockKeepingUnitId");
    openapiRequiredFields.add("UpdateDate");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetSKUseller200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetSKUseller200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetSKUseller200Response is not found in the empty JSON string", GetSKUseller200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetSKUseller200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetSKUseller200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetSKUseller200Response.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("RequestedUpdateDate") != null && !jsonObj.get("RequestedUpdateDate").isJsonNull()) && !jsonObj.get("RequestedUpdateDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `RequestedUpdateDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("RequestedUpdateDate").toString()));
      }
      if (!jsonObj.get("SellerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SellerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SellerId").toString()));
      }
      if (!jsonObj.get("SellerStockKeepingUnitId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SellerStockKeepingUnitId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SellerStockKeepingUnitId").toString()));
      }
      if (!jsonObj.get("UpdateDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `UpdateDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("UpdateDate").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetSKUseller200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetSKUseller200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetSKUseller200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetSKUseller200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetSKUseller200Response>() {
           @Override
           public void write(JsonWriter out, GetSKUseller200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetSKUseller200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetSKUseller200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetSKUseller200Response
   * @throws IOException if the JSON string is invalid with respect to GetSKUseller200Response
   */
  public static GetSKUseller200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetSKUseller200Response.class);
  }

  /**
   * Convert an instance of GetSKUseller200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

