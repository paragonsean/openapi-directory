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
import org.openapitools.client.model.BasketLiveShippingServiceCreate200ResponseResult;

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
 * BasketLiveShippingServiceCreate200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:09.268126-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BasketLiveShippingServiceCreate200Response {
  public static final String SERIALIZED_NAME_RESULT = "result";
  @SerializedName(SERIALIZED_NAME_RESULT)
  private BasketLiveShippingServiceCreate200ResponseResult result;

  public static final String SERIALIZED_NAME_RETURN_CODE = "return_code";
  @SerializedName(SERIALIZED_NAME_RETURN_CODE)
  private Integer returnCode;

  public static final String SERIALIZED_NAME_RETURN_MESSAGE = "return_message";
  @SerializedName(SERIALIZED_NAME_RETURN_MESSAGE)
  private String returnMessage;

  public BasketLiveShippingServiceCreate200Response() {
  }

  public BasketLiveShippingServiceCreate200Response result(BasketLiveShippingServiceCreate200ResponseResult result) {
    this.result = result;
    return this;
  }

  /**
   * Get result
   * @return result
   */
  @javax.annotation.Nullable
  public BasketLiveShippingServiceCreate200ResponseResult getResult() {
    return result;
  }

  public void setResult(BasketLiveShippingServiceCreate200ResponseResult result) {
    this.result = result;
  }


  public BasketLiveShippingServiceCreate200Response returnCode(Integer returnCode) {
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


  public BasketLiveShippingServiceCreate200Response returnMessage(String returnMessage) {
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
    BasketLiveShippingServiceCreate200Response basketLiveShippingServiceCreate200Response = (BasketLiveShippingServiceCreate200Response) o;
    return Objects.equals(this.result, basketLiveShippingServiceCreate200Response.result) &&
        Objects.equals(this.returnCode, basketLiveShippingServiceCreate200Response.returnCode) &&
        Objects.equals(this.returnMessage, basketLiveShippingServiceCreate200Response.returnMessage);
  }

  @Override
  public int hashCode() {
    return Objects.hash(result, returnCode, returnMessage);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BasketLiveShippingServiceCreate200Response {\n");
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
   * @throws IOException if the JSON Element is invalid with respect to BasketLiveShippingServiceCreate200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BasketLiveShippingServiceCreate200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BasketLiveShippingServiceCreate200Response is not found in the empty JSON string", BasketLiveShippingServiceCreate200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BasketLiveShippingServiceCreate200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BasketLiveShippingServiceCreate200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `result`
      if (jsonObj.get("result") != null && !jsonObj.get("result").isJsonNull()) {
        BasketLiveShippingServiceCreate200ResponseResult.validateJsonElement(jsonObj.get("result"));
      }
      if ((jsonObj.get("return_message") != null && !jsonObj.get("return_message").isJsonNull()) && !jsonObj.get("return_message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `return_message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("return_message").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BasketLiveShippingServiceCreate200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BasketLiveShippingServiceCreate200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BasketLiveShippingServiceCreate200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BasketLiveShippingServiceCreate200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<BasketLiveShippingServiceCreate200Response>() {
           @Override
           public void write(JsonWriter out, BasketLiveShippingServiceCreate200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BasketLiveShippingServiceCreate200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BasketLiveShippingServiceCreate200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BasketLiveShippingServiceCreate200Response
   * @throws IOException if the JSON string is invalid with respect to BasketLiveShippingServiceCreate200Response
   */
  public static BasketLiveShippingServiceCreate200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BasketLiveShippingServiceCreate200Response.class);
  }

  /**
   * Convert an instance of BasketLiveShippingServiceCreate200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

