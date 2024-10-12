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
import org.openapitools.client.model.ActionExecutionErrorDetails;
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
 * ActionStateLatestExecution
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:02:26.715942-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ActionStateLatestExecution {
  public static final String SERIALIZED_NAME_ACTION_EXECUTION_ID = "actionExecutionId";
  @SerializedName(SERIALIZED_NAME_ACTION_EXECUTION_ID)
  private String actionExecutionId;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private ActionExecutionStatus status;

  public static final String SERIALIZED_NAME_SUMMARY = "summary";
  @SerializedName(SERIALIZED_NAME_SUMMARY)
  private String summary;

  public static final String SERIALIZED_NAME_LAST_STATUS_CHANGE = "lastStatusChange";
  @SerializedName(SERIALIZED_NAME_LAST_STATUS_CHANGE)
  private OffsetDateTime lastStatusChange;

  public static final String SERIALIZED_NAME_TOKEN = "token";
  @SerializedName(SERIALIZED_NAME_TOKEN)
  private String token;

  public static final String SERIALIZED_NAME_LAST_UPDATED_BY = "lastUpdatedBy";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED_BY)
  private String lastUpdatedBy;

  public static final String SERIALIZED_NAME_EXTERNAL_EXECUTION_ID = "externalExecutionId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_EXECUTION_ID)
  private String externalExecutionId;

  public static final String SERIALIZED_NAME_EXTERNAL_EXECUTION_URL = "externalExecutionUrl";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_EXECUTION_URL)
  private String externalExecutionUrl;

  public static final String SERIALIZED_NAME_PERCENT_COMPLETE = "percentComplete";
  @SerializedName(SERIALIZED_NAME_PERCENT_COMPLETE)
  private Integer percentComplete;

  public static final String SERIALIZED_NAME_ERROR_DETAILS = "errorDetails";
  @SerializedName(SERIALIZED_NAME_ERROR_DETAILS)
  private ActionExecutionErrorDetails errorDetails;

  public ActionStateLatestExecution() {
  }

  public ActionStateLatestExecution actionExecutionId(String actionExecutionId) {
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


  public ActionStateLatestExecution status(ActionExecutionStatus status) {
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


  public ActionStateLatestExecution summary(String summary) {
    this.summary = summary;
    return this;
  }

  /**
   * Get summary
   * @return summary
   */
  @javax.annotation.Nullable
  public String getSummary() {
    return summary;
  }

  public void setSummary(String summary) {
    this.summary = summary;
  }


  public ActionStateLatestExecution lastStatusChange(OffsetDateTime lastStatusChange) {
    this.lastStatusChange = lastStatusChange;
    return this;
  }

  /**
   * Get lastStatusChange
   * @return lastStatusChange
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastStatusChange() {
    return lastStatusChange;
  }

  public void setLastStatusChange(OffsetDateTime lastStatusChange) {
    this.lastStatusChange = lastStatusChange;
  }


  public ActionStateLatestExecution token(String token) {
    this.token = token;
    return this;
  }

  /**
   * Get token
   * @return token
   */
  @javax.annotation.Nullable
  public String getToken() {
    return token;
  }

  public void setToken(String token) {
    this.token = token;
  }


  public ActionStateLatestExecution lastUpdatedBy(String lastUpdatedBy) {
    this.lastUpdatedBy = lastUpdatedBy;
    return this;
  }

  /**
   * Get lastUpdatedBy
   * @return lastUpdatedBy
   */
  @javax.annotation.Nullable
  public String getLastUpdatedBy() {
    return lastUpdatedBy;
  }

  public void setLastUpdatedBy(String lastUpdatedBy) {
    this.lastUpdatedBy = lastUpdatedBy;
  }


  public ActionStateLatestExecution externalExecutionId(String externalExecutionId) {
    this.externalExecutionId = externalExecutionId;
    return this;
  }

  /**
   * Get externalExecutionId
   * @return externalExecutionId
   */
  @javax.annotation.Nullable
  public String getExternalExecutionId() {
    return externalExecutionId;
  }

  public void setExternalExecutionId(String externalExecutionId) {
    this.externalExecutionId = externalExecutionId;
  }


  public ActionStateLatestExecution externalExecutionUrl(String externalExecutionUrl) {
    this.externalExecutionUrl = externalExecutionUrl;
    return this;
  }

  /**
   * Get externalExecutionUrl
   * @return externalExecutionUrl
   */
  @javax.annotation.Nullable
  public String getExternalExecutionUrl() {
    return externalExecutionUrl;
  }

  public void setExternalExecutionUrl(String externalExecutionUrl) {
    this.externalExecutionUrl = externalExecutionUrl;
  }


  public ActionStateLatestExecution percentComplete(Integer percentComplete) {
    this.percentComplete = percentComplete;
    return this;
  }

  /**
   * Get percentComplete
   * @return percentComplete
   */
  @javax.annotation.Nullable
  public Integer getPercentComplete() {
    return percentComplete;
  }

  public void setPercentComplete(Integer percentComplete) {
    this.percentComplete = percentComplete;
  }


  public ActionStateLatestExecution errorDetails(ActionExecutionErrorDetails errorDetails) {
    this.errorDetails = errorDetails;
    return this;
  }

  /**
   * Get errorDetails
   * @return errorDetails
   */
  @javax.annotation.Nullable
  public ActionExecutionErrorDetails getErrorDetails() {
    return errorDetails;
  }

  public void setErrorDetails(ActionExecutionErrorDetails errorDetails) {
    this.errorDetails = errorDetails;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ActionStateLatestExecution actionStateLatestExecution = (ActionStateLatestExecution) o;
    return Objects.equals(this.actionExecutionId, actionStateLatestExecution.actionExecutionId) &&
        Objects.equals(this.status, actionStateLatestExecution.status) &&
        Objects.equals(this.summary, actionStateLatestExecution.summary) &&
        Objects.equals(this.lastStatusChange, actionStateLatestExecution.lastStatusChange) &&
        Objects.equals(this.token, actionStateLatestExecution.token) &&
        Objects.equals(this.lastUpdatedBy, actionStateLatestExecution.lastUpdatedBy) &&
        Objects.equals(this.externalExecutionId, actionStateLatestExecution.externalExecutionId) &&
        Objects.equals(this.externalExecutionUrl, actionStateLatestExecution.externalExecutionUrl) &&
        Objects.equals(this.percentComplete, actionStateLatestExecution.percentComplete) &&
        Objects.equals(this.errorDetails, actionStateLatestExecution.errorDetails);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actionExecutionId, status, summary, lastStatusChange, token, lastUpdatedBy, externalExecutionId, externalExecutionUrl, percentComplete, errorDetails);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ActionStateLatestExecution {\n");
    sb.append("    actionExecutionId: ").append(toIndentedString(actionExecutionId)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    summary: ").append(toIndentedString(summary)).append("\n");
    sb.append("    lastStatusChange: ").append(toIndentedString(lastStatusChange)).append("\n");
    sb.append("    token: ").append(toIndentedString(token)).append("\n");
    sb.append("    lastUpdatedBy: ").append(toIndentedString(lastUpdatedBy)).append("\n");
    sb.append("    externalExecutionId: ").append(toIndentedString(externalExecutionId)).append("\n");
    sb.append("    externalExecutionUrl: ").append(toIndentedString(externalExecutionUrl)).append("\n");
    sb.append("    percentComplete: ").append(toIndentedString(percentComplete)).append("\n");
    sb.append("    errorDetails: ").append(toIndentedString(errorDetails)).append("\n");
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
    openapiFields.add("actionExecutionId");
    openapiFields.add("status");
    openapiFields.add("summary");
    openapiFields.add("lastStatusChange");
    openapiFields.add("token");
    openapiFields.add("lastUpdatedBy");
    openapiFields.add("externalExecutionId");
    openapiFields.add("externalExecutionUrl");
    openapiFields.add("percentComplete");
    openapiFields.add("errorDetails");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ActionStateLatestExecution
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ActionStateLatestExecution.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ActionStateLatestExecution is not found in the empty JSON string", ActionStateLatestExecution.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ActionStateLatestExecution.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ActionStateLatestExecution` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `actionExecutionId`
      if (jsonObj.get("actionExecutionId") != null && !jsonObj.get("actionExecutionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("actionExecutionId"));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        ActionExecutionStatus.validateJsonElement(jsonObj.get("status"));
      }
      // validate the optional field `summary`
      if (jsonObj.get("summary") != null && !jsonObj.get("summary").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("summary"));
      }
      // validate the optional field `lastStatusChange`
      if (jsonObj.get("lastStatusChange") != null && !jsonObj.get("lastStatusChange").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("lastStatusChange"));
      }
      // validate the optional field `token`
      if (jsonObj.get("token") != null && !jsonObj.get("token").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("token"));
      }
      // validate the optional field `lastUpdatedBy`
      if (jsonObj.get("lastUpdatedBy") != null && !jsonObj.get("lastUpdatedBy").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("lastUpdatedBy"));
      }
      // validate the optional field `externalExecutionId`
      if (jsonObj.get("externalExecutionId") != null && !jsonObj.get("externalExecutionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("externalExecutionId"));
      }
      // validate the optional field `externalExecutionUrl`
      if (jsonObj.get("externalExecutionUrl") != null && !jsonObj.get("externalExecutionUrl").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("externalExecutionUrl"));
      }
      // validate the optional field `percentComplete`
      if (jsonObj.get("percentComplete") != null && !jsonObj.get("percentComplete").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("percentComplete"));
      }
      // validate the optional field `errorDetails`
      if (jsonObj.get("errorDetails") != null && !jsonObj.get("errorDetails").isJsonNull()) {
        ActionExecutionErrorDetails.validateJsonElement(jsonObj.get("errorDetails"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ActionStateLatestExecution.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ActionStateLatestExecution' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ActionStateLatestExecution> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ActionStateLatestExecution.class));

       return (TypeAdapter<T>) new TypeAdapter<ActionStateLatestExecution>() {
           @Override
           public void write(JsonWriter out, ActionStateLatestExecution value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ActionStateLatestExecution read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ActionStateLatestExecution given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ActionStateLatestExecution
   * @throws IOException if the JSON string is invalid with respect to ActionStateLatestExecution
   */
  public static ActionStateLatestExecution fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ActionStateLatestExecution.class);
  }

  /**
   * Convert an instance of ActionStateLatestExecution to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

