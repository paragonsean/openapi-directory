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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CreateNetworkWebhooksPayloadTemplateRequestHeadersInner;

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
 * UpdateNetworkWebhooksPayloadTemplateRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkWebhooksPayloadTemplateRequest {
  public static final String SERIALIZED_NAME_BODY = "body";
  @SerializedName(SERIALIZED_NAME_BODY)
  private String body;

  public static final String SERIALIZED_NAME_BODY_FILE = "bodyFile";
  @SerializedName(SERIALIZED_NAME_BODY_FILE)
  private byte[] bodyFile;

  public static final String SERIALIZED_NAME_HEADERS = "headers";
  @SerializedName(SERIALIZED_NAME_HEADERS)
  private List<CreateNetworkWebhooksPayloadTemplateRequestHeadersInner> headers = new ArrayList<>();

  public static final String SERIALIZED_NAME_HEADERS_FILE = "headersFile";
  @SerializedName(SERIALIZED_NAME_HEADERS_FILE)
  private byte[] headersFile;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public UpdateNetworkWebhooksPayloadTemplateRequest() {
  }

  public UpdateNetworkWebhooksPayloadTemplateRequest body(String body) {
    this.body = body;
    return this;
  }

  /**
   * The liquid template used for the body of the webhook message.
   * @return body
   */
  @javax.annotation.Nullable
  public String getBody() {
    return body;
  }

  public void setBody(String body) {
    this.body = body;
  }


  public UpdateNetworkWebhooksPayloadTemplateRequest bodyFile(byte[] bodyFile) {
    this.bodyFile = bodyFile;
    return this;
  }

  /**
   * A file containing liquid template used for the body of the webhook message.
   * @return bodyFile
   */
  @javax.annotation.Nullable
  public byte[] getBodyFile() {
    return bodyFile;
  }

  public void setBodyFile(byte[] bodyFile) {
    this.bodyFile = bodyFile;
  }


  public UpdateNetworkWebhooksPayloadTemplateRequest headers(List<CreateNetworkWebhooksPayloadTemplateRequestHeadersInner> headers) {
    this.headers = headers;
    return this;
  }

  public UpdateNetworkWebhooksPayloadTemplateRequest addHeadersItem(CreateNetworkWebhooksPayloadTemplateRequestHeadersInner headersItem) {
    if (this.headers == null) {
      this.headers = new ArrayList<>();
    }
    this.headers.add(headersItem);
    return this;
  }

  /**
   * The liquid template used with the webhook headers.
   * @return headers
   */
  @javax.annotation.Nullable
  public List<CreateNetworkWebhooksPayloadTemplateRequestHeadersInner> getHeaders() {
    return headers;
  }

  public void setHeaders(List<CreateNetworkWebhooksPayloadTemplateRequestHeadersInner> headers) {
    this.headers = headers;
  }


  public UpdateNetworkWebhooksPayloadTemplateRequest headersFile(byte[] headersFile) {
    this.headersFile = headersFile;
    return this;
  }

  /**
   * A file containing the liquid template used with the webhook headers.
   * @return headersFile
   */
  @javax.annotation.Nullable
  public byte[] getHeadersFile() {
    return headersFile;
  }

  public void setHeadersFile(byte[] headersFile) {
    this.headersFile = headersFile;
  }


  public UpdateNetworkWebhooksPayloadTemplateRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the template
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkWebhooksPayloadTemplateRequest updateNetworkWebhooksPayloadTemplateRequest = (UpdateNetworkWebhooksPayloadTemplateRequest) o;
    return Objects.equals(this.body, updateNetworkWebhooksPayloadTemplateRequest.body) &&
        Arrays.equals(this.bodyFile, updateNetworkWebhooksPayloadTemplateRequest.bodyFile) &&
        Objects.equals(this.headers, updateNetworkWebhooksPayloadTemplateRequest.headers) &&
        Arrays.equals(this.headersFile, updateNetworkWebhooksPayloadTemplateRequest.headersFile) &&
        Objects.equals(this.name, updateNetworkWebhooksPayloadTemplateRequest.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(body, Arrays.hashCode(bodyFile), headers, Arrays.hashCode(headersFile), name);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkWebhooksPayloadTemplateRequest {\n");
    sb.append("    body: ").append(toIndentedString(body)).append("\n");
    sb.append("    bodyFile: ").append(toIndentedString(bodyFile)).append("\n");
    sb.append("    headers: ").append(toIndentedString(headers)).append("\n");
    sb.append("    headersFile: ").append(toIndentedString(headersFile)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("body");
    openapiFields.add("bodyFile");
    openapiFields.add("headers");
    openapiFields.add("headersFile");
    openapiFields.add("name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkWebhooksPayloadTemplateRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkWebhooksPayloadTemplateRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkWebhooksPayloadTemplateRequest is not found in the empty JSON string", UpdateNetworkWebhooksPayloadTemplateRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkWebhooksPayloadTemplateRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkWebhooksPayloadTemplateRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("body") != null && !jsonObj.get("body").isJsonNull()) && !jsonObj.get("body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("body").toString()));
      }
      if (jsonObj.get("headers") != null && !jsonObj.get("headers").isJsonNull()) {
        JsonArray jsonArrayheaders = jsonObj.getAsJsonArray("headers");
        if (jsonArrayheaders != null) {
          // ensure the json data is an array
          if (!jsonObj.get("headers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `headers` to be an array in the JSON string but got `%s`", jsonObj.get("headers").toString()));
          }

          // validate the optional field `headers` (array)
          for (int i = 0; i < jsonArrayheaders.size(); i++) {
            CreateNetworkWebhooksPayloadTemplateRequestHeadersInner.validateJsonElement(jsonArrayheaders.get(i));
          };
        }
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkWebhooksPayloadTemplateRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkWebhooksPayloadTemplateRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkWebhooksPayloadTemplateRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkWebhooksPayloadTemplateRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkWebhooksPayloadTemplateRequest>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkWebhooksPayloadTemplateRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkWebhooksPayloadTemplateRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkWebhooksPayloadTemplateRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkWebhooksPayloadTemplateRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkWebhooksPayloadTemplateRequest
   */
  public static UpdateNetworkWebhooksPayloadTemplateRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkWebhooksPayloadTemplateRequest.class);
  }

  /**
   * Convert an instance of UpdateNetworkWebhooksPayloadTemplateRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

