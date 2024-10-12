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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AgentProperties;
import org.openapitools.client.model.ImageDescriptor;
import org.openapitools.client.model.ImageUpdateTrigger;
import org.openapitools.client.model.PlatformProperties;
import org.openapitools.client.model.SourceTriggerDescriptor;
import org.openapitools.client.model.TimerTriggerDescriptor;

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
 * The properties for a run.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RunProperties {
  public static final String SERIALIZED_NAME_AGENT_CONFIGURATION = "agentConfiguration";
  @SerializedName(SERIALIZED_NAME_AGENT_CONFIGURATION)
  private AgentProperties agentConfiguration;

  public static final String SERIALIZED_NAME_CREATE_TIME = "createTime";
  @SerializedName(SERIALIZED_NAME_CREATE_TIME)
  private OffsetDateTime createTime;

  public static final String SERIALIZED_NAME_CUSTOM_REGISTRIES = "customRegistries";
  @SerializedName(SERIALIZED_NAME_CUSTOM_REGISTRIES)
  private List<String> customRegistries = new ArrayList<>();

  public static final String SERIALIZED_NAME_FINISH_TIME = "finishTime";
  @SerializedName(SERIALIZED_NAME_FINISH_TIME)
  private OffsetDateTime finishTime;

  public static final String SERIALIZED_NAME_IMAGE_UPDATE_TRIGGER = "imageUpdateTrigger";
  @SerializedName(SERIALIZED_NAME_IMAGE_UPDATE_TRIGGER)
  private ImageUpdateTrigger imageUpdateTrigger;

  public static final String SERIALIZED_NAME_IS_ARCHIVE_ENABLED = "isArchiveEnabled";
  @SerializedName(SERIALIZED_NAME_IS_ARCHIVE_ENABLED)
  private Boolean isArchiveEnabled = false;

  public static final String SERIALIZED_NAME_LAST_UPDATED_TIME = "lastUpdatedTime";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED_TIME)
  private OffsetDateTime lastUpdatedTime;

  public static final String SERIALIZED_NAME_OUTPUT_IMAGES = "outputImages";
  @SerializedName(SERIALIZED_NAME_OUTPUT_IMAGES)
  private List<ImageDescriptor> outputImages = new ArrayList<>();

  public static final String SERIALIZED_NAME_PLATFORM = "platform";
  @SerializedName(SERIALIZED_NAME_PLATFORM)
  private PlatformProperties platform;

  /**
   * The provisioning state of a run.
   */
  @JsonAdapter(ProvisioningStateEnum.Adapter.class)
  public enum ProvisioningStateEnum {
    CREATING("Creating"),
    
    UPDATING("Updating"),
    
    DELETING("Deleting"),
    
    SUCCEEDED("Succeeded"),
    
    FAILED("Failed"),
    
    CANCELED("Canceled");

    private String value;

    ProvisioningStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProvisioningStateEnum fromValue(String value) {
      for (ProvisioningStateEnum b : ProvisioningStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProvisioningStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProvisioningStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProvisioningStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProvisioningStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProvisioningStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROVISIONING_STATE = "provisioningState";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_STATE)
  private ProvisioningStateEnum provisioningState;

  public static final String SERIALIZED_NAME_RUN_ERROR_MESSAGE = "runErrorMessage";
  @SerializedName(SERIALIZED_NAME_RUN_ERROR_MESSAGE)
  private String runErrorMessage;

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

  public static final String SERIALIZED_NAME_SOURCE_REGISTRY_AUTH = "sourceRegistryAuth";
  @SerializedName(SERIALIZED_NAME_SOURCE_REGISTRY_AUTH)
  private String sourceRegistryAuth;

  public static final String SERIALIZED_NAME_SOURCE_TRIGGER = "sourceTrigger";
  @SerializedName(SERIALIZED_NAME_SOURCE_TRIGGER)
  private SourceTriggerDescriptor sourceTrigger;

  public static final String SERIALIZED_NAME_START_TIME = "startTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private OffsetDateTime startTime;

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

  public static final String SERIALIZED_NAME_TASK = "task";
  @SerializedName(SERIALIZED_NAME_TASK)
  private String task;

  public static final String SERIALIZED_NAME_TIMER_TRIGGER = "timerTrigger";
  @SerializedName(SERIALIZED_NAME_TIMER_TRIGGER)
  private TimerTriggerDescriptor timerTrigger;

  public RunProperties() {
  }

  public RunProperties(
     String runErrorMessage
  ) {
    this();
    this.runErrorMessage = runErrorMessage;
  }

  public RunProperties agentConfiguration(AgentProperties agentConfiguration) {
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


  public RunProperties createTime(OffsetDateTime createTime) {
    this.createTime = createTime;
    return this;
  }

  /**
   * The time the run was scheduled.
   * @return createTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreateTime() {
    return createTime;
  }

  public void setCreateTime(OffsetDateTime createTime) {
    this.createTime = createTime;
  }


  public RunProperties customRegistries(List<String> customRegistries) {
    this.customRegistries = customRegistries;
    return this;
  }

  public RunProperties addCustomRegistriesItem(String customRegistriesItem) {
    if (this.customRegistries == null) {
      this.customRegistries = new ArrayList<>();
    }
    this.customRegistries.add(customRegistriesItem);
    return this;
  }

  /**
   * The list of custom registries that were logged in during this run.
   * @return customRegistries
   */
  @javax.annotation.Nullable
  public List<String> getCustomRegistries() {
    return customRegistries;
  }

  public void setCustomRegistries(List<String> customRegistries) {
    this.customRegistries = customRegistries;
  }


  public RunProperties finishTime(OffsetDateTime finishTime) {
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


  public RunProperties imageUpdateTrigger(ImageUpdateTrigger imageUpdateTrigger) {
    this.imageUpdateTrigger = imageUpdateTrigger;
    return this;
  }

  /**
   * Get imageUpdateTrigger
   * @return imageUpdateTrigger
   */
  @javax.annotation.Nullable
  public ImageUpdateTrigger getImageUpdateTrigger() {
    return imageUpdateTrigger;
  }

  public void setImageUpdateTrigger(ImageUpdateTrigger imageUpdateTrigger) {
    this.imageUpdateTrigger = imageUpdateTrigger;
  }


  public RunProperties isArchiveEnabled(Boolean isArchiveEnabled) {
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


  public RunProperties lastUpdatedTime(OffsetDateTime lastUpdatedTime) {
    this.lastUpdatedTime = lastUpdatedTime;
    return this;
  }

  /**
   * The last updated time for the run.
   * @return lastUpdatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastUpdatedTime() {
    return lastUpdatedTime;
  }

  public void setLastUpdatedTime(OffsetDateTime lastUpdatedTime) {
    this.lastUpdatedTime = lastUpdatedTime;
  }


  public RunProperties outputImages(List<ImageDescriptor> outputImages) {
    this.outputImages = outputImages;
    return this;
  }

  public RunProperties addOutputImagesItem(ImageDescriptor outputImagesItem) {
    if (this.outputImages == null) {
      this.outputImages = new ArrayList<>();
    }
    this.outputImages.add(outputImagesItem);
    return this;
  }

  /**
   * The list of all images that were generated from the run. This is applicable if the run generates base image dependencies.
   * @return outputImages
   */
  @javax.annotation.Nullable
  public List<ImageDescriptor> getOutputImages() {
    return outputImages;
  }

  public void setOutputImages(List<ImageDescriptor> outputImages) {
    this.outputImages = outputImages;
  }


  public RunProperties platform(PlatformProperties platform) {
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


  public RunProperties provisioningState(ProvisioningStateEnum provisioningState) {
    this.provisioningState = provisioningState;
    return this;
  }

  /**
   * The provisioning state of a run.
   * @return provisioningState
   */
  @javax.annotation.Nullable
  public ProvisioningStateEnum getProvisioningState() {
    return provisioningState;
  }

  public void setProvisioningState(ProvisioningStateEnum provisioningState) {
    this.provisioningState = provisioningState;
  }


  /**
   * The error message received from backend systems after the run is scheduled.
   * @return runErrorMessage
   */
  @javax.annotation.Nullable
  public String getRunErrorMessage() {
    return runErrorMessage;
  }



  public RunProperties runId(String runId) {
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


  public RunProperties runType(RunTypeEnum runType) {
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


  public RunProperties sourceRegistryAuth(String sourceRegistryAuth) {
    this.sourceRegistryAuth = sourceRegistryAuth;
    return this;
  }

  /**
   * The scope of the credentials that were used to login to the source registry during this run.
   * @return sourceRegistryAuth
   */
  @javax.annotation.Nullable
  public String getSourceRegistryAuth() {
    return sourceRegistryAuth;
  }

  public void setSourceRegistryAuth(String sourceRegistryAuth) {
    this.sourceRegistryAuth = sourceRegistryAuth;
  }


  public RunProperties sourceTrigger(SourceTriggerDescriptor sourceTrigger) {
    this.sourceTrigger = sourceTrigger;
    return this;
  }

  /**
   * Get sourceTrigger
   * @return sourceTrigger
   */
  @javax.annotation.Nullable
  public SourceTriggerDescriptor getSourceTrigger() {
    return sourceTrigger;
  }

  public void setSourceTrigger(SourceTriggerDescriptor sourceTrigger) {
    this.sourceTrigger = sourceTrigger;
  }


  public RunProperties startTime(OffsetDateTime startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * The time the run started.
   * @return startTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartTime() {
    return startTime;
  }

  public void setStartTime(OffsetDateTime startTime) {
    this.startTime = startTime;
  }


  public RunProperties status(StatusEnum status) {
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


  public RunProperties task(String task) {
    this.task = task;
    return this;
  }

  /**
   * The task against which run was scheduled.
   * @return task
   */
  @javax.annotation.Nullable
  public String getTask() {
    return task;
  }

  public void setTask(String task) {
    this.task = task;
  }


  public RunProperties timerTrigger(TimerTriggerDescriptor timerTrigger) {
    this.timerTrigger = timerTrigger;
    return this;
  }

  /**
   * Get timerTrigger
   * @return timerTrigger
   */
  @javax.annotation.Nullable
  public TimerTriggerDescriptor getTimerTrigger() {
    return timerTrigger;
  }

  public void setTimerTrigger(TimerTriggerDescriptor timerTrigger) {
    this.timerTrigger = timerTrigger;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RunProperties runProperties = (RunProperties) o;
    return Objects.equals(this.agentConfiguration, runProperties.agentConfiguration) &&
        Objects.equals(this.createTime, runProperties.createTime) &&
        Objects.equals(this.customRegistries, runProperties.customRegistries) &&
        Objects.equals(this.finishTime, runProperties.finishTime) &&
        Objects.equals(this.imageUpdateTrigger, runProperties.imageUpdateTrigger) &&
        Objects.equals(this.isArchiveEnabled, runProperties.isArchiveEnabled) &&
        Objects.equals(this.lastUpdatedTime, runProperties.lastUpdatedTime) &&
        Objects.equals(this.outputImages, runProperties.outputImages) &&
        Objects.equals(this.platform, runProperties.platform) &&
        Objects.equals(this.provisioningState, runProperties.provisioningState) &&
        Objects.equals(this.runErrorMessage, runProperties.runErrorMessage) &&
        Objects.equals(this.runId, runProperties.runId) &&
        Objects.equals(this.runType, runProperties.runType) &&
        Objects.equals(this.sourceRegistryAuth, runProperties.sourceRegistryAuth) &&
        Objects.equals(this.sourceTrigger, runProperties.sourceTrigger) &&
        Objects.equals(this.startTime, runProperties.startTime) &&
        Objects.equals(this.status, runProperties.status) &&
        Objects.equals(this.task, runProperties.task) &&
        Objects.equals(this.timerTrigger, runProperties.timerTrigger);
  }

  @Override
  public int hashCode() {
    return Objects.hash(agentConfiguration, createTime, customRegistries, finishTime, imageUpdateTrigger, isArchiveEnabled, lastUpdatedTime, outputImages, platform, provisioningState, runErrorMessage, runId, runType, sourceRegistryAuth, sourceTrigger, startTime, status, task, timerTrigger);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RunProperties {\n");
    sb.append("    agentConfiguration: ").append(toIndentedString(agentConfiguration)).append("\n");
    sb.append("    createTime: ").append(toIndentedString(createTime)).append("\n");
    sb.append("    customRegistries: ").append(toIndentedString(customRegistries)).append("\n");
    sb.append("    finishTime: ").append(toIndentedString(finishTime)).append("\n");
    sb.append("    imageUpdateTrigger: ").append(toIndentedString(imageUpdateTrigger)).append("\n");
    sb.append("    isArchiveEnabled: ").append(toIndentedString(isArchiveEnabled)).append("\n");
    sb.append("    lastUpdatedTime: ").append(toIndentedString(lastUpdatedTime)).append("\n");
    sb.append("    outputImages: ").append(toIndentedString(outputImages)).append("\n");
    sb.append("    platform: ").append(toIndentedString(platform)).append("\n");
    sb.append("    provisioningState: ").append(toIndentedString(provisioningState)).append("\n");
    sb.append("    runErrorMessage: ").append(toIndentedString(runErrorMessage)).append("\n");
    sb.append("    runId: ").append(toIndentedString(runId)).append("\n");
    sb.append("    runType: ").append(toIndentedString(runType)).append("\n");
    sb.append("    sourceRegistryAuth: ").append(toIndentedString(sourceRegistryAuth)).append("\n");
    sb.append("    sourceTrigger: ").append(toIndentedString(sourceTrigger)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    task: ").append(toIndentedString(task)).append("\n");
    sb.append("    timerTrigger: ").append(toIndentedString(timerTrigger)).append("\n");
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
    openapiFields.add("agentConfiguration");
    openapiFields.add("createTime");
    openapiFields.add("customRegistries");
    openapiFields.add("finishTime");
    openapiFields.add("imageUpdateTrigger");
    openapiFields.add("isArchiveEnabled");
    openapiFields.add("lastUpdatedTime");
    openapiFields.add("outputImages");
    openapiFields.add("platform");
    openapiFields.add("provisioningState");
    openapiFields.add("runErrorMessage");
    openapiFields.add("runId");
    openapiFields.add("runType");
    openapiFields.add("sourceRegistryAuth");
    openapiFields.add("sourceTrigger");
    openapiFields.add("startTime");
    openapiFields.add("status");
    openapiFields.add("task");
    openapiFields.add("timerTrigger");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RunProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RunProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RunProperties is not found in the empty JSON string", RunProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RunProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RunProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `agentConfiguration`
      if (jsonObj.get("agentConfiguration") != null && !jsonObj.get("agentConfiguration").isJsonNull()) {
        AgentProperties.validateJsonElement(jsonObj.get("agentConfiguration"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("customRegistries") != null && !jsonObj.get("customRegistries").isJsonNull() && !jsonObj.get("customRegistries").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `customRegistries` to be an array in the JSON string but got `%s`", jsonObj.get("customRegistries").toString()));
      }
      // validate the optional field `imageUpdateTrigger`
      if (jsonObj.get("imageUpdateTrigger") != null && !jsonObj.get("imageUpdateTrigger").isJsonNull()) {
        ImageUpdateTrigger.validateJsonElement(jsonObj.get("imageUpdateTrigger"));
      }
      if (jsonObj.get("outputImages") != null && !jsonObj.get("outputImages").isJsonNull()) {
        JsonArray jsonArrayoutputImages = jsonObj.getAsJsonArray("outputImages");
        if (jsonArrayoutputImages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("outputImages").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `outputImages` to be an array in the JSON string but got `%s`", jsonObj.get("outputImages").toString()));
          }

          // validate the optional field `outputImages` (array)
          for (int i = 0; i < jsonArrayoutputImages.size(); i++) {
            ImageDescriptor.validateJsonElement(jsonArrayoutputImages.get(i));
          };
        }
      }
      // validate the optional field `platform`
      if (jsonObj.get("platform") != null && !jsonObj.get("platform").isJsonNull()) {
        PlatformProperties.validateJsonElement(jsonObj.get("platform"));
      }
      if ((jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) && !jsonObj.get("provisioningState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provisioningState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provisioningState").toString()));
      }
      // validate the optional field `provisioningState`
      if (jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) {
        ProvisioningStateEnum.validateJsonElement(jsonObj.get("provisioningState"));
      }
      if ((jsonObj.get("runErrorMessage") != null && !jsonObj.get("runErrorMessage").isJsonNull()) && !jsonObj.get("runErrorMessage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `runErrorMessage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("runErrorMessage").toString()));
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
      if ((jsonObj.get("sourceRegistryAuth") != null && !jsonObj.get("sourceRegistryAuth").isJsonNull()) && !jsonObj.get("sourceRegistryAuth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceRegistryAuth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceRegistryAuth").toString()));
      }
      // validate the optional field `sourceTrigger`
      if (jsonObj.get("sourceTrigger") != null && !jsonObj.get("sourceTrigger").isJsonNull()) {
        SourceTriggerDescriptor.validateJsonElement(jsonObj.get("sourceTrigger"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("task") != null && !jsonObj.get("task").isJsonNull()) && !jsonObj.get("task").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `task` to be a primitive type in the JSON string but got `%s`", jsonObj.get("task").toString()));
      }
      // validate the optional field `timerTrigger`
      if (jsonObj.get("timerTrigger") != null && !jsonObj.get("timerTrigger").isJsonNull()) {
        TimerTriggerDescriptor.validateJsonElement(jsonObj.get("timerTrigger"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RunProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RunProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RunProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RunProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<RunProperties>() {
           @Override
           public void write(JsonWriter out, RunProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RunProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RunProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RunProperties
   * @throws IOException if the JSON string is invalid with respect to RunProperties
   */
  public static RunProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RunProperties.class);
  }

  /**
   * Convert an instance of RunProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

