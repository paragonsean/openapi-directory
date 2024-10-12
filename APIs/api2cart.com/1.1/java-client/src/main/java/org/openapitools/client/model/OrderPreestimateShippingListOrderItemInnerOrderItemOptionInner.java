/*
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
 * OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner {
  public static final String SERIALIZED_NAME_ORDER_ITEM_OPTION_ID = "order_item_option_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ITEM_OPTION_ID)
  private String orderItemOptionId;

  public static final String SERIALIZED_NAME_ORDER_ITEM_OPTION_NAME = "order_item_option_name";
  @SerializedName(SERIALIZED_NAME_ORDER_ITEM_OPTION_NAME)
  private String orderItemOptionName;

  public static final String SERIALIZED_NAME_ORDER_ITEM_OPTION_USED_IN_COMBINATIONS = "order_item_option_used_in_combinations";
  @SerializedName(SERIALIZED_NAME_ORDER_ITEM_OPTION_USED_IN_COMBINATIONS)
  private Boolean orderItemOptionUsedInCombinations;

  public static final String SERIALIZED_NAME_ORDER_ITEM_OPTION_VALUE = "order_item_option_value";
  @SerializedName(SERIALIZED_NAME_ORDER_ITEM_OPTION_VALUE)
  private String orderItemOptionValue;

  public static final String SERIALIZED_NAME_ORDER_ITEM_OPTION_VALUE_ID = "order_item_option_value_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ITEM_OPTION_VALUE_ID)
  private String orderItemOptionValueId;

  public OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner() {
  }

  public OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner orderItemOptionId(String orderItemOptionId) {
    this.orderItemOptionId = orderItemOptionId;
    return this;
  }

  /**
   * Product Option ID. Where x is order item ID, y is order item option ID
   * @return orderItemOptionId
   */
  @javax.annotation.Nullable
  public String getOrderItemOptionId() {
    return orderItemOptionId;
  }

  public void setOrderItemOptionId(String orderItemOptionId) {
    this.orderItemOptionId = orderItemOptionId;
  }


  public OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner orderItemOptionName(String orderItemOptionName) {
    this.orderItemOptionName = orderItemOptionName;
    return this;
  }

  /**
   * Ordered Product Option Name. Where x is order item ID, y is order item option ID
   * @return orderItemOptionName
   */
  @javax.annotation.Nullable
  public String getOrderItemOptionName() {
    return orderItemOptionName;
  }

  public void setOrderItemOptionName(String orderItemOptionName) {
    this.orderItemOptionName = orderItemOptionName;
  }


  public OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner orderItemOptionUsedInCombinations(Boolean orderItemOptionUsedInCombinations) {
    this.orderItemOptionUsedInCombinations = orderItemOptionUsedInCombinations;
    return this;
  }

  /**
   * Product option used in combinations flag, where x is order item ID, y - order item option ID
   * @return orderItemOptionUsedInCombinations
   */
  @javax.annotation.Nullable
  public Boolean getOrderItemOptionUsedInCombinations() {
    return orderItemOptionUsedInCombinations;
  }

  public void setOrderItemOptionUsedInCombinations(Boolean orderItemOptionUsedInCombinations) {
    this.orderItemOptionUsedInCombinations = orderItemOptionUsedInCombinations;
  }


  public OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner orderItemOptionValue(String orderItemOptionValue) {
    this.orderItemOptionValue = orderItemOptionValue;
    return this;
  }

  /**
   * Ordered product option value Where x is order item ID, y - order item option ID
   * @return orderItemOptionValue
   */
  @javax.annotation.Nullable
  public String getOrderItemOptionValue() {
    return orderItemOptionValue;
  }

  public void setOrderItemOptionValue(String orderItemOptionValue) {
    this.orderItemOptionValue = orderItemOptionValue;
  }


  public OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner orderItemOptionValueId(String orderItemOptionValueId) {
    this.orderItemOptionValueId = orderItemOptionValueId;
    return this;
  }

  /**
   * Product option value ID, where x is order item ID, y - order item option ID
   * @return orderItemOptionValueId
   */
  @javax.annotation.Nullable
  public String getOrderItemOptionValueId() {
    return orderItemOptionValueId;
  }

  public void setOrderItemOptionValueId(String orderItemOptionValueId) {
    this.orderItemOptionValueId = orderItemOptionValueId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner orderPreestimateShippingListOrderItemInnerOrderItemOptionInner = (OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner) o;
    return Objects.equals(this.orderItemOptionId, orderPreestimateShippingListOrderItemInnerOrderItemOptionInner.orderItemOptionId) &&
        Objects.equals(this.orderItemOptionName, orderPreestimateShippingListOrderItemInnerOrderItemOptionInner.orderItemOptionName) &&
        Objects.equals(this.orderItemOptionUsedInCombinations, orderPreestimateShippingListOrderItemInnerOrderItemOptionInner.orderItemOptionUsedInCombinations) &&
        Objects.equals(this.orderItemOptionValue, orderPreestimateShippingListOrderItemInnerOrderItemOptionInner.orderItemOptionValue) &&
        Objects.equals(this.orderItemOptionValueId, orderPreestimateShippingListOrderItemInnerOrderItemOptionInner.orderItemOptionValueId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(orderItemOptionId, orderItemOptionName, orderItemOptionUsedInCombinations, orderItemOptionValue, orderItemOptionValueId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner {\n");
    sb.append("    orderItemOptionId: ").append(toIndentedString(orderItemOptionId)).append("\n");
    sb.append("    orderItemOptionName: ").append(toIndentedString(orderItemOptionName)).append("\n");
    sb.append("    orderItemOptionUsedInCombinations: ").append(toIndentedString(orderItemOptionUsedInCombinations)).append("\n");
    sb.append("    orderItemOptionValue: ").append(toIndentedString(orderItemOptionValue)).append("\n");
    sb.append("    orderItemOptionValueId: ").append(toIndentedString(orderItemOptionValueId)).append("\n");
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
    openapiFields.add("order_item_option_id");
    openapiFields.add("order_item_option_name");
    openapiFields.add("order_item_option_used_in_combinations");
    openapiFields.add("order_item_option_value");
    openapiFields.add("order_item_option_value_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner is not found in the empty JSON string", OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("order_item_option_id") != null && !jsonObj.get("order_item_option_id").isJsonNull()) && !jsonObj.get("order_item_option_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_item_option_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_item_option_id").toString()));
      }
      if ((jsonObj.get("order_item_option_name") != null && !jsonObj.get("order_item_option_name").isJsonNull()) && !jsonObj.get("order_item_option_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_item_option_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_item_option_name").toString()));
      }
      if ((jsonObj.get("order_item_option_value") != null && !jsonObj.get("order_item_option_value").isJsonNull()) && !jsonObj.get("order_item_option_value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_item_option_value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_item_option_value").toString()));
      }
      if ((jsonObj.get("order_item_option_value_id") != null && !jsonObj.get("order_item_option_value_id").isJsonNull()) && !jsonObj.get("order_item_option_value_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_item_option_value_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_item_option_value_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner>() {
           @Override
           public void write(JsonWriter out, OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner
   * @throws IOException if the JSON string is invalid with respect to OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner
   */
  public static OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner.class);
  }

  /**
   * Convert an instance of OrderPreestimateShippingListOrderItemInnerOrderItemOptionInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

