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
import org.openapitools.client.model.ServicePipeline;
import org.openapitools.client.model.ServiceStatus;

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
 * GetServiceOutputService
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetServiceOutputService {
  public static final String SERIALIZED_NAME_ARN = "arn";
  @SerializedName(SERIALIZED_NAME_ARN)
  private String arn;

  public static final String SERIALIZED_NAME_BRANCH_NAME = "branchName";
  @SerializedName(SERIALIZED_NAME_BRANCH_NAME)
  private String branchName;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_LAST_MODIFIED_AT = "lastModifiedAt";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED_AT)
  private OffsetDateTime lastModifiedAt;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PIPELINE = "pipeline";
  @SerializedName(SERIALIZED_NAME_PIPELINE)
  private ServicePipeline pipeline;

  public static final String SERIALIZED_NAME_REPOSITORY_CONNECTION_ARN = "repositoryConnectionArn";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_CONNECTION_ARN)
  private String repositoryConnectionArn;

  public static final String SERIALIZED_NAME_REPOSITORY_ID = "repositoryId";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_ID)
  private String repositoryId;

  public static final String SERIALIZED_NAME_SPEC = "spec";
  @SerializedName(SERIALIZED_NAME_SPEC)
  private String spec;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private ServiceStatus status;

  public static final String SERIALIZED_NAME_STATUS_MESSAGE = "statusMessage";
  @SerializedName(SERIALIZED_NAME_STATUS_MESSAGE)
  private String statusMessage;

  public static final String SERIALIZED_NAME_TEMPLATE_NAME = "templateName";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_NAME)
  private String templateName;

  public GetServiceOutputService() {
  }

  public GetServiceOutputService arn(String arn) {
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


  public GetServiceOutputService branchName(String branchName) {
    this.branchName = branchName;
    return this;
  }

  /**
   * Get branchName
   * @return branchName
   */
  @javax.annotation.Nullable
  public String getBranchName() {
    return branchName;
  }

  public void setBranchName(String branchName) {
    this.branchName = branchName;
  }


  public GetServiceOutputService createdAt(OffsetDateTime createdAt) {
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


  public GetServiceOutputService description(String description) {
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


  public GetServiceOutputService lastModifiedAt(OffsetDateTime lastModifiedAt) {
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


  public GetServiceOutputService name(String name) {
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


  public GetServiceOutputService pipeline(ServicePipeline pipeline) {
    this.pipeline = pipeline;
    return this;
  }

  /**
   * Get pipeline
   * @return pipeline
   */
  @javax.annotation.Nullable
  public ServicePipeline getPipeline() {
    return pipeline;
  }

  public void setPipeline(ServicePipeline pipeline) {
    this.pipeline = pipeline;
  }


  public GetServiceOutputService repositoryConnectionArn(String repositoryConnectionArn) {
    this.repositoryConnectionArn = repositoryConnectionArn;
    return this;
  }

  /**
   * Get repositoryConnectionArn
   * @return repositoryConnectionArn
   */
  @javax.annotation.Nullable
  public String getRepositoryConnectionArn() {
    return repositoryConnectionArn;
  }

  public void setRepositoryConnectionArn(String repositoryConnectionArn) {
    this.repositoryConnectionArn = repositoryConnectionArn;
  }


  public GetServiceOutputService repositoryId(String repositoryId) {
    this.repositoryId = repositoryId;
    return this;
  }

  /**
   * Get repositoryId
   * @return repositoryId
   */
  @javax.annotation.Nullable
  public String getRepositoryId() {
    return repositoryId;
  }

  public void setRepositoryId(String repositoryId) {
    this.repositoryId = repositoryId;
  }


  public GetServiceOutputService spec(String spec) {
    this.spec = spec;
    return this;
  }

  /**
   * Get spec
   * @return spec
   */
  @javax.annotation.Nonnull
  public String getSpec() {
    return spec;
  }

  public void setSpec(String spec) {
    this.spec = spec;
  }


  public GetServiceOutputService status(ServiceStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public ServiceStatus getStatus() {
    return status;
  }

  public void setStatus(ServiceStatus status) {
    this.status = status;
  }


  public GetServiceOutputService statusMessage(String statusMessage) {
    this.statusMessage = statusMessage;
    return this;
  }

  /**
   * Get statusMessage
   * @return statusMessage
   */
  @javax.annotation.Nullable
  public String getStatusMessage() {
    return statusMessage;
  }

  public void setStatusMessage(String statusMessage) {
    this.statusMessage = statusMessage;
  }


  public GetServiceOutputService templateName(String templateName) {
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
    GetServiceOutputService getServiceOutputService = (GetServiceOutputService) o;
    return Objects.equals(this.arn, getServiceOutputService.arn) &&
        Objects.equals(this.branchName, getServiceOutputService.branchName) &&
        Objects.equals(this.createdAt, getServiceOutputService.createdAt) &&
        Objects.equals(this.description, getServiceOutputService.description) &&
        Objects.equals(this.lastModifiedAt, getServiceOutputService.lastModifiedAt) &&
        Objects.equals(this.name, getServiceOutputService.name) &&
        Objects.equals(this.pipeline, getServiceOutputService.pipeline) &&
        Objects.equals(this.repositoryConnectionArn, getServiceOutputService.repositoryConnectionArn) &&
        Objects.equals(this.repositoryId, getServiceOutputService.repositoryId) &&
        Objects.equals(this.spec, getServiceOutputService.spec) &&
        Objects.equals(this.status, getServiceOutputService.status) &&
        Objects.equals(this.statusMessage, getServiceOutputService.statusMessage) &&
        Objects.equals(this.templateName, getServiceOutputService.templateName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(arn, branchName, createdAt, description, lastModifiedAt, name, pipeline, repositoryConnectionArn, repositoryId, spec, status, statusMessage, templateName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetServiceOutputService {\n");
    sb.append("    arn: ").append(toIndentedString(arn)).append("\n");
    sb.append("    branchName: ").append(toIndentedString(branchName)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    lastModifiedAt: ").append(toIndentedString(lastModifiedAt)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    pipeline: ").append(toIndentedString(pipeline)).append("\n");
    sb.append("    repositoryConnectionArn: ").append(toIndentedString(repositoryConnectionArn)).append("\n");
    sb.append("    repositoryId: ").append(toIndentedString(repositoryId)).append("\n");
    sb.append("    spec: ").append(toIndentedString(spec)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statusMessage: ").append(toIndentedString(statusMessage)).append("\n");
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
    openapiFields.add("branchName");
    openapiFields.add("createdAt");
    openapiFields.add("description");
    openapiFields.add("lastModifiedAt");
    openapiFields.add("name");
    openapiFields.add("pipeline");
    openapiFields.add("repositoryConnectionArn");
    openapiFields.add("repositoryId");
    openapiFields.add("spec");
    openapiFields.add("status");
    openapiFields.add("statusMessage");
    openapiFields.add("templateName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("arn");
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("lastModifiedAt");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("spec");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("templateName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetServiceOutputService
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetServiceOutputService.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetServiceOutputService is not found in the empty JSON string", GetServiceOutputService.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetServiceOutputService.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetServiceOutputService` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetServiceOutputService.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `arn`
      String.validateJsonElement(jsonObj.get("arn"));
      // validate the optional field `branchName`
      if (jsonObj.get("branchName") != null && !jsonObj.get("branchName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("branchName"));
      }
      // validate the required field `createdAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("createdAt"));
      // validate the optional field `description`
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("description"));
      }
      // validate the required field `lastModifiedAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("lastModifiedAt"));
      // validate the required field `name`
      String.validateJsonElement(jsonObj.get("name"));
      // validate the optional field `pipeline`
      if (jsonObj.get("pipeline") != null && !jsonObj.get("pipeline").isJsonNull()) {
        ServicePipeline.validateJsonElement(jsonObj.get("pipeline"));
      }
      // validate the optional field `repositoryConnectionArn`
      if (jsonObj.get("repositoryConnectionArn") != null && !jsonObj.get("repositoryConnectionArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("repositoryConnectionArn"));
      }
      // validate the optional field `repositoryId`
      if (jsonObj.get("repositoryId") != null && !jsonObj.get("repositoryId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("repositoryId"));
      }
      // validate the required field `spec`
      String.validateJsonElement(jsonObj.get("spec"));
      // validate the required field `status`
      ServiceStatus.validateJsonElement(jsonObj.get("status"));
      // validate the optional field `statusMessage`
      if (jsonObj.get("statusMessage") != null && !jsonObj.get("statusMessage").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("statusMessage"));
      }
      // validate the required field `templateName`
      String.validateJsonElement(jsonObj.get("templateName"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetServiceOutputService.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetServiceOutputService' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetServiceOutputService> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetServiceOutputService.class));

       return (TypeAdapter<T>) new TypeAdapter<GetServiceOutputService>() {
           @Override
           public void write(JsonWriter out, GetServiceOutputService value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetServiceOutputService read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetServiceOutputService given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetServiceOutputService
   * @throws IOException if the JSON string is invalid with respect to GetServiceOutputService
   */
  public static GetServiceOutputService fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetServiceOutputService.class);
  }

  /**
   * Convert an instance of GetServiceOutputService to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

