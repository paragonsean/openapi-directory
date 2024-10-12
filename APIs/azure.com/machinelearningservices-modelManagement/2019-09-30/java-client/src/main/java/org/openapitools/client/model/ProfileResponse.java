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
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import org.openapitools.client.model.ModelErrorResponse;

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
 * The profile response.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:35:06.363531-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProfileResponse {
  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private ModelErrorResponse error;

  public static final String SERIALIZED_NAME_IMAGE_ID = "imageId";
  @SerializedName(SERIALIZED_NAME_IMAGE_ID)
  private String imageId;

  public static final String SERIALIZED_NAME_INPUT_DATA = "inputData";
  @SerializedName(SERIALIZED_NAME_INPUT_DATA)
  private String inputData;

  public static final String SERIALIZED_NAME_KV_TAGS = "kvTags";
  @SerializedName(SERIALIZED_NAME_KV_TAGS)
  private Map<String, String> kvTags = new HashMap<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROFILE_RUN_RESULT = "profileRunResult";
  @SerializedName(SERIALIZED_NAME_PROFILE_RUN_RESULT)
  private String profileRunResult;

  public static final String SERIALIZED_NAME_PROFILING_ERROR_LOGS = "profilingErrorLogs";
  @SerializedName(SERIALIZED_NAME_PROFILING_ERROR_LOGS)
  private String profilingErrorLogs;

  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private Map<String, String> properties = new HashMap<>();

  public static final String SERIALIZED_NAME_RECOMMENDATION_LATENCY_IN_MS = "recommendationLatencyInMs";
  @SerializedName(SERIALIZED_NAME_RECOMMENDATION_LATENCY_IN_MS)
  private Double recommendationLatencyInMs;

  public static final String SERIALIZED_NAME_RECOMMENDED_CPU = "recommendedCpu";
  @SerializedName(SERIALIZED_NAME_RECOMMENDED_CPU)
  private Double recommendedCpu;

  public static final String SERIALIZED_NAME_RECOMMENDED_MEMORY_IN_G_B = "recommendedMemoryInGB";
  @SerializedName(SERIALIZED_NAME_RECOMMENDED_MEMORY_IN_G_B)
  private Double recommendedMemoryInGB;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private String state;

  public ProfileResponse() {
  }

  public ProfileResponse createdTime(OffsetDateTime createdTime) {
    this.createdTime = createdTime;
    return this;
  }

  /**
   * The profile creation time (UTC).
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }

  public void setCreatedTime(OffsetDateTime createdTime) {
    this.createdTime = createdTime;
  }


  public ProfileResponse description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The profile description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ProfileResponse error(ModelErrorResponse error) {
    this.error = error;
    return this;
  }

  /**
   * Get error
   * @return error
   */
  @javax.annotation.Nullable
  public ModelErrorResponse getError() {
    return error;
  }

  public void setError(ModelErrorResponse error) {
    this.error = error;
  }


  public ProfileResponse imageId(String imageId) {
    this.imageId = imageId;
    return this;
  }

  /**
   * The Image Id.
   * @return imageId
   */
  @javax.annotation.Nullable
  public String getImageId() {
    return imageId;
  }

  public void setImageId(String imageId) {
    this.imageId = imageId;
  }


  public ProfileResponse inputData(String inputData) {
    this.inputData = inputData;
    return this;
  }

  /**
   * The input data.
   * @return inputData
   */
  @javax.annotation.Nullable
  public String getInputData() {
    return inputData;
  }

  public void setInputData(String inputData) {
    this.inputData = inputData;
  }


  public ProfileResponse kvTags(Map<String, String> kvTags) {
    this.kvTags = kvTags;
    return this;
  }

  public ProfileResponse putKvTagsItem(String key, String kvTagsItem) {
    if (this.kvTags == null) {
      this.kvTags = new HashMap<>();
    }
    this.kvTags.put(key, kvTagsItem);
    return this;
  }

  /**
   * The profile tags dictionary. Tags are mutable.
   * @return kvTags
   */
  @javax.annotation.Nullable
  public Map<String, String> getKvTags() {
    return kvTags;
  }

  public void setKvTags(Map<String, String> kvTags) {
    this.kvTags = kvTags;
  }


  public ProfileResponse name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The profile name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ProfileResponse profileRunResult(String profileRunResult) {
    this.profileRunResult = profileRunResult;
    return this;
  }

  /**
   * The profile run result.
   * @return profileRunResult
   */
  @javax.annotation.Nullable
  public String getProfileRunResult() {
    return profileRunResult;
  }

  public void setProfileRunResult(String profileRunResult) {
    this.profileRunResult = profileRunResult;
  }


  public ProfileResponse profilingErrorLogs(String profilingErrorLogs) {
    this.profilingErrorLogs = profilingErrorLogs;
    return this;
  }

  /**
   * The profiling error logs.
   * @return profilingErrorLogs
   */
  @javax.annotation.Nullable
  public String getProfilingErrorLogs() {
    return profilingErrorLogs;
  }

  public void setProfilingErrorLogs(String profilingErrorLogs) {
    this.profilingErrorLogs = profilingErrorLogs;
  }


  public ProfileResponse properties(Map<String, String> properties) {
    this.properties = properties;
    return this;
  }

  public ProfileResponse putPropertiesItem(String key, String propertiesItem) {
    if (this.properties == null) {
      this.properties = new HashMap<>();
    }
    this.properties.put(key, propertiesItem);
    return this;
  }

  /**
   * The profile properties dictionary. Properties are immutable.
   * @return properties
   */
  @javax.annotation.Nullable
  public Map<String, String> getProperties() {
    return properties;
  }

  public void setProperties(Map<String, String> properties) {
    this.properties = properties;
  }


  public ProfileResponse recommendationLatencyInMs(Double recommendationLatencyInMs) {
    this.recommendationLatencyInMs = recommendationLatencyInMs;
    return this;
  }

  /**
   * Latency associated with the recommended memory/cpu config
   * @return recommendationLatencyInMs
   */
  @javax.annotation.Nullable
  public Double getRecommendationLatencyInMs() {
    return recommendationLatencyInMs;
  }

  public void setRecommendationLatencyInMs(Double recommendationLatencyInMs) {
    this.recommendationLatencyInMs = recommendationLatencyInMs;
  }


  public ProfileResponse recommendedCpu(Double recommendedCpu) {
    this.recommendedCpu = recommendedCpu;
    return this;
  }

  /**
   * The recommended CPU allocation.
   * @return recommendedCpu
   */
  @javax.annotation.Nullable
  public Double getRecommendedCpu() {
    return recommendedCpu;
  }

  public void setRecommendedCpu(Double recommendedCpu) {
    this.recommendedCpu = recommendedCpu;
  }


  public ProfileResponse recommendedMemoryInGB(Double recommendedMemoryInGB) {
    this.recommendedMemoryInGB = recommendedMemoryInGB;
    return this;
  }

  /**
   * The recommended amount of memory to allocate in GB.
   * @return recommendedMemoryInGB
   */
  @javax.annotation.Nullable
  public Double getRecommendedMemoryInGB() {
    return recommendedMemoryInGB;
  }

  public void setRecommendedMemoryInGB(Double recommendedMemoryInGB) {
    this.recommendedMemoryInGB = recommendedMemoryInGB;
  }


  public ProfileResponse state(String state) {
    this.state = state;
    return this;
  }

  /**
   * The state of the profile.
   * @return state
   */
  @javax.annotation.Nullable
  public String getState() {
    return state;
  }

  public void setState(String state) {
    this.state = state;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProfileResponse profileResponse = (ProfileResponse) o;
    return Objects.equals(this.createdTime, profileResponse.createdTime) &&
        Objects.equals(this.description, profileResponse.description) &&
        Objects.equals(this.error, profileResponse.error) &&
        Objects.equals(this.imageId, profileResponse.imageId) &&
        Objects.equals(this.inputData, profileResponse.inputData) &&
        Objects.equals(this.kvTags, profileResponse.kvTags) &&
        Objects.equals(this.name, profileResponse.name) &&
        Objects.equals(this.profileRunResult, profileResponse.profileRunResult) &&
        Objects.equals(this.profilingErrorLogs, profileResponse.profilingErrorLogs) &&
        Objects.equals(this.properties, profileResponse.properties) &&
        Objects.equals(this.recommendationLatencyInMs, profileResponse.recommendationLatencyInMs) &&
        Objects.equals(this.recommendedCpu, profileResponse.recommendedCpu) &&
        Objects.equals(this.recommendedMemoryInGB, profileResponse.recommendedMemoryInGB) &&
        Objects.equals(this.state, profileResponse.state);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdTime, description, error, imageId, inputData, kvTags, name, profileRunResult, profilingErrorLogs, properties, recommendationLatencyInMs, recommendedCpu, recommendedMemoryInGB, state);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProfileResponse {\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    imageId: ").append(toIndentedString(imageId)).append("\n");
    sb.append("    inputData: ").append(toIndentedString(inputData)).append("\n");
    sb.append("    kvTags: ").append(toIndentedString(kvTags)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    profileRunResult: ").append(toIndentedString(profileRunResult)).append("\n");
    sb.append("    profilingErrorLogs: ").append(toIndentedString(profilingErrorLogs)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
    sb.append("    recommendationLatencyInMs: ").append(toIndentedString(recommendationLatencyInMs)).append("\n");
    sb.append("    recommendedCpu: ").append(toIndentedString(recommendedCpu)).append("\n");
    sb.append("    recommendedMemoryInGB: ").append(toIndentedString(recommendedMemoryInGB)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
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
    openapiFields.add("createdTime");
    openapiFields.add("description");
    openapiFields.add("error");
    openapiFields.add("imageId");
    openapiFields.add("inputData");
    openapiFields.add("kvTags");
    openapiFields.add("name");
    openapiFields.add("profileRunResult");
    openapiFields.add("profilingErrorLogs");
    openapiFields.add("properties");
    openapiFields.add("recommendationLatencyInMs");
    openapiFields.add("recommendedCpu");
    openapiFields.add("recommendedMemoryInGB");
    openapiFields.add("state");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProfileResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProfileResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProfileResponse is not found in the empty JSON string", ProfileResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProfileResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProfileResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `error`
      if (jsonObj.get("error") != null && !jsonObj.get("error").isJsonNull()) {
        ModelErrorResponse.validateJsonElement(jsonObj.get("error"));
      }
      if ((jsonObj.get("imageId") != null && !jsonObj.get("imageId").isJsonNull()) && !jsonObj.get("imageId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `imageId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("imageId").toString()));
      }
      if ((jsonObj.get("inputData") != null && !jsonObj.get("inputData").isJsonNull()) && !jsonObj.get("inputData").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `inputData` to be a primitive type in the JSON string but got `%s`", jsonObj.get("inputData").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("profileRunResult") != null && !jsonObj.get("profileRunResult").isJsonNull()) && !jsonObj.get("profileRunResult").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profileRunResult` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profileRunResult").toString()));
      }
      if ((jsonObj.get("profilingErrorLogs") != null && !jsonObj.get("profilingErrorLogs").isJsonNull()) && !jsonObj.get("profilingErrorLogs").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profilingErrorLogs` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profilingErrorLogs").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProfileResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProfileResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProfileResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProfileResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<ProfileResponse>() {
           @Override
           public void write(JsonWriter out, ProfileResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProfileResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProfileResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProfileResponse
   * @throws IOException if the JSON string is invalid with respect to ProfileResponse
   */
  public static ProfileResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProfileResponse.class);
  }

  /**
   * Convert an instance of ProfileResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

