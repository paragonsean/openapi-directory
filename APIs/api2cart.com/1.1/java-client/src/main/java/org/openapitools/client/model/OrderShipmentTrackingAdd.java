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
 * OrderShipmentTrackingAdd
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderShipmentTrackingAdd {
  public static final String SERIALIZED_NAME_CARRIER_ID = "carrier_id";
  @SerializedName(SERIALIZED_NAME_CARRIER_ID)
  private String carrierId;

  public static final String SERIALIZED_NAME_ORDER_ID = "order_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_SEND_NOTIFICATIONS = "send_notifications";
  @SerializedName(SERIALIZED_NAME_SEND_NOTIFICATIONS)
  private Boolean sendNotifications = false;

  public static final String SERIALIZED_NAME_SHIPMENT_ID = "shipment_id";
  @SerializedName(SERIALIZED_NAME_SHIPMENT_ID)
  private String shipmentId;

  public static final String SERIALIZED_NAME_STORE_ID = "store_id";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private String storeId;

  public static final String SERIALIZED_NAME_TRACKING_LINK = "tracking_link";
  @SerializedName(SERIALIZED_NAME_TRACKING_LINK)
  private String trackingLink;

  public static final String SERIALIZED_NAME_TRACKING_NUMBER = "tracking_number";
  @SerializedName(SERIALIZED_NAME_TRACKING_NUMBER)
  private String trackingNumber;

  public static final String SERIALIZED_NAME_TRACKING_PROVIDER = "tracking_provider";
  @SerializedName(SERIALIZED_NAME_TRACKING_PROVIDER)
  private String trackingProvider;

  public OrderShipmentTrackingAdd() {
  }

  public OrderShipmentTrackingAdd carrierId(String carrierId) {
    this.carrierId = carrierId;
    return this;
  }

  /**
   * Defines tracking carrier id
   * @return carrierId
   */
  @javax.annotation.Nullable
  public String getCarrierId() {
    return carrierId;
  }

  public void setCarrierId(String carrierId) {
    this.carrierId = carrierId;
  }


  public OrderShipmentTrackingAdd orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * Defines the order id
   * @return orderId
   */
  @javax.annotation.Nullable
  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  public OrderShipmentTrackingAdd sendNotifications(Boolean sendNotifications) {
    this.sendNotifications = sendNotifications;
    return this;
  }

  /**
   * Send notifications to customer after tracking was created
   * @return sendNotifications
   */
  @javax.annotation.Nullable
  public Boolean getSendNotifications() {
    return sendNotifications;
  }

  public void setSendNotifications(Boolean sendNotifications) {
    this.sendNotifications = sendNotifications;
  }


  public OrderShipmentTrackingAdd shipmentId(String shipmentId) {
    this.shipmentId = shipmentId;
    return this;
  }

  /**
   * Shipment id indicates the number of delivery
   * @return shipmentId
   */
  @javax.annotation.Nonnull
  public String getShipmentId() {
    return shipmentId;
  }

  public void setShipmentId(String shipmentId) {
    this.shipmentId = shipmentId;
  }


  public OrderShipmentTrackingAdd storeId(String storeId) {
    this.storeId = storeId;
    return this;
  }

  /**
   * Store Id
   * @return storeId
   */
  @javax.annotation.Nullable
  public String getStoreId() {
    return storeId;
  }

  public void setStoreId(String storeId) {
    this.storeId = storeId;
  }


  public OrderShipmentTrackingAdd trackingLink(String trackingLink) {
    this.trackingLink = trackingLink;
    return this;
  }

  /**
   * Defines custom tracking link
   * @return trackingLink
   */
  @javax.annotation.Nullable
  public String getTrackingLink() {
    return trackingLink;
  }

  public void setTrackingLink(String trackingLink) {
    this.trackingLink = trackingLink;
  }


  public OrderShipmentTrackingAdd trackingNumber(String trackingNumber) {
    this.trackingNumber = trackingNumber;
    return this;
  }

  /**
   * Defines tracking number
   * @return trackingNumber
   */
  @javax.annotation.Nonnull
  public String getTrackingNumber() {
    return trackingNumber;
  }

  public void setTrackingNumber(String trackingNumber) {
    this.trackingNumber = trackingNumber;
  }


  public OrderShipmentTrackingAdd trackingProvider(String trackingProvider) {
    this.trackingProvider = trackingProvider;
    return this;
  }

  /**
   * Defines name of the company which provides shipment tracking
   * @return trackingProvider
   */
  @javax.annotation.Nullable
  public String getTrackingProvider() {
    return trackingProvider;
  }

  public void setTrackingProvider(String trackingProvider) {
    this.trackingProvider = trackingProvider;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderShipmentTrackingAdd orderShipmentTrackingAdd = (OrderShipmentTrackingAdd) o;
    return Objects.equals(this.carrierId, orderShipmentTrackingAdd.carrierId) &&
        Objects.equals(this.orderId, orderShipmentTrackingAdd.orderId) &&
        Objects.equals(this.sendNotifications, orderShipmentTrackingAdd.sendNotifications) &&
        Objects.equals(this.shipmentId, orderShipmentTrackingAdd.shipmentId) &&
        Objects.equals(this.storeId, orderShipmentTrackingAdd.storeId) &&
        Objects.equals(this.trackingLink, orderShipmentTrackingAdd.trackingLink) &&
        Objects.equals(this.trackingNumber, orderShipmentTrackingAdd.trackingNumber) &&
        Objects.equals(this.trackingProvider, orderShipmentTrackingAdd.trackingProvider);
  }

  @Override
  public int hashCode() {
    return Objects.hash(carrierId, orderId, sendNotifications, shipmentId, storeId, trackingLink, trackingNumber, trackingProvider);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderShipmentTrackingAdd {\n");
    sb.append("    carrierId: ").append(toIndentedString(carrierId)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    sendNotifications: ").append(toIndentedString(sendNotifications)).append("\n");
    sb.append("    shipmentId: ").append(toIndentedString(shipmentId)).append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
    sb.append("    trackingLink: ").append(toIndentedString(trackingLink)).append("\n");
    sb.append("    trackingNumber: ").append(toIndentedString(trackingNumber)).append("\n");
    sb.append("    trackingProvider: ").append(toIndentedString(trackingProvider)).append("\n");
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
    openapiFields.add("carrier_id");
    openapiFields.add("order_id");
    openapiFields.add("send_notifications");
    openapiFields.add("shipment_id");
    openapiFields.add("store_id");
    openapiFields.add("tracking_link");
    openapiFields.add("tracking_number");
    openapiFields.add("tracking_provider");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("shipment_id");
    openapiRequiredFields.add("tracking_number");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderShipmentTrackingAdd
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderShipmentTrackingAdd.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderShipmentTrackingAdd is not found in the empty JSON string", OrderShipmentTrackingAdd.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderShipmentTrackingAdd.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderShipmentTrackingAdd` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OrderShipmentTrackingAdd.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("carrier_id") != null && !jsonObj.get("carrier_id").isJsonNull()) && !jsonObj.get("carrier_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrier_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrier_id").toString()));
      }
      if ((jsonObj.get("order_id") != null && !jsonObj.get("order_id").isJsonNull()) && !jsonObj.get("order_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_id").toString()));
      }
      if (!jsonObj.get("shipment_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipment_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipment_id").toString()));
      }
      if ((jsonObj.get("store_id") != null && !jsonObj.get("store_id").isJsonNull()) && !jsonObj.get("store_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `store_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("store_id").toString()));
      }
      if ((jsonObj.get("tracking_link") != null && !jsonObj.get("tracking_link").isJsonNull()) && !jsonObj.get("tracking_link").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tracking_link` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tracking_link").toString()));
      }
      if (!jsonObj.get("tracking_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tracking_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tracking_number").toString()));
      }
      if ((jsonObj.get("tracking_provider") != null && !jsonObj.get("tracking_provider").isJsonNull()) && !jsonObj.get("tracking_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tracking_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tracking_provider").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrderShipmentTrackingAdd.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderShipmentTrackingAdd' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderShipmentTrackingAdd> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderShipmentTrackingAdd.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderShipmentTrackingAdd>() {
           @Override
           public void write(JsonWriter out, OrderShipmentTrackingAdd value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderShipmentTrackingAdd read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderShipmentTrackingAdd given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderShipmentTrackingAdd
   * @throws IOException if the JSON string is invalid with respect to OrderShipmentTrackingAdd
   */
  public static OrderShipmentTrackingAdd fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderShipmentTrackingAdd.class);
  }

  /**
   * Convert an instance of OrderShipmentTrackingAdd to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

