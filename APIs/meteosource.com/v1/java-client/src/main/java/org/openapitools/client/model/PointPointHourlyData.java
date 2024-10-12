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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.PointPointHourlyCloudCoverData;
import org.openapitools.client.model.PointPointHourlyPrecipitationData;
import org.openapitools.client.model.PointPointHourlyProbData;
import org.openapitools.client.model.PointPointHourlyWindData;

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
 * PointPointHourlyData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:13.236583-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PointPointHourlyData {
  public static final String SERIALIZED_NAME_CAPE = "cape";
  @SerializedName(SERIALIZED_NAME_CAPE)
  private BigDecimal cape;

  public static final String SERIALIZED_NAME_CLOUD_COVER = "cloud_cover";
  @SerializedName(SERIALIZED_NAME_CLOUD_COVER)
  private PointPointHourlyCloudCoverData cloudCover;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private OffsetDateTime date;

  public static final String SERIALIZED_NAME_DEW_POINT = "dew_point";
  @SerializedName(SERIALIZED_NAME_DEW_POINT)
  private BigDecimal dewPoint;

  public static final String SERIALIZED_NAME_EVAPORATION = "evaporation";
  @SerializedName(SERIALIZED_NAME_EVAPORATION)
  private BigDecimal evaporation;

  public static final String SERIALIZED_NAME_FEELS_LIKE = "feels_like";
  @SerializedName(SERIALIZED_NAME_FEELS_LIKE)
  private BigDecimal feelsLike;

  public static final String SERIALIZED_NAME_HUMIDITY = "humidity";
  @SerializedName(SERIALIZED_NAME_HUMIDITY)
  private Integer humidity;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private Integer icon;

  public static final String SERIALIZED_NAME_IRRADIANCE = "irradiance";
  @SerializedName(SERIALIZED_NAME_IRRADIANCE)
  private BigDecimal irradiance;

  public static final String SERIALIZED_NAME_LFTX = "lftx";
  @SerializedName(SERIALIZED_NAME_LFTX)
  private BigDecimal lftx;

  public static final String SERIALIZED_NAME_OZONE = "ozone";
  @SerializedName(SERIALIZED_NAME_OZONE)
  private BigDecimal ozone;

  public static final String SERIALIZED_NAME_PRECIPITATION = "precipitation";
  @SerializedName(SERIALIZED_NAME_PRECIPITATION)
  private PointPointHourlyPrecipitationData precipitation;

  public static final String SERIALIZED_NAME_PRESSURE = "pressure";
  @SerializedName(SERIALIZED_NAME_PRESSURE)
  private BigDecimal pressure;

  public static final String SERIALIZED_NAME_PROBABILITY = "probability";
  @SerializedName(SERIALIZED_NAME_PROBABILITY)
  private PointPointHourlyProbData probability;

  public static final String SERIALIZED_NAME_SNOW_DEPTH = "snow_depth";
  @SerializedName(SERIALIZED_NAME_SNOW_DEPTH)
  private BigDecimal snowDepth;

  public static final String SERIALIZED_NAME_SOIL_TEMPERATURE = "soil_temperature";
  @SerializedName(SERIALIZED_NAME_SOIL_TEMPERATURE)
  private BigDecimal soilTemperature;

  public static final String SERIALIZED_NAME_SUMMARY = "summary";
  @SerializedName(SERIALIZED_NAME_SUMMARY)
  private String summary;

  public static final String SERIALIZED_NAME_SUNSHINE_DURATION = "sunshine_duration";
  @SerializedName(SERIALIZED_NAME_SUNSHINE_DURATION)
  private BigDecimal sunshineDuration;

  public static final String SERIALIZED_NAME_SURFACE_TEMPERATURE = "surface_temperature";
  @SerializedName(SERIALIZED_NAME_SURFACE_TEMPERATURE)
  private BigDecimal surfaceTemperature;

  public static final String SERIALIZED_NAME_TEMPERATURE = "temperature";
  @SerializedName(SERIALIZED_NAME_TEMPERATURE)
  private BigDecimal temperature;

  public static final String SERIALIZED_NAME_UV_INDEX = "uv_index";
  @SerializedName(SERIALIZED_NAME_UV_INDEX)
  private BigDecimal uvIndex;

  public static final String SERIALIZED_NAME_VISIBILITY = "visibility";
  @SerializedName(SERIALIZED_NAME_VISIBILITY)
  private BigDecimal visibility;

  public static final String SERIALIZED_NAME_WEATHER = "weather";
  @SerializedName(SERIALIZED_NAME_WEATHER)
  private String weather;

  public static final String SERIALIZED_NAME_WIND = "wind";
  @SerializedName(SERIALIZED_NAME_WIND)
  private PointPointHourlyWindData wind;

  public static final String SERIALIZED_NAME_WIND_CHILL = "wind_chill";
  @SerializedName(SERIALIZED_NAME_WIND_CHILL)
  private BigDecimal windChill;

  public PointPointHourlyData() {
  }

  public PointPointHourlyData cape(BigDecimal cape) {
    this.cape = cape;
    return this;
  }

  /**
   * Convective available potential energy. Unit: J/kg
   * @return cape
   */
  @javax.annotation.Nullable
  public BigDecimal getCape() {
    return cape;
  }

  public void setCape(BigDecimal cape) {
    this.cape = cape;
  }


  public PointPointHourlyData cloudCover(PointPointHourlyCloudCoverData cloudCover) {
    this.cloudCover = cloudCover;
    return this;
  }

  /**
   * Get cloudCover
   * @return cloudCover
   */
  @javax.annotation.Nonnull
  public PointPointHourlyCloudCoverData getCloudCover() {
    return cloudCover;
  }

  public void setCloudCover(PointPointHourlyCloudCoverData cloudCover) {
    this.cloudCover = cloudCover;
  }


  public PointPointHourlyData date(OffsetDateTime date) {
    this.date = date;
    return this;
  }

  /**
   * Datetime in YYYY-MM-DDTHH:MM:SS format.
   * @return date
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDate() {
    return date;
  }

  public void setDate(OffsetDateTime date) {
    this.date = date;
  }


  public PointPointHourlyData dewPoint(BigDecimal dewPoint) {
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


  public PointPointHourlyData evaporation(BigDecimal evaporation) {
    this.evaporation = evaporation;
    return this;
  }

  /**
   * Evaporation of liquid water into water vapor. Unit: mm/h
   * @return evaporation
   */
  @javax.annotation.Nullable
  public BigDecimal getEvaporation() {
    return evaporation;
  }

  public void setEvaporation(BigDecimal evaporation) {
    this.evaporation = evaporation;
  }


  public PointPointHourlyData feelsLike(BigDecimal feelsLike) {
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


  public PointPointHourlyData humidity(Integer humidity) {
    this.humidity = humidity;
    return this;
  }

  /**
   * Relative humidity. Unit: \\%
   * @return humidity
   */
  @javax.annotation.Nullable
  public Integer getHumidity() {
    return humidity;
  }

  public void setHumidity(Integer humidity) {
    this.humidity = humidity;
  }


  public PointPointHourlyData icon(Integer icon) {
    this.icon = icon;
    return this;
  }

  /**
   * Numeric identifier of the weather icon. The following values can appear:  * 1 - Not available * 2 - Sunny * 3 - Mostly sunny * 4 - Partly sunny * 5 - Mostly cloudy * 6 - Cloudy * 7 - Overcast * 8 - Overcast with low clouds * 9 - Fog * 10 - Light rain * 11 - Rain * 12 - Possible rain * 13 - Rain shower * 14 - Thunderstorm * 15 - Local thunderstorms * 16 - Light snow * 17 - Snow * 18 - Possible snow * 19 - Snow shower * 20 - Rain and snow * 21 - Possible rain and snow * 22 - Rain and snow * 23 - Freezing rain * 24 - Possible freezing rain * 25 - Hail * 26 - Clear (night) * 27 - Mostly clear (night) * 28 - Partly clear (night) * 29 - Mostly cloudy (night) * 30 - Cloudy (night) * 31 - Overcast with low clouds (night) * 32 - Rain shower (night) * 33 - Local thunderstorms (night) * 34 - Snow shower (night) * 35 - Rain and snow (night) * 36 - Possible freezing rain (night)  Unit: weather_ico0_36
   * @return icon
   */
  @javax.annotation.Nullable
  public Integer getIcon() {
    return icon;
  }

  public void setIcon(Integer icon) {
    this.icon = icon;
  }


  public PointPointHourlyData irradiance(BigDecimal irradiance) {
    this.irradiance = irradiance;
    return this;
  }

  /**
   * Global downward short-wave radiation flux. Unit: W/m2
   * @return irradiance
   */
  @javax.annotation.Nullable
  public BigDecimal getIrradiance() {
    return irradiance;
  }

  public void setIrradiance(BigDecimal irradiance) {
    this.irradiance = irradiance;
  }


  public PointPointHourlyData lftx(BigDecimal lftx) {
    this.lftx = lftx;
    return this;
  }

  /**
   * Surface lifted index. Unit: K
   * @return lftx
   */
  @javax.annotation.Nullable
  public BigDecimal getLftx() {
    return lftx;
  }

  public void setLftx(BigDecimal lftx) {
    this.lftx = lftx;
  }


  public PointPointHourlyData ozone(BigDecimal ozone) {
    this.ozone = ozone;
    return this;
  }

  /**
   * Total column of ozone. Unit: Dobson
   * @return ozone
   */
  @javax.annotation.Nullable
  public BigDecimal getOzone() {
    return ozone;
  }

  public void setOzone(BigDecimal ozone) {
    this.ozone = ozone;
  }


  public PointPointHourlyData precipitation(PointPointHourlyPrecipitationData precipitation) {
    this.precipitation = precipitation;
    return this;
  }

  /**
   * Get precipitation
   * @return precipitation
   */
  @javax.annotation.Nonnull
  public PointPointHourlyPrecipitationData getPrecipitation() {
    return precipitation;
  }

  public void setPrecipitation(PointPointHourlyPrecipitationData precipitation) {
    this.precipitation = precipitation;
  }


  public PointPointHourlyData pressure(BigDecimal pressure) {
    this.pressure = pressure;
    return this;
  }

  /**
   * Atmospheric pressure at mean sea level. Units: metric &#x3D; hPa, us &#x3D; Hg, uk &#x3D; hPa, ca &#x3D; kPa
   * @return pressure
   */
  @javax.annotation.Nullable
  public BigDecimal getPressure() {
    return pressure;
  }

  public void setPressure(BigDecimal pressure) {
    this.pressure = pressure;
  }


  public PointPointHourlyData probability(PointPointHourlyProbData probability) {
    this.probability = probability;
    return this;
  }

  /**
   * Get probability
   * @return probability
   */
  @javax.annotation.Nonnull
  public PointPointHourlyProbData getProbability() {
    return probability;
  }

  public void setProbability(PointPointHourlyProbData probability) {
    this.probability = probability;
  }


  public PointPointHourlyData snowDepth(BigDecimal snowDepth) {
    this.snowDepth = snowDepth;
    return this;
  }

  /**
   * Snow depth. Units: metric &#x3D; cm, us &#x3D; inch, uk &#x3D; cm, ca &#x3D; cm
   * @return snowDepth
   */
  @javax.annotation.Nullable
  public BigDecimal getSnowDepth() {
    return snowDepth;
  }

  public void setSnowDepth(BigDecimal snowDepth) {
    this.snowDepth = snowDepth;
  }


  public PointPointHourlyData soilTemperature(BigDecimal soilTemperature) {
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


  public PointPointHourlyData summary(String summary) {
    this.summary = summary;
    return this;
  }

  /**
   * Short text summary of the weather, e.g. &#x60;Light rain&#x60;.
   * @return summary
   */
  @javax.annotation.Nullable
  public String getSummary() {
    return summary;
  }

  public void setSummary(String summary) {
    this.summary = summary;
  }


  public PointPointHourlyData sunshineDuration(BigDecimal sunshineDuration) {
    this.sunshineDuration = sunshineDuration;
    return this;
  }

  /**
   * Sunshine duration since start of previous hour. Unit: s
   * @return sunshineDuration
   */
  @javax.annotation.Nullable
  public BigDecimal getSunshineDuration() {
    return sunshineDuration;
  }

  public void setSunshineDuration(BigDecimal sunshineDuration) {
    this.sunshineDuration = sunshineDuration;
  }


  public PointPointHourlyData surfaceTemperature(BigDecimal surfaceTemperature) {
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


  public PointPointHourlyData temperature(BigDecimal temperature) {
    this.temperature = temperature;
    return this;
  }

  /**
   * Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
   * @return temperature
   */
  @javax.annotation.Nullable
  public BigDecimal getTemperature() {
    return temperature;
  }

  public void setTemperature(BigDecimal temperature) {
    this.temperature = temperature;
  }


  public PointPointHourlyData uvIndex(BigDecimal uvIndex) {
    this.uvIndex = uvIndex;
    return this;
  }

  /**
   * UV index, values from zero (low risk of harm) to 11+ (extreme risk of harm). Unit: uv_index
   * @return uvIndex
   */
  @javax.annotation.Nullable
  public BigDecimal getUvIndex() {
    return uvIndex;
  }

  public void setUvIndex(BigDecimal uvIndex) {
    this.uvIndex = uvIndex;
  }


  public PointPointHourlyData visibility(BigDecimal visibility) {
    this.visibility = visibility;
    return this;
  }

  /**
   * Visibility. Units: metric &#x3D; km, us &#x3D; mi, uk &#x3D; mi, ca &#x3D; km
   * @return visibility
   */
  @javax.annotation.Nullable
  public BigDecimal getVisibility() {
    return visibility;
  }

  public void setVisibility(BigDecimal visibility) {
    this.visibility = visibility;
  }


  public PointPointHourlyData weather(String weather) {
    this.weather = weather;
    return this;
  }

  /**
   * String identifier of the weather icon, e.g. &#x60;light_rain&#x60;.
   * @return weather
   */
  @javax.annotation.Nullable
  public String getWeather() {
    return weather;
  }

  public void setWeather(String weather) {
    this.weather = weather;
  }


  public PointPointHourlyData wind(PointPointHourlyWindData wind) {
    this.wind = wind;
    return this;
  }

  /**
   * Get wind
   * @return wind
   */
  @javax.annotation.Nonnull
  public PointPointHourlyWindData getWind() {
    return wind;
  }

  public void setWind(PointPointHourlyWindData wind) {
    this.wind = wind;
  }


  public PointPointHourlyData windChill(BigDecimal windChill) {
    this.windChill = windChill;
    return this;
  }

  /**
   * Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C
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
    PointPointHourlyData pointPointHourlyData = (PointPointHourlyData) o;
    return Objects.equals(this.cape, pointPointHourlyData.cape) &&
        Objects.equals(this.cloudCover, pointPointHourlyData.cloudCover) &&
        Objects.equals(this.date, pointPointHourlyData.date) &&
        Objects.equals(this.dewPoint, pointPointHourlyData.dewPoint) &&
        Objects.equals(this.evaporation, pointPointHourlyData.evaporation) &&
        Objects.equals(this.feelsLike, pointPointHourlyData.feelsLike) &&
        Objects.equals(this.humidity, pointPointHourlyData.humidity) &&
        Objects.equals(this.icon, pointPointHourlyData.icon) &&
        Objects.equals(this.irradiance, pointPointHourlyData.irradiance) &&
        Objects.equals(this.lftx, pointPointHourlyData.lftx) &&
        Objects.equals(this.ozone, pointPointHourlyData.ozone) &&
        Objects.equals(this.precipitation, pointPointHourlyData.precipitation) &&
        Objects.equals(this.pressure, pointPointHourlyData.pressure) &&
        Objects.equals(this.probability, pointPointHourlyData.probability) &&
        Objects.equals(this.snowDepth, pointPointHourlyData.snowDepth) &&
        Objects.equals(this.soilTemperature, pointPointHourlyData.soilTemperature) &&
        Objects.equals(this.summary, pointPointHourlyData.summary) &&
        Objects.equals(this.sunshineDuration, pointPointHourlyData.sunshineDuration) &&
        Objects.equals(this.surfaceTemperature, pointPointHourlyData.surfaceTemperature) &&
        Objects.equals(this.temperature, pointPointHourlyData.temperature) &&
        Objects.equals(this.uvIndex, pointPointHourlyData.uvIndex) &&
        Objects.equals(this.visibility, pointPointHourlyData.visibility) &&
        Objects.equals(this.weather, pointPointHourlyData.weather) &&
        Objects.equals(this.wind, pointPointHourlyData.wind) &&
        Objects.equals(this.windChill, pointPointHourlyData.windChill);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cape, cloudCover, date, dewPoint, evaporation, feelsLike, humidity, icon, irradiance, lftx, ozone, precipitation, pressure, probability, snowDepth, soilTemperature, summary, sunshineDuration, surfaceTemperature, temperature, uvIndex, visibility, weather, wind, windChill);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PointPointHourlyData {\n");
    sb.append("    cape: ").append(toIndentedString(cape)).append("\n");
    sb.append("    cloudCover: ").append(toIndentedString(cloudCover)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    dewPoint: ").append(toIndentedString(dewPoint)).append("\n");
    sb.append("    evaporation: ").append(toIndentedString(evaporation)).append("\n");
    sb.append("    feelsLike: ").append(toIndentedString(feelsLike)).append("\n");
    sb.append("    humidity: ").append(toIndentedString(humidity)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    irradiance: ").append(toIndentedString(irradiance)).append("\n");
    sb.append("    lftx: ").append(toIndentedString(lftx)).append("\n");
    sb.append("    ozone: ").append(toIndentedString(ozone)).append("\n");
    sb.append("    precipitation: ").append(toIndentedString(precipitation)).append("\n");
    sb.append("    pressure: ").append(toIndentedString(pressure)).append("\n");
    sb.append("    probability: ").append(toIndentedString(probability)).append("\n");
    sb.append("    snowDepth: ").append(toIndentedString(snowDepth)).append("\n");
    sb.append("    soilTemperature: ").append(toIndentedString(soilTemperature)).append("\n");
    sb.append("    summary: ").append(toIndentedString(summary)).append("\n");
    sb.append("    sunshineDuration: ").append(toIndentedString(sunshineDuration)).append("\n");
    sb.append("    surfaceTemperature: ").append(toIndentedString(surfaceTemperature)).append("\n");
    sb.append("    temperature: ").append(toIndentedString(temperature)).append("\n");
    sb.append("    uvIndex: ").append(toIndentedString(uvIndex)).append("\n");
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
    openapiFields.add("cape");
    openapiFields.add("cloud_cover");
    openapiFields.add("date");
    openapiFields.add("dew_point");
    openapiFields.add("evaporation");
    openapiFields.add("feels_like");
    openapiFields.add("humidity");
    openapiFields.add("icon");
    openapiFields.add("irradiance");
    openapiFields.add("lftx");
    openapiFields.add("ozone");
    openapiFields.add("precipitation");
    openapiFields.add("pressure");
    openapiFields.add("probability");
    openapiFields.add("snow_depth");
    openapiFields.add("soil_temperature");
    openapiFields.add("summary");
    openapiFields.add("sunshine_duration");
    openapiFields.add("surface_temperature");
    openapiFields.add("temperature");
    openapiFields.add("uv_index");
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
   * @throws IOException if the JSON Element is invalid with respect to PointPointHourlyData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PointPointHourlyData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PointPointHourlyData is not found in the empty JSON string", PointPointHourlyData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PointPointHourlyData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PointPointHourlyData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PointPointHourlyData.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `cloud_cover`
      PointPointHourlyCloudCoverData.validateJsonElement(jsonObj.get("cloud_cover"));
      // validate the required field `precipitation`
      PointPointHourlyPrecipitationData.validateJsonElement(jsonObj.get("precipitation"));
      // validate the required field `probability`
      PointPointHourlyProbData.validateJsonElement(jsonObj.get("probability"));
      if ((jsonObj.get("summary") != null && !jsonObj.get("summary").isJsonNull()) && !jsonObj.get("summary").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `summary` to be a primitive type in the JSON string but got `%s`", jsonObj.get("summary").toString()));
      }
      if ((jsonObj.get("weather") != null && !jsonObj.get("weather").isJsonNull()) && !jsonObj.get("weather").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `weather` to be a primitive type in the JSON string but got `%s`", jsonObj.get("weather").toString()));
      }
      // validate the required field `wind`
      PointPointHourlyWindData.validateJsonElement(jsonObj.get("wind"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PointPointHourlyData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PointPointHourlyData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PointPointHourlyData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PointPointHourlyData.class));

       return (TypeAdapter<T>) new TypeAdapter<PointPointHourlyData>() {
           @Override
           public void write(JsonWriter out, PointPointHourlyData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PointPointHourlyData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PointPointHourlyData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PointPointHourlyData
   * @throws IOException if the JSON string is invalid with respect to PointPointHourlyData
   */
  public static PointPointHourlyData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PointPointHourlyData.class);
  }

  /**
   * Convert an instance of PointPointHourlyData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

