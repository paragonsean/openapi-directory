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
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdDoor;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdIndoorAirQuality;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdPm25;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTemperature;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTvoc;
import org.openapitools.client.model.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdWater;

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
 * Threshold for sensor readings that will cause an alert to be sent. This object should contain a single property key matching the condition&#39;s &#39;metric&#39; value.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold {
  public static final String SERIALIZED_NAME_DOOR = "door";
  @SerializedName(SERIALIZED_NAME_DOOR)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdDoor door;

  public static final String SERIALIZED_NAME_HUMIDITY = "humidity";
  @SerializedName(SERIALIZED_NAME_HUMIDITY)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity humidity;

  public static final String SERIALIZED_NAME_INDOOR_AIR_QUALITY = "indoorAirQuality";
  @SerializedName(SERIALIZED_NAME_INDOOR_AIR_QUALITY)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdIndoorAirQuality indoorAirQuality;

  public static final String SERIALIZED_NAME_NOISE = "noise";
  @SerializedName(SERIALIZED_NAME_NOISE)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise noise;

  public static final String SERIALIZED_NAME_PM25 = "pm25";
  @SerializedName(SERIALIZED_NAME_PM25)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdPm25 pm25;

  public static final String SERIALIZED_NAME_TEMPERATURE = "temperature";
  @SerializedName(SERIALIZED_NAME_TEMPERATURE)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTemperature temperature;

  public static final String SERIALIZED_NAME_TVOC = "tvoc";
  @SerializedName(SERIALIZED_NAME_TVOC)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTvoc tvoc;

  public static final String SERIALIZED_NAME_WATER = "water";
  @SerializedName(SERIALIZED_NAME_WATER)
  private GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdWater water;

  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold() {
  }

  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold door(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdDoor door) {
    this.door = door;
    return this;
  }

  /**
   * Get door
   * @return door
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdDoor getDoor() {
    return door;
  }

  public void setDoor(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdDoor door) {
    this.door = door;
  }


  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold humidity(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity humidity) {
    this.humidity = humidity;
    return this;
  }

  /**
   * Get humidity
   * @return humidity
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity getHumidity() {
    return humidity;
  }

  public void setHumidity(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity humidity) {
    this.humidity = humidity;
  }


  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold indoorAirQuality(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdIndoorAirQuality indoorAirQuality) {
    this.indoorAirQuality = indoorAirQuality;
    return this;
  }

  /**
   * Get indoorAirQuality
   * @return indoorAirQuality
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdIndoorAirQuality getIndoorAirQuality() {
    return indoorAirQuality;
  }

  public void setIndoorAirQuality(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdIndoorAirQuality indoorAirQuality) {
    this.indoorAirQuality = indoorAirQuality;
  }


  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold noise(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise noise) {
    this.noise = noise;
    return this;
  }

  /**
   * Get noise
   * @return noise
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise getNoise() {
    return noise;
  }

  public void setNoise(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise noise) {
    this.noise = noise;
  }


  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold pm25(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdPm25 pm25) {
    this.pm25 = pm25;
    return this;
  }

  /**
   * Get pm25
   * @return pm25
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdPm25 getPm25() {
    return pm25;
  }

  public void setPm25(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdPm25 pm25) {
    this.pm25 = pm25;
  }


  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold temperature(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTemperature temperature) {
    this.temperature = temperature;
    return this;
  }

  /**
   * Get temperature
   * @return temperature
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTemperature getTemperature() {
    return temperature;
  }

  public void setTemperature(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTemperature temperature) {
    this.temperature = temperature;
  }


  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold tvoc(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTvoc tvoc) {
    this.tvoc = tvoc;
    return this;
  }

  /**
   * Get tvoc
   * @return tvoc
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTvoc getTvoc() {
    return tvoc;
  }

  public void setTvoc(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTvoc tvoc) {
    this.tvoc = tvoc;
  }


  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold water(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdWater water) {
    this.water = water;
    return this;
  }

  /**
   * Get water
   * @return water
   */
  @javax.annotation.Nullable
  public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdWater getWater() {
    return water;
  }

  public void setWater(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdWater water) {
    this.water = water;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold = (GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold) o;
    return Objects.equals(this.door, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.door) &&
        Objects.equals(this.humidity, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.humidity) &&
        Objects.equals(this.indoorAirQuality, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.indoorAirQuality) &&
        Objects.equals(this.noise, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.noise) &&
        Objects.equals(this.pm25, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.pm25) &&
        Objects.equals(this.temperature, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.temperature) &&
        Objects.equals(this.tvoc, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.tvoc) &&
        Objects.equals(this.water, getNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.water);
  }

  @Override
  public int hashCode() {
    return Objects.hash(door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, water);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold {\n");
    sb.append("    door: ").append(toIndentedString(door)).append("\n");
    sb.append("    humidity: ").append(toIndentedString(humidity)).append("\n");
    sb.append("    indoorAirQuality: ").append(toIndentedString(indoorAirQuality)).append("\n");
    sb.append("    noise: ").append(toIndentedString(noise)).append("\n");
    sb.append("    pm25: ").append(toIndentedString(pm25)).append("\n");
    sb.append("    temperature: ").append(toIndentedString(temperature)).append("\n");
    sb.append("    tvoc: ").append(toIndentedString(tvoc)).append("\n");
    sb.append("    water: ").append(toIndentedString(water)).append("\n");
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
    openapiFields.add("door");
    openapiFields.add("humidity");
    openapiFields.add("indoorAirQuality");
    openapiFields.add("noise");
    openapiFields.add("pm25");
    openapiFields.add("temperature");
    openapiFields.add("tvoc");
    openapiFields.add("water");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold is not found in the empty JSON string", GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `door`
      if (jsonObj.get("door") != null && !jsonObj.get("door").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdDoor.validateJsonElement(jsonObj.get("door"));
      }
      // validate the optional field `humidity`
      if (jsonObj.get("humidity") != null && !jsonObj.get("humidity").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity.validateJsonElement(jsonObj.get("humidity"));
      }
      // validate the optional field `indoorAirQuality`
      if (jsonObj.get("indoorAirQuality") != null && !jsonObj.get("indoorAirQuality").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdIndoorAirQuality.validateJsonElement(jsonObj.get("indoorAirQuality"));
      }
      // validate the optional field `noise`
      if (jsonObj.get("noise") != null && !jsonObj.get("noise").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoise.validateJsonElement(jsonObj.get("noise"));
      }
      // validate the optional field `pm25`
      if (jsonObj.get("pm25") != null && !jsonObj.get("pm25").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdPm25.validateJsonElement(jsonObj.get("pm25"));
      }
      // validate the optional field `temperature`
      if (jsonObj.get("temperature") != null && !jsonObj.get("temperature").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTemperature.validateJsonElement(jsonObj.get("temperature"));
      }
      // validate the optional field `tvoc`
      if (jsonObj.get("tvoc") != null && !jsonObj.get("tvoc").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTvoc.validateJsonElement(jsonObj.get("tvoc"));
      }
      // validate the optional field `water`
      if (jsonObj.get("water") != null && !jsonObj.get("water").isJsonNull()) {
        GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdWater.validateJsonElement(jsonObj.get("water"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold>() {
           @Override
           public void write(JsonWriter out, GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold
   * @throws IOException if the JSON string is invalid with respect to GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold
   */
  public static GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.class);
  }

  /**
   * Convert an instance of GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

