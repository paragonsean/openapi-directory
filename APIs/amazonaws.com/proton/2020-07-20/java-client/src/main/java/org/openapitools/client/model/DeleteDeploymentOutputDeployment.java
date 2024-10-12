/*
 * AWS Proton
 * <p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-20
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
import org.openapitools.client.model.DeploymentInitialState;
import org.openapitools.client.model.DeploymentStatus;
import org.openapitools.client.model.DeploymentTargetResourceType;
import org.openapitools.client.model.DeploymentTargetState;

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
 * DeleteDeploymentOutputDeployment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeleteDeploymentOutputDeployment {
  public static final String SERIALIZED_NAME_ARN = "arn";
  @SerializedName(SERIALIZED_NAME_ARN)
  private String arn;

  public static final String SERIALIZED_NAME_COMPLETED_AT = "completedAt";
  @SerializedName(SERIALIZED_NAME_COMPLETED_AT)
  private OffsetDateTime completedAt;

  public static final String SERIALIZED_NAME_COMPONENT_NAME = "componentName";
  @SerializedName(SERIALIZED_NAME_COMPONENT_NAME)
  private String componentName;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DEPLOYMENT_STATUS = "deploymentStatus";
  @SerializedName(SERIALIZED_NAME_DEPLOYMENT_STATUS)
  private DeploymentStatus deploymentStatus;

  public static final String SERIALIZED_NAME_DEPLOYMENT_STATUS_MESSAGE = "deploymentStatusMessage";
  @SerializedName(SERIALIZED_NAME_DEPLOYMENT_STATUS_MESSAGE)
  private String deploymentStatusMessage;

  public static final String SERIALIZED_NAME_ENVIRONMENT_NAME = "environmentName";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_NAME)
  private String environmentName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_INITIAL_STATE = "initialState";
  @SerializedName(SERIALIZED_NAME_INITIAL_STATE)
  private DeploymentInitialState initialState;

  public static final String SERIALIZED_NAME_LAST_ATTEMPTED_DEPLOYMENT_ID = "lastAttemptedDeploymentId";
  @SerializedName(SERIALIZED_NAME_LAST_ATTEMPTED_DEPLOYMENT_ID)
  private String lastAttemptedDeploymentId;

  public static final String SERIALIZED_NAME_LAST_MODIFIED_AT = "lastModifiedAt";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED_AT)
  private OffsetDateTime lastModifiedAt;

  public static final String SERIALIZED_NAME_LAST_SUCCEEDED_DEPLOYMENT_ID = "lastSucceededDeploymentId";
  @SerializedName(SERIALIZED_NAME_LAST_SUCCEEDED_DEPLOYMENT_ID)
  private String lastSucceededDeploymentId;

  public static final String SERIALIZED_NAME_SERVICE_INSTANCE_NAME = "serviceInstanceName";
  @SerializedName(SERIALIZED_NAME_SERVICE_INSTANCE_NAME)
  private String serviceInstanceName;

  public static final String SERIALIZED_NAME_SERVICE_NAME = "serviceName";
  @SerializedName(SERIALIZED_NAME_SERVICE_NAME)
  private String serviceName;

  public static final String SERIALIZED_NAME_TARGET_ARN = "targetArn";
  @SerializedName(SERIALIZED_NAME_TARGET_ARN)
  private String targetArn;

  public static final String SERIALIZED_NAME_TARGET_RESOURCE_CREATED_AT = "targetResourceCreatedAt";
  @SerializedName(SERIALIZED_NAME_TARGET_RESOURCE_CREATED_AT)
  private OffsetDateTime targetResourceCreatedAt;

  public static final String SERIALIZED_NAME_TARGET_RESOURCE_TYPE = "targetResourceType";
  @SerializedName(SERIALIZED_NAME_TARGET_RESOURCE_TYPE)
  private DeploymentTargetResourceType targetResourceType;

  public static final String SERIALIZED_NAME_TARGET_STATE = "targetState";
  @SerializedName(SERIALIZED_NAME_TARGET_STATE)
  private DeploymentTargetState targetState;

  public DeleteDeploymentOutputDeployment() {
  }

  public DeleteDeploymentOutputDeployment arn(String arn) {
    this.arn = arn;
    return this;
  }

  /**
   * Get arn
   * @return arn
   */
  @javax.annotation.Nonnull
  public String getArn() {
    return arn;
  }

  public void setArn(String arn) {
    this.arn = arn;
  }


  public DeleteDeploymentOutputDeployment completedAt(OffsetDateTime completedAt) {
    this.completedAt = completedAt;
    return this;
  }

  /**
   * Get completedAt
   * @return completedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCompletedAt() {
    return completedAt;
  }

  public void setCompletedAt(OffsetDateTime completedAt) {
    this.completedAt = completedAt;
  }


  public DeleteDeploymentOutputDeployment componentName(String componentName) {
    this.componentName = componentName;
    return this;
  }

  /**
   * Get componentName
   * @return componentName
   */
  @javax.annotation.Nullable
  public String getComponentName() {
    return componentName;
  }

  public void setComponentName(String componentName) {
    this.componentName = componentName;
  }


  public DeleteDeploymentOutputDeployment createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public DeleteDeploymentOutputDeployment deploymentStatus(DeploymentStatus deploymentStatus) {
    this.deploymentStatus = deploymentStatus;
    return this;
  }

  /**
   * Get deploymentStatus
   * @return deploymentStatus
   */
  @javax.annotation.Nonnull
  public DeploymentStatus getDeploymentStatus() {
    return deploymentStatus;
  }

  public void setDeploymentStatus(DeploymentStatus deploymentStatus) {
    this.deploymentStatus = deploymentStatus;
  }


  public DeleteDeploymentOutputDeployment deploymentStatusMessage(String deploymentStatusMessage) {
    this.deploymentStatusMessage = deploymentStatusMessage;
    return this;
  }

  /**
   * Get deploymentStatusMessage
   * @return deploymentStatusMessage
   */
  @javax.annotation.Nullable
  public String getDeploymentStatusMessage() {
    return deploymentStatusMessage;
  }

  public void setDeploymentStatusMessage(String deploymentStatusMessage) {
    this.deploymentStatusMessage = deploymentStatusMessage;
  }


  public DeleteDeploymentOutputDeployment environmentName(String environmentName) {
    this.environmentName = environmentName;
    return this;
  }

  /**
   * Get environmentName
   * @return environmentName
   */
  @javax.annotation.Nonnull
  public String getEnvironmentName() {
    return environmentName;
  }

  public void setEnvironmentName(String environmentName) {
    this.environmentName = environmentName;
  }


  public DeleteDeploymentOutputDeployment id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public DeleteDeploymentOutputDeployment initialState(DeploymentInitialState initialState) {
    this.initialState = initialState;
    return this;
  }

  /**
   * Get initialState
   * @return initialState
   */
  @javax.annotation.Nullable
  public DeploymentInitialState getInitialState() {
    return initialState;
  }

  public void setInitialState(DeploymentInitialState initialState) {
    this.initialState = initialState;
  }


  public DeleteDeploymentOutputDeployment lastAttemptedDeploymentId(String lastAttemptedDeploymentId) {
    this.lastAttemptedDeploymentId = lastAttemptedDeploymentId;
    return this;
  }

  /**
   * Get lastAttemptedDeploymentId
   * @return lastAttemptedDeploymentId
   */
  @javax.annotation.Nullable
  public String getLastAttemptedDeploymentId() {
    return lastAttemptedDeploymentId;
  }

  public void setLastAttemptedDeploymentId(String lastAttemptedDeploymentId) {
    this.lastAttemptedDeploymentId = lastAttemptedDeploymentId;
  }


  public DeleteDeploymentOutputDeployment lastModifiedAt(OffsetDateTime lastModifiedAt) {
    this.lastModifiedAt = lastModifiedAt;
    return this;
  }

  /**
   * Get lastModifiedAt
   * @return lastModifiedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getLastModifiedAt() {
    return lastModifiedAt;
  }

  public void setLastModifiedAt(OffsetDateTime lastModifiedAt) {
    this.lastModifiedAt = lastModifiedAt;
  }


  public DeleteDeploymentOutputDeployment lastSucceededDeploymentId(String lastSucceededDeploymentId) {
    this.lastSucceededDeploymentId = lastSucceededDeploymentId;
    return this;
  }

  /**
   * Get lastSucceededDeploymentId
   * @return lastSucceededDeploymentId
   */
  @javax.annotation.Nullable
  public String getLastSucceededDeploymentId() {
    return lastSucceededDeploymentId;
  }

  public void setLastSucceededDeploymentId(String lastSucceededDeploymentId) {
    this.lastSucceededDeploymentId = lastSucceededDeploymentId;
  }


  public DeleteDeploymentOutputDeployment serviceInstanceName(String serviceInstanceName) {
    this.serviceInstanceName = serviceInstanceName;
    return this;
  }

  /**
   * Get serviceInstanceName
   * @return serviceInstanceName
   */
  @javax.annotation.Nullable
  public String getServiceInstanceName() {
    return serviceInstanceName;
  }

  public void setServiceInstanceName(String serviceInstanceName) {
    this.serviceInstanceName = serviceInstanceName;
  }


  public DeleteDeploymentOutputDeployment serviceName(String serviceName) {
    this.serviceName = serviceName;
    return this;
  }

  /**
   * Get serviceName
   * @return serviceName
   */
  @javax.annotation.Nullable
  public String getServiceName() {
    return serviceName;
  }

  public void setServiceName(String serviceName) {
    this.serviceName = serviceName;
  }


  public DeleteDeploymentOutputDeployment targetArn(String targetArn) {
    this.targetArn = targetArn;
    return this;
  }

  /**
   * Get targetArn
   * @return targetArn
   */
  @javax.annotation.Nonnull
  public String getTargetArn() {
    return targetArn;
  }

  public void setTargetArn(String targetArn) {
    this.targetArn = targetArn;
  }


  public DeleteDeploymentOutputDeployment targetResourceCreatedAt(OffsetDateTime targetResourceCreatedAt) {
    this.targetResourceCreatedAt = targetResourceCreatedAt;
    return this;
  }

  /**
   * Get targetResourceCreatedAt
   * @return targetResourceCreatedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getTargetResourceCreatedAt() {
    return targetResourceCreatedAt;
  }

  public void setTargetResourceCreatedAt(OffsetDateTime targetResourceCreatedAt) {
    this.targetResourceCreatedAt = targetResourceCreatedAt;
  }


  public DeleteDeploymentOutputDeployment targetResourceType(DeploymentTargetResourceType targetResourceType) {
    this.targetResourceType = targetResourceType;
    return this;
  }

  /**
   * Get targetResourceType
   * @return targetResourceType
   */
  @javax.annotation.Nonnull
  public DeploymentTargetResourceType getTargetResourceType() {
    return targetResourceType;
  }

  public void setTargetResourceType(DeploymentTargetResourceType targetResourceType) {
    this.targetResourceType = targetResourceType;
  }


  public DeleteDeploymentOutputDeployment targetState(DeploymentTargetState targetState) {
    this.targetState = targetState;
    return this;
  }

  /**
   * Get targetState
   * @return targetState
   */
  @javax.annotation.Nullable
  public DeploymentTargetState getTargetState() {
    return targetState;
  }

  public void setTargetState(DeploymentTargetState targetState) {
    this.targetState = targetState;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeleteDeploymentOutputDeployment deleteDeploymentOutputDeployment = (DeleteDeploymentOutputDeployment) o;
    return Objects.equals(this.arn, deleteDeploymentOutputDeployment.arn) &&
        Objects.equals(this.completedAt, deleteDeploymentOutputDeployment.completedAt) &&
        Objects.equals(this.componentName, deleteDeploymentOutputDeployment.componentName) &&
        Objects.equals(this.createdAt, deleteDeploymentOutputDeployment.createdAt) &&
        Objects.equals(this.deploymentStatus, deleteDeploymentOutputDeployment.deploymentStatus) &&
        Objects.equals(this.deploymentStatusMessage, deleteDeploymentOutputDeployment.deploymentStatusMessage) &&
        Objects.equals(this.environmentName, deleteDeploymentOutputDeployment.environmentName) &&
        Objects.equals(this.id, deleteDeploymentOutputDeployment.id) &&
        Objects.equals(this.initialState, deleteDeploymentOutputDeployment.initialState) &&
        Objects.equals(this.lastAttemptedDeploymentId, deleteDeploymentOutputDeployment.lastAttemptedDeploymentId) &&
        Objects.equals(this.lastModifiedAt, deleteDeploymentOutputDeployment.lastModifiedAt) &&
        Objects.equals(this.lastSucceededDeploymentId, deleteDeploymentOutputDeployment.lastSucceededDeploymentId) &&
        Objects.equals(this.serviceInstanceName, deleteDeploymentOutputDeployment.serviceInstanceName) &&
        Objects.equals(this.serviceName, deleteDeploymentOutputDeployment.serviceName) &&
        Objects.equals(this.targetArn, deleteDeploymentOutputDeployment.targetArn) &&
        Objects.equals(this.targetResourceCreatedAt, deleteDeploymentOutputDeployment.targetResourceCreatedAt) &&
        Objects.equals(this.targetResourceType, deleteDeploymentOutputDeployment.targetResourceType) &&
        Objects.equals(this.targetState, deleteDeploymentOutputDeployment.targetState);
  }

  @Override
  public int hashCode() {
    return Objects.hash(arn, completedAt, componentName, createdAt, deploymentStatus, deploymentStatusMessage, environmentName, id, initialState, lastAttemptedDeploymentId, lastModifiedAt, lastSucceededDeploymentId, serviceInstanceName, serviceName, targetArn, targetResourceCreatedAt, targetResourceType, targetState);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeleteDeploymentOutputDeployment {\n");
    sb.append("    arn: ").append(toIndentedString(arn)).append("\n");
    sb.append("    completedAt: ").append(toIndentedString(completedAt)).append("\n");
    sb.append("    componentName: ").append(toIndentedString(componentName)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    deploymentStatus: ").append(toIndentedString(deploymentStatus)).append("\n");
    sb.append("    deploymentStatusMessage: ").append(toIndentedString(deploymentStatusMessage)).append("\n");
    sb.append("    environmentName: ").append(toIndentedString(environmentName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    initialState: ").append(toIndentedString(initialState)).append("\n");
    sb.append("    lastAttemptedDeploymentId: ").append(toIndentedString(lastAttemptedDeploymentId)).append("\n");
    sb.append("    lastModifiedAt: ").append(toIndentedString(lastModifiedAt)).append("\n");
    sb.append("    lastSucceededDeploymentId: ").append(toIndentedString(lastSucceededDeploymentId)).append("\n");
    sb.append("    serviceInstanceName: ").append(toIndentedString(serviceInstanceName)).append("\n");
    sb.append("    serviceName: ").append(toIndentedString(serviceName)).append("\n");
    sb.append("    targetArn: ").append(toIndentedString(targetArn)).append("\n");
    sb.append("    targetResourceCreatedAt: ").append(toIndentedString(targetResourceCreatedAt)).append("\n");
    sb.append("    targetResourceType: ").append(toIndentedString(targetResourceType)).append("\n");
    sb.append("    targetState: ").append(toIndentedString(targetState)).append("\n");
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
    openapiFields.add("arn");
    openapiFields.add("completedAt");
    openapiFields.add("componentName");
    openapiFields.add("createdAt");
    openapiFields.add("deploymentStatus");
    openapiFields.add("deploymentStatusMessage");
    openapiFields.add("environmentName");
    openapiFields.add("id");
    openapiFields.add("initialState");
    openapiFields.add("lastAttemptedDeploymentId");
    openapiFields.add("lastModifiedAt");
    openapiFields.add("lastSucceededDeploymentId");
    openapiFields.add("serviceInstanceName");
    openapiFields.add("serviceName");
    openapiFields.add("targetArn");
    openapiFields.add("targetResourceCreatedAt");
    openapiFields.add("targetResourceType");
    openapiFields.add("targetState");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("arn");
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("deploymentStatus");
    openapiRequiredFields.add("environmentName");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("lastModifiedAt");
    openapiRequiredFields.add("targetArn");
    openapiRequiredFields.add("targetResourceCreatedAt");
    openapiRequiredFields.add("targetResourceType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeleteDeploymentOutputDeployment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeleteDeploymentOutputDeployment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeleteDeploymentOutputDeployment is not found in the empty JSON string", DeleteDeploymentOutputDeployment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeleteDeploymentOutputDeployment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeleteDeploymentOutputDeployment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DeleteDeploymentOutputDeployment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `arn`
      String.validateJsonElement(jsonObj.get("arn"));
      // validate the optional field `completedAt`
      if (jsonObj.get("completedAt") != null && !jsonObj.get("completedAt").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("completedAt"));
      }
      // validate the optional field `componentName`
      if (jsonObj.get("componentName") != null && !jsonObj.get("componentName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("componentName"));
      }
      // validate the required field `createdAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("createdAt"));
      // validate the required field `deploymentStatus`
      DeploymentStatus.validateJsonElement(jsonObj.get("deploymentStatus"));
      // validate the optional field `deploymentStatusMessage`
      if (jsonObj.get("deploymentStatusMessage") != null && !jsonObj.get("deploymentStatusMessage").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("deploymentStatusMessage"));
      }
      // validate the required field `environmentName`
      String.validateJsonElement(jsonObj.get("environmentName"));
      // validate the required field `id`
      String.validateJsonElement(jsonObj.get("id"));
      // validate the optional field `initialState`
      if (jsonObj.get("initialState") != null && !jsonObj.get("initialState").isJsonNull()) {
        DeploymentInitialState.validateJsonElement(jsonObj.get("initialState"));
      }
      // validate the optional field `lastAttemptedDeploymentId`
      if (jsonObj.get("lastAttemptedDeploymentId") != null && !jsonObj.get("lastAttemptedDeploymentId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("lastAttemptedDeploymentId"));
      }
      // validate the required field `lastModifiedAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("lastModifiedAt"));
      // validate the optional field `lastSucceededDeploymentId`
      if (jsonObj.get("lastSucceededDeploymentId") != null && !jsonObj.get("lastSucceededDeploymentId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("lastSucceededDeploymentId"));
      }
      // validate the optional field `serviceInstanceName`
      if (jsonObj.get("serviceInstanceName") != null && !jsonObj.get("serviceInstanceName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("serviceInstanceName"));
      }
      // validate the optional field `serviceName`
      if (jsonObj.get("serviceName") != null && !jsonObj.get("serviceName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("serviceName"));
      }
      // validate the required field `targetArn`
      String.validateJsonElement(jsonObj.get("targetArn"));
      // validate the required field `targetResourceCreatedAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("targetResourceCreatedAt"));
      // validate the required field `targetResourceType`
      DeploymentTargetResourceType.validateJsonElement(jsonObj.get("targetResourceType"));
      // validate the optional field `targetState`
      if (jsonObj.get("targetState") != null && !jsonObj.get("targetState").isJsonNull()) {
        DeploymentTargetState.validateJsonElement(jsonObj.get("targetState"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeleteDeploymentOutputDeployment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeleteDeploymentOutputDeployment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeleteDeploymentOutputDeployment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeleteDeploymentOutputDeployment.class));

       return (TypeAdapter<T>) new TypeAdapter<DeleteDeploymentOutputDeployment>() {
           @Override
           public void write(JsonWriter out, DeleteDeploymentOutputDeployment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeleteDeploymentOutputDeployment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeleteDeploymentOutputDeployment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeleteDeploymentOutputDeployment
   * @throws IOException if the JSON string is invalid with respect to DeleteDeploymentOutputDeployment
   */
  public static DeleteDeploymentOutputDeployment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeleteDeploymentOutputDeployment.class);
  }

  /**
   * Convert an instance of DeleteDeploymentOutputDeployment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

