/*
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
 * ReportRun
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:56.484539-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReportRun {
  public static final String SERIALIZED_NAME_AUTO_PUBLISH = "autoPublish";
  @SerializedName(SERIALIZED_NAME_AUTO_PUBLISH)
  private Boolean autoPublish;

  public static final String SERIALIZED_NAME_GUID = "guid";
  @SerializedName(SERIALIZED_NAME_GUID)
  private String guid;

  public static final String SERIALIZED_NAME_LATEST_CONFIG_ID = "latestConfigId";
  @SerializedName(SERIALIZED_NAME_LATEST_CONFIG_ID)
  private String latestConfigId;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public ReportRun() {
  }

  public ReportRun autoPublish(Boolean autoPublish) {
    this.autoPublish = autoPublish;
    return this;
  }

  /**
   * Get autoPublish
   * @return autoPublish
   */
  @javax.annotation.Nullable
  public Boolean getAutoPublish() {
    return autoPublish;
  }

  public void setAutoPublish(Boolean autoPublish) {
    this.autoPublish = autoPublish;
  }


  public ReportRun guid(String guid) {
    this.guid = guid;
    return this;
  }

  /**
   * Get guid
   * @return guid
   */
  @javax.annotation.Nullable
  public String getGuid() {
    return guid;
  }

  public void setGuid(String guid) {
    this.guid = guid;
  }


  public ReportRun latestConfigId(String latestConfigId) {
    this.latestConfigId = latestConfigId;
    return this;
  }

  /**
   * Get latestConfigId
   * @return latestConfigId
   */
  @javax.annotation.Nullable
  public String getLatestConfigId() {
    return latestConfigId;
  }

  public void setLatestConfigId(String latestConfigId) {
    this.latestConfigId = latestConfigId;
  }


  public ReportRun name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ReportRun type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReportRun reportRun = (ReportRun) o;
    return Objects.equals(this.autoPublish, reportRun.autoPublish) &&
        Objects.equals(this.guid, reportRun.guid) &&
        Objects.equals(this.latestConfigId, reportRun.latestConfigId) &&
        Objects.equals(this.name, reportRun.name) &&
        Objects.equals(this.type, reportRun.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoPublish, guid, latestConfigId, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReportRun {\n");
    sb.append("    autoPublish: ").append(toIndentedString(autoPublish)).append("\n");
    sb.append("    guid: ").append(toIndentedString(guid)).append("\n");
    sb.append("    latestConfigId: ").append(toIndentedString(latestConfigId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("autoPublish");
    openapiFields.add("guid");
    openapiFields.add("latestConfigId");
    openapiFields.add("name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReportRun
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReportRun.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReportRun is not found in the empty JSON string", ReportRun.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReportRun.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReportRun` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("guid") != null && !jsonObj.get("guid").isJsonNull()) && !jsonObj.get("guid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `guid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("guid").toString()));
      }
      if ((jsonObj.get("latestConfigId") != null && !jsonObj.get("latestConfigId").isJsonNull()) && !jsonObj.get("latestConfigId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `latestConfigId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("latestConfigId").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReportRun.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReportRun' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReportRun> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReportRun.class));

       return (TypeAdapter<T>) new TypeAdapter<ReportRun>() {
           @Override
           public void write(JsonWriter out, ReportRun value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReportRun read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReportRun given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReportRun
   * @throws IOException if the JSON string is invalid with respect to ReportRun
   */
  public static ReportRun fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReportRun.class);
  }

  /**
   * Convert an instance of ReportRun to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

