/*
 * IoTSpacesClient
 * Use this API to manage the IoTSpaces service instances in your Azure subscription.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
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
 * The properties of the Azure Storage Container for file archive.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:35:12.658988-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StorageContainerProperties {
  public static final String SERIALIZED_NAME_CONNECTION_STRING = "connectionString";
  @SerializedName(SERIALIZED_NAME_CONNECTION_STRING)
  private String connectionString;

  public static final String SERIALIZED_NAME_CONTAINER_NAME = "containerName";
  @SerializedName(SERIALIZED_NAME_CONTAINER_NAME)
  private String containerName;

  public static final String SERIALIZED_NAME_RESOURCE_GROUP = "resourceGroup";
  @SerializedName(SERIALIZED_NAME_RESOURCE_GROUP)
  private String resourceGroup;

  public static final String SERIALIZED_NAME_SUBSCRIPTION_ID = "subscriptionId";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTION_ID)
  private String subscriptionId;

  public StorageContainerProperties() {
  }

  public StorageContainerProperties connectionString(String connectionString) {
    this.connectionString = connectionString;
    return this;
  }

  /**
   * The connection string of the storage account.
   * @return connectionString
   */
  @javax.annotation.Nullable
  public String getConnectionString() {
    return connectionString;
  }

  public void setConnectionString(String connectionString) {
    this.connectionString = connectionString;
  }


  public StorageContainerProperties containerName(String containerName) {
    this.containerName = containerName;
    return this;
  }

  /**
   * The name of storage container in the storage account.
   * @return containerName
   */
  @javax.annotation.Nullable
  public String getContainerName() {
    return containerName;
  }

  public void setContainerName(String containerName) {
    this.containerName = containerName;
  }


  public StorageContainerProperties resourceGroup(String resourceGroup) {
    this.resourceGroup = resourceGroup;
    return this;
  }

  /**
   * The name of the resource group of the storage account.
   * @return resourceGroup
   */
  @javax.annotation.Nullable
  public String getResourceGroup() {
    return resourceGroup;
  }

  public void setResourceGroup(String resourceGroup) {
    this.resourceGroup = resourceGroup;
  }


  public StorageContainerProperties subscriptionId(String subscriptionId) {
    this.subscriptionId = subscriptionId;
    return this;
  }

  /**
   * The subscription identifier of the storage account.
   * @return subscriptionId
   */
  @javax.annotation.Nullable
  public String getSubscriptionId() {
    return subscriptionId;
  }

  public void setSubscriptionId(String subscriptionId) {
    this.subscriptionId = subscriptionId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StorageContainerProperties storageContainerProperties = (StorageContainerProperties) o;
    return Objects.equals(this.connectionString, storageContainerProperties.connectionString) &&
        Objects.equals(this.containerName, storageContainerProperties.containerName) &&
        Objects.equals(this.resourceGroup, storageContainerProperties.resourceGroup) &&
        Objects.equals(this.subscriptionId, storageContainerProperties.subscriptionId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(connectionString, containerName, resourceGroup, subscriptionId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StorageContainerProperties {\n");
    sb.append("    connectionString: ").append(toIndentedString(connectionString)).append("\n");
    sb.append("    containerName: ").append(toIndentedString(containerName)).append("\n");
    sb.append("    resourceGroup: ").append(toIndentedString(resourceGroup)).append("\n");
    sb.append("    subscriptionId: ").append(toIndentedString(subscriptionId)).append("\n");
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
    openapiFields.add("connectionString");
    openapiFields.add("containerName");
    openapiFields.add("resourceGroup");
    openapiFields.add("subscriptionId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StorageContainerProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StorageContainerProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StorageContainerProperties is not found in the empty JSON string", StorageContainerProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StorageContainerProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StorageContainerProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("connectionString") != null && !jsonObj.get("connectionString").isJsonNull()) && !jsonObj.get("connectionString").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `connectionString` to be a primitive type in the JSON string but got `%s`", jsonObj.get("connectionString").toString()));
      }
      if ((jsonObj.get("containerName") != null && !jsonObj.get("containerName").isJsonNull()) && !jsonObj.get("containerName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `containerName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("containerName").toString()));
      }
      if ((jsonObj.get("resourceGroup") != null && !jsonObj.get("resourceGroup").isJsonNull()) && !jsonObj.get("resourceGroup").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceGroup` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceGroup").toString()));
      }
      if ((jsonObj.get("subscriptionId") != null && !jsonObj.get("subscriptionId").isJsonNull()) && !jsonObj.get("subscriptionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriptionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriptionId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StorageContainerProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StorageContainerProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StorageContainerProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StorageContainerProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<StorageContainerProperties>() {
           @Override
           public void write(JsonWriter out, StorageContainerProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StorageContainerProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StorageContainerProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StorageContainerProperties
   * @throws IOException if the JSON string is invalid with respect to StorageContainerProperties
   */
  public static StorageContainerProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StorageContainerProperties.class);
  }

  /**
   * Convert an instance of StorageContainerProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

