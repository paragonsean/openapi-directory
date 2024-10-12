/*
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
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
 * PhotoEditability
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:49.490227-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PhotoEditability {
  public static final String SERIALIZED_NAME_CANADDMETA = "canaddmeta";
  @SerializedName(SERIALIZED_NAME_CANADDMETA)
  private Boolean canaddmeta;

  public static final String SERIALIZED_NAME_CANCOMMENT = "cancomment";
  @SerializedName(SERIALIZED_NAME_CANCOMMENT)
  private Boolean cancomment;

  public PhotoEditability() {
  }

  public PhotoEditability canaddmeta(Boolean canaddmeta) {
    this.canaddmeta = canaddmeta;
    return this;
  }

  /**
   * Get canaddmeta
   * @return canaddmeta
   */
  @javax.annotation.Nullable
  public Boolean getCanaddmeta() {
    return canaddmeta;
  }

  public void setCanaddmeta(Boolean canaddmeta) {
    this.canaddmeta = canaddmeta;
  }


  public PhotoEditability cancomment(Boolean cancomment) {
    this.cancomment = cancomment;
    return this;
  }

  /**
   * Get cancomment
   * @return cancomment
   */
  @javax.annotation.Nullable
  public Boolean getCancomment() {
    return cancomment;
  }

  public void setCancomment(Boolean cancomment) {
    this.cancomment = cancomment;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PhotoEditability photoEditability = (PhotoEditability) o;
    return Objects.equals(this.canaddmeta, photoEditability.canaddmeta) &&
        Objects.equals(this.cancomment, photoEditability.cancomment);
  }

  @Override
  public int hashCode() {
    return Objects.hash(canaddmeta, cancomment);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PhotoEditability {\n");
    sb.append("    canaddmeta: ").append(toIndentedString(canaddmeta)).append("\n");
    sb.append("    cancomment: ").append(toIndentedString(cancomment)).append("\n");
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
    openapiFields.add("canaddmeta");
    openapiFields.add("cancomment");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PhotoEditability
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PhotoEditability.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PhotoEditability is not found in the empty JSON string", PhotoEditability.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PhotoEditability.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PhotoEditability` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PhotoEditability.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PhotoEditability' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PhotoEditability> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PhotoEditability.class));

       return (TypeAdapter<T>) new TypeAdapter<PhotoEditability>() {
           @Override
           public void write(JsonWriter out, PhotoEditability value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PhotoEditability read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PhotoEditability given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PhotoEditability
   * @throws IOException if the JSON string is invalid with respect to PhotoEditability
   */
  public static PhotoEditability fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PhotoEditability.class);
  }

  /**
   * Convert an instance of PhotoEditability to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

