/*
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
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
import org.openapitools.client.model.ImageObject;
import org.openapitools.client.model.StructuredValue;

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
 * Defines a region of an image. The region is defined by the coordinates of the top, left corner and bottom, right corner of the region. The coordinates are fractional values of the original image&#39;s width and height in the range 0.0 through 1.0.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:10:59.700770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NormalizedRectangle extends StructuredValue {
  public static final String SERIALIZED_NAME_BOTTOM = "bottom";
  @SerializedName(SERIALIZED_NAME_BOTTOM)
  private Float bottom;

  public static final String SERIALIZED_NAME_LEFT = "left";
  @SerializedName(SERIALIZED_NAME_LEFT)
  private Float left;

  public static final String SERIALIZED_NAME_RIGHT = "right";
  @SerializedName(SERIALIZED_NAME_RIGHT)
  private Float right;

  public static final String SERIALIZED_NAME_TOP = "top";
  @SerializedName(SERIALIZED_NAME_TOP)
  private Float top;

  public NormalizedRectangle() {
    this.type = this.getClass().getSimpleName();
  }

  public NormalizedRectangle(
     String alternateName, 
     String bingId, 
     String description, 
     String name, 
     String url, 
     String readLink, 
     String webSearchUrl, 
     String id
  ) {
    this();
    this.alternateName = alternateName;
    this.bingId = bingId;
    this.description = description;
    this.name = name;
    this.url = url;
    this.readLink = readLink;
    this.webSearchUrl = webSearchUrl;
    this.id = id;
  }

  public NormalizedRectangle bottom(Float bottom) {
    this.bottom = bottom;
    return this;
  }

  /**
   * The bottom coordinate
   * @return bottom
   */
  @javax.annotation.Nonnull
  public Float getBottom() {
    return bottom;
  }

  public void setBottom(Float bottom) {
    this.bottom = bottom;
  }


  public NormalizedRectangle left(Float left) {
    this.left = left;
    return this;
  }

  /**
   * The left coordinate.
   * @return left
   */
  @javax.annotation.Nonnull
  public Float getLeft() {
    return left;
  }

  public void setLeft(Float left) {
    this.left = left;
  }


  public NormalizedRectangle right(Float right) {
    this.right = right;
    return this;
  }

  /**
   * The right coordinate
   * @return right
   */
  @javax.annotation.Nonnull
  public Float getRight() {
    return right;
  }

  public void setRight(Float right) {
    this.right = right;
  }


  public NormalizedRectangle top(Float top) {
    this.top = top;
    return this;
  }

  /**
   * The top coordinate
   * @return top
   */
  @javax.annotation.Nonnull
  public Float getTop() {
    return top;
  }

  public void setTop(Float top) {
    this.top = top;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NormalizedRectangle normalizedRectangle = (NormalizedRectangle) o;
    return Objects.equals(this.bottom, normalizedRectangle.bottom) &&
        Objects.equals(this.left, normalizedRectangle.left) &&
        Objects.equals(this.right, normalizedRectangle.right) &&
        Objects.equals(this.top, normalizedRectangle.top) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bottom, left, right, top, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NormalizedRectangle {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    bottom: ").append(toIndentedString(bottom)).append("\n");
    sb.append("    left: ").append(toIndentedString(left)).append("\n");
    sb.append("    right: ").append(toIndentedString(right)).append("\n");
    sb.append("    top: ").append(toIndentedString(top)).append("\n");
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
    openapiFields.add("alternateName");
    openapiFields.add("bingId");
    openapiFields.add("description");
    openapiFields.add("image");
    openapiFields.add("name");
    openapiFields.add("url");
    openapiFields.add("readLink");
    openapiFields.add("webSearchUrl");
    openapiFields.add("id");
    openapiFields.add("_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("bottom");
    openapiRequiredFields.add("left");
    openapiRequiredFields.add("right");
    openapiRequiredFields.add("top");
    openapiRequiredFields.add("_type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NormalizedRectangle
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NormalizedRectangle.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NormalizedRectangle is not found in the empty JSON string", NormalizedRectangle.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NormalizedRectangle.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NormalizedRectangle` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : NormalizedRectangle.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NormalizedRectangle.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NormalizedRectangle' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NormalizedRectangle> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NormalizedRectangle.class));

       return (TypeAdapter<T>) new TypeAdapter<NormalizedRectangle>() {
           @Override
           public void write(JsonWriter out, NormalizedRectangle value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NormalizedRectangle read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NormalizedRectangle given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NormalizedRectangle
   * @throws IOException if the JSON string is invalid with respect to NormalizedRectangle
   */
  public static NormalizedRectangle fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NormalizedRectangle.class);
  }

  /**
   * Convert an instance of NormalizedRectangle to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

