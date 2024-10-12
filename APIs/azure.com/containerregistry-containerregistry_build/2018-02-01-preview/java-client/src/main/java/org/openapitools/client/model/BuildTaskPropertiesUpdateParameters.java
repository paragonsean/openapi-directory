/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
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
import org.openapitools.client.model.PlatformProperties;
import org.openapitools.client.model.SourceRepositoryUpdateParameters;

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
 * The properties for updating a build task.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:59.640634-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BuildTaskPropertiesUpdateParameters {
  public static final String SERIALIZED_NAME_ALIAS = "alias";
  @SerializedName(SERIALIZED_NAME_ALIAS)
  private String alias;

  public static final String SERIALIZED_NAME_PLATFORM = "platform";
  @SerializedName(SERIALIZED_NAME_PLATFORM)
  private PlatformProperties platform;

  public static final String SERIALIZED_NAME_SOURCE_REPOSITORY = "sourceRepository";
  @SerializedName(SERIALIZED_NAME_SOURCE_REPOSITORY)
  private SourceRepositoryUpdateParameters sourceRepository;

  /**
   * The current status of build task.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    DISABLED("Disabled"),
    
    ENABLED("Enabled");

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

  public static final String SERIALIZED_NAME_TIMEOUT = "timeout";
  @SerializedName(SERIALIZED_NAME_TIMEOUT)
  private Integer timeout;

  public BuildTaskPropertiesUpdateParameters() {
  }

  public BuildTaskPropertiesUpdateParameters alias(String alias) {
    this.alias = alias;
    return this;
  }

  /**
   * The alternative updatable name for a build task.
   * @return alias
   */
  @javax.annotation.Nullable
  public String getAlias() {
    return alias;
  }

  public void setAlias(String alias) {
    this.alias = alias;
  }


  public BuildTaskPropertiesUpdateParameters platform(PlatformProperties platform) {
    this.platform = platform;
    return this;
  }

  /**
   * Get platform
   * @return platform
   */
  @javax.annotation.Nullable
  public PlatformProperties getPlatform() {
    return platform;
  }

  public void setPlatform(PlatformProperties platform) {
    this.platform = platform;
  }


  public BuildTaskPropertiesUpdateParameters sourceRepository(SourceRepositoryUpdateParameters sourceRepository) {
    this.sourceRepository = sourceRepository;
    return this;
  }

  /**
   * Get sourceRepository
   * @return sourceRepository
   */
  @javax.annotation.Nullable
  public SourceRepositoryUpdateParameters getSourceRepository() {
    return sourceRepository;
  }

  public void setSourceRepository(SourceRepositoryUpdateParameters sourceRepository) {
    this.sourceRepository = sourceRepository;
  }


  public BuildTaskPropertiesUpdateParameters status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * The current status of build task.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public BuildTaskPropertiesUpdateParameters timeout(Integer timeout) {
    this.timeout = timeout;
    return this;
  }

  /**
   * Build timeout in seconds.
   * minimum: 300
   * maximum: 28800
   * @return timeout
   */
  @javax.annotation.Nullable
  public Integer getTimeout() {
    return timeout;
  }

  public void setTimeout(Integer timeout) {
    this.timeout = timeout;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BuildTaskPropertiesUpdateParameters buildTaskPropertiesUpdateParameters = (BuildTaskPropertiesUpdateParameters) o;
    return Objects.equals(this.alias, buildTaskPropertiesUpdateParameters.alias) &&
        Objects.equals(this.platform, buildTaskPropertiesUpdateParameters.platform) &&
        Objects.equals(this.sourceRepository, buildTaskPropertiesUpdateParameters.sourceRepository) &&
        Objects.equals(this.status, buildTaskPropertiesUpdateParameters.status) &&
        Objects.equals(this.timeout, buildTaskPropertiesUpdateParameters.timeout);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alias, platform, sourceRepository, status, timeout);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BuildTaskPropertiesUpdateParameters {\n");
    sb.append("    alias: ").append(toIndentedString(alias)).append("\n");
    sb.append("    platform: ").append(toIndentedString(platform)).append("\n");
    sb.append("    sourceRepository: ").append(toIndentedString(sourceRepository)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    timeout: ").append(toIndentedString(timeout)).append("\n");
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
    openapiFields.add("alias");
    openapiFields.add("platform");
    openapiFields.add("sourceRepository");
    openapiFields.add("status");
    openapiFields.add("timeout");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BuildTaskPropertiesUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BuildTaskPropertiesUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BuildTaskPropertiesUpdateParameters is not found in the empty JSON string", BuildTaskPropertiesUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BuildTaskPropertiesUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BuildTaskPropertiesUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("alias") != null && !jsonObj.get("alias").isJsonNull()) && !jsonObj.get("alias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alias").toString()));
      }
      // validate the optional field `platform`
      if (jsonObj.get("platform") != null && !jsonObj.get("platform").isJsonNull()) {
        PlatformProperties.validateJsonElement(jsonObj.get("platform"));
      }
      // validate the optional field `sourceRepository`
      if (jsonObj.get("sourceRepository") != null && !jsonObj.get("sourceRepository").isJsonNull()) {
        SourceRepositoryUpdateParameters.validateJsonElement(jsonObj.get("sourceRepository"));
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
       if (!BuildTaskPropertiesUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BuildTaskPropertiesUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BuildTaskPropertiesUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BuildTaskPropertiesUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<BuildTaskPropertiesUpdateParameters>() {
           @Override
           public void write(JsonWriter out, BuildTaskPropertiesUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BuildTaskPropertiesUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BuildTaskPropertiesUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BuildTaskPropertiesUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to BuildTaskPropertiesUpdateParameters
   */
  public static BuildTaskPropertiesUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BuildTaskPropertiesUpdateParameters.class);
  }

  /**
   * Convert an instance of BuildTaskPropertiesUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

