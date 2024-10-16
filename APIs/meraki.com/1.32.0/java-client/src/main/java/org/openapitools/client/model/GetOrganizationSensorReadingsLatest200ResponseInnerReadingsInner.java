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
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerBattery;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerButton;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerDoor;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerHumidity;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerNoise;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerPm25;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerTemperature;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerTvoc;
import org.openapitools.client.model.GetOrganizationSensorReadingsHistory200ResponseInnerWater;

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
 * GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner {
  public static final String SERIALIZED_NAME_BATTERY = "battery";
  @SerializedName(SERIALIZED_NAME_BATTERY)
  private GetOrganizationSensorReadingsHistory200ResponseInnerBattery battery;

  public static final String SERIALIZED_NAME_BUTTON = "button";
  @SerializedName(SERIALIZED_NAME_BUTTON)
  private GetOrganizationSensorReadingsHistory200ResponseInnerButton button;

  public static final String SERIALIZED_NAME_DOOR = "door";
  @SerializedName(SERIALIZED_NAME_DOOR)
  private GetOrganizationSensorReadingsHistory200ResponseInnerDoor door;

  public static final String SERIALIZED_NAME_HUMIDITY = "humidity";
  @SerializedName(SERIALIZED_NAME_HUMIDITY)
  private GetOrganizationSensorReadingsHistory200ResponseInnerHumidity humidity;

  public static final String SERIALIZED_NAME_INDOOR_AIR_QUALITY = "indoorAirQuality";
  @SerializedName(SERIALIZED_NAME_INDOOR_AIR_QUALITY)
  private GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality indoorAirQuality;

  /**
   * Type of sensor reading.
   */
  @JsonAdapter(MetricEnum.Adapter.class)
  public enum MetricEnum {
    BATTERY("battery"),
    
    BUTTON("button"),
    
    DOOR("door"),
    
    HUMIDITY("humidity"),
    
    INDOOR_AIR_QUALITY("indoorAirQuality"),
    
    NOISE("noise"),
    
    PM25("pm25"),
    
    TEMPERATURE("temperature"),
    
    TVOC("tvoc"),
    
    WATER("water");

    private String value;

    MetricEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MetricEnum fromValue(String value) {
      for (MetricEnum b : MetricEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MetricEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MetricEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MetricEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MetricEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MetricEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_METRIC = "metric";
  @SerializedName(SERIALIZED_NAME_METRIC)
  private MetricEnum metric;

  public static final String SERIALIZED_NAME_NOISE = "noise";
  @SerializedName(SERIALIZED_NAME_NOISE)
  private GetOrganizationSensorReadingsHistory200ResponseInnerNoise noise;

  public static final String SERIALIZED_NAME_PM25 = "pm25";
  @SerializedName(SERIALIZED_NAME_PM25)
  private GetOrganizationSensorReadingsHistory200ResponseInnerPm25 pm25;

  public static final String SERIALIZED_NAME_TEMPERATURE = "temperature";
  @SerializedName(SERIALIZED_NAME_TEMPERATURE)
  private GetOrganizationSensorReadingsHistory200ResponseInnerTemperature temperature;

  public static final String SERIALIZED_NAME_TS = "ts";
  @SerializedName(SERIALIZED_NAME_TS)
  private String ts;

  public static final String SERIALIZED_NAME_TVOC = "tvoc";
  @SerializedName(SERIALIZED_NAME_TVOC)
  private GetOrganizationSensorReadingsHistory200ResponseInnerTvoc tvoc;

  public static final String SERIALIZED_NAME_WATER = "water";
  @SerializedName(SERIALIZED_NAME_WATER)
  private GetOrganizationSensorReadingsHistory200ResponseInnerWater water;

  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner() {
  }

  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner battery(GetOrganizationSensorReadingsHistory200ResponseInnerBattery battery) {
    this.battery = battery;
    return this;
  }

  /**
   * Get battery
   * @return battery
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerBattery getBattery() {
    return battery;
  }

  public void setBattery(GetOrganizationSensorReadingsHistory200ResponseInnerBattery battery) {
    this.battery = battery;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner button(GetOrganizationSensorReadingsHistory200ResponseInnerButton button) {
    this.button = button;
    return this;
  }

  /**
   * Get button
   * @return button
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerButton getButton() {
    return button;
  }

  public void setButton(GetOrganizationSensorReadingsHistory200ResponseInnerButton button) {
    this.button = button;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner door(GetOrganizationSensorReadingsHistory200ResponseInnerDoor door) {
    this.door = door;
    return this;
  }

  /**
   * Get door
   * @return door
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerDoor getDoor() {
    return door;
  }

  public void setDoor(GetOrganizationSensorReadingsHistory200ResponseInnerDoor door) {
    this.door = door;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner humidity(GetOrganizationSensorReadingsHistory200ResponseInnerHumidity humidity) {
    this.humidity = humidity;
    return this;
  }

  /**
   * Get humidity
   * @return humidity
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerHumidity getHumidity() {
    return humidity;
  }

  public void setHumidity(GetOrganizationSensorReadingsHistory200ResponseInnerHumidity humidity) {
    this.humidity = humidity;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner indoorAirQuality(GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality indoorAirQuality) {
    this.indoorAirQuality = indoorAirQuality;
    return this;
  }

  /**
   * Get indoorAirQuality
   * @return indoorAirQuality
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality getIndoorAirQuality() {
    return indoorAirQuality;
  }

  public void setIndoorAirQuality(GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality indoorAirQuality) {
    this.indoorAirQuality = indoorAirQuality;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner metric(MetricEnum metric) {
    this.metric = metric;
    return this;
  }

  /**
   * Type of sensor reading.
   * @return metric
   */
  @javax.annotation.Nullable
  public MetricEnum getMetric() {
    return metric;
  }

  public void setMetric(MetricEnum metric) {
    this.metric = metric;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner noise(GetOrganizationSensorReadingsHistory200ResponseInnerNoise noise) {
    this.noise = noise;
    return this;
  }

  /**
   * Get noise
   * @return noise
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerNoise getNoise() {
    return noise;
  }

  public void setNoise(GetOrganizationSensorReadingsHistory200ResponseInnerNoise noise) {
    this.noise = noise;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner pm25(GetOrganizationSensorReadingsHistory200ResponseInnerPm25 pm25) {
    this.pm25 = pm25;
    return this;
  }

  /**
   * Get pm25
   * @return pm25
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerPm25 getPm25() {
    return pm25;
  }

  public void setPm25(GetOrganizationSensorReadingsHistory200ResponseInnerPm25 pm25) {
    this.pm25 = pm25;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner temperature(GetOrganizationSensorReadingsHistory200ResponseInnerTemperature temperature) {
    this.temperature = temperature;
    return this;
  }

  /**
   * Get temperature
   * @return temperature
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerTemperature getTemperature() {
    return temperature;
  }

  public void setTemperature(GetOrganizationSensorReadingsHistory200ResponseInnerTemperature temperature) {
    this.temperature = temperature;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner ts(String ts) {
    this.ts = ts;
    return this;
  }

  /**
   * Time at which the reading occurred, in ISO8601 format.
   * @return ts
   */
  @javax.annotation.Nullable
  public String getTs() {
    return ts;
  }

  public void setTs(String ts) {
    this.ts = ts;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner tvoc(GetOrganizationSensorReadingsHistory200ResponseInnerTvoc tvoc) {
    this.tvoc = tvoc;
    return this;
  }

  /**
   * Get tvoc
   * @return tvoc
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerTvoc getTvoc() {
    return tvoc;
  }

  public void setTvoc(GetOrganizationSensorReadingsHistory200ResponseInnerTvoc tvoc) {
    this.tvoc = tvoc;
  }


  public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner water(GetOrganizationSensorReadingsHistory200ResponseInnerWater water) {
    this.water = water;
    return this;
  }

  /**
   * Get water
   * @return water
   */
  @javax.annotation.Nullable
  public GetOrganizationSensorReadingsHistory200ResponseInnerWater getWater() {
    return water;
  }

  public void setWater(GetOrganizationSensorReadingsHistory200ResponseInnerWater water) {
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
    GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner = (GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner) o;
    return Objects.equals(this.battery, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.battery) &&
        Objects.equals(this.button, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.button) &&
        Objects.equals(this.door, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.door) &&
        Objects.equals(this.humidity, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.humidity) &&
        Objects.equals(this.indoorAirQuality, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.indoorAirQuality) &&
        Objects.equals(this.metric, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.metric) &&
        Objects.equals(this.noise, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.noise) &&
        Objects.equals(this.pm25, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.pm25) &&
        Objects.equals(this.temperature, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.temperature) &&
        Objects.equals(this.ts, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.ts) &&
        Objects.equals(this.tvoc, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.tvoc) &&
        Objects.equals(this.water, getOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.water);
  }

  @Override
  public int hashCode() {
    return Objects.hash(battery, button, door, humidity, indoorAirQuality, metric, noise, pm25, temperature, ts, tvoc, water);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner {\n");
    sb.append("    battery: ").append(toIndentedString(battery)).append("\n");
    sb.append("    button: ").append(toIndentedString(button)).append("\n");
    sb.append("    door: ").append(toIndentedString(door)).append("\n");
    sb.append("    humidity: ").append(toIndentedString(humidity)).append("\n");
    sb.append("    indoorAirQuality: ").append(toIndentedString(indoorAirQuality)).append("\n");
    sb.append("    metric: ").append(toIndentedString(metric)).append("\n");
    sb.append("    noise: ").append(toIndentedString(noise)).append("\n");
    sb.append("    pm25: ").append(toIndentedString(pm25)).append("\n");
    sb.append("    temperature: ").append(toIndentedString(temperature)).append("\n");
    sb.append("    ts: ").append(toIndentedString(ts)).append("\n");
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
    openapiFields.add("battery");
    openapiFields.add("button");
    openapiFields.add("door");
    openapiFields.add("humidity");
    openapiFields.add("indoorAirQuality");
    openapiFields.add("metric");
    openapiFields.add("noise");
    openapiFields.add("pm25");
    openapiFields.add("temperature");
    openapiFields.add("ts");
    openapiFields.add("tvoc");
    openapiFields.add("water");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner is not found in the empty JSON string", GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `battery`
      if (jsonObj.get("battery") != null && !jsonObj.get("battery").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerBattery.validateJsonElement(jsonObj.get("battery"));
      }
      // validate the optional field `button`
      if (jsonObj.get("button") != null && !jsonObj.get("button").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerButton.validateJsonElement(jsonObj.get("button"));
      }
      // validate the optional field `door`
      if (jsonObj.get("door") != null && !jsonObj.get("door").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerDoor.validateJsonElement(jsonObj.get("door"));
      }
      // validate the optional field `humidity`
      if (jsonObj.get("humidity") != null && !jsonObj.get("humidity").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerHumidity.validateJsonElement(jsonObj.get("humidity"));
      }
      // validate the optional field `indoorAirQuality`
      if (jsonObj.get("indoorAirQuality") != null && !jsonObj.get("indoorAirQuality").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality.validateJsonElement(jsonObj.get("indoorAirQuality"));
      }
      if ((jsonObj.get("metric") != null && !jsonObj.get("metric").isJsonNull()) && !jsonObj.get("metric").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `metric` to be a primitive type in the JSON string but got `%s`", jsonObj.get("metric").toString()));
      }
      // validate the optional field `metric`
      if (jsonObj.get("metric") != null && !jsonObj.get("metric").isJsonNull()) {
        MetricEnum.validateJsonElement(jsonObj.get("metric"));
      }
      // validate the optional field `noise`
      if (jsonObj.get("noise") != null && !jsonObj.get("noise").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerNoise.validateJsonElement(jsonObj.get("noise"));
      }
      // validate the optional field `pm25`
      if (jsonObj.get("pm25") != null && !jsonObj.get("pm25").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerPm25.validateJsonElement(jsonObj.get("pm25"));
      }
      // validate the optional field `temperature`
      if (jsonObj.get("temperature") != null && !jsonObj.get("temperature").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerTemperature.validateJsonElement(jsonObj.get("temperature"));
      }
      if ((jsonObj.get("ts") != null && !jsonObj.get("ts").isJsonNull()) && !jsonObj.get("ts").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ts` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ts").toString()));
      }
      // validate the optional field `tvoc`
      if (jsonObj.get("tvoc") != null && !jsonObj.get("tvoc").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerTvoc.validateJsonElement(jsonObj.get("tvoc"));
      }
      // validate the optional field `water`
      if (jsonObj.get("water") != null && !jsonObj.get("water").isJsonNull()) {
        GetOrganizationSensorReadingsHistory200ResponseInnerWater.validateJsonElement(jsonObj.get("water"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner>() {
           @Override
           public void write(JsonWriter out, GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner
   */
  public static GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner.class);
  }

  /**
   * Convert an instance of GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

