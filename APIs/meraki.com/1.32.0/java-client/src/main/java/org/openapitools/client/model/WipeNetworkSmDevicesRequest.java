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
 * WipeNetworkSmDevicesRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WipeNetworkSmDevicesRequest {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_PIN = "pin";
  @SerializedName(SERIALIZED_NAME_PIN)
  private Integer pin;

  public static final String SERIALIZED_NAME_SERIAL = "serial";
  @SerializedName(SERIALIZED_NAME_SERIAL)
  private String serial;

  public static final String SERIALIZED_NAME_WIFI_MAC = "wifiMac";
  @SerializedName(SERIALIZED_NAME_WIFI_MAC)
  private String wifiMac;

  public WipeNetworkSmDevicesRequest() {
  }

  public WipeNetworkSmDevicesRequest id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The id of the device to be wiped.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public WipeNetworkSmDevicesRequest pin(Integer pin) {
    this.pin = pin;
    return this;
  }

  /**
   * The pin number (a six digit value) for wiping a macOS device. Required only for macOS devices.
   * @return pin
   */
  @javax.annotation.Nullable
  public Integer getPin() {
    return pin;
  }

  public void setPin(Integer pin) {
    this.pin = pin;
  }


  public WipeNetworkSmDevicesRequest serial(String serial) {
    this.serial = serial;
    return this;
  }

  /**
   * The serial of the device to be wiped.
   * @return serial
   */
  @javax.annotation.Nullable
  public String getSerial() {
    return serial;
  }

  public void setSerial(String serial) {
    this.serial = serial;
  }


  public WipeNetworkSmDevicesRequest wifiMac(String wifiMac) {
    this.wifiMac = wifiMac;
    return this;
  }

  /**
   * The wifiMac of the device to be wiped.
   * @return wifiMac
   */
  @javax.annotation.Nullable
  public String getWifiMac() {
    return wifiMac;
  }

  public void setWifiMac(String wifiMac) {
    this.wifiMac = wifiMac;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WipeNetworkSmDevicesRequest wipeNetworkSmDevicesRequest = (WipeNetworkSmDevicesRequest) o;
    return Objects.equals(this.id, wipeNetworkSmDevicesRequest.id) &&
        Objects.equals(this.pin, wipeNetworkSmDevicesRequest.pin) &&
        Objects.equals(this.serial, wipeNetworkSmDevicesRequest.serial) &&
        Objects.equals(this.wifiMac, wipeNetworkSmDevicesRequest.wifiMac);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, pin, serial, wifiMac);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WipeNetworkSmDevicesRequest {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    pin: ").append(toIndentedString(pin)).append("\n");
    sb.append("    serial: ").append(toIndentedString(serial)).append("\n");
    sb.append("    wifiMac: ").append(toIndentedString(wifiMac)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("pin");
    openapiFields.add("serial");
    openapiFields.add("wifiMac");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WipeNetworkSmDevicesRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WipeNetworkSmDevicesRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WipeNetworkSmDevicesRequest is not found in the empty JSON string", WipeNetworkSmDevicesRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WipeNetworkSmDevicesRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WipeNetworkSmDevicesRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("serial") != null && !jsonObj.get("serial").isJsonNull()) && !jsonObj.get("serial").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `serial` to be a primitive type in the JSON string but got `%s`", jsonObj.get("serial").toString()));
      }
      if ((jsonObj.get("wifiMac") != null && !jsonObj.get("wifiMac").isJsonNull()) && !jsonObj.get("wifiMac").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `wifiMac` to be a primitive type in the JSON string but got `%s`", jsonObj.get("wifiMac").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WipeNetworkSmDevicesRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WipeNetworkSmDevicesRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WipeNetworkSmDevicesRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WipeNetworkSmDevicesRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<WipeNetworkSmDevicesRequest>() {
           @Override
           public void write(JsonWriter out, WipeNetworkSmDevicesRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WipeNetworkSmDevicesRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WipeNetworkSmDevicesRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WipeNetworkSmDevicesRequest
   * @throws IOException if the JSON string is invalid with respect to WipeNetworkSmDevicesRequest
   */
  public static WipeNetworkSmDevicesRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WipeNetworkSmDevicesRequest.class);
  }

  /**
   * Convert an instance of WipeNetworkSmDevicesRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

