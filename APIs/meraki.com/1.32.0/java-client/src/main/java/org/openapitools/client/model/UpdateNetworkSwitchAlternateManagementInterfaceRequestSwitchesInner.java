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
 * UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner {
  public static final String SERIALIZED_NAME_ALTERNATE_MANAGEMENT_IP = "alternateManagementIp";
  @SerializedName(SERIALIZED_NAME_ALTERNATE_MANAGEMENT_IP)
  private String alternateManagementIp;

  public static final String SERIALIZED_NAME_GATEWAY = "gateway";
  @SerializedName(SERIALIZED_NAME_GATEWAY)
  private String gateway;

  public static final String SERIALIZED_NAME_SERIAL = "serial";
  @SerializedName(SERIALIZED_NAME_SERIAL)
  private String serial;

  public static final String SERIALIZED_NAME_SUBNET_MASK = "subnetMask";
  @SerializedName(SERIALIZED_NAME_SUBNET_MASK)
  private String subnetMask;

  public UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner() {
  }

  public UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner alternateManagementIp(String alternateManagementIp) {
    this.alternateManagementIp = alternateManagementIp;
    return this;
  }

  /**
   * Switch alternative management IP. To remove a prior IP setting, provide an empty string
   * @return alternateManagementIp
   */
  @javax.annotation.Nonnull
  public String getAlternateManagementIp() {
    return alternateManagementIp;
  }

  public void setAlternateManagementIp(String alternateManagementIp) {
    this.alternateManagementIp = alternateManagementIp;
  }


  public UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner gateway(String gateway) {
    this.gateway = gateway;
    return this;
  }

  /**
   * Switch gateway must be in IP format. Only and must be specified for Polaris switches
   * @return gateway
   */
  @javax.annotation.Nullable
  public String getGateway() {
    return gateway;
  }

  public void setGateway(String gateway) {
    this.gateway = gateway;
  }


  public UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner serial(String serial) {
    this.serial = serial;
    return this;
  }

  /**
   * Switch serial number
   * @return serial
   */
  @javax.annotation.Nonnull
  public String getSerial() {
    return serial;
  }

  public void setSerial(String serial) {
    this.serial = serial;
  }


  public UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner subnetMask(String subnetMask) {
    this.subnetMask = subnetMask;
    return this;
  }

  /**
   * Switch subnet mask must be in IP format. Only and must be specified for Polaris switches
   * @return subnetMask
   */
  @javax.annotation.Nullable
  public String getSubnetMask() {
    return subnetMask;
  }

  public void setSubnetMask(String subnetMask) {
    this.subnetMask = subnetMask;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner updateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner = (UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner) o;
    return Objects.equals(this.alternateManagementIp, updateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.alternateManagementIp) &&
        Objects.equals(this.gateway, updateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.gateway) &&
        Objects.equals(this.serial, updateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.serial) &&
        Objects.equals(this.subnetMask, updateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.subnetMask);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alternateManagementIp, gateway, serial, subnetMask);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner {\n");
    sb.append("    alternateManagementIp: ").append(toIndentedString(alternateManagementIp)).append("\n");
    sb.append("    gateway: ").append(toIndentedString(gateway)).append("\n");
    sb.append("    serial: ").append(toIndentedString(serial)).append("\n");
    sb.append("    subnetMask: ").append(toIndentedString(subnetMask)).append("\n");
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
    openapiFields.add("alternateManagementIp");
    openapiFields.add("gateway");
    openapiFields.add("serial");
    openapiFields.add("subnetMask");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("alternateManagementIp");
    openapiRequiredFields.add("serial");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner is not found in the empty JSON string", UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("alternateManagementIp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alternateManagementIp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alternateManagementIp").toString()));
      }
      if ((jsonObj.get("gateway") != null && !jsonObj.get("gateway").isJsonNull()) && !jsonObj.get("gateway").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gateway` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gateway").toString()));
      }
      if (!jsonObj.get("serial").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serial` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serial").toString()));
      }
      if ((jsonObj.get("subnetMask") != null && !jsonObj.get("subnetMask").isJsonNull()) && !jsonObj.get("subnetMask").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subnetMask` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subnetMask").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner
   */
  public static UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.class);
  }

  /**
   * Convert an instance of UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

