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
import org.openapitools.client.model.HIPHealthInformationRequestAcknowledgementHiRequest;
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
 * HIPHealthInformationRequestAcknowledgement
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:45.290770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HIPHealthInformationRequestAcknowledgement {
  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private Error error;

  public static final String SERIALIZED_NAME_HI_REQUEST = "hiRequest";
  @SerializedName(SERIALIZED_NAME_HI_REQUEST)
  private HIPHealthInformationRequestAcknowledgementHiRequest hiRequest;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private UUID requestId;

  public static final String SERIALIZED_NAME_RESP = "resp";
  @SerializedName(SERIALIZED_NAME_RESP)
  private RequestReference resp;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private OffsetDateTime timestamp;

  public HIPHealthInformationRequestAcknowledgement() {
  }

  public HIPHealthInformationRequestAcknowledgement error(Error error) {
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


  public HIPHealthInformationRequestAcknowledgement hiRequest(HIPHealthInformationRequestAcknowledgementHiRequest hiRequest) {
    this.hiRequest = hiRequest;
    return this;
  }

  /**
   * Get hiRequest
   * @return hiRequest
   */
  @javax.annotation.Nullable
  public HIPHealthInformationRequestAcknowledgementHiRequest getHiRequest() {
    return hiRequest;
  }

  public void setHiRequest(HIPHealthInformationRequestAcknowledgementHiRequest hiRequest) {
    this.hiRequest = hiRequest;
  }


  public HIPHealthInformationRequestAcknowledgement requestId(UUID requestId) {
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


  public HIPHealthInformationRequestAcknowledgement resp(RequestReference resp) {
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


  public HIPHealthInformationRequestAcknowledgement timestamp(OffsetDateTime timestamp) {
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
    HIPHealthInformationRequestAcknowledgement hiPHealthInformationRequestAcknowledgement = (HIPHealthInformationRequestAcknowledgement) o;
    return Objects.equals(this.error, hiPHealthInformationRequestAcknowledgement.error) &&
        Objects.equals(this.hiRequest, hiPHealthInformationRequestAcknowledgement.hiRequest) &&
        Objects.equals(this.requestId, hiPHealthInformationRequestAcknowledgement.requestId) &&
        Objects.equals(this.resp, hiPHealthInformationRequestAcknowledgement.resp) &&
        Objects.equals(this.timestamp, hiPHealthInformationRequestAcknowledgement.timestamp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(error, hiRequest, requestId, resp, timestamp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HIPHealthInformationRequestAcknowledgement {\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    hiRequest: ").append(toIndentedString(hiRequest)).append("\n");
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
    openapiFields.add("error");
    openapiFields.add("hiRequest");
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
   * @throws IOException if the JSON Element is invalid with respect to HIPHealthInformationRequestAcknowledgement
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HIPHealthInformationRequestAcknowledgement.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HIPHealthInformationRequestAcknowledgement is not found in the empty JSON string", HIPHealthInformationRequestAcknowledgement.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HIPHealthInformationRequestAcknowledgement.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HIPHealthInformationRequestAcknowledgement` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : HIPHealthInformationRequestAcknowledgement.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `error`
      if (jsonObj.get("error") != null && !jsonObj.get("error").isJsonNull()) {
        Error.validateJsonElement(jsonObj.get("error"));
      }
      // validate the optional field `hiRequest`
      if (jsonObj.get("hiRequest") != null && !jsonObj.get("hiRequest").isJsonNull()) {
        HIPHealthInformationRequestAcknowledgementHiRequest.validateJsonElement(jsonObj.get("hiRequest"));
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
       if (!HIPHealthInformationRequestAcknowledgement.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HIPHealthInformationRequestAcknowledgement' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HIPHealthInformationRequestAcknowledgement> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HIPHealthInformationRequestAcknowledgement.class));

       return (TypeAdapter<T>) new TypeAdapter<HIPHealthInformationRequestAcknowledgement>() {
           @Override
           public void write(JsonWriter out, HIPHealthInformationRequestAcknowledgement value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HIPHealthInformationRequestAcknowledgement read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HIPHealthInformationRequestAcknowledgement given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HIPHealthInformationRequestAcknowledgement
   * @throws IOException if the JSON string is invalid with respect to HIPHealthInformationRequestAcknowledgement
   */
  public static HIPHealthInformationRequestAcknowledgement fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HIPHealthInformationRequestAcknowledgement.class);
  }

  /**
   * Convert an instance of HIPHealthInformationRequestAcknowledgement to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

