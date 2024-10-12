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
 * BillingAggregatedInformationGetByAppDefaultResponseError
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BillingAggregatedInformationGetByAppDefaultResponseError {
  /**
   * The status code return by the API. It can be 400 or 403 or 500.
   */
  @JsonAdapter(CodeEnum.Adapter.class)
  public enum CodeEnum {
    NUMBER_400(400),
    
    NUMBER_403(403),
    
    NUMBER_500(500);

    private Integer value;

    CodeEnum(Integer value) {
      this.value = value;
    }

    public Integer getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CodeEnum fromValue(Integer value) {
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
        Integer value =  jsonReader.nextInt();
        return CodeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      Integer value = jsonElement.getAsInt();
      CodeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private CodeEnum code;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public BillingAggregatedInformationGetByAppDefaultResponseError() {
  }

  public BillingAggregatedInformationGetByAppDefaultResponseError code(CodeEnum code) {
    this.code = code;
    return this;
  }

  /**
   * The status code return by the API. It can be 400 or 403 or 500.
   * @return code
   */
  @javax.annotation.Nullable
  public CodeEnum getCode() {
    return code;
  }

  public void setCode(CodeEnum code) {
    this.code = code;
  }


  public BillingAggregatedInformationGetByAppDefaultResponseError message(String message) {
    this.message = message;
    return this;
  }

  /**
   * The reason for the request failed
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BillingAggregatedInformationGetByAppDefaultResponseError billingAggregatedInformationGetByAppDefaultResponseError = (BillingAggregatedInformationGetByAppDefaultResponseError) o;
    return Objects.equals(this.code, billingAggregatedInformationGetByAppDefaultResponseError.code) &&
        Objects.equals(this.message, billingAggregatedInformationGetByAppDefaultResponseError.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, message);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BillingAggregatedInformationGetByAppDefaultResponseError {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
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

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BillingAggregatedInformationGetByAppDefaultResponseError
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BillingAggregatedInformationGetByAppDefaultResponseError.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BillingAggregatedInformationGetByAppDefaultResponseError is not found in the empty JSON string", BillingAggregatedInformationGetByAppDefaultResponseError.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BillingAggregatedInformationGetByAppDefaultResponseError.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BillingAggregatedInformationGetByAppDefaultResponseError` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `code`
      if (jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) {
        CodeEnum.validateJsonElement(jsonObj.get("code"));
      }
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BillingAggregatedInformationGetByAppDefaultResponseError.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BillingAggregatedInformationGetByAppDefaultResponseError' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BillingAggregatedInformationGetByAppDefaultResponseError> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BillingAggregatedInformationGetByAppDefaultResponseError.class));

       return (TypeAdapter<T>) new TypeAdapter<BillingAggregatedInformationGetByAppDefaultResponseError>() {
           @Override
           public void write(JsonWriter out, BillingAggregatedInformationGetByAppDefaultResponseError value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BillingAggregatedInformationGetByAppDefaultResponseError read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BillingAggregatedInformationGetByAppDefaultResponseError given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BillingAggregatedInformationGetByAppDefaultResponseError
   * @throws IOException if the JSON string is invalid with respect to BillingAggregatedInformationGetByAppDefaultResponseError
   */
  public static BillingAggregatedInformationGetByAppDefaultResponseError fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BillingAggregatedInformationGetByAppDefaultResponseError.class);
  }

  /**
   * Convert an instance of BillingAggregatedInformationGetByAppDefaultResponseError to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

