/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.openapitools.client.model.ImageRegion;
import org.openapitools.client.model.ImageTag;
import org.openapitools.client.model.Prediction;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * Image performance model.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:13.015357-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImagePerformance {
  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private Integer height;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IMAGE_URI = "imageUri";
  @SerializedName(SERIALIZED_NAME_IMAGE_URI)
  private String imageUri;

  public static final String SERIALIZED_NAME_PREDICTIONS = "predictions";
  @SerializedName(SERIALIZED_NAME_PREDICTIONS)
  private List<Prediction> predictions;

  public static final String SERIALIZED_NAME_REGIONS = "regions";
  @SerializedName(SERIALIZED_NAME_REGIONS)
  private List<ImageRegion> regions;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<ImageTag> tags;

  public static final String SERIALIZED_NAME_THUMBNAIL_URI = "thumbnailUri";
  @SerializedName(SERIALIZED_NAME_THUMBNAIL_URI)
  private String thumbnailUri;

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private Integer width;

  public ImagePerformance() {
  }

  public ImagePerformance(
     OffsetDateTime created, 
     Integer height, 
     UUID id, 
     String imageUri, 
     List<Prediction> predictions, 
     List<ImageRegion> regions, 
     List<ImageTag> tags, 
     String thumbnailUri, 
     Integer width
  ) {
    this();
    this.created = created;
    this.height = height;
    this.id = id;
    this.imageUri = imageUri;
    this.predictions = predictions;
    this.regions = regions;
    this.tags = tags;
    this.thumbnailUri = thumbnailUri;
    this.width = width;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }



  /**
   * Get height
   * @return height
   */
  @javax.annotation.Nullable
  public Integer getHeight() {
    return height;
  }



  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }



  /**
   * Get imageUri
   * @return imageUri
   */
  @javax.annotation.Nullable
  public String getImageUri() {
    return imageUri;
  }



  /**
   * Get predictions
   * @return predictions
   */
  @javax.annotation.Nullable
  public List<Prediction> getPredictions() {
    return predictions;
  }



  /**
   * Get regions
   * @return regions
   */
  @javax.annotation.Nullable
  public List<ImageRegion> getRegions() {
    return regions;
  }



  /**
   * Get tags
   * @return tags
   */
  @javax.annotation.Nullable
  public List<ImageTag> getTags() {
    return tags;
  }



  /**
   * Get thumbnailUri
   * @return thumbnailUri
   */
  @javax.annotation.Nullable
  public String getThumbnailUri() {
    return thumbnailUri;
  }



  /**
   * Get width
   * @return width
   */
  @javax.annotation.Nullable
  public Integer getWidth() {
    return width;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ImagePerformance imagePerformance = (ImagePerformance) o;
    return Objects.equals(this.created, imagePerformance.created) &&
        Objects.equals(this.height, imagePerformance.height) &&
        Objects.equals(this.id, imagePerformance.id) &&
        Objects.equals(this.imageUri, imagePerformance.imageUri) &&
        Objects.equals(this.predictions, imagePerformance.predictions) &&
        Objects.equals(this.regions, imagePerformance.regions) &&
        Objects.equals(this.tags, imagePerformance.tags) &&
        Objects.equals(this.thumbnailUri, imagePerformance.thumbnailUri) &&
        Objects.equals(this.width, imagePerformance.width);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(created, height, id, imageUri, predictions, regions, tags, thumbnailUri, width);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ImagePerformance {\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    imageUri: ").append(toIndentedString(imageUri)).append("\n");
    sb.append("    predictions: ").append(toIndentedString(predictions)).append("\n");
    sb.append("    regions: ").append(toIndentedString(regions)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    thumbnailUri: ").append(toIndentedString(thumbnailUri)).append("\n");
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
    openapiFields.add("created");
    openapiFields.add("height");
    openapiFields.add("id");
    openapiFields.add("imageUri");
    openapiFields.add("predictions");
    openapiFields.add("regions");
    openapiFields.add("tags");
    openapiFields.add("thumbnailUri");
    openapiFields.add("width");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ImagePerformance
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImagePerformance.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImagePerformance is not found in the empty JSON string", ImagePerformance.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImagePerformance.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImagePerformance` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("imageUri") != null && !jsonObj.get("imageUri").isJsonNull()) && !jsonObj.get("imageUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `imageUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("imageUri").toString()));
      }
      if (jsonObj.get("predictions") != null && !jsonObj.get("predictions").isJsonNull()) {
        JsonArray jsonArraypredictions = jsonObj.getAsJsonArray("predictions");
        if (jsonArraypredictions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("predictions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `predictions` to be an array in the JSON string but got `%s`", jsonObj.get("predictions").toString()));
          }

          // validate the optional field `predictions` (array)
          for (int i = 0; i < jsonArraypredictions.size(); i++) {
            Prediction.validateJsonElement(jsonArraypredictions.get(i));
          };
        }
      }
      if (jsonObj.get("regions") != null && !jsonObj.get("regions").isJsonNull()) {
        JsonArray jsonArrayregions = jsonObj.getAsJsonArray("regions");
        if (jsonArrayregions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("regions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `regions` to be an array in the JSON string but got `%s`", jsonObj.get("regions").toString()));
          }

          // validate the optional field `regions` (array)
          for (int i = 0; i < jsonArrayregions.size(); i++) {
            ImageRegion.validateJsonElement(jsonArrayregions.get(i));
          };
        }
      }
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull()) {
        JsonArray jsonArraytags = jsonObj.getAsJsonArray("tags");
        if (jsonArraytags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
          }

          // validate the optional field `tags` (array)
          for (int i = 0; i < jsonArraytags.size(); i++) {
            ImageTag.validateJsonElement(jsonArraytags.get(i));
          };
        }
      }
      if ((jsonObj.get("thumbnailUri") != null && !jsonObj.get("thumbnailUri").isJsonNull()) && !jsonObj.get("thumbnailUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `thumbnailUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("thumbnailUri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImagePerformance.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImagePerformance' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImagePerformance> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImagePerformance.class));

       return (TypeAdapter<T>) new TypeAdapter<ImagePerformance>() {
           @Override
           public void write(JsonWriter out, ImagePerformance value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImagePerformance read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImagePerformance given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImagePerformance
   * @throws IOException if the JSON string is invalid with respect to ImagePerformance
   */
  public static ImagePerformance fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImagePerformance.class);
  }

  /**
   * Convert an instance of ImagePerformance to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

