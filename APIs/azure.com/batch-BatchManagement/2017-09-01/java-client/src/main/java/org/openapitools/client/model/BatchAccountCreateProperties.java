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
import org.openapitools.client.model.AutoStorageBaseProperties;
import org.openapitools.client.model.KeyVaultReference;
import org.openapitools.client.model.PoolAllocationMode;

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
 * The properties of a Batch account.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:39.479442-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BatchAccountCreateProperties {
  public static final String SERIALIZED_NAME_AUTO_STORAGE = "autoStorage";
  @SerializedName(SERIALIZED_NAME_AUTO_STORAGE)
  private AutoStorageBaseProperties autoStorage;

  public static final String SERIALIZED_NAME_KEY_VAULT_REFERENCE = "keyVaultReference";
  @SerializedName(SERIALIZED_NAME_KEY_VAULT_REFERENCE)
  private KeyVaultReference keyVaultReference;

  public static final String SERIALIZED_NAME_POOL_ALLOCATION_MODE = "poolAllocationMode";
  @SerializedName(SERIALIZED_NAME_POOL_ALLOCATION_MODE)
  private PoolAllocationMode poolAllocationMode;

  public BatchAccountCreateProperties() {
  }

  public BatchAccountCreateProperties autoStorage(AutoStorageBaseProperties autoStorage) {
    this.autoStorage = autoStorage;
    return this;
  }

  /**
   * Get autoStorage
   * @return autoStorage
   */
  @javax.annotation.Nullable
  public AutoStorageBaseProperties getAutoStorage() {
    return autoStorage;
  }

  public void setAutoStorage(AutoStorageBaseProperties autoStorage) {
    this.autoStorage = autoStorage;
  }


  public BatchAccountCreateProperties keyVaultReference(KeyVaultReference keyVaultReference) {
    this.keyVaultReference = keyVaultReference;
    return this;
  }

  /**
   * Get keyVaultReference
   * @return keyVaultReference
   */
  @javax.annotation.Nullable
  public KeyVaultReference getKeyVaultReference() {
    return keyVaultReference;
  }

  public void setKeyVaultReference(KeyVaultReference keyVaultReference) {
    this.keyVaultReference = keyVaultReference;
  }


  public BatchAccountCreateProperties poolAllocationMode(PoolAllocationMode poolAllocationMode) {
    this.poolAllocationMode = poolAllocationMode;
    return this;
  }

  /**
   * Get poolAllocationMode
   * @return poolAllocationMode
   */
  @javax.annotation.Nullable
  public PoolAllocationMode getPoolAllocationMode() {
    return poolAllocationMode;
  }

  public void setPoolAllocationMode(PoolAllocationMode poolAllocationMode) {
    this.poolAllocationMode = poolAllocationMode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BatchAccountCreateProperties batchAccountCreateProperties = (BatchAccountCreateProperties) o;
    return Objects.equals(this.autoStorage, batchAccountCreateProperties.autoStorage) &&
        Objects.equals(this.keyVaultReference, batchAccountCreateProperties.keyVaultReference) &&
        Objects.equals(this.poolAllocationMode, batchAccountCreateProperties.poolAllocationMode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoStorage, keyVaultReference, poolAllocationMode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BatchAccountCreateProperties {\n");
    sb.append("    autoStorage: ").append(toIndentedString(autoStorage)).append("\n");
    sb.append("    keyVaultReference: ").append(toIndentedString(keyVaultReference)).append("\n");
    sb.append("    poolAllocationMode: ").append(toIndentedString(poolAllocationMode)).append("\n");
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
    openapiFields.add("autoStorage");
    openapiFields.add("keyVaultReference");
    openapiFields.add("poolAllocationMode");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BatchAccountCreateProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BatchAccountCreateProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BatchAccountCreateProperties is not found in the empty JSON string", BatchAccountCreateProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BatchAccountCreateProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BatchAccountCreateProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `autoStorage`
      if (jsonObj.get("autoStorage") != null && !jsonObj.get("autoStorage").isJsonNull()) {
        AutoStorageBaseProperties.validateJsonElement(jsonObj.get("autoStorage"));
      }
      // validate the optional field `keyVaultReference`
      if (jsonObj.get("keyVaultReference") != null && !jsonObj.get("keyVaultReference").isJsonNull()) {
        KeyVaultReference.validateJsonElement(jsonObj.get("keyVaultReference"));
      }
      // validate the optional field `poolAllocationMode`
      if (jsonObj.get("poolAllocationMode") != null && !jsonObj.get("poolAllocationMode").isJsonNull()) {
        PoolAllocationMode.validateJsonElement(jsonObj.get("poolAllocationMode"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BatchAccountCreateProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BatchAccountCreateProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BatchAccountCreateProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BatchAccountCreateProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<BatchAccountCreateProperties>() {
           @Override
           public void write(JsonWriter out, BatchAccountCreateProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BatchAccountCreateProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BatchAccountCreateProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BatchAccountCreateProperties
   * @throws IOException if the JSON string is invalid with respect to BatchAccountCreateProperties
   */
  public static BatchAccountCreateProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BatchAccountCreateProperties.class);
  }

  /**
   * Convert an instance of BatchAccountCreateProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

