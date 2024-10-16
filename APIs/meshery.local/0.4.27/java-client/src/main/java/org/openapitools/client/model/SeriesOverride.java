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
import org.openapitools.client.model.BoolString;

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
 * for a graph panel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:51.881749-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SeriesOverride {
  public static final String SERIALIZED_NAME_ALIAS = "alias";
  @SerializedName(SERIALIZED_NAME_ALIAS)
  private String alias;

  public static final String SERIALIZED_NAME_BARS = "bars";
  @SerializedName(SERIALIZED_NAME_BARS)
  private Boolean bars;

  public static final String SERIALIZED_NAME_COLOR = "color";
  @SerializedName(SERIALIZED_NAME_COLOR)
  private String color;

  public static final String SERIALIZED_NAME_DASHES = "dashes";
  @SerializedName(SERIALIZED_NAME_DASHES)
  private Boolean dashes;

  public static final String SERIALIZED_NAME_FILL = "fill";
  @SerializedName(SERIALIZED_NAME_FILL)
  private Long fill;

  public static final String SERIALIZED_NAME_FILL_BELOW_TO = "fillBelowTo";
  @SerializedName(SERIALIZED_NAME_FILL_BELOW_TO)
  private String fillBelowTo;

  public static final String SERIALIZED_NAME_LEGEND = "legend";
  @SerializedName(SERIALIZED_NAME_LEGEND)
  private Boolean legend;

  public static final String SERIALIZED_NAME_LINES = "lines";
  @SerializedName(SERIALIZED_NAME_LINES)
  private Boolean lines;

  public static final String SERIALIZED_NAME_LINEWIDTH = "linewidth";
  @SerializedName(SERIALIZED_NAME_LINEWIDTH)
  private Long linewidth;

  public static final String SERIALIZED_NAME_NULL_POINT_MODE = "nullPointMode";
  @SerializedName(SERIALIZED_NAME_NULL_POINT_MODE)
  private String nullPointMode;

  public static final String SERIALIZED_NAME_STACK = "stack";
  @SerializedName(SERIALIZED_NAME_STACK)
  private BoolString stack;

  public static final String SERIALIZED_NAME_TRANSFORM = "transform";
  @SerializedName(SERIALIZED_NAME_TRANSFORM)
  private String transform;

  public static final String SERIALIZED_NAME_YAXIS = "yaxis";
  @SerializedName(SERIALIZED_NAME_YAXIS)
  private Long yaxis;

  public static final String SERIALIZED_NAME_ZINDEX = "zindex";
  @SerializedName(SERIALIZED_NAME_ZINDEX)
  private Long zindex;

  public SeriesOverride() {
  }

  public SeriesOverride alias(String alias) {
    this.alias = alias;
    return this;
  }

  /**
   * Get alias
   * @return alias
   */
  @javax.annotation.Nullable
  public String getAlias() {
    return alias;
  }

  public void setAlias(String alias) {
    this.alias = alias;
  }


  public SeriesOverride bars(Boolean bars) {
    this.bars = bars;
    return this;
  }

  /**
   * Get bars
   * @return bars
   */
  @javax.annotation.Nullable
  public Boolean getBars() {
    return bars;
  }

  public void setBars(Boolean bars) {
    this.bars = bars;
  }


  public SeriesOverride color(String color) {
    this.color = color;
    return this;
  }

  /**
   * Get color
   * @return color
   */
  @javax.annotation.Nullable
  public String getColor() {
    return color;
  }

  public void setColor(String color) {
    this.color = color;
  }


  public SeriesOverride dashes(Boolean dashes) {
    this.dashes = dashes;
    return this;
  }

  /**
   * Get dashes
   * @return dashes
   */
  @javax.annotation.Nullable
  public Boolean getDashes() {
    return dashes;
  }

  public void setDashes(Boolean dashes) {
    this.dashes = dashes;
  }


  public SeriesOverride fill(Long fill) {
    this.fill = fill;
    return this;
  }

  /**
   * Get fill
   * @return fill
   */
  @javax.annotation.Nullable
  public Long getFill() {
    return fill;
  }

  public void setFill(Long fill) {
    this.fill = fill;
  }


  public SeriesOverride fillBelowTo(String fillBelowTo) {
    this.fillBelowTo = fillBelowTo;
    return this;
  }

  /**
   * Get fillBelowTo
   * @return fillBelowTo
   */
  @javax.annotation.Nullable
  public String getFillBelowTo() {
    return fillBelowTo;
  }

  public void setFillBelowTo(String fillBelowTo) {
    this.fillBelowTo = fillBelowTo;
  }


  public SeriesOverride legend(Boolean legend) {
    this.legend = legend;
    return this;
  }

  /**
   * Get legend
   * @return legend
   */
  @javax.annotation.Nullable
  public Boolean getLegend() {
    return legend;
  }

  public void setLegend(Boolean legend) {
    this.legend = legend;
  }


  public SeriesOverride lines(Boolean lines) {
    this.lines = lines;
    return this;
  }

  /**
   * Get lines
   * @return lines
   */
  @javax.annotation.Nullable
  public Boolean getLines() {
    return lines;
  }

  public void setLines(Boolean lines) {
    this.lines = lines;
  }


  public SeriesOverride linewidth(Long linewidth) {
    this.linewidth = linewidth;
    return this;
  }

  /**
   * Get linewidth
   * @return linewidth
   */
  @javax.annotation.Nullable
  public Long getLinewidth() {
    return linewidth;
  }

  public void setLinewidth(Long linewidth) {
    this.linewidth = linewidth;
  }


  public SeriesOverride nullPointMode(String nullPointMode) {
    this.nullPointMode = nullPointMode;
    return this;
  }

  /**
   * Get nullPointMode
   * @return nullPointMode
   */
  @javax.annotation.Nullable
  public String getNullPointMode() {
    return nullPointMode;
  }

  public void setNullPointMode(String nullPointMode) {
    this.nullPointMode = nullPointMode;
  }


  public SeriesOverride stack(BoolString stack) {
    this.stack = stack;
    return this;
  }

  /**
   * Get stack
   * @return stack
   */
  @javax.annotation.Nullable
  public BoolString getStack() {
    return stack;
  }

  public void setStack(BoolString stack) {
    this.stack = stack;
  }


  public SeriesOverride transform(String transform) {
    this.transform = transform;
    return this;
  }

  /**
   * Get transform
   * @return transform
   */
  @javax.annotation.Nullable
  public String getTransform() {
    return transform;
  }

  public void setTransform(String transform) {
    this.transform = transform;
  }


  public SeriesOverride yaxis(Long yaxis) {
    this.yaxis = yaxis;
    return this;
  }

  /**
   * Get yaxis
   * @return yaxis
   */
  @javax.annotation.Nullable
  public Long getYaxis() {
    return yaxis;
  }

  public void setYaxis(Long yaxis) {
    this.yaxis = yaxis;
  }


  public SeriesOverride zindex(Long zindex) {
    this.zindex = zindex;
    return this;
  }

  /**
   * Get zindex
   * @return zindex
   */
  @javax.annotation.Nullable
  public Long getZindex() {
    return zindex;
  }

  public void setZindex(Long zindex) {
    this.zindex = zindex;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SeriesOverride seriesOverride = (SeriesOverride) o;
    return Objects.equals(this.alias, seriesOverride.alias) &&
        Objects.equals(this.bars, seriesOverride.bars) &&
        Objects.equals(this.color, seriesOverride.color) &&
        Objects.equals(this.dashes, seriesOverride.dashes) &&
        Objects.equals(this.fill, seriesOverride.fill) &&
        Objects.equals(this.fillBelowTo, seriesOverride.fillBelowTo) &&
        Objects.equals(this.legend, seriesOverride.legend) &&
        Objects.equals(this.lines, seriesOverride.lines) &&
        Objects.equals(this.linewidth, seriesOverride.linewidth) &&
        Objects.equals(this.nullPointMode, seriesOverride.nullPointMode) &&
        Objects.equals(this.stack, seriesOverride.stack) &&
        Objects.equals(this.transform, seriesOverride.transform) &&
        Objects.equals(this.yaxis, seriesOverride.yaxis) &&
        Objects.equals(this.zindex, seriesOverride.zindex);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alias, bars, color, dashes, fill, fillBelowTo, legend, lines, linewidth, nullPointMode, stack, transform, yaxis, zindex);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SeriesOverride {\n");
    sb.append("    alias: ").append(toIndentedString(alias)).append("\n");
    sb.append("    bars: ").append(toIndentedString(bars)).append("\n");
    sb.append("    color: ").append(toIndentedString(color)).append("\n");
    sb.append("    dashes: ").append(toIndentedString(dashes)).append("\n");
    sb.append("    fill: ").append(toIndentedString(fill)).append("\n");
    sb.append("    fillBelowTo: ").append(toIndentedString(fillBelowTo)).append("\n");
    sb.append("    legend: ").append(toIndentedString(legend)).append("\n");
    sb.append("    lines: ").append(toIndentedString(lines)).append("\n");
    sb.append("    linewidth: ").append(toIndentedString(linewidth)).append("\n");
    sb.append("    nullPointMode: ").append(toIndentedString(nullPointMode)).append("\n");
    sb.append("    stack: ").append(toIndentedString(stack)).append("\n");
    sb.append("    transform: ").append(toIndentedString(transform)).append("\n");
    sb.append("    yaxis: ").append(toIndentedString(yaxis)).append("\n");
    sb.append("    zindex: ").append(toIndentedString(zindex)).append("\n");
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
    openapiFields.add("alias");
    openapiFields.add("bars");
    openapiFields.add("color");
    openapiFields.add("dashes");
    openapiFields.add("fill");
    openapiFields.add("fillBelowTo");
    openapiFields.add("legend");
    openapiFields.add("lines");
    openapiFields.add("linewidth");
    openapiFields.add("nullPointMode");
    openapiFields.add("stack");
    openapiFields.add("transform");
    openapiFields.add("yaxis");
    openapiFields.add("zindex");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SeriesOverride
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SeriesOverride.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SeriesOverride is not found in the empty JSON string", SeriesOverride.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SeriesOverride.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SeriesOverride` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("alias") != null && !jsonObj.get("alias").isJsonNull()) && !jsonObj.get("alias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alias").toString()));
      }
      if ((jsonObj.get("color") != null && !jsonObj.get("color").isJsonNull()) && !jsonObj.get("color").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `color` to be a primitive type in the JSON string but got `%s`", jsonObj.get("color").toString()));
      }
      if ((jsonObj.get("fillBelowTo") != null && !jsonObj.get("fillBelowTo").isJsonNull()) && !jsonObj.get("fillBelowTo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fillBelowTo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fillBelowTo").toString()));
      }
      if ((jsonObj.get("nullPointMode") != null && !jsonObj.get("nullPointMode").isJsonNull()) && !jsonObj.get("nullPointMode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nullPointMode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nullPointMode").toString()));
      }
      // validate the optional field `stack`
      if (jsonObj.get("stack") != null && !jsonObj.get("stack").isJsonNull()) {
        BoolString.validateJsonElement(jsonObj.get("stack"));
      }
      if ((jsonObj.get("transform") != null && !jsonObj.get("transform").isJsonNull()) && !jsonObj.get("transform").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transform` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transform").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SeriesOverride.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SeriesOverride' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SeriesOverride> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SeriesOverride.class));

       return (TypeAdapter<T>) new TypeAdapter<SeriesOverride>() {
           @Override
           public void write(JsonWriter out, SeriesOverride value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SeriesOverride read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SeriesOverride given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SeriesOverride
   * @throws IOException if the JSON string is invalid with respect to SeriesOverride
   */
  public static SeriesOverride fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SeriesOverride.class);
  }

  /**
   * Convert an instance of SeriesOverride to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

