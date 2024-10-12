/*
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.GroupMessage;

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
 * EndpointPostGroupsMessagesMetadataFiltersDataInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:21.899808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EndpointPostGroupsMessagesMetadataFiltersDataInner {
  public static final String SERIALIZED_NAME_MATCHED_METADATA = "matched_metadata";
  @SerializedName(SERIALIZED_NAME_MATCHED_METADATA)
  private Map<String, List<String>> matchedMetadata = new HashMap<>();

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private GroupMessage message;

  public EndpointPostGroupsMessagesMetadataFiltersDataInner() {
  }

  public EndpointPostGroupsMessagesMetadataFiltersDataInner matchedMetadata(Map<String, List<String>> matchedMetadata) {
    this.matchedMetadata = matchedMetadata;
    return this;
  }

  public EndpointPostGroupsMessagesMetadataFiltersDataInner putMatchedMetadataItem(String key, List<String> matchedMetadataItem) {
    if (this.matchedMetadata == null) {
      this.matchedMetadata = new HashMap<>();
    }
    this.matchedMetadata.put(key, matchedMetadataItem);
    return this;
  }

  /**
   * Get matchedMetadata
   * @return matchedMetadata
   */
  @javax.annotation.Nullable
  public Map<String, List<String>> getMatchedMetadata() {
    return matchedMetadata;
  }

  public void setMatchedMetadata(Map<String, List<String>> matchedMetadata) {
    this.matchedMetadata = matchedMetadata;
  }


  public EndpointPostGroupsMessagesMetadataFiltersDataInner message(GroupMessage message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public GroupMessage getMessage() {
    return message;
  }

  public void setMessage(GroupMessage message) {
    this.message = message;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EndpointPostGroupsMessagesMetadataFiltersDataInner endpointPostGroupsMessagesMetadataFiltersDataInner = (EndpointPostGroupsMessagesMetadataFiltersDataInner) o;
    return Objects.equals(this.matchedMetadata, endpointPostGroupsMessagesMetadataFiltersDataInner.matchedMetadata) &&
        Objects.equals(this.message, endpointPostGroupsMessagesMetadataFiltersDataInner.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(matchedMetadata, message);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EndpointPostGroupsMessagesMetadataFiltersDataInner {\n");
    sb.append("    matchedMetadata: ").append(toIndentedString(matchedMetadata)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
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
    openapiFields.add("matched_metadata");
    openapiFields.add("message");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EndpointPostGroupsMessagesMetadataFiltersDataInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EndpointPostGroupsMessagesMetadataFiltersDataInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EndpointPostGroupsMessagesMetadataFiltersDataInner is not found in the empty JSON string", EndpointPostGroupsMessagesMetadataFiltersDataInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EndpointPostGroupsMessagesMetadataFiltersDataInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EndpointPostGroupsMessagesMetadataFiltersDataInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `message`
      if (jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) {
        GroupMessage.validateJsonElement(jsonObj.get("message"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EndpointPostGroupsMessagesMetadataFiltersDataInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EndpointPostGroupsMessagesMetadataFiltersDataInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EndpointPostGroupsMessagesMetadataFiltersDataInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EndpointPostGroupsMessagesMetadataFiltersDataInner.class));

       return (TypeAdapter<T>) new TypeAdapter<EndpointPostGroupsMessagesMetadataFiltersDataInner>() {
           @Override
           public void write(JsonWriter out, EndpointPostGroupsMessagesMetadataFiltersDataInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EndpointPostGroupsMessagesMetadataFiltersDataInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EndpointPostGroupsMessagesMetadataFiltersDataInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EndpointPostGroupsMessagesMetadataFiltersDataInner
   * @throws IOException if the JSON string is invalid with respect to EndpointPostGroupsMessagesMetadataFiltersDataInner
   */
  public static EndpointPostGroupsMessagesMetadataFiltersDataInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EndpointPostGroupsMessagesMetadataFiltersDataInner.class);
  }

  /**
   * Convert an instance of EndpointPostGroupsMessagesMetadataFiltersDataInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

