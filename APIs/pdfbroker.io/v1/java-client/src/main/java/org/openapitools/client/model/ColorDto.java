/*
 * PdfBroker.io API
 * PdfBroker.io is an api for creating pdf files from Xsl-Fo or Html and other useful pdf utilities.
 *
 * The version of the OpenAPI document: v1
 * Contact: support@pdfbroker.io
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
 * Set color
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:46.869013-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ColorDto {
  public static final String SERIALIZED_NAME_B = "b";
  @SerializedName(SERIALIZED_NAME_B)
  private Integer b;

  public static final String SERIALIZED_NAME_G = "g";
  @SerializedName(SERIALIZED_NAME_G)
  private Integer g;

  public static final String SERIALIZED_NAME_R = "r";
  @SerializedName(SERIALIZED_NAME_R)
  private Integer r;

  public ColorDto() {
  }

  public ColorDto b(Integer b) {
    this.b = b;
    return this;
  }

  /**
   * Get or sets B value of RGB color
   * minimum: 0
   * maximum: 255
   * @return b
   */
  @javax.annotation.Nullable
  public Integer getB() {
    return b;
  }

  public void setB(Integer b) {
    this.b = b;
  }


  public ColorDto g(Integer g) {
    this.g = g;
    return this;
  }

  /**
   * Get or sets G value of RGB color
   * minimum: 0
   * maximum: 255
   * @return g
   */
  @javax.annotation.Nullable
  public Integer getG() {
    return g;
  }

  public void setG(Integer g) {
    this.g = g;
  }


  public ColorDto r(Integer r) {
    this.r = r;
    return this;
  }

  /**
   * Get or sets R value of RGB color
   * minimum: 0
   * maximum: 255
   * @return r
   */
  @javax.annotation.Nullable
  public Integer getR() {
    return r;
  }

  public void setR(Integer r) {
    this.r = r;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ColorDto colorDto = (ColorDto) o;
    return Objects.equals(this.b, colorDto.b) &&
        Objects.equals(this.g, colorDto.g) &&
        Objects.equals(this.r, colorDto.r);
  }

  @Override
  public int hashCode() {
    return Objects.hash(b, g, r);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ColorDto {\n");
    sb.append("    b: ").append(toIndentedString(b)).append("\n");
    sb.append("    g: ").append(toIndentedString(g)).append("\n");
    sb.append("    r: ").append(toIndentedString(r)).append("\n");
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
    openapiFields.add("b");
    openapiFields.add("g");
    openapiFields.add("r");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ColorDto
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ColorDto.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ColorDto is not found in the empty JSON string", ColorDto.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ColorDto.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ColorDto` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ColorDto.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ColorDto' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ColorDto> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ColorDto.class));

       return (TypeAdapter<T>) new TypeAdapter<ColorDto>() {
           @Override
           public void write(JsonWriter out, ColorDto value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ColorDto read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ColorDto given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ColorDto
   * @throws IOException if the JSON string is invalid with respect to ColorDto
   */
  public static ColorDto fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ColorDto.class);
  }

  /**
   * Convert an instance of ColorDto to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

