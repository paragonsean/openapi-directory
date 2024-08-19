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
import org.openapitools.client.model.EnvironmentAccountConnectionStatus;

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
 * AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection {
  public static final String SERIALIZED_NAME_ARN = "arn";
  @SerializedName(SERIALIZED_NAME_ARN)
  private String arn;

  public static final String SERIALIZED_NAME_CODEBUILD_ROLE_ARN = "codebuildRoleArn";
  @SerializedName(SERIALIZED_NAME_CODEBUILD_ROLE_ARN)
  private String codebuildRoleArn;

  public static final String SERIALIZED_NAME_COMPONENT_ROLE_ARN = "componentRoleArn";
  @SerializedName(SERIALIZED_NAME_COMPONENT_ROLE_ARN)
  private String componentRoleArn;

  public static final String SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_ID = "environmentAccountId";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_ID)
  private String environmentAccountId;

  public static final String SERIALIZED_NAME_ENVIRONMENT_NAME = "environmentName";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_NAME)
  private String environmentName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LAST_MODIFIED_AT = "lastModifiedAt";
  @SerializedName(SERIALIZED_NAME_LAST_MODIFIED_AT)
  private OffsetDateTime lastModifiedAt;

  public static final String SERIALIZED_NAME_MANAGEMENT_ACCOUNT_ID = "managementAccountId";
  @SerializedName(SERIALIZED_NAME_MANAGEMENT_ACCOUNT_ID)
  private String managementAccountId;

  public static final String SERIALIZED_NAME_REQUESTED_AT = "requestedAt";
  @SerializedName(SERIALIZED_NAME_REQUESTED_AT)
  private OffsetDateTime requestedAt;

  public static final String SERIALIZED_NAME_ROLE_ARN = "roleArn";
  @SerializedName(SERIALIZED_NAME_ROLE_ARN)
  private String roleArn;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private EnvironmentAccountConnectionStatus status;

  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection() {
  }

  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection arn(String arn) {
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


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection codebuildRoleArn(String codebuildRoleArn) {
    this.codebuildRoleArn = codebuildRoleArn;
    return this;
  }

  /**
   * Get codebuildRoleArn
   * @return codebuildRoleArn
   */
  @javax.annotation.Nullable
  public String getCodebuildRoleArn() {
    return codebuildRoleArn;
  }

  public void setCodebuildRoleArn(String codebuildRoleArn) {
    this.codebuildRoleArn = codebuildRoleArn;
  }


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection componentRoleArn(String componentRoleArn) {
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


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection environmentAccountId(String environmentAccountId) {
    this.environmentAccountId = environmentAccountId;
    return this;
  }

  /**
   * Get environmentAccountId
   * @return environmentAccountId
   */
  @javax.annotation.Nonnull
  public String getEnvironmentAccountId() {
    return environmentAccountId;
  }

  public void setEnvironmentAccountId(String environmentAccountId) {
    this.environmentAccountId = environmentAccountId;
  }


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection environmentName(String environmentName) {
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


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection id(String id) {
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


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection lastModifiedAt(OffsetDateTime lastModifiedAt) {
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


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection managementAccountId(String managementAccountId) {
    this.managementAccountId = managementAccountId;
    return this;
  }

  /**
   * Get managementAccountId
   * @return managementAccountId
   */
  @javax.annotation.Nonnull
  public String getManagementAccountId() {
    return managementAccountId;
  }

  public void setManagementAccountId(String managementAccountId) {
    this.managementAccountId = managementAccountId;
  }


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection requestedAt(OffsetDateTime requestedAt) {
    this.requestedAt = requestedAt;
    return this;
  }

  /**
   * Get requestedAt
   * @return requestedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getRequestedAt() {
    return requestedAt;
  }

  public void setRequestedAt(OffsetDateTime requestedAt) {
    this.requestedAt = requestedAt;
  }


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection roleArn(String roleArn) {
    this.roleArn = roleArn;
    return this;
  }

  /**
   * Get roleArn
   * @return roleArn
   */
  @javax.annotation.Nonnull
  public String getRoleArn() {
    return roleArn;
  }

  public void setRoleArn(String roleArn) {
    this.roleArn = roleArn;
  }


  public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection status(EnvironmentAccountConnectionStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public EnvironmentAccountConnectionStatus getStatus() {
    return status;
  }

  public void setStatus(EnvironmentAccountConnectionStatus status) {
    this.status = status;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection = (AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection) o;
    return Objects.equals(this.arn, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.arn) &&
        Objects.equals(this.codebuildRoleArn, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.codebuildRoleArn) &&
        Objects.equals(this.componentRoleArn, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.componentRoleArn) &&
        Objects.equals(this.environmentAccountId, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.environmentAccountId) &&
        Objects.equals(this.environmentName, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.environmentName) &&
        Objects.equals(this.id, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.id) &&
        Objects.equals(this.lastModifiedAt, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.lastModifiedAt) &&
        Objects.equals(this.managementAccountId, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.managementAccountId) &&
        Objects.equals(this.requestedAt, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.requestedAt) &&
        Objects.equals(this.roleArn, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.roleArn) &&
        Objects.equals(this.status, acceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(arn, codebuildRoleArn, componentRoleArn, environmentAccountId, environmentName, id, lastModifiedAt, managementAccountId, requestedAt, roleArn, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection {\n");
    sb.append("    arn: ").append(toIndentedString(arn)).append("\n");
    sb.append("    codebuildRoleArn: ").append(toIndentedString(codebuildRoleArn)).append("\n");
    sb.append("    componentRoleArn: ").append(toIndentedString(componentRoleArn)).append("\n");
    sb.append("    environmentAccountId: ").append(toIndentedString(environmentAccountId)).append("\n");
    sb.append("    environmentName: ").append(toIndentedString(environmentName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastModifiedAt: ").append(toIndentedString(lastModifiedAt)).append("\n");
    sb.append("    managementAccountId: ").append(toIndentedString(managementAccountId)).append("\n");
    sb.append("    requestedAt: ").append(toIndentedString(requestedAt)).append("\n");
    sb.append("    roleArn: ").append(toIndentedString(roleArn)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("codebuildRoleArn");
    openapiFields.add("componentRoleArn");
    openapiFields.add("environmentAccountId");
    openapiFields.add("environmentName");
    openapiFields.add("id");
    openapiFields.add("lastModifiedAt");
    openapiFields.add("managementAccountId");
    openapiFields.add("requestedAt");
    openapiFields.add("roleArn");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("arn");
    openapiRequiredFields.add("environmentAccountId");
    openapiRequiredFields.add("environmentName");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("lastModifiedAt");
    openapiRequiredFields.add("managementAccountId");
    openapiRequiredFields.add("requestedAt");
    openapiRequiredFields.add("roleArn");
    openapiRequiredFields.add("status");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection is not found in the empty JSON string", AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `arn`
      String.validateJsonElement(jsonObj.get("arn"));
      // validate the optional field `codebuildRoleArn`
      if (jsonObj.get("codebuildRoleArn") != null && !jsonObj.get("codebuildRoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("codebuildRoleArn"));
      }
      // validate the optional field `componentRoleArn`
      if (jsonObj.get("componentRoleArn") != null && !jsonObj.get("componentRoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("componentRoleArn"));
      }
      // validate the required field `environmentAccountId`
      String.validateJsonElement(jsonObj.get("environmentAccountId"));
      // validate the required field `environmentName`
      String.validateJsonElement(jsonObj.get("environmentName"));
      // validate the required field `id`
      String.validateJsonElement(jsonObj.get("id"));
      // validate the required field `lastModifiedAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("lastModifiedAt"));
      // validate the required field `managementAccountId`
      String.validateJsonElement(jsonObj.get("managementAccountId"));
      // validate the required field `requestedAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("requestedAt"));
      // validate the required field `roleArn`
      String.validateJsonElement(jsonObj.get("roleArn"));
      // validate the required field `status`
      EnvironmentAccountConnectionStatus.validateJsonElement(jsonObj.get("status"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.class));

       return (TypeAdapter<T>) new TypeAdapter<AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection>() {
           @Override
           public void write(JsonWriter out, AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection
   * @throws IOException if the JSON string is invalid with respect to AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection
   */
  public static AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection.class);
  }

  /**
   * Convert an instance of AcceptEnvironmentAccountConnectionOutputEnvironmentAccountConnection to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

