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
 * Settings for SSID 6
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateNetworkWirelessRfProfileRequestPerSsidSettings6 {
  /**
   * Choice between &#39;dual&#39;, &#39;2.4ghz&#39; or &#39;5ghz&#39;.
   */
  @JsonAdapter(BandOperationModeEnum.Adapter.class)
  public enum BandOperationModeEnum {
    _2_4GHZ("2.4ghz"),
    
    _5GHZ("5ghz"),
    
    DUAL("dual");

    private String value;

    BandOperationModeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BandOperationModeEnum fromValue(String value) {
      for (BandOperationModeEnum b : BandOperationModeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BandOperationModeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BandOperationModeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BandOperationModeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BandOperationModeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BandOperationModeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BAND_OPERATION_MODE = "bandOperationMode";
  @SerializedName(SERIALIZED_NAME_BAND_OPERATION_MODE)
  private BandOperationModeEnum bandOperationMode;

  public static final String SERIALIZED_NAME_BAND_STEERING_ENABLED = "bandSteeringEnabled";
  @SerializedName(SERIALIZED_NAME_BAND_STEERING_ENABLED)
  private Boolean bandSteeringEnabled;

  public static final String SERIALIZED_NAME_MIN_BITRATE = "minBitrate";
  @SerializedName(SERIALIZED_NAME_MIN_BITRATE)
  private Float minBitrate;

  public CreateNetworkWirelessRfProfileRequestPerSsidSettings6() {
  }

  public CreateNetworkWirelessRfProfileRequestPerSsidSettings6 bandOperationMode(BandOperationModeEnum bandOperationMode) {
    this.bandOperationMode = bandOperationMode;
    return this;
  }

  /**
   * Choice between &#39;dual&#39;, &#39;2.4ghz&#39; or &#39;5ghz&#39;.
   * @return bandOperationMode
   */
  @javax.annotation.Nullable
  public BandOperationModeEnum getBandOperationMode() {
    return bandOperationMode;
  }

  public void setBandOperationMode(BandOperationModeEnum bandOperationMode) {
    this.bandOperationMode = bandOperationMode;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings6 bandSteeringEnabled(Boolean bandSteeringEnabled) {
    this.bandSteeringEnabled = bandSteeringEnabled;
    return this;
  }

  /**
   * Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false.
   * @return bandSteeringEnabled
   */
  @javax.annotation.Nullable
  public Boolean getBandSteeringEnabled() {
    return bandSteeringEnabled;
  }

  public void setBandSteeringEnabled(Boolean bandSteeringEnabled) {
    this.bandSteeringEnabled = bandSteeringEnabled;
  }


  public CreateNetworkWirelessRfProfileRequestPerSsidSettings6 minBitrate(Float minBitrate) {
    this.minBitrate = minBitrate;
    return this;
  }

  /**
   * Sets min bitrate (Mbps) of this SSID. Can be one of &#39;1&#39;, &#39;2&#39;, &#39;5.5&#39;, &#39;6&#39;, &#39;9&#39;, &#39;11&#39;, &#39;12&#39;, &#39;18&#39;, &#39;24&#39;, &#39;36&#39;, &#39;48&#39; or &#39;54&#39;.
   * @return minBitrate
   */
  @javax.annotation.Nullable
  public Float getMinBitrate() {
    return minBitrate;
  }

  public void setMinBitrate(Float minBitrate) {
    this.minBitrate = minBitrate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateNetworkWirelessRfProfileRequestPerSsidSettings6 createNetworkWirelessRfProfileRequestPerSsidSettings6 = (CreateNetworkWirelessRfProfileRequestPerSsidSettings6) o;
    return Objects.equals(this.bandOperationMode, createNetworkWirelessRfProfileRequestPerSsidSettings6.bandOperationMode) &&
        Objects.equals(this.bandSteeringEnabled, createNetworkWirelessRfProfileRequestPerSsidSettings6.bandSteeringEnabled) &&
        Objects.equals(this.minBitrate, createNetworkWirelessRfProfileRequestPerSsidSettings6.minBitrate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bandOperationMode, bandSteeringEnabled, minBitrate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateNetworkWirelessRfProfileRequestPerSsidSettings6 {\n");
    sb.append("    bandOperationMode: ").append(toIndentedString(bandOperationMode)).append("\n");
    sb.append("    bandSteeringEnabled: ").append(toIndentedString(bandSteeringEnabled)).append("\n");
    sb.append("    minBitrate: ").append(toIndentedString(minBitrate)).append("\n");
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
    openapiFields.add("bandOperationMode");
    openapiFields.add("bandSteeringEnabled");
    openapiFields.add("minBitrate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateNetworkWirelessRfProfileRequestPerSsidSettings6
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateNetworkWirelessRfProfileRequestPerSsidSettings6.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateNetworkWirelessRfProfileRequestPerSsidSettings6 is not found in the empty JSON string", CreateNetworkWirelessRfProfileRequestPerSsidSettings6.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateNetworkWirelessRfProfileRequestPerSsidSettings6.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateNetworkWirelessRfProfileRequestPerSsidSettings6` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("bandOperationMode") != null && !jsonObj.get("bandOperationMode").isJsonNull()) && !jsonObj.get("bandOperationMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bandOperationMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bandOperationMode").toString()));
      }
      // validate the optional field `bandOperationMode`
      if (jsonObj.get("bandOperationMode") != null && !jsonObj.get("bandOperationMode").isJsonNull()) {
        BandOperationModeEnum.validateJsonElement(jsonObj.get("bandOperationMode"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateNetworkWirelessRfProfileRequestPerSsidSettings6.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateNetworkWirelessRfProfileRequestPerSsidSettings6' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateNetworkWirelessRfProfileRequestPerSsidSettings6> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateNetworkWirelessRfProfileRequestPerSsidSettings6.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateNetworkWirelessRfProfileRequestPerSsidSettings6>() {
           @Override
           public void write(JsonWriter out, CreateNetworkWirelessRfProfileRequestPerSsidSettings6 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateNetworkWirelessRfProfileRequestPerSsidSettings6 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateNetworkWirelessRfProfileRequestPerSsidSettings6 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateNetworkWirelessRfProfileRequestPerSsidSettings6
   * @throws IOException if the JSON string is invalid with respect to CreateNetworkWirelessRfProfileRequestPerSsidSettings6
   */
  public static CreateNetworkWirelessRfProfileRequestPerSsidSettings6 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateNetworkWirelessRfProfileRequestPerSsidSettings6.class);
  }

  /**
   * Convert an instance of CreateNetworkWirelessRfProfileRequestPerSsidSettings6 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

