/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.2
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
import java.util.UUID;

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
 * Entry associating a region to an image.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:01.424629-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImageRegionCreateEntry {
  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private Float height;

  public static final String SERIALIZED_NAME_IMAGE_ID = "imageId";
  @SerializedName(SERIALIZED_NAME_IMAGE_ID)
  private UUID imageId;

  public static final String SERIALIZED_NAME_LEFT = "left";
  @SerializedName(SERIALIZED_NAME_LEFT)
  private Float left;

  public static final String SERIALIZED_NAME_TAG_ID = "tagId";
  @SerializedName(SERIALIZED_NAME_TAG_ID)
  private UUID tagId;

  public static final String SERIALIZED_NAME_TOP = "top";
  @SerializedName(SERIALIZED_NAME_TOP)
  private Float top;

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private Float width;

  public ImageRegionCreateEntry() {
  }

  public ImageRegionCreateEntry height(Float height) {
    this.height = height;
    return this;
  }

  /**
   * Get height
   * @return height
   */
  @javax.annotation.Nullable
  public Float getHeight() {
    return height;
  }

  public void setHeight(Float height) {
    this.height = height;
  }


  public ImageRegionCreateEntry imageId(UUID imageId) {
    this.imageId = imageId;
    return this;
  }

  /**
   * Id of the image.
   * @return imageId
   */
  @javax.annotation.Nullable
  public UUID getImageId() {
    return imageId;
  }

  public void setImageId(UUID imageId) {
    this.imageId = imageId;
  }


  public ImageRegionCreateEntry left(Float left) {
    this.left = left;
    return this;
  }

  /**
   * Get left
   * @return left
   */
  @javax.annotation.Nullable
  public Float getLeft() {
    return left;
  }

  public void setLeft(Float left) {
    this.left = left;
  }


  public ImageRegionCreateEntry tagId(UUID tagId) {
    this.tagId = tagId;
    return this;
  }

  /**
   * Id of the tag associated with this region.
   * @return tagId
   */
  @javax.annotation.Nullable
  public UUID getTagId() {
    return tagId;
  }

  public void setTagId(UUID tagId) {
    this.tagId = tagId;
  }


  public ImageRegionCreateEntry top(Float top) {
    this.top = top;
    return this;
  }

  /**
   * Get top
   * @return top
   */
  @javax.annotation.Nullable
  public Float getTop() {
    return top;
  }

  public void setTop(Float top) {
    this.top = top;
  }


  public ImageRegionCreateEntry width(Float width) {
    this.width = width;
    return this;
  }

  /**
   * Get width
   * @return width
   */
  @javax.annotation.Nullable
  public Float getWidth() {
    return width;
  }

  public void setWidth(Float width) {
    this.width = width;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ImageRegionCreateEntry imageRegionCreateEntry = (ImageRegionCreateEntry) o;
    return Objects.equals(this.height, imageRegionCreateEntry.height) &&
        Objects.equals(this.imageId, imageRegionCreateEntry.imageId) &&
        Objects.equals(this.left, imageRegionCreateEntry.left) &&
        Objects.equals(this.tagId, imageRegionCreateEntry.tagId) &&
        Objects.equals(this.top, imageRegionCreateEntry.top) &&
        Objects.equals(this.width, imageRegionCreateEntry.width);
  }

  @Override
  public int hashCode() {
    return Objects.hash(height, imageId, left, tagId, top, width);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ImageRegionCreateEntry {\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    imageId: ").append(toIndentedString(imageId)).append("\n");
    sb.append("    left: ").append(toIndentedString(left)).append("\n");
    sb.append("    tagId: ").append(toIndentedString(tagId)).append("\n");
    sb.append("    top: ").append(toIndentedString(top)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
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
    openapiFields.add("height");
    openapiFields.add("imageId");
    openapiFields.add("left");
    openapiFields.add("tagId");
    openapiFields.add("top");
    openapiFields.add("width");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ImageRegionCreateEntry
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImageRegionCreateEntry.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImageRegionCreateEntry is not found in the empty JSON string", ImageRegionCreateEntry.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImageRegionCreateEntry.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImageRegionCreateEntry` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("imageId") != null && !jsonObj.get("imageId").isJsonNull()) && !jsonObj.get("imageId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `imageId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("imageId").toString()));
      }
      if ((jsonObj.get("tagId") != null && !jsonObj.get("tagId").isJsonNull()) && !jsonObj.get("tagId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tagId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tagId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImageRegionCreateEntry.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImageRegionCreateEntry' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImageRegionCreateEntry> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImageRegionCreateEntry.class));

       return (TypeAdapter<T>) new TypeAdapter<ImageRegionCreateEntry>() {
           @Override
           public void write(JsonWriter out, ImageRegionCreateEntry value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImageRegionCreateEntry read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImageRegionCreateEntry given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImageRegionCreateEntry
   * @throws IOException if the JSON string is invalid with respect to ImageRegionCreateEntry
   */
  public static ImageRegionCreateEntry fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImageRegionCreateEntry.class);
  }

  /**
   * Convert an instance of ImageRegionCreateEntry to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

