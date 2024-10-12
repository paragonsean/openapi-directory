/*
 * Mixed Reality
 * Mixed Reality Resource Provider Proxy API
 *
 * The version of the OpenAPI document: 2019-12-02-preview
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
 * Response on Error
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:19:38.523181-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OperationsListDefaultResponse {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_DETAILS = "details";
  @SerializedName(SERIALIZED_NAME_DETAILS)
  private String details;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public OperationsListDefaultResponse() {
  }

  public OperationsListDefaultResponse code(String code) {
    this.code = code;
    return this;
  }

  /**
   * String that can be used to programmatically identify the error.
   * @return code
   */
  @javax.annotation.Nonnull
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public OperationsListDefaultResponse details(String details) {
    this.details = details;
    return this;
  }

  /**
   * An array of JSON objects that MUST contain name/value pairs for code and message, and MAY contain a name/value pair for target, as described above.The contents of this section are service-defined but must adhere to the aforementioned schema.
   * @return details
   */
  @javax.annotation.Nullable
  public String getDetails() {
    return details;
  }

  public void setDetails(String details) {
    this.details = details;
  }


  public OperationsListDefaultResponse message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Describes the error in detail and provides debugging information
   * @return message
   */
  @javax.annotation.Nonnull
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public OperationsListDefaultResponse target(String target) {
    this.target = target;
    return this;
  }

  /**
   * The target of the particular error
   * @return target
   */
  @javax.annotation.Nullable
  public String getTarget() {
    return target;
  }

  public void setTarget(String target) {
    this.target = target;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OperationsListDefaultResponse operationsListDefaultResponse = (OperationsListDefaultResponse) o;
    return Objects.equals(this.code, operationsListDefaultResponse.code) &&
        Objects.equals(this.details, operationsListDefaultResponse.details) &&
        Objects.equals(this.message, operationsListDefaultResponse.message) &&
        Objects.equals(this.target, operationsListDefaultResponse.target);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, details, message, target);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OperationsListDefaultResponse {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    details: ").append(toIndentedString(details)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
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
    openapiFields.add("code");
    openapiFields.add("details");
    openapiFields.add("message");
    openapiFields.add("target");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("code");
    openapiRequiredFields.add("message");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OperationsListDefaultResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OperationsListDefaultResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OperationsListDefaultResponse is not found in the empty JSON string", OperationsListDefaultResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OperationsListDefaultResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OperationsListDefaultResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OperationsListDefaultResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("details") != null && !jsonObj.get("details").isJsonNull()) && !jsonObj.get("details").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `details` to be a primitive type in the JSON string but got `%s`", jsonObj.get("details").toString()));
      }
      if (!jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("target") != null && !jsonObj.get("target").isJsonNull()) && !jsonObj.get("target").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `target` to be a primitive type in the JSON string but got `%s`", jsonObj.get("target").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OperationsListDefaultResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OperationsListDefaultResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OperationsListDefaultResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OperationsListDefaultResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<OperationsListDefaultResponse>() {
           @Override
           public void write(JsonWriter out, OperationsListDefaultResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OperationsListDefaultResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OperationsListDefaultResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OperationsListDefaultResponse
   * @throws IOException if the JSON string is invalid with respect to OperationsListDefaultResponse
   */
  public static OperationsListDefaultResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OperationsListDefaultResponse.class);
  }

  /**
   * Convert an instance of OperationsListDefaultResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

