/*
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
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
import org.openapitools.jackson.nullable.JsonNullable;

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
 * VerifyAccountId400Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:03.399628-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VerifyAccountId400Response {
  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private Object error = null;

  public static final String SERIALIZED_NAME_ERROR_DESCRIPTION = "error_description";
  @SerializedName(SERIALIZED_NAME_ERROR_DESCRIPTION)
  private Object errorDescription = null;

  public VerifyAccountId400Response() {
  }

  public VerifyAccountId400Response error(Object error) {
    this.error = error;
    return this;
  }

  /**
   * invalid_parameter
   * @return error
   */
  @javax.annotation.Nullable
  public Object getError() {
    return error;
  }

  public void setError(Object error) {
    this.error = error;
  }


  public VerifyAccountId400Response errorDescription(Object errorDescription) {
    this.errorDescription = errorDescription;
    return this;
  }

  /**
   * One or more of the mandatory parameters is missing or invalid. The error description text will contain one or more of the following error texts:|-  Either one of uid or mobile number is mandatory  Timestamp parameter is missing or invalid  HMAC parameter is missing or invalid
   * @return errorDescription
   */
  @javax.annotation.Nullable
  public Object getErrorDescription() {
    return errorDescription;
  }

  public void setErrorDescription(Object errorDescription) {
    this.errorDescription = errorDescription;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VerifyAccountId400Response verifyAccountId400Response = (VerifyAccountId400Response) o;
    return Objects.equals(this.error, verifyAccountId400Response.error) &&
        Objects.equals(this.errorDescription, verifyAccountId400Response.errorDescription);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(error, errorDescription);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VerifyAccountId400Response {\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    errorDescription: ").append(toIndentedString(errorDescription)).append("\n");
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
    openapiFields.add("error");
    openapiFields.add("error_description");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VerifyAccountId400Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VerifyAccountId400Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VerifyAccountId400Response is not found in the empty JSON string", VerifyAccountId400Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VerifyAccountId400Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VerifyAccountId400Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VerifyAccountId400Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VerifyAccountId400Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VerifyAccountId400Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VerifyAccountId400Response.class));

       return (TypeAdapter<T>) new TypeAdapter<VerifyAccountId400Response>() {
           @Override
           public void write(JsonWriter out, VerifyAccountId400Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VerifyAccountId400Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VerifyAccountId400Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VerifyAccountId400Response
   * @throws IOException if the JSON string is invalid with respect to VerifyAccountId400Response
   */
  public static VerifyAccountId400Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VerifyAccountId400Response.class);
  }

  /**
   * Convert an instance of VerifyAccountId400Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

