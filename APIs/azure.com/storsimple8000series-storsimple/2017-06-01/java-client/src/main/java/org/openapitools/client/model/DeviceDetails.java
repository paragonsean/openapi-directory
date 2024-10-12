/*
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
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
 * The additional device details regarding the end point count and volume container count.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:41.316643-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeviceDetails {
  public static final String SERIALIZED_NAME_ENDPOINT_COUNT = "endpointCount";
  @SerializedName(SERIALIZED_NAME_ENDPOINT_COUNT)
  private Integer endpointCount;

  public static final String SERIALIZED_NAME_VOLUME_CONTAINER_COUNT = "volumeContainerCount";
  @SerializedName(SERIALIZED_NAME_VOLUME_CONTAINER_COUNT)
  private Integer volumeContainerCount;

  public DeviceDetails() {
  }

  public DeviceDetails endpointCount(Integer endpointCount) {
    this.endpointCount = endpointCount;
    return this;
  }

  /**
   * The total number of endpoints that are currently on the device ( i.e. number of volumes).
   * @return endpointCount
   */
  @javax.annotation.Nullable
  public Integer getEndpointCount() {
    return endpointCount;
  }

  public void setEndpointCount(Integer endpointCount) {
    this.endpointCount = endpointCount;
  }


  public DeviceDetails volumeContainerCount(Integer volumeContainerCount) {
    this.volumeContainerCount = volumeContainerCount;
    return this;
  }

  /**
   * The total number of volume containers on the device.
   * @return volumeContainerCount
   */
  @javax.annotation.Nullable
  public Integer getVolumeContainerCount() {
    return volumeContainerCount;
  }

  public void setVolumeContainerCount(Integer volumeContainerCount) {
    this.volumeContainerCount = volumeContainerCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeviceDetails deviceDetails = (DeviceDetails) o;
    return Objects.equals(this.endpointCount, deviceDetails.endpointCount) &&
        Objects.equals(this.volumeContainerCount, deviceDetails.volumeContainerCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(endpointCount, volumeContainerCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeviceDetails {\n");
    sb.append("    endpointCount: ").append(toIndentedString(endpointCount)).append("\n");
    sb.append("    volumeContainerCount: ").append(toIndentedString(volumeContainerCount)).append("\n");
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
    openapiFields.add("endpointCount");
    openapiFields.add("volumeContainerCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeviceDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeviceDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeviceDetails is not found in the empty JSON string", DeviceDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeviceDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeviceDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeviceDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeviceDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeviceDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeviceDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<DeviceDetails>() {
           @Override
           public void write(JsonWriter out, DeviceDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeviceDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeviceDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeviceDetails
   * @throws IOException if the JSON string is invalid with respect to DeviceDetails
   */
  public static DeviceDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeviceDetails.class);
  }

  /**
   * Convert an instance of DeviceDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

