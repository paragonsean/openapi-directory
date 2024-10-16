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
 * Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings {
  public static final String SERIALIZED_NAME_FLOOD_UNKNOWN_MULTICAST_TRAFFIC_ENABLED = "floodUnknownMulticastTrafficEnabled";
  @SerializedName(SERIALIZED_NAME_FLOOD_UNKNOWN_MULTICAST_TRAFFIC_ENABLED)
  private Boolean floodUnknownMulticastTrafficEnabled;

  public static final String SERIALIZED_NAME_IGMP_SNOOPING_ENABLED = "igmpSnoopingEnabled";
  @SerializedName(SERIALIZED_NAME_IGMP_SNOOPING_ENABLED)
  private Boolean igmpSnoopingEnabled;

  public UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings() {
  }

  public UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings floodUnknownMulticastTrafficEnabled(Boolean floodUnknownMulticastTrafficEnabled) {
    this.floodUnknownMulticastTrafficEnabled = floodUnknownMulticastTrafficEnabled;
    return this;
  }

  /**
   * Flood unknown multicast traffic setting for entire network
   * @return floodUnknownMulticastTrafficEnabled
   */
  @javax.annotation.Nullable
  public Boolean getFloodUnknownMulticastTrafficEnabled() {
    return floodUnknownMulticastTrafficEnabled;
  }

  public void setFloodUnknownMulticastTrafficEnabled(Boolean floodUnknownMulticastTrafficEnabled) {
    this.floodUnknownMulticastTrafficEnabled = floodUnknownMulticastTrafficEnabled;
  }


  public UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings igmpSnoopingEnabled(Boolean igmpSnoopingEnabled) {
    this.igmpSnoopingEnabled = igmpSnoopingEnabled;
    return this;
  }

  /**
   * IGMP snooping setting for entire network
   * @return igmpSnoopingEnabled
   */
  @javax.annotation.Nullable
  public Boolean getIgmpSnoopingEnabled() {
    return igmpSnoopingEnabled;
  }

  public void setIgmpSnoopingEnabled(Boolean igmpSnoopingEnabled) {
    this.igmpSnoopingEnabled = igmpSnoopingEnabled;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings updateNetworkSwitchRoutingMulticastRequestDefaultSettings = (UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings) o;
    return Objects.equals(this.floodUnknownMulticastTrafficEnabled, updateNetworkSwitchRoutingMulticastRequestDefaultSettings.floodUnknownMulticastTrafficEnabled) &&
        Objects.equals(this.igmpSnoopingEnabled, updateNetworkSwitchRoutingMulticastRequestDefaultSettings.igmpSnoopingEnabled);
  }

  @Override
  public int hashCode() {
    return Objects.hash(floodUnknownMulticastTrafficEnabled, igmpSnoopingEnabled);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings {\n");
    sb.append("    floodUnknownMulticastTrafficEnabled: ").append(toIndentedString(floodUnknownMulticastTrafficEnabled)).append("\n");
    sb.append("    igmpSnoopingEnabled: ").append(toIndentedString(igmpSnoopingEnabled)).append("\n");
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
    openapiFields.add("floodUnknownMulticastTrafficEnabled");
    openapiFields.add("igmpSnoopingEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings is not found in the empty JSON string", UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings
   */
  public static UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings.class);
  }

  /**
   * Convert an instance of UpdateNetworkSwitchRoutingMulticastRequestDefaultSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

