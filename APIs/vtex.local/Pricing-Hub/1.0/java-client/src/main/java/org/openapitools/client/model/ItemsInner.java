/*
 * Pricing Hub
 * > This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests).      In the B2B scenario, it is common for stores to have personalized prices per customer and complex pricing systems that require external integrations. Pricing Hub is a system developed for the B2B context that works as an intermediary between VTEX and external pricing systems.     In VTEX, B2B stores have the option to use our internal pricing system or an external one. If the store chooses to operate with an external pricing system, Pricing Hub will query an external price calculation API. The external API should then respond with the price for all items in the shopping cart according to its predefined tax rules.    ![Pricing hub protocal diagram](https://user-images.githubusercontent.com/77292838/211634260-e4f7a516-91df-416e-ab43-d9c79d56bc91.png)    ## Implementation    To connect with external pricing systems using Pricing Hub, it is necessary to build a VTEX IO middleware app. We offer two reference implementation templates to simplify this process:    - [C# template](https://github.com/vtex-apps/external-prices-app)  - [Node template](https://github.com/vtex-apps/external-prices-node)    Read the documentation on each repository to learn more about the required steps to use and customize the app.    > The app used by Pricing Hub to connect must be a `major 0`.     ## Specifications    See below all the specifications of the request and the response expected when communicating with Pricing Hub.    ### Price calculation request    The external prices calculation tool must provide an endpoint that will receive a `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices) request. This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.    >⚠️ Responses from Pricing Hub tend to have a greater delay when compared to other VTEX systems. That is expected, however, due to the complexity of its nested requests. The timeout for this request is 900 milliseconds.    In this request, Pricing Hub provides a body in a specific format, exemplified below. This means that either the endpoint must be prepared to receive this body format, or the app must contain a parser to adapt it to the correct format.    #### Request body example    ```json  {      \"item\":           {              \"index\": 0,              \"skuId\": \"880011\",              \"quantity\": 1          },      \"context\":{          \"email\": \"john@email.com\"      }  }  ```    The request body should have the following properties:    | **Attribute** | **Type** | **Description**                                                                                                                                                                                          |  |---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`        | object   | The item whose price is supposed to be fetched by Pricing Hub.                                                                                                                                           |  | ↪ `index`     | integer  | This is the index of the item at Checkout's cart. It has to be unique in the items array.                                                                                                                |  | ↪ `skuId`     | string   | This is the SKU ID of the item that will be priced.                                                                                                                                                      |  | ↪ `quantity`  | integer  | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price. |  | `context`     | object   | The object that contains the context to inform the query.                                                                                                                                                |  | ↪ `email`     | string   | The customer's email address. If there is no value, use an empty string.                                                                                                                                 |    ### External prices provider response    In response to the request sent by Pricing Hub, we expect an outcome in the following format:    ```json  {      \"item\": {          \"price\": 54035,          \"priceTables\": \"special\",          \"index\": 0,          \"skuId\": \"880011\",          \"listPrice\": 54035,          \"costPrice\": 50000,          \"sellingPrice\": 54035,          \"priceValidUntil\": \"2023-01-27T20:29:57Z\",          \"tradePolicyId\": \"special\"      }  }  ```    The response should have the following properties:    | **Attribute**       | **Type** | **Description**                                                                                                                                        |  |---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`              | object   | The object that contains the price data.                                                                                                               |  | ↪ `price`           | integer  | The price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.                    |  | ↪ `priceTables`     | string   | The price table that was used to price the item.                                                                                                       |  | ↪ `index`           | integer  | The same index referring to Checkout's cart that was passed to the API.                                                                                |  | ↪ `skuId`           | string   | The same SKU ID that was passed to the API.                                                                                                            |  | ↪ `listPrice`       | integer  | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `costPrice`       | integer  | The cost price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `sellingPrice`    | integer  | The computed price before applying coupons, taxes or promotions.                                                                                       |  | ↪ `priceValidUntil` | string   | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339. |  | ↪ `tradePolicyId`   | string   | Trade Policy ID.                                                                                                                                       |    ## Index - Pricing Hub API    `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices)  `PUT` [Configure External Price Source](https://developers.vtex.com/docs/api-reference/pricing-hub#put-/config)  
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
 * Each item to be priced by Pricing Hub
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:40.459-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ItemsInner {
  public static final String SERIALIZED_NAME_BRAND_ID = "brandId";
  @SerializedName(SERIALIZED_NAME_BRAND_ID)
  private String brandId = "2000000";

  public static final String SERIALIZED_NAME_CATEGORIES_IDS = "categoriesIds";
  @SerializedName(SERIALIZED_NAME_CATEGORIES_IDS)
  private List<String> categoriesIds = new ArrayList<>(Arrays.asList("1"));

  public static final String SERIALIZED_NAME_INDEX = "index";
  @SerializedName(SERIALIZED_NAME_INDEX)
  private Integer index = 0;

  public static final String SERIALIZED_NAME_PRICE_TABLE_IDS = "priceTableIds";
  @SerializedName(SERIALIZED_NAME_PRICE_TABLE_IDS)
  private List<String> priceTableIds = new ArrayList<>(Arrays.asList("1"));

  public static final String SERIALIZED_NAME_QUANTITY = "quantity";
  @SerializedName(SERIALIZED_NAME_QUANTITY)
  private Integer quantity = 1;

  public static final String SERIALIZED_NAME_SELLER_ID = "sellerId";
  @SerializedName(SERIALIZED_NAME_SELLER_ID)
  private String sellerId = "1";

  public static final String SERIALIZED_NAME_SKU_ID = "skuId";
  @SerializedName(SERIALIZED_NAME_SKU_ID)
  private String skuId = "13";

  public ItemsInner() {
  }

  public ItemsInner brandId(String brandId) {
    this.brandId = brandId;
    return this;
  }

  /**
   * This is the brand ID for the item
   * @return brandId
   */
  @javax.annotation.Nonnull
  public String getBrandId() {
    return brandId;
  }

  public void setBrandId(String brandId) {
    this.brandId = brandId;
  }


  public ItemsInner categoriesIds(List<String> categoriesIds) {
    this.categoriesIds = categoriesIds;
    return this;
  }

  public ItemsInner addCategoriesIdsItem(String categoriesIdsItem) {
    if (this.categoriesIds == null) {
      this.categoriesIds = new ArrayList<>(Arrays.asList("1"));
    }
    this.categoriesIds.add(categoriesIdsItem);
    return this;
  }

  /**
   * ID of the categories that will be used to compute the price
   * @return categoriesIds
   */
  @javax.annotation.Nonnull
  public List<String> getCategoriesIds() {
    return categoriesIds;
  }

  public void setCategoriesIds(List<String> categoriesIds) {
    this.categoriesIds = categoriesIds;
  }


  public ItemsInner index(Integer index) {
    this.index = index;
    return this;
  }

  /**
   * This is the index of the item at Checkout&#39;s cart. It has to be unique in the items array
   * @return index
   */
  @javax.annotation.Nonnull
  public Integer getIndex() {
    return index;
  }

  public void setIndex(Integer index) {
    this.index = index;
  }


  public ItemsInner priceTableIds(List<String> priceTableIds) {
    this.priceTableIds = priceTableIds;
    return this;
  }

  public ItemsInner addPriceTableIdsItem(String priceTableIdsItem) {
    if (this.priceTableIds == null) {
      this.priceTableIds = new ArrayList<>(Arrays.asList("1"));
    }
    this.priceTableIds.add(priceTableIdsItem);
    return this;
  }

  /**
   * IDs of the price tables that will be used to compute the price. More than one price table might be passed to the array. The final price rule might be more complex than the lowest or the highest price
   * @return priceTableIds
   */
  @javax.annotation.Nonnull
  public List<String> getPriceTableIds() {
    return priceTableIds;
  }

  public void setPriceTableIds(List<String> priceTableIds) {
    this.priceTableIds = priceTableIds;
  }


  public ItemsInner quantity(Integer quantity) {
    this.quantity = quantity;
    return this;
  }

  /**
   * This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price
   * @return quantity
   */
  @javax.annotation.Nonnull
  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }


  public ItemsInner sellerId(String sellerId) {
    this.sellerId = sellerId;
    return this;
  }

  /**
   * This is the seller ID for the item
   * @return sellerId
   */
  @javax.annotation.Nonnull
  public String getSellerId() {
    return sellerId;
  }

  public void setSellerId(String sellerId) {
    this.sellerId = sellerId;
  }


  public ItemsInner skuId(String skuId) {
    this.skuId = skuId;
    return this;
  }

  /**
   * This is the sku id of the item that will be priced
   * @return skuId
   */
  @javax.annotation.Nonnull
  public String getSkuId() {
    return skuId;
  }

  public void setSkuId(String skuId) {
    this.skuId = skuId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ItemsInner itemsInner = (ItemsInner) o;
    return Objects.equals(this.brandId, itemsInner.brandId) &&
        Objects.equals(this.categoriesIds, itemsInner.categoriesIds) &&
        Objects.equals(this.index, itemsInner.index) &&
        Objects.equals(this.priceTableIds, itemsInner.priceTableIds) &&
        Objects.equals(this.quantity, itemsInner.quantity) &&
        Objects.equals(this.sellerId, itemsInner.sellerId) &&
        Objects.equals(this.skuId, itemsInner.skuId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(brandId, categoriesIds, index, priceTableIds, quantity, sellerId, skuId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ItemsInner {\n");
    sb.append("    brandId: ").append(toIndentedString(brandId)).append("\n");
    sb.append("    categoriesIds: ").append(toIndentedString(categoriesIds)).append("\n");
    sb.append("    index: ").append(toIndentedString(index)).append("\n");
    sb.append("    priceTableIds: ").append(toIndentedString(priceTableIds)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    sellerId: ").append(toIndentedString(sellerId)).append("\n");
    sb.append("    skuId: ").append(toIndentedString(skuId)).append("\n");
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
    openapiFields.add("brandId");
    openapiFields.add("categoriesIds");
    openapiFields.add("index");
    openapiFields.add("priceTableIds");
    openapiFields.add("quantity");
    openapiFields.add("sellerId");
    openapiFields.add("skuId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("brandId");
    openapiRequiredFields.add("categoriesIds");
    openapiRequiredFields.add("index");
    openapiRequiredFields.add("priceTableIds");
    openapiRequiredFields.add("quantity");
    openapiRequiredFields.add("sellerId");
    openapiRequiredFields.add("skuId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ItemsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ItemsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ItemsInner is not found in the empty JSON string", ItemsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ItemsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ItemsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ItemsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("brandId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `brandId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("brandId").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("categoriesIds") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("categoriesIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `categoriesIds` to be an array in the JSON string but got `%s`", jsonObj.get("categoriesIds").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("priceTableIds") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("priceTableIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `priceTableIds` to be an array in the JSON string but got `%s`", jsonObj.get("priceTableIds").toString()));
      }
      if (!jsonObj.get("sellerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sellerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sellerId").toString()));
      }
      if (!jsonObj.get("skuId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `skuId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("skuId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ItemsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ItemsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ItemsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ItemsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ItemsInner>() {
           @Override
           public void write(JsonWriter out, ItemsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ItemsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ItemsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ItemsInner
   * @throws IOException if the JSON string is invalid with respect to ItemsInner
   */
  public static ItemsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ItemsInner.class);
  }

  /**
   * Convert an instance of ItemsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

