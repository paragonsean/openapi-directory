/*
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Metadatum;

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
 * HTTPHealthCheck
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:51.953320-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HTTPHealthCheck {
  public static final String SERIALIZED_NAME_HOST = "host";
  @SerializedName(SERIALIZED_NAME_HOST)
  private String host;

  public static final String SERIALIZED_NAME_PATH = "path";
  @SerializedName(SERIALIZED_NAME_PATH)
  private String path;

  public static final String SERIALIZED_NAME_REQUEST_HEADERS_TO_ADD = "request_headers_to_add";
  @SerializedName(SERIALIZED_NAME_REQUEST_HEADERS_TO_ADD)
  private List<Metadatum> requestHeadersToAdd;

  public static final String SERIALIZED_NAME_SERVICE_NAME = "service_name";
  @SerializedName(SERIALIZED_NAME_SERVICE_NAME)
  private String serviceName;

  public HTTPHealthCheck() {
  }

  public HTTPHealthCheck host(String host) {
    this.host = host;
    return this;
  }

  /**
   * The value of the host header in the HTTP health check request. If left empty, the name of the cluster being health checked will be used. 
   * @return host
   */
  @javax.annotation.Nullable
  public String getHost() {
    return host;
  }

  public void setHost(String host) {
    this.host = host;
  }


  public HTTPHealthCheck path(String path) {
    this.path = path;
    return this;
  }

  /**
   * Specifies the HTTP path that will be requested during health checking. 
   * @return path
   */
  @javax.annotation.Nullable
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  public HTTPHealthCheck requestHeadersToAdd(List<Metadatum> requestHeadersToAdd) {
    this.requestHeadersToAdd = requestHeadersToAdd;
    return this;
  }

  public HTTPHealthCheck addRequestHeadersToAddItem(Metadatum requestHeadersToAddItem) {
    if (this.requestHeadersToAdd == null) {
      this.requestHeadersToAdd = new ArrayList<>();
    }
    this.requestHeadersToAdd.add(requestHeadersToAddItem);
    return this;
  }

  /**
   * Specifies a list of HTTP headers that should be added to each request sent to the health checked cluster. 
   * @return requestHeadersToAdd
   */
  @javax.annotation.Nullable
  public List<Metadatum> getRequestHeadersToAdd() {
    return requestHeadersToAdd;
  }

  public void setRequestHeadersToAdd(List<Metadatum> requestHeadersToAdd) {
    this.requestHeadersToAdd = requestHeadersToAdd;
  }


  public HTTPHealthCheck serviceName(String serviceName) {
    this.serviceName = serviceName;
    return this;
  }

  /**
   * An optional service name parameter which is used to validate the identity of the health checked cluster. 
   * @return serviceName
   */
  @javax.annotation.Nullable
  public String getServiceName() {
    return serviceName;
  }

  public void setServiceName(String serviceName) {
    this.serviceName = serviceName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HTTPHealthCheck htTPHealthCheck = (HTTPHealthCheck) o;
    return Objects.equals(this.host, htTPHealthCheck.host) &&
        Objects.equals(this.path, htTPHealthCheck.path) &&
        Objects.equals(this.requestHeadersToAdd, htTPHealthCheck.requestHeadersToAdd) &&
        Objects.equals(this.serviceName, htTPHealthCheck.serviceName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(host, path, requestHeadersToAdd, serviceName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HTTPHealthCheck {\n");
    sb.append("    host: ").append(toIndentedString(host)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    requestHeadersToAdd: ").append(toIndentedString(requestHeadersToAdd)).append("\n");
    sb.append("    serviceName: ").append(toIndentedString(serviceName)).append("\n");
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
    openapiFields.add("host");
    openapiFields.add("path");
    openapiFields.add("request_headers_to_add");
    openapiFields.add("service_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HTTPHealthCheck
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HTTPHealthCheck.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HTTPHealthCheck is not found in the empty JSON string", HTTPHealthCheck.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HTTPHealthCheck.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HTTPHealthCheck` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("host") != null && !jsonObj.get("host").isJsonNull()) && !jsonObj.get("host").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `host` to be a primitive type in the JSON string but got `%s`", jsonObj.get("host").toString()));
      }
      if ((jsonObj.get("path") != null && !jsonObj.get("path").isJsonNull()) && !jsonObj.get("path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("path").toString()));
      }
      if (jsonObj.get("request_headers_to_add") != null && !jsonObj.get("request_headers_to_add").isJsonNull()) {
        JsonArray jsonArrayrequestHeadersToAdd = jsonObj.getAsJsonArray("request_headers_to_add");
        if (jsonArrayrequestHeadersToAdd != null) {
          // ensure the json data is an array
          if (!jsonObj.get("request_headers_to_add").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `request_headers_to_add` to be an array in the JSON string but got `%s`", jsonObj.get("request_headers_to_add").toString()));
          }

          // validate the optional field `request_headers_to_add` (array)
          for (int i = 0; i < jsonArrayrequestHeadersToAdd.size(); i++) {
            Metadatum.validateJsonElement(jsonArrayrequestHeadersToAdd.get(i));
          };
        }
      }
      if ((jsonObj.get("service_name") != null && !jsonObj.get("service_name").isJsonNull()) && !jsonObj.get("service_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HTTPHealthCheck.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HTTPHealthCheck' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HTTPHealthCheck> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HTTPHealthCheck.class));

       return (TypeAdapter<T>) new TypeAdapter<HTTPHealthCheck>() {
           @Override
           public void write(JsonWriter out, HTTPHealthCheck value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HTTPHealthCheck read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HTTPHealthCheck given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HTTPHealthCheck
   * @throws IOException if the JSON string is invalid with respect to HTTPHealthCheck
   */
  public static HTTPHealthCheck fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HTTPHealthCheck.class);
  }

  /**
   * Convert an instance of HTTPHealthCheck to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

