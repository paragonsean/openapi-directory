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
import org.openapitools.client.model.Error;
import org.openapitools.client.model.HIUConsentRequestStatusConsentRequest;
import org.openapitools.client.model.RequestReference;

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
 * HIUConsentRequestStatus
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:45.290770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HIUConsentRequestStatus {
  public static final String SERIALIZED_NAME_CONSENT_REQUEST = "consentRequest";
  @SerializedName(SERIALIZED_NAME_CONSENT_REQUEST)
  private HIUConsentRequestStatusConsentRequest consentRequest;

  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private Error error;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private UUID requestId;

  public static final String SERIALIZED_NAME_RESP = "resp";
  @SerializedName(SERIALIZED_NAME_RESP)
  private RequestReference resp;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private OffsetDateTime timestamp;

  public HIUConsentRequestStatus() {
  }

  public HIUConsentRequestStatus consentRequest(HIUConsentRequestStatusConsentRequest consentRequest) {
    this.consentRequest = consentRequest;
    return this;
  }

  /**
   * Get consentRequest
   * @return consentRequest
   */
  @javax.annotation.Nullable
  public HIUConsentRequestStatusConsentRequest getConsentRequest() {
    return consentRequest;
  }

  public void setConsentRequest(HIUConsentRequestStatusConsentRequest consentRequest) {
    this.consentRequest = consentRequest;
  }


  public HIUConsentRequestStatus error(Error error) {
    this.error = error;
    return this;
  }

  /**
   * Get error
   * @return error
   */
  @javax.annotation.Nullable
  public Error getError() {
    return error;
  }

  public void setError(Error error) {
    this.error = error;
  }


  public HIUConsentRequestStatus requestId(UUID requestId) {
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


  public HIUConsentRequestStatus resp(RequestReference resp) {
    this.resp = resp;
    return this;
  }

  /**
   * Get resp
   * @return resp
   */
  @javax.annotation.Nonnull
  public RequestReference getResp() {
    return resp;
  }

  public void setResp(RequestReference resp) {
    this.resp = resp;
  }


  public HIUConsentRequestStatus timestamp(OffsetDateTime timestamp) {
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
    HIUConsentRequestStatus hiUConsentRequestStatus = (HIUConsentRequestStatus) o;
    return Objects.equals(this.consentRequest, hiUConsentRequestStatus.consentRequest) &&
        Objects.equals(this.error, hiUConsentRequestStatus.error) &&
        Objects.equals(this.requestId, hiUConsentRequestStatus.requestId) &&
        Objects.equals(this.resp, hiUConsentRequestStatus.resp) &&
        Objects.equals(this.timestamp, hiUConsentRequestStatus.timestamp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consentRequest, error, requestId, resp, timestamp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HIUConsentRequestStatus {\n");
    sb.append("    consentRequest: ").append(toIndentedString(consentRequest)).append("\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    resp: ").append(toIndentedString(resp)).append("\n");
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
    openapiFields.add("consentRequest");
    openapiFields.add("error");
    openapiFields.add("requestId");
    openapiFields.add("resp");
    openapiFields.add("timestamp");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("requestId");
    openapiRequiredFields.add("resp");
    openapiRequiredFields.add("timestamp");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HIUConsentRequestStatus
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HIUConsentRequestStatus.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HIUConsentRequestStatus is not found in the empty JSON string", HIUConsentRequestStatus.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HIUConsentRequestStatus.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HIUConsentRequestStatus` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HIUConsentRequestStatus.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `consentRequest`
      if (jsonObj.get("consentRequest") != null && !jsonObj.get("consentRequest").isJsonNull()) {
        HIUConsentRequestStatusConsentRequest.validateJsonElement(jsonObj.get("consentRequest"));
      }
      // validate the optional field `error`
      if (jsonObj.get("error") != null && !jsonObj.get("error").isJsonNull()) {
        Error.validateJsonElement(jsonObj.get("error"));
      }
      if (!jsonObj.get("requestId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestId").toString()));
      }
      // validate the required field `resp`
      RequestReference.validateJsonElement(jsonObj.get("resp"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HIUConsentRequestStatus.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HIUConsentRequestStatus' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HIUConsentRequestStatus> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HIUConsentRequestStatus.class));

       return (TypeAdapter<T>) new TypeAdapter<HIUConsentRequestStatus>() {
           @Override
           public void write(JsonWriter out, HIUConsentRequestStatus value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HIUConsentRequestStatus read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HIUConsentRequestStatus given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HIUConsentRequestStatus
   * @throws IOException if the JSON string is invalid with respect to HIUConsentRequestStatus
   */
  public static HIUConsentRequestStatus fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HIUConsentRequestStatus.class);
  }

  /**
   * Convert an instance of HIUConsentRequestStatus to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

