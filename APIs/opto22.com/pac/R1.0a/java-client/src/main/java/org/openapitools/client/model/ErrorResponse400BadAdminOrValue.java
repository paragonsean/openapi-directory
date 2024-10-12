/*
 * PAC Control REST API
 * #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller's variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC's strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   ``` https://1.2.3.4/api/v1/device/strategy/vars/int32s ``` and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  ```json [ { \"nMyVeryFavoriteNumber\": 22 },   { \"nWidgetsProducedToday\": 22222 },   { \"DELAY_LOOP_TIME_IN_MSECS\"  : 200 } ] ``` **Read the engineering units** (EU) of an analog input point configured in the PAC's strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   `https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu`  The GET response will be a single JSON name-value pair such as: ```json { \"value\": 72.22 } ```      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
 *
 * The version of the OpenAPI document: R1.0a
 * Contact: developer@opto22.com
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
 * ErrorResponse400BadAdminOrValue
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:29.356996-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorResponse400BadAdminOrValue {
  public static final String SERIALIZED_NAME_ERROR_CODE = "errorCode";
  @SerializedName(SERIALIZED_NAME_ERROR_CODE)
  private Integer errorCode;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public ErrorResponse400BadAdminOrValue() {
  }

  public ErrorResponse400BadAdminOrValue errorCode(Integer errorCode) {
    this.errorCode = errorCode;
    return this;
  }

  /**
   * Details: ** -1 ** Invalid or no strategy. Use PAC Control to download strategy logic. ** -3 ** Buffer overrun or invalid length. The number or range of table indicies you specified exceeds elements in the PAC Control table. ** -8 ** Invalid data. Check format of data written. Compare to what&#39;s read for the same endpoint. ** -12 ** You&#39;ve passed a table index that is less than zero or greater than the length of the table minus 1. ** -13 ** The value you passed to write is outside of the valid range for the PAC Control data type you&#39;re writing to. For example, if you specified the value 999999999999999 for an integer32 (since integer32 data types must be in the range: -2147483648 to 2147483647). ** -17 or -20 ** The controller is busy with another task, for example, downloading a new strategy. Try again later. ** -36 ** Endpoint is not defined. ** -109 ** Attempting to write without write permissions. Check /admin/keys settings. ** -13019 ** Invalid endpoint. Check syntax of the URL (e.g. did you use &#39;ev&#39; instead of &#39;eu&#39;). ** 400 ** Before using the API on this device, you must first change the default user name and password via the URL /admin/keys. Use the default User Name: &#39;admin&#39; and Password: &#39;password&#39; to log ininitially.
   * @return errorCode
   */
  @javax.annotation.Nonnull
  public Integer getErrorCode() {
    return errorCode;
  }

  public void setErrorCode(Integer errorCode) {
    this.errorCode = errorCode;
  }


  public ErrorResponse400BadAdminOrValue message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nonnull
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
    ErrorResponse400BadAdminOrValue errorResponse400BadAdminOrValue = (ErrorResponse400BadAdminOrValue) o;
    return Objects.equals(this.errorCode, errorResponse400BadAdminOrValue.errorCode) &&
        Objects.equals(this.message, errorResponse400BadAdminOrValue.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(errorCode, message);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorResponse400BadAdminOrValue {\n");
    sb.append("    errorCode: ").append(toIndentedString(errorCode)).append("\n");
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
    openapiFields.add("errorCode");
    openapiFields.add("message");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("errorCode");
    openapiRequiredFields.add("message");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorResponse400BadAdminOrValue
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorResponse400BadAdminOrValue.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorResponse400BadAdminOrValue is not found in the empty JSON string", ErrorResponse400BadAdminOrValue.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorResponse400BadAdminOrValue.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorResponse400BadAdminOrValue` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ErrorResponse400BadAdminOrValue.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ErrorResponse400BadAdminOrValue.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorResponse400BadAdminOrValue' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorResponse400BadAdminOrValue> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorResponse400BadAdminOrValue.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorResponse400BadAdminOrValue>() {
           @Override
           public void write(JsonWriter out, ErrorResponse400BadAdminOrValue value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorResponse400BadAdminOrValue read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorResponse400BadAdminOrValue given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorResponse400BadAdminOrValue
   * @throws IOException if the JSON string is invalid with respect to ErrorResponse400BadAdminOrValue
   */
  public static ErrorResponse400BadAdminOrValue fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorResponse400BadAdminOrValue.class);
  }

  /**
   * Convert an instance of ErrorResponse400BadAdminOrValue to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

