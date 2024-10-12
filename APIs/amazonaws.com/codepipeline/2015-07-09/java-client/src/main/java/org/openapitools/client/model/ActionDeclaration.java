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
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.ActionDeclarationActionTypeId;

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
 * Represents information about an action declaration.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:02:26.715942-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ActionDeclaration {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ACTION_TYPE_ID = "actionTypeId";
  @SerializedName(SERIALIZED_NAME_ACTION_TYPE_ID)
  private ActionDeclarationActionTypeId actionTypeId;

  public static final String SERIALIZED_NAME_RUN_ORDER = "runOrder";
  @SerializedName(SERIALIZED_NAME_RUN_ORDER)
  private Integer runOrder;

  public static final String SERIALIZED_NAME_CONFIGURATION = "configuration";
  @SerializedName(SERIALIZED_NAME_CONFIGURATION)
  private Map _configuration;

  public static final String SERIALIZED_NAME_OUTPUT_ARTIFACTS = "outputArtifacts";
  @SerializedName(SERIALIZED_NAME_OUTPUT_ARTIFACTS)
  private List outputArtifacts;

  public static final String SERIALIZED_NAME_INPUT_ARTIFACTS = "inputArtifacts";
  @SerializedName(SERIALIZED_NAME_INPUT_ARTIFACTS)
  private List inputArtifacts;

  public static final String SERIALIZED_NAME_ROLE_ARN = "roleArn";
  @SerializedName(SERIALIZED_NAME_ROLE_ARN)
  private String roleArn;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_NAMESPACE = "namespace";
  @SerializedName(SERIALIZED_NAME_NAMESPACE)
  private String namespace;

  public ActionDeclaration() {
  }

  public ActionDeclaration name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ActionDeclaration actionTypeId(ActionDeclarationActionTypeId actionTypeId) {
    this.actionTypeId = actionTypeId;
    return this;
  }

  /**
   * Get actionTypeId
   * @return actionTypeId
   */
  @javax.annotation.Nonnull
  public ActionDeclarationActionTypeId getActionTypeId() {
    return actionTypeId;
  }

  public void setActionTypeId(ActionDeclarationActionTypeId actionTypeId) {
    this.actionTypeId = actionTypeId;
  }


  public ActionDeclaration runOrder(Integer runOrder) {
    this.runOrder = runOrder;
    return this;
  }

  /**
   * Get runOrder
   * @return runOrder
   */
  @javax.annotation.Nullable
  public Integer getRunOrder() {
    return runOrder;
  }

  public void setRunOrder(Integer runOrder) {
    this.runOrder = runOrder;
  }


  public ActionDeclaration _configuration(Map _configuration) {
    this._configuration = _configuration;
    return this;
  }

  /**
   * Get _configuration
   * @return _configuration
   */
  @javax.annotation.Nullable
  public Map getConfiguration() {
    return _configuration;
  }

  public void setConfiguration(Map _configuration) {
    this._configuration = _configuration;
  }


  public ActionDeclaration outputArtifacts(List outputArtifacts) {
    this.outputArtifacts = outputArtifacts;
    return this;
  }

  /**
   * Get outputArtifacts
   * @return outputArtifacts
   */
  @javax.annotation.Nullable
  public List getOutputArtifacts() {
    return outputArtifacts;
  }

  public void setOutputArtifacts(List outputArtifacts) {
    this.outputArtifacts = outputArtifacts;
  }


  public ActionDeclaration inputArtifacts(List inputArtifacts) {
    this.inputArtifacts = inputArtifacts;
    return this;
  }

  /**
   * Get inputArtifacts
   * @return inputArtifacts
   */
  @javax.annotation.Nullable
  public List getInputArtifacts() {
    return inputArtifacts;
  }

  public void setInputArtifacts(List inputArtifacts) {
    this.inputArtifacts = inputArtifacts;
  }


  public ActionDeclaration roleArn(String roleArn) {
    this.roleArn = roleArn;
    return this;
  }

  /**
   * Get roleArn
   * @return roleArn
   */
  @javax.annotation.Nullable
  public String getRoleArn() {
    return roleArn;
  }

  public void setRoleArn(String roleArn) {
    this.roleArn = roleArn;
  }


  public ActionDeclaration region(String region) {
    this.region = region;
    return this;
  }

  /**
   * Get region
   * @return region
   */
  @javax.annotation.Nullable
  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }


  public ActionDeclaration namespace(String namespace) {
    this.namespace = namespace;
    return this;
  }

  /**
   * Get namespace
   * @return namespace
   */
  @javax.annotation.Nullable
  public String getNamespace() {
    return namespace;
  }

  public void setNamespace(String namespace) {
    this.namespace = namespace;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ActionDeclaration actionDeclaration = (ActionDeclaration) o;
    return Objects.equals(this.name, actionDeclaration.name) &&
        Objects.equals(this.actionTypeId, actionDeclaration.actionTypeId) &&
        Objects.equals(this.runOrder, actionDeclaration.runOrder) &&
        Objects.equals(this._configuration, actionDeclaration._configuration) &&
        Objects.equals(this.outputArtifacts, actionDeclaration.outputArtifacts) &&
        Objects.equals(this.inputArtifacts, actionDeclaration.inputArtifacts) &&
        Objects.equals(this.roleArn, actionDeclaration.roleArn) &&
        Objects.equals(this.region, actionDeclaration.region) &&
        Objects.equals(this.namespace, actionDeclaration.namespace);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, actionTypeId, runOrder, _configuration, outputArtifacts, inputArtifacts, roleArn, region, namespace);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ActionDeclaration {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    actionTypeId: ").append(toIndentedString(actionTypeId)).append("\n");
    sb.append("    runOrder: ").append(toIndentedString(runOrder)).append("\n");
    sb.append("    _configuration: ").append(toIndentedString(_configuration)).append("\n");
    sb.append("    outputArtifacts: ").append(toIndentedString(outputArtifacts)).append("\n");
    sb.append("    inputArtifacts: ").append(toIndentedString(inputArtifacts)).append("\n");
    sb.append("    roleArn: ").append(toIndentedString(roleArn)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    namespace: ").append(toIndentedString(namespace)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("actionTypeId");
    openapiFields.add("runOrder");
    openapiFields.add("configuration");
    openapiFields.add("outputArtifacts");
    openapiFields.add("inputArtifacts");
    openapiFields.add("roleArn");
    openapiFields.add("region");
    openapiFields.add("namespace");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("actionTypeId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ActionDeclaration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ActionDeclaration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ActionDeclaration is not found in the empty JSON string", ActionDeclaration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ActionDeclaration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ActionDeclaration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ActionDeclaration.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `name`
      String.validateJsonElement(jsonObj.get("name"));
      // validate the required field `actionTypeId`
      ActionDeclarationActionTypeId.validateJsonElement(jsonObj.get("actionTypeId"));
      // validate the optional field `runOrder`
      if (jsonObj.get("runOrder") != null && !jsonObj.get("runOrder").isJsonNull()) {
        Integer.validateJsonElement(jsonObj.get("runOrder"));
      }
      // validate the optional field `configuration`
      if (jsonObj.get("configuration") != null && !jsonObj.get("configuration").isJsonNull()) {
        Map.validateJsonElement(jsonObj.get("configuration"));
      }
      // validate the optional field `outputArtifacts`
      if (jsonObj.get("outputArtifacts") != null && !jsonObj.get("outputArtifacts").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("outputArtifacts"));
      }
      // validate the optional field `inputArtifacts`
      if (jsonObj.get("inputArtifacts") != null && !jsonObj.get("inputArtifacts").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("inputArtifacts"));
      }
      // validate the optional field `roleArn`
      if (jsonObj.get("roleArn") != null && !jsonObj.get("roleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("roleArn"));
      }
      // validate the optional field `region`
      if (jsonObj.get("region") != null && !jsonObj.get("region").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("region"));
      }
      // validate the optional field `namespace`
      if (jsonObj.get("namespace") != null && !jsonObj.get("namespace").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("namespace"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ActionDeclaration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ActionDeclaration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ActionDeclaration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ActionDeclaration.class));

       return (TypeAdapter<T>) new TypeAdapter<ActionDeclaration>() {
           @Override
           public void write(JsonWriter out, ActionDeclaration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ActionDeclaration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ActionDeclaration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ActionDeclaration
   * @throws IOException if the JSON string is invalid with respect to ActionDeclaration
   */
  public static ActionDeclaration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ActionDeclaration.class);
  }

  /**
   * Convert an instance of ActionDeclaration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

