/*
 * FabricAdminClient
 * Volume operation endpoints and objects.
 *
 * The version of the OpenAPI document: 2016-05-01
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
 * Properties of a volume.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:19:37.928746-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VolumeModel {
  public static final String SERIALIZED_NAME_FILE_SYSTEM = "fileSystem";
  @SerializedName(SERIALIZED_NAME_FILE_SYSTEM)
  private String fileSystem;

  public static final String SERIALIZED_NAME_REMAINING_SIZE_G_B = "remainingSizeGB";
  @SerializedName(SERIALIZED_NAME_REMAINING_SIZE_G_B)
  private Integer remainingSizeGB;

  public static final String SERIALIZED_NAME_SIZE_G_B = "sizeGB";
  @SerializedName(SERIALIZED_NAME_SIZE_G_B)
  private Integer sizeGB;

  public static final String SERIALIZED_NAME_VOLUME_LABEL = "volumeLabel";
  @SerializedName(SERIALIZED_NAME_VOLUME_LABEL)
  private String volumeLabel;

  public VolumeModel() {
  }

  public VolumeModel fileSystem(String fileSystem) {
    this.fileSystem = fileSystem;
    return this;
  }

  /**
   * Filesystem type.
   * @return fileSystem
   */
  @javax.annotation.Nullable
  public String getFileSystem() {
    return fileSystem;
  }

  public void setFileSystem(String fileSystem) {
    this.fileSystem = fileSystem;
  }


  public VolumeModel remainingSizeGB(Integer remainingSizeGB) {
    this.remainingSizeGB = remainingSizeGB;
    return this;
  }

  /**
   * Amount of free space in GB.
   * @return remainingSizeGB
   */
  @javax.annotation.Nullable
  public Integer getRemainingSizeGB() {
    return remainingSizeGB;
  }

  public void setRemainingSizeGB(Integer remainingSizeGB) {
    this.remainingSizeGB = remainingSizeGB;
  }


  public VolumeModel sizeGB(Integer sizeGB) {
    this.sizeGB = sizeGB;
    return this;
  }

  /**
   * Total amount of space in GB.
   * @return sizeGB
   */
  @javax.annotation.Nullable
  public Integer getSizeGB() {
    return sizeGB;
  }

  public void setSizeGB(Integer sizeGB) {
    this.sizeGB = sizeGB;
  }


  public VolumeModel volumeLabel(String volumeLabel) {
    this.volumeLabel = volumeLabel;
    return this;
  }

  /**
   * Volume label.
   * @return volumeLabel
   */
  @javax.annotation.Nullable
  public String getVolumeLabel() {
    return volumeLabel;
  }

  public void setVolumeLabel(String volumeLabel) {
    this.volumeLabel = volumeLabel;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VolumeModel volumeModel = (VolumeModel) o;
    return Objects.equals(this.fileSystem, volumeModel.fileSystem) &&
        Objects.equals(this.remainingSizeGB, volumeModel.remainingSizeGB) &&
        Objects.equals(this.sizeGB, volumeModel.sizeGB) &&
        Objects.equals(this.volumeLabel, volumeModel.volumeLabel);
  }

  @Override
  public int hashCode() {
    return Objects.hash(fileSystem, remainingSizeGB, sizeGB, volumeLabel);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VolumeModel {\n");
    sb.append("    fileSystem: ").append(toIndentedString(fileSystem)).append("\n");
    sb.append("    remainingSizeGB: ").append(toIndentedString(remainingSizeGB)).append("\n");
    sb.append("    sizeGB: ").append(toIndentedString(sizeGB)).append("\n");
    sb.append("    volumeLabel: ").append(toIndentedString(volumeLabel)).append("\n");
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
    openapiFields.add("fileSystem");
    openapiFields.add("remainingSizeGB");
    openapiFields.add("sizeGB");
    openapiFields.add("volumeLabel");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VolumeModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VolumeModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VolumeModel is not found in the empty JSON string", VolumeModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VolumeModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VolumeModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("fileSystem") != null && !jsonObj.get("fileSystem").isJsonNull()) && !jsonObj.get("fileSystem").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fileSystem` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fileSystem").toString()));
      }
      if ((jsonObj.get("volumeLabel") != null && !jsonObj.get("volumeLabel").isJsonNull()) && !jsonObj.get("volumeLabel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `volumeLabel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("volumeLabel").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VolumeModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VolumeModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VolumeModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VolumeModel.class));

       return (TypeAdapter<T>) new TypeAdapter<VolumeModel>() {
           @Override
           public void write(JsonWriter out, VolumeModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VolumeModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VolumeModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VolumeModel
   * @throws IOException if the JSON string is invalid with respect to VolumeModel
   */
  public static VolumeModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VolumeModel.class);
  }

  /**
   * Convert an instance of VolumeModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

