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
import org.openapitools.client.model.AuthInfo;

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
 * The properties of the source code repository.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SourceProperties {
  public static final String SERIALIZED_NAME_BRANCH = "branch";
  @SerializedName(SERIALIZED_NAME_BRANCH)
  private String branch;

  public static final String SERIALIZED_NAME_REPOSITORY_URL = "repositoryUrl";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_URL)
  private String repositoryUrl;

  public static final String SERIALIZED_NAME_SOURCE_CONTROL_AUTH_PROPERTIES = "sourceControlAuthProperties";
  @SerializedName(SERIALIZED_NAME_SOURCE_CONTROL_AUTH_PROPERTIES)
  private AuthInfo sourceControlAuthProperties;

  /**
   * The type of source control service.
   */
  @JsonAdapter(SourceControlTypeEnum.Adapter.class)
  public enum SourceControlTypeEnum {
    GITHUB("Github"),
    
    VISUAL_STUDIO_TEAM_SERVICE("VisualStudioTeamService");

    private String value;

    SourceControlTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SourceControlTypeEnum fromValue(String value) {
      for (SourceControlTypeEnum b : SourceControlTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SourceControlTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SourceControlTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SourceControlTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SourceControlTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SourceControlTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SOURCE_CONTROL_TYPE = "sourceControlType";
  @SerializedName(SERIALIZED_NAME_SOURCE_CONTROL_TYPE)
  private SourceControlTypeEnum sourceControlType;

  public SourceProperties() {
  }

  public SourceProperties branch(String branch) {
    this.branch = branch;
    return this;
  }

  /**
   * The branch name of the source code.
   * @return branch
   */
  @javax.annotation.Nullable
  public String getBranch() {
    return branch;
  }

  public void setBranch(String branch) {
    this.branch = branch;
  }


  public SourceProperties repositoryUrl(String repositoryUrl) {
    this.repositoryUrl = repositoryUrl;
    return this;
  }

  /**
   * The full URL to the source code repository
   * @return repositoryUrl
   */
  @javax.annotation.Nonnull
  public String getRepositoryUrl() {
    return repositoryUrl;
  }

  public void setRepositoryUrl(String repositoryUrl) {
    this.repositoryUrl = repositoryUrl;
  }


  public SourceProperties sourceControlAuthProperties(AuthInfo sourceControlAuthProperties) {
    this.sourceControlAuthProperties = sourceControlAuthProperties;
    return this;
  }

  /**
   * Get sourceControlAuthProperties
   * @return sourceControlAuthProperties
   */
  @javax.annotation.Nullable
  public AuthInfo getSourceControlAuthProperties() {
    return sourceControlAuthProperties;
  }

  public void setSourceControlAuthProperties(AuthInfo sourceControlAuthProperties) {
    this.sourceControlAuthProperties = sourceControlAuthProperties;
  }


  public SourceProperties sourceControlType(SourceControlTypeEnum sourceControlType) {
    this.sourceControlType = sourceControlType;
    return this;
  }

  /**
   * The type of source control service.
   * @return sourceControlType
   */
  @javax.annotation.Nonnull
  public SourceControlTypeEnum getSourceControlType() {
    return sourceControlType;
  }

  public void setSourceControlType(SourceControlTypeEnum sourceControlType) {
    this.sourceControlType = sourceControlType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SourceProperties sourceProperties = (SourceProperties) o;
    return Objects.equals(this.branch, sourceProperties.branch) &&
        Objects.equals(this.repositoryUrl, sourceProperties.repositoryUrl) &&
        Objects.equals(this.sourceControlAuthProperties, sourceProperties.sourceControlAuthProperties) &&
        Objects.equals(this.sourceControlType, sourceProperties.sourceControlType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(branch, repositoryUrl, sourceControlAuthProperties, sourceControlType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SourceProperties {\n");
    sb.append("    branch: ").append(toIndentedString(branch)).append("\n");
    sb.append("    repositoryUrl: ").append(toIndentedString(repositoryUrl)).append("\n");
    sb.append("    sourceControlAuthProperties: ").append(toIndentedString(sourceControlAuthProperties)).append("\n");
    sb.append("    sourceControlType: ").append(toIndentedString(sourceControlType)).append("\n");
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
    openapiFields.add("branch");
    openapiFields.add("repositoryUrl");
    openapiFields.add("sourceControlAuthProperties");
    openapiFields.add("sourceControlType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("repositoryUrl");
    openapiRequiredFields.add("sourceControlType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SourceProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SourceProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SourceProperties is not found in the empty JSON string", SourceProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SourceProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SourceProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SourceProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("branch") != null && !jsonObj.get("branch").isJsonNull()) && !jsonObj.get("branch").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `branch` to be a primitive type in the JSON string but got `%s`", jsonObj.get("branch").toString()));
      }
      if (!jsonObj.get("repositoryUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `repositoryUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("repositoryUrl").toString()));
      }
      // validate the optional field `sourceControlAuthProperties`
      if (jsonObj.get("sourceControlAuthProperties") != null && !jsonObj.get("sourceControlAuthProperties").isJsonNull()) {
        AuthInfo.validateJsonElement(jsonObj.get("sourceControlAuthProperties"));
      }
      if (!jsonObj.get("sourceControlType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceControlType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceControlType").toString()));
      }
      // validate the required field `sourceControlType`
      SourceControlTypeEnum.validateJsonElement(jsonObj.get("sourceControlType"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SourceProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SourceProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SourceProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SourceProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<SourceProperties>() {
           @Override
           public void write(JsonWriter out, SourceProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SourceProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SourceProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SourceProperties
   * @throws IOException if the JSON string is invalid with respect to SourceProperties
   */
  public static SourceProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SourceProperties.class);
  }

  /**
   * Convert an instance of SourceProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

