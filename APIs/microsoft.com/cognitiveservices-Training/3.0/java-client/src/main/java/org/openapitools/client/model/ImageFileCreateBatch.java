/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.openapitools.client.model.ImageFileCreateEntry;

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
 * ImageFileCreateBatch
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:14.859299-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImageFileCreateBatch {
  public static final String SERIALIZED_NAME_IMAGES = "images";
  @SerializedName(SERIALIZED_NAME_IMAGES)
  private List<ImageFileCreateEntry> images = new ArrayList<>();

  public static final String SERIALIZED_NAME_TAG_IDS = "tagIds";
  @SerializedName(SERIALIZED_NAME_TAG_IDS)
  private List<UUID> tagIds = new ArrayList<>();

  public ImageFileCreateBatch() {
  }

  public ImageFileCreateBatch images(List<ImageFileCreateEntry> images) {
    this.images = images;
    return this;
  }

  public ImageFileCreateBatch addImagesItem(ImageFileCreateEntry imagesItem) {
    if (this.images == null) {
      this.images = new ArrayList<>();
    }
    this.images.add(imagesItem);
    return this;
  }

  /**
   * Get images
   * @return images
   */
  @javax.annotation.Nullable
  public List<ImageFileCreateEntry> getImages() {
    return images;
  }

  public void setImages(List<ImageFileCreateEntry> images) {
    this.images = images;
  }


  public ImageFileCreateBatch tagIds(List<UUID> tagIds) {
    this.tagIds = tagIds;
    return this;
  }

  public ImageFileCreateBatch addTagIdsItem(UUID tagIdsItem) {
    if (this.tagIds == null) {
      this.tagIds = new ArrayList<>();
    }
    this.tagIds.add(tagIdsItem);
    return this;
  }

  /**
   * Get tagIds
   * @return tagIds
   */
  @javax.annotation.Nullable
  public List<UUID> getTagIds() {
    return tagIds;
  }

  public void setTagIds(List<UUID> tagIds) {
    this.tagIds = tagIds;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ImageFileCreateBatch imageFileCreateBatch = (ImageFileCreateBatch) o;
    return Objects.equals(this.images, imageFileCreateBatch.images) &&
        Objects.equals(this.tagIds, imageFileCreateBatch.tagIds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(images, tagIds);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ImageFileCreateBatch {\n");
    sb.append("    images: ").append(toIndentedString(images)).append("\n");
    sb.append("    tagIds: ").append(toIndentedString(tagIds)).append("\n");
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
    openapiFields.add("images");
    openapiFields.add("tagIds");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ImageFileCreateBatch
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImageFileCreateBatch.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImageFileCreateBatch is not found in the empty JSON string", ImageFileCreateBatch.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImageFileCreateBatch.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImageFileCreateBatch` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("images") != null && !jsonObj.get("images").isJsonNull()) {
        JsonArray jsonArrayimages = jsonObj.getAsJsonArray("images");
        if (jsonArrayimages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("images").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `images` to be an array in the JSON string but got `%s`", jsonObj.get("images").toString()));
          }

          // validate the optional field `images` (array)
          for (int i = 0; i < jsonArrayimages.size(); i++) {
            ImageFileCreateEntry.validateJsonElement(jsonArrayimages.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tagIds") != null && !jsonObj.get("tagIds").isJsonNull() && !jsonObj.get("tagIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tagIds` to be an array in the JSON string but got `%s`", jsonObj.get("tagIds").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImageFileCreateBatch.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImageFileCreateBatch' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImageFileCreateBatch> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImageFileCreateBatch.class));

       return (TypeAdapter<T>) new TypeAdapter<ImageFileCreateBatch>() {
           @Override
           public void write(JsonWriter out, ImageFileCreateBatch value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImageFileCreateBatch read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImageFileCreateBatch given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImageFileCreateBatch
   * @throws IOException if the JSON string is invalid with respect to ImageFileCreateBatch
   */
  public static ImageFileCreateBatch fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImageFileCreateBatch.class);
  }

  /**
   * Convert an instance of ImageFileCreateBatch to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

