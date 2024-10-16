/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import java.util.Arrays;

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
 * SubmitDsrOperationRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SubmitDsrOperationRequest {
  public static final String SERIALIZED_NAME_ACCOUNT_ID = "accountId";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_ID)
  private String accountId;

  public static final String SERIALIZED_NAME_APP_ID = "appId";
  @SerializedName(SERIALIZED_NAME_APP_ID)
  private String appId;

  public static final String SERIALIZED_NAME_OPERATION_ID = "operationId";
  @SerializedName(SERIALIZED_NAME_OPERATION_ID)
  private String operationId;

  /**
   * Gets or Sets request
   */
  @JsonAdapter(RequestEnum.Adapter.class)
  public enum RequestEnum {
    DELETE("Delete"),
    
    PURGE("Purge"),
    
    UNDO_DELETE("UndoDelete"),
    
    EXPORT("Export");

    private String value;

    RequestEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RequestEnum fromValue(String value) {
      for (RequestEnum b : RequestEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RequestEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RequestEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RequestEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RequestEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RequestEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REQUEST = "request";
  @SerializedName(SERIALIZED_NAME_REQUEST)
  private RequestEnum request;

  public static final String SERIALIZED_NAME_REQUEST_ID = "requestId";
  @SerializedName(SERIALIZED_NAME_REQUEST_ID)
  private String requestId;

  public SubmitDsrOperationRequest() {
  }

  public SubmitDsrOperationRequest accountId(String accountId) {
    this.accountId = accountId;
    return this;
  }

  /**
   * Get accountId
   * @return accountId
   */
  @javax.annotation.Nullable
  public String getAccountId() {
    return accountId;
  }

  public void setAccountId(String accountId) {
    this.accountId = accountId;
  }


  public SubmitDsrOperationRequest appId(String appId) {
    this.appId = appId;
    return this;
  }

  /**
   * Get appId
   * @return appId
   */
  @javax.annotation.Nullable
  public String getAppId() {
    return appId;
  }

  public void setAppId(String appId) {
    this.appId = appId;
  }


  public SubmitDsrOperationRequest operationId(String operationId) {
    this.operationId = operationId;
    return this;
  }

  /**
   * The DSR operation ID provided by the GDPR coordinator. Used for tracking only.
   * @return operationId
   */
  @javax.annotation.Nullable
  public String getOperationId() {
    return operationId;
  }

  public void setOperationId(String operationId) {
    this.operationId = operationId;
  }


  public SubmitDsrOperationRequest request(RequestEnum request) {
    this.request = request;
    return this;
  }

  /**
   * Get request
   * @return request
   */
  @javax.annotation.Nullable
  public RequestEnum getRequest() {
    return request;
  }

  public void setRequest(RequestEnum request) {
    this.request = request;
  }


  public SubmitDsrOperationRequest requestId(String requestId) {
    this.requestId = requestId;
    return this;
  }

  /**
   * Request ID provided by the GDPR coordinator. Used for tracking.
   * @return requestId
   */
  @javax.annotation.Nullable
  public String getRequestId() {
    return requestId;
  }

  public void setRequestId(String requestId) {
    this.requestId = requestId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SubmitDsrOperationRequest submitDsrOperationRequest = (SubmitDsrOperationRequest) o;
    return Objects.equals(this.accountId, submitDsrOperationRequest.accountId) &&
        Objects.equals(this.appId, submitDsrOperationRequest.appId) &&
        Objects.equals(this.operationId, submitDsrOperationRequest.operationId) &&
        Objects.equals(this.request, submitDsrOperationRequest.request) &&
        Objects.equals(this.requestId, submitDsrOperationRequest.requestId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountId, appId, operationId, request, requestId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SubmitDsrOperationRequest {\n");
    sb.append("    accountId: ").append(toIndentedString(accountId)).append("\n");
    sb.append("    appId: ").append(toIndentedString(appId)).append("\n");
    sb.append("    operationId: ").append(toIndentedString(operationId)).append("\n");
    sb.append("    request: ").append(toIndentedString(request)).append("\n");
    sb.append("    requestId: ").append(toIndentedString(requestId)).append("\n");
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
    openapiFields.add("accountId");
    openapiFields.add("appId");
    openapiFields.add("operationId");
    openapiFields.add("request");
    openapiFields.add("requestId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SubmitDsrOperationRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SubmitDsrOperationRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SubmitDsrOperationRequest is not found in the empty JSON string", SubmitDsrOperationRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SubmitDsrOperationRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SubmitDsrOperationRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("accountId") != null && !jsonObj.get("accountId").isJsonNull()) && !jsonObj.get("accountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountId").toString()));
      }
      if ((jsonObj.get("appId") != null && !jsonObj.get("appId").isJsonNull()) && !jsonObj.get("appId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appId").toString()));
      }
      if ((jsonObj.get("operationId") != null && !jsonObj.get("operationId").isJsonNull()) && !jsonObj.get("operationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `operationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("operationId").toString()));
      }
      if ((jsonObj.get("request") != null && !jsonObj.get("request").isJsonNull()) && !jsonObj.get("request").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `request` to be a primitive type in the JSON string but got `%s`", jsonObj.get("request").toString()));
      }
      // validate the optional field `request`
      if (jsonObj.get("request") != null && !jsonObj.get("request").isJsonNull()) {
        RequestEnum.validateJsonElement(jsonObj.get("request"));
      }
      if ((jsonObj.get("requestId") != null && !jsonObj.get("requestId").isJsonNull()) && !jsonObj.get("requestId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SubmitDsrOperationRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SubmitDsrOperationRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SubmitDsrOperationRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SubmitDsrOperationRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<SubmitDsrOperationRequest>() {
           @Override
           public void write(JsonWriter out, SubmitDsrOperationRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SubmitDsrOperationRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SubmitDsrOperationRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SubmitDsrOperationRequest
   * @throws IOException if the JSON string is invalid with respect to SubmitDsrOperationRequest
   */
  public static SubmitDsrOperationRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SubmitDsrOperationRequest.class);
  }

  /**
   * Convert an instance of SubmitDsrOperationRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

