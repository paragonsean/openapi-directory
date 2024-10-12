/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-09-01
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
import org.openapitools.client.model.Argument;
import org.openapitools.client.model.Credentials;
import org.openapitools.client.model.PlatformProperties;
import org.openapitools.client.model.RunRequest;

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
 * The parameters for a docker quick build.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:53.147540-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DockerBuildRequest extends RunRequest {
  public static final String SERIALIZED_NAME_AGENT_CONFIGURATION = "agentConfiguration";
  @SerializedName(SERIALIZED_NAME_AGENT_CONFIGURATION)
  private AgentProperties agentConfiguration;

  public static final String SERIALIZED_NAME_ARGUMENTS = "arguments";
  @SerializedName(SERIALIZED_NAME_ARGUMENTS)
  private List<Argument> arguments = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREDENTIALS = "credentials";
  @SerializedName(SERIALIZED_NAME_CREDENTIALS)
  private Credentials credentials;

  public static final String SERIALIZED_NAME_DOCKER_FILE_PATH = "dockerFilePath";
  @SerializedName(SERIALIZED_NAME_DOCKER_FILE_PATH)
  private String dockerFilePath;

  public static final String SERIALIZED_NAME_IMAGE_NAMES = "imageNames";
  @SerializedName(SERIALIZED_NAME_IMAGE_NAMES)
  private List<String> imageNames = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_PUSH_ENABLED = "isPushEnabled";
  @SerializedName(SERIALIZED_NAME_IS_PUSH_ENABLED)
  private Boolean isPushEnabled = true;

  public static final String SERIALIZED_NAME_NO_CACHE = "noCache";
  @SerializedName(SERIALIZED_NAME_NO_CACHE)
  private Boolean noCache = false;

  public static final String SERIALIZED_NAME_PLATFORM = "platform";
  @SerializedName(SERIALIZED_NAME_PLATFORM)
  private PlatformProperties platform;

  public static final String SERIALIZED_NAME_SOURCE_LOCATION = "sourceLocation";
  @SerializedName(SERIALIZED_NAME_SOURCE_LOCATION)
  private String sourceLocation;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public static final String SERIALIZED_NAME_TIMEOUT = "timeout";
  @SerializedName(SERIALIZED_NAME_TIMEOUT)
  private Integer timeout = 3600;

  public DockerBuildRequest() {
    this.type = this.getClass().getSimpleName();
  }

  public DockerBuildRequest(
     String type
  ) {
    this();
    this.type = type;
  }

  public DockerBuildRequest agentConfiguration(AgentProperties agentConfiguration) {
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


  public DockerBuildRequest arguments(List<Argument> arguments) {
    this.arguments = arguments;
    return this;
  }

  public DockerBuildRequest addArgumentsItem(Argument argumentsItem) {
    if (this.arguments == null) {
      this.arguments = new ArrayList<>();
    }
    this.arguments.add(argumentsItem);
    return this;
  }

  /**
   * The collection of override arguments to be used when executing the run.
   * @return arguments
   */
  @javax.annotation.Nullable
  public List<Argument> getArguments() {
    return arguments;
  }

  public void setArguments(List<Argument> arguments) {
    this.arguments = arguments;
  }


  public DockerBuildRequest credentials(Credentials credentials) {
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


  public DockerBuildRequest dockerFilePath(String dockerFilePath) {
    this.dockerFilePath = dockerFilePath;
    return this;
  }

  /**
   * The Docker file path relative to the source location.
   * @return dockerFilePath
   */
  @javax.annotation.Nonnull
  public String getDockerFilePath() {
    return dockerFilePath;
  }

  public void setDockerFilePath(String dockerFilePath) {
    this.dockerFilePath = dockerFilePath;
  }


  public DockerBuildRequest imageNames(List<String> imageNames) {
    this.imageNames = imageNames;
    return this;
  }

  public DockerBuildRequest addImageNamesItem(String imageNamesItem) {
    if (this.imageNames == null) {
      this.imageNames = new ArrayList<>();
    }
    this.imageNames.add(imageNamesItem);
    return this;
  }

  /**
   * The fully qualified image names including the repository and tag.
   * @return imageNames
   */
  @javax.annotation.Nullable
  public List<String> getImageNames() {
    return imageNames;
  }

  public void setImageNames(List<String> imageNames) {
    this.imageNames = imageNames;
  }


  public DockerBuildRequest isPushEnabled(Boolean isPushEnabled) {
    this.isPushEnabled = isPushEnabled;
    return this;
  }

  /**
   * The value of this property indicates whether the image built should be pushed to the registry or not.
   * @return isPushEnabled
   */
  @javax.annotation.Nullable
  public Boolean getIsPushEnabled() {
    return isPushEnabled;
  }

  public void setIsPushEnabled(Boolean isPushEnabled) {
    this.isPushEnabled = isPushEnabled;
  }


  public DockerBuildRequest noCache(Boolean noCache) {
    this.noCache = noCache;
    return this;
  }

  /**
   * The value of this property indicates whether the image cache is enabled or not.
   * @return noCache
   */
  @javax.annotation.Nullable
  public Boolean getNoCache() {
    return noCache;
  }

  public void setNoCache(Boolean noCache) {
    this.noCache = noCache;
  }


  public DockerBuildRequest platform(PlatformProperties platform) {
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


  public DockerBuildRequest sourceLocation(String sourceLocation) {
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


  public DockerBuildRequest target(String target) {
    this.target = target;
    return this;
  }

  /**
   * The name of the target build stage for the docker build.
   * @return target
   */
  @javax.annotation.Nullable
  public String getTarget() {
    return target;
  }

  public void setTarget(String target) {
    this.target = target;
  }


  public DockerBuildRequest timeout(Integer timeout) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DockerBuildRequest dockerBuildRequest = (DockerBuildRequest) o;
    return Objects.equals(this.agentConfiguration, dockerBuildRequest.agentConfiguration) &&
        Objects.equals(this.arguments, dockerBuildRequest.arguments) &&
        Objects.equals(this.credentials, dockerBuildRequest.credentials) &&
        Objects.equals(this.dockerFilePath, dockerBuildRequest.dockerFilePath) &&
        Objects.equals(this.imageNames, dockerBuildRequest.imageNames) &&
        Objects.equals(this.isPushEnabled, dockerBuildRequest.isPushEnabled) &&
        Objects.equals(this.noCache, dockerBuildRequest.noCache) &&
        Objects.equals(this.platform, dockerBuildRequest.platform) &&
        Objects.equals(this.sourceLocation, dockerBuildRequest.sourceLocation) &&
        Objects.equals(this.target, dockerBuildRequest.target) &&
        Objects.equals(this.timeout, dockerBuildRequest.timeout) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(agentConfiguration, arguments, credentials, dockerFilePath, imageNames, isPushEnabled, noCache, platform, sourceLocation, target, timeout, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DockerBuildRequest {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    agentConfiguration: ").append(toIndentedString(agentConfiguration)).append("\n");
    sb.append("    arguments: ").append(toIndentedString(arguments)).append("\n");
    sb.append("    credentials: ").append(toIndentedString(credentials)).append("\n");
    sb.append("    dockerFilePath: ").append(toIndentedString(dockerFilePath)).append("\n");
    sb.append("    imageNames: ").append(toIndentedString(imageNames)).append("\n");
    sb.append("    isPushEnabled: ").append(toIndentedString(isPushEnabled)).append("\n");
    sb.append("    noCache: ").append(toIndentedString(noCache)).append("\n");
    sb.append("    platform: ").append(toIndentedString(platform)).append("\n");
    sb.append("    sourceLocation: ").append(toIndentedString(sourceLocation)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
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
    openapiFields.add("isArchiveEnabled");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("dockerFilePath");
    openapiRequiredFields.add("platform");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DockerBuildRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DockerBuildRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DockerBuildRequest is not found in the empty JSON string", DockerBuildRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DockerBuildRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DockerBuildRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DockerBuildRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DockerBuildRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DockerBuildRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DockerBuildRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DockerBuildRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<DockerBuildRequest>() {
           @Override
           public void write(JsonWriter out, DockerBuildRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DockerBuildRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DockerBuildRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DockerBuildRequest
   * @throws IOException if the JSON string is invalid with respect to DockerBuildRequest
   */
  public static DockerBuildRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DockerBuildRequest.class);
  }

  /**
   * Convert an instance of DockerBuildRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

