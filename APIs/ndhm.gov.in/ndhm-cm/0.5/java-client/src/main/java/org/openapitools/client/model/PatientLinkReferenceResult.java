/*
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
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
import org.openapitools.client.model.PatientLinkReferenceResultLink;
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
 * PatientLinkReferenceResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:38.835611-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientLinkReferenceResult {
  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private Error error;

  public static final String SERIALIZED_NAME_LINK = "link";
  @SerializedName(SERIALIZED_NAME_LINK)
  private PatientLinkReferenceResultLink link;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private UUID requestId;

  public static final String SERIALIZED_NAME_RESP = "resp";
  @SerializedName(SERIALIZED_NAME_RESP)
  private RequestReference resp;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private OffsetDateTime timestamp;

  public static final String SERIALIZED_NAME_TRANSACTION_ID = "transactionId";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_ID)
  private UUID transactionId;

  public PatientLinkReferenceResult() {
  }

  public PatientLinkReferenceResult error(Error error) {
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


  public PatientLinkReferenceResult link(PatientLinkReferenceResultLink link) {
    this.link = link;
    return this;
  }

  /**
   * Get link
   * @return link
   */
  @javax.annotation.Nullable
  public PatientLinkReferenceResultLink getLink() {
    return link;
  }

  public void setLink(PatientLinkReferenceResultLink link) {
    this.link = link;
  }


  public PatientLinkReferenceResult requestId(UUID requestId) {
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


  public PatientLinkReferenceResult resp(RequestReference resp) {
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


  public PatientLinkReferenceResult timestamp(OffsetDateTime timestamp) {
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


  public PatientLinkReferenceResult transactionId(UUID transactionId) {
    this.transactionId = transactionId;
    return this;
  }

  /**
   * Get transactionId
   * @return transactionId
   */
  @javax.annotation.Nonnull
  public UUID getTransactionId() {
    return transactionId;
  }

  public void setTransactionId(UUID transactionId) {
    this.transactionId = transactionId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientLinkReferenceResult patientLinkReferenceResult = (PatientLinkReferenceResult) o;
    return Objects.equals(this.error, patientLinkReferenceResult.error) &&
        Objects.equals(this.link, patientLinkReferenceResult.link) &&
        Objects.equals(this.requestId, patientLinkReferenceResult.requestId) &&
        Objects.equals(this.resp, patientLinkReferenceResult.resp) &&
        Objects.equals(this.timestamp, patientLinkReferenceResult.timestamp) &&
        Objects.equals(this.transactionId, patientLinkReferenceResult.transactionId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(error, link, requestId, resp, timestamp, transactionId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientLinkReferenceResult {\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    link: ").append(toIndentedString(link)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
    sb.append("    resp: ").append(toIndentedString(resp)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
    sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
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
    openapiFields.add("error");
    openapiFields.add("link");
    openapiFields.add("requestId");
    openapiFields.add("resp");
    openapiFields.add("timestamp");
    openapiFields.add("transactionId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("requestId");
    openapiRequiredFields.add("resp");
    openapiRequiredFields.add("timestamp");
    openapiRequiredFields.add("transactionId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientLinkReferenceResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientLinkReferenceResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientLinkReferenceResult is not found in the empty JSON string", PatientLinkReferenceResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientLinkReferenceResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientLinkReferenceResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientLinkReferenceResult.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `error`
      if (jsonObj.get("error") != null && !jsonObj.get("error").isJsonNull()) {
        Error.validateJsonElement(jsonObj.get("error"));
      }
      // validate the optional field `link`
      if (jsonObj.get("link") != null && !jsonObj.get("link").isJsonNull()) {
        PatientLinkReferenceResultLink.validateJsonElement(jsonObj.get("link"));
      }
      if (!jsonObj.get("requestId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestId").toString()));
      }
      // validate the required field `resp`
      RequestReference.validateJsonElement(jsonObj.get("resp"));
      if (!jsonObj.get("transactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactionId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientLinkReferenceResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientLinkReferenceResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientLinkReferenceResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientLinkReferenceResult.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientLinkReferenceResult>() {
           @Override
           public void write(JsonWriter out, PatientLinkReferenceResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientLinkReferenceResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientLinkReferenceResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientLinkReferenceResult
   * @throws IOException if the JSON string is invalid with respect to PatientLinkReferenceResult
   */
  public static PatientLinkReferenceResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientLinkReferenceResult.class);
  }

  /**
   * Convert an instance of PatientLinkReferenceResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

