/*
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
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
import org.openapitools.client.model.HIUSubscriptionNotificationAcknowledgmentAcknowledgement;
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
 * HIUSubscriptionNotificationAcknowledgment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:36.866529-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HIUSubscriptionNotificationAcknowledgment {
  public static final String SERIALIZED_NAME_ACKNOWLEDGEMENT = "acknowledgement";
  @SerializedName(SERIALIZED_NAME_ACKNOWLEDGEMENT)
  private HIUSubscriptionNotificationAcknowledgmentAcknowledgement acknowledgement;

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

  public HIUSubscriptionNotificationAcknowledgment() {
  }

  public HIUSubscriptionNotificationAcknowledgment acknowledgement(HIUSubscriptionNotificationAcknowledgmentAcknowledgement acknowledgement) {
    this.acknowledgement = acknowledgement;
    return this;
  }

  /**
   * Get acknowledgement
   * @return acknowledgement
   */
  @javax.annotation.Nullable
  public HIUSubscriptionNotificationAcknowledgmentAcknowledgement getAcknowledgement() {
    return acknowledgement;
  }

  public void setAcknowledgement(HIUSubscriptionNotificationAcknowledgmentAcknowledgement acknowledgement) {
    this.acknowledgement = acknowledgement;
  }


  public HIUSubscriptionNotificationAcknowledgment error(Error error) {
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


  public HIUSubscriptionNotificationAcknowledgment requestId(UUID requestId) {
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


  public HIUSubscriptionNotificationAcknowledgment resp(RequestReference resp) {
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


  public HIUSubscriptionNotificationAcknowledgment timestamp(OffsetDateTime timestamp) {
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
    HIUSubscriptionNotificationAcknowledgment hiUSubscriptionNotificationAcknowledgment = (HIUSubscriptionNotificationAcknowledgment) o;
    return Objects.equals(this.acknowledgement, hiUSubscriptionNotificationAcknowledgment.acknowledgement) &&
        Objects.equals(this.error, hiUSubscriptionNotificationAcknowledgment.error) &&
        Objects.equals(this.requestId, hiUSubscriptionNotificationAcknowledgment.requestId) &&
        Objects.equals(this.resp, hiUSubscriptionNotificationAcknowledgment.resp) &&
        Objects.equals(this.timestamp, hiUSubscriptionNotificationAcknowledgment.timestamp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(acknowledgement, error, requestId, resp, timestamp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HIUSubscriptionNotificationAcknowledgment {\n");
    sb.append("    acknowledgement: ").append(toIndentedString(acknowledgement)).append("\n");
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
    openapiFields.add("acknowledgement");
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
   * @throws IOException if the JSON Element is invalid with respect to HIUSubscriptionNotificationAcknowledgment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HIUSubscriptionNotificationAcknowledgment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HIUSubscriptionNotificationAcknowledgment is not found in the empty JSON string", HIUSubscriptionNotificationAcknowledgment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HIUSubscriptionNotificationAcknowledgment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HIUSubscriptionNotificationAcknowledgment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HIUSubscriptionNotificationAcknowledgment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `acknowledgement`
      if (jsonObj.get("acknowledgement") != null && !jsonObj.get("acknowledgement").isJsonNull()) {
        HIUSubscriptionNotificationAcknowledgmentAcknowledgement.validateJsonElement(jsonObj.get("acknowledgement"));
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
       if (!HIUSubscriptionNotificationAcknowledgment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HIUSubscriptionNotificationAcknowledgment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HIUSubscriptionNotificationAcknowledgment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HIUSubscriptionNotificationAcknowledgment.class));

       return (TypeAdapter<T>) new TypeAdapter<HIUSubscriptionNotificationAcknowledgment>() {
           @Override
           public void write(JsonWriter out, HIUSubscriptionNotificationAcknowledgment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HIUSubscriptionNotificationAcknowledgment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HIUSubscriptionNotificationAcknowledgment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HIUSubscriptionNotificationAcknowledgment
   * @throws IOException if the JSON string is invalid with respect to HIUSubscriptionNotificationAcknowledgment
   */
  public static HIUSubscriptionNotificationAcknowledgment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HIUSubscriptionNotificationAcknowledgment.class);
  }

  /**
   * Convert an instance of HIUSubscriptionNotificationAcknowledgment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

