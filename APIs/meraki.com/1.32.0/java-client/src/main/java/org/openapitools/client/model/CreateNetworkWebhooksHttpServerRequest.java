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
import java.util.Arrays;
import org.openapitools.client.model.CreateNetworkWebhooksHttpServerRequestPayloadTemplate;

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
 * CreateNetworkWebhooksHttpServerRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateNetworkWebhooksHttpServerRequest {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PAYLOAD_TEMPLATE = "payloadTemplate";
  @SerializedName(SERIALIZED_NAME_PAYLOAD_TEMPLATE)
  private CreateNetworkWebhooksHttpServerRequestPayloadTemplate payloadTemplate;

  public static final String SERIALIZED_NAME_SHARED_SECRET = "sharedSecret";
  @SerializedName(SERIALIZED_NAME_SHARED_SECRET)
  private String sharedSecret;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public CreateNetworkWebhooksHttpServerRequest() {
  }

  public CreateNetworkWebhooksHttpServerRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * A name for easy reference to the HTTP server
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateNetworkWebhooksHttpServerRequest payloadTemplate(CreateNetworkWebhooksHttpServerRequestPayloadTemplate payloadTemplate) {
    this.payloadTemplate = payloadTemplate;
    return this;
  }

  /**
   * Get payloadTemplate
   * @return payloadTemplate
   */
  @javax.annotation.Nullable
  public CreateNetworkWebhooksHttpServerRequestPayloadTemplate getPayloadTemplate() {
    return payloadTemplate;
  }

  public void setPayloadTemplate(CreateNetworkWebhooksHttpServerRequestPayloadTemplate payloadTemplate) {
    this.payloadTemplate = payloadTemplate;
  }


  public CreateNetworkWebhooksHttpServerRequest sharedSecret(String sharedSecret) {
    this.sharedSecret = sharedSecret;
    return this;
  }

  /**
   * A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
   * @return sharedSecret
   */
  @javax.annotation.Nullable
  public String getSharedSecret() {
    return sharedSecret;
  }

  public void setSharedSecret(String sharedSecret) {
    this.sharedSecret = sharedSecret;
  }


  public CreateNetworkWebhooksHttpServerRequest url(String url) {
    this.url = url;
    return this;
  }

  /**
   * The URL of the HTTP server. Once set, cannot be updated.
   * @return url
   */
  @javax.annotation.Nonnull
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateNetworkWebhooksHttpServerRequest createNetworkWebhooksHttpServerRequest = (CreateNetworkWebhooksHttpServerRequest) o;
    return Objects.equals(this.name, createNetworkWebhooksHttpServerRequest.name) &&
        Objects.equals(this.payloadTemplate, createNetworkWebhooksHttpServerRequest.payloadTemplate) &&
        Objects.equals(this.sharedSecret, createNetworkWebhooksHttpServerRequest.sharedSecret) &&
        Objects.equals(this.url, createNetworkWebhooksHttpServerRequest.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, payloadTemplate, sharedSecret, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateNetworkWebhooksHttpServerRequest {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    payloadTemplate: ").append(toIndentedString(payloadTemplate)).append("\n");
    sb.append("    sharedSecret: ").append(toIndentedString(sharedSecret)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("payloadTemplate");
    openapiFields.add("sharedSecret");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateNetworkWebhooksHttpServerRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateNetworkWebhooksHttpServerRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateNetworkWebhooksHttpServerRequest is not found in the empty JSON string", CreateNetworkWebhooksHttpServerRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateNetworkWebhooksHttpServerRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateNetworkWebhooksHttpServerRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateNetworkWebhooksHttpServerRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `payloadTemplate`
      if (jsonObj.get("payloadTemplate") != null && !jsonObj.get("payloadTemplate").isJsonNull()) {
        CreateNetworkWebhooksHttpServerRequestPayloadTemplate.validateJsonElement(jsonObj.get("payloadTemplate"));
      }
      if ((jsonObj.get("sharedSecret") != null && !jsonObj.get("sharedSecret").isJsonNull()) && !jsonObj.get("sharedSecret").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sharedSecret` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sharedSecret").toString()));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateNetworkWebhooksHttpServerRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateNetworkWebhooksHttpServerRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateNetworkWebhooksHttpServerRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateNetworkWebhooksHttpServerRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateNetworkWebhooksHttpServerRequest>() {
           @Override
           public void write(JsonWriter out, CreateNetworkWebhooksHttpServerRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateNetworkWebhooksHttpServerRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateNetworkWebhooksHttpServerRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateNetworkWebhooksHttpServerRequest
   * @throws IOException if the JSON string is invalid with respect to CreateNetworkWebhooksHttpServerRequest
   */
  public static CreateNetworkWebhooksHttpServerRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateNetworkWebhooksHttpServerRequest.class);
  }

  /**
   * Convert an instance of CreateNetworkWebhooksHttpServerRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

