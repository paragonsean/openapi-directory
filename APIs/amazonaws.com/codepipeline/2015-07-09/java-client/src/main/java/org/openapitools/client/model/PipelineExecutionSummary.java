/*
 * AWS CodePipeline
 * <fullname>CodePipeline</fullname> <p> <b>Overview</b> </p> <p>This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html\">CodePipeline User Guide</a>.</p> <p>You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.</p> <p> <i>Pipelines</i> are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions. </p> <p>You can work with pipelines by calling:</p> <ul> <li> <p> <a>CreatePipeline</a>, which creates a uniquely named pipeline.</p> </li> <li> <p> <a>DeletePipeline</a>, which deletes the specified pipeline.</p> </li> <li> <p> <a>GetPipeline</a>, which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).</p> </li> <li> <p> <a>GetPipelineExecution</a>, which returns information about a specific execution of a pipeline.</p> </li> <li> <p> <a>GetPipelineState</a>, which returns information about the current state of the stages and actions of a pipeline.</p> </li> <li> <p> <a>ListActionExecutions</a>, which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.</p> </li> <li> <p> <a>ListPipelines</a>, which gets a summary of all of the pipelines associated with your account.</p> </li> <li> <p> <a>ListPipelineExecutions</a>, which gets a summary of the most recent executions for a pipeline.</p> </li> <li> <p> <a>StartPipelineExecution</a>, which runs the most recent revision of an artifact through the pipeline.</p> </li> <li> <p> <a>StopPipelineExecution</a>, which stops the specified pipeline execution from continuing through the pipeline.</p> </li> <li> <p> <a>UpdatePipeline</a>, which updates a pipeline with edits or changes to the structure of the pipeline.</p> </li> </ul> <p>Pipelines include <i>stages</i>. Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call <a>GetPipelineState</a>, which displays the status of a pipeline, including the status of stages in the pipeline, or <a>GetPipeline</a>, which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see <a href=\"https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html\">CodePipeline Pipeline Structure Reference</a>.</p> <p>Pipeline stages include <i>actions</i> that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as <a>CreatePipeline</a> and <a>GetPipelineState</a>. Valid action categories are:</p> <ul> <li> <p>Source</p> </li> <li> <p>Build</p> </li> <li> <p>Test</p> </li> <li> <p>Deploy</p> </li> <li> <p>Approval</p> </li> <li> <p>Invoke</p> </li> </ul> <p>Pipelines also include <i>transitions</i>, which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.</p> <p>You can work with transitions by calling:</p> <ul> <li> <p> <a>DisableStageTransition</a>, which prevents artifacts from transitioning to the next stage in a pipeline.</p> </li> <li> <p> <a>EnableStageTransition</a>, which enables transition of artifacts between stages in a pipeline. </p> </li> </ul> <p> <b>Using the API to integrate with CodePipeline</b> </p> <p>For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:</p> <p> <b>Jobs</b>, which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source. </p> <p>You can work with jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetJobDetails</a>, which returns the details of a job.</p> </li> <li> <p> <a>PollForJobs</a>, which determines whether there are any jobs to act on.</p> </li> <li> <p> <a>PutJobFailureResult</a>, which provides details of a job failure. </p> </li> <li> <p> <a>PutJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul> <p> <b>Third party jobs</b>, which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.</p> <p>You can work with third party jobs by calling:</p> <ul> <li> <p> <a>AcknowledgeThirdPartyJob</a>, which confirms whether a job worker has received the specified job.</p> </li> <li> <p> <a>GetThirdPartyJobDetails</a>, which requests the details of a job for a partner action.</p> </li> <li> <p> <a>PollForThirdPartyJobs</a>, which determines whether there are any jobs to act on. </p> </li> <li> <p> <a>PutThirdPartyJobFailureResult</a>, which provides details of a job failure.</p> </li> <li> <p> <a>PutThirdPartyJobSuccessResult</a>, which provides details of a job success.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2015-07-09
 * Contact: mike.ralphson@gmail.com
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
import java.util.List;
import org.openapitools.client.model.PipelineExecutionStatus;
import org.openapitools.client.model.PipelineExecutionSummaryStopTrigger;
import org.openapitools.client.model.PipelineExecutionSummaryTrigger;

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
 * Summary information about a pipeline execution.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:02:26.715942-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PipelineExecutionSummary {
  public static final String SERIALIZED_NAME_PIPELINE_EXECUTION_ID = "pipelineExecutionId";
  @SerializedName(SERIALIZED_NAME_PIPELINE_EXECUTION_ID)
  private String pipelineExecutionId;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private PipelineExecutionStatus status;

  public static final String SERIALIZED_NAME_START_TIME = "startTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private OffsetDateTime startTime;

  public static final String SERIALIZED_NAME_LAST_UPDATE_TIME = "lastUpdateTime";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE_TIME)
  private OffsetDateTime lastUpdateTime;

  public static final String SERIALIZED_NAME_SOURCE_REVISIONS = "sourceRevisions";
  @SerializedName(SERIALIZED_NAME_SOURCE_REVISIONS)
  private List sourceRevisions;

  public static final String SERIALIZED_NAME_TRIGGER = "trigger";
  @SerializedName(SERIALIZED_NAME_TRIGGER)
  private PipelineExecutionSummaryTrigger trigger;

  public static final String SERIALIZED_NAME_STOP_TRIGGER = "stopTrigger";
  @SerializedName(SERIALIZED_NAME_STOP_TRIGGER)
  private PipelineExecutionSummaryStopTrigger stopTrigger;

  public PipelineExecutionSummary() {
  }

  public PipelineExecutionSummary pipelineExecutionId(String pipelineExecutionId) {
    this.pipelineExecutionId = pipelineExecutionId;
    return this;
  }

  /**
   * Get pipelineExecutionId
   * @return pipelineExecutionId
   */
  @javax.annotation.Nullable
  public String getPipelineExecutionId() {
    return pipelineExecutionId;
  }

  public void setPipelineExecutionId(String pipelineExecutionId) {
    this.pipelineExecutionId = pipelineExecutionId;
  }


  public PipelineExecutionSummary status(PipelineExecutionStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public PipelineExecutionStatus getStatus() {
    return status;
  }

  public void setStatus(PipelineExecutionStatus status) {
    this.status = status;
  }


  public PipelineExecutionSummary startTime(OffsetDateTime startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Get startTime
   * @return startTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStartTime() {
    return startTime;
  }

  public void setStartTime(OffsetDateTime startTime) {
    this.startTime = startTime;
  }


  public PipelineExecutionSummary lastUpdateTime(OffsetDateTime lastUpdateTime) {
    this.lastUpdateTime = lastUpdateTime;
    return this;
  }

  /**
   * Get lastUpdateTime
   * @return lastUpdateTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastUpdateTime() {
    return lastUpdateTime;
  }

  public void setLastUpdateTime(OffsetDateTime lastUpdateTime) {
    this.lastUpdateTime = lastUpdateTime;
  }


  public PipelineExecutionSummary sourceRevisions(List sourceRevisions) {
    this.sourceRevisions = sourceRevisions;
    return this;
  }

  /**
   * Get sourceRevisions
   * @return sourceRevisions
   */
  @javax.annotation.Nullable
  public List getSourceRevisions() {
    return sourceRevisions;
  }

  public void setSourceRevisions(List sourceRevisions) {
    this.sourceRevisions = sourceRevisions;
  }


  public PipelineExecutionSummary trigger(PipelineExecutionSummaryTrigger trigger) {
    this.trigger = trigger;
    return this;
  }

  /**
   * Get trigger
   * @return trigger
   */
  @javax.annotation.Nullable
  public PipelineExecutionSummaryTrigger getTrigger() {
    return trigger;
  }

  public void setTrigger(PipelineExecutionSummaryTrigger trigger) {
    this.trigger = trigger;
  }


  public PipelineExecutionSummary stopTrigger(PipelineExecutionSummaryStopTrigger stopTrigger) {
    this.stopTrigger = stopTrigger;
    return this;
  }

  /**
   * Get stopTrigger
   * @return stopTrigger
   */
  @javax.annotation.Nullable
  public PipelineExecutionSummaryStopTrigger getStopTrigger() {
    return stopTrigger;
  }

  public void setStopTrigger(PipelineExecutionSummaryStopTrigger stopTrigger) {
    this.stopTrigger = stopTrigger;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PipelineExecutionSummary pipelineExecutionSummary = (PipelineExecutionSummary) o;
    return Objects.equals(this.pipelineExecutionId, pipelineExecutionSummary.pipelineExecutionId) &&
        Objects.equals(this.status, pipelineExecutionSummary.status) &&
        Objects.equals(this.startTime, pipelineExecutionSummary.startTime) &&
        Objects.equals(this.lastUpdateTime, pipelineExecutionSummary.lastUpdateTime) &&
        Objects.equals(this.sourceRevisions, pipelineExecutionSummary.sourceRevisions) &&
        Objects.equals(this.trigger, pipelineExecutionSummary.trigger) &&
        Objects.equals(this.stopTrigger, pipelineExecutionSummary.stopTrigger);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pipelineExecutionId, status, startTime, lastUpdateTime, sourceRevisions, trigger, stopTrigger);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PipelineExecutionSummary {\n");
    sb.append("    pipelineExecutionId: ").append(toIndentedString(pipelineExecutionId)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    lastUpdateTime: ").append(toIndentedString(lastUpdateTime)).append("\n");
    sb.append("    sourceRevisions: ").append(toIndentedString(sourceRevisions)).append("\n");
    sb.append("    trigger: ").append(toIndentedString(trigger)).append("\n");
    sb.append("    stopTrigger: ").append(toIndentedString(stopTrigger)).append("\n");
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
    openapiFields.add("pipelineExecutionId");
    openapiFields.add("status");
    openapiFields.add("startTime");
    openapiFields.add("lastUpdateTime");
    openapiFields.add("sourceRevisions");
    openapiFields.add("trigger");
    openapiFields.add("stopTrigger");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PipelineExecutionSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PipelineExecutionSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PipelineExecutionSummary is not found in the empty JSON string", PipelineExecutionSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PipelineExecutionSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PipelineExecutionSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `pipelineExecutionId`
      if (jsonObj.get("pipelineExecutionId") != null && !jsonObj.get("pipelineExecutionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("pipelineExecutionId"));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        PipelineExecutionStatus.validateJsonElement(jsonObj.get("status"));
      }
      // validate the optional field `startTime`
      if (jsonObj.get("startTime") != null && !jsonObj.get("startTime").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("startTime"));
      }
      // validate the optional field `lastUpdateTime`
      if (jsonObj.get("lastUpdateTime") != null && !jsonObj.get("lastUpdateTime").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("lastUpdateTime"));
      }
      // validate the optional field `sourceRevisions`
      if (jsonObj.get("sourceRevisions") != null && !jsonObj.get("sourceRevisions").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("sourceRevisions"));
      }
      // validate the optional field `trigger`
      if (jsonObj.get("trigger") != null && !jsonObj.get("trigger").isJsonNull()) {
        PipelineExecutionSummaryTrigger.validateJsonElement(jsonObj.get("trigger"));
      }
      // validate the optional field `stopTrigger`
      if (jsonObj.get("stopTrigger") != null && !jsonObj.get("stopTrigger").isJsonNull()) {
        PipelineExecutionSummaryStopTrigger.validateJsonElement(jsonObj.get("stopTrigger"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PipelineExecutionSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PipelineExecutionSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PipelineExecutionSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PipelineExecutionSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<PipelineExecutionSummary>() {
           @Override
           public void write(JsonWriter out, PipelineExecutionSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PipelineExecutionSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PipelineExecutionSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PipelineExecutionSummary
   * @throws IOException if the JSON string is invalid with respect to PipelineExecutionSummary
   */
  public static PipelineExecutionSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PipelineExecutionSummary.class);
  }

  /**
   * Convert an instance of PipelineExecutionSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

