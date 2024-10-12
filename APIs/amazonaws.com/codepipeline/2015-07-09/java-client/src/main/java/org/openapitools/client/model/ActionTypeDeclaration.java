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
import org.openapitools.client.model.ActionTypeDeclarationExecutor;
import org.openapitools.client.model.ActionTypeDeclarationId;
import org.openapitools.client.model.ActionTypeDeclarationInputArtifactDetails;
import org.openapitools.client.model.ActionTypeDeclarationOutputArtifactDetails;
import org.openapitools.client.model.ActionTypeDeclarationPermissions;
import org.openapitools.client.model.ActionTypeDeclarationUrls;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * The parameters for the action type definition that are provided when the action type is created or updated.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:02:26.715942-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ActionTypeDeclaration {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXECUTOR = "executor";
  @SerializedName(SERIALIZED_NAME_EXECUTOR)
  private ActionTypeDeclarationExecutor executor;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private ActionTypeDeclarationId id;

  public static final String SERIALIZED_NAME_INPUT_ARTIFACT_DETAILS = "inputArtifactDetails";
  @SerializedName(SERIALIZED_NAME_INPUT_ARTIFACT_DETAILS)
  private ActionTypeDeclarationInputArtifactDetails inputArtifactDetails;

  public static final String SERIALIZED_NAME_OUTPUT_ARTIFACT_DETAILS = "outputArtifactDetails";
  @SerializedName(SERIALIZED_NAME_OUTPUT_ARTIFACT_DETAILS)
  private ActionTypeDeclarationOutputArtifactDetails outputArtifactDetails;

  public static final String SERIALIZED_NAME_PERMISSIONS = "permissions";
  @SerializedName(SERIALIZED_NAME_PERMISSIONS)
  private ActionTypeDeclarationPermissions permissions;

  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private Object properties = null;

  public static final String SERIALIZED_NAME_URLS = "urls";
  @SerializedName(SERIALIZED_NAME_URLS)
  private ActionTypeDeclarationUrls urls;

  public ActionTypeDeclaration() {
  }

  public ActionTypeDeclaration description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ActionTypeDeclaration executor(ActionTypeDeclarationExecutor executor) {
    this.executor = executor;
    return this;
  }

  /**
   * Get executor
   * @return executor
   */
  @javax.annotation.Nonnull
  public ActionTypeDeclarationExecutor getExecutor() {
    return executor;
  }

  public void setExecutor(ActionTypeDeclarationExecutor executor) {
    this.executor = executor;
  }


  public ActionTypeDeclaration id(ActionTypeDeclarationId id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public ActionTypeDeclarationId getId() {
    return id;
  }

  public void setId(ActionTypeDeclarationId id) {
    this.id = id;
  }


  public ActionTypeDeclaration inputArtifactDetails(ActionTypeDeclarationInputArtifactDetails inputArtifactDetails) {
    this.inputArtifactDetails = inputArtifactDetails;
    return this;
  }

  /**
   * Get inputArtifactDetails
   * @return inputArtifactDetails
   */
  @javax.annotation.Nonnull
  public ActionTypeDeclarationInputArtifactDetails getInputArtifactDetails() {
    return inputArtifactDetails;
  }

  public void setInputArtifactDetails(ActionTypeDeclarationInputArtifactDetails inputArtifactDetails) {
    this.inputArtifactDetails = inputArtifactDetails;
  }


  public ActionTypeDeclaration outputArtifactDetails(ActionTypeDeclarationOutputArtifactDetails outputArtifactDetails) {
    this.outputArtifactDetails = outputArtifactDetails;
    return this;
  }

  /**
   * Get outputArtifactDetails
   * @return outputArtifactDetails
   */
  @javax.annotation.Nonnull
  public ActionTypeDeclarationOutputArtifactDetails getOutputArtifactDetails() {
    return outputArtifactDetails;
  }

  public void setOutputArtifactDetails(ActionTypeDeclarationOutputArtifactDetails outputArtifactDetails) {
    this.outputArtifactDetails = outputArtifactDetails;
  }


  public ActionTypeDeclaration permissions(ActionTypeDeclarationPermissions permissions) {
    this.permissions = permissions;
    return this;
  }

  /**
   * Get permissions
   * @return permissions
   */
  @javax.annotation.Nullable
  public ActionTypeDeclarationPermissions getPermissions() {
    return permissions;
  }

  public void setPermissions(ActionTypeDeclarationPermissions permissions) {
    this.permissions = permissions;
  }


  public ActionTypeDeclaration properties(Object properties) {
    this.properties = properties;
    return this;
  }

  /**
   * The properties of the action type to be updated.
   * @return properties
   */
  @javax.annotation.Nullable
  public Object getProperties() {
    return properties;
  }

  public void setProperties(Object properties) {
    this.properties = properties;
  }


  public ActionTypeDeclaration urls(ActionTypeDeclarationUrls urls) {
    this.urls = urls;
    return this;
  }

  /**
   * Get urls
   * @return urls
   */
  @javax.annotation.Nullable
  public ActionTypeDeclarationUrls getUrls() {
    return urls;
  }

  public void setUrls(ActionTypeDeclarationUrls urls) {
    this.urls = urls;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ActionTypeDeclaration actionTypeDeclaration = (ActionTypeDeclaration) o;
    return Objects.equals(this.description, actionTypeDeclaration.description) &&
        Objects.equals(this.executor, actionTypeDeclaration.executor) &&
        Objects.equals(this.id, actionTypeDeclaration.id) &&
        Objects.equals(this.inputArtifactDetails, actionTypeDeclaration.inputArtifactDetails) &&
        Objects.equals(this.outputArtifactDetails, actionTypeDeclaration.outputArtifactDetails) &&
        Objects.equals(this.permissions, actionTypeDeclaration.permissions) &&
        Objects.equals(this.properties, actionTypeDeclaration.properties) &&
        Objects.equals(this.urls, actionTypeDeclaration.urls);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, executor, id, inputArtifactDetails, outputArtifactDetails, permissions, properties, urls);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ActionTypeDeclaration {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    executor: ").append(toIndentedString(executor)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    inputArtifactDetails: ").append(toIndentedString(inputArtifactDetails)).append("\n");
    sb.append("    outputArtifactDetails: ").append(toIndentedString(outputArtifactDetails)).append("\n");
    sb.append("    permissions: ").append(toIndentedString(permissions)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
    sb.append("    urls: ").append(toIndentedString(urls)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("executor");
    openapiFields.add("id");
    openapiFields.add("inputArtifactDetails");
    openapiFields.add("outputArtifactDetails");
    openapiFields.add("permissions");
    openapiFields.add("properties");
    openapiFields.add("urls");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("executor");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("inputArtifactDetails");
    openapiRequiredFields.add("outputArtifactDetails");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ActionTypeDeclaration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ActionTypeDeclaration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ActionTypeDeclaration is not found in the empty JSON string", ActionTypeDeclaration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ActionTypeDeclaration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ActionTypeDeclaration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ActionTypeDeclaration.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `description`
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("description"));
      }
      // validate the required field `executor`
      ActionTypeDeclarationExecutor.validateJsonElement(jsonObj.get("executor"));
      // validate the required field `id`
      ActionTypeDeclarationId.validateJsonElement(jsonObj.get("id"));
      // validate the required field `inputArtifactDetails`
      ActionTypeDeclarationInputArtifactDetails.validateJsonElement(jsonObj.get("inputArtifactDetails"));
      // validate the required field `outputArtifactDetails`
      ActionTypeDeclarationOutputArtifactDetails.validateJsonElement(jsonObj.get("outputArtifactDetails"));
      // validate the optional field `permissions`
      if (jsonObj.get("permissions") != null && !jsonObj.get("permissions").isJsonNull()) {
        ActionTypeDeclarationPermissions.validateJsonElement(jsonObj.get("permissions"));
      }
      // validate the optional field `urls`
      if (jsonObj.get("urls") != null && !jsonObj.get("urls").isJsonNull()) {
        ActionTypeDeclarationUrls.validateJsonElement(jsonObj.get("urls"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ActionTypeDeclaration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ActionTypeDeclaration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ActionTypeDeclaration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ActionTypeDeclaration.class));

       return (TypeAdapter<T>) new TypeAdapter<ActionTypeDeclaration>() {
           @Override
           public void write(JsonWriter out, ActionTypeDeclaration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ActionTypeDeclaration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ActionTypeDeclaration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ActionTypeDeclaration
   * @throws IOException if the JSON string is invalid with respect to ActionTypeDeclaration
   */
  public static ActionTypeDeclaration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ActionTypeDeclaration.class);
  }

  /**
   * Convert an instance of ActionTypeDeclaration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

