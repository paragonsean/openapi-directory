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
import java.util.List;
import org.openapitools.client.model.BlockerStatus;
import org.openapitools.client.model.BlockerType;

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
 * UpdateServiceSyncBlockerOutputServiceSyncBlocker
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateServiceSyncBlockerOutputServiceSyncBlocker {
  public static final String SERIALIZED_NAME_CONTEXTS = "contexts";
  @SerializedName(SERIALIZED_NAME_CONTEXTS)
  private List contexts;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_REASON = "createdReason";
  @SerializedName(SERIALIZED_NAME_CREATED_REASON)
  private String createdReason;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_RESOLVED_AT = "resolvedAt";
  @SerializedName(SERIALIZED_NAME_RESOLVED_AT)
  private OffsetDateTime resolvedAt;

  public static final String SERIALIZED_NAME_RESOLVED_REASON = "resolvedReason";
  @SerializedName(SERIALIZED_NAME_RESOLVED_REASON)
  private String resolvedReason;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private BlockerStatus status;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private BlockerType type;

  public UpdateServiceSyncBlockerOutputServiceSyncBlocker() {
  }

  public UpdateServiceSyncBlockerOutputServiceSyncBlocker contexts(List contexts) {
    this.contexts = contexts;
    return this;
  }

  /**
   * Get contexts
   * @return contexts
   */
  @javax.annotation.Nullable
  public List getContexts() {
    return contexts;
  }

  public void setContexts(List contexts) {
    this.contexts = contexts;
  }


  public UpdateServiceSyncBlockerOutputServiceSyncBlocker createdAt(OffsetDateTime createdAt) {
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


  public UpdateServiceSyncBlockerOutputServiceSyncBlocker createdReason(String createdReason) {
    this.createdReason = createdReason;
    return this;
  }

  /**
   * Get createdReason
   * @return createdReason
   */
  @javax.annotation.Nonnull
  public String getCreatedReason() {
    return createdReason;
  }

  public void setCreatedReason(String createdReason) {
    this.createdReason = createdReason;
  }


  public UpdateServiceSyncBlockerOutputServiceSyncBlocker id(String id) {
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


  public UpdateServiceSyncBlockerOutputServiceSyncBlocker resolvedAt(OffsetDateTime resolvedAt) {
    this.resolvedAt = resolvedAt;
    return this;
  }

  /**
   * Get resolvedAt
   * @return resolvedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getResolvedAt() {
    return resolvedAt;
  }

  public void setResolvedAt(OffsetDateTime resolvedAt) {
    this.resolvedAt = resolvedAt;
  }


  public UpdateServiceSyncBlockerOutputServiceSyncBlocker resolvedReason(String resolvedReason) {
    this.resolvedReason = resolvedReason;
    return this;
  }

  /**
   * Get resolvedReason
   * @return resolvedReason
   */
  @javax.annotation.Nullable
  public String getResolvedReason() {
    return resolvedReason;
  }

  public void setResolvedReason(String resolvedReason) {
    this.resolvedReason = resolvedReason;
  }


  public UpdateServiceSyncBlockerOutputServiceSyncBlocker status(BlockerStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public BlockerStatus getStatus() {
    return status;
  }

  public void setStatus(BlockerStatus status) {
    this.status = status;
  }


  public UpdateServiceSyncBlockerOutputServiceSyncBlocker type(BlockerType type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nonnull
  public BlockerType getType() {
    return type;
  }

  public void setType(BlockerType type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateServiceSyncBlockerOutputServiceSyncBlocker updateServiceSyncBlockerOutputServiceSyncBlocker = (UpdateServiceSyncBlockerOutputServiceSyncBlocker) o;
    return Objects.equals(this.contexts, updateServiceSyncBlockerOutputServiceSyncBlocker.contexts) &&
        Objects.equals(this.createdAt, updateServiceSyncBlockerOutputServiceSyncBlocker.createdAt) &&
        Objects.equals(this.createdReason, updateServiceSyncBlockerOutputServiceSyncBlocker.createdReason) &&
        Objects.equals(this.id, updateServiceSyncBlockerOutputServiceSyncBlocker.id) &&
        Objects.equals(this.resolvedAt, updateServiceSyncBlockerOutputServiceSyncBlocker.resolvedAt) &&
        Objects.equals(this.resolvedReason, updateServiceSyncBlockerOutputServiceSyncBlocker.resolvedReason) &&
        Objects.equals(this.status, updateServiceSyncBlockerOutputServiceSyncBlocker.status) &&
        Objects.equals(this.type, updateServiceSyncBlockerOutputServiceSyncBlocker.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contexts, createdAt, createdReason, id, resolvedAt, resolvedReason, status, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateServiceSyncBlockerOutputServiceSyncBlocker {\n");
    sb.append("    contexts: ").append(toIndentedString(contexts)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdReason: ").append(toIndentedString(createdReason)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    resolvedAt: ").append(toIndentedString(resolvedAt)).append("\n");
    sb.append("    resolvedReason: ").append(toIndentedString(resolvedReason)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("contexts");
    openapiFields.add("createdAt");
    openapiFields.add("createdReason");
    openapiFields.add("id");
    openapiFields.add("resolvedAt");
    openapiFields.add("resolvedReason");
    openapiFields.add("status");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("createdReason");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateServiceSyncBlockerOutputServiceSyncBlocker
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateServiceSyncBlockerOutputServiceSyncBlocker.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateServiceSyncBlockerOutputServiceSyncBlocker is not found in the empty JSON string", UpdateServiceSyncBlockerOutputServiceSyncBlocker.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateServiceSyncBlockerOutputServiceSyncBlocker.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateServiceSyncBlockerOutputServiceSyncBlocker` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateServiceSyncBlockerOutputServiceSyncBlocker.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `contexts`
      if (jsonObj.get("contexts") != null && !jsonObj.get("contexts").isJsonNull()) {
        List.validateJsonElement(jsonObj.get("contexts"));
      }
      // validate the required field `createdAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("createdAt"));
      // validate the required field `createdReason`
      String.validateJsonElement(jsonObj.get("createdReason"));
      // validate the required field `id`
      String.validateJsonElement(jsonObj.get("id"));
      // validate the optional field `resolvedAt`
      if (jsonObj.get("resolvedAt") != null && !jsonObj.get("resolvedAt").isJsonNull()) {
        OffsetDateTime.validateJsonElement(jsonObj.get("resolvedAt"));
      }
      // validate the optional field `resolvedReason`
      if (jsonObj.get("resolvedReason") != null && !jsonObj.get("resolvedReason").isJsonNull()) {
        String.validateJsonElement(jsonObj.get("resolvedReason"));
      }
      // validate the required field `status`
      BlockerStatus.validateJsonElement(jsonObj.get("status"));
      // validate the required field `type`
      BlockerType.validateJsonElement(jsonObj.get("type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateServiceSyncBlockerOutputServiceSyncBlocker.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateServiceSyncBlockerOutputServiceSyncBlocker' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateServiceSyncBlockerOutputServiceSyncBlocker> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateServiceSyncBlockerOutputServiceSyncBlocker.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateServiceSyncBlockerOutputServiceSyncBlocker>() {
           @Override
           public void write(JsonWriter out, UpdateServiceSyncBlockerOutputServiceSyncBlocker value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateServiceSyncBlockerOutputServiceSyncBlocker read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateServiceSyncBlockerOutputServiceSyncBlocker given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateServiceSyncBlockerOutputServiceSyncBlocker
   * @throws IOException if the JSON string is invalid with respect to UpdateServiceSyncBlockerOutputServiceSyncBlocker
   */
  public static UpdateServiceSyncBlockerOutputServiceSyncBlocker fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateServiceSyncBlockerOutputServiceSyncBlocker.class);
  }

  /**
   * Convert an instance of UpdateServiceSyncBlockerOutputServiceSyncBlocker to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

