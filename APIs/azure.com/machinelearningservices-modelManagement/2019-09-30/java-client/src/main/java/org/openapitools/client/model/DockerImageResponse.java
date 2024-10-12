/*
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.EnvironmentImageAsset;
import org.openapitools.client.model.ImageResponseBase;
import org.openapitools.client.model.Model;
import org.openapitools.client.model.ModelErrorResponse;
import org.openapitools.client.model.TargetRuntime;

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
 * DockerImageResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:35:06.363531-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DockerImageResponse extends ImageResponseBase {
  public static final String SERIALIZED_NAME_ASSETS = "assets";
  @SerializedName(SERIALIZED_NAME_ASSETS)
  private List<EnvironmentImageAsset> assets = new ArrayList<>();

  public static final String SERIALIZED_NAME_DOCKER_FILE_URI = "dockerFileUri";
  @SerializedName(SERIALIZED_NAME_DOCKER_FILE_URI)
  private String dockerFileUri;

  public static final String SERIALIZED_NAME_DRIVER_PROGRAM = "driverProgram";
  @SerializedName(SERIALIZED_NAME_DRIVER_PROGRAM)
  private String driverProgram;

  public static final String SERIALIZED_NAME_GENERATED_DOCKER_FILE_URI = "generatedDockerFileUri";
  @SerializedName(SERIALIZED_NAME_GENERATED_DOCKER_FILE_URI)
  private String generatedDockerFileUri;

  public static final String SERIALIZED_NAME_TARGET_RUNTIME = "targetRuntime";
  @SerializedName(SERIALIZED_NAME_TARGET_RUNTIME)
  private TargetRuntime targetRuntime;

  public DockerImageResponse() {
    this.imageFlavor = this.getClass().getSimpleName();
  }

  public DockerImageResponse assets(List<EnvironmentImageAsset> assets) {
    this.assets = assets;
    return this;
  }

  public DockerImageResponse addAssetsItem(EnvironmentImageAsset assetsItem) {
    if (this.assets == null) {
      this.assets = new ArrayList<>();
    }
    this.assets.add(assetsItem);
    return this;
  }

  /**
   * The list of assets.
   * @return assets
   */
  @javax.annotation.Nullable
  public List<EnvironmentImageAsset> getAssets() {
    return assets;
  }

  public void setAssets(List<EnvironmentImageAsset> assets) {
    this.assets = assets;
  }


  public DockerImageResponse dockerFileUri(String dockerFileUri) {
    this.dockerFileUri = dockerFileUri;
    return this;
  }

  /**
   * The Uri to the docker file.
   * @return dockerFileUri
   */
  @javax.annotation.Nullable
  public String getDockerFileUri() {
    return dockerFileUri;
  }

  public void setDockerFileUri(String dockerFileUri) {
    this.dockerFileUri = dockerFileUri;
  }


  public DockerImageResponse driverProgram(String driverProgram) {
    this.driverProgram = driverProgram;
    return this;
  }

  /**
   * The name of the driver file.
   * @return driverProgram
   */
  @javax.annotation.Nullable
  public String getDriverProgram() {
    return driverProgram;
  }

  public void setDriverProgram(String driverProgram) {
    this.driverProgram = driverProgram;
  }


  public DockerImageResponse generatedDockerFileUri(String generatedDockerFileUri) {
    this.generatedDockerFileUri = generatedDockerFileUri;
    return this;
  }

  /**
   * The Uri to the generated docker file.
   * @return generatedDockerFileUri
   */
  @javax.annotation.Nullable
  public String getGeneratedDockerFileUri() {
    return generatedDockerFileUri;
  }

  public void setGeneratedDockerFileUri(String generatedDockerFileUri) {
    this.generatedDockerFileUri = generatedDockerFileUri;
  }


  public DockerImageResponse targetRuntime(TargetRuntime targetRuntime) {
    this.targetRuntime = targetRuntime;
    return this;
  }

  /**
   * Get targetRuntime
   * @return targetRuntime
   */
  @javax.annotation.Nullable
  public TargetRuntime getTargetRuntime() {
    return targetRuntime;
  }

  public void setTargetRuntime(TargetRuntime targetRuntime) {
    this.targetRuntime = targetRuntime;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DockerImageResponse dockerImageResponse = (DockerImageResponse) o;
    return Objects.equals(this.assets, dockerImageResponse.assets) &&
        Objects.equals(this.dockerFileUri, dockerImageResponse.dockerFileUri) &&
        Objects.equals(this.driverProgram, dockerImageResponse.driverProgram) &&
        Objects.equals(this.generatedDockerFileUri, dockerImageResponse.generatedDockerFileUri) &&
        Objects.equals(this.targetRuntime, dockerImageResponse.targetRuntime) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assets, dockerFileUri, driverProgram, generatedDockerFileUri, targetRuntime, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DockerImageResponse {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    assets: ").append(toIndentedString(assets)).append("\n");
    sb.append("    dockerFileUri: ").append(toIndentedString(dockerFileUri)).append("\n");
    sb.append("    driverProgram: ").append(toIndentedString(driverProgram)).append("\n");
    sb.append("    generatedDockerFileUri: ").append(toIndentedString(generatedDockerFileUri)).append("\n");
    sb.append("    targetRuntime: ").append(toIndentedString(targetRuntime)).append("\n");
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
    openapiFields.add("autoDelete");
    openapiFields.add("createdTime");
    openapiFields.add("creationState");
    openapiFields.add("description");
    openapiFields.add("error");
    openapiFields.add("id");
    openapiFields.add("imageBuildLogUri");
    openapiFields.add("imageFlavor");
    openapiFields.add("imageLocation");
    openapiFields.add("imageType");
    openapiFields.add("kvTags");
    openapiFields.add("modelDetails");
    openapiFields.add("modelIds");
    openapiFields.add("modifiedTime");
    openapiFields.add("name");
    openapiFields.add("operationId");
    openapiFields.add("properties");
    openapiFields.add("version");
    openapiFields.add("assets");
    openapiFields.add("dockerFileUri");
    openapiFields.add("driverProgram");
    openapiFields.add("generatedDockerFileUri");
    openapiFields.add("targetRuntime");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("imageFlavor");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DockerImageResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DockerImageResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DockerImageResponse is not found in the empty JSON string", DockerImageResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DockerImageResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DockerImageResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DockerImageResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DockerImageResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DockerImageResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DockerImageResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DockerImageResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<DockerImageResponse>() {
           @Override
           public void write(JsonWriter out, DockerImageResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DockerImageResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DockerImageResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DockerImageResponse
   * @throws IOException if the JSON string is invalid with respect to DockerImageResponse
   */
  public static DockerImageResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DockerImageResponse.class);
  }

  /**
   * Convert an instance of DockerImageResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

