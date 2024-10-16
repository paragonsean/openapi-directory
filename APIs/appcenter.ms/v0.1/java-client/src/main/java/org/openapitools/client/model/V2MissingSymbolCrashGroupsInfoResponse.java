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
 * missing symbol groups
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class V2MissingSymbolCrashGroupsInfoResponse {
  public static final String SERIALIZED_NAME_TOTAL_CRASH_COUNT = "total_crash_count";
  @SerializedName(SERIALIZED_NAME_TOTAL_CRASH_COUNT)
  private Integer totalCrashCount;

  public V2MissingSymbolCrashGroupsInfoResponse() {
  }

  public V2MissingSymbolCrashGroupsInfoResponse totalCrashCount(Integer totalCrashCount) {
    this.totalCrashCount = totalCrashCount;
    return this;
  }

  /**
   * total number of crashes for all missing symbol groups
   * @return totalCrashCount
   */
  @javax.annotation.Nonnull
  public Integer getTotalCrashCount() {
    return totalCrashCount;
  }

  public void setTotalCrashCount(Integer totalCrashCount) {
    this.totalCrashCount = totalCrashCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V2MissingSymbolCrashGroupsInfoResponse v2MissingSymbolCrashGroupsInfoResponse = (V2MissingSymbolCrashGroupsInfoResponse) o;
    return Objects.equals(this.totalCrashCount, v2MissingSymbolCrashGroupsInfoResponse.totalCrashCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(totalCrashCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V2MissingSymbolCrashGroupsInfoResponse {\n");
    sb.append("    totalCrashCount: ").append(toIndentedString(totalCrashCount)).append("\n");
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
    openapiFields.add("total_crash_count");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("total_crash_count");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to V2MissingSymbolCrashGroupsInfoResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!V2MissingSymbolCrashGroupsInfoResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in V2MissingSymbolCrashGroupsInfoResponse is not found in the empty JSON string", V2MissingSymbolCrashGroupsInfoResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!V2MissingSymbolCrashGroupsInfoResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `V2MissingSymbolCrashGroupsInfoResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : V2MissingSymbolCrashGroupsInfoResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!V2MissingSymbolCrashGroupsInfoResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'V2MissingSymbolCrashGroupsInfoResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<V2MissingSymbolCrashGroupsInfoResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(V2MissingSymbolCrashGroupsInfoResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<V2MissingSymbolCrashGroupsInfoResponse>() {
           @Override
           public void write(JsonWriter out, V2MissingSymbolCrashGroupsInfoResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public V2MissingSymbolCrashGroupsInfoResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of V2MissingSymbolCrashGroupsInfoResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of V2MissingSymbolCrashGroupsInfoResponse
   * @throws IOException if the JSON string is invalid with respect to V2MissingSymbolCrashGroupsInfoResponse
   */
  public static V2MissingSymbolCrashGroupsInfoResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, V2MissingSymbolCrashGroupsInfoResponse.class);
  }

  /**
   * Convert an instance of V2MissingSymbolCrashGroupsInfoResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

