/*
 * Noosh API application
 * Full description of Noosh API
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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ShipmentRequestBaseVO;
import org.openapitools.client.model.SpecBaseVO;

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
 * Java type: com.noosh.nooshapi.vo.ShipmentDetailVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ShipmentDetailVO {
  public static final String SERIALIZED_NAME_LOCATIONS = "locations";
  @SerializedName(SERIALIZED_NAME_LOCATIONS)
  private List<ShipmentRequestBaseVO> locations = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOCATIONS_COUNT = "locations_count";
  @SerializedName(SERIALIZED_NAME_LOCATIONS_COUNT)
  private Long locationsCount;

  public static final String SERIALIZED_NAME_QTY_RECEIVED = "qty_received";
  @SerializedName(SERIALIZED_NAME_QTY_RECEIVED)
  private Long qtyReceived;

  public static final String SERIALIZED_NAME_QTY_REQUESTED = "qty_requested";
  @SerializedName(SERIALIZED_NAME_QTY_REQUESTED)
  private Long qtyRequested;

  public static final String SERIALIZED_NAME_QTY_SHIPPED = "qty_shipped";
  @SerializedName(SERIALIZED_NAME_QTY_SHIPPED)
  private Long qtyShipped;

  public static final String SERIALIZED_NAME_RECEIVED_DATE = "received_date";
  @SerializedName(SERIALIZED_NAME_RECEIVED_DATE)
  private LocalDate receivedDate;

  public static final String SERIALIZED_NAME_SHIPMENT_ID = "shipment_id";
  @SerializedName(SERIALIZED_NAME_SHIPMENT_ID)
  private Long shipmentId;

  public static final String SERIALIZED_NAME_SHIPMENT_STATUS = "shipment_status";
  @SerializedName(SERIALIZED_NAME_SHIPMENT_STATUS)
  private String shipmentStatus;

  public static final String SERIALIZED_NAME_SHIPPED_DATE = "shipped_date";
  @SerializedName(SERIALIZED_NAME_SHIPPED_DATE)
  private LocalDate shippedDate;

  public static final String SERIALIZED_NAME_SPEC = "spec";
  @SerializedName(SERIALIZED_NAME_SPEC)
  private SpecBaseVO spec;

  public ShipmentDetailVO() {
  }

  public ShipmentDetailVO locations(List<ShipmentRequestBaseVO> locations) {
    this.locations = locations;
    return this;
  }

  public ShipmentDetailVO addLocationsItem(ShipmentRequestBaseVO locationsItem) {
    if (this.locations == null) {
      this.locations = new ArrayList<>();
    }
    this.locations.add(locationsItem);
    return this;
  }

  /**
   * 
   * @return locations
   */
  @javax.annotation.Nullable
  public List<ShipmentRequestBaseVO> getLocations() {
    return locations;
  }

  public void setLocations(List<ShipmentRequestBaseVO> locations) {
    this.locations = locations;
  }


  public ShipmentDetailVO locationsCount(Long locationsCount) {
    this.locationsCount = locationsCount;
    return this;
  }

  /**
   * 
   * @return locationsCount
   */
  @javax.annotation.Nullable
  public Long getLocationsCount() {
    return locationsCount;
  }

  public void setLocationsCount(Long locationsCount) {
    this.locationsCount = locationsCount;
  }


  public ShipmentDetailVO qtyReceived(Long qtyReceived) {
    this.qtyReceived = qtyReceived;
    return this;
  }

  /**
   * 
   * @return qtyReceived
   */
  @javax.annotation.Nullable
  public Long getQtyReceived() {
    return qtyReceived;
  }

  public void setQtyReceived(Long qtyReceived) {
    this.qtyReceived = qtyReceived;
  }


  public ShipmentDetailVO qtyRequested(Long qtyRequested) {
    this.qtyRequested = qtyRequested;
    return this;
  }

  /**
   * 
   * @return qtyRequested
   */
  @javax.annotation.Nullable
  public Long getQtyRequested() {
    return qtyRequested;
  }

  public void setQtyRequested(Long qtyRequested) {
    this.qtyRequested = qtyRequested;
  }


  public ShipmentDetailVO qtyShipped(Long qtyShipped) {
    this.qtyShipped = qtyShipped;
    return this;
  }

  /**
   * 
   * @return qtyShipped
   */
  @javax.annotation.Nullable
  public Long getQtyShipped() {
    return qtyShipped;
  }

  public void setQtyShipped(Long qtyShipped) {
    this.qtyShipped = qtyShipped;
  }


  public ShipmentDetailVO receivedDate(LocalDate receivedDate) {
    this.receivedDate = receivedDate;
    return this;
  }

  /**
   * 
   * @return receivedDate
   */
  @javax.annotation.Nullable
  public LocalDate getReceivedDate() {
    return receivedDate;
  }

  public void setReceivedDate(LocalDate receivedDate) {
    this.receivedDate = receivedDate;
  }


  public ShipmentDetailVO shipmentId(Long shipmentId) {
    this.shipmentId = shipmentId;
    return this;
  }

  /**
   * 
   * @return shipmentId
   */
  @javax.annotation.Nullable
  public Long getShipmentId() {
    return shipmentId;
  }

  public void setShipmentId(Long shipmentId) {
    this.shipmentId = shipmentId;
  }


  public ShipmentDetailVO shipmentStatus(String shipmentStatus) {
    this.shipmentStatus = shipmentStatus;
    return this;
  }

  /**
   * 
   * @return shipmentStatus
   */
  @javax.annotation.Nullable
  public String getShipmentStatus() {
    return shipmentStatus;
  }

  public void setShipmentStatus(String shipmentStatus) {
    this.shipmentStatus = shipmentStatus;
  }


  public ShipmentDetailVO shippedDate(LocalDate shippedDate) {
    this.shippedDate = shippedDate;
    return this;
  }

  /**
   * 
   * @return shippedDate
   */
  @javax.annotation.Nullable
  public LocalDate getShippedDate() {
    return shippedDate;
  }

  public void setShippedDate(LocalDate shippedDate) {
    this.shippedDate = shippedDate;
  }


  public ShipmentDetailVO spec(SpecBaseVO spec) {
    this.spec = spec;
    return this;
  }

  /**
   * Get spec
   * @return spec
   */
  @javax.annotation.Nullable
  public SpecBaseVO getSpec() {
    return spec;
  }

  public void setSpec(SpecBaseVO spec) {
    this.spec = spec;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ShipmentDetailVO shipmentDetailVO = (ShipmentDetailVO) o;
    return Objects.equals(this.locations, shipmentDetailVO.locations) &&
        Objects.equals(this.locationsCount, shipmentDetailVO.locationsCount) &&
        Objects.equals(this.qtyReceived, shipmentDetailVO.qtyReceived) &&
        Objects.equals(this.qtyRequested, shipmentDetailVO.qtyRequested) &&
        Objects.equals(this.qtyShipped, shipmentDetailVO.qtyShipped) &&
        Objects.equals(this.receivedDate, shipmentDetailVO.receivedDate) &&
        Objects.equals(this.shipmentId, shipmentDetailVO.shipmentId) &&
        Objects.equals(this.shipmentStatus, shipmentDetailVO.shipmentStatus) &&
        Objects.equals(this.shippedDate, shipmentDetailVO.shippedDate) &&
        Objects.equals(this.spec, shipmentDetailVO.spec);
  }

  @Override
  public int hashCode() {
    return Objects.hash(locations, locationsCount, qtyReceived, qtyRequested, qtyShipped, receivedDate, shipmentId, shipmentStatus, shippedDate, spec);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ShipmentDetailVO {\n");
    sb.append("    locations: ").append(toIndentedString(locations)).append("\n");
    sb.append("    locationsCount: ").append(toIndentedString(locationsCount)).append("\n");
    sb.append("    qtyReceived: ").append(toIndentedString(qtyReceived)).append("\n");
    sb.append("    qtyRequested: ").append(toIndentedString(qtyRequested)).append("\n");
    sb.append("    qtyShipped: ").append(toIndentedString(qtyShipped)).append("\n");
    sb.append("    receivedDate: ").append(toIndentedString(receivedDate)).append("\n");
    sb.append("    shipmentId: ").append(toIndentedString(shipmentId)).append("\n");
    sb.append("    shipmentStatus: ").append(toIndentedString(shipmentStatus)).append("\n");
    sb.append("    shippedDate: ").append(toIndentedString(shippedDate)).append("\n");
    sb.append("    spec: ").append(toIndentedString(spec)).append("\n");
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
    openapiFields.add("locations");
    openapiFields.add("locations_count");
    openapiFields.add("qty_received");
    openapiFields.add("qty_requested");
    openapiFields.add("qty_shipped");
    openapiFields.add("received_date");
    openapiFields.add("shipment_id");
    openapiFields.add("shipment_status");
    openapiFields.add("shipped_date");
    openapiFields.add("spec");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ShipmentDetailVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ShipmentDetailVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ShipmentDetailVO is not found in the empty JSON string", ShipmentDetailVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ShipmentDetailVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ShipmentDetailVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("locations") != null && !jsonObj.get("locations").isJsonNull()) {
        JsonArray jsonArraylocations = jsonObj.getAsJsonArray("locations");
        if (jsonArraylocations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("locations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `locations` to be an array in the JSON string but got `%s`", jsonObj.get("locations").toString()));
          }

          // validate the optional field `locations` (array)
          for (int i = 0; i < jsonArraylocations.size(); i++) {
            ShipmentRequestBaseVO.validateJsonElement(jsonArraylocations.get(i));
          };
        }
      }
      if ((jsonObj.get("shipment_status") != null && !jsonObj.get("shipment_status").isJsonNull()) && !jsonObj.get("shipment_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipment_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipment_status").toString()));
      }
      // validate the optional field `spec`
      if (jsonObj.get("spec") != null && !jsonObj.get("spec").isJsonNull()) {
        SpecBaseVO.validateJsonElement(jsonObj.get("spec"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ShipmentDetailVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ShipmentDetailVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ShipmentDetailVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ShipmentDetailVO.class));

       return (TypeAdapter<T>) new TypeAdapter<ShipmentDetailVO>() {
           @Override
           public void write(JsonWriter out, ShipmentDetailVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ShipmentDetailVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ShipmentDetailVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ShipmentDetailVO
   * @throws IOException if the JSON string is invalid with respect to ShipmentDetailVO
   */
  public static ShipmentDetailVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ShipmentDetailVO.class);
  }

  /**
   * Convert an instance of ShipmentDetailVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

