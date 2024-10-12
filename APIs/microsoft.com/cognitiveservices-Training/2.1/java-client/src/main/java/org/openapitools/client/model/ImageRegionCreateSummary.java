/*
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
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
import org.openapitools.client.model.ImageRegionCreateEntry;
import org.openapitools.client.model.ImageRegionCreateResult;
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
 * ImageRegionCreateSummary
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:10.847797-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImageRegionCreateSummary {
  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private List<ImageRegionCreateResult> created;

  public static final String SERIALIZED_NAME_DUPLICATED = "duplicated";
  @SerializedName(SERIALIZED_NAME_DUPLICATED)
  private List<ImageRegionCreateEntry> duplicated;

  public static final String SERIALIZED_NAME_EXCEEDED = "exceeded";
  @SerializedName(SERIALIZED_NAME_EXCEEDED)
  private List<ImageRegionCreateEntry> exceeded;

  public ImageRegionCreateSummary() {
  }

  public ImageRegionCreateSummary created(List<ImageRegionCreateResult> created) {
    this.created = created;
    return this;
  }

  public ImageRegionCreateSummary addCreatedItem(ImageRegionCreateResult createdItem) {
    if (this.created == null) {
      this.created = new ArrayList<>();
    }
    this.created.add(createdItem);
    return this;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public List<ImageRegionCreateResult> getCreated() {
    return created;
  }

  public void setCreated(List<ImageRegionCreateResult> created) {
    this.created = created;
  }


  public ImageRegionCreateSummary duplicated(List<ImageRegionCreateEntry> duplicated) {
    this.duplicated = duplicated;
    return this;
  }

  public ImageRegionCreateSummary addDuplicatedItem(ImageRegionCreateEntry duplicatedItem) {
    if (this.duplicated == null) {
      this.duplicated = new ArrayList<>();
    }
    this.duplicated.add(duplicatedItem);
    return this;
  }

  /**
   * Get duplicated
   * @return duplicated
   */
  @javax.annotation.Nullable
  public List<ImageRegionCreateEntry> getDuplicated() {
    return duplicated;
  }

  public void setDuplicated(List<ImageRegionCreateEntry> duplicated) {
    this.duplicated = duplicated;
  }


  public ImageRegionCreateSummary exceeded(List<ImageRegionCreateEntry> exceeded) {
    this.exceeded = exceeded;
    return this;
  }

  public ImageRegionCreateSummary addExceededItem(ImageRegionCreateEntry exceededItem) {
    if (this.exceeded == null) {
      this.exceeded = new ArrayList<>();
    }
    this.exceeded.add(exceededItem);
    return this;
  }

  /**
   * Get exceeded
   * @return exceeded
   */
  @javax.annotation.Nullable
  public List<ImageRegionCreateEntry> getExceeded() {
    return exceeded;
  }

  public void setExceeded(List<ImageRegionCreateEntry> exceeded) {
    this.exceeded = exceeded;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ImageRegionCreateSummary imageRegionCreateSummary = (ImageRegionCreateSummary) o;
    return Objects.equals(this.created, imageRegionCreateSummary.created) &&
        Objects.equals(this.duplicated, imageRegionCreateSummary.duplicated) &&
        Objects.equals(this.exceeded, imageRegionCreateSummary.exceeded);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(created, duplicated, exceeded);
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
    sb.append("class ImageRegionCreateSummary {\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    duplicated: ").append(toIndentedString(duplicated)).append("\n");
    sb.append("    exceeded: ").append(toIndentedString(exceeded)).append("\n");
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
    openapiFields.add("duplicated");
    openapiFields.add("exceeded");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ImageRegionCreateSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImageRegionCreateSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImageRegionCreateSummary is not found in the empty JSON string", ImageRegionCreateSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImageRegionCreateSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImageRegionCreateSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) {
        JsonArray jsonArraycreated = jsonObj.getAsJsonArray("created");
        if (jsonArraycreated != null) {
          // ensure the json data is an array
          if (!jsonObj.get("created").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `created` to be an array in the JSON string but got `%s`", jsonObj.get("created").toString()));
          }

          // validate the optional field `created` (array)
          for (int i = 0; i < jsonArraycreated.size(); i++) {
            ImageRegionCreateResult.validateJsonElement(jsonArraycreated.get(i));
          };
        }
      }
      if (jsonObj.get("duplicated") != null && !jsonObj.get("duplicated").isJsonNull()) {
        JsonArray jsonArrayduplicated = jsonObj.getAsJsonArray("duplicated");
        if (jsonArrayduplicated != null) {
          // ensure the json data is an array
          if (!jsonObj.get("duplicated").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `duplicated` to be an array in the JSON string but got `%s`", jsonObj.get("duplicated").toString()));
          }

          // validate the optional field `duplicated` (array)
          for (int i = 0; i < jsonArrayduplicated.size(); i++) {
            ImageRegionCreateEntry.validateJsonElement(jsonArrayduplicated.get(i));
          };
        }
      }
      if (jsonObj.get("exceeded") != null && !jsonObj.get("exceeded").isJsonNull()) {
        JsonArray jsonArrayexceeded = jsonObj.getAsJsonArray("exceeded");
        if (jsonArrayexceeded != null) {
          // ensure the json data is an array
          if (!jsonObj.get("exceeded").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `exceeded` to be an array in the JSON string but got `%s`", jsonObj.get("exceeded").toString()));
          }

          // validate the optional field `exceeded` (array)
          for (int i = 0; i < jsonArrayexceeded.size(); i++) {
            ImageRegionCreateEntry.validateJsonElement(jsonArrayexceeded.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImageRegionCreateSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImageRegionCreateSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImageRegionCreateSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImageRegionCreateSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<ImageRegionCreateSummary>() {
           @Override
           public void write(JsonWriter out, ImageRegionCreateSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImageRegionCreateSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImageRegionCreateSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImageRegionCreateSummary
   * @throws IOException if the JSON string is invalid with respect to ImageRegionCreateSummary
   */
  public static ImageRegionCreateSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImageRegionCreateSummary.class);
  }

  /**
   * Convert an instance of ImageRegionCreateSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

