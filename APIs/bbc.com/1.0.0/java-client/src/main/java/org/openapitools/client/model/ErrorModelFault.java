/*
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
import org.openapitools.client.model.ErrorModelFaultDetail;

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
 * ErrorModelFault
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorModelFault {
  public static final String SERIALIZED_NAME_DETAIL = "detail";
  @SerializedName(SERIALIZED_NAME_DETAIL)
  private ErrorModelFaultDetail detail;

  public static final String SERIALIZED_NAME_FAULT_STRING = "faultString";
  @SerializedName(SERIALIZED_NAME_FAULT_STRING)
  private String faultString;

  public ErrorModelFault() {
  }

  public ErrorModelFault detail(ErrorModelFaultDetail detail) {
    this.detail = detail;
    return this;
  }

  /**
   * Get detail
   * @return detail
   */
  @javax.annotation.Nullable
  public ErrorModelFaultDetail getDetail() {
    return detail;
  }

  public void setDetail(ErrorModelFaultDetail detail) {
    this.detail = detail;
  }


  public ErrorModelFault faultString(String faultString) {
    this.faultString = faultString;
    return this;
  }

  /**
   * Get faultString
   * @return faultString
   */
  @javax.annotation.Nullable
  public String getFaultString() {
    return faultString;
  }

  public void setFaultString(String faultString) {
    this.faultString = faultString;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ErrorModelFault errorModelFault = (ErrorModelFault) o;
    return Objects.equals(this.detail, errorModelFault.detail) &&
        Objects.equals(this.faultString, errorModelFault.faultString);
  }

  @Override
  public int hashCode() {
    return Objects.hash(detail, faultString);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorModelFault {\n");
    sb.append("    detail: ").append(toIndentedString(detail)).append("\n");
    sb.append("    faultString: ").append(toIndentedString(faultString)).append("\n");
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
    openapiFields.add("detail");
    openapiFields.add("faultString");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorModelFault
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorModelFault.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorModelFault is not found in the empty JSON string", ErrorModelFault.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorModelFault.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorModelFault` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `detail`
      if (jsonObj.get("detail") != null && !jsonObj.get("detail").isJsonNull()) {
        ErrorModelFaultDetail.validateJsonElement(jsonObj.get("detail"));
      }
      if ((jsonObj.get("faultString") != null && !jsonObj.get("faultString").isJsonNull()) && !jsonObj.get("faultString").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `faultString` to be a primitive type in the JSON string but got `%s`", jsonObj.get("faultString").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ErrorModelFault.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorModelFault' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorModelFault> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorModelFault.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorModelFault>() {
           @Override
           public void write(JsonWriter out, ErrorModelFault value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorModelFault read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorModelFault given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorModelFault
   * @throws IOException if the JSON string is invalid with respect to ErrorModelFault
   */
  public static ErrorModelFault fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorModelFault.class);
  }

  /**
   * Convert an instance of ErrorModelFault to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

