/*
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.client.model.PointPointDailyEveningCloudCoverData;
import org.openapitools.client.model.PointPointDailyEveningPrecipitationData;
import org.openapitools.client.model.PointPointDailyEveningProbData;
import org.openapitools.client.model.PointPointDailyEveningWindData;

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
 * PointPointDailyEveningData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:13.236583-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PointPointDailyEveningData {
  public static final String SERIALIZED_NAME_CLOUD_COVER = "cloud_cover";
  @SerializedName(SERIALIZED_NAME_CLOUD_COVER)
  private PointPointDailyEveningCloudCoverData cloudCover;

  public static final String SERIALIZED_NAME_DEW_POINT = "dew_point";
  @SerializedName(SERIALIZED_NAME_DEW_POINT)
  private BigDecimal dewPoint;

  public static final String SERIALIZED_NAME_FEELS_LIKE = "feels_like";
  @SerializedName(SERIALIZED_NAME_FEELS_LIKE)
  private BigDecimal feelsLike;

  public static final String SERIALIZED_NAME_HUMIDITY = "humidity";
  @SerializedName(SERIALIZED_NAME_HUMIDITY)
  private Integer humidity;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private Integer icon;

  public static final String SERIALIZED_NAME_OZONE = "ozone";
  @SerializedName(SERIALIZED_NAME_OZONE)
  private BigDecimal ozone;

  public static final String SERIALIZED_NAME_PRECIPITATION = "precipitation";
  @SerializedName(SERIALIZED_NAME_PRECIPITATION)
  private PointPointDailyEveningPrecipitationData precipitation;

  public static final String SERIALIZED_NAME_PRESSURE = "pressure";
  @SerializedName(SERIALIZED_NAME_PRESSURE)
  private BigDecimal pressure;

  public static final String SERIALIZED_NAME_PROBABILITY = "probability";
  @SerializedName(SERIALIZED_NAME_PROBABILITY)
  private PointPointDailyEveningProbData probability;

  public static final String SERIALIZED_NAME_SNOW_DEPTH = "snow_depth";
  @SerializedName(SERIALIZED_NAME_SNOW_DEPTH)
  private BigDecimal snowDepth;

  public static final String SERIALIZED_NAME_SOIL_TEMPERATURE = "soil_temperature";
  @SerializedName(SERIALIZED_NAME_SOIL_TEMPERATURE)
  private BigDecimal soilTemperature;

  public static final String SERIALIZED_NAME_SURFACE_TEMPERATURE = "surface_temperature";
  @SerializedName(SERIALIZED_NAME_SURFACE_TEMPERATURE)
  private BigDecimal surfaceTemperature;

  public static final String SERIALIZED_NAME_TEMPERATURE = "temperature";
  @SerializedName(SERIALIZED_NAME_TEMPERATURE)
  private BigDecimal temperature;

  public static final String SERIALIZED_NAME_VISIBILITY = "visibility";
  @SerializedName(SERIALIZED_NAME_VISIBILITY)
  private BigDecimal visibility;

  public static final String SERIALIZED_NAME_WEATHER = "weather";
  @SerializedName(SERIALIZED_NAME_WEATHER)
  private String weather;

  public static final String SERIALIZED_NAME_WIND = "wind";
  @SerializedName(SERIALIZED_NAME_WIND)
  private PointPointDailyEveningWindData wind;

  public static final String SERIALIZED_NAME_WIND_CHILL = "wind_chill";
  @SerializedName(SERIALIZED_NAME_WIND_CHILL)
  private BigDecimal windChill;

  public PointPointDailyEveningData() {
  }

  public PointPointDailyEveningData cloudCover(PointPointDailyEveningCloudCoverData cloudCover) {
    this.cloudCover = cloudCover;
    return this;
  }

  /**
   * Get cloudCover
   * @return cloudCover
   */
  @javax.annotation.Nonnull
  public PointPointDailyEveningCloudCoverData getCloudCover() {
    return cloudCover;
  }

  public void setCloudCover(PointPointDailyEveningCloudCoverData cloudCover) {
    this.cloudCover = cloudCover;
  }


  public PointPointDailyEveningData dewPoint(BigDecimal dewPoint) {
    this.dewPoint = dewPoint;
    return this;
  }

  /**
   * Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
   * @return dewPoint
   */
  @javax.annotation.Nullable
  public BigDecimal getDewPoint() {
    return dewPoint;
  }

  public void setDewPoint(BigDecimal dewPoint) {
    this.dewPoint = dewPoint;
  }


  public PointPointDailyEveningData feelsLike(BigDecimal feelsLike) {
    this.feelsLike = feelsLike;
    return this;
  }

  /**
   * Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
   * @return feelsLike
   */
  @javax.annotation.Nullable
  public BigDecimal getFeelsLike() {
    return feelsLike;
  }

  public void setFeelsLike(BigDecimal feelsLike) {
    this.feelsLike = feelsLike;
  }


  public PointPointDailyEveningData humidity(Integer humidity) {
    this.humidity = humidity;
    return this;
  }

  /**
   * Relative humidity. (evening avg) Unit: \\%
   * @return humidity
   */
  @javax.annotation.Nullable
  public Integer getHumidity() {
    return humidity;
  }

  public void setHumidity(Integer humidity) {
    this.humidity = humidity;
  }


  public PointPointDailyEveningData icon(Integer icon) {
    this.icon = icon;
    return this;
  }

  /**
   * Evening numeric identifier of the weather icon. The following values can appear:  * 1 - Not available * 2 - Sunny * 3 - Mostly sunny * 4 - Partly sunny * 5 - Mostly cloudy * 6 - Cloudy * 7 - Overcast * 8 - Overcast with low clouds * 9 - Fog * 10 - Light rain * 11 - Rain * 12 - Possible rain * 13 - Rain shower * 14 - Thunderstorm * 15 - Local thunderstorms * 16 - Light snow * 17 - Snow * 18 - Possible snow * 19 - Snow shower * 20 - Rain and snow * 21 - Possible rain and snow * 22 - Rain and snow * 23 - Freezing rain * 24 - Possible freezing rain * 25 - Hail * 26 - Clear (night) * 27 - Mostly clear (night) * 28 - Partly clear (night) * 29 - Mostly cloudy (night) * 30 - Cloudy (night) * 31 - Overcast with low clouds (night) * 32 - Rain shower (night) * 33 - Local thunderstorms (night) * 34 - Snow shower (night) * 35 - Rain and snow (night) * 36 - Possible freezing rain (night)  Unit: icon
   * @return icon
   */
  @javax.annotation.Nullable
  public Integer getIcon() {
    return icon;
  }

  public void setIcon(Integer icon) {
    this.icon = icon;
  }


  public PointPointDailyEveningData ozone(BigDecimal ozone) {
    this.ozone = ozone;
    return this;
  }

  /**
   * Total column of ozone. (evening avg) Unit: Dobson
   * @return ozone
   */
  @javax.annotation.Nullable
  public BigDecimal getOzone() {
    return ozone;
  }

  public void setOzone(BigDecimal ozone) {
    this.ozone = ozone;
  }


  public PointPointDailyEveningData precipitation(PointPointDailyEveningPrecipitationData precipitation) {
    this.precipitation = precipitation;
    return this;
  }

  /**
   * Get precipitation
   * @return precipitation
   */
  @javax.annotation.Nonnull
  public PointPointDailyEveningPrecipitationData getPrecipitation() {
    return precipitation;
  }

  public void setPrecipitation(PointPointDailyEveningPrecipitationData precipitation) {
    this.precipitation = precipitation;
  }


  public PointPointDailyEveningData pressure(BigDecimal pressure) {
    this.pressure = pressure;
    return this;
  }

  /**
   * Atmospheric pressure at mean sea level. (evening avg) Units: metric &#x3D; hPa, us &#x3D; Hg, uk &#x3D; hPa, ca &#x3D; kPa
   * @return pressure
   */
  @javax.annotation.Nullable
  public BigDecimal getPressure() {
    return pressure;
  }

  public void setPressure(BigDecimal pressure) {
    this.pressure = pressure;
  }


  public PointPointDailyEveningData probability(PointPointDailyEveningProbData probability) {
    this.probability = probability;
    return this;
  }

  /**
   * Get probability
   * @return probability
   */
  @javax.annotation.Nonnull
  public PointPointDailyEveningProbData getProbability() {
    return probability;
  }

  public void setProbability(PointPointDailyEveningProbData probability) {
    this.probability = probability;
  }


  public PointPointDailyEveningData snowDepth(BigDecimal snowDepth) {
    this.snowDepth = snowDepth;
    return this;
  }

  /**
   * Snow depth. (evening avg) Units: metric &#x3D; cm, us &#x3D; inch, uk &#x3D; cm, ca &#x3D; cm
   * @return snowDepth
   */
  @javax.annotation.Nullable
  public BigDecimal getSnowDepth() {
    return snowDepth;
  }

  public void setSnowDepth(BigDecimal snowDepth) {
    this.snowDepth = snowDepth;
  }


  public PointPointDailyEveningData soilTemperature(BigDecimal soilTemperature) {
    this.soilTemperature = soilTemperature;
    return this;
  }

  /**
   * Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
   * @return soilTemperature
   */
  @javax.annotation.Nullable
  public BigDecimal getSoilTemperature() {
    return soilTemperature;
  }

  public void setSoilTemperature(BigDecimal soilTemperature) {
    this.soilTemperature = soilTemperature;
  }


  public PointPointDailyEveningData surfaceTemperature(BigDecimal surfaceTemperature) {
    this.surfaceTemperature = surfaceTemperature;
    return this;
  }

  /**
   * Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
   * @return surfaceTemperature
   */
  @javax.annotation.Nullable
  public BigDecimal getSurfaceTemperature() {
    return surfaceTemperature;
  }

  public void setSurfaceTemperature(BigDecimal surfaceTemperature) {
    this.surfaceTemperature = surfaceTemperature;
  }


  public PointPointDailyEveningData temperature(BigDecimal temperature) {
    this.temperature = temperature;
    return this;
  }

  /**
   * Temperature 2 metres above ground. (evening avg) Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
   * @return temperature
   */
  @javax.annotation.Nullable
  public BigDecimal getTemperature() {
    return temperature;
  }

  public void setTemperature(BigDecimal temperature) {
    this.temperature = temperature;
  }


  public PointPointDailyEveningData visibility(BigDecimal visibility) {
    this.visibility = visibility;
    return this;
  }

  /**
   * Visibility. (evening avg) Units: metric &#x3D; km, us &#x3D; mi, uk &#x3D; mi, ca &#x3D; km
   * @return visibility
   */
  @javax.annotation.Nullable
  public BigDecimal getVisibility() {
    return visibility;
  }

  public void setVisibility(BigDecimal visibility) {
    this.visibility = visibility;
  }


  public PointPointDailyEveningData weather(String weather) {
    this.weather = weather;
    return this;
  }

  /**
   * Evening day string identifier of the weather icon, e.g. &#x60;light_rain&#x60;.
   * @return weather
   */
  @javax.annotation.Nullable
  public String getWeather() {
    return weather;
  }

  public void setWeather(String weather) {
    this.weather = weather;
  }


  public PointPointDailyEveningData wind(PointPointDailyEveningWindData wind) {
    this.wind = wind;
    return this;
  }

  /**
   * Get wind
   * @return wind
   */
  @javax.annotation.Nonnull
  public PointPointDailyEveningWindData getWind() {
    return wind;
  }

  public void setWind(PointPointDailyEveningWindData wind) {
    this.wind = wind;
  }


  public PointPointDailyEveningData windChill(BigDecimal windChill) {
    this.windChill = windChill;
    return this;
  }

  /**
   * Temperature 2 metres above ground. (evening avg) Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
   * @return windChill
   */
  @javax.annotation.Nullable
  public BigDecimal getWindChill() {
    return windChill;
  }

  public void setWindChill(BigDecimal windChill) {
    this.windChill = windChill;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PointPointDailyEveningData pointPointDailyEveningData = (PointPointDailyEveningData) o;
    return Objects.equals(this.cloudCover, pointPointDailyEveningData.cloudCover) &&
        Objects.equals(this.dewPoint, pointPointDailyEveningData.dewPoint) &&
        Objects.equals(this.feelsLike, pointPointDailyEveningData.feelsLike) &&
        Objects.equals(this.humidity, pointPointDailyEveningData.humidity) &&
        Objects.equals(this.icon, pointPointDailyEveningData.icon) &&
        Objects.equals(this.ozone, pointPointDailyEveningData.ozone) &&
        Objects.equals(this.precipitation, pointPointDailyEveningData.precipitation) &&
        Objects.equals(this.pressure, pointPointDailyEveningData.pressure) &&
        Objects.equals(this.probability, pointPointDailyEveningData.probability) &&
        Objects.equals(this.snowDepth, pointPointDailyEveningData.snowDepth) &&
        Objects.equals(this.soilTemperature, pointPointDailyEveningData.soilTemperature) &&
        Objects.equals(this.surfaceTemperature, pointPointDailyEveningData.surfaceTemperature) &&
        Objects.equals(this.temperature, pointPointDailyEveningData.temperature) &&
        Objects.equals(this.visibility, pointPointDailyEveningData.visibility) &&
        Objects.equals(this.weather, pointPointDailyEveningData.weather) &&
        Objects.equals(this.wind, pointPointDailyEveningData.wind) &&
        Objects.equals(this.windChill, pointPointDailyEveningData.windChill);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cloudCover, dewPoint, feelsLike, humidity, icon, ozone, precipitation, pressure, probability, snowDepth, soilTemperature, surfaceTemperature, temperature, visibility, weather, wind, windChill);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PointPointDailyEveningData {\n");
    sb.append("    cloudCover: ").append(toIndentedString(cloudCover)).append("\n");
    sb.append("    dewPoint: ").append(toIndentedString(dewPoint)).append("\n");
    sb.append("    feelsLike: ").append(toIndentedString(feelsLike)).append("\n");
    sb.append("    humidity: ").append(toIndentedString(humidity)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    ozone: ").append(toIndentedString(ozone)).append("\n");
    sb.append("    precipitation: ").append(toIndentedString(precipitation)).append("\n");
    sb.append("    pressure: ").append(toIndentedString(pressure)).append("\n");
    sb.append("    probability: ").append(toIndentedString(probability)).append("\n");
    sb.append("    snowDepth: ").append(toIndentedString(snowDepth)).append("\n");
    sb.append("    soilTemperature: ").append(toIndentedString(soilTemperature)).append("\n");
    sb.append("    surfaceTemperature: ").append(toIndentedString(surfaceTemperature)).append("\n");
    sb.append("    temperature: ").append(toIndentedString(temperature)).append("\n");
    sb.append("    visibility: ").append(toIndentedString(visibility)).append("\n");
    sb.append("    weather: ").append(toIndentedString(weather)).append("\n");
    sb.append("    wind: ").append(toIndentedString(wind)).append("\n");
    sb.append("    windChill: ").append(toIndentedString(windChill)).append("\n");
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
    openapiFields.add("cloud_cover");
    openapiFields.add("dew_point");
    openapiFields.add("feels_like");
    openapiFields.add("humidity");
    openapiFields.add("icon");
    openapiFields.add("ozone");
    openapiFields.add("precipitation");
    openapiFields.add("pressure");
    openapiFields.add("probability");
    openapiFields.add("snow_depth");
    openapiFields.add("soil_temperature");
    openapiFields.add("surface_temperature");
    openapiFields.add("temperature");
    openapiFields.add("visibility");
    openapiFields.add("weather");
    openapiFields.add("wind");
    openapiFields.add("wind_chill");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("cloud_cover");
    openapiRequiredFields.add("precipitation");
    openapiRequiredFields.add("probability");
    openapiRequiredFields.add("wind");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PointPointDailyEveningData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PointPointDailyEveningData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PointPointDailyEveningData is not found in the empty JSON string", PointPointDailyEveningData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PointPointDailyEveningData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PointPointDailyEveningData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PointPointDailyEveningData.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `cloud_cover`
      PointPointDailyEveningCloudCoverData.validateJsonElement(jsonObj.get("cloud_cover"));
      // validate the required field `precipitation`
      PointPointDailyEveningPrecipitationData.validateJsonElement(jsonObj.get("precipitation"));
      // validate the required field `probability`
      PointPointDailyEveningProbData.validateJsonElement(jsonObj.get("probability"));
      if ((jsonObj.get("weather") != null && !jsonObj.get("weather").isJsonNull()) && !jsonObj.get("weather").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `weather` to be a primitive type in the JSON string but got `%s`", jsonObj.get("weather").toString()));
      }
      // validate the required field `wind`
      PointPointDailyEveningWindData.validateJsonElement(jsonObj.get("wind"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PointPointDailyEveningData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PointPointDailyEveningData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PointPointDailyEveningData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PointPointDailyEveningData.class));

       return (TypeAdapter<T>) new TypeAdapter<PointPointDailyEveningData>() {
           @Override
           public void write(JsonWriter out, PointPointDailyEveningData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PointPointDailyEveningData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PointPointDailyEveningData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PointPointDailyEveningData
   * @throws IOException if the JSON string is invalid with respect to PointPointDailyEveningData
   */
  public static PointPointDailyEveningData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PointPointDailyEveningData.class);
  }

  /**
   * Convert an instance of PointPointDailyEveningData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

