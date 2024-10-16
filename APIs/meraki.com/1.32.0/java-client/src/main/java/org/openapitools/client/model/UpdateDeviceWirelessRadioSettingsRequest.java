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
import org.openapitools.client.model.UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings;
import org.openapitools.client.model.UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings;

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
 * UpdateDeviceWirelessRadioSettingsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateDeviceWirelessRadioSettingsRequest {
  public static final String SERIALIZED_NAME_FIVE_GHZ_SETTINGS = "fiveGhzSettings";
  @SerializedName(SERIALIZED_NAME_FIVE_GHZ_SETTINGS)
  private UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings fiveGhzSettings;

  public static final String SERIALIZED_NAME_RF_PROFILE_ID = "rfProfileId";
  @SerializedName(SERIALIZED_NAME_RF_PROFILE_ID)
  private String rfProfileId;

  public static final String SERIALIZED_NAME_TWO_FOUR_GHZ_SETTINGS = "twoFourGhzSettings";
  @SerializedName(SERIALIZED_NAME_TWO_FOUR_GHZ_SETTINGS)
  private UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings twoFourGhzSettings;

  public UpdateDeviceWirelessRadioSettingsRequest() {
  }

  public UpdateDeviceWirelessRadioSettingsRequest fiveGhzSettings(UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings fiveGhzSettings) {
    this.fiveGhzSettings = fiveGhzSettings;
    return this;
  }

  /**
   * Get fiveGhzSettings
   * @return fiveGhzSettings
   */
  @javax.annotation.Nullable
  public UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings getFiveGhzSettings() {
    return fiveGhzSettings;
  }

  public void setFiveGhzSettings(UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings fiveGhzSettings) {
    this.fiveGhzSettings = fiveGhzSettings;
  }


  public UpdateDeviceWirelessRadioSettingsRequest rfProfileId(String rfProfileId) {
    this.rfProfileId = rfProfileId;
    return this;
  }

  /**
   * The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
   * @return rfProfileId
   */
  @javax.annotation.Nullable
  public String getRfProfileId() {
    return rfProfileId;
  }

  public void setRfProfileId(String rfProfileId) {
    this.rfProfileId = rfProfileId;
  }


  public UpdateDeviceWirelessRadioSettingsRequest twoFourGhzSettings(UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings twoFourGhzSettings) {
    this.twoFourGhzSettings = twoFourGhzSettings;
    return this;
  }

  /**
   * Get twoFourGhzSettings
   * @return twoFourGhzSettings
   */
  @javax.annotation.Nullable
  public UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings getTwoFourGhzSettings() {
    return twoFourGhzSettings;
  }

  public void setTwoFourGhzSettings(UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings twoFourGhzSettings) {
    this.twoFourGhzSettings = twoFourGhzSettings;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateDeviceWirelessRadioSettingsRequest updateDeviceWirelessRadioSettingsRequest = (UpdateDeviceWirelessRadioSettingsRequest) o;
    return Objects.equals(this.fiveGhzSettings, updateDeviceWirelessRadioSettingsRequest.fiveGhzSettings) &&
        Objects.equals(this.rfProfileId, updateDeviceWirelessRadioSettingsRequest.rfProfileId) &&
        Objects.equals(this.twoFourGhzSettings, updateDeviceWirelessRadioSettingsRequest.twoFourGhzSettings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fiveGhzSettings, rfProfileId, twoFourGhzSettings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateDeviceWirelessRadioSettingsRequest {\n");
    sb.append("    fiveGhzSettings: ").append(toIndentedString(fiveGhzSettings)).append("\n");
    sb.append("    rfProfileId: ").append(toIndentedString(rfProfileId)).append("\n");
    sb.append("    twoFourGhzSettings: ").append(toIndentedString(twoFourGhzSettings)).append("\n");
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
    openapiFields.add("fiveGhzSettings");
    openapiFields.add("rfProfileId");
    openapiFields.add("twoFourGhzSettings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateDeviceWirelessRadioSettingsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateDeviceWirelessRadioSettingsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateDeviceWirelessRadioSettingsRequest is not found in the empty JSON string", UpdateDeviceWirelessRadioSettingsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateDeviceWirelessRadioSettingsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateDeviceWirelessRadioSettingsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `fiveGhzSettings`
      if (jsonObj.get("fiveGhzSettings") != null && !jsonObj.get("fiveGhzSettings").isJsonNull()) {
        UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings.validateJsonElement(jsonObj.get("fiveGhzSettings"));
      }
      if ((jsonObj.get("rfProfileId") != null && !jsonObj.get("rfProfileId").isJsonNull()) && !jsonObj.get("rfProfileId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rfProfileId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rfProfileId").toString()));
      }
      // validate the optional field `twoFourGhzSettings`
      if (jsonObj.get("twoFourGhzSettings") != null && !jsonObj.get("twoFourGhzSettings").isJsonNull()) {
        UpdateDeviceWirelessRadioSettingsRequestTwoFourGhzSettings.validateJsonElement(jsonObj.get("twoFourGhzSettings"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateDeviceWirelessRadioSettingsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateDeviceWirelessRadioSettingsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateDeviceWirelessRadioSettingsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateDeviceWirelessRadioSettingsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateDeviceWirelessRadioSettingsRequest>() {
           @Override
           public void write(JsonWriter out, UpdateDeviceWirelessRadioSettingsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateDeviceWirelessRadioSettingsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateDeviceWirelessRadioSettingsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateDeviceWirelessRadioSettingsRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateDeviceWirelessRadioSettingsRequest
   */
  public static UpdateDeviceWirelessRadioSettingsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateDeviceWirelessRadioSettingsRequest.class);
  }

  /**
   * Convert an instance of UpdateDeviceWirelessRadioSettingsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

