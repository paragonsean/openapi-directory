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
 * The properties of access control record.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:41.316643-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AccessControlRecordProperties {
  public static final String SERIALIZED_NAME_INITIATOR_NAME = "initiatorName";
  @SerializedName(SERIALIZED_NAME_INITIATOR_NAME)
  private String initiatorName;

  public static final String SERIALIZED_NAME_VOLUME_COUNT = "volumeCount";
  @SerializedName(SERIALIZED_NAME_VOLUME_COUNT)
  private Integer volumeCount;

  public AccessControlRecordProperties() {
  }

  public AccessControlRecordProperties(
     Integer volumeCount
  ) {
    this();
    this.volumeCount = volumeCount;
  }

  public AccessControlRecordProperties initiatorName(String initiatorName) {
    this.initiatorName = initiatorName;
    return this;
  }

  /**
   * The iSCSI initiator name (IQN).
   * @return initiatorName
   */
  @javax.annotation.Nonnull
  public String getInitiatorName() {
    return initiatorName;
  }

  public void setInitiatorName(String initiatorName) {
    this.initiatorName = initiatorName;
  }


  /**
   * The number of volumes using the access control record.
   * @return volumeCount
   */
  @javax.annotation.Nullable
  public Integer getVolumeCount() {
    return volumeCount;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccessControlRecordProperties accessControlRecordProperties = (AccessControlRecordProperties) o;
    return Objects.equals(this.initiatorName, accessControlRecordProperties.initiatorName) &&
        Objects.equals(this.volumeCount, accessControlRecordProperties.volumeCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(initiatorName, volumeCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccessControlRecordProperties {\n");
    sb.append("    initiatorName: ").append(toIndentedString(initiatorName)).append("\n");
    sb.append("    volumeCount: ").append(toIndentedString(volumeCount)).append("\n");
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
    openapiFields.add("initiatorName");
    openapiFields.add("volumeCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("initiatorName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AccessControlRecordProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AccessControlRecordProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AccessControlRecordProperties is not found in the empty JSON string", AccessControlRecordProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AccessControlRecordProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AccessControlRecordProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AccessControlRecordProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("initiatorName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `initiatorName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("initiatorName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AccessControlRecordProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AccessControlRecordProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AccessControlRecordProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AccessControlRecordProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<AccessControlRecordProperties>() {
           @Override
           public void write(JsonWriter out, AccessControlRecordProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AccessControlRecordProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AccessControlRecordProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AccessControlRecordProperties
   * @throws IOException if the JSON string is invalid with respect to AccessControlRecordProperties
   */
  public static AccessControlRecordProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AccessControlRecordProperties.class);
  }

  /**
   * Convert an instance of AccessControlRecordProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

