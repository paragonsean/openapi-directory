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
import org.openapitools.client.model.ArrayOfStreamTargets;
import org.openapitools.client.model.HashOfTotals;

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
 * UsageNetworkStreamTargets
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:34.965109-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UsageNetworkStreamTargets {
  public static final String SERIALIZED_NAME_STREAM_TARGETS = "stream_targets";
  @SerializedName(SERIALIZED_NAME_STREAM_TARGETS)
  private ArrayOfStreamTargets streamTargets;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private HashOfTotals total;

  public UsageNetworkStreamTargets() {
  }

  public UsageNetworkStreamTargets streamTargets(ArrayOfStreamTargets streamTargets) {
    this.streamTargets = streamTargets;
    return this;
  }

  /**
   * Get streamTargets
   * @return streamTargets
   */
  @javax.annotation.Nullable
  public ArrayOfStreamTargets getStreamTargets() {
    return streamTargets;
  }

  public void setStreamTargets(ArrayOfStreamTargets streamTargets) {
    this.streamTargets = streamTargets;
  }


  public UsageNetworkStreamTargets total(HashOfTotals total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public HashOfTotals getTotal() {
    return total;
  }

  public void setTotal(HashOfTotals total) {
    this.total = total;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UsageNetworkStreamTargets usageNetworkStreamTargets = (UsageNetworkStreamTargets) o;
    return Objects.equals(this.streamTargets, usageNetworkStreamTargets.streamTargets) &&
        Objects.equals(this.total, usageNetworkStreamTargets.total);
  }

  @Override
  public int hashCode() {
    return Objects.hash(streamTargets, total);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UsageNetworkStreamTargets {\n");
    sb.append("    streamTargets: ").append(toIndentedString(streamTargets)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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
    openapiFields.add("stream_targets");
    openapiFields.add("total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UsageNetworkStreamTargets
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UsageNetworkStreamTargets.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UsageNetworkStreamTargets is not found in the empty JSON string", UsageNetworkStreamTargets.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UsageNetworkStreamTargets.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UsageNetworkStreamTargets` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `stream_targets`
      if (jsonObj.get("stream_targets") != null && !jsonObj.get("stream_targets").isJsonNull()) {
        ArrayOfStreamTargets.validateJsonElement(jsonObj.get("stream_targets"));
      }
      // validate the optional field `total`
      if (jsonObj.get("total") != null && !jsonObj.get("total").isJsonNull()) {
        HashOfTotals.validateJsonElement(jsonObj.get("total"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UsageNetworkStreamTargets.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UsageNetworkStreamTargets' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UsageNetworkStreamTargets> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UsageNetworkStreamTargets.class));

       return (TypeAdapter<T>) new TypeAdapter<UsageNetworkStreamTargets>() {
           @Override
           public void write(JsonWriter out, UsageNetworkStreamTargets value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UsageNetworkStreamTargets read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UsageNetworkStreamTargets given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UsageNetworkStreamTargets
   * @throws IOException if the JSON string is invalid with respect to UsageNetworkStreamTargets
   */
  public static UsageNetworkStreamTargets fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UsageNetworkStreamTargets.class);
  }

  /**
   * Convert an instance of UsageNetworkStreamTargets to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

