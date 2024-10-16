/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
 * AnalyticsCrashGroupModelCounts200ResponseModelsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AnalyticsCrashGroupModelCounts200ResponseModelsInner {
  public static final String SERIALIZED_NAME_CRASH_COUNT = "crash_count";
  @SerializedName(SERIALIZED_NAME_CRASH_COUNT)
  private Long crashCount;

  public static final String SERIALIZED_NAME_MODEL_NAME = "model_name";
  @SerializedName(SERIALIZED_NAME_MODEL_NAME)
  private String modelName;

  public AnalyticsCrashGroupModelCounts200ResponseModelsInner() {
  }

  public AnalyticsCrashGroupModelCounts200ResponseModelsInner crashCount(Long crashCount) {
    this.crashCount = crashCount;
    return this;
  }

  /**
   * Count of model.
   * @return crashCount
   */
  @javax.annotation.Nullable
  public Long getCrashCount() {
    return crashCount;
  }

  public void setCrashCount(Long crashCount) {
    this.crashCount = crashCount;
  }


  public AnalyticsCrashGroupModelCounts200ResponseModelsInner modelName(String modelName) {
    this.modelName = modelName;
    return this;
  }

  /**
   * Model&#39;s name.
   * @return modelName
   */
  @javax.annotation.Nullable
  public String getModelName() {
    return modelName;
  }

  public void setModelName(String modelName) {
    this.modelName = modelName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnalyticsCrashGroupModelCounts200ResponseModelsInner analyticsCrashGroupModelCounts200ResponseModelsInner = (AnalyticsCrashGroupModelCounts200ResponseModelsInner) o;
    return Objects.equals(this.crashCount, analyticsCrashGroupModelCounts200ResponseModelsInner.crashCount) &&
        Objects.equals(this.modelName, analyticsCrashGroupModelCounts200ResponseModelsInner.modelName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(crashCount, modelName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnalyticsCrashGroupModelCounts200ResponseModelsInner {\n");
    sb.append("    crashCount: ").append(toIndentedString(crashCount)).append("\n");
    sb.append("    modelName: ").append(toIndentedString(modelName)).append("\n");
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
    openapiFields.add("crash_count");
    openapiFields.add("model_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AnalyticsCrashGroupModelCounts200ResponseModelsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AnalyticsCrashGroupModelCounts200ResponseModelsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AnalyticsCrashGroupModelCounts200ResponseModelsInner is not found in the empty JSON string", AnalyticsCrashGroupModelCounts200ResponseModelsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AnalyticsCrashGroupModelCounts200ResponseModelsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AnalyticsCrashGroupModelCounts200ResponseModelsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("model_name") != null && !jsonObj.get("model_name").isJsonNull()) && !jsonObj.get("model_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `model_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("model_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AnalyticsCrashGroupModelCounts200ResponseModelsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AnalyticsCrashGroupModelCounts200ResponseModelsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AnalyticsCrashGroupModelCounts200ResponseModelsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AnalyticsCrashGroupModelCounts200ResponseModelsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AnalyticsCrashGroupModelCounts200ResponseModelsInner>() {
           @Override
           public void write(JsonWriter out, AnalyticsCrashGroupModelCounts200ResponseModelsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AnalyticsCrashGroupModelCounts200ResponseModelsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AnalyticsCrashGroupModelCounts200ResponseModelsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AnalyticsCrashGroupModelCounts200ResponseModelsInner
   * @throws IOException if the JSON string is invalid with respect to AnalyticsCrashGroupModelCounts200ResponseModelsInner
   */
  public static AnalyticsCrashGroupModelCounts200ResponseModelsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AnalyticsCrashGroupModelCounts200ResponseModelsInner.class);
  }

  /**
   * Convert an instance of AnalyticsCrashGroupModelCounts200ResponseModelsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

