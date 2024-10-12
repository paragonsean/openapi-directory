/*
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
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
 * Defines the error that occurred.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:10:59.700770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Error {
  /**
   * The error code that identifies the category of error.
   */
  @JsonAdapter(CodeEnum.Adapter.class)
  public enum CodeEnum {
    NONE("None"),
    
    SERVER_ERROR("ServerError"),
    
    INVALID_REQUEST("InvalidRequest"),
    
    RATE_LIMIT_EXCEEDED("RateLimitExceeded"),
    
    INVALID_AUTHORIZATION("InvalidAuthorization"),
    
    INSUFFICIENT_AUTHORIZATION("InsufficientAuthorization");

    private String value;

    CodeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CodeEnum fromValue(String value) {
      for (CodeEnum b : CodeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CodeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CodeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CodeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CodeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CodeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private CodeEnum code = CodeEnum.NONE;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_MORE_DETAILS = "moreDetails";
  @SerializedName(SERIALIZED_NAME_MORE_DETAILS)
  private String moreDetails;

  public static final String SERIALIZED_NAME_PARAMETER = "parameter";
  @SerializedName(SERIALIZED_NAME_PARAMETER)
  private String parameter;

  /**
   * The error code that further helps to identify the error.
   */
  @JsonAdapter(SubCodeEnum.Adapter.class)
  public enum SubCodeEnum {
    UNEXPECTED_ERROR("UnexpectedError"),
    
    RESOURCE_ERROR("ResourceError"),
    
    NOT_IMPLEMENTED("NotImplemented"),
    
    PARAMETER_MISSING("ParameterMissing"),
    
    PARAMETER_INVALID_VALUE("ParameterInvalidValue"),
    
    HTTP_NOT_ALLOWED("HttpNotAllowed"),
    
    BLOCKED("Blocked"),
    
    AUTHORIZATION_MISSING("AuthorizationMissing"),
    
    AUTHORIZATION_REDUNDANCY("AuthorizationRedundancy"),
    
    AUTHORIZATION_DISABLED("AuthorizationDisabled"),
    
    AUTHORIZATION_EXPIRED("AuthorizationExpired");

    private String value;

    SubCodeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SubCodeEnum fromValue(String value) {
      for (SubCodeEnum b : SubCodeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SubCodeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SubCodeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SubCodeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SubCodeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SubCodeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SUB_CODE = "subCode";
  @SerializedName(SERIALIZED_NAME_SUB_CODE)
  private SubCodeEnum subCode;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public Error() {
  }

  public Error(
     String moreDetails, 
     String parameter, 
     SubCodeEnum subCode, 
     String value
  ) {
    this();
    this.moreDetails = moreDetails;
    this.parameter = parameter;
    this.subCode = subCode;
    this.value = value;
  }

  public Error code(CodeEnum code) {
    this.code = code;
    return this;
  }

  /**
   * The error code that identifies the category of error.
   * @return code
   */
  @javax.annotation.Nonnull
  public CodeEnum getCode() {
    return code;
  }

  public void setCode(CodeEnum code) {
    this.code = code;
  }


  public Error message(String message) {
    this.message = message;
    return this;
  }

  /**
   * A description of the error.
   * @return message
   */
  @javax.annotation.Nonnull
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  /**
   * A description that provides additional information about the error.
   * @return moreDetails
   */
  @javax.annotation.Nullable
  public String getMoreDetails() {
    return moreDetails;
  }



  /**
   * The parameter in the request that caused the error.
   * @return parameter
   */
  @javax.annotation.Nullable
  public String getParameter() {
    return parameter;
  }



  /**
   * The error code that further helps to identify the error.
   * @return subCode
   */
  @javax.annotation.Nullable
  public SubCodeEnum getSubCode() {
    return subCode;
  }



  /**
   * The parameter&#39;s value in the request that was not valid.
   * @return value
   */
  @javax.annotation.Nullable
  public String getValue() {
    return value;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Error error = (Error) o;
    return Objects.equals(this.code, error.code) &&
        Objects.equals(this.message, error.message) &&
        Objects.equals(this.moreDetails, error.moreDetails) &&
        Objects.equals(this.parameter, error.parameter) &&
        Objects.equals(this.subCode, error.subCode) &&
        Objects.equals(this.value, error.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, message, moreDetails, parameter, subCode, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Error {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    moreDetails: ").append(toIndentedString(moreDetails)).append("\n");
    sb.append("    parameter: ").append(toIndentedString(parameter)).append("\n");
    sb.append("    subCode: ").append(toIndentedString(subCode)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("message");
    openapiFields.add("moreDetails");
    openapiFields.add("parameter");
    openapiFields.add("subCode");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("code");
    openapiRequiredFields.add("message");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Error
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Error.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Error is not found in the empty JSON string", Error.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Error.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Error` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Error.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      // validate the required field `code`
      CodeEnum.validateJsonElement(jsonObj.get("code"));
      if (!jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("moreDetails") != null && !jsonObj.get("moreDetails").isJsonNull()) && !jsonObj.get("moreDetails").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `moreDetails` to be a primitive type in the JSON string but got `%s`", jsonObj.get("moreDetails").toString()));
      }
      if ((jsonObj.get("parameter") != null && !jsonObj.get("parameter").isJsonNull()) && !jsonObj.get("parameter").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parameter` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parameter").toString()));
      }
      if ((jsonObj.get("subCode") != null && !jsonObj.get("subCode").isJsonNull()) && !jsonObj.get("subCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subCode").toString()));
      }
      // validate the optional field `subCode`
      if (jsonObj.get("subCode") != null && !jsonObj.get("subCode").isJsonNull()) {
        SubCodeEnum.validateJsonElement(jsonObj.get("subCode"));
      }
      if ((jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Error.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Error' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Error> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Error.class));

       return (TypeAdapter<T>) new TypeAdapter<Error>() {
           @Override
           public void write(JsonWriter out, Error value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Error read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Error given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Error
   * @throws IOException if the JSON string is invalid with respect to Error
   */
  public static Error fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Error.class);
  }

  /**
   * Convert an instance of Error to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

