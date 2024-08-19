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
import org.openapitools.client.model.DeploymentStatus;
import org.openapitools.client.model.Provisioning;

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
 * Summary data of an Proton environment resource. An Proton environment is a set of resources shared across Proton services.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EnvironmentSummary {
  public static final String SERIALIZED_NAME_ARN = "arn";
  @SerializedName(SERIALIZED_NAME_ARN)
  private String arn;

  public static final String SERIALIZED_NAME_COMPONENT_ROLE_ARN = "componentRoleArn";
  @SerializedName(SERIALIZED_NAME_COMPONENT_ROLE_ARN)
  private String componentRoleArn;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DEPLOYMENT_STATUS = "deploymentStatus";
  @SerializedName(SERIALIZED_NAME_DEPLOYMENT_STATUS)
  private DeploymentStatus deploymentStatus;

  public static final String SERIALIZED_NAME_DEPLOYMENT_STATUS_MESSAGE = "deploymentStatusMessage";
  @SerializedName(SERIALIZED_NAME_DEPLOYMENT_STATUS_MESSAGE)
  private String deploymentStatusMessage;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_CONNECTION_ID = "environmentAccountConnectionId";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_CONNECTION_ID)
  private String environmentAccountConnectionId;

  public static final String SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_ID = "environmentAccountId";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_ID)
  private String environmentAccountId;

  public static final String SERIALIZED_NAME_LAST_ATTEMPTED_DEPLOYMENT_ID = "lastAttemptedDeploymentId";
  @SerializedName(SERIALIZED_NAME_LAST_ATTEMPTED_DEPLOYMENT_ID)
  private String lastAttemptedDeploymentId;

  public static final String SERIALIZED_NAME_LAST_DEPLOYMENT_ATTEMPTED_AT = "lastDeploymentAttemptedAt";
  @SerializedName(SERIALIZED_NAME_LAST_DEPLOYMENT_ATTEMPTED_AT)
  private OffsetDateTime lastDeploymentAttemptedAt;

  public static final String SERIALIZED_NAME_LAST_DEPLOYMENT_SUCCEEDED_AT = "lastDeploymentSucceededAt";
  @SerializedName(SERIALIZED_NAME_LAST_DEPLOYMENT_SUCCEEDED_AT)
  private OffsetDateTime lastDeploymentSucceededAt;

  public static final String SERIALIZED_NAME_LAST_SUCCEEDED_DEPLOYMENT_ID = "lastSucceededDeploymentId";
  @SerializedName(SERIALIZED_NAME_LAST_SUCCEEDED_DEPLOYMENT_ID)
  private String lastSucceededDeploymentId;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROTON_SERVICE_ROLE_ARN = "protonServiceRoleArn";
  @SerializedName(SERIALIZED_NAME_PROTON_SERVICE_ROLE_ARN)
  private String protonServiceRoleArn;

  public static final String SERIALIZED_NAME_PROVISIONING = "provisioning";
  @SerializedName(SERIALIZED_NAME_PROVISIONING)
  private Provisioning provisioning;

  public static final String SERIALIZED_NAME_TEMPLATE_MAJOR_VERSION = "templateMajorVersion";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_MAJOR_VERSION)
  private String templateMajorVersion;

  public static final String SERIALIZED_NAME_TEMPLATE_MINOR_VERSION = "templateMinorVersion";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_MINOR_VERSION)
  private String templateMinorVersion;

  public static final String SERIALIZED_NAME_TEMPLATE_NAME = "templateName";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_NAME)
  private String templateName;

  public EnvironmentSummary() {
  }

  public EnvironmentSummary arn(String arn) {
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


  public EnvironmentSummary componentRoleArn(String componentRoleArn) {
    this.componentRoleArn = componentRoleArn;
    return this;
  }

  /**
   * Get componentRoleArn
   * @return componentRoleArn
   */
  @javax.annotation.Nullable
  public String getComponentRoleArn() {
    return componentRoleArn;
  }

  public void setComponentRoleArn(String componentRoleArn) {
    this.componentRoleArn = componentRoleArn;
  }


  public EnvironmentSummary createdAt(OffsetDateTime createdAt) {
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


  public EnvironmentSummary deploymentStatus(DeploymentStatus deploymentStatus) {
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


  public EnvironmentSummary deploymentStatusMessage(String deploymentStatusMessage) {
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


  public EnvironmentSummary description(String description) {
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


  public EnvironmentSummary environmentAccountConnectionId(String environmentAccountConnectionId) {
    this.environmentAccountConnectionId = environmentAccountConnectionId;
    return this;
  }

  /**
   * Get environmentAccountConnectionId
   * @return environmentAccountConnectionId
   */
  @javax.annotation.Nullable
  public String getEnvironmentAccountConnectionId() {
    return environmentAccountConnectionId;
  }

  public void setEnvironmentAccountConnectionId(String environmentAccountConnectionId) {
    this.environmentAccountConnectionId = environmentAccountConnectionId;
  }


  public EnvironmentSummary environmentAccountId(String environmentAccountId) {
    this.environmentAccountId = environmentAccountId;
    return this;
  }

  /**
   * Get environmentAccountId
   * @return environmentAccountId
   */
  @javax.annotation.Nullable
  public String getEnvironmentAccountId() {
    return environmentAccountId;
  }

  public void setEnvironmentAccountId(String environmentAccountId) {
    this.environmentAccountId = environmentAccountId;
  }


  public EnvironmentSummary lastAttemptedDeploymentId(String lastAttemptedDeploymentId) {
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


  public EnvironmentSummary lastDeploymentAttemptedAt(OffsetDateTime lastDeploymentAttemptedAt) {
    this.lastDeploymentAttemptedAt = lastDeploymentAttemptedAt;
    return this;
  }

  /**
   * Get lastDeploymentAttemptedAt
   * @return lastDeploymentAttemptedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getLastDeploymentAttemptedAt() {
    return lastDeploymentAttemptedAt;
  }

  public void setLastDeploymentAttemptedAt(OffsetDateTime lastDeploymentAttemptedAt) {
    this.lastDeploymentAttemptedAt = lastDeploymentAttemptedAt;
  }


  public EnvironmentSummary lastDeploymentSucceededAt(OffsetDateTime lastDeploymentSucceededAt) {
    this.lastDeploymentSucceededAt = lastDeploymentSucceededAt;
    return this;
  }

  /**
   * Get lastDeploymentSucceededAt
   * @return lastDeploymentSucceededAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getLastDeploymentSucceededAt() {
    return lastDeploymentSucceededAt;
  }

  public void setLastDeploymentSucceededAt(OffsetDateTime lastDeploymentSucceededAt) {
    this.lastDeploymentSucceededAt = lastDeploymentSucceededAt;
  }


  public EnvironmentSummary lastSucceededDeploymentId(String lastSucceededDeploymentId) {
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


  public EnvironmentSummary name(String name) {
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


  public EnvironmentSummary protonServiceRoleArn(String protonServiceRoleArn) {
    this.protonServiceRoleArn = protonServiceRoleArn;
    return this;
  }

  /**
   * Get protonServiceRoleArn
   * @return protonServiceRoleArn
   */
  @javax.annotation.Nullable
  public String getProtonServiceRoleArn() {
    return protonServiceRoleArn;
  }

  public void setProtonServiceRoleArn(String protonServiceRoleArn) {
    this.protonServiceRoleArn = protonServiceRoleArn;
  }


  public EnvironmentSummary provisioning(Provisioning provisioning) {
    this.provisioning = provisioning;
    return this;
  }

  /**
   * Get provisioning
   * @return provisioning
   */
  @javax.annotation.Nullable
  public Provisioning getProvisioning() {
    return provisioning;
  }

  public void setProvisioning(Provisioning provisioning) {
    this.provisioning = provisioning;
  }


  public EnvironmentSummary templateMajorVersion(String templateMajorVersion) {
    this.templateMajorVersion = templateMajorVersion;
    return this;
  }

  /**
   * Get templateMajorVersion
   * @return templateMajorVersion
   */
  @javax.annotation.Nonnull
  public String getTemplateMajorVersion() {
    return templateMajorVersion;
  }

  public void setTemplateMajorVersion(String templateMajorVersion) {
    this.templateMajorVersion = templateMajorVersion;
  }


  public EnvironmentSummary templateMinorVersion(String templateMinorVersion) {
    this.templateMinorVersion = templateMinorVersion;
    return this;
  }

  /**
   * Get templateMinorVersion
   * @return templateMinorVersion
   */
  @javax.annotation.Nonnull
  public String getTemplateMinorVersion() {
    return templateMinorVersion;
  }

  public void setTemplateMinorVersion(String templateMinorVersion) {
    this.templateMinorVersion = templateMinorVersion;
  }


  public EnvironmentSummary templateName(String templateName) {
    this.templateName = templateName;
    return this;
  }

  /**
   * Get templateName
   * @return templateName
   */
  @javax.annotation.Nonnull
  public String getTemplateName() {
    return templateName;
  }

  public void setTemplateName(String templateName) {
    this.templateName = templateName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EnvironmentSummary environmentSummary = (EnvironmentSummary) o;
    return Objects.equals(this.arn, environmentSummary.arn) &&
        Objects.equals(this.componentRoleArn, environmentSummary.componentRoleArn) &&
        Objects.equals(this.createdAt, environmentSummary.createdAt) &&
        Objects.equals(this.deploymentStatus, environmentSummary.deploymentStatus) &&
        Objects.equals(this.deploymentStatusMessage, environmentSummary.deploymentStatusMessage) &&
        Objects.equals(this.description, environmentSummary.description) &&
        Objects.equals(this.environmentAccountConnectionId, environmentSummary.environmentAccountConnectionId) &&
        Objects.equals(this.environmentAccountId, environmentSummary.environmentAccountId) &&
        Objects.equals(this.lastAttemptedDeploymentId, environmentSummary.lastAttemptedDeploymentId) &&
        Objects.equals(this.lastDeploymentAttemptedAt, environmentSummary.lastDeploymentAttemptedAt) &&
        Objects.equals(this.lastDeploymentSucceededAt, environmentSummary.lastDeploymentSucceededAt) &&
        Objects.equals(this.lastSucceededDeploymentId, environmentSummary.lastSucceededDeploymentId) &&
        Objects.equals(this.name, environmentSummary.name) &&
        Objects.equals(this.protonServiceRoleArn, environmentSummary.protonServiceRoleArn) &&
        Objects.equals(this.provisioning, environmentSummary.provisioning) &&
        Objects.equals(this.templateMajorVersion, environmentSummary.templateMajorVersion) &&
        Objects.equals(this.templateMinorVersion, environmentSummary.templateMinorVersion) &&
        Objects.equals(this.templateName, environmentSummary.templateName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(arn, componentRoleArn, createdAt, deploymentStatus, deploymentStatusMessage, description, environmentAccountConnectionId, environmentAccountId, lastAttemptedDeploymentId, lastDeploymentAttemptedAt, lastDeploymentSucceededAt, lastSucceededDeploymentId, name, protonServiceRoleArn, provisioning, templateMajorVersion, templateMinorVersion, templateName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EnvironmentSummary {\n");
    sb.append("    arn: ").append(toIndentedString(arn)).append("\n");
    sb.append("    componentRoleArn: ").append(toIndentedString(componentRoleArn)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    deploymentStatus: ").append(toIndentedString(deploymentStatus)).append("\n");
    sb.append("    deploymentStatusMessage: ").append(toIndentedString(deploymentStatusMessage)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    environmentAccountConnectionId: ").append(toIndentedString(environmentAccountConnectionId)).append("\n");
    sb.append("    environmentAccountId: ").append(toIndentedString(environmentAccountId)).append("\n");
    sb.append("    lastAttemptedDeploymentId: ").append(toIndentedString(lastAttemptedDeploymentId)).append("\n");
    sb.append("    lastDeploymentAttemptedAt: ").append(toIndentedString(lastDeploymentAttemptedAt)).append("\n");
    sb.append("    lastDeploymentSucceededAt: ").append(toIndentedString(lastDeploymentSucceededAt)).append("\n");
    sb.append("    lastSucceededDeploymentId: ").append(toIndentedString(lastSucceededDeploymentId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    protonServiceRoleArn: ").append(toIndentedString(protonServiceRoleArn)).append("\n");
    sb.append("    provisioning: ").append(toIndentedString(provisioning)).append("\n");
    sb.append("    templateMajorVersion: ").append(toIndentedString(templateMajorVersion)).append("\n");
    sb.append("    templateMinorVersion: ").append(toIndentedString(templateMinorVersion)).append("\n");
    sb.append("    templateName: ").append(toIndentedString(templateName)).append("\n");
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
    openapiFields.add("componentRoleArn");
    openapiFields.add("createdAt");
    openapiFields.add("deploymentStatus");
    openapiFields.add("deploymentStatusMessage");
    openapiFields.add("description");
    openapiFields.add("environmentAccountConnectionId");
    openapiFields.add("environmentAccountId");
    openapiFields.add("lastAttemptedDeploymentId");
    openapiFields.add("lastDeploymentAttemptedAt");
    openapiFields.add("lastDeploymentSucceededAt");
    openapiFields.add("lastSucceededDeploymentId");
    openapiFields.add("name");
    openapiFields.add("protonServiceRoleArn");
    openapiFields.add("provisioning");
    openapiFields.add("templateMajorVersion");
    openapiFields.add("templateMinorVersion");
    openapiFields.add("templateName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("arn");
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("deploymentStatus");
    openapiRequiredFields.add("lastDeploymentAttemptedAt");
    openapiRequiredFields.add("lastDeploymentSucceededAt");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("templateMajorVersion");
    openapiRequiredFields.add("templateMinorVersion");
    openapiRequiredFields.add("templateName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EnvironmentSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EnvironmentSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EnvironmentSummary is not found in the empty JSON string", EnvironmentSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EnvironmentSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EnvironmentSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EnvironmentSummary.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `arn`
      String.validateJsonElement(jsonObj.get("arn"));
      // validate the optional field `componentRoleArn`
      if (jsonObj.get("componentRoleArn") != null && !jsonObj.get("componentRoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("componentRoleArn"));
      }
      // validate the required field `createdAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("createdAt"));
      // validate the required field `deploymentStatus`
      DeploymentStatus.validateJsonElement(jsonObj.get("deploymentStatus"));
      // validate the optional field `deploymentStatusMessage`
      if (jsonObj.get("deploymentStatusMessage") != null && !jsonObj.get("deploymentStatusMessage").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("deploymentStatusMessage"));
      }
      // validate the optional field `description`
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("description"));
      }
      // validate the optional field `environmentAccountConnectionId`
      if (jsonObj.get("environmentAccountConnectionId") != null && !jsonObj.get("environmentAccountConnectionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("environmentAccountConnectionId"));
      }
      // validate the optional field `environmentAccountId`
      if (jsonObj.get("environmentAccountId") != null && !jsonObj.get("environmentAccountId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("environmentAccountId"));
      }
      // validate the optional field `lastAttemptedDeploymentId`
      if (jsonObj.get("lastAttemptedDeploymentId") != null && !jsonObj.get("lastAttemptedDeploymentId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("lastAttemptedDeploymentId"));
      }
      // validate the required field `lastDeploymentAttemptedAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("lastDeploymentAttemptedAt"));
      // validate the required field `lastDeploymentSucceededAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("lastDeploymentSucceededAt"));
      // validate the optional field `lastSucceededDeploymentId`
      if (jsonObj.get("lastSucceededDeploymentId") != null && !jsonObj.get("lastSucceededDeploymentId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("lastSucceededDeploymentId"));
      }
      // validate the required field `name`
      String.validateJsonElement(jsonObj.get("name"));
      // validate the optional field `protonServiceRoleArn`
      if (jsonObj.get("protonServiceRoleArn") != null && !jsonObj.get("protonServiceRoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("protonServiceRoleArn"));
      }
      // validate the optional field `provisioning`
      if (jsonObj.get("provisioning") != null && !jsonObj.get("provisioning").isJsonNull()) {
        Provisioning.validateJsonElement(jsonObj.get("provisioning"));
      }
      // validate the required field `templateMajorVersion`
      String.validateJsonElement(jsonObj.get("templateMajorVersion"));
      // validate the required field `templateMinorVersion`
      String.validateJsonElement(jsonObj.get("templateMinorVersion"));
      // validate the required field `templateName`
      String.validateJsonElement(jsonObj.get("templateName"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EnvironmentSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EnvironmentSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EnvironmentSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EnvironmentSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<EnvironmentSummary>() {
           @Override
           public void write(JsonWriter out, EnvironmentSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EnvironmentSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EnvironmentSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EnvironmentSummary
   * @throws IOException if the JSON string is invalid with respect to EnvironmentSummary
   */
  public static EnvironmentSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EnvironmentSummary.class);
  }

  /**
   * Convert an instance of EnvironmentSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

