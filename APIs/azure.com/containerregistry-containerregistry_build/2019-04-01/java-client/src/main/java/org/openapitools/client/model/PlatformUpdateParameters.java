/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-04-01
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
 * The properties for updating the platform configuration.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlatformUpdateParameters {
  /**
   * The OS architecture.
   */
  @JsonAdapter(ArchitectureEnum.Adapter.class)
  public enum ArchitectureEnum {
    AMD64("amd64"),
    
    X86("x86"),
    
    ARM("arm");

    private String value;

    ArchitectureEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ArchitectureEnum fromValue(String value) {
      for (ArchitectureEnum b : ArchitectureEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ArchitectureEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ArchitectureEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ArchitectureEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ArchitectureEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ArchitectureEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ARCHITECTURE = "architecture";
  @SerializedName(SERIALIZED_NAME_ARCHITECTURE)
  private ArchitectureEnum architecture;

  /**
   * The operating system type required for the run.
   */
  @JsonAdapter(OsEnum.Adapter.class)
  public enum OsEnum {
    WINDOWS("Windows"),
    
    LINUX("Linux");

    private String value;

    OsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OsEnum fromValue(String value) {
      for (OsEnum b : OsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_OS = "os";
  @SerializedName(SERIALIZED_NAME_OS)
  private OsEnum os;

  /**
   * Variant of the CPU.
   */
  @JsonAdapter(VariantEnum.Adapter.class)
  public enum VariantEnum {
    V6("v6"),
    
    V7("v7"),
    
    V8("v8");

    private String value;

    VariantEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static VariantEnum fromValue(String value) {
      for (VariantEnum b : VariantEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<VariantEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final VariantEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public VariantEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return VariantEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      VariantEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VARIANT = "variant";
  @SerializedName(SERIALIZED_NAME_VARIANT)
  private VariantEnum variant;

  public PlatformUpdateParameters() {
  }

  public PlatformUpdateParameters architecture(ArchitectureEnum architecture) {
    this.architecture = architecture;
    return this;
  }

  /**
   * The OS architecture.
   * @return architecture
   */
  @javax.annotation.Nullable
  public ArchitectureEnum getArchitecture() {
    return architecture;
  }

  public void setArchitecture(ArchitectureEnum architecture) {
    this.architecture = architecture;
  }


  public PlatformUpdateParameters os(OsEnum os) {
    this.os = os;
    return this;
  }

  /**
   * The operating system type required for the run.
   * @return os
   */
  @javax.annotation.Nullable
  public OsEnum getOs() {
    return os;
  }

  public void setOs(OsEnum os) {
    this.os = os;
  }


  public PlatformUpdateParameters variant(VariantEnum variant) {
    this.variant = variant;
    return this;
  }

  /**
   * Variant of the CPU.
   * @return variant
   */
  @javax.annotation.Nullable
  public VariantEnum getVariant() {
    return variant;
  }

  public void setVariant(VariantEnum variant) {
    this.variant = variant;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PlatformUpdateParameters platformUpdateParameters = (PlatformUpdateParameters) o;
    return Objects.equals(this.architecture, platformUpdateParameters.architecture) &&
        Objects.equals(this.os, platformUpdateParameters.os) &&
        Objects.equals(this.variant, platformUpdateParameters.variant);
  }

  @Override
  public int hashCode() {
    return Objects.hash(architecture, os, variant);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PlatformUpdateParameters {\n");
    sb.append("    architecture: ").append(toIndentedString(architecture)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    variant: ").append(toIndentedString(variant)).append("\n");
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
    openapiFields.add("architecture");
    openapiFields.add("os");
    openapiFields.add("variant");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlatformUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlatformUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlatformUpdateParameters is not found in the empty JSON string", PlatformUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlatformUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlatformUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("architecture") != null && !jsonObj.get("architecture").isJsonNull()) && !jsonObj.get("architecture").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `architecture` to be a primitive type in the JSON string but got `%s`", jsonObj.get("architecture").toString()));
      }
      // validate the optional field `architecture`
      if (jsonObj.get("architecture") != null && !jsonObj.get("architecture").isJsonNull()) {
        ArchitectureEnum.validateJsonElement(jsonObj.get("architecture"));
      }
      if ((jsonObj.get("os") != null && !jsonObj.get("os").isJsonNull()) && !jsonObj.get("os").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `os` to be a primitive type in the JSON string but got `%s`", jsonObj.get("os").toString()));
      }
      // validate the optional field `os`
      if (jsonObj.get("os") != null && !jsonObj.get("os").isJsonNull()) {
        OsEnum.validateJsonElement(jsonObj.get("os"));
      }
      if ((jsonObj.get("variant") != null && !jsonObj.get("variant").isJsonNull()) && !jsonObj.get("variant").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `variant` to be a primitive type in the JSON string but got `%s`", jsonObj.get("variant").toString()));
      }
      // validate the optional field `variant`
      if (jsonObj.get("variant") != null && !jsonObj.get("variant").isJsonNull()) {
        VariantEnum.validateJsonElement(jsonObj.get("variant"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlatformUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlatformUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlatformUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlatformUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<PlatformUpdateParameters>() {
           @Override
           public void write(JsonWriter out, PlatformUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlatformUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlatformUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlatformUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to PlatformUpdateParameters
   */
  public static PlatformUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlatformUpdateParameters.class);
  }

  /**
   * Convert an instance of PlatformUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

