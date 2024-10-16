/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
import org.openapitools.client.model.GetNetworkAlertsHistory200ResponseInnerDestinations;
import org.openapitools.client.model.GetNetworkAlertsHistory200ResponseInnerDevice;

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
 * GetNetworkAlertsHistory200ResponseInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkAlertsHistory200ResponseInner {
  public static final String SERIALIZED_NAME_ALERT_DATA = "alertData";
  @SerializedName(SERIALIZED_NAME_ALERT_DATA)
  private Object alertData;

  public static final String SERIALIZED_NAME_ALERT_TYPE = "alertType";
  @SerializedName(SERIALIZED_NAME_ALERT_TYPE)
  private String alertType;

  public static final String SERIALIZED_NAME_ALERT_TYPE_ID = "alertTypeId";
  @SerializedName(SERIALIZED_NAME_ALERT_TYPE_ID)
  private String alertTypeId;

  public static final String SERIALIZED_NAME_DESTINATIONS = "destinations";
  @SerializedName(SERIALIZED_NAME_DESTINATIONS)
  private GetNetworkAlertsHistory200ResponseInnerDestinations destinations;

  public static final String SERIALIZED_NAME_DEVICE = "device";
  @SerializedName(SERIALIZED_NAME_DEVICE)
  private GetNetworkAlertsHistory200ResponseInnerDevice device;

  public static final String SERIALIZED_NAME_OCCURRED_AT = "occurredAt";
  @SerializedName(SERIALIZED_NAME_OCCURRED_AT)
  private String occurredAt;

  public GetNetworkAlertsHistory200ResponseInner() {
  }

  public GetNetworkAlertsHistory200ResponseInner alertData(Object alertData) {
    this.alertData = alertData;
    return this;
  }

  /**
   * relevant data about the event that caused the alert
   * @return alertData
   */
  @javax.annotation.Nullable
  public Object getAlertData() {
    return alertData;
  }

  public void setAlertData(Object alertData) {
    this.alertData = alertData;
  }


  public GetNetworkAlertsHistory200ResponseInner alertType(String alertType) {
    this.alertType = alertType;
    return this;
  }

  /**
   * user friendly alert type
   * @return alertType
   */
  @javax.annotation.Nullable
  public String getAlertType() {
    return alertType;
  }

  public void setAlertType(String alertType) {
    this.alertType = alertType;
  }


  public GetNetworkAlertsHistory200ResponseInner alertTypeId(String alertTypeId) {
    this.alertTypeId = alertTypeId;
    return this;
  }

  /**
   * type of alert
   * @return alertTypeId
   */
  @javax.annotation.Nullable
  public String getAlertTypeId() {
    return alertTypeId;
  }

  public void setAlertTypeId(String alertTypeId) {
    this.alertTypeId = alertTypeId;
  }


  public GetNetworkAlertsHistory200ResponseInner destinations(GetNetworkAlertsHistory200ResponseInnerDestinations destinations) {
    this.destinations = destinations;
    return this;
  }

  /**
   * Get destinations
   * @return destinations
   */
  @javax.annotation.Nullable
  public GetNetworkAlertsHistory200ResponseInnerDestinations getDestinations() {
    return destinations;
  }

  public void setDestinations(GetNetworkAlertsHistory200ResponseInnerDestinations destinations) {
    this.destinations = destinations;
  }


  public GetNetworkAlertsHistory200ResponseInner device(GetNetworkAlertsHistory200ResponseInnerDevice device) {
    this.device = device;
    return this;
  }

  /**
   * Get device
   * @return device
   */
  @javax.annotation.Nullable
  public GetNetworkAlertsHistory200ResponseInnerDevice getDevice() {
    return device;
  }

  public void setDevice(GetNetworkAlertsHistory200ResponseInnerDevice device) {
    this.device = device;
  }


  public GetNetworkAlertsHistory200ResponseInner occurredAt(String occurredAt) {
    this.occurredAt = occurredAt;
    return this;
  }

  /**
   * time when the event occurred
   * @return occurredAt
   */
  @javax.annotation.Nullable
  public String getOccurredAt() {
    return occurredAt;
  }

  public void setOccurredAt(String occurredAt) {
    this.occurredAt = occurredAt;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkAlertsHistory200ResponseInner getNetworkAlertsHistory200ResponseInner = (GetNetworkAlertsHistory200ResponseInner) o;
    return Objects.equals(this.alertData, getNetworkAlertsHistory200ResponseInner.alertData) &&
        Objects.equals(this.alertType, getNetworkAlertsHistory200ResponseInner.alertType) &&
        Objects.equals(this.alertTypeId, getNetworkAlertsHistory200ResponseInner.alertTypeId) &&
        Objects.equals(this.destinations, getNetworkAlertsHistory200ResponseInner.destinations) &&
        Objects.equals(this.device, getNetworkAlertsHistory200ResponseInner.device) &&
        Objects.equals(this.occurredAt, getNetworkAlertsHistory200ResponseInner.occurredAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alertData, alertType, alertTypeId, destinations, device, occurredAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkAlertsHistory200ResponseInner {\n");
    sb.append("    alertData: ").append(toIndentedString(alertData)).append("\n");
    sb.append("    alertType: ").append(toIndentedString(alertType)).append("\n");
    sb.append("    alertTypeId: ").append(toIndentedString(alertTypeId)).append("\n");
    sb.append("    destinations: ").append(toIndentedString(destinations)).append("\n");
    sb.append("    device: ").append(toIndentedString(device)).append("\n");
    sb.append("    occurredAt: ").append(toIndentedString(occurredAt)).append("\n");
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
    openapiFields.add("alertData");
    openapiFields.add("alertType");
    openapiFields.add("alertTypeId");
    openapiFields.add("destinations");
    openapiFields.add("device");
    openapiFields.add("occurredAt");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkAlertsHistory200ResponseInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkAlertsHistory200ResponseInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkAlertsHistory200ResponseInner is not found in the empty JSON string", GetNetworkAlertsHistory200ResponseInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkAlertsHistory200ResponseInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkAlertsHistory200ResponseInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("alertType") != null && !jsonObj.get("alertType").isJsonNull()) && !jsonObj.get("alertType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alertType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alertType").toString()));
      }
      if ((jsonObj.get("alertTypeId") != null && !jsonObj.get("alertTypeId").isJsonNull()) && !jsonObj.get("alertTypeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alertTypeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alertTypeId").toString()));
      }
      // validate the optional field `destinations`
      if (jsonObj.get("destinations") != null && !jsonObj.get("destinations").isJsonNull()) {
        GetNetworkAlertsHistory200ResponseInnerDestinations.validateJsonElement(jsonObj.get("destinations"));
      }
      // validate the optional field `device`
      if (jsonObj.get("device") != null && !jsonObj.get("device").isJsonNull()) {
        GetNetworkAlertsHistory200ResponseInnerDevice.validateJsonElement(jsonObj.get("device"));
      }
      if ((jsonObj.get("occurredAt") != null && !jsonObj.get("occurredAt").isJsonNull()) && !jsonObj.get("occurredAt").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `occurredAt` to be a primitive type in the JSON string but got `%s`", jsonObj.get("occurredAt").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkAlertsHistory200ResponseInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkAlertsHistory200ResponseInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkAlertsHistory200ResponseInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkAlertsHistory200ResponseInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkAlertsHistory200ResponseInner>() {
           @Override
           public void write(JsonWriter out, GetNetworkAlertsHistory200ResponseInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkAlertsHistory200ResponseInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkAlertsHistory200ResponseInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkAlertsHistory200ResponseInner
   * @throws IOException if the JSON string is invalid with respect to GetNetworkAlertsHistory200ResponseInner
   */
  public static GetNetworkAlertsHistory200ResponseInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkAlertsHistory200ResponseInner.class);
  }

  /**
   * Convert an instance of GetNetworkAlertsHistory200ResponseInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

