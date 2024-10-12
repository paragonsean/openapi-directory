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
import org.openapitools.client.model.RepositoryProvider;
import org.openapitools.client.model.TemplateType;

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
 * CreateTemplateSyncConfigInput
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateTemplateSyncConfigInput {
  public static final String SERIALIZED_NAME_BRANCH = "branch";
  @SerializedName(SERIALIZED_NAME_BRANCH)
  private String branch;

  public static final String SERIALIZED_NAME_REPOSITORY_NAME = "repositoryName";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_NAME)
  private String repositoryName;

  public static final String SERIALIZED_NAME_REPOSITORY_PROVIDER = "repositoryProvider";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_PROVIDER)
  private RepositoryProvider repositoryProvider;

  public static final String SERIALIZED_NAME_SUBDIRECTORY = "subdirectory";
  @SerializedName(SERIALIZED_NAME_SUBDIRECTORY)
  private String subdirectory;

  public static final String SERIALIZED_NAME_TEMPLATE_NAME = "templateName";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_NAME)
  private String templateName;

  public static final String SERIALIZED_NAME_TEMPLATE_TYPE = "templateType";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_TYPE)
  private TemplateType templateType;

  public CreateTemplateSyncConfigInput() {
  }

  public CreateTemplateSyncConfigInput branch(String branch) {
    this.branch = branch;
    return this;
  }

  /**
   * Get branch
   * @return branch
   */
  @javax.annotation.Nonnull
  public String getBranch() {
    return branch;
  }

  public void setBranch(String branch) {
    this.branch = branch;
  }


  public CreateTemplateSyncConfigInput repositoryName(String repositoryName) {
    this.repositoryName = repositoryName;
    return this;
  }

  /**
   * Get repositoryName
   * @return repositoryName
   */
  @javax.annotation.Nonnull
  public String getRepositoryName() {
    return repositoryName;
  }

  public void setRepositoryName(String repositoryName) {
    this.repositoryName = repositoryName;
  }


  public CreateTemplateSyncConfigInput repositoryProvider(RepositoryProvider repositoryProvider) {
    this.repositoryProvider = repositoryProvider;
    return this;
  }

  /**
   * Get repositoryProvider
   * @return repositoryProvider
   */
  @javax.annotation.Nonnull
  public RepositoryProvider getRepositoryProvider() {
    return repositoryProvider;
  }

  public void setRepositoryProvider(RepositoryProvider repositoryProvider) {
    this.repositoryProvider = repositoryProvider;
  }


  public CreateTemplateSyncConfigInput subdirectory(String subdirectory) {
    this.subdirectory = subdirectory;
    return this;
  }

  /**
   * Get subdirectory
   * @return subdirectory
   */
  @javax.annotation.Nullable
  public String getSubdirectory() {
    return subdirectory;
  }

  public void setSubdirectory(String subdirectory) {
    this.subdirectory = subdirectory;
  }


  public CreateTemplateSyncConfigInput templateName(String templateName) {
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


  public CreateTemplateSyncConfigInput templateType(TemplateType templateType) {
    this.templateType = templateType;
    return this;
  }

  /**
   * Get templateType
   * @return templateType
   */
  @javax.annotation.Nonnull
  public TemplateType getTemplateType() {
    return templateType;
  }

  public void setTemplateType(TemplateType templateType) {
    this.templateType = templateType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateTemplateSyncConfigInput createTemplateSyncConfigInput = (CreateTemplateSyncConfigInput) o;
    return Objects.equals(this.branch, createTemplateSyncConfigInput.branch) &&
        Objects.equals(this.repositoryName, createTemplateSyncConfigInput.repositoryName) &&
        Objects.equals(this.repositoryProvider, createTemplateSyncConfigInput.repositoryProvider) &&
        Objects.equals(this.subdirectory, createTemplateSyncConfigInput.subdirectory) &&
        Objects.equals(this.templateName, createTemplateSyncConfigInput.templateName) &&
        Objects.equals(this.templateType, createTemplateSyncConfigInput.templateType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(branch, repositoryName, repositoryProvider, subdirectory, templateName, templateType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateTemplateSyncConfigInput {\n");
    sb.append("    branch: ").append(toIndentedString(branch)).append("\n");
    sb.append("    repositoryName: ").append(toIndentedString(repositoryName)).append("\n");
    sb.append("    repositoryProvider: ").append(toIndentedString(repositoryProvider)).append("\n");
    sb.append("    subdirectory: ").append(toIndentedString(subdirectory)).append("\n");
    sb.append("    templateName: ").append(toIndentedString(templateName)).append("\n");
    sb.append("    templateType: ").append(toIndentedString(templateType)).append("\n");
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
    openapiFields.add("branch");
    openapiFields.add("repositoryName");
    openapiFields.add("repositoryProvider");
    openapiFields.add("subdirectory");
    openapiFields.add("templateName");
    openapiFields.add("templateType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("branch");
    openapiRequiredFields.add("repositoryName");
    openapiRequiredFields.add("repositoryProvider");
    openapiRequiredFields.add("templateName");
    openapiRequiredFields.add("templateType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateTemplateSyncConfigInput
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateTemplateSyncConfigInput.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateTemplateSyncConfigInput is not found in the empty JSON string", CreateTemplateSyncConfigInput.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateTemplateSyncConfigInput.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateTemplateSyncConfigInput` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateTemplateSyncConfigInput.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `branch`
      String.validateJsonElement(jsonObj.get("branch"));
      // validate the required field `repositoryName`
      String.validateJsonElement(jsonObj.get("repositoryName"));
      // validate the required field `repositoryProvider`
      RepositoryProvider.validateJsonElement(jsonObj.get("repositoryProvider"));
      // validate the optional field `subdirectory`
      if (jsonObj.get("subdirectory") != null && !jsonObj.get("subdirectory").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("subdirectory"));
      }
      // validate the required field `templateName`
      String.validateJsonElement(jsonObj.get("templateName"));
      // validate the required field `templateType`
      TemplateType.validateJsonElement(jsonObj.get("templateType"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateTemplateSyncConfigInput.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateTemplateSyncConfigInput' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateTemplateSyncConfigInput> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateTemplateSyncConfigInput.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateTemplateSyncConfigInput>() {
           @Override
           public void write(JsonWriter out, CreateTemplateSyncConfigInput value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateTemplateSyncConfigInput read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateTemplateSyncConfigInput given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateTemplateSyncConfigInput
   * @throws IOException if the JSON string is invalid with respect to CreateTemplateSyncConfigInput
   */
  public static CreateTemplateSyncConfigInput fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateTemplateSyncConfigInput.class);
  }

  /**
   * Convert an instance of CreateTemplateSyncConfigInput to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

