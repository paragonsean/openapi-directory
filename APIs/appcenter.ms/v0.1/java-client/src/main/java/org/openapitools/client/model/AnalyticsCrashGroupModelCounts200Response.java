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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AnalyticsCrashGroupModelCounts200ResponseModelsInner;

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
 * AnalyticsCrashGroupModelCounts200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AnalyticsCrashGroupModelCounts200Response {
  public static final String SERIALIZED_NAME_CRASH_COUNT = "crash_count";
  @SerializedName(SERIALIZED_NAME_CRASH_COUNT)
  private Long crashCount;

  public static final String SERIALIZED_NAME_MODELS = "models";
  @SerializedName(SERIALIZED_NAME_MODELS)
  private List<AnalyticsCrashGroupModelCounts200ResponseModelsInner> models = new ArrayList<>();

  public AnalyticsCrashGroupModelCounts200Response() {
  }

  public AnalyticsCrashGroupModelCounts200Response crashCount(Long crashCount) {
    this.crashCount = crashCount;
    return this;
  }

  /**
   * Get crashCount
   * @return crashCount
   */
  @javax.annotation.Nullable
  public Long getCrashCount() {
    return crashCount;
  }

  public void setCrashCount(Long crashCount) {
    this.crashCount = crashCount;
  }


  public AnalyticsCrashGroupModelCounts200Response models(List<AnalyticsCrashGroupModelCounts200ResponseModelsInner> models) {
    this.models = models;
    return this;
  }

  public AnalyticsCrashGroupModelCounts200Response addModelsItem(AnalyticsCrashGroupModelCounts200ResponseModelsInner modelsItem) {
    if (this.models == null) {
      this.models = new ArrayList<>();
    }
    this.models.add(modelsItem);
    return this;
  }

  /**
   * Get models
   * @return models
   */
  @javax.annotation.Nullable
  public List<AnalyticsCrashGroupModelCounts200ResponseModelsInner> getModels() {
    return models;
  }

  public void setModels(List<AnalyticsCrashGroupModelCounts200ResponseModelsInner> models) {
    this.models = models;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnalyticsCrashGroupModelCounts200Response analyticsCrashGroupModelCounts200Response = (AnalyticsCrashGroupModelCounts200Response) o;
    return Objects.equals(this.crashCount, analyticsCrashGroupModelCounts200Response.crashCount) &&
        Objects.equals(this.models, analyticsCrashGroupModelCounts200Response.models);
  }

  @Override
  public int hashCode() {
    return Objects.hash(crashCount, models);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnalyticsCrashGroupModelCounts200Response {\n");
    sb.append("    crashCount: ").append(toIndentedString(crashCount)).append("\n");
    sb.append("    models: ").append(toIndentedString(models)).append("\n");
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
    openapiFields.add("models");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AnalyticsCrashGroupModelCounts200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AnalyticsCrashGroupModelCounts200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AnalyticsCrashGroupModelCounts200Response is not found in the empty JSON string", AnalyticsCrashGroupModelCounts200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AnalyticsCrashGroupModelCounts200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AnalyticsCrashGroupModelCounts200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("models") != null && !jsonObj.get("models").isJsonNull()) {
        JsonArray jsonArraymodels = jsonObj.getAsJsonArray("models");
        if (jsonArraymodels != null) {
          // ensure the json data is an array
          if (!jsonObj.get("models").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `models` to be an array in the JSON string but got `%s`", jsonObj.get("models").toString()));
          }

          // validate the optional field `models` (array)
          for (int i = 0; i < jsonArraymodels.size(); i++) {
            AnalyticsCrashGroupModelCounts200ResponseModelsInner.validateJsonElement(jsonArraymodels.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AnalyticsCrashGroupModelCounts200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AnalyticsCrashGroupModelCounts200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AnalyticsCrashGroupModelCounts200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AnalyticsCrashGroupModelCounts200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<AnalyticsCrashGroupModelCounts200Response>() {
           @Override
           public void write(JsonWriter out, AnalyticsCrashGroupModelCounts200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AnalyticsCrashGroupModelCounts200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AnalyticsCrashGroupModelCounts200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AnalyticsCrashGroupModelCounts200Response
   * @throws IOException if the JSON string is invalid with respect to AnalyticsCrashGroupModelCounts200Response
   */
  public static AnalyticsCrashGroupModelCounts200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AnalyticsCrashGroupModelCounts200Response.class);
  }

  /**
   * Convert an instance of AnalyticsCrashGroupModelCounts200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

