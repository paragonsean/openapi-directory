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
 * GetNetworkWirelessBluetoothSettings200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkWirelessBluetoothSettings200Response {
  public static final String SERIALIZED_NAME_ADVERTISING_ENABLED = "advertisingEnabled";
  @SerializedName(SERIALIZED_NAME_ADVERTISING_ENABLED)
  private Boolean advertisingEnabled;

  public static final String SERIALIZED_NAME_ESL_ENABLED = "eslEnabled";
  @SerializedName(SERIALIZED_NAME_ESL_ENABLED)
  private Boolean eslEnabled;

  public static final String SERIALIZED_NAME_MAJOR = "major";
  @SerializedName(SERIALIZED_NAME_MAJOR)
  private Integer major;

  public static final String SERIALIZED_NAME_MAJOR_MINOR_ASSIGNMENT_MODE = "majorMinorAssignmentMode";
  @SerializedName(SERIALIZED_NAME_MAJOR_MINOR_ASSIGNMENT_MODE)
  private String majorMinorAssignmentMode;

  public static final String SERIALIZED_NAME_MINOR = "minor";
  @SerializedName(SERIALIZED_NAME_MINOR)
  private Integer minor;

  public static final String SERIALIZED_NAME_SCANNING_ENABLED = "scanningEnabled";
  @SerializedName(SERIALIZED_NAME_SCANNING_ENABLED)
  private Boolean scanningEnabled;

  public static final String SERIALIZED_NAME_UUID = "uuid";
  @SerializedName(SERIALIZED_NAME_UUID)
  private String uuid;

  public GetNetworkWirelessBluetoothSettings200Response() {
  }

  public GetNetworkWirelessBluetoothSettings200Response advertisingEnabled(Boolean advertisingEnabled) {
    this.advertisingEnabled = advertisingEnabled;
    return this;
  }

  /**
   * Whether APs will advertise beacons.
   * @return advertisingEnabled
   */
  @javax.annotation.Nullable
  public Boolean getAdvertisingEnabled() {
    return advertisingEnabled;
  }

  public void setAdvertisingEnabled(Boolean advertisingEnabled) {
    this.advertisingEnabled = advertisingEnabled;
  }


  public GetNetworkWirelessBluetoothSettings200Response eslEnabled(Boolean eslEnabled) {
    this.eslEnabled = eslEnabled;
    return this;
  }

  /**
   * Whether ESL is enabled on this network.
   * @return eslEnabled
   */
  @javax.annotation.Nullable
  public Boolean getEslEnabled() {
    return eslEnabled;
  }

  public void setEslEnabled(Boolean eslEnabled) {
    this.eslEnabled = eslEnabled;
  }


  public GetNetworkWirelessBluetoothSettings200Response major(Integer major) {
    this.major = major;
    return this;
  }

  /**
   * The major number to be used in the beacon identifier. Only valid in &#39;Non-unique&#39; mode.
   * @return major
   */
  @javax.annotation.Nullable
  public Integer getMajor() {
    return major;
  }

  public void setMajor(Integer major) {
    this.major = major;
  }


  public GetNetworkWirelessBluetoothSettings200Response majorMinorAssignmentMode(String majorMinorAssignmentMode) {
    this.majorMinorAssignmentMode = majorMinorAssignmentMode;
    return this;
  }

  /**
   * The way major and minor number should be assigned to nodes in the network. (&#39;Unique&#39;, &#39;Non-unique&#39;)
   * @return majorMinorAssignmentMode
   */
  @javax.annotation.Nullable
  public String getMajorMinorAssignmentMode() {
    return majorMinorAssignmentMode;
  }

  public void setMajorMinorAssignmentMode(String majorMinorAssignmentMode) {
    this.majorMinorAssignmentMode = majorMinorAssignmentMode;
  }


  public GetNetworkWirelessBluetoothSettings200Response minor(Integer minor) {
    this.minor = minor;
    return this;
  }

  /**
   * The minor number to be used in the beacon identifier. Only valid in &#39;Non-unique&#39; mode.
   * @return minor
   */
  @javax.annotation.Nullable
  public Integer getMinor() {
    return minor;
  }

  public void setMinor(Integer minor) {
    this.minor = minor;
  }


  public GetNetworkWirelessBluetoothSettings200Response scanningEnabled(Boolean scanningEnabled) {
    this.scanningEnabled = scanningEnabled;
    return this;
  }

  /**
   * Whether APs will scan for Bluetooth enabled clients.
   * @return scanningEnabled
   */
  @javax.annotation.Nullable
  public Boolean getScanningEnabled() {
    return scanningEnabled;
  }

  public void setScanningEnabled(Boolean scanningEnabled) {
    this.scanningEnabled = scanningEnabled;
  }


  public GetNetworkWirelessBluetoothSettings200Response uuid(String uuid) {
    this.uuid = uuid;
    return this;
  }

  /**
   * The UUID to be used in the beacon identifier.
   * @return uuid
   */
  @javax.annotation.Nullable
  public String getUuid() {
    return uuid;
  }

  public void setUuid(String uuid) {
    this.uuid = uuid;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkWirelessBluetoothSettings200Response getNetworkWirelessBluetoothSettings200Response = (GetNetworkWirelessBluetoothSettings200Response) o;
    return Objects.equals(this.advertisingEnabled, getNetworkWirelessBluetoothSettings200Response.advertisingEnabled) &&
        Objects.equals(this.eslEnabled, getNetworkWirelessBluetoothSettings200Response.eslEnabled) &&
        Objects.equals(this.major, getNetworkWirelessBluetoothSettings200Response.major) &&
        Objects.equals(this.majorMinorAssignmentMode, getNetworkWirelessBluetoothSettings200Response.majorMinorAssignmentMode) &&
        Objects.equals(this.minor, getNetworkWirelessBluetoothSettings200Response.minor) &&
        Objects.equals(this.scanningEnabled, getNetworkWirelessBluetoothSettings200Response.scanningEnabled) &&
        Objects.equals(this.uuid, getNetworkWirelessBluetoothSettings200Response.uuid);
  }

  @Override
  public int hashCode() {
    return Objects.hash(advertisingEnabled, eslEnabled, major, majorMinorAssignmentMode, minor, scanningEnabled, uuid);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkWirelessBluetoothSettings200Response {\n");
    sb.append("    advertisingEnabled: ").append(toIndentedString(advertisingEnabled)).append("\n");
    sb.append("    eslEnabled: ").append(toIndentedString(eslEnabled)).append("\n");
    sb.append("    major: ").append(toIndentedString(major)).append("\n");
    sb.append("    majorMinorAssignmentMode: ").append(toIndentedString(majorMinorAssignmentMode)).append("\n");
    sb.append("    minor: ").append(toIndentedString(minor)).append("\n");
    sb.append("    scanningEnabled: ").append(toIndentedString(scanningEnabled)).append("\n");
    sb.append("    uuid: ").append(toIndentedString(uuid)).append("\n");
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
    openapiFields.add("advertisingEnabled");
    openapiFields.add("eslEnabled");
    openapiFields.add("major");
    openapiFields.add("majorMinorAssignmentMode");
    openapiFields.add("minor");
    openapiFields.add("scanningEnabled");
    openapiFields.add("uuid");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkWirelessBluetoothSettings200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkWirelessBluetoothSettings200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkWirelessBluetoothSettings200Response is not found in the empty JSON string", GetNetworkWirelessBluetoothSettings200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkWirelessBluetoothSettings200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkWirelessBluetoothSettings200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("majorMinorAssignmentMode") != null && !jsonObj.get("majorMinorAssignmentMode").isJsonNull()) && !jsonObj.get("majorMinorAssignmentMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `majorMinorAssignmentMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("majorMinorAssignmentMode").toString()));
      }
      if ((jsonObj.get("uuid") != null && !jsonObj.get("uuid").isJsonNull()) && !jsonObj.get("uuid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uuid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uuid").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkWirelessBluetoothSettings200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkWirelessBluetoothSettings200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkWirelessBluetoothSettings200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkWirelessBluetoothSettings200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkWirelessBluetoothSettings200Response>() {
           @Override
           public void write(JsonWriter out, GetNetworkWirelessBluetoothSettings200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkWirelessBluetoothSettings200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkWirelessBluetoothSettings200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkWirelessBluetoothSettings200Response
   * @throws IOException if the JSON string is invalid with respect to GetNetworkWirelessBluetoothSettings200Response
   */
  public static GetNetworkWirelessBluetoothSettings200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkWirelessBluetoothSettings200Response.class);
  }

  /**
   * Convert an instance of GetNetworkWirelessBluetoothSettings200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

