/*
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
 * for a stat
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:51.881749-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SparkLine {
  public static final String SERIALIZED_NAME_FILL_COLOR = "fillColor";
  @SerializedName(SERIALIZED_NAME_FILL_COLOR)
  private String fillColor;

  public static final String SERIALIZED_NAME_FULL = "full";
  @SerializedName(SERIALIZED_NAME_FULL)
  private Boolean full;

  public static final String SERIALIZED_NAME_LINE_COLOR = "lineColor";
  @SerializedName(SERIALIZED_NAME_LINE_COLOR)
  private String lineColor;

  public static final String SERIALIZED_NAME_SHOW = "show";
  @SerializedName(SERIALIZED_NAME_SHOW)
  private Boolean show;

  public static final String SERIALIZED_NAME_YMAX = "ymax";
  @SerializedName(SERIALIZED_NAME_YMAX)
  private Double ymax;

  public static final String SERIALIZED_NAME_YMIN = "ymin";
  @SerializedName(SERIALIZED_NAME_YMIN)
  private Double ymin;

  public SparkLine() {
  }

  public SparkLine fillColor(String fillColor) {
    this.fillColor = fillColor;
    return this;
  }

  /**
   * Get fillColor
   * @return fillColor
   */
  @javax.annotation.Nullable
  public String getFillColor() {
    return fillColor;
  }

  public void setFillColor(String fillColor) {
    this.fillColor = fillColor;
  }


  public SparkLine full(Boolean full) {
    this.full = full;
    return this;
  }

  /**
   * Get full
   * @return full
   */
  @javax.annotation.Nullable
  public Boolean getFull() {
    return full;
  }

  public void setFull(Boolean full) {
    this.full = full;
  }


  public SparkLine lineColor(String lineColor) {
    this.lineColor = lineColor;
    return this;
  }

  /**
   * Get lineColor
   * @return lineColor
   */
  @javax.annotation.Nullable
  public String getLineColor() {
    return lineColor;
  }

  public void setLineColor(String lineColor) {
    this.lineColor = lineColor;
  }


  public SparkLine show(Boolean show) {
    this.show = show;
    return this;
  }

  /**
   * Get show
   * @return show
   */
  @javax.annotation.Nullable
  public Boolean getShow() {
    return show;
  }

  public void setShow(Boolean show) {
    this.show = show;
  }


  public SparkLine ymax(Double ymax) {
    this.ymax = ymax;
    return this;
  }

  /**
   * Get ymax
   * @return ymax
   */
  @javax.annotation.Nullable
  public Double getYmax() {
    return ymax;
  }

  public void setYmax(Double ymax) {
    this.ymax = ymax;
  }


  public SparkLine ymin(Double ymin) {
    this.ymin = ymin;
    return this;
  }

  /**
   * Get ymin
   * @return ymin
   */
  @javax.annotation.Nullable
  public Double getYmin() {
    return ymin;
  }

  public void setYmin(Double ymin) {
    this.ymin = ymin;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SparkLine sparkLine = (SparkLine) o;
    return Objects.equals(this.fillColor, sparkLine.fillColor) &&
        Objects.equals(this.full, sparkLine.full) &&
        Objects.equals(this.lineColor, sparkLine.lineColor) &&
        Objects.equals(this.show, sparkLine.show) &&
        Objects.equals(this.ymax, sparkLine.ymax) &&
        Objects.equals(this.ymin, sparkLine.ymin);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fillColor, full, lineColor, show, ymax, ymin);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SparkLine {\n");
    sb.append("    fillColor: ").append(toIndentedString(fillColor)).append("\n");
    sb.append("    full: ").append(toIndentedString(full)).append("\n");
    sb.append("    lineColor: ").append(toIndentedString(lineColor)).append("\n");
    sb.append("    show: ").append(toIndentedString(show)).append("\n");
    sb.append("    ymax: ").append(toIndentedString(ymax)).append("\n");
    sb.append("    ymin: ").append(toIndentedString(ymin)).append("\n");
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
    openapiFields.add("fillColor");
    openapiFields.add("full");
    openapiFields.add("lineColor");
    openapiFields.add("show");
    openapiFields.add("ymax");
    openapiFields.add("ymin");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SparkLine
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SparkLine.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SparkLine is not found in the empty JSON string", SparkLine.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SparkLine.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SparkLine` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("fillColor") != null && !jsonObj.get("fillColor").isJsonNull()) && !jsonObj.get("fillColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fillColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fillColor").toString()));
      }
      if ((jsonObj.get("lineColor") != null && !jsonObj.get("lineColor").isJsonNull()) && !jsonObj.get("lineColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lineColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lineColor").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SparkLine.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SparkLine' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SparkLine> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SparkLine.class));

       return (TypeAdapter<T>) new TypeAdapter<SparkLine>() {
           @Override
           public void write(JsonWriter out, SparkLine value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SparkLine read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SparkLine given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SparkLine
   * @throws IOException if the JSON string is invalid with respect to SparkLine
   */
  public static SparkLine fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SparkLine.class);
  }

  /**
   * Convert an instance of SparkLine to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

