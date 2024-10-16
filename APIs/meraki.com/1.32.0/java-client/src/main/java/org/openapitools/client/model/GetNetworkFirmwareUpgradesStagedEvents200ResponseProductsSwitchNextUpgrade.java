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
import org.openapitools.client.model.GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgradeToVersion;

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
 * Details of the next firmware upgrade
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade {
  public static final String SERIALIZED_NAME_TO_VERSION = "toVersion";
  @SerializedName(SERIALIZED_NAME_TO_VERSION)
  private GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgradeToVersion toVersion;

  public GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade() {
  }

  public GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade toVersion(GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgradeToVersion toVersion) {
    this.toVersion = toVersion;
    return this;
  }

  /**
   * Get toVersion
   * @return toVersion
   */
  @javax.annotation.Nullable
  public GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgradeToVersion getToVersion() {
    return toVersion;
  }

  public void setToVersion(GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgradeToVersion toVersion) {
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
    GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade getNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade = (GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade) o;
    return Objects.equals(this.toVersion, getNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade.toVersion);
  }

  @Override
  public int hashCode() {
    return Objects.hash(toVersion);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade {\n");
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
    openapiFields.add("toVersion");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade is not found in the empty JSON string", GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `toVersion`
      if (jsonObj.get("toVersion") != null && !jsonObj.get("toVersion").isJsonNull()) {
        GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgradeToVersion.validateJsonElement(jsonObj.get("toVersion"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade>() {
           @Override
           public void write(JsonWriter out, GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade
   * @throws IOException if the JSON string is invalid with respect to GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade
   */
  public static GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade.class);
  }

  /**
   * Convert an instance of GetNetworkFirmwareUpgradesStagedEvents200ResponseProductsSwitchNextUpgrade to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

