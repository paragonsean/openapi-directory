/*
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
import org.openapitools.client.model.AttributeDelete200ResponseResult;

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
 * AttributeDelete200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AttributeDelete200Response {
  public static final String SERIALIZED_NAME_RESULT = "result";
  @SerializedName(SERIALIZED_NAME_RESULT)
  private AttributeDelete200ResponseResult result;

  public static final String SERIALIZED_NAME_RETURN_CODE = "return_code";
  @SerializedName(SERIALIZED_NAME_RETURN_CODE)
  private Integer returnCode;

  public static final String SERIALIZED_NAME_RETURN_MESSAGE = "return_message";
  @SerializedName(SERIALIZED_NAME_RETURN_MESSAGE)
  private String returnMessage;

  public AttributeDelete200Response() {
  }

  public AttributeDelete200Response result(AttributeDelete200ResponseResult result) {
    this.result = result;
    return this;
  }

  /**
   * Get result
   * @return result
   */
  @javax.annotation.Nullable
  public AttributeDelete200ResponseResult getResult() {
    return result;
  }

  public void setResult(AttributeDelete200ResponseResult result) {
    this.result = result;
  }


  public AttributeDelete200Response returnCode(Integer returnCode) {
    this.returnCode = returnCode;
    return this;
  }

  /**
   * Get returnCode
   * @return returnCode
   */
  @javax.annotation.Nullable
  public Integer getReturnCode() {
    return returnCode;
  }

  public void setReturnCode(Integer returnCode) {
    this.returnCode = returnCode;
  }


  public AttributeDelete200Response returnMessage(String returnMessage) {
    this.returnMessage = returnMessage;
    return this;
  }

  /**
   * Get returnMessage
   * @return returnMessage
   */
  @javax.annotation.Nullable
  public String getReturnMessage() {
    return returnMessage;
  }

  public void setReturnMessage(String returnMessage) {
    this.returnMessage = returnMessage;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AttributeDelete200Response attributeDelete200Response = (AttributeDelete200Response) o;
    return Objects.equals(this.result, attributeDelete200Response.result) &&
        Objects.equals(this.returnCode, attributeDelete200Response.returnCode) &&
        Objects.equals(this.returnMessage, attributeDelete200Response.returnMessage);
  }

  @Override
  public int hashCode() {
    return Objects.hash(result, returnCode, returnMessage);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AttributeDelete200Response {\n");
    sb.append("    result: ").append(toIndentedString(result)).append("\n");
    sb.append("    returnCode: ").append(toIndentedString(returnCode)).append("\n");
    sb.append("    returnMessage: ").append(toIndentedString(returnMessage)).append("\n");
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
    openapiFields.add("result");
    openapiFields.add("return_code");
    openapiFields.add("return_message");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AttributeDelete200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AttributeDelete200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AttributeDelete200Response is not found in the empty JSON string", AttributeDelete200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AttributeDelete200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AttributeDelete200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `result`
      if (jsonObj.get("result") != null && !jsonObj.get("result").isJsonNull()) {
        AttributeDelete200ResponseResult.validateJsonElement(jsonObj.get("result"));
      }
      if ((jsonObj.get("return_message") != null && !jsonObj.get("return_message").isJsonNull()) && !jsonObj.get("return_message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `return_message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("return_message").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AttributeDelete200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AttributeDelete200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AttributeDelete200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AttributeDelete200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<AttributeDelete200Response>() {
           @Override
           public void write(JsonWriter out, AttributeDelete200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AttributeDelete200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AttributeDelete200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AttributeDelete200Response
   * @throws IOException if the JSON string is invalid with respect to AttributeDelete200Response
   */
  public static AttributeDelete200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AttributeDelete200Response.class);
  }

  /**
   * Convert an instance of AttributeDelete200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

