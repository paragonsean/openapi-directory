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
 * IntuneAppsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IntuneAppsRequest {
  public static final String SERIALIZED_NAME_CREATED_MONTH = "created_month";
  @SerializedName(SERIALIZED_NAME_CREATED_MONTH)
  private String createdMonth;

  public IntuneAppsRequest() {
  }

  public IntuneAppsRequest createdMonth(String createdMonth) {
    this.createdMonth = createdMonth;
    return this;
  }

  /**
   * PartitionKey year-month
   * @return createdMonth
   */
  @javax.annotation.Nullable
  public String getCreatedMonth() {
    return createdMonth;
  }

  public void setCreatedMonth(String createdMonth) {
    this.createdMonth = createdMonth;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IntuneAppsRequest intuneAppsRequest = (IntuneAppsRequest) o;
    return Objects.equals(this.createdMonth, intuneAppsRequest.createdMonth);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdMonth);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IntuneAppsRequest {\n");
    sb.append("    createdMonth: ").append(toIndentedString(createdMonth)).append("\n");
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
    openapiFields.add("created_month");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IntuneAppsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IntuneAppsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IntuneAppsRequest is not found in the empty JSON string", IntuneAppsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IntuneAppsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IntuneAppsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("created_month") != null && !jsonObj.get("created_month").isJsonNull()) && !jsonObj.get("created_month").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_month` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_month").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IntuneAppsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IntuneAppsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IntuneAppsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IntuneAppsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<IntuneAppsRequest>() {
           @Override
           public void write(JsonWriter out, IntuneAppsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IntuneAppsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IntuneAppsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IntuneAppsRequest
   * @throws IOException if the JSON string is invalid with respect to IntuneAppsRequest
   */
  public static IntuneAppsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IntuneAppsRequest.class);
  }

  /**
   * Convert an instance of IntuneAppsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

