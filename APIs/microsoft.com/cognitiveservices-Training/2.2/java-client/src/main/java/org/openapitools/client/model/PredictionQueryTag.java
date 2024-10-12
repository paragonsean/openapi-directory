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
 * PredictionQueryTag
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:01.424629-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PredictionQueryTag {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_MAX_THRESHOLD = "maxThreshold";
  @SerializedName(SERIALIZED_NAME_MAX_THRESHOLD)
  private Float maxThreshold;

  public static final String SERIALIZED_NAME_MIN_THRESHOLD = "minThreshold";
  @SerializedName(SERIALIZED_NAME_MIN_THRESHOLD)
  private Float minThreshold;

  public PredictionQueryTag() {
  }

  public PredictionQueryTag(
     UUID id, 
     Float maxThreshold, 
     Float minThreshold
  ) {
    this();
    this.id = id;
    this.maxThreshold = maxThreshold;
    this.minThreshold = minThreshold;
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
   * Get maxThreshold
   * @return maxThreshold
   */
  @javax.annotation.Nullable
  public Float getMaxThreshold() {
    return maxThreshold;
  }



  /**
   * Get minThreshold
   * @return minThreshold
   */
  @javax.annotation.Nullable
  public Float getMinThreshold() {
    return minThreshold;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PredictionQueryTag predictionQueryTag = (PredictionQueryTag) o;
    return Objects.equals(this.id, predictionQueryTag.id) &&
        Objects.equals(this.maxThreshold, predictionQueryTag.maxThreshold) &&
        Objects.equals(this.minThreshold, predictionQueryTag.minThreshold);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, maxThreshold, minThreshold);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PredictionQueryTag {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    maxThreshold: ").append(toIndentedString(maxThreshold)).append("\n");
    sb.append("    minThreshold: ").append(toIndentedString(minThreshold)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("maxThreshold");
    openapiFields.add("minThreshold");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PredictionQueryTag
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PredictionQueryTag.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PredictionQueryTag is not found in the empty JSON string", PredictionQueryTag.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PredictionQueryTag.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PredictionQueryTag` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PredictionQueryTag.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PredictionQueryTag' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PredictionQueryTag> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PredictionQueryTag.class));

       return (TypeAdapter<T>) new TypeAdapter<PredictionQueryTag>() {
           @Override
           public void write(JsonWriter out, PredictionQueryTag value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PredictionQueryTag read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PredictionQueryTag given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PredictionQueryTag
   * @throws IOException if the JSON string is invalid with respect to PredictionQueryTag
   */
  public static PredictionQueryTag fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PredictionQueryTag.class);
  }

  /**
   * Convert an instance of PredictionQueryTag to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

