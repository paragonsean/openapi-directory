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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion;
import org.openapitools.client.model.GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion;

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
 * Details of the last firmware upgrade on the device
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade {
  public static final String SERIALIZED_NAME_FROM_VERSION = "fromVersion";
  @SerializedName(SERIALIZED_NAME_FROM_VERSION)
  private GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion fromVersion;

  public static final String SERIALIZED_NAME_TIME = "time";
  @SerializedName(SERIALIZED_NAME_TIME)
  private OffsetDateTime time;

  public static final String SERIALIZED_NAME_TO_VERSION = "toVersion";
  @SerializedName(SERIALIZED_NAME_TO_VERSION)
  private GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion toVersion;

  public GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade() {
  }

  public GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade fromVersion(GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion fromVersion) {
    this.fromVersion = fromVersion;
    return this;
  }

  /**
   * Get fromVersion
   * @return fromVersion
   */
  @javax.annotation.Nullable
  public GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion getFromVersion() {
    return fromVersion;
  }

  public void setFromVersion(GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion fromVersion) {
    this.fromVersion = fromVersion;
  }


  public GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade time(OffsetDateTime time) {
    this.time = time;
    return this;
  }

  /**
   * Timestamp of the last successful firmware upgrade
   * @return time
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTime() {
    return time;
  }

  public void setTime(OffsetDateTime time) {
    this.time = time;
  }


  public GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade toVersion(GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion toVersion) {
    this.toVersion = toVersion;
    return this;
  }

  /**
   * Get toVersion
   * @return toVersion
   */
  @javax.annotation.Nullable
  public GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion getToVersion() {
    return toVersion;
  }

  public void setToVersion(GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion toVersion) {
    this.toVersion = toVersion;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade getNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade = (GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade) o;
    return Objects.equals(this.fromVersion, getNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.fromVersion) &&
        Objects.equals(this.time, getNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.time) &&
        Objects.equals(this.toVersion, getNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.toVersion);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fromVersion, time, toVersion);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade {\n");
    sb.append("    fromVersion: ").append(toIndentedString(fromVersion)).append("\n");
    sb.append("    time: ").append(toIndentedString(time)).append("\n");
    sb.append("    toVersion: ").append(toIndentedString(toVersion)).append("\n");
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
    openapiFields.add("fromVersion");
    openapiFields.add("time");
    openapiFields.add("toVersion");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade is not found in the empty JSON string", GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `fromVersion`
      if (jsonObj.get("fromVersion") != null && !jsonObj.get("fromVersion").isJsonNull()) {
        GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeFromVersion.validateJsonElement(jsonObj.get("fromVersion"));
      }
      // validate the optional field `toVersion`
      if (jsonObj.get("toVersion") != null && !jsonObj.get("toVersion").isJsonNull()) {
        GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgradeToVersion.validateJsonElement(jsonObj.get("toVersion"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade>() {
           @Override
           public void write(JsonWriter out, GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade
   * @throws IOException if the JSON string is invalid with respect to GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade
   */
  public static GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade.class);
  }

  /**
   * Convert an instance of GetNetworkFirmwareUpgrades200ResponseProductsApplianceLastUpgrade to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

