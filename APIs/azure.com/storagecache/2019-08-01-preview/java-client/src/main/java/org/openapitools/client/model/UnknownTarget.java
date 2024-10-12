/*
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
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
 * Storage container for use as a Unknown StorageTarget.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:44:28.365652-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UnknownTarget {
  public static final String SERIALIZED_NAME_UNKNOWN_MAP = "unknownMap";
  @SerializedName(SERIALIZED_NAME_UNKNOWN_MAP)
  private Map<String, String> unknownMap = new HashMap<>();

  public UnknownTarget() {
  }

  public UnknownTarget unknownMap(Map<String, String> unknownMap) {
    this.unknownMap = unknownMap;
    return this;
  }

  public UnknownTarget putUnknownMapItem(String key, String unknownMapItem) {
    if (this.unknownMap == null) {
      this.unknownMap = new HashMap<>();
    }
    this.unknownMap.put(key, unknownMapItem);
    return this;
  }

  /**
   * Properties of an unknown type of StorageTarget
   * @return unknownMap
   */
  @javax.annotation.Nullable
  public Map<String, String> getUnknownMap() {
    return unknownMap;
  }

  public void setUnknownMap(Map<String, String> unknownMap) {
    this.unknownMap = unknownMap;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UnknownTarget unknownTarget = (UnknownTarget) o;
    return Objects.equals(this.unknownMap, unknownTarget.unknownMap);
  }

  @Override
  public int hashCode() {
    return Objects.hash(unknownMap);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UnknownTarget {\n");
    sb.append("    unknownMap: ").append(toIndentedString(unknownMap)).append("\n");
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
    openapiFields.add("unknownMap");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UnknownTarget
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UnknownTarget.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UnknownTarget is not found in the empty JSON string", UnknownTarget.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UnknownTarget.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UnknownTarget` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UnknownTarget.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UnknownTarget' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UnknownTarget> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UnknownTarget.class));

       return (TypeAdapter<T>) new TypeAdapter<UnknownTarget>() {
           @Override
           public void write(JsonWriter out, UnknownTarget value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UnknownTarget read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UnknownTarget given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UnknownTarget
   * @throws IOException if the JSON string is invalid with respect to UnknownTarget
   */
  public static UnknownTarget fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UnknownTarget.class);
  }

  /**
   * Convert an instance of UnknownTarget to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

