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
import org.openapitools.client.model.Argument;
import org.openapitools.client.model.TaskStepUpdateParameters;

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
 * The properties for updating a docker build step.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:53.147540-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DockerBuildStepUpdateParameters extends TaskStepUpdateParameters {
  public static final String SERIALIZED_NAME_ARGUMENTS = "arguments";
  @SerializedName(SERIALIZED_NAME_ARGUMENTS)
  private List<Argument> arguments = new ArrayList<>();

  public static final String SERIALIZED_NAME_DOCKER_FILE_PATH = "dockerFilePath";
  @SerializedName(SERIALIZED_NAME_DOCKER_FILE_PATH)
  private String dockerFilePath;

  public static final String SERIALIZED_NAME_IMAGE_NAMES = "imageNames";
  @SerializedName(SERIALIZED_NAME_IMAGE_NAMES)
  private List<String> imageNames = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_PUSH_ENABLED = "isPushEnabled";
  @SerializedName(SERIALIZED_NAME_IS_PUSH_ENABLED)
  private Boolean isPushEnabled;

  public static final String SERIALIZED_NAME_NO_CACHE = "noCache";
  @SerializedName(SERIALIZED_NAME_NO_CACHE)
  private Boolean noCache;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public DockerBuildStepUpdateParameters() {
    this.type = this.getClass().getSimpleName();
  }

  public DockerBuildStepUpdateParameters(
     TypeEnum type
  ) {
    this();
    this.type = type;
  }

  public DockerBuildStepUpdateParameters arguments(List<Argument> arguments) {
    this.arguments = arguments;
    return this;
  }

  public DockerBuildStepUpdateParameters addArgumentsItem(Argument argumentsItem) {
    if (this.arguments == null) {
      this.arguments = new ArrayList<>();
    }
    this.arguments.add(argumentsItem);
    return this;
  }

  /**
   * The collection of override arguments to be used when executing this build step.
   * @return arguments
   */
  @javax.annotation.Nullable
  public List<Argument> getArguments() {
    return arguments;
  }

  public void setArguments(List<Argument> arguments) {
    this.arguments = arguments;
  }


  public DockerBuildStepUpdateParameters dockerFilePath(String dockerFilePath) {
    this.dockerFilePath = dockerFilePath;
    return this;
  }

  /**
   * The Docker file path relative to the source context.
   * @return dockerFilePath
   */
  @javax.annotation.Nullable
  public String getDockerFilePath() {
    return dockerFilePath;
  }

  public void setDockerFilePath(String dockerFilePath) {
    this.dockerFilePath = dockerFilePath;
  }


  public DockerBuildStepUpdateParameters imageNames(List<String> imageNames) {
    this.imageNames = imageNames;
    return this;
  }

  public DockerBuildStepUpdateParameters addImageNamesItem(String imageNamesItem) {
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


  public DockerBuildStepUpdateParameters isPushEnabled(Boolean isPushEnabled) {
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


  public DockerBuildStepUpdateParameters noCache(Boolean noCache) {
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


  public DockerBuildStepUpdateParameters target(String target) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DockerBuildStepUpdateParameters dockerBuildStepUpdateParameters = (DockerBuildStepUpdateParameters) o;
    return Objects.equals(this.arguments, dockerBuildStepUpdateParameters.arguments) &&
        Objects.equals(this.dockerFilePath, dockerBuildStepUpdateParameters.dockerFilePath) &&
        Objects.equals(this.imageNames, dockerBuildStepUpdateParameters.imageNames) &&
        Objects.equals(this.isPushEnabled, dockerBuildStepUpdateParameters.isPushEnabled) &&
        Objects.equals(this.noCache, dockerBuildStepUpdateParameters.noCache) &&
        Objects.equals(this.target, dockerBuildStepUpdateParameters.target) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(arguments, dockerFilePath, imageNames, isPushEnabled, noCache, target, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DockerBuildStepUpdateParameters {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    arguments: ").append(toIndentedString(arguments)).append("\n");
    sb.append("    dockerFilePath: ").append(toIndentedString(dockerFilePath)).append("\n");
    sb.append("    imageNames: ").append(toIndentedString(imageNames)).append("\n");
    sb.append("    isPushEnabled: ").append(toIndentedString(isPushEnabled)).append("\n");
    sb.append("    noCache: ").append(toIndentedString(noCache)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
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
    openapiFields.add("contextAccessToken");
    openapiFields.add("contextPath");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DockerBuildStepUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DockerBuildStepUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DockerBuildStepUpdateParameters is not found in the empty JSON string", DockerBuildStepUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DockerBuildStepUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DockerBuildStepUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DockerBuildStepUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DockerBuildStepUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DockerBuildStepUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DockerBuildStepUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<DockerBuildStepUpdateParameters>() {
           @Override
           public void write(JsonWriter out, DockerBuildStepUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DockerBuildStepUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DockerBuildStepUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DockerBuildStepUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to DockerBuildStepUpdateParameters
   */
  public static DockerBuildStepUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DockerBuildStepUpdateParameters.class);
  }

  /**
   * Convert an instance of DockerBuildStepUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

