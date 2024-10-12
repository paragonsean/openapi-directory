/*
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
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
 * Azure container mapping of the endpoint.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:10.716364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AzureContainerInfo {
  public static final String SERIALIZED_NAME_CONTAINER_NAME = "containerName";
  @SerializedName(SERIALIZED_NAME_CONTAINER_NAME)
  private String containerName;

  /**
   * Storage format used for the file represented by the share.
   */
  @JsonAdapter(DataFormatEnum.Adapter.class)
  public enum DataFormatEnum {
    BLOCK_BLOB("BlockBlob"),
    
    PAGE_BLOB("PageBlob"),
    
    AZURE_FILE("AzureFile");

    private String value;

    DataFormatEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static DataFormatEnum fromValue(String value) {
      for (DataFormatEnum b : DataFormatEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<DataFormatEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final DataFormatEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public DataFormatEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return DataFormatEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      DataFormatEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_DATA_FORMAT = "dataFormat";
  @SerializedName(SERIALIZED_NAME_DATA_FORMAT)
  private DataFormatEnum dataFormat;

  public static final String SERIALIZED_NAME_STORAGE_ACCOUNT_CREDENTIAL_ID = "storageAccountCredentialId";
  @SerializedName(SERIALIZED_NAME_STORAGE_ACCOUNT_CREDENTIAL_ID)
  private String storageAccountCredentialId;

  public AzureContainerInfo() {
  }

  public AzureContainerInfo containerName(String containerName) {
    this.containerName = containerName;
    return this;
  }

  /**
   * Container name (Based on the data format specified, this represents the name of Azure Files/Page blob/Block blob).
   * @return containerName
   */
  @javax.annotation.Nonnull
  public String getContainerName() {
    return containerName;
  }

  public void setContainerName(String containerName) {
    this.containerName = containerName;
  }


  public AzureContainerInfo dataFormat(DataFormatEnum dataFormat) {
    this.dataFormat = dataFormat;
    return this;
  }

  /**
   * Storage format used for the file represented by the share.
   * @return dataFormat
   */
  @javax.annotation.Nonnull
  public DataFormatEnum getDataFormat() {
    return dataFormat;
  }

  public void setDataFormat(DataFormatEnum dataFormat) {
    this.dataFormat = dataFormat;
  }


  public AzureContainerInfo storageAccountCredentialId(String storageAccountCredentialId) {
    this.storageAccountCredentialId = storageAccountCredentialId;
    return this;
  }

  /**
   * ID of the storage account credential used to access storage.
   * @return storageAccountCredentialId
   */
  @javax.annotation.Nonnull
  public String getStorageAccountCredentialId() {
    return storageAccountCredentialId;
  }

  public void setStorageAccountCredentialId(String storageAccountCredentialId) {
    this.storageAccountCredentialId = storageAccountCredentialId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AzureContainerInfo azureContainerInfo = (AzureContainerInfo) o;
    return Objects.equals(this.containerName, azureContainerInfo.containerName) &&
        Objects.equals(this.dataFormat, azureContainerInfo.dataFormat) &&
        Objects.equals(this.storageAccountCredentialId, azureContainerInfo.storageAccountCredentialId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(containerName, dataFormat, storageAccountCredentialId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AzureContainerInfo {\n");
    sb.append("    containerName: ").append(toIndentedString(containerName)).append("\n");
    sb.append("    dataFormat: ").append(toIndentedString(dataFormat)).append("\n");
    sb.append("    storageAccountCredentialId: ").append(toIndentedString(storageAccountCredentialId)).append("\n");
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
    openapiFields.add("containerName");
    openapiFields.add("dataFormat");
    openapiFields.add("storageAccountCredentialId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("containerName");
    openapiRequiredFields.add("dataFormat");
    openapiRequiredFields.add("storageAccountCredentialId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AzureContainerInfo
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AzureContainerInfo.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AzureContainerInfo is not found in the empty JSON string", AzureContainerInfo.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AzureContainerInfo.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AzureContainerInfo` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AzureContainerInfo.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("containerName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `containerName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("containerName").toString()));
      }
      if (!jsonObj.get("dataFormat").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dataFormat` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dataFormat").toString()));
      }
      // validate the required field `dataFormat`
      DataFormatEnum.validateJsonElement(jsonObj.get("dataFormat"));
      if (!jsonObj.get("storageAccountCredentialId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `storageAccountCredentialId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("storageAccountCredentialId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AzureContainerInfo.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AzureContainerInfo' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AzureContainerInfo> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AzureContainerInfo.class));

       return (TypeAdapter<T>) new TypeAdapter<AzureContainerInfo>() {
           @Override
           public void write(JsonWriter out, AzureContainerInfo value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AzureContainerInfo read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AzureContainerInfo given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AzureContainerInfo
   * @throws IOException if the JSON string is invalid with respect to AzureContainerInfo
   */
  public static AzureContainerInfo fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AzureContainerInfo.class);
  }

  /**
   * Convert an instance of AzureContainerInfo to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

