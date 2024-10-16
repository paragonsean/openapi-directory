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
import org.openapitools.client.model.ErrorsCountsPerDay200ResponseErrorsInner;

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
 * ErrorsCountsPerDay200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorsCountsPerDay200Response {
  public static final String SERIALIZED_NAME_COUNT = "count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Long count;

  public static final String SERIALIZED_NAME_ERRORS = "errors";
  @SerializedName(SERIALIZED_NAME_ERRORS)
  private List<ErrorsCountsPerDay200ResponseErrorsInner> errors = new ArrayList<>();

  public ErrorsCountsPerDay200Response() {
  }

  public ErrorsCountsPerDay200Response count(Long count) {
    this.count = count;
    return this;
  }

  /**
   * total error count
   * @return count
   */
  @javax.annotation.Nullable
  public Long getCount() {
    return count;
  }

  public void setCount(Long count) {
    this.count = count;
  }


  public ErrorsCountsPerDay200Response errors(List<ErrorsCountsPerDay200ResponseErrorsInner> errors) {
    this.errors = errors;
    return this;
  }

  public ErrorsCountsPerDay200Response addErrorsItem(ErrorsCountsPerDay200ResponseErrorsInner errorsItem) {
    if (this.errors == null) {
      this.errors = new ArrayList<>();
    }
    this.errors.add(errorsItem);
    return this;
  }

  /**
   * the total error count for day
   * @return errors
   */
  @javax.annotation.Nullable
  public List<ErrorsCountsPerDay200ResponseErrorsInner> getErrors() {
    return errors;
  }

  public void setErrors(List<ErrorsCountsPerDay200ResponseErrorsInner> errors) {
    this.errors = errors;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ErrorsCountsPerDay200Response errorsCountsPerDay200Response = (ErrorsCountsPerDay200Response) o;
    return Objects.equals(this.count, errorsCountsPerDay200Response.count) &&
        Objects.equals(this.errors, errorsCountsPerDay200Response.errors);
  }

  @Override
  public int hashCode() {
    return Objects.hash(count, errors);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorsCountsPerDay200Response {\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    errors: ").append(toIndentedString(errors)).append("\n");
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
    openapiFields.add("count");
    openapiFields.add("errors");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorsCountsPerDay200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorsCountsPerDay200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorsCountsPerDay200Response is not found in the empty JSON string", ErrorsCountsPerDay200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorsCountsPerDay200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorsCountsPerDay200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("errors") != null && !jsonObj.get("errors").isJsonNull()) {
        JsonArray jsonArrayerrors = jsonObj.getAsJsonArray("errors");
        if (jsonArrayerrors != null) {
          // ensure the json data is an array
          if (!jsonObj.get("errors").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `errors` to be an array in the JSON string but got `%s`", jsonObj.get("errors").toString()));
          }

          // validate the optional field `errors` (array)
          for (int i = 0; i < jsonArrayerrors.size(); i++) {
            ErrorsCountsPerDay200ResponseErrorsInner.validateJsonElement(jsonArrayerrors.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ErrorsCountsPerDay200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorsCountsPerDay200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorsCountsPerDay200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorsCountsPerDay200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorsCountsPerDay200Response>() {
           @Override
           public void write(JsonWriter out, ErrorsCountsPerDay200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorsCountsPerDay200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorsCountsPerDay200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorsCountsPerDay200Response
   * @throws IOException if the JSON string is invalid with respect to ErrorsCountsPerDay200Response
   */
  public static ErrorsCountsPerDay200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorsCountsPerDay200Response.class);
  }

  /**
   * Convert an instance of ErrorsCountsPerDay200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

