/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
 * Set of multi-factor authentication policies
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateMfaPoliciesConfig {
  public static final String SERIALIZED_NAME_IS_MFA_ENFORCED = "isMfaEnforced";
  @SerializedName(SERIALIZED_NAME_IS_MFA_ENFORCED)
  private Boolean isMfaEnforced;

  public UpdateMfaPoliciesConfig() {
  }

  public UpdateMfaPoliciesConfig isMfaEnforced(Boolean isMfaEnforced) {
    this.isMfaEnforced = isMfaEnforced;
    return this;
  }

  /**
   * Determines whether multi-factor authentication is enforced
   * @return isMfaEnforced
   */
  @javax.annotation.Nonnull
  public Boolean getIsMfaEnforced() {
    return isMfaEnforced;
  }

  public void setIsMfaEnforced(Boolean isMfaEnforced) {
    this.isMfaEnforced = isMfaEnforced;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateMfaPoliciesConfig updateMfaPoliciesConfig = (UpdateMfaPoliciesConfig) o;
    return Objects.equals(this.isMfaEnforced, updateMfaPoliciesConfig.isMfaEnforced);
  }

  @Override
  public int hashCode() {
    return Objects.hash(isMfaEnforced);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateMfaPoliciesConfig {\n");
    sb.append("    isMfaEnforced: ").append(toIndentedString(isMfaEnforced)).append("\n");
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
    openapiFields.add("isMfaEnforced");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("isMfaEnforced");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateMfaPoliciesConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateMfaPoliciesConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateMfaPoliciesConfig is not found in the empty JSON string", UpdateMfaPoliciesConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateMfaPoliciesConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateMfaPoliciesConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateMfaPoliciesConfig.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateMfaPoliciesConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateMfaPoliciesConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateMfaPoliciesConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateMfaPoliciesConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateMfaPoliciesConfig>() {
           @Override
           public void write(JsonWriter out, UpdateMfaPoliciesConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateMfaPoliciesConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateMfaPoliciesConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateMfaPoliciesConfig
   * @throws IOException if the JSON string is invalid with respect to UpdateMfaPoliciesConfig
   */
  public static UpdateMfaPoliciesConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateMfaPoliciesConfig.class);
  }

  /**
   * Convert an instance of UpdateMfaPoliciesConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

