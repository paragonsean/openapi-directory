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
import org.openapitools.client.model.Item1;

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
 * Response2
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:55:40.459-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Response2 {
  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<Item1> items = new ArrayList<>();

  public Response2() {
  }

  public Response2 items(List<Item1> items) {
    this.items = items;
    return this;
  }

  public Response2 addItemsItem(Item1 itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * List of items and their respective prices applied by Pricing Hub
   * @return items
   */
  @javax.annotation.Nonnull
  public List<Item1> getItems() {
    return items;
  }

  public void setItems(List<Item1> items) {
    this.items = items;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Response2 response2 = (Response2) o;
    return Objects.equals(this.items, response2.items);
  }

  @Override
  public int hashCode() {
    return Objects.hash(items);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Response2 {\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
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
    openapiFields.add("items");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("items");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Response2
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Response2.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Response2 is not found in the empty JSON string", Response2.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Response2.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Response2` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Response2.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("items").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
      }

      JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
      // validate the required field `items` (array)
      for (int i = 0; i < jsonArrayitems.size(); i++) {
        Item1.validateJsonElement(jsonArrayitems.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Response2.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Response2' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Response2> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Response2.class));

       return (TypeAdapter<T>) new TypeAdapter<Response2>() {
           @Override
           public void write(JsonWriter out, Response2 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Response2 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Response2 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Response2
   * @throws IOException if the JSON string is invalid with respect to Response2
   */
  public static Response2 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Response2.class);
  }

  /**
   * Convert an instance of Response2 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

