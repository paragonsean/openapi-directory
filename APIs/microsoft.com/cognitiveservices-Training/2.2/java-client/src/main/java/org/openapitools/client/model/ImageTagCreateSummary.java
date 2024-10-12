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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.ImageTagCreateEntry;
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
 * ImageTagCreateSummary
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:01.424629-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImageTagCreateSummary {
  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private List<ImageTagCreateEntry> created;

  public static final String SERIALIZED_NAME_DUPLICATED = "duplicated";
  @SerializedName(SERIALIZED_NAME_DUPLICATED)
  private List<ImageTagCreateEntry> duplicated;

  public static final String SERIALIZED_NAME_EXCEEDED = "exceeded";
  @SerializedName(SERIALIZED_NAME_EXCEEDED)
  private List<ImageTagCreateEntry> exceeded;

  public ImageTagCreateSummary() {
  }

  public ImageTagCreateSummary created(List<ImageTagCreateEntry> created) {
    this.created = created;
    return this;
  }

  public ImageTagCreateSummary addCreatedItem(ImageTagCreateEntry createdItem) {
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
  public List<ImageTagCreateEntry> getCreated() {
    return created;
  }

  public void setCreated(List<ImageTagCreateEntry> created) {
    this.created = created;
  }


  public ImageTagCreateSummary duplicated(List<ImageTagCreateEntry> duplicated) {
    this.duplicated = duplicated;
    return this;
  }

  public ImageTagCreateSummary addDuplicatedItem(ImageTagCreateEntry duplicatedItem) {
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
  public List<ImageTagCreateEntry> getDuplicated() {
    return duplicated;
  }

  public void setDuplicated(List<ImageTagCreateEntry> duplicated) {
    this.duplicated = duplicated;
  }


  public ImageTagCreateSummary exceeded(List<ImageTagCreateEntry> exceeded) {
    this.exceeded = exceeded;
    return this;
  }

  public ImageTagCreateSummary addExceededItem(ImageTagCreateEntry exceededItem) {
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
  public List<ImageTagCreateEntry> getExceeded() {
    return exceeded;
  }

  public void setExceeded(List<ImageTagCreateEntry> exceeded) {
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
    ImageTagCreateSummary imageTagCreateSummary = (ImageTagCreateSummary) o;
    return Objects.equals(this.created, imageTagCreateSummary.created) &&
        Objects.equals(this.duplicated, imageTagCreateSummary.duplicated) &&
        Objects.equals(this.exceeded, imageTagCreateSummary.exceeded);
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
    sb.append("class ImageTagCreateSummary {\n");
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
   * @throws IOException if the JSON Element is invalid with respect to ImageTagCreateSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImageTagCreateSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImageTagCreateSummary is not found in the empty JSON string", ImageTagCreateSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImageTagCreateSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImageTagCreateSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            ImageTagCreateEntry.validateJsonElement(jsonArraycreated.get(i));
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
            ImageTagCreateEntry.validateJsonElement(jsonArrayduplicated.get(i));
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
            ImageTagCreateEntry.validateJsonElement(jsonArrayexceeded.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImageTagCreateSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImageTagCreateSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImageTagCreateSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImageTagCreateSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<ImageTagCreateSummary>() {
           @Override
           public void write(JsonWriter out, ImageTagCreateSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImageTagCreateSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImageTagCreateSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImageTagCreateSummary
   * @throws IOException if the JSON string is invalid with respect to ImageTagCreateSummary
   */
  public static ImageTagCreateSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImageTagCreateSummary.class);
  }

  /**
   * Convert an instance of ImageTagCreateSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

