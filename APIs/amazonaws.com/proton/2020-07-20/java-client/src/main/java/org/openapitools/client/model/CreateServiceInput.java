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
import java.util.List;

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
 * CreateServiceInput
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateServiceInput {
  public static final String SERIALIZED_NAME_BRANCH_NAME = "branchName";
  @SerializedName(SERIALIZED_NAME_BRANCH_NAME)
  private String branchName;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_REPOSITORY_CONNECTION_ARN = "repositoryConnectionArn";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_CONNECTION_ARN)
  private String repositoryConnectionArn;

  public static final String SERIALIZED_NAME_REPOSITORY_ID = "repositoryId";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_ID)
  private String repositoryId;

  public static final String SERIALIZED_NAME_SPEC = "spec";
  @SerializedName(SERIALIZED_NAME_SPEC)
  private String spec;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List tags;

  public static final String SERIALIZED_NAME_TEMPLATE_MAJOR_VERSION = "templateMajorVersion";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_MAJOR_VERSION)
  private String templateMajorVersion;

  public static final String SERIALIZED_NAME_TEMPLATE_MINOR_VERSION = "templateMinorVersion";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_MINOR_VERSION)
  private String templateMinorVersion;

  public static final String SERIALIZED_NAME_TEMPLATE_NAME = "templateName";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_NAME)
  private String templateName;

  public CreateServiceInput() {
  }

  public CreateServiceInput branchName(String branchName) {
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


  public CreateServiceInput description(String description) {
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


  public CreateServiceInput name(String name) {
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


  public CreateServiceInput repositoryConnectionArn(String repositoryConnectionArn) {
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


  public CreateServiceInput repositoryId(String repositoryId) {
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


  public CreateServiceInput spec(String spec) {
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


  public CreateServiceInput tags(List tags) {
    this.tags = tags;
    return this;
  }

  /**
   * Get tags
   * @return tags
   */
  @javax.annotation.Nullable
  public List getTags() {
    return tags;
  }

  public void setTags(List tags) {
    this.tags = tags;
  }


  public CreateServiceInput templateMajorVersion(String templateMajorVersion) {
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


  public CreateServiceInput templateMinorVersion(String templateMinorVersion) {
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


  public CreateServiceInput templateName(String templateName) {
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
    CreateServiceInput createServiceInput = (CreateServiceInput) o;
    return Objects.equals(this.branchName, createServiceInput.branchName) &&
        Objects.equals(this.description, createServiceInput.description) &&
        Objects.equals(this.name, createServiceInput.name) &&
        Objects.equals(this.repositoryConnectionArn, createServiceInput.repositoryConnectionArn) &&
        Objects.equals(this.repositoryId, createServiceInput.repositoryId) &&
        Objects.equals(this.spec, createServiceInput.spec) &&
        Objects.equals(this.tags, createServiceInput.tags) &&
        Objects.equals(this.templateMajorVersion, createServiceInput.templateMajorVersion) &&
        Objects.equals(this.templateMinorVersion, createServiceInput.templateMinorVersion) &&
        Objects.equals(this.templateName, createServiceInput.templateName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(branchName, description, name, repositoryConnectionArn, repositoryId, spec, tags, templateMajorVersion, templateMinorVersion, templateName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateServiceInput {\n");
    sb.append("    branchName: ").append(toIndentedString(branchName)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    repositoryConnectionArn: ").append(toIndentedString(repositoryConnectionArn)).append("\n");
    sb.append("    repositoryId: ").append(toIndentedString(repositoryId)).append("\n");
    sb.append("    spec: ").append(toIndentedString(spec)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
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
    openapiFields.add("branchName");
    openapiFields.add("description");
    openapiFields.add("name");
    openapiFields.add("repositoryConnectionArn");
    openapiFields.add("repositoryId");
    openapiFields.add("spec");
    openapiFields.add("tags");
    openapiFields.add("templateMajorVersion");
    openapiFields.add("templateMinorVersion");
    openapiFields.add("templateName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("spec");
    openapiRequiredFields.add("templateMajorVersion");
    openapiRequiredFields.add("templateName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateServiceInput
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateServiceInput.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateServiceInput is not found in the empty JSON string", CreateServiceInput.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateServiceInput.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateServiceInput` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateServiceInput.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `branchName`
      if (jsonObj.get("branchName") != null && !jsonObj.get("branchName").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("branchName"));
      }
      // validate the optional field `description`
      if (jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("description"));
      }
      // validate the required field `name`
      String.validateJsonElement(jsonObj.get("name"));
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
      // validate the optional field `tags`
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("tags"));
      }
      // validate the required field `templateMajorVersion`
      String.validateJsonElement(jsonObj.get("templateMajorVersion"));
      // validate the optional field `templateMinorVersion`
      if (jsonObj.get("templateMinorVersion") != null && !jsonObj.get("templateMinorVersion").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("templateMinorVersion"));
      }
      // validate the required field `templateName`
      String.validateJsonElement(jsonObj.get("templateName"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateServiceInput.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateServiceInput' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateServiceInput> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateServiceInput.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateServiceInput>() {
           @Override
           public void write(JsonWriter out, CreateServiceInput value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateServiceInput read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateServiceInput given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateServiceInput
   * @throws IOException if the JSON string is invalid with respect to CreateServiceInput
   */
  public static CreateServiceInput fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateServiceInput.class);
  }

  /**
   * Convert an instance of CreateServiceInput to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

