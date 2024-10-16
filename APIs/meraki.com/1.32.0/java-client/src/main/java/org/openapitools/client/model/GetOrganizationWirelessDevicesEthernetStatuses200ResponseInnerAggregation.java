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
 * Aggregation details object
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation {
  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_SPEED = "speed";
  @SerializedName(SERIALIZED_NAME_SPEED)
  private Integer speed;

  public GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation() {
  }

  public GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Link Aggregation enabled flag
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation speed(Integer speed) {
    this.speed = speed;
    return this;
  }

  /**
   * Link Aggregation speed
   * @return speed
   */
  @javax.annotation.Nullable
  public Integer getSpeed() {
    return speed;
  }

  public void setSpeed(Integer speed) {
    this.speed = speed;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation getOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation = (GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation) o;
    return Objects.equals(this.enabled, getOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.enabled) &&
        Objects.equals(this.speed, getOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.speed);
  }

  @Override
  public int hashCode() {
    return Objects.hash(enabled, speed);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation {\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    speed: ").append(toIndentedString(speed)).append("\n");
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
    openapiFields.add("enabled");
    openapiFields.add("speed");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation is not found in the empty JSON string", GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation>() {
           @Override
           public void write(JsonWriter out, GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation
   */
  public static GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation.class);
  }

  /**
   * Convert an instance of GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerAggregation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

