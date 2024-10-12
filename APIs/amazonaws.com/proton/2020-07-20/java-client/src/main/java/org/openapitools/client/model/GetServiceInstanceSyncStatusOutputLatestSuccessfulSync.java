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
import org.openapitools.client.model.ResourceSyncAttemptInitialRevision;
import org.openapitools.client.model.ResourceSyncAttemptTargetRevision;
import org.openapitools.client.model.ResourceSyncStatus;

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
 * GetServiceInstanceSyncStatusOutputLatestSuccessfulSync
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:26:35.899404-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetServiceInstanceSyncStatusOutputLatestSuccessfulSync {
  public static final String SERIALIZED_NAME_EVENTS = "events";
  @SerializedName(SERIALIZED_NAME_EVENTS)
  private List events;

  public static final String SERIALIZED_NAME_INITIAL_REVISION = "initialRevision";
  @SerializedName(SERIALIZED_NAME_INITIAL_REVISION)
  private ResourceSyncAttemptInitialRevision initialRevision;

  public static final String SERIALIZED_NAME_STARTED_AT = "startedAt";
  @SerializedName(SERIALIZED_NAME_STARTED_AT)
  private OffsetDateTime startedAt;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private ResourceSyncStatus status;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public static final String SERIALIZED_NAME_TARGET_REVISION = "targetRevision";
  @SerializedName(SERIALIZED_NAME_TARGET_REVISION)
  private ResourceSyncAttemptTargetRevision targetRevision;

  public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync() {
  }

  public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync events(List events) {
    this.events = events;
    return this;
  }

  /**
   * Get events
   * @return events
   */
  @javax.annotation.Nonnull
  public List getEvents() {
    return events;
  }

  public void setEvents(List events) {
    this.events = events;
  }


  public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync initialRevision(ResourceSyncAttemptInitialRevision initialRevision) {
    this.initialRevision = initialRevision;
    return this;
  }

  /**
   * Get initialRevision
   * @return initialRevision
   */
  @javax.annotation.Nonnull
  public ResourceSyncAttemptInitialRevision getInitialRevision() {
    return initialRevision;
  }

  public void setInitialRevision(ResourceSyncAttemptInitialRevision initialRevision) {
    this.initialRevision = initialRevision;
  }


  public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync startedAt(OffsetDateTime startedAt) {
    this.startedAt = startedAt;
    return this;
  }

  /**
   * Get startedAt
   * @return startedAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getStartedAt() {
    return startedAt;
  }

  public void setStartedAt(OffsetDateTime startedAt) {
    this.startedAt = startedAt;
  }


  public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync status(ResourceSyncStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public ResourceSyncStatus getStatus() {
    return status;
  }

  public void setStatus(ResourceSyncStatus status) {
    this.status = status;
  }


  public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync target(String target) {
    this.target = target;
    return this;
  }

  /**
   * Get target
   * @return target
   */
  @javax.annotation.Nonnull
  public String getTarget() {
    return target;
  }

  public void setTarget(String target) {
    this.target = target;
  }


  public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync targetRevision(ResourceSyncAttemptTargetRevision targetRevision) {
    this.targetRevision = targetRevision;
    return this;
  }

  /**
   * Get targetRevision
   * @return targetRevision
   */
  @javax.annotation.Nonnull
  public ResourceSyncAttemptTargetRevision getTargetRevision() {
    return targetRevision;
  }

  public void setTargetRevision(ResourceSyncAttemptTargetRevision targetRevision) {
    this.targetRevision = targetRevision;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetServiceInstanceSyncStatusOutputLatestSuccessfulSync getServiceInstanceSyncStatusOutputLatestSuccessfulSync = (GetServiceInstanceSyncStatusOutputLatestSuccessfulSync) o;
    return Objects.equals(this.events, getServiceInstanceSyncStatusOutputLatestSuccessfulSync.events) &&
        Objects.equals(this.initialRevision, getServiceInstanceSyncStatusOutputLatestSuccessfulSync.initialRevision) &&
        Objects.equals(this.startedAt, getServiceInstanceSyncStatusOutputLatestSuccessfulSync.startedAt) &&
        Objects.equals(this.status, getServiceInstanceSyncStatusOutputLatestSuccessfulSync.status) &&
        Objects.equals(this.target, getServiceInstanceSyncStatusOutputLatestSuccessfulSync.target) &&
        Objects.equals(this.targetRevision, getServiceInstanceSyncStatusOutputLatestSuccessfulSync.targetRevision);
  }

  @Override
  public int hashCode() {
    return Objects.hash(events, initialRevision, startedAt, status, target, targetRevision);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetServiceInstanceSyncStatusOutputLatestSuccessfulSync {\n");
    sb.append("    events: ").append(toIndentedString(events)).append("\n");
    sb.append("    initialRevision: ").append(toIndentedString(initialRevision)).append("\n");
    sb.append("    startedAt: ").append(toIndentedString(startedAt)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
    sb.append("    targetRevision: ").append(toIndentedString(targetRevision)).append("\n");
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
    openapiFields.add("events");
    openapiFields.add("initialRevision");
    openapiFields.add("startedAt");
    openapiFields.add("status");
    openapiFields.add("target");
    openapiFields.add("targetRevision");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("events");
    openapiRequiredFields.add("initialRevision");
    openapiRequiredFields.add("startedAt");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("target");
    openapiRequiredFields.add("targetRevision");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetServiceInstanceSyncStatusOutputLatestSuccessfulSync
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetServiceInstanceSyncStatusOutputLatestSuccessfulSync is not found in the empty JSON string", GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetServiceInstanceSyncStatusOutputLatestSuccessfulSync` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `events`
      List.validateJsonElement(jsonObj.get("events"));
      // validate the required field `initialRevision`
      ResourceSyncAttemptInitialRevision.validateJsonElement(jsonObj.get("initialRevision"));
      // validate the required field `startedAt`
      OffsetDateTime.validateJsonElement(jsonObj.get("startedAt"));
      // validate the required field `status`
      ResourceSyncStatus.validateJsonElement(jsonObj.get("status"));
      // validate the required field `target`
      String.validateJsonElement(jsonObj.get("target"));
      // validate the required field `targetRevision`
      ResourceSyncAttemptTargetRevision.validateJsonElement(jsonObj.get("targetRevision"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetServiceInstanceSyncStatusOutputLatestSuccessfulSync' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetServiceInstanceSyncStatusOutputLatestSuccessfulSync> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.class));

       return (TypeAdapter<T>) new TypeAdapter<GetServiceInstanceSyncStatusOutputLatestSuccessfulSync>() {
           @Override
           public void write(JsonWriter out, GetServiceInstanceSyncStatusOutputLatestSuccessfulSync value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetServiceInstanceSyncStatusOutputLatestSuccessfulSync read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetServiceInstanceSyncStatusOutputLatestSuccessfulSync given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetServiceInstanceSyncStatusOutputLatestSuccessfulSync
   * @throws IOException if the JSON string is invalid with respect to GetServiceInstanceSyncStatusOutputLatestSuccessfulSync
   */
  public static GetServiceInstanceSyncStatusOutputLatestSuccessfulSync fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetServiceInstanceSyncStatusOutputLatestSuccessfulSync.class);
  }

  /**
   * Convert an instance of GetServiceInstanceSyncStatusOutputLatestSuccessfulSync to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

