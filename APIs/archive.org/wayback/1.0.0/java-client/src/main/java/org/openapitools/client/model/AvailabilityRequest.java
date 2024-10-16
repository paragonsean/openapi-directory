/*
 * Wayback API
 * API for Internet Archive's Wayback Machine
 *
 * The version of the OpenAPI document: 1.0.0
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
 * AvailabilityRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:54.904307-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AvailabilityRequest {
  /**
   * The direction to find the closest snapshot to the requested timestamp
   */
  @JsonAdapter(ClosestEnum.Adapter.class)
  public enum ClosestEnum {
    EITHER("either"),
    
    AFTER("after"),
    
    BEFORE("before");

    private String value;

    ClosestEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ClosestEnum fromValue(String value) {
      for (ClosestEnum b : ClosestEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ClosestEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ClosestEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ClosestEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ClosestEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ClosestEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CLOSEST = "closest";
  @SerializedName(SERIALIZED_NAME_CLOSEST)
  private ClosestEnum closest;

  public static final String SERIALIZED_NAME_TAG = "tag";
  @SerializedName(SERIALIZED_NAME_TAG)
  private String tag;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private String timestamp;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public AvailabilityRequest() {
  }

  public AvailabilityRequest closest(ClosestEnum closest) {
    this.closest = closest;
    return this;
  }

  /**
   * The direction to find the closest snapshot to the requested timestamp
   * @return closest
   */
  @javax.annotation.Nullable
  public ClosestEnum getClosest() {
    return closest;
  }

  public void setClosest(ClosestEnum closest) {
    this.closest = closest;
  }


  public AvailabilityRequest tag(String tag) {
    this.tag = tag;
    return this;
  }

  /**
   * A user-supplied tag, used for collation
   * @return tag
   */
  @javax.annotation.Nullable
  public String getTag() {
    return tag;
  }

  public void setTag(String tag) {
    this.tag = tag;
  }


  public AvailabilityRequest timestamp(String timestamp) {
    this.timestamp = timestamp;
    return this;
  }

  /**
   * Timestamp requested in ISO 8601 format. The following formats are acceptable: - YYYY - YYYY-MM - YYYY-MM-DD - YYYY-MM-DDTHH:mm:SSz - YYYY-MM-DD:HH:mm+00:00 
   * @return timestamp
   */
  @javax.annotation.Nullable
  public String getTimestamp() {
    return timestamp;
  }

  public void setTimestamp(String timestamp) {
    this.timestamp = timestamp;
  }


  public AvailabilityRequest url(String url) {
    this.url = url;
    return this;
  }

  /**
   * The URL requested
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
    AvailabilityRequest availabilityRequest = (AvailabilityRequest) o;
    return Objects.equals(this.closest, availabilityRequest.closest) &&
        Objects.equals(this.tag, availabilityRequest.tag) &&
        Objects.equals(this.timestamp, availabilityRequest.timestamp) &&
        Objects.equals(this.url, availabilityRequest.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(closest, tag, timestamp, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AvailabilityRequest {\n");
    sb.append("    closest: ").append(toIndentedString(closest)).append("\n");
    sb.append("    tag: ").append(toIndentedString(tag)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
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
    openapiFields.add("closest");
    openapiFields.add("tag");
    openapiFields.add("timestamp");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AvailabilityRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AvailabilityRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AvailabilityRequest is not found in the empty JSON string", AvailabilityRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AvailabilityRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AvailabilityRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AvailabilityRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("closest") != null && !jsonObj.get("closest").isJsonNull()) && !jsonObj.get("closest").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `closest` to be a primitive type in the JSON string but got `%s`", jsonObj.get("closest").toString()));
      }
      // validate the optional field `closest`
      if (jsonObj.get("closest") != null && !jsonObj.get("closest").isJsonNull()) {
        ClosestEnum.validateJsonElement(jsonObj.get("closest"));
      }
      if ((jsonObj.get("tag") != null && !jsonObj.get("tag").isJsonNull()) && !jsonObj.get("tag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tag").toString()));
      }
      if ((jsonObj.get("timestamp") != null && !jsonObj.get("timestamp").isJsonNull()) && !jsonObj.get("timestamp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timestamp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timestamp").toString()));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AvailabilityRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AvailabilityRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AvailabilityRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AvailabilityRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AvailabilityRequest>() {
           @Override
           public void write(JsonWriter out, AvailabilityRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AvailabilityRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AvailabilityRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AvailabilityRequest
   * @throws IOException if the JSON string is invalid with respect to AvailabilityRequest
   */
  public static AvailabilityRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AvailabilityRequest.class);
  }

  /**
   * Convert an instance of AvailabilityRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

