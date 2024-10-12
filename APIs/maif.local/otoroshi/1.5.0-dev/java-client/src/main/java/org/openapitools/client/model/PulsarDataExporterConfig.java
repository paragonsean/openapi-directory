/*
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
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
 * The configuration for kafka access
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:27.562730-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PulsarDataExporterConfig {
  public static final String SERIALIZED_NAME_NAMESPACE = "namespace";
  @SerializedName(SERIALIZED_NAME_NAMESPACE)
  private String namespace;

  public static final String SERIALIZED_NAME_TENANT = "tenant";
  @SerializedName(SERIALIZED_NAME_TENANT)
  private String tenant;

  public static final String SERIALIZED_NAME_TOPIC = "topic";
  @SerializedName(SERIALIZED_NAME_TOPIC)
  private String topic;

  public static final String SERIALIZED_NAME_URI = "uri";
  @SerializedName(SERIALIZED_NAME_URI)
  private List<String> uri = new ArrayList<>();

  public PulsarDataExporterConfig() {
  }

  public PulsarDataExporterConfig namespace(String namespace) {
    this.namespace = namespace;
    return this;
  }

  /**
   * Namespace
   * @return namespace
   */
  @javax.annotation.Nonnull
  public String getNamespace() {
    return namespace;
  }

  public void setNamespace(String namespace) {
    this.namespace = namespace;
  }


  public PulsarDataExporterConfig tenant(String tenant) {
    this.tenant = tenant;
    return this;
  }

  /**
   * Tenant
   * @return tenant
   */
  @javax.annotation.Nonnull
  public String getTenant() {
    return tenant;
  }

  public void setTenant(String tenant) {
    this.tenant = tenant;
  }


  public PulsarDataExporterConfig topic(String topic) {
    this.topic = topic;
    return this;
  }

  /**
   * Topic
   * @return topic
   */
  @javax.annotation.Nonnull
  public String getTopic() {
    return topic;
  }

  public void setTopic(String topic) {
    this.topic = topic;
  }


  public PulsarDataExporterConfig uri(List<String> uri) {
    this.uri = uri;
    return this;
  }

  public PulsarDataExporterConfig addUriItem(String uriItem) {
    if (this.uri == null) {
      this.uri = new ArrayList<>();
    }
    this.uri.add(uriItem);
    return this;
  }

  /**
   * URI of the pulsar server
   * @return uri
   */
  @javax.annotation.Nonnull
  public List<String> getUri() {
    return uri;
  }

  public void setUri(List<String> uri) {
    this.uri = uri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PulsarDataExporterConfig pulsarDataExporterConfig = (PulsarDataExporterConfig) o;
    return Objects.equals(this.namespace, pulsarDataExporterConfig.namespace) &&
        Objects.equals(this.tenant, pulsarDataExporterConfig.tenant) &&
        Objects.equals(this.topic, pulsarDataExporterConfig.topic) &&
        Objects.equals(this.uri, pulsarDataExporterConfig.uri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(namespace, tenant, topic, uri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PulsarDataExporterConfig {\n");
    sb.append("    namespace: ").append(toIndentedString(namespace)).append("\n");
    sb.append("    tenant: ").append(toIndentedString(tenant)).append("\n");
    sb.append("    topic: ").append(toIndentedString(topic)).append("\n");
    sb.append("    uri: ").append(toIndentedString(uri)).append("\n");
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
    openapiFields.add("namespace");
    openapiFields.add("tenant");
    openapiFields.add("topic");
    openapiFields.add("uri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("namespace");
    openapiRequiredFields.add("tenant");
    openapiRequiredFields.add("topic");
    openapiRequiredFields.add("uri");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PulsarDataExporterConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PulsarDataExporterConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PulsarDataExporterConfig is not found in the empty JSON string", PulsarDataExporterConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PulsarDataExporterConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PulsarDataExporterConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PulsarDataExporterConfig.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("namespace").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `namespace` to be a primitive type in the JSON string but got `%s`", jsonObj.get("namespace").toString()));
      }
      if (!jsonObj.get("tenant").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tenant` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tenant").toString()));
      }
      if (!jsonObj.get("topic").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `topic` to be a primitive type in the JSON string but got `%s`", jsonObj.get("topic").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("uri") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("uri").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `uri` to be an array in the JSON string but got `%s`", jsonObj.get("uri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PulsarDataExporterConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PulsarDataExporterConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PulsarDataExporterConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PulsarDataExporterConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<PulsarDataExporterConfig>() {
           @Override
           public void write(JsonWriter out, PulsarDataExporterConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PulsarDataExporterConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PulsarDataExporterConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PulsarDataExporterConfig
   * @throws IOException if the JSON string is invalid with respect to PulsarDataExporterConfig
   */
  public static PulsarDataExporterConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PulsarDataExporterConfig.class);
  }

  /**
   * Convert an instance of PulsarDataExporterConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

