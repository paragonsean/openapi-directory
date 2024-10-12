/*
 * Customer Lockbox
 * Azure Customer Lockbox API Reference
 *
 * The version of the OpenAPI document: 2018-02-28-preview
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
import org.openapitools.client.model.ErrorAdditionalInfo;

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
 * An error response body from the Lockbox service.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:44:18.780867-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorBody {
  public static final String SERIALIZED_NAME_ADDITIONAL_INFO = "additionalInfo";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_INFO)
  private List<ErrorAdditionalInfo> additionalInfo = new ArrayList<>();

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public ErrorBody() {
  }

  public ErrorBody additionalInfo(List<ErrorAdditionalInfo> additionalInfo) {
    this.additionalInfo = additionalInfo;
    return this;
  }

  public ErrorBody addAdditionalInfoItem(ErrorAdditionalInfo additionalInfoItem) {
    if (this.additionalInfo == null) {
      this.additionalInfo = new ArrayList<>();
    }
    this.additionalInfo.add(additionalInfoItem);
    return this;
  }

  /**
   * A list of error details about the error.
   * @return additionalInfo
   */
  @javax.annotation.Nullable
  public List<ErrorAdditionalInfo> getAdditionalInfo() {
    return additionalInfo;
  }

  public void setAdditionalInfo(List<ErrorAdditionalInfo> additionalInfo) {
    this.additionalInfo = additionalInfo;
  }


  public ErrorBody code(String code) {
    this.code = code;
    return this;
  }

  /**
   * An identifier for the error. Codes are invariant and are intended to be consumed programmatically.
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public ErrorBody message(String message) {
    this.message = message;
    return this;
  }

  /**
   * A message describing the error, intended to be suitable for display in a user interface.
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public ErrorBody target(String target) {
    this.target = target;
    return this;
  }

  /**
   * The target of the particular error. For example, the name of the property in error.
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
    ErrorBody errorBody = (ErrorBody) o;
    return Objects.equals(this.additionalInfo, errorBody.additionalInfo) &&
        Objects.equals(this.code, errorBody.code) &&
        Objects.equals(this.message, errorBody.message) &&
        Objects.equals(this.target, errorBody.target);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalInfo, code, message, target);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorBody {\n");
    sb.append("    additionalInfo: ").append(toIndentedString(additionalInfo)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
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
    openapiFields.add("additionalInfo");
    openapiFields.add("code");
    openapiFields.add("message");
    openapiFields.add("target");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorBody
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorBody.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorBody is not found in the empty JSON string", ErrorBody.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorBody.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorBody` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("additionalInfo") != null && !jsonObj.get("additionalInfo").isJsonNull()) {
        JsonArray jsonArrayadditionalInfo = jsonObj.getAsJsonArray("additionalInfo");
        if (jsonArrayadditionalInfo != null) {
          // ensure the json data is an array
          if (!jsonObj.get("additionalInfo").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `additionalInfo` to be an array in the JSON string but got `%s`", jsonObj.get("additionalInfo").toString()));
          }

          // validate the optional field `additionalInfo` (array)
          for (int i = 0; i < jsonArrayadditionalInfo.size(); i++) {
            ErrorAdditionalInfo.validateJsonElement(jsonArrayadditionalInfo.get(i));
          };
        }
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
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
       if (!ErrorBody.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorBody' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorBody> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorBody.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorBody>() {
           @Override
           public void write(JsonWriter out, ErrorBody value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorBody read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorBody given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorBody
   * @throws IOException if the JSON string is invalid with respect to ErrorBody
   */
  public static ErrorBody fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorBody.class);
  }

  /**
   * Convert an instance of ErrorBody to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

