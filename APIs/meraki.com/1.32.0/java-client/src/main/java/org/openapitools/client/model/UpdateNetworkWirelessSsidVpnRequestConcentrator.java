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
 * The VPN concentrator settings for this SSID.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkWirelessSsidVpnRequestConcentrator {
  public static final String SERIALIZED_NAME_NETWORK_ID = "networkId";
  @SerializedName(SERIALIZED_NAME_NETWORK_ID)
  private String networkId;

  public static final String SERIALIZED_NAME_VLAN_ID = "vlanId";
  @SerializedName(SERIALIZED_NAME_VLAN_ID)
  private Integer vlanId;

  public UpdateNetworkWirelessSsidVpnRequestConcentrator() {
  }

  public UpdateNetworkWirelessSsidVpnRequestConcentrator networkId(String networkId) {
    this.networkId = networkId;
    return this;
  }

  /**
   * The NAT ID of the concentrator that should be set.
   * @return networkId
   */
  @javax.annotation.Nullable
  public String getNetworkId() {
    return networkId;
  }

  public void setNetworkId(String networkId) {
    this.networkId = networkId;
  }


  public UpdateNetworkWirelessSsidVpnRequestConcentrator vlanId(Integer vlanId) {
    this.vlanId = vlanId;
    return this;
  }

  /**
   * The VLAN that should be tagged for the concentrator.
   * @return vlanId
   */
  @javax.annotation.Nullable
  public Integer getVlanId() {
    return vlanId;
  }

  public void setVlanId(Integer vlanId) {
    this.vlanId = vlanId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkWirelessSsidVpnRequestConcentrator updateNetworkWirelessSsidVpnRequestConcentrator = (UpdateNetworkWirelessSsidVpnRequestConcentrator) o;
    return Objects.equals(this.networkId, updateNetworkWirelessSsidVpnRequestConcentrator.networkId) &&
        Objects.equals(this.vlanId, updateNetworkWirelessSsidVpnRequestConcentrator.vlanId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(networkId, vlanId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkWirelessSsidVpnRequestConcentrator {\n");
    sb.append("    networkId: ").append(toIndentedString(networkId)).append("\n");
    sb.append("    vlanId: ").append(toIndentedString(vlanId)).append("\n");
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
    openapiFields.add("networkId");
    openapiFields.add("vlanId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkWirelessSsidVpnRequestConcentrator
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkWirelessSsidVpnRequestConcentrator.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkWirelessSsidVpnRequestConcentrator is not found in the empty JSON string", UpdateNetworkWirelessSsidVpnRequestConcentrator.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkWirelessSsidVpnRequestConcentrator.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkWirelessSsidVpnRequestConcentrator` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("networkId") != null && !jsonObj.get("networkId").isJsonNull()) && !jsonObj.get("networkId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `networkId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("networkId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkWirelessSsidVpnRequestConcentrator.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkWirelessSsidVpnRequestConcentrator' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkWirelessSsidVpnRequestConcentrator> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkWirelessSsidVpnRequestConcentrator.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkWirelessSsidVpnRequestConcentrator>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkWirelessSsidVpnRequestConcentrator value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkWirelessSsidVpnRequestConcentrator read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkWirelessSsidVpnRequestConcentrator given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkWirelessSsidVpnRequestConcentrator
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkWirelessSsidVpnRequestConcentrator
   */
  public static UpdateNetworkWirelessSsidVpnRequestConcentrator fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkWirelessSsidVpnRequestConcentrator.class);
  }

  /**
   * Convert an instance of UpdateNetworkWirelessSsidVpnRequestConcentrator to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

