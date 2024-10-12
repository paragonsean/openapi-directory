/*
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
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
 * TranscoderProperty
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:34.965109-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TranscoderProperty {
  public static final String SERIALIZED_NAME_KEY = "key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_SECTION = "section";
  @SerializedName(SERIALIZED_NAME_SECTION)
  private String section;

  public static final String SERIALIZED_NAME_TRANSCODER_ID = "transcoder_id";
  @SerializedName(SERIALIZED_NAME_TRANSCODER_ID)
  private String transcoderId;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public TranscoderProperty() {
  }

  public TranscoderProperty key(String key) {
    this.key = key;
    return this;
  }

  /**
   * The key of the property. For &lt;strong&gt;rtsp&lt;/strong&gt;, valid values are &lt;strong&gt;debugRtspSession&lt;/strong&gt;, &lt;strong&gt;maxRtcpWaitTime&lt;/strong&gt;, &lt;strong&gt;avSyncMethod&lt;/strong&gt;, &lt;strong&gt;rtspValidationFrequency&lt;/strong&gt;, &lt;strong&gt;rtpTransportMode&lt;/strong&gt;, &lt;strong&gt;rtspFilterUnknownTracks&lt;/strong&gt;, &lt;strong&gt;rtpIgnoreSpropParameterSets&lt;/strong&gt;, and &lt;strong&gt;rtpIgnoreProfileLevelId&lt;/strong&gt;. For &lt;strong&gt;cupertino&lt;/strong&gt;, valid values are &lt;strong&gt;cupertinoEnableProgramDateTime&lt;/strong&gt;, &lt;strong&gt;cupertinoEnableId3ProgramDateTime&lt;/strong&gt;, and &lt;strong&gt;cupertinoProgramDateTimeOffset&lt;/strong&gt;.
   * @return key
   */
  @javax.annotation.Nullable
  public String getKey() {
    return key;
  }

  public void setKey(String key) {
    this.key = key;
  }


  public TranscoderProperty section(String section) {
    this.section = section;
    return this;
  }

  /**
   * The section of the transcoder configuration table that contains the property. Valid values are &lt;strong&gt;rtsp&lt;/strong&gt; and &lt;strong&gt;cupertino&lt;/strong&gt;.
   * @return section
   */
  @javax.annotation.Nullable
  public String getSection() {
    return section;
  }

  public void setSection(String section) {
    this.section = section;
  }


  public TranscoderProperty transcoderId(String transcoderId) {
    this.transcoderId = transcoderId;
    return this;
  }

  /**
   * The unique alphanumeric string that identifies the transcoder.
   * @return transcoderId
   */
  @javax.annotation.Nullable
  public String getTranscoderId() {
    return transcoderId;
  }

  public void setTranscoderId(String transcoderId) {
    this.transcoderId = transcoderId;
  }


  public TranscoderProperty value(String value) {
    this.value = value;
    return this;
  }

  /**
   * The value of the property. For &lt;strong&gt;debugRtspSession&lt;/strong&gt;, &lt;strong&gt;avSyncMethod&lt;/strong&gt;, &lt;strong&gt;rtspFilterUnknownTracks&lt;/strong&gt;, &lt;strong&gt;rtpIgnoreSpropParameterSets&lt;/strong&gt;, &lt;strong&gt;rtpIgnoreProfileLevelId&lt;/strong&gt;, &lt;strong&gt;cupertinoEnableProgramDateTime&lt;/strong&gt;, and &lt;strong&gt;cupertinoEnableId3ProgramDateTime&lt;/strong&gt;, valid values are &lt;strong&gt;true&lt;/strong&gt; or &lt;strong&gt;false&lt;/strong&gt;. &lt;strong&gt;maxRtcpWaitTime&lt;/strong&gt; must be &lt;strong&gt;0&lt;/strong&gt; (ms, off) or greater. The default is &lt;strong&gt;2000&lt;/strong&gt;. Valid values for &lt;strong&gt;rtpTransportMode&lt;/strong&gt; are &lt;strong&gt;udp&lt;/strong&gt; or &lt;strong&gt;interleave&lt;/strong&gt; (the default). &lt;strong&gt;rtspValidationFrequency&lt;/strong&gt; must be &lt;strong&gt;0&lt;/strong&gt; (ms, off) or greater. The default is &lt;strong&gt;15000&lt;/strong&gt;. &lt;strong&gt;cupertinoProgramDateTimeOffset&lt;/strong&gt; must be an integer, positive or negative. The default is &lt;strong&gt;0&lt;/strong&gt; (ms).
   * @return value
   */
  @javax.annotation.Nullable
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TranscoderProperty transcoderProperty = (TranscoderProperty) o;
    return Objects.equals(this.key, transcoderProperty.key) &&
        Objects.equals(this.section, transcoderProperty.section) &&
        Objects.equals(this.transcoderId, transcoderProperty.transcoderId) &&
        Objects.equals(this.value, transcoderProperty.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(key, section, transcoderId, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TranscoderProperty {\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    section: ").append(toIndentedString(section)).append("\n");
    sb.append("    transcoderId: ").append(toIndentedString(transcoderId)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("key");
    openapiFields.add("section");
    openapiFields.add("transcoder_id");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TranscoderProperty
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TranscoderProperty.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TranscoderProperty is not found in the empty JSON string", TranscoderProperty.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TranscoderProperty.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TranscoderProperty` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("key") != null && !jsonObj.get("key").isJsonNull()) && !jsonObj.get("key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("key").toString()));
      }
      if ((jsonObj.get("section") != null && !jsonObj.get("section").isJsonNull()) && !jsonObj.get("section").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `section` to be a primitive type in the JSON string but got `%s`", jsonObj.get("section").toString()));
      }
      if ((jsonObj.get("transcoder_id") != null && !jsonObj.get("transcoder_id").isJsonNull()) && !jsonObj.get("transcoder_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transcoder_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transcoder_id").toString()));
      }
      if ((jsonObj.get("value") != null && !jsonObj.get("value").isJsonNull()) && !jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TranscoderProperty.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TranscoderProperty' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TranscoderProperty> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TranscoderProperty.class));

       return (TypeAdapter<T>) new TypeAdapter<TranscoderProperty>() {
           @Override
           public void write(JsonWriter out, TranscoderProperty value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TranscoderProperty read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TranscoderProperty given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TranscoderProperty
   * @throws IOException if the JSON string is invalid with respect to TranscoderProperty
   */
  public static TranscoderProperty fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TranscoderProperty.class);
  }

  /**
   * Convert an instance of TranscoderProperty to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

