/*
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
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
import java.time.OffsetDateTime;
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
 * KeyObject
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:45.290770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class KeyObject {
  public static final String SERIALIZED_NAME_EXPIRY = "expiry";
  @SerializedName(SERIALIZED_NAME_EXPIRY)
  private OffsetDateTime expiry;

  public static final String SERIALIZED_NAME_KEY_VALUE = "keyValue";
  @SerializedName(SERIALIZED_NAME_KEY_VALUE)
  private String keyValue;

  public static final String SERIALIZED_NAME_PARAMETERS = "parameters";
  @SerializedName(SERIALIZED_NAME_PARAMETERS)
  private String parameters;

  public KeyObject() {
  }

  public KeyObject expiry(OffsetDateTime expiry) {
    this.expiry = expiry;
    return this;
  }

  /**
   * Get expiry
   * @return expiry
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getExpiry() {
    return expiry;
  }

  public void setExpiry(OffsetDateTime expiry) {
    this.expiry = expiry;
  }


  public KeyObject keyValue(String keyValue) {
    this.keyValue = keyValue;
    return this;
  }

  /**
   * Get keyValue
   * @return keyValue
   */
  @javax.annotation.Nonnull
  public String getKeyValue() {
    return keyValue;
  }

  public void setKeyValue(String keyValue) {
    this.keyValue = keyValue;
  }


  public KeyObject parameters(String parameters) {
    this.parameters = parameters;
    return this;
  }

  /**
   * Get parameters
   * @return parameters
   */
  @javax.annotation.Nonnull
  public String getParameters() {
    return parameters;
  }

  public void setParameters(String parameters) {
    this.parameters = parameters;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    KeyObject keyObject = (KeyObject) o;
    return Objects.equals(this.expiry, keyObject.expiry) &&
        Objects.equals(this.keyValue, keyObject.keyValue) &&
        Objects.equals(this.parameters, keyObject.parameters);
  }

  @Override
  public int hashCode() {
    return Objects.hash(expiry, keyValue, parameters);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class KeyObject {\n");
    sb.append("    expiry: ").append(toIndentedString(expiry)).append("\n");
    sb.append("    keyValue: ").append(toIndentedString(keyValue)).append("\n");
    sb.append("    parameters: ").append(toIndentedString(parameters)).append("\n");
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
    openapiFields.add("expiry");
    openapiFields.add("keyValue");
    openapiFields.add("parameters");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("expiry");
    openapiRequiredFields.add("keyValue");
    openapiRequiredFields.add("parameters");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to KeyObject
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!KeyObject.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in KeyObject is not found in the empty JSON string", KeyObject.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!KeyObject.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `KeyObject` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : KeyObject.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("keyValue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `keyValue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("keyValue").toString()));
      }
      if (!jsonObj.get("parameters").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parameters` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parameters").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!KeyObject.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'KeyObject' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<KeyObject> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(KeyObject.class));

       return (TypeAdapter<T>) new TypeAdapter<KeyObject>() {
           @Override
           public void write(JsonWriter out, KeyObject value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public KeyObject read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of KeyObject given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of KeyObject
   * @throws IOException if the JSON string is invalid with respect to KeyObject
   */
  public static KeyObject fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, KeyObject.class);
  }

  /**
   * Convert an instance of KeyObject to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

