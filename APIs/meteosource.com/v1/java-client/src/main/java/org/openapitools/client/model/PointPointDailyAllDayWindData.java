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
import java.io.File;
import java.io.IOException;
import java.math.BigDecimal;
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
 * PointPointDailyAllDayWindData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:13.236583-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PointPointDailyAllDayWindData {
  public static final String SERIALIZED_NAME_ANGLE = "angle";
  @SerializedName(SERIALIZED_NAME_ANGLE)
  private BigDecimal angle;

  public static final String SERIALIZED_NAME_DIR = "dir";
  @SerializedName(SERIALIZED_NAME_DIR)
  private File dir;

  public static final String SERIALIZED_NAME_GUSTS = "gusts";
  @SerializedName(SERIALIZED_NAME_GUSTS)
  private BigDecimal gusts;

  public static final String SERIALIZED_NAME_SPEED = "speed";
  @SerializedName(SERIALIZED_NAME_SPEED)
  private BigDecimal speed;

  public PointPointDailyAllDayWindData() {
  }

  public PointPointDailyAllDayWindData angle(BigDecimal angle) {
    this.angle = angle;
    return this;
  }

  /**
   * All day wind direction angle in degrees, 180° means wind from the south. Unit: degrees
   * @return angle
   */
  @javax.annotation.Nullable
  public BigDecimal getAngle() {
    return angle;
  }

  public void setAngle(BigDecimal angle) {
    this.angle = angle;
  }


  public PointPointDailyAllDayWindData dir(File dir) {
    this.dir = dir;
    return this;
  }

  /**
   * All day wind direction in &#x60;N&#x60;, &#x60;NNE&#x60;, &#x60;NE&#x60;, ..., &#x60;NNW&#x60; format. Unit: 16dir
   * @return dir
   */
  @javax.annotation.Nullable
  public File getDir() {
    return dir;
  }

  public void setDir(File dir) {
    this.dir = dir;
  }


  public PointPointDailyAllDayWindData gusts(BigDecimal gusts) {
    this.gusts = gusts;
    return this;
  }

  /**
   * Units: metric &#x3D; m/s, us &#x3D; mph, uk &#x3D; mph, ca &#x3D; km/h
   * @return gusts
   */
  @javax.annotation.Nullable
  public BigDecimal getGusts() {
    return gusts;
  }

  public void setGusts(BigDecimal gusts) {
    this.gusts = gusts;
  }


  public PointPointDailyAllDayWindData speed(BigDecimal speed) {
    this.speed = speed;
    return this;
  }

  /**
   * Units: metric &#x3D; m/s, us &#x3D; mph, uk &#x3D; mph, ca &#x3D; km/h
   * @return speed
   */
  @javax.annotation.Nullable
  public BigDecimal getSpeed() {
    return speed;
  }

  public void setSpeed(BigDecimal speed) {
    this.speed = speed;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PointPointDailyAllDayWindData pointPointDailyAllDayWindData = (PointPointDailyAllDayWindData) o;
    return Objects.equals(this.angle, pointPointDailyAllDayWindData.angle) &&
        Objects.equals(this.dir, pointPointDailyAllDayWindData.dir) &&
        Objects.equals(this.gusts, pointPointDailyAllDayWindData.gusts) &&
        Objects.equals(this.speed, pointPointDailyAllDayWindData.speed);
  }

  @Override
  public int hashCode() {
    return Objects.hash(angle, dir, gusts, speed);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PointPointDailyAllDayWindData {\n");
    sb.append("    angle: ").append(toIndentedString(angle)).append("\n");
    sb.append("    dir: ").append(toIndentedString(dir)).append("\n");
    sb.append("    gusts: ").append(toIndentedString(gusts)).append("\n");
    sb.append("    speed: ").append(toIndentedString(speed)).append("\n");
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
    openapiFields.add("angle");
    openapiFields.add("dir");
    openapiFields.add("gusts");
    openapiFields.add("speed");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PointPointDailyAllDayWindData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PointPointDailyAllDayWindData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PointPointDailyAllDayWindData is not found in the empty JSON string", PointPointDailyAllDayWindData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PointPointDailyAllDayWindData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PointPointDailyAllDayWindData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PointPointDailyAllDayWindData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PointPointDailyAllDayWindData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PointPointDailyAllDayWindData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PointPointDailyAllDayWindData.class));

       return (TypeAdapter<T>) new TypeAdapter<PointPointDailyAllDayWindData>() {
           @Override
           public void write(JsonWriter out, PointPointDailyAllDayWindData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PointPointDailyAllDayWindData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PointPointDailyAllDayWindData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PointPointDailyAllDayWindData
   * @throws IOException if the JSON string is invalid with respect to PointPointDailyAllDayWindData
   */
  public static PointPointDailyAllDayWindData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PointPointDailyAllDayWindData.class);
  }

  /**
   * Convert an instance of PointPointDailyAllDayWindData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

