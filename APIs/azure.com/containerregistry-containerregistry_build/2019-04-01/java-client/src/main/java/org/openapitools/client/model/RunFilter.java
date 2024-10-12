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
import java.time.OffsetDateTime;
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
 * Properties that are enabled for Odata querying on runs.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RunFilter {
  public static final String SERIALIZED_NAME_CREATE_TIME = "createTime";
  @SerializedName(SERIALIZED_NAME_CREATE_TIME)
  private OffsetDateTime createTime;

  public static final String SERIALIZED_NAME_FINISH_TIME = "finishTime";
  @SerializedName(SERIALIZED_NAME_FINISH_TIME)
  private OffsetDateTime finishTime;

  public static final String SERIALIZED_NAME_IS_ARCHIVE_ENABLED = "isArchiveEnabled";
  @SerializedName(SERIALIZED_NAME_IS_ARCHIVE_ENABLED)
  private Boolean isArchiveEnabled;

  public static final String SERIALIZED_NAME_OUTPUT_IMAGE_MANIFESTS = "outputImageManifests";
  @SerializedName(SERIALIZED_NAME_OUTPUT_IMAGE_MANIFESTS)
  private String outputImageManifests;

  public static final String SERIALIZED_NAME_RUN_ID = "runId";
  @SerializedName(SERIALIZED_NAME_RUN_ID)
  private String runId;

  /**
   * The type of run.
   */
  @JsonAdapter(RunTypeEnum.Adapter.class)
  public enum RunTypeEnum {
    QUICK_BUILD("QuickBuild"),
    
    QUICK_RUN("QuickRun"),
    
    AUTO_BUILD("AutoBuild"),
    
    AUTO_RUN("AutoRun");

    private String value;

    RunTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RunTypeEnum fromValue(String value) {
      for (RunTypeEnum b : RunTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RunTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RunTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RunTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RunTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RunTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RUN_TYPE = "runType";
  @SerializedName(SERIALIZED_NAME_RUN_TYPE)
  private RunTypeEnum runType;

  /**
   * The current status of the run.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    QUEUED("Queued"),
    
    STARTED("Started"),
    
    RUNNING("Running"),
    
    SUCCEEDED("Succeeded"),
    
    FAILED("Failed"),
    
    CANCELED("Canceled"),
    
    ERROR("Error"),
    
    TIMEOUT("Timeout");

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

  public static final String SERIALIZED_NAME_TASK_NAME = "taskName";
  @SerializedName(SERIALIZED_NAME_TASK_NAME)
  private String taskName;

  public RunFilter() {
  }

  public RunFilter createTime(OffsetDateTime createTime) {
    this.createTime = createTime;
    return this;
  }

  /**
   * The create time for a run.
   * @return createTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreateTime() {
    return createTime;
  }

  public void setCreateTime(OffsetDateTime createTime) {
    this.createTime = createTime;
  }


  public RunFilter finishTime(OffsetDateTime finishTime) {
    this.finishTime = finishTime;
    return this;
  }

  /**
   * The time the run finished.
   * @return finishTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getFinishTime() {
    return finishTime;
  }

  public void setFinishTime(OffsetDateTime finishTime) {
    this.finishTime = finishTime;
  }


  public RunFilter isArchiveEnabled(Boolean isArchiveEnabled) {
    this.isArchiveEnabled = isArchiveEnabled;
    return this;
  }

  /**
   * The value that indicates whether archiving is enabled or not.
   * @return isArchiveEnabled
   */
  @javax.annotation.Nullable
  public Boolean getIsArchiveEnabled() {
    return isArchiveEnabled;
  }

  public void setIsArchiveEnabled(Boolean isArchiveEnabled) {
    this.isArchiveEnabled = isArchiveEnabled;
  }


  public RunFilter outputImageManifests(String outputImageManifests) {
    this.outputImageManifests = outputImageManifests;
    return this;
  }

  /**
   * The list of comma-separated image manifests that were generated from the run. This is applicable if the run is of  build type.
   * @return outputImageManifests
   */
  @javax.annotation.Nullable
  public String getOutputImageManifests() {
    return outputImageManifests;
  }

  public void setOutputImageManifests(String outputImageManifests) {
    this.outputImageManifests = outputImageManifests;
  }


  public RunFilter runId(String runId) {
    this.runId = runId;
    return this;
  }

  /**
   * The unique identifier for the run.
   * @return runId
   */
  @javax.annotation.Nullable
  public String getRunId() {
    return runId;
  }

  public void setRunId(String runId) {
    this.runId = runId;
  }


  public RunFilter runType(RunTypeEnum runType) {
    this.runType = runType;
    return this;
  }

  /**
   * The type of run.
   * @return runType
   */
  @javax.annotation.Nullable
  public RunTypeEnum getRunType() {
    return runType;
  }

  public void setRunType(RunTypeEnum runType) {
    this.runType = runType;
  }


  public RunFilter status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * The current status of the run.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public RunFilter taskName(String taskName) {
    this.taskName = taskName;
    return this;
  }

  /**
   * The name of the task that the run corresponds to.
   * @return taskName
   */
  @javax.annotation.Nullable
  public String getTaskName() {
    return taskName;
  }

  public void setTaskName(String taskName) {
    this.taskName = taskName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RunFilter runFilter = (RunFilter) o;
    return Objects.equals(this.createTime, runFilter.createTime) &&
        Objects.equals(this.finishTime, runFilter.finishTime) &&
        Objects.equals(this.isArchiveEnabled, runFilter.isArchiveEnabled) &&
        Objects.equals(this.outputImageManifests, runFilter.outputImageManifests) &&
        Objects.equals(this.runId, runFilter.runId) &&
        Objects.equals(this.runType, runFilter.runType) &&
        Objects.equals(this.status, runFilter.status) &&
        Objects.equals(this.taskName, runFilter.taskName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createTime, finishTime, isArchiveEnabled, outputImageManifests, runId, runType, status, taskName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RunFilter {\n");
    sb.append("    createTime: ").append(toIndentedString(createTime)).append("\n");
    sb.append("    finishTime: ").append(toIndentedString(finishTime)).append("\n");
    sb.append("    isArchiveEnabled: ").append(toIndentedString(isArchiveEnabled)).append("\n");
    sb.append("    outputImageManifests: ").append(toIndentedString(outputImageManifests)).append("\n");
    sb.append("    runId: ").append(toIndentedString(runId)).append("\n");
    sb.append("    runType: ").append(toIndentedString(runType)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    taskName: ").append(toIndentedString(taskName)).append("\n");
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
    openapiFields.add("createTime");
    openapiFields.add("finishTime");
    openapiFields.add("isArchiveEnabled");
    openapiFields.add("outputImageManifests");
    openapiFields.add("runId");
    openapiFields.add("runType");
    openapiFields.add("status");
    openapiFields.add("taskName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RunFilter
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RunFilter.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RunFilter is not found in the empty JSON string", RunFilter.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RunFilter.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RunFilter` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("outputImageManifests") != null && !jsonObj.get("outputImageManifests").isJsonNull()) && !jsonObj.get("outputImageManifests").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `outputImageManifests` to be a primitive type in the JSON string but got `%s`", jsonObj.get("outputImageManifests").toString()));
      }
      if ((jsonObj.get("runId") != null && !jsonObj.get("runId").isJsonNull()) && !jsonObj.get("runId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `runId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("runId").toString()));
      }
      if ((jsonObj.get("runType") != null && !jsonObj.get("runType").isJsonNull()) && !jsonObj.get("runType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `runType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("runType").toString()));
      }
      // validate the optional field `runType`
      if (jsonObj.get("runType") != null && !jsonObj.get("runType").isJsonNull()) {
        RunTypeEnum.validateJsonElement(jsonObj.get("runType"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("taskName") != null && !jsonObj.get("taskName").isJsonNull()) && !jsonObj.get("taskName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `taskName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("taskName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RunFilter.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RunFilter' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RunFilter> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RunFilter.class));

       return (TypeAdapter<T>) new TypeAdapter<RunFilter>() {
           @Override
           public void write(JsonWriter out, RunFilter value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RunFilter read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RunFilter given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RunFilter
   * @throws IOException if the JSON string is invalid with respect to RunFilter
   */
  public static RunFilter fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RunFilter.class);
  }

  /**
   * Convert an instance of RunFilter to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

