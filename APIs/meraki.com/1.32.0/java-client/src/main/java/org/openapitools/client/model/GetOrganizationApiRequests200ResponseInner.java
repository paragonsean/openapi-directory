/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * GetOrganizationApiRequests200ResponseInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationApiRequests200ResponseInner {
  public static final String SERIALIZED_NAME_ADMIN_ID = "adminId";
  @SerializedName(SERIALIZED_NAME_ADMIN_ID)
  private String adminId;

  public static final String SERIALIZED_NAME_HOST = "host";
  @SerializedName(SERIALIZED_NAME_HOST)
  private String host;

  public static final String SERIALIZED_NAME_METHOD = "method";
  @SerializedName(SERIALIZED_NAME_METHOD)
  private String method;

  public static final String SERIALIZED_NAME_OPERATION_ID = "operationId";
  @SerializedName(SERIALIZED_NAME_OPERATION_ID)
  private String operationId;

  public static final String SERIALIZED_NAME_PATH = "path";
  @SerializedName(SERIALIZED_NAME_PATH)
  private String path;

  public static final String SERIALIZED_NAME_QUERY_STRING = "queryString";
  @SerializedName(SERIALIZED_NAME_QUERY_STRING)
  private String queryString;

  public static final String SERIALIZED_NAME_RESPONSE_CODE = "responseCode";
  @SerializedName(SERIALIZED_NAME_RESPONSE_CODE)
  private Integer responseCode;

  public static final String SERIALIZED_NAME_SOURCE_IP = "sourceIp";
  @SerializedName(SERIALIZED_NAME_SOURCE_IP)
  private String sourceIp;

  public static final String SERIALIZED_NAME_TS = "ts";
  @SerializedName(SERIALIZED_NAME_TS)
  private OffsetDateTime ts;

  public static final String SERIALIZED_NAME_USER_AGENT = "userAgent";
  @SerializedName(SERIALIZED_NAME_USER_AGENT)
  private String userAgent;

  /**
   * API version of the endpoint.
   */
  @JsonAdapter(VersionEnum.Adapter.class)
  public enum VersionEnum {
    NUMBER_0(0),
    
    NUMBER_1(1);

    private Integer value;

    VersionEnum(Integer value) {
      this.value = value;
    }

    public Integer getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static VersionEnum fromValue(Integer value) {
      for (VersionEnum b : VersionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<VersionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final VersionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public VersionEnum read(final JsonReader jsonReader) throws IOException {
        Integer value =  jsonReader.nextInt();
        return VersionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      Integer value = jsonElement.getAsInt();
      VersionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private VersionEnum version;

  public GetOrganizationApiRequests200ResponseInner() {
  }

  public GetOrganizationApiRequests200ResponseInner adminId(String adminId) {
    this.adminId = adminId;
    return this;
  }

  /**
   * Database ID for the admin user who made the API request.
   * @return adminId
   */
  @javax.annotation.Nullable
  public String getAdminId() {
    return adminId;
  }

  public void setAdminId(String adminId) {
    this.adminId = adminId;
  }


  public GetOrganizationApiRequests200ResponseInner host(String host) {
    this.host = host;
    return this;
  }

  /**
   * The host which the API request was directed at.
   * @return host
   */
  @javax.annotation.Nullable
  public String getHost() {
    return host;
  }

  public void setHost(String host) {
    this.host = host;
  }


  public GetOrganizationApiRequests200ResponseInner method(String method) {
    this.method = method;
    return this;
  }

  /**
   * HTTP method used in the API request.
   * @return method
   */
  @javax.annotation.Nullable
  public String getMethod() {
    return method;
  }

  public void setMethod(String method) {
    this.method = method;
  }


  public GetOrganizationApiRequests200ResponseInner operationId(String operationId) {
    this.operationId = operationId;
    return this;
  }

  /**
   * Operation ID for the endpoint.
   * @return operationId
   */
  @javax.annotation.Nullable
  public String getOperationId() {
    return operationId;
  }

  public void setOperationId(String operationId) {
    this.operationId = operationId;
  }


  public GetOrganizationApiRequests200ResponseInner path(String path) {
    this.path = path;
    return this;
  }

  /**
   * The API request path.
   * @return path
   */
  @javax.annotation.Nullable
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  public GetOrganizationApiRequests200ResponseInner queryString(String queryString) {
    this.queryString = queryString;
    return this;
  }

  /**
   * The query string sent with the API request.
   * @return queryString
   */
  @javax.annotation.Nullable
  public String getQueryString() {
    return queryString;
  }

  public void setQueryString(String queryString) {
    this.queryString = queryString;
  }


  public GetOrganizationApiRequests200ResponseInner responseCode(Integer responseCode) {
    this.responseCode = responseCode;
    return this;
  }

  /**
   * API request response code.
   * @return responseCode
   */
  @javax.annotation.Nullable
  public Integer getResponseCode() {
    return responseCode;
  }

  public void setResponseCode(Integer responseCode) {
    this.responseCode = responseCode;
  }


  public GetOrganizationApiRequests200ResponseInner sourceIp(String sourceIp) {
    this.sourceIp = sourceIp;
    return this;
  }

  /**
   * Public IP address from which the API request was made.
   * @return sourceIp
   */
  @javax.annotation.Nullable
  public String getSourceIp() {
    return sourceIp;
  }

  public void setSourceIp(String sourceIp) {
    this.sourceIp = sourceIp;
  }


  public GetOrganizationApiRequests200ResponseInner ts(OffsetDateTime ts) {
    this.ts = ts;
    return this;
  }

  /**
   * Timestamp, in iso8601 format, indicating when the API request was made.
   * @return ts
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTs() {
    return ts;
  }

  public void setTs(OffsetDateTime ts) {
    this.ts = ts;
  }


  public GetOrganizationApiRequests200ResponseInner userAgent(String userAgent) {
    this.userAgent = userAgent;
    return this;
  }

  /**
   * The API request user agent.
   * @return userAgent
   */
  @javax.annotation.Nullable
  public String getUserAgent() {
    return userAgent;
  }

  public void setUserAgent(String userAgent) {
    this.userAgent = userAgent;
  }


  public GetOrganizationApiRequests200ResponseInner version(VersionEnum version) {
    this.version = version;
    return this;
  }

  /**
   * API version of the endpoint.
   * @return version
   */
  @javax.annotation.Nullable
  public VersionEnum getVersion() {
    return version;
  }

  public void setVersion(VersionEnum version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationApiRequests200ResponseInner getOrganizationApiRequests200ResponseInner = (GetOrganizationApiRequests200ResponseInner) o;
    return Objects.equals(this.adminId, getOrganizationApiRequests200ResponseInner.adminId) &&
        Objects.equals(this.host, getOrganizationApiRequests200ResponseInner.host) &&
        Objects.equals(this.method, getOrganizationApiRequests200ResponseInner.method) &&
        Objects.equals(this.operationId, getOrganizationApiRequests200ResponseInner.operationId) &&
        Objects.equals(this.path, getOrganizationApiRequests200ResponseInner.path) &&
        Objects.equals(this.queryString, getOrganizationApiRequests200ResponseInner.queryString) &&
        Objects.equals(this.responseCode, getOrganizationApiRequests200ResponseInner.responseCode) &&
        Objects.equals(this.sourceIp, getOrganizationApiRequests200ResponseInner.sourceIp) &&
        Objects.equals(this.ts, getOrganizationApiRequests200ResponseInner.ts) &&
        Objects.equals(this.userAgent, getOrganizationApiRequests200ResponseInner.userAgent) &&
        Objects.equals(this.version, getOrganizationApiRequests200ResponseInner.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(adminId, host, method, operationId, path, queryString, responseCode, sourceIp, ts, userAgent, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationApiRequests200ResponseInner {\n");
    sb.append("    adminId: ").append(toIndentedString(adminId)).append("\n");
    sb.append("    host: ").append(toIndentedString(host)).append("\n");
    sb.append("    method: ").append(toIndentedString(method)).append("\n");
    sb.append("    operationId: ").append(toIndentedString(operationId)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    queryString: ").append(toIndentedString(queryString)).append("\n");
    sb.append("    responseCode: ").append(toIndentedString(responseCode)).append("\n");
    sb.append("    sourceIp: ").append(toIndentedString(sourceIp)).append("\n");
    sb.append("    ts: ").append(toIndentedString(ts)).append("\n");
    sb.append("    userAgent: ").append(toIndentedString(userAgent)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("adminId");
    openapiFields.add("host");
    openapiFields.add("method");
    openapiFields.add("operationId");
    openapiFields.add("path");
    openapiFields.add("queryString");
    openapiFields.add("responseCode");
    openapiFields.add("sourceIp");
    openapiFields.add("ts");
    openapiFields.add("userAgent");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationApiRequests200ResponseInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationApiRequests200ResponseInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationApiRequests200ResponseInner is not found in the empty JSON string", GetOrganizationApiRequests200ResponseInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationApiRequests200ResponseInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationApiRequests200ResponseInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("adminId") != null && !jsonObj.get("adminId").isJsonNull()) && !jsonObj.get("adminId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `adminId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("adminId").toString()));
      }
      if ((jsonObj.get("host") != null && !jsonObj.get("host").isJsonNull()) && !jsonObj.get("host").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `host` to be a primitive type in the JSON string but got `%s`", jsonObj.get("host").toString()));
      }
      if ((jsonObj.get("method") != null && !jsonObj.get("method").isJsonNull()) && !jsonObj.get("method").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `method` to be a primitive type in the JSON string but got `%s`", jsonObj.get("method").toString()));
      }
      if ((jsonObj.get("operationId") != null && !jsonObj.get("operationId").isJsonNull()) && !jsonObj.get("operationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `operationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("operationId").toString()));
      }
      if ((jsonObj.get("path") != null && !jsonObj.get("path").isJsonNull()) && !jsonObj.get("path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("path").toString()));
      }
      if ((jsonObj.get("queryString") != null && !jsonObj.get("queryString").isJsonNull()) && !jsonObj.get("queryString").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `queryString` to be a primitive type in the JSON string but got `%s`", jsonObj.get("queryString").toString()));
      }
      if ((jsonObj.get("sourceIp") != null && !jsonObj.get("sourceIp").isJsonNull()) && !jsonObj.get("sourceIp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceIp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceIp").toString()));
      }
      if ((jsonObj.get("userAgent") != null && !jsonObj.get("userAgent").isJsonNull()) && !jsonObj.get("userAgent").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userAgent` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userAgent").toString()));
      }
      // validate the optional field `version`
      if (jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) {
        VersionEnum.validateJsonElement(jsonObj.get("version"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationApiRequests200ResponseInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationApiRequests200ResponseInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationApiRequests200ResponseInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationApiRequests200ResponseInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationApiRequests200ResponseInner>() {
           @Override
           public void write(JsonWriter out, GetOrganizationApiRequests200ResponseInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationApiRequests200ResponseInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationApiRequests200ResponseInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationApiRequests200ResponseInner
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationApiRequests200ResponseInner
   */
  public static GetOrganizationApiRequests200ResponseInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationApiRequests200ResponseInner.class);
  }

  /**
   * Convert an instance of GetOrganizationApiRequests200ResponseInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

