/*
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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
 * The backup element.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:41.316643-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BackupElement {
  public static final String SERIALIZED_NAME_ELEMENT_ID = "elementId";
  @SerializedName(SERIALIZED_NAME_ELEMENT_ID)
  private String elementId;

  public static final String SERIALIZED_NAME_ELEMENT_NAME = "elementName";
  @SerializedName(SERIALIZED_NAME_ELEMENT_NAME)
  private String elementName;

  public static final String SERIALIZED_NAME_ELEMENT_TYPE = "elementType";
  @SerializedName(SERIALIZED_NAME_ELEMENT_TYPE)
  private String elementType;

  public static final String SERIALIZED_NAME_SIZE_IN_BYTES = "sizeInBytes";
  @SerializedName(SERIALIZED_NAME_SIZE_IN_BYTES)
  private Long sizeInBytes;

  public static final String SERIALIZED_NAME_VOLUME_CONTAINER_ID = "volumeContainerId";
  @SerializedName(SERIALIZED_NAME_VOLUME_CONTAINER_ID)
  private String volumeContainerId;

  public static final String SERIALIZED_NAME_VOLUME_NAME = "volumeName";
  @SerializedName(SERIALIZED_NAME_VOLUME_NAME)
  private String volumeName;

  /**
   * The volume type.
   */
  @JsonAdapter(VolumeTypeEnum.Adapter.class)
  public enum VolumeTypeEnum {
    TIERED("Tiered"),
    
    ARCHIVAL("Archival"),
    
    LOCALLY_PINNED("LocallyPinned");

    private String value;

    VolumeTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static VolumeTypeEnum fromValue(String value) {
      for (VolumeTypeEnum b : VolumeTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<VolumeTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final VolumeTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public VolumeTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return VolumeTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      VolumeTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VOLUME_TYPE = "volumeType";
  @SerializedName(SERIALIZED_NAME_VOLUME_TYPE)
  private VolumeTypeEnum volumeType;

  public BackupElement() {
  }

  public BackupElement elementId(String elementId) {
    this.elementId = elementId;
    return this;
  }

  /**
   * The path ID that uniquely identifies the backup element.
   * @return elementId
   */
  @javax.annotation.Nonnull
  public String getElementId() {
    return elementId;
  }

  public void setElementId(String elementId) {
    this.elementId = elementId;
  }


  public BackupElement elementName(String elementName) {
    this.elementName = elementName;
    return this;
  }

  /**
   * The name of the backup element.
   * @return elementName
   */
  @javax.annotation.Nonnull
  public String getElementName() {
    return elementName;
  }

  public void setElementName(String elementName) {
    this.elementName = elementName;
  }


  public BackupElement elementType(String elementType) {
    this.elementType = elementType;
    return this;
  }

  /**
   * The hierarchical type of the backup element.
   * @return elementType
   */
  @javax.annotation.Nonnull
  public String getElementType() {
    return elementType;
  }

  public void setElementType(String elementType) {
    this.elementType = elementType;
  }


  public BackupElement sizeInBytes(Long sizeInBytes) {
    this.sizeInBytes = sizeInBytes;
    return this;
  }

  /**
   * The size in bytes.
   * @return sizeInBytes
   */
  @javax.annotation.Nonnull
  public Long getSizeInBytes() {
    return sizeInBytes;
  }

  public void setSizeInBytes(Long sizeInBytes) {
    this.sizeInBytes = sizeInBytes;
  }


  public BackupElement volumeContainerId(String volumeContainerId) {
    this.volumeContainerId = volumeContainerId;
    return this;
  }

  /**
   * The path ID of the volume container.
   * @return volumeContainerId
   */
  @javax.annotation.Nonnull
  public String getVolumeContainerId() {
    return volumeContainerId;
  }

  public void setVolumeContainerId(String volumeContainerId) {
    this.volumeContainerId = volumeContainerId;
  }


  public BackupElement volumeName(String volumeName) {
    this.volumeName = volumeName;
    return this;
  }

  /**
   * The name of the volume.
   * @return volumeName
   */
  @javax.annotation.Nonnull
  public String getVolumeName() {
    return volumeName;
  }

  public void setVolumeName(String volumeName) {
    this.volumeName = volumeName;
  }


  public BackupElement volumeType(VolumeTypeEnum volumeType) {
    this.volumeType = volumeType;
    return this;
  }

  /**
   * The volume type.
   * @return volumeType
   */
  @javax.annotation.Nullable
  public VolumeTypeEnum getVolumeType() {
    return volumeType;
  }

  public void setVolumeType(VolumeTypeEnum volumeType) {
    this.volumeType = volumeType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BackupElement backupElement = (BackupElement) o;
    return Objects.equals(this.elementId, backupElement.elementId) &&
        Objects.equals(this.elementName, backupElement.elementName) &&
        Objects.equals(this.elementType, backupElement.elementType) &&
        Objects.equals(this.sizeInBytes, backupElement.sizeInBytes) &&
        Objects.equals(this.volumeContainerId, backupElement.volumeContainerId) &&
        Objects.equals(this.volumeName, backupElement.volumeName) &&
        Objects.equals(this.volumeType, backupElement.volumeType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(elementId, elementName, elementType, sizeInBytes, volumeContainerId, volumeName, volumeType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BackupElement {\n");
    sb.append("    elementId: ").append(toIndentedString(elementId)).append("\n");
    sb.append("    elementName: ").append(toIndentedString(elementName)).append("\n");
    sb.append("    elementType: ").append(toIndentedString(elementType)).append("\n");
    sb.append("    sizeInBytes: ").append(toIndentedString(sizeInBytes)).append("\n");
    sb.append("    volumeContainerId: ").append(toIndentedString(volumeContainerId)).append("\n");
    sb.append("    volumeName: ").append(toIndentedString(volumeName)).append("\n");
    sb.append("    volumeType: ").append(toIndentedString(volumeType)).append("\n");
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
    openapiFields.add("elementId");
    openapiFields.add("elementName");
    openapiFields.add("elementType");
    openapiFields.add("sizeInBytes");
    openapiFields.add("volumeContainerId");
    openapiFields.add("volumeName");
    openapiFields.add("volumeType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("elementId");
    openapiRequiredFields.add("elementName");
    openapiRequiredFields.add("elementType");
    openapiRequiredFields.add("sizeInBytes");
    openapiRequiredFields.add("volumeContainerId");
    openapiRequiredFields.add("volumeName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BackupElement
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BackupElement.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BackupElement is not found in the empty JSON string", BackupElement.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BackupElement.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BackupElement` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BackupElement.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("elementId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `elementId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("elementId").toString()));
      }
      if (!jsonObj.get("elementName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `elementName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("elementName").toString()));
      }
      if (!jsonObj.get("elementType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `elementType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("elementType").toString()));
      }
      if (!jsonObj.get("volumeContainerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `volumeContainerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("volumeContainerId").toString()));
      }
      if (!jsonObj.get("volumeName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `volumeName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("volumeName").toString()));
      }
      if ((jsonObj.get("volumeType") != null && !jsonObj.get("volumeType").isJsonNull()) && !jsonObj.get("volumeType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `volumeType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("volumeType").toString()));
      }
      // validate the optional field `volumeType`
      if (jsonObj.get("volumeType") != null && !jsonObj.get("volumeType").isJsonNull()) {
        VolumeTypeEnum.validateJsonElement(jsonObj.get("volumeType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BackupElement.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BackupElement' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BackupElement> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BackupElement.class));

       return (TypeAdapter<T>) new TypeAdapter<BackupElement>() {
           @Override
           public void write(JsonWriter out, BackupElement value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BackupElement read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BackupElement given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BackupElement
   * @throws IOException if the JSON string is invalid with respect to BackupElement
   */
  public static BackupElement fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BackupElement.class);
  }

  /**
   * Convert an instance of BackupElement to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

