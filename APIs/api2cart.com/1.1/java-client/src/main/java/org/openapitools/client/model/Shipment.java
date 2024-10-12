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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.A2CDateTime;
import org.openapitools.client.model.ShipmentItem;
import org.openapitools.client.model.ShipmentTrackingNumber;

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
 * Shipment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Shipment {
  public static final String SERIALIZED_NAME_ADDITIONAL_FIELDS = "additional_fields";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_FIELDS)
  private Object additionalFields;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private A2CDateTime createdAt;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private Object customFields;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_SHIPPED = "is_shipped";
  @SerializedName(SERIALIZED_NAME_IS_SHIPPED)
  private Boolean isShipped;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<ShipmentItem> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODIFIED_TIME = "modified_time";
  @SerializedName(SERIALIZED_NAME_MODIFIED_TIME)
  private A2CDateTime modifiedTime;

  public static final String SERIALIZED_NAME_ORDER_ID = "order_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_SHIPMENT_PROVIDER = "shipment_provider";
  @SerializedName(SERIALIZED_NAME_SHIPMENT_PROVIDER)
  private String shipmentProvider;

  public static final String SERIALIZED_NAME_TRACKING_NUMBERS = "tracking_numbers";
  @SerializedName(SERIALIZED_NAME_TRACKING_NUMBERS)
  private List<ShipmentTrackingNumber> trackingNumbers = new ArrayList<>();

  public static final String SERIALIZED_NAME_WAREHOUSE_ID = "warehouse_id";
  @SerializedName(SERIALIZED_NAME_WAREHOUSE_ID)
  private String warehouseId;

  public Shipment() {
  }

  public Shipment additionalFields(Object additionalFields) {
    this.additionalFields = additionalFields;
    return this;
  }

  /**
   * Get additionalFields
   * @return additionalFields
   */
  @javax.annotation.Nullable
  public Object getAdditionalFields() {
    return additionalFields;
  }

  public void setAdditionalFields(Object additionalFields) {
    this.additionalFields = additionalFields;
  }


  public Shipment createdAt(A2CDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public A2CDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(A2CDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public Shipment customFields(Object customFields) {
    this.customFields = customFields;
    return this;
  }

  /**
   * Get customFields
   * @return customFields
   */
  @javax.annotation.Nullable
  public Object getCustomFields() {
    return customFields;
  }

  public void setCustomFields(Object customFields) {
    this.customFields = customFields;
  }


  public Shipment id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Shipment isShipped(Boolean isShipped) {
    this.isShipped = isShipped;
    return this;
  }

  /**
   * Get isShipped
   * @return isShipped
   */
  @javax.annotation.Nullable
  public Boolean getIsShipped() {
    return isShipped;
  }

  public void setIsShipped(Boolean isShipped) {
    this.isShipped = isShipped;
  }


  public Shipment items(List<ShipmentItem> items) {
    this.items = items;
    return this;
  }

  public Shipment addItemsItem(ShipmentItem itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Get items
   * @return items
   */
  @javax.annotation.Nullable
  public List<ShipmentItem> getItems() {
    return items;
  }

  public void setItems(List<ShipmentItem> items) {
    this.items = items;
  }


  public Shipment modifiedTime(A2CDateTime modifiedTime) {
    this.modifiedTime = modifiedTime;
    return this;
  }

  /**
   * Get modifiedTime
   * @return modifiedTime
   */
  @javax.annotation.Nullable
  public A2CDateTime getModifiedTime() {
    return modifiedTime;
  }

  public void setModifiedTime(A2CDateTime modifiedTime) {
    this.modifiedTime = modifiedTime;
  }


  public Shipment orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * Get orderId
   * @return orderId
   */
  @javax.annotation.Nullable
  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  public Shipment shipmentProvider(String shipmentProvider) {
    this.shipmentProvider = shipmentProvider;
    return this;
  }

  /**
   * Get shipmentProvider
   * @return shipmentProvider
   */
  @javax.annotation.Nullable
  public String getShipmentProvider() {
    return shipmentProvider;
  }

  public void setShipmentProvider(String shipmentProvider) {
    this.shipmentProvider = shipmentProvider;
  }


  public Shipment trackingNumbers(List<ShipmentTrackingNumber> trackingNumbers) {
    this.trackingNumbers = trackingNumbers;
    return this;
  }

  public Shipment addTrackingNumbersItem(ShipmentTrackingNumber trackingNumbersItem) {
    if (this.trackingNumbers == null) {
      this.trackingNumbers = new ArrayList<>();
    }
    this.trackingNumbers.add(trackingNumbersItem);
    return this;
  }

  /**
   * Get trackingNumbers
   * @return trackingNumbers
   */
  @javax.annotation.Nullable
  public List<ShipmentTrackingNumber> getTrackingNumbers() {
    return trackingNumbers;
  }

  public void setTrackingNumbers(List<ShipmentTrackingNumber> trackingNumbers) {
    this.trackingNumbers = trackingNumbers;
  }


  public Shipment warehouseId(String warehouseId) {
    this.warehouseId = warehouseId;
    return this;
  }

  /**
   * Get warehouseId
   * @return warehouseId
   */
  @javax.annotation.Nullable
  public String getWarehouseId() {
    return warehouseId;
  }

  public void setWarehouseId(String warehouseId) {
    this.warehouseId = warehouseId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Shipment shipment = (Shipment) o;
    return Objects.equals(this.additionalFields, shipment.additionalFields) &&
        Objects.equals(this.createdAt, shipment.createdAt) &&
        Objects.equals(this.customFields, shipment.customFields) &&
        Objects.equals(this.id, shipment.id) &&
        Objects.equals(this.isShipped, shipment.isShipped) &&
        Objects.equals(this.items, shipment.items) &&
        Objects.equals(this.modifiedTime, shipment.modifiedTime) &&
        Objects.equals(this.orderId, shipment.orderId) &&
        Objects.equals(this.shipmentProvider, shipment.shipmentProvider) &&
        Objects.equals(this.trackingNumbers, shipment.trackingNumbers) &&
        Objects.equals(this.warehouseId, shipment.warehouseId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalFields, createdAt, customFields, id, isShipped, items, modifiedTime, orderId, shipmentProvider, trackingNumbers, warehouseId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Shipment {\n");
    sb.append("    additionalFields: ").append(toIndentedString(additionalFields)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isShipped: ").append(toIndentedString(isShipped)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    modifiedTime: ").append(toIndentedString(modifiedTime)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    shipmentProvider: ").append(toIndentedString(shipmentProvider)).append("\n");
    sb.append("    trackingNumbers: ").append(toIndentedString(trackingNumbers)).append("\n");
    sb.append("    warehouseId: ").append(toIndentedString(warehouseId)).append("\n");
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
    openapiFields.add("additional_fields");
    openapiFields.add("created_at");
    openapiFields.add("custom_fields");
    openapiFields.add("id");
    openapiFields.add("is_shipped");
    openapiFields.add("items");
    openapiFields.add("modified_time");
    openapiFields.add("order_id");
    openapiFields.add("shipment_provider");
    openapiFields.add("tracking_numbers");
    openapiFields.add("warehouse_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Shipment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Shipment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Shipment is not found in the empty JSON string", Shipment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Shipment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Shipment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `created_at`
      if (jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) {
        A2CDateTime.validateJsonElement(jsonObj.get("created_at"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            ShipmentItem.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      // validate the optional field `modified_time`
      if (jsonObj.get("modified_time") != null && !jsonObj.get("modified_time").isJsonNull()) {
        A2CDateTime.validateJsonElement(jsonObj.get("modified_time"));
      }
      if ((jsonObj.get("order_id") != null && !jsonObj.get("order_id").isJsonNull()) && !jsonObj.get("order_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_id").toString()));
      }
      if ((jsonObj.get("shipment_provider") != null && !jsonObj.get("shipment_provider").isJsonNull()) && !jsonObj.get("shipment_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipment_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipment_provider").toString()));
      }
      if (jsonObj.get("tracking_numbers") != null && !jsonObj.get("tracking_numbers").isJsonNull()) {
        JsonArray jsonArraytrackingNumbers = jsonObj.getAsJsonArray("tracking_numbers");
        if (jsonArraytrackingNumbers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tracking_numbers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tracking_numbers` to be an array in the JSON string but got `%s`", jsonObj.get("tracking_numbers").toString()));
          }

          // validate the optional field `tracking_numbers` (array)
          for (int i = 0; i < jsonArraytrackingNumbers.size(); i++) {
            ShipmentTrackingNumber.validateJsonElement(jsonArraytrackingNumbers.get(i));
          };
        }
      }
      if ((jsonObj.get("warehouse_id") != null && !jsonObj.get("warehouse_id").isJsonNull()) && !jsonObj.get("warehouse_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `warehouse_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("warehouse_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Shipment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Shipment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Shipment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Shipment.class));

       return (TypeAdapter<T>) new TypeAdapter<Shipment>() {
           @Override
           public void write(JsonWriter out, Shipment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Shipment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Shipment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Shipment
   * @throws IOException if the JSON string is invalid with respect to Shipment
   */
  public static Shipment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Shipment.class);
  }

  /**
   * Convert an instance of Shipment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

