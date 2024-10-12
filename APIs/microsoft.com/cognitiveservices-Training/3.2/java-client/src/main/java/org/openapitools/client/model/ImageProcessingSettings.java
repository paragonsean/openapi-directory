/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
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
import java.util.HashMap;
import java.util.Map;
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
 * Represents image preprocessing settings used by image augmentation.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:05.173515-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ImageProcessingSettings {
  public static final String SERIALIZED_NAME_AUGMENTATION_METHODS = "augmentationMethods";
  @SerializedName(SERIALIZED_NAME_AUGMENTATION_METHODS)
  private Map<String, Boolean> augmentationMethods;

  public ImageProcessingSettings() {
  }

  public ImageProcessingSettings augmentationMethods(Map<String, Boolean> augmentationMethods) {
    this.augmentationMethods = augmentationMethods;
    return this;
  }

  public ImageProcessingSettings putAugmentationMethodsItem(String key, Boolean augmentationMethodsItem) {
    if (this.augmentationMethods == null) {
      this.augmentationMethods = new HashMap<>();
    }
    this.augmentationMethods.put(key, augmentationMethodsItem);
    return this;
  }

  /**
   * Gets or sets enabled image transforms. The key corresponds to the transform name. If value is set to true, then correspondent transform is enabled. Otherwise this transform will not be used.  Augmentation will be uniformly distributed among enabled transforms.
   * @return augmentationMethods
   */
  @javax.annotation.Nullable
  public Map<String, Boolean> getAugmentationMethods() {
    return augmentationMethods;
  }

  public void setAugmentationMethods(Map<String, Boolean> augmentationMethods) {
    this.augmentationMethods = augmentationMethods;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ImageProcessingSettings imageProcessingSettings = (ImageProcessingSettings) o;
    return Objects.equals(this.augmentationMethods, imageProcessingSettings.augmentationMethods);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(augmentationMethods);
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
    sb.append("class ImageProcessingSettings {\n");
    sb.append("    augmentationMethods: ").append(toIndentedString(augmentationMethods)).append("\n");
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
    openapiFields.add("augmentationMethods");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ImageProcessingSettings
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ImageProcessingSettings.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ImageProcessingSettings is not found in the empty JSON string", ImageProcessingSettings.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ImageProcessingSettings.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ImageProcessingSettings` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ImageProcessingSettings.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ImageProcessingSettings' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ImageProcessingSettings> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ImageProcessingSettings.class));

       return (TypeAdapter<T>) new TypeAdapter<ImageProcessingSettings>() {
           @Override
           public void write(JsonWriter out, ImageProcessingSettings value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ImageProcessingSettings read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ImageProcessingSettings given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ImageProcessingSettings
   * @throws IOException if the JSON string is invalid with respect to ImageProcessingSettings
   */
  public static ImageProcessingSettings fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ImageProcessingSettings.class);
  }

  /**
   * Convert an instance of ImageProcessingSettings to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

