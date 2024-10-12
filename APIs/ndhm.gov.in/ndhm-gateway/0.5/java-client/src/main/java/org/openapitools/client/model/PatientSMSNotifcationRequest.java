/*
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 * 
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
import java.util.UUID;
import org.openapitools.client.model.PatientSMSNotifcationRequestNotification;

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
 * PatientSMSNotifcationRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:45.290770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientSMSNotifcationRequest {
  public static final String SERIALIZED_NAME_NOTIFICATION = "notification";
  @SerializedName(SERIALIZED_NAME_NOTIFICATION)
  private PatientSMSNotifcationRequestNotification notification;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private UUID requestId;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private OffsetDateTime timestamp;

  public PatientSMSNotifcationRequest() {
  }

  public PatientSMSNotifcationRequest notification(PatientSMSNotifcationRequestNotification notification) {
    this.notification = notification;
    return this;
  }

  /**
   * Get notification
   * @return notification
   */
  @javax.annotation.Nonnull
  public PatientSMSNotifcationRequestNotification getNotification() {
    return notification;
  }

  public void setNotification(PatientSMSNotifcationRequestNotification notification) {
    this.notification = notification;
  }


  public PatientSMSNotifcationRequest requestId(UUID requestId) {
    this.requestId = requestId;
    return this;
  }

  /**
   * a nonce, unique for each HTTP request
   * @return requestId
   */
  @javax.annotation.Nonnull
  public UUID getRequestId() {
    return requestId;
  }

  public void setRequestId(UUID requestId) {
    this.requestId = requestId;
  }


  public PatientSMSNotifcationRequest timestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
    return this;
  }

  /**
   * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
   * @return timestamp
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getTimestamp() {
    return timestamp;
  }

  public void setTimestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientSMSNotifcationRequest patientSMSNotifcationRequest = (PatientSMSNotifcationRequest) o;
    return Objects.equals(this.notification, patientSMSNotifcationRequest.notification) &&
        Objects.equals(this.requestId, patientSMSNotifcationRequest.requestId) &&
        Objects.equals(this.timestamp, patientSMSNotifcationRequest.timestamp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(notification, requestId, timestamp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientSMSNotifcationRequest {\n");
    sb.append("    notification: ").append(toIndentedString(notification)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
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
    openapiFields.add("notification");
    openapiFields.add("requestId");
    openapiFields.add("timestamp");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("notification");
    openapiRequiredFields.add("requestId");
    openapiRequiredFields.add("timestamp");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientSMSNotifcationRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientSMSNotifcationRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientSMSNotifcationRequest is not found in the empty JSON string", PatientSMSNotifcationRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientSMSNotifcationRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientSMSNotifcationRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientSMSNotifcationRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `notification`
      PatientSMSNotifcationRequestNotification.validateJsonElement(jsonObj.get("notification"));
      if (!jsonObj.get("requestId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientSMSNotifcationRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientSMSNotifcationRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientSMSNotifcationRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientSMSNotifcationRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientSMSNotifcationRequest>() {
           @Override
           public void write(JsonWriter out, PatientSMSNotifcationRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientSMSNotifcationRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientSMSNotifcationRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientSMSNotifcationRequest
   * @throws IOException if the JSON string is invalid with respect to PatientSMSNotifcationRequest
   */
  public static PatientSMSNotifcationRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientSMSNotifcationRequest.class);
  }

  /**
   * Convert an instance of PatientSMSNotifcationRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

