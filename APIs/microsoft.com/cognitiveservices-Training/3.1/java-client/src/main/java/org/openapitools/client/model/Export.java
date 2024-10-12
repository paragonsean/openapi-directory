/*
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
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
 * Export
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:13.015357-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Export {
  public static final String SERIALIZED_NAME_DOWNLOAD_URI = "downloadUri";
  @SerializedName(SERIALIZED_NAME_DOWNLOAD_URI)
  private String downloadUri;

  /**
   * Flavor of the export.
   */
  @JsonAdapter(FlavorEnum.Adapter.class)
  public enum FlavorEnum {
    LINUX("Linux"),
    
    WINDOWS("Windows"),
    
    ONNX10("ONNX10"),
    
    ONNX12("ONNX12"),
    
    ARM("ARM"),
    
    TENSOR_FLOW_NORMAL("TensorFlowNormal"),
    
    TENSOR_FLOW_LITE("TensorFlowLite");

    private String value;

    FlavorEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static FlavorEnum fromValue(String value) {
      for (FlavorEnum b : FlavorEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      return null;
    }

    public static class Adapter extends TypeAdapter<FlavorEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final FlavorEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public FlavorEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return FlavorEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      FlavorEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_FLAVOR = "flavor";
  @SerializedName(SERIALIZED_NAME_FLAVOR)
  private FlavorEnum flavor;

  public static final String SERIALIZED_NAME_NEWER_VERSION_AVAILABLE = "newerVersionAvailable";
  @SerializedName(SERIALIZED_NAME_NEWER_VERSION_AVAILABLE)
  private Boolean newerVersionAvailable;

  /**
   * Platform of the export.
   */
  @JsonAdapter(PlatformEnum.Adapter.class)
  public enum PlatformEnum {
    CORE_ML("CoreML"),
    
    TENSOR_FLOW("TensorFlow"),
    
    DOCKER_FILE("DockerFile"),
    
    ONNX("ONNX"),
    
    VAIDK("VAIDK");

    private String value;

    PlatformEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PlatformEnum fromValue(String value) {
      for (PlatformEnum b : PlatformEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PlatformEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PlatformEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PlatformEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PlatformEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PlatformEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PLATFORM = "platform";
  @SerializedName(SERIALIZED_NAME_PLATFORM)
  private PlatformEnum platform;

  /**
   * Status of the export.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    EXPORTING("Exporting"),
    
    FAILED("Failed"),
    
    DONE("Done");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public Export() {
  }

  public Export(
     String downloadUri, 
     FlavorEnum flavor, 
     Boolean newerVersionAvailable, 
     PlatformEnum platform, 
     StatusEnum status
  ) {
    this();
    this.downloadUri = downloadUri;
    this.flavor = flavor;
    this.newerVersionAvailable = newerVersionAvailable;
    this.platform = platform;
    this.status = status;
  }

  /**
   * URI used to download the model.
   * @return downloadUri
   */
  @javax.annotation.Nullable
  public String getDownloadUri() {
    return downloadUri;
  }



  /**
   * Flavor of the export.
   * @return flavor
   */
  @javax.annotation.Nullable
  public FlavorEnum getFlavor() {
    return flavor;
  }



  /**
   * Indicates an updated version of the export package is available and should be re-exported for the latest changes.
   * @return newerVersionAvailable
   */
  @javax.annotation.Nullable
  public Boolean getNewerVersionAvailable() {
    return newerVersionAvailable;
  }



  /**
   * Platform of the export.
   * @return platform
   */
  @javax.annotation.Nullable
  public PlatformEnum getPlatform() {
    return platform;
  }



  /**
   * Status of the export.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Export export = (Export) o;
    return Objects.equals(this.downloadUri, export.downloadUri) &&
        Objects.equals(this.flavor, export.flavor) &&
        Objects.equals(this.newerVersionAvailable, export.newerVersionAvailable) &&
        Objects.equals(this.platform, export.platform) &&
        Objects.equals(this.status, export.status);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(downloadUri, flavor, newerVersionAvailable, platform, status);
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
    sb.append("class Export {\n");
    sb.append("    downloadUri: ").append(toIndentedString(downloadUri)).append("\n");
    sb.append("    flavor: ").append(toIndentedString(flavor)).append("\n");
    sb.append("    newerVersionAvailable: ").append(toIndentedString(newerVersionAvailable)).append("\n");
    sb.append("    platform: ").append(toIndentedString(platform)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("downloadUri");
    openapiFields.add("flavor");
    openapiFields.add("newerVersionAvailable");
    openapiFields.add("platform");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Export
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Export.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Export is not found in the empty JSON string", Export.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Export.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Export` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("downloadUri") != null && !jsonObj.get("downloadUri").isJsonNull()) && !jsonObj.get("downloadUri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `downloadUri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("downloadUri").toString()));
      }
      if ((jsonObj.get("flavor") != null && !jsonObj.get("flavor").isJsonNull()) && !jsonObj.get("flavor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `flavor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("flavor").toString()));
      }
      // validate the optional field `flavor`
      if (jsonObj.get("flavor") != null && !jsonObj.get("flavor").isJsonNull()) {
        FlavorEnum.validateJsonElement(jsonObj.get("flavor"));
      }
      if ((jsonObj.get("platform") != null && !jsonObj.get("platform").isJsonNull()) && !jsonObj.get("platform").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `platform` to be a primitive type in the JSON string but got `%s`", jsonObj.get("platform").toString()));
      }
      // validate the optional field `platform`
      if (jsonObj.get("platform") != null && !jsonObj.get("platform").isJsonNull()) {
        PlatformEnum.validateJsonElement(jsonObj.get("platform"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Export.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Export' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Export> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Export.class));

       return (TypeAdapter<T>) new TypeAdapter<Export>() {
           @Override
           public void write(JsonWriter out, Export value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Export read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Export given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Export
   * @throws IOException if the JSON string is invalid with respect to Export
   */
  public static Export fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Export.class);
  }

  /**
   * Convert an instance of Export to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

