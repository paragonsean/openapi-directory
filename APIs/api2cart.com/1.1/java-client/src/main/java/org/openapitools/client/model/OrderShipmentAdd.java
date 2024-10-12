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
import org.openapitools.client.model.OrderShipmentAddItemsInner;
import org.openapitools.client.model.OrderShipmentAddTrackingNumbersInner;

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
 * OrderShipmentAdd
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderShipmentAdd {
  public static final String SERIALIZED_NAME_ADJUST_STOCK = "adjust_stock";
  @SerializedName(SERIALIZED_NAME_ADJUST_STOCK)
  private Boolean adjustStock = false;

  public static final String SERIALIZED_NAME_ENABLE_CACHE = "enable_cache";
  @SerializedName(SERIALIZED_NAME_ENABLE_CACHE)
  private Boolean enableCache = false;

  public static final String SERIALIZED_NAME_IS_SHIPPED = "is_shipped";
  @SerializedName(SERIALIZED_NAME_IS_SHIPPED)
  private Boolean isShipped = true;

  public static final String SERIALIZED_NAME_ITEMS = "items";
  @SerializedName(SERIALIZED_NAME_ITEMS)
  private List<OrderShipmentAddItemsInner> items = new ArrayList<>();

  public static final String SERIALIZED_NAME_ORDER_ID = "order_id";
  @SerializedName(SERIALIZED_NAME_ORDER_ID)
  private String orderId;

  public static final String SERIALIZED_NAME_SEND_NOTIFICATIONS = "send_notifications";
  @SerializedName(SERIALIZED_NAME_SEND_NOTIFICATIONS)
  private Boolean sendNotifications = false;

  public static final String SERIALIZED_NAME_SHIPMENT_PROVIDER = "shipment_provider";
  @SerializedName(SERIALIZED_NAME_SHIPMENT_PROVIDER)
  private String shipmentProvider;

  public static final String SERIALIZED_NAME_SHIPPING_METHOD = "shipping_method";
  @SerializedName(SERIALIZED_NAME_SHIPPING_METHOD)
  private String shippingMethod;

  public static final String SERIALIZED_NAME_STORE_ID = "store_id";
  @SerializedName(SERIALIZED_NAME_STORE_ID)
  private String storeId;

  public static final String SERIALIZED_NAME_TRACKING_LINK = "tracking_link";
  @SerializedName(SERIALIZED_NAME_TRACKING_LINK)
  private String trackingLink;

  public static final String SERIALIZED_NAME_TRACKING_NUMBERS = "tracking_numbers";
  @SerializedName(SERIALIZED_NAME_TRACKING_NUMBERS)
  private List<OrderShipmentAddTrackingNumbersInner> trackingNumbers = new ArrayList<>();

  public static final String SERIALIZED_NAME_WAREHOUSE_ID = "warehouse_id";
  @SerializedName(SERIALIZED_NAME_WAREHOUSE_ID)
  private String warehouseId;

  public OrderShipmentAdd() {
  }

  public OrderShipmentAdd adjustStock(Boolean adjustStock) {
    this.adjustStock = adjustStock;
    return this;
  }

  /**
   * This parameter is used for adjust stock.
   * @return adjustStock
   */
  @javax.annotation.Nullable
  public Boolean getAdjustStock() {
    return adjustStock;
  }

  public void setAdjustStock(Boolean adjustStock) {
    this.adjustStock = adjustStock;
  }


  public OrderShipmentAdd enableCache(Boolean enableCache) {
    this.enableCache = enableCache;
    return this;
  }

  /**
   * If the value is &#39;true&#39; and order exist in our cache, we will use order.info from cache to prepare shipment items.
   * @return enableCache
   */
  @javax.annotation.Nullable
  public Boolean getEnableCache() {
    return enableCache;
  }

  public void setEnableCache(Boolean enableCache) {
    this.enableCache = enableCache;
  }


  public OrderShipmentAdd isShipped(Boolean isShipped) {
    this.isShipped = isShipped;
    return this;
  }

  /**
   * Defines shipment&#39;s status
   * @return isShipped
   */
  @javax.annotation.Nullable
  public Boolean getIsShipped() {
    return isShipped;
  }

  public void setIsShipped(Boolean isShipped) {
    this.isShipped = isShipped;
  }


  public OrderShipmentAdd items(List<OrderShipmentAddItemsInner> items) {
    this.items = items;
    return this;
  }

  public OrderShipmentAdd addItemsItem(OrderShipmentAddItemsInner itemsItem) {
    if (this.items == null) {
      this.items = new ArrayList<>();
    }
    this.items.add(itemsItem);
    return this;
  }

  /**
   * Defines items in the order that will be shipped
   * @return items
   */
  @javax.annotation.Nullable
  public List<OrderShipmentAddItemsInner> getItems() {
    return items;
  }

  public void setItems(List<OrderShipmentAddItemsInner> items) {
    this.items = items;
  }


  public OrderShipmentAdd orderId(String orderId) {
    this.orderId = orderId;
    return this;
  }

  /**
   * Defines the order for which the shipment will be created
   * @return orderId
   */
  @javax.annotation.Nullable
  public String getOrderId() {
    return orderId;
  }

  public void setOrderId(String orderId) {
    this.orderId = orderId;
  }


  public OrderShipmentAdd sendNotifications(Boolean sendNotifications) {
    this.sendNotifications = sendNotifications;
    return this;
  }

  /**
   * Send notifications to customer after shipment was created
   * @return sendNotifications
   */
  @javax.annotation.Nullable
  public Boolean getSendNotifications() {
    return sendNotifications;
  }

  public void setSendNotifications(Boolean sendNotifications) {
    this.sendNotifications = sendNotifications;
  }


  public OrderShipmentAdd shipmentProvider(String shipmentProvider) {
    this.shipmentProvider = shipmentProvider;
    return this;
  }

  /**
   * Defines company name that provide tracking of shipment
   * @return shipmentProvider
   */
  @javax.annotation.Nullable
  public String getShipmentProvider() {
    return shipmentProvider;
  }

  public void setShipmentProvider(String shipmentProvider) {
    this.shipmentProvider = shipmentProvider;
  }


  public OrderShipmentAdd shippingMethod(String shippingMethod) {
    this.shippingMethod = shippingMethod;
    return this;
  }

  /**
   * Define shipping method
   * @return shippingMethod
   */
  @javax.annotation.Nullable
  public String getShippingMethod() {
    return shippingMethod;
  }

  public void setShippingMethod(String shippingMethod) {
    this.shippingMethod = shippingMethod;
  }


  public OrderShipmentAdd storeId(String storeId) {
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


  public OrderShipmentAdd trackingLink(String trackingLink) {
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


  public OrderShipmentAdd trackingNumbers(List<OrderShipmentAddTrackingNumbersInner> trackingNumbers) {
    this.trackingNumbers = trackingNumbers;
    return this;
  }

  public OrderShipmentAdd addTrackingNumbersItem(OrderShipmentAddTrackingNumbersInner trackingNumbersItem) {
    if (this.trackingNumbers == null) {
      this.trackingNumbers = new ArrayList<>();
    }
    this.trackingNumbers.add(trackingNumbersItem);
    return this;
  }

  /**
   * Defines shipment&#39;s tracking numbers that have to be added&lt;/br&gt; How set tracking numbers to appropriate carrier:&lt;ul&gt;&lt;li&gt;tracking_numbers[]&#x3D;a2c.demo1,a2c.demo2 - set default carrier&lt;/li&gt;&lt;li&gt;tracking_numbers[&lt;b&gt;carrier_id&lt;/b&gt;]&#x3D;a2c.demo - set appropriate carrier&lt;/li&gt;&lt;/ul&gt;To get the list of carriers IDs that are available in your store, use the &lt;a href &#x3D; \&quot;https://api2cart.com/docs/#/cart/CartInfo\&quot;&gt;cart.info&lt;/a &gt; method
   * @return trackingNumbers
   */
  @javax.annotation.Nullable
  public List<OrderShipmentAddTrackingNumbersInner> getTrackingNumbers() {
    return trackingNumbers;
  }

  public void setTrackingNumbers(List<OrderShipmentAddTrackingNumbersInner> trackingNumbers) {
    this.trackingNumbers = trackingNumbers;
  }


  public OrderShipmentAdd warehouseId(String warehouseId) {
    this.warehouseId = warehouseId;
    return this;
  }

  /**
   * This parameter is used for selecting a warehouse where you need to set/modify a product quantity.
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
    OrderShipmentAdd orderShipmentAdd = (OrderShipmentAdd) o;
    return Objects.equals(this.adjustStock, orderShipmentAdd.adjustStock) &&
        Objects.equals(this.enableCache, orderShipmentAdd.enableCache) &&
        Objects.equals(this.isShipped, orderShipmentAdd.isShipped) &&
        Objects.equals(this.items, orderShipmentAdd.items) &&
        Objects.equals(this.orderId, orderShipmentAdd.orderId) &&
        Objects.equals(this.sendNotifications, orderShipmentAdd.sendNotifications) &&
        Objects.equals(this.shipmentProvider, orderShipmentAdd.shipmentProvider) &&
        Objects.equals(this.shippingMethod, orderShipmentAdd.shippingMethod) &&
        Objects.equals(this.storeId, orderShipmentAdd.storeId) &&
        Objects.equals(this.trackingLink, orderShipmentAdd.trackingLink) &&
        Objects.equals(this.trackingNumbers, orderShipmentAdd.trackingNumbers) &&
        Objects.equals(this.warehouseId, orderShipmentAdd.warehouseId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(adjustStock, enableCache, isShipped, items, orderId, sendNotifications, shipmentProvider, shippingMethod, storeId, trackingLink, trackingNumbers, warehouseId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderShipmentAdd {\n");
    sb.append("    adjustStock: ").append(toIndentedString(adjustStock)).append("\n");
    sb.append("    enableCache: ").append(toIndentedString(enableCache)).append("\n");
    sb.append("    isShipped: ").append(toIndentedString(isShipped)).append("\n");
    sb.append("    items: ").append(toIndentedString(items)).append("\n");
    sb.append("    orderId: ").append(toIndentedString(orderId)).append("\n");
    sb.append("    sendNotifications: ").append(toIndentedString(sendNotifications)).append("\n");
    sb.append("    shipmentProvider: ").append(toIndentedString(shipmentProvider)).append("\n");
    sb.append("    shippingMethod: ").append(toIndentedString(shippingMethod)).append("\n");
    sb.append("    storeId: ").append(toIndentedString(storeId)).append("\n");
    sb.append("    trackingLink: ").append(toIndentedString(trackingLink)).append("\n");
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
    openapiFields.add("adjust_stock");
    openapiFields.add("enable_cache");
    openapiFields.add("is_shipped");
    openapiFields.add("items");
    openapiFields.add("order_id");
    openapiFields.add("send_notifications");
    openapiFields.add("shipment_provider");
    openapiFields.add("shipping_method");
    openapiFields.add("store_id");
    openapiFields.add("tracking_link");
    openapiFields.add("tracking_numbers");
    openapiFields.add("warehouse_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderShipmentAdd
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderShipmentAdd.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderShipmentAdd is not found in the empty JSON string", OrderShipmentAdd.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderShipmentAdd.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderShipmentAdd` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("items") != null && !jsonObj.get("items").isJsonNull()) {
        JsonArray jsonArrayitems = jsonObj.getAsJsonArray("items");
        if (jsonArrayitems != null) {
          // ensure the json data is an array
          if (!jsonObj.get("items").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `items` to be an array in the JSON string but got `%s`", jsonObj.get("items").toString()));
          }

          // validate the optional field `items` (array)
          for (int i = 0; i < jsonArrayitems.size(); i++) {
            OrderShipmentAddItemsInner.validateJsonElement(jsonArrayitems.get(i));
          };
        }
      }
      if ((jsonObj.get("order_id") != null && !jsonObj.get("order_id").isJsonNull()) && !jsonObj.get("order_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `order_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("order_id").toString()));
      }
      if ((jsonObj.get("shipment_provider") != null && !jsonObj.get("shipment_provider").isJsonNull()) && !jsonObj.get("shipment_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipment_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipment_provider").toString()));
      }
      if ((jsonObj.get("shipping_method") != null && !jsonObj.get("shipping_method").isJsonNull()) && !jsonObj.get("shipping_method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipping_method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipping_method").toString()));
      }
      if ((jsonObj.get("store_id") != null && !jsonObj.get("store_id").isJsonNull()) && !jsonObj.get("store_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `store_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("store_id").toString()));
      }
      if ((jsonObj.get("tracking_link") != null && !jsonObj.get("tracking_link").isJsonNull()) && !jsonObj.get("tracking_link").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tracking_link` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tracking_link").toString()));
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
            OrderShipmentAddTrackingNumbersInner.validateJsonElement(jsonArraytrackingNumbers.get(i));
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
       if (!OrderShipmentAdd.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderShipmentAdd' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderShipmentAdd> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderShipmentAdd.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderShipmentAdd>() {
           @Override
           public void write(JsonWriter out, OrderShipmentAdd value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderShipmentAdd read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderShipmentAdd given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderShipmentAdd
   * @throws IOException if the JSON string is invalid with respect to OrderShipmentAdd
   */
  public static OrderShipmentAdd fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderShipmentAdd.class);
  }

  /**
   * Convert an instance of OrderShipmentAdd to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

