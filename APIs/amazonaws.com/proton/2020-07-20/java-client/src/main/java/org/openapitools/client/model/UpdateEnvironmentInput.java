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
import java.util.Arrays;
import org.openapitools.client.model.DeploymentUpdateType;
import org.openapitools.client.model.UpdateEnvironmentInputProvisioningRepository;

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
 * UpdateEnvironmentInput
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateEnvironmentInput {
  public static final String SERIALIZED_NAME_CODEBUILD_ROLE_ARN = "codebuildRoleArn";
  @SerializedName(SERIALIZED_NAME_CODEBUILD_ROLE_ARN)
  private String codebuildRoleArn;

  public static final String SERIALIZED_NAME_COMPONENT_ROLE_ARN = "componentRoleArn";
  @SerializedName(SERIALIZED_NAME_COMPONENT_ROLE_ARN)
  private String componentRoleArn;

  public static final String SERIALIZED_NAME_DEPLOYMENT_TYPE = "deploymentType";
  @SerializedName(SERIALIZED_NAME_DEPLOYMENT_TYPE)
  private DeploymentUpdateType deploymentType;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_CONNECTION_ID = "environmentAccountConnectionId";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT_ACCOUNT_CONNECTION_ID)
  private String environmentAccountConnectionId;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROTON_SERVICE_ROLE_ARN = "protonServiceRoleArn";
  @SerializedName(SERIALIZED_NAME_PROTON_SERVICE_ROLE_ARN)
  private String protonServiceRoleArn;

  public static final String SERIALIZED_NAME_PROVISIONING_REPOSITORY = "provisioningRepository";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_REPOSITORY)
  private UpdateEnvironmentInputProvisioningRepository provisioningRepository;

  public static final String SERIALIZED_NAME_SPEC = "spec";
  @SerializedName(SERIALIZED_NAME_SPEC)
  private String spec;

  public static final String SERIALIZED_NAME_TEMPLATE_MAJOR_VERSION = "templateMajorVersion";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_MAJOR_VERSION)
  private String templateMajorVersion;

  public static final String SERIALIZED_NAME_TEMPLATE_MINOR_VERSION = "templateMinorVersion";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_MINOR_VERSION)
  private String templateMinorVersion;

  public UpdateEnvironmentInput() {
  }

  public UpdateEnvironmentInput codebuildRoleArn(String codebuildRoleArn) {
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


  public UpdateEnvironmentInput componentRoleArn(String componentRoleArn) {
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


  public UpdateEnvironmentInput deploymentType(DeploymentUpdateType deploymentType) {
    this.deploymentType = deploymentType;
    return this;
  }

  /**
   * Get deploymentType
   * @return deploymentType
   */
  @javax.annotation.Nonnull
  public DeploymentUpdateType getDeploymentType() {
    return deploymentType;
  }

  public void setDeploymentType(DeploymentUpdateType deploymentType) {
    this.deploymentType = deploymentType;
  }


  public UpdateEnvironmentInput description(String description) {
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


  public UpdateEnvironmentInput environmentAccountConnectionId(String environmentAccountConnectionId) {
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


  public UpdateEnvironmentInput name(String name) {
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


  public UpdateEnvironmentInput protonServiceRoleArn(String protonServiceRoleArn) {
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


  public UpdateEnvironmentInput provisioningRepository(UpdateEnvironmentInputProvisioningRepository provisioningRepository) {
    this.provisioningRepository = provisioningRepository;
    return this;
  }

  /**
   * Get provisioningRepository
   * @return provisioningRepository
   */
  @javax.annotation.Nullable
  public UpdateEnvironmentInputProvisioningRepository getProvisioningRepository() {
    return provisioningRepository;
  }

  public void setProvisioningRepository(UpdateEnvironmentInputProvisioningRepository provisioningRepository) {
    this.provisioningRepository = provisioningRepository;
  }


  public UpdateEnvironmentInput spec(String spec) {
    this.spec = spec;
    return this;
  }

  /**
   * Get spec
   * @return spec
   */
  @javax.annotation.Nullable
  public String getSpec() {
    return spec;
  }

  public void setSpec(String spec) {
    this.spec = spec;
  }


  public UpdateEnvironmentInput templateMajorVersion(String templateMajorVersion) {
    this.templateMajorVersion = templateMajorVersion;
    return this;
  }

  /**
   * Get templateMajorVersion
   * @return templateMajorVersion
   */
  @javax.annotation.Nullable
  public String getTemplateMajorVersion() {
    return templateMajorVersion;
  }

  public void setTemplateMajorVersion(String templateMajorVersion) {
    this.templateMajorVersion = templateMajorVersion;
  }


  public UpdateEnvironmentInput templateMinorVersion(String templateMinorVersion) {
    this.templateMinorVersion = templateMinorVersion;
    return this;
  }

  /**
   * Get templateMinorVersion
   * @return templateMinorVersion
   */
  @javax.annotation.Nullable
  public String getTemplateMinorVersion() {
    return templateMinorVersion;
  }

  public void setTemplateMinorVersion(String templateMinorVersion) {
    this.templateMinorVersion = templateMinorVersion;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateEnvironmentInput updateEnvironmentInput = (UpdateEnvironmentInput) o;
    return Objects.equals(this.codebuildRoleArn, updateEnvironmentInput.codebuildRoleArn) &&
        Objects.equals(this.componentRoleArn, updateEnvironmentInput.componentRoleArn) &&
        Objects.equals(this.deploymentType, updateEnvironmentInput.deploymentType) &&
        Objects.equals(this.description, updateEnvironmentInput.description) &&
        Objects.equals(this.environmentAccountConnectionId, updateEnvironmentInput.environmentAccountConnectionId) &&
        Objects.equals(this.name, updateEnvironmentInput.name) &&
        Objects.equals(this.protonServiceRoleArn, updateEnvironmentInput.protonServiceRoleArn) &&
        Objects.equals(this.provisioningRepository, updateEnvironmentInput.provisioningRepository) &&
        Objects.equals(this.spec, updateEnvironmentInput.spec) &&
        Objects.equals(this.templateMajorVersion, updateEnvironmentInput.templateMajorVersion) &&
        Objects.equals(this.templateMinorVersion, updateEnvironmentInput.templateMinorVersion);
  }

  @Override
  public int hashCode() {
    return Objects.hash(codebuildRoleArn, componentRoleArn, deploymentType, description, environmentAccountConnectionId, name, protonServiceRoleArn, provisioningRepository, spec, templateMajorVersion, templateMinorVersion);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateEnvironmentInput {\n");
    sb.append("    codebuildRoleArn: ").append(toIndentedString(codebuildRoleArn)).append("\n");
    sb.append("    componentRoleArn: ").append(toIndentedString(componentRoleArn)).append("\n");
    sb.append("    deploymentType: ").append(toIndentedString(deploymentType)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    environmentAccountConnectionId: ").append(toIndentedString(environmentAccountConnectionId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    protonServiceRoleArn: ").append(toIndentedString(protonServiceRoleArn)).append("\n");
    sb.append("    provisioningRepository: ").append(toIndentedString(provisioningRepository)).append("\n");
    sb.append("    spec: ").append(toIndentedString(spec)).append("\n");
    sb.append("    templateMajorVersion: ").append(toIndentedString(templateMajorVersion)).append("\n");
    sb.append("    templateMinorVersion: ").append(toIndentedString(templateMinorVersion)).append("\n");
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
    openapiFields.add("codebuildRoleArn");
    openapiFields.add("componentRoleArn");
    openapiFields.add("deploymentType");
    openapiFields.add("description");
    openapiFields.add("environmentAccountConnectionId");
    openapiFields.add("name");
    openapiFields.add("protonServiceRoleArn");
    openapiFields.add("provisioningRepository");
    openapiFields.add("spec");
    openapiFields.add("templateMajorVersion");
    openapiFields.add("templateMinorVersion");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("deploymentType");
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateEnvironmentInput
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateEnvironmentInput.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateEnvironmentInput is not found in the empty JSON string", UpdateEnvironmentInput.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateEnvironmentInput.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateEnvironmentInput` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateEnvironmentInput.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `codebuildRoleArn`
      if (jsonObj.get("codebuildRoleArn") != null && !jsonObj.get("codebuildRoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("codebuildRoleArn"));
      }
      // validate the optional field `componentRoleArn`
      if (jsonObj.get("componentRoleArn") != null && !jsonObj.get("componentRoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("componentRoleArn"));
      }
      // validate the required field `deploymentType`
      DeploymentUpdateType.validateJsonElement(jsonObj.get("deploymentType"));
      // validate the optional field `description`
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("description"));
      }
      // validate the optional field `environmentAccountConnectionId`
      if (jsonObj.get("environmentAccountConnectionId") != null && !jsonObj.get("environmentAccountConnectionId").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("environmentAccountConnectionId"));
      }
      // validate the required field `name`
      String.validateJsonElement(jsonObj.get("name"));
      // validate the optional field `protonServiceRoleArn`
      if (jsonObj.get("protonServiceRoleArn") != null && !jsonObj.get("protonServiceRoleArn").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("protonServiceRoleArn"));
      }
      // validate the optional field `provisioningRepository`
      if (jsonObj.get("provisioningRepository") != null && !jsonObj.get("provisioningRepository").isJsonNull()) {
        UpdateEnvironmentInputProvisioningRepository.validateJsonElement(jsonObj.get("provisioningRepository"));
      }
      // validate the optional field `spec`
      if (jsonObj.get("spec") != null && !jsonObj.get("spec").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("spec"));
      }
      // validate the optional field `templateMajorVersion`
      if (jsonObj.get("templateMajorVersion") != null && !jsonObj.get("templateMajorVersion").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("templateMajorVersion"));
      }
      // validate the optional field `templateMinorVersion`
      if (jsonObj.get("templateMinorVersion") != null && !jsonObj.get("templateMinorVersion").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("templateMinorVersion"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateEnvironmentInput.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateEnvironmentInput' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateEnvironmentInput> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateEnvironmentInput.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateEnvironmentInput>() {
           @Override
           public void write(JsonWriter out, UpdateEnvironmentInput value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateEnvironmentInput read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateEnvironmentInput given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateEnvironmentInput
   * @throws IOException if the JSON string is invalid with respect to UpdateEnvironmentInput
   */
  public static UpdateEnvironmentInput fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateEnvironmentInput.class);
  }

  /**
   * Convert an instance of UpdateEnvironmentInput to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

