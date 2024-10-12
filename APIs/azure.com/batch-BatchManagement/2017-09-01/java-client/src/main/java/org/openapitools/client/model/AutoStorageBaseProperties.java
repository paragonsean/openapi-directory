/*
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
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
 * The properties related to the auto-storage account.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:39.479442-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AutoStorageBaseProperties {
  public static final String SERIALIZED_NAME_STORAGE_ACCOUNT_ID = "storageAccountId";
  @SerializedName(SERIALIZED_NAME_STORAGE_ACCOUNT_ID)
  private String storageAccountId;

  public AutoStorageBaseProperties() {
  }

  public AutoStorageBaseProperties storageAccountId(String storageAccountId) {
    this.storageAccountId = storageAccountId;
    return this;
  }

  /**
   * The resource ID of the storage account to be used for auto-storage account.
   * @return storageAccountId
   */
  @javax.annotation.Nonnull
  public String getStorageAccountId() {
    return storageAccountId;
  }

  public void setStorageAccountId(String storageAccountId) {
    this.storageAccountId = storageAccountId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AutoStorageBaseProperties autoStorageBaseProperties = (AutoStorageBaseProperties) o;
    return Objects.equals(this.storageAccountId, autoStorageBaseProperties.storageAccountId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(storageAccountId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AutoStorageBaseProperties {\n");
    sb.append("    storageAccountId: ").append(toIndentedString(storageAccountId)).append("\n");
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
    openapiFields.add("storageAccountId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("storageAccountId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AutoStorageBaseProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AutoStorageBaseProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AutoStorageBaseProperties is not found in the empty JSON string", AutoStorageBaseProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AutoStorageBaseProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AutoStorageBaseProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AutoStorageBaseProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("storageAccountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `storageAccountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("storageAccountId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AutoStorageBaseProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AutoStorageBaseProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AutoStorageBaseProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AutoStorageBaseProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<AutoStorageBaseProperties>() {
           @Override
           public void write(JsonWriter out, AutoStorageBaseProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AutoStorageBaseProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AutoStorageBaseProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AutoStorageBaseProperties
   * @throws IOException if the JSON string is invalid with respect to AutoStorageBaseProperties
   */
  public static AutoStorageBaseProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AutoStorageBaseProperties.class);
  }

  /**
   * Convert an instance of AutoStorageBaseProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

