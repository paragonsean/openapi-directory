/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AgentProperties;
import org.openapitools.client.model.Credentials;
import org.openapitools.client.model.PlatformProperties;
import org.openapitools.client.model.RunRequest;
import org.openapitools.client.model.SetValue;

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
 * The request parameters for a scheduling run against a task file.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:55.681670-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FileTaskRunRequest extends RunRequest {
  public static final String SERIALIZED_NAME_AGENT_CONFIGURATION = "agentConfiguration";
  @SerializedName(SERIALIZED_NAME_AGENT_CONFIGURATION)
  private AgentProperties agentConfiguration;

  public static final String SERIALIZED_NAME_CREDENTIALS = "credentials";
  @SerializedName(SERIALIZED_NAME_CREDENTIALS)
  private Credentials credentials;

  public static final String SERIALIZED_NAME_PLATFORM = "platform";
  @SerializedName(SERIALIZED_NAME_PLATFORM)
  private PlatformProperties platform;

  public static final String SERIALIZED_NAME_SOURCE_LOCATION = "sourceLocation";
  @SerializedName(SERIALIZED_NAME_SOURCE_LOCATION)
  private String sourceLocation;

  public static final String SERIALIZED_NAME_TASK_FILE_PATH = "taskFilePath";
  @SerializedName(SERIALIZED_NAME_TASK_FILE_PATH)
  private String taskFilePath;

  public static final String SERIALIZED_NAME_TIMEOUT = "timeout";
  @SerializedName(SERIALIZED_NAME_TIMEOUT)
  private Integer timeout = 3600;

  public static final String SERIALIZED_NAME_VALUES = "values";
  @SerializedName(SERIALIZED_NAME_VALUES)
  private List<SetValue> values = new ArrayList<>();

  public static final String SERIALIZED_NAME_VALUES_FILE_PATH = "valuesFilePath";
  @SerializedName(SERIALIZED_NAME_VALUES_FILE_PATH)
  private String valuesFilePath;

  public FileTaskRunRequest() {
    this.type = this.getClass().getSimpleName();
  }

  public FileTaskRunRequest agentConfiguration(AgentProperties agentConfiguration) {
    this.agentConfiguration = agentConfiguration;
    return this;
  }

  /**
   * Get agentConfiguration
   * @return agentConfiguration
   */
  @javax.annotation.Nullable
  public AgentProperties getAgentConfiguration() {
    return agentConfiguration;
  }

  public void setAgentConfiguration(AgentProperties agentConfiguration) {
    this.agentConfiguration = agentConfiguration;
  }


  public FileTaskRunRequest credentials(Credentials credentials) {
    this.credentials = credentials;
    return this;
  }

  /**
   * Get credentials
   * @return credentials
   */
  @javax.annotation.Nullable
  public Credentials getCredentials() {
    return credentials;
  }

  public void setCredentials(Credentials credentials) {
    this.credentials = credentials;
  }


  public FileTaskRunRequest platform(PlatformProperties platform) {
    this.platform = platform;
    return this;
  }

  /**
   * Get platform
   * @return platform
   */
  @javax.annotation.Nonnull
  public PlatformProperties getPlatform() {
    return platform;
  }

  public void setPlatform(PlatformProperties platform) {
    this.platform = platform;
  }


  public FileTaskRunRequest sourceLocation(String sourceLocation) {
    this.sourceLocation = sourceLocation;
    return this;
  }

  /**
   * The URL(absolute or relative) of the source context. It can be an URL to a tar or git repository.  If it is relative URL, the relative path should be obtained from calling listBuildSourceUploadUrl API.
   * @return sourceLocation
   */
  @javax.annotation.Nullable
  public String getSourceLocation() {
    return sourceLocation;
  }

  public void setSourceLocation(String sourceLocation) {
    this.sourceLocation = sourceLocation;
  }


  public FileTaskRunRequest taskFilePath(String taskFilePath) {
    this.taskFilePath = taskFilePath;
    return this;
  }

  /**
   * The template/definition file path relative to the source.
   * @return taskFilePath
   */
  @javax.annotation.Nonnull
  public String getTaskFilePath() {
    return taskFilePath;
  }

  public void setTaskFilePath(String taskFilePath) {
    this.taskFilePath = taskFilePath;
  }


  public FileTaskRunRequest timeout(Integer timeout) {
    this.timeout = timeout;
    return this;
  }

  /**
   * Run timeout in seconds.
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


  public FileTaskRunRequest values(List<SetValue> values) {
    this.values = values;
    return this;
  }

  public FileTaskRunRequest addValuesItem(SetValue valuesItem) {
    if (this.values == null) {
      this.values = new ArrayList<>();
    }
    this.values.add(valuesItem);
    return this;
  }

  /**
   * The collection of overridable values that can be passed when running a task.
   * @return values
   */
  @javax.annotation.Nullable
  public List<SetValue> getValues() {
    return values;
  }

  public void setValues(List<SetValue> values) {
    this.values = values;
  }


  public FileTaskRunRequest valuesFilePath(String valuesFilePath) {
    this.valuesFilePath = valuesFilePath;
    return this;
  }

  /**
   * The values/parameters file path relative to the source.
   * @return valuesFilePath
   */
  @javax.annotation.Nullable
  public String getValuesFilePath() {
    return valuesFilePath;
  }

  public void setValuesFilePath(String valuesFilePath) {
    this.valuesFilePath = valuesFilePath;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FileTaskRunRequest fileTaskRunRequest = (FileTaskRunRequest) o;
    return Objects.equals(this.agentConfiguration, fileTaskRunRequest.agentConfiguration) &&
        Objects.equals(this.credentials, fileTaskRunRequest.credentials) &&
        Objects.equals(this.platform, fileTaskRunRequest.platform) &&
        Objects.equals(this.sourceLocation, fileTaskRunRequest.sourceLocation) &&
        Objects.equals(this.taskFilePath, fileTaskRunRequest.taskFilePath) &&
        Objects.equals(this.timeout, fileTaskRunRequest.timeout) &&
        Objects.equals(this.values, fileTaskRunRequest.values) &&
        Objects.equals(this.valuesFilePath, fileTaskRunRequest.valuesFilePath) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(agentConfiguration, credentials, platform, sourceLocation, taskFilePath, timeout, values, valuesFilePath, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FileTaskRunRequest {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    agentConfiguration: ").append(toIndentedString(agentConfiguration)).append("\n");
    sb.append("    credentials: ").append(toIndentedString(credentials)).append("\n");
    sb.append("    platform: ").append(toIndentedString(platform)).append("\n");
    sb.append("    sourceLocation: ").append(toIndentedString(sourceLocation)).append("\n");
    sb.append("    taskFilePath: ").append(toIndentedString(taskFilePath)).append("\n");
    sb.append("    timeout: ").append(toIndentedString(timeout)).append("\n");
    sb.append("    values: ").append(toIndentedString(values)).append("\n");
    sb.append("    valuesFilePath: ").append(toIndentedString(valuesFilePath)).append("\n");
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
    openapiFields.add("isArchiveEnabled");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("platform");
    openapiRequiredFields.add("taskFilePath");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FileTaskRunRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FileTaskRunRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FileTaskRunRequest is not found in the empty JSON string", FileTaskRunRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FileTaskRunRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FileTaskRunRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : FileTaskRunRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FileTaskRunRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FileTaskRunRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FileTaskRunRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FileTaskRunRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<FileTaskRunRequest>() {
           @Override
           public void write(JsonWriter out, FileTaskRunRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FileTaskRunRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FileTaskRunRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FileTaskRunRequest
   * @throws IOException if the JSON string is invalid with respect to FileTaskRunRequest
   */
  public static FileTaskRunRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FileTaskRunRequest.class);
  }

  /**
   * Convert an instance of FileTaskRunRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

