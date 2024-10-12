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
import org.openapitools.client.model.ActionExecutionDetailInput;
import org.openapitools.client.model.ActionExecutionDetailOutput;
import org.openapitools.client.model.ActionExecutionStatus;

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
 * Returns information about an execution of an action, including the action execution ID, and the name, version, and timing of the action. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:02:26.715942-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ActionExecutionDetail {
  public static final String SERIALIZED_NAME_PIPELINE_EXECUTION_ID = "pipelineExecutionId";
  @SerializedName(SERIALIZED_NAME_PIPELINE_EXECUTION_ID)
  private String pipelineExecutionId;

  public static final String SERIALIZED_NAME_ACTION_EXECUTION_ID = "actionExecutionId";
  @SerializedName(SERIALIZED_NAME_ACTION_EXECUTION_ID)
  private String actionExecutionId;

  public static final String SERIALIZED_NAME_PIPELINE_VERSION = "pipelineVersion";
  @SerializedName(SERIALIZED_NAME_PIPELINE_VERSION)
  private Integer pipelineVersion;

  public static final String SERIALIZED_NAME_STAGE_NAME = "stageName";
  @SerializedName(SERIALIZED_NAME_STAGE_NAME)
  private String stageName;

  public static final String SERIALIZED_NAME_ACTION_NAME = "actionName";
  @SerializedName(SERIALIZED_NAME_ACTION_NAME)
  private String actionName;

  public static final String SERIALIZED_NAME_START_TIME = "startTime";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private OffsetDateTime startTime;

  public static final String SERIALIZED_NAME_LAST_UPDATE_TIME = "lastUpdateTime";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATE_TIME)
  private OffsetDateTime lastUpdateTime;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private ActionExecutionStatus status;

  public static final String SERIALIZED_NAME_INPUT = "input";
  @SerializedName(SERIALIZED_NAME_INPUT)
  private ActionExecutionDetailInput input;

  public static final String SERIALIZED_NAME_OUTPUT = "output";
  @SerializedName(SERIALIZED_NAME_OUTPUT)
  private ActionExecutionDetailOutput output;

  public ActionExecutionDetail() {
  }

  public ActionExecutionDetail pipelineExecutionId(String pipelineExecutionId) {
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


  public ActionExecutionDetail actionExecutionId(String actionExecutionId) {
    this.actionExecutionId = actionExecutionId;
    return this;
  }

  /**
   * Get actionExecutionId
   * @return actionExecutionId
   */
  @javax.annotation.Nullable
  public String getActionExecutionId() {
    return actionExecutionId;
  }

  public void setActionExecutionId(String actionExecutionId) {
    this.actionExecutionId = actionExecutionId;
  }


  public ActionExecutionDetail pipelineVersion(Integer pipelineVersion) {
    this.pipelineVersion = pipelineVersion;
    return this;
  }

  /**
   * Get pipelineVersion
   * @return pipelineVersion
   */
  @javax.annotation.Nullable
  public Integer getPipelineVersion() {
    return pipelineVersion;
  }

  public void setPipelineVersion(Integer pipelineVersion) {
    this.pipelineVersion = pipelineVersion;
  }


  public ActionExecutionDetail stageName(String stageName) {
    this.stageName = stageName;
    return this;
  }

  /**
   * Get stageName
   * @return stageName
   */
  @javax.annotation.Nullable
  public String getStageName() {
    return stageName;
  }

  public void setStageName(String stageName) {
    this.stageName = stageName;
  }


  public ActionExecutionDetail actionName(String actionName) {
    this.actionName = actionName;
    return this;
  }

  /**
   * Get actionName
   * @return actionName
   */
  @javax.annotation.Nullable
  public String getActionName() {
    return actionName;
  }

  public void setActionName(String actionName) {
    this.actionName = actionName;
  }


  public ActionExecutionDetail startTime(OffsetDateTime startTime) {
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


  public ActionExecutionDetail lastUpdateTime(OffsetDateTime lastUpdateTime) {
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


  public ActionExecutionDetail status(ActionExecutionStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public ActionExecutionStatus getStatus() {
    return status;
  }

  public void setStatus(ActionExecutionStatus status) {
    this.status = status;
  }


  public ActionExecutionDetail input(ActionExecutionDetailInput input) {
    this.input = input;
    return this;
  }

  /**
   * Get input
   * @return input
   */
  @javax.annotation.Nullable
  public ActionExecutionDetailInput getInput() {
    return input;
  }

  public void setInput(ActionExecutionDetailInput input) {
    this.input = input;
  }


  public ActionExecutionDetail output(ActionExecutionDetailOutput output) {
    this.output = output;
    return this;
  }

  /**
   * Get output
   * @return output
   */
  @javax.annotation.Nullable
  public ActionExecutionDetailOutput getOutput() {
    return output;
  }

  public void setOutput(ActionExecutionDetailOutput output) {
    this.output = output;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ActionExecutionDetail actionExecutionDetail = (ActionExecutionDetail) o;
    return Objects.equals(this.pipelineExecutionId, actionExecutionDetail.pipelineExecutionId) &&
        Objects.equals(this.actionExecutionId, actionExecutionDetail.actionExecutionId) &&
        Objects.equals(this.pipelineVersion, actionExecutionDetail.pipelineVersion) &&
        Objects.equals(this.stageName, actionExecutionDetail.stageName) &&
        Objects.equals(this.actionName, actionExecutionDetail.actionName) &&
        Objects.equals(this.startTime, actionExecutionDetail.startTime) &&
        Objects.equals(this.lastUpdateTime, actionExecutionDetail.lastUpdateTime) &&
        Objects.equals(this.status, actionExecutionDetail.status) &&
        Objects.equals(this.input, actionExecutionDetail.input) &&
        Objects.equals(this.output, actionExecutionDetail.output);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pipelineExecutionId, actionExecutionId, pipelineVersion, stageName, actionName, startTime, lastUpdateTime, status, input, output);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ActionExecutionDetail {\n");
    sb.append("    pipelineExecutionId: ").append(toIndentedString(pipelineExecutionId)).append("\n");
    sb.append("    actionExecutionId: ").append(toIndentedString(actionExecutionId)).append("\n");
    sb.append("    pipelineVersion: ").append(toIndentedString(pipelineVersion)).append("\n");
    sb.append("    stageName: ").append(toIndentedString(stageName)).append("\n");
    sb.append("    actionName: ").append(toIndentedString(actionName)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    lastUpdateTime: ").append(toIndentedString(lastUpdateTime)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    input: ").append(toIndentedString(input)).append("\n");
    sb.append("    output: ").append(toIndentedString(output)).append("\n");
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
    openapiFields.add("actionExecutionId");
    openapiFields.add("pipelineVersion");
    openapiFields.add("stageName");
    openapiFields.add("actionName");
    openapiFields.add("startTime");
    openapiFields.add("lastUpdateTime");
    openapiFields.add("status");
    openapiFields.add("input");
    openapiFields.add("output");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ActionExecutionDetail
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ActionExecutionDetail.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ActionExecutionDetail is not found in the empty JSON string", ActionExecutionDetail.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ActionExecutionDetail.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ActionExecutionDetail` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `pipelineExecutionId`
      if (jsonObj.get("pipelineExecutionId") != null && !jsonObj.get("pipelineExecutionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("pipelineExecutionId"));
      }
      // validate the optional field `actionExecutionId`
      if (jsonObj.get("actionExecutionId") != null && !jsonObj.get("actionExecutionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("actionExecutionId"));
      }
      // validate the optional field `pipelineVersion`
      if (jsonObj.get("pipelineVersion") != null && !jsonObj.get("pipelineVersion").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("pipelineVersion"));
      }
      // validate the optional field `stageName`
      if (jsonObj.get("stageName") != null && !jsonObj.get("stageName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("stageName"));
      }
      // validate the optional field `actionName`
      if (jsonObj.get("actionName") != null && !jsonObj.get("actionName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("actionName"));
      }
      // validate the optional field `startTime`
      if (jsonObj.get("startTime") != null && !jsonObj.get("startTime").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("startTime"));
      }
      // validate the optional field `lastUpdateTime`
      if (jsonObj.get("lastUpdateTime") != null && !jsonObj.get("lastUpdateTime").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("lastUpdateTime"));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        ActionExecutionStatus.validateJsonElement(jsonObj.get("status"));
      }
      // validate the optional field `input`
      if (jsonObj.get("input") != null && !jsonObj.get("input").isJsonNull()) {
        ActionExecutionDetailInput.validateJsonElement(jsonObj.get("input"));
      }
      // validate the optional field `output`
      if (jsonObj.get("output") != null && !jsonObj.get("output").isJsonNull()) {
        ActionExecutionDetailOutput.validateJsonElement(jsonObj.get("output"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ActionExecutionDetail.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ActionExecutionDetail' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ActionExecutionDetail> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ActionExecutionDetail.class));

       return (TypeAdapter<T>) new TypeAdapter<ActionExecutionDetail>() {
           @Override
           public void write(JsonWriter out, ActionExecutionDetail value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ActionExecutionDetail read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ActionExecutionDetail given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ActionExecutionDetail
   * @throws IOException if the JSON string is invalid with respect to ActionExecutionDetail
   */
  public static ActionExecutionDetail fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ActionExecutionDetail.class);
  }

  /**
   * Convert an instance of ActionExecutionDetail to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

