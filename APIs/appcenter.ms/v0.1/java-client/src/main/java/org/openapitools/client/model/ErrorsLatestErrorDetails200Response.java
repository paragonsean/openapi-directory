/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner;

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
 * ErrorsLatestErrorDetails200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorsLatestErrorDetails200Response {
  public static final String SERIALIZED_NAME_APP_LAUNCH_TIMESTAMP = "appLaunchTimestamp";
  @SerializedName(SERIALIZED_NAME_APP_LAUNCH_TIMESTAMP)
  private OffsetDateTime appLaunchTimestamp;

  public static final String SERIALIZED_NAME_CARRIER_NAME = "carrierName";
  @SerializedName(SERIALIZED_NAME_CARRIER_NAME)
  private String carrierName;

  public static final String SERIALIZED_NAME_JAILBREAK = "jailbreak";
  @SerializedName(SERIALIZED_NAME_JAILBREAK)
  private Boolean jailbreak;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private Map<String, String> properties = new HashMap<>();

  public static final String SERIALIZED_NAME_REASON_FRAMES = "reasonFrames";
  @SerializedName(SERIALIZED_NAME_REASON_FRAMES)
  private List<ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner> reasonFrames = new ArrayList<>();

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_DEVICE_NAME = "deviceName";
  @SerializedName(SERIALIZED_NAME_DEVICE_NAME)
  private String deviceName;

  public static final String SERIALIZED_NAME_ERROR_ID = "errorId";
  @SerializedName(SERIALIZED_NAME_ERROR_ID)
  private String errorId;

  public static final String SERIALIZED_NAME_HAS_ATTACHMENTS = "hasAttachments";
  @SerializedName(SERIALIZED_NAME_HAS_ATTACHMENTS)
  private Boolean hasAttachments;

  public static final String SERIALIZED_NAME_HAS_BREADCRUMBS = "hasBreadcrumbs";
  @SerializedName(SERIALIZED_NAME_HAS_BREADCRUMBS)
  private Boolean hasBreadcrumbs;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_OS_TYPE = "osType";
  @SerializedName(SERIALIZED_NAME_OS_TYPE)
  private String osType;

  public static final String SERIALIZED_NAME_OS_VERSION = "osVersion";
  @SerializedName(SERIALIZED_NAME_OS_VERSION)
  private String osVersion;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private OffsetDateTime timestamp;

  public static final String SERIALIZED_NAME_USER_ID = "userId";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public ErrorsLatestErrorDetails200Response() {
  }

  public ErrorsLatestErrorDetails200Response appLaunchTimestamp(OffsetDateTime appLaunchTimestamp) {
    this.appLaunchTimestamp = appLaunchTimestamp;
    return this;
  }

  /**
   * Timestamp when the app was launched, example: &#39;2017-03-13T18:05:42Z&#39;. 
   * @return appLaunchTimestamp
   */
  @javax.annotation.Nullable
  public OffsetDateTime getAppLaunchTimestamp() {
    return appLaunchTimestamp;
  }

  public void setAppLaunchTimestamp(OffsetDateTime appLaunchTimestamp) {
    this.appLaunchTimestamp = appLaunchTimestamp;
  }


  public ErrorsLatestErrorDetails200Response carrierName(String carrierName) {
    this.carrierName = carrierName;
    return this;
  }

  /**
   * Carrier name (for mobile devices). 
   * @return carrierName
   */
  @javax.annotation.Nullable
  public String getCarrierName() {
    return carrierName;
  }

  public void setCarrierName(String carrierName) {
    this.carrierName = carrierName;
  }


  public ErrorsLatestErrorDetails200Response jailbreak(Boolean jailbreak) {
    this.jailbreak = jailbreak;
    return this;
  }

  /**
   * Flag indicating if device is jailbroken 
   * @return jailbreak
   */
  @javax.annotation.Nullable
  public Boolean getJailbreak() {
    return jailbreak;
  }

  public void setJailbreak(Boolean jailbreak) {
    this.jailbreak = jailbreak;
  }


  public ErrorsLatestErrorDetails200Response name(String name) {
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


  public ErrorsLatestErrorDetails200Response properties(Map<String, String> properties) {
    this.properties = properties;
    return this;
  }

  public ErrorsLatestErrorDetails200Response putPropertiesItem(String key, String propertiesItem) {
    if (this.properties == null) {
      this.properties = new HashMap<>();
    }
    this.properties.put(key, propertiesItem);
    return this;
  }

  /**
   * Get properties
   * @return properties
   */
  @javax.annotation.Nullable
  public Map<String, String> getProperties() {
    return properties;
  }

  public void setProperties(Map<String, String> properties) {
    this.properties = properties;
  }


  public ErrorsLatestErrorDetails200Response reasonFrames(List<ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner> reasonFrames) {
    this.reasonFrames = reasonFrames;
    return this;
  }

  public ErrorsLatestErrorDetails200Response addReasonFramesItem(ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner reasonFramesItem) {
    if (this.reasonFrames == null) {
      this.reasonFrames = new ArrayList<>();
    }
    this.reasonFrames.add(reasonFramesItem);
    return this;
  }

  /**
   * Get reasonFrames
   * @return reasonFrames
   */
  @javax.annotation.Nullable
  public List<ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner> getReasonFrames() {
    return reasonFrames;
  }

  public void setReasonFrames(List<ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner> reasonFrames) {
    this.reasonFrames = reasonFrames;
  }


  public ErrorsLatestErrorDetails200Response country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Get country
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public ErrorsLatestErrorDetails200Response deviceName(String deviceName) {
    this.deviceName = deviceName;
    return this;
  }

  /**
   * Get deviceName
   * @return deviceName
   */
  @javax.annotation.Nullable
  public String getDeviceName() {
    return deviceName;
  }

  public void setDeviceName(String deviceName) {
    this.deviceName = deviceName;
  }


  public ErrorsLatestErrorDetails200Response errorId(String errorId) {
    this.errorId = errorId;
    return this;
  }

  /**
   * Get errorId
   * @return errorId
   */
  @javax.annotation.Nullable
  public String getErrorId() {
    return errorId;
  }

  public void setErrorId(String errorId) {
    this.errorId = errorId;
  }


  public ErrorsLatestErrorDetails200Response hasAttachments(Boolean hasAttachments) {
    this.hasAttachments = hasAttachments;
    return this;
  }

  /**
   * Get hasAttachments
   * @return hasAttachments
   */
  @javax.annotation.Nullable
  public Boolean getHasAttachments() {
    return hasAttachments;
  }

  public void setHasAttachments(Boolean hasAttachments) {
    this.hasAttachments = hasAttachments;
  }


  public ErrorsLatestErrorDetails200Response hasBreadcrumbs(Boolean hasBreadcrumbs) {
    this.hasBreadcrumbs = hasBreadcrumbs;
    return this;
  }

  /**
   * Get hasBreadcrumbs
   * @return hasBreadcrumbs
   */
  @javax.annotation.Nullable
  public Boolean getHasBreadcrumbs() {
    return hasBreadcrumbs;
  }

  public void setHasBreadcrumbs(Boolean hasBreadcrumbs) {
    this.hasBreadcrumbs = hasBreadcrumbs;
  }


  public ErrorsLatestErrorDetails200Response language(String language) {
    this.language = language;
    return this;
  }

  /**
   * Get language
   * @return language
   */
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public ErrorsLatestErrorDetails200Response osType(String osType) {
    this.osType = osType;
    return this;
  }

  /**
   * Get osType
   * @return osType
   */
  @javax.annotation.Nullable
  public String getOsType() {
    return osType;
  }

  public void setOsType(String osType) {
    this.osType = osType;
  }


  public ErrorsLatestErrorDetails200Response osVersion(String osVersion) {
    this.osVersion = osVersion;
    return this;
  }

  /**
   * Get osVersion
   * @return osVersion
   */
  @javax.annotation.Nullable
  public String getOsVersion() {
    return osVersion;
  }

  public void setOsVersion(String osVersion) {
    this.osVersion = osVersion;
  }


  public ErrorsLatestErrorDetails200Response timestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
    return this;
  }

  /**
   * Get timestamp
   * @return timestamp
   */
  @javax.annotation.Nullable
  public OffsetDateTime getTimestamp() {
    return timestamp;
  }

  public void setTimestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
  }


  public ErrorsLatestErrorDetails200Response userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * Get userId
   * @return userId
   */
  @javax.annotation.Nullable
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ErrorsLatestErrorDetails200Response errorsLatestErrorDetails200Response = (ErrorsLatestErrorDetails200Response) o;
    return Objects.equals(this.appLaunchTimestamp, errorsLatestErrorDetails200Response.appLaunchTimestamp) &&
        Objects.equals(this.carrierName, errorsLatestErrorDetails200Response.carrierName) &&
        Objects.equals(this.jailbreak, errorsLatestErrorDetails200Response.jailbreak) &&
        Objects.equals(this.name, errorsLatestErrorDetails200Response.name) &&
        Objects.equals(this.properties, errorsLatestErrorDetails200Response.properties) &&
        Objects.equals(this.reasonFrames, errorsLatestErrorDetails200Response.reasonFrames) &&
        Objects.equals(this.country, errorsLatestErrorDetails200Response.country) &&
        Objects.equals(this.deviceName, errorsLatestErrorDetails200Response.deviceName) &&
        Objects.equals(this.errorId, errorsLatestErrorDetails200Response.errorId) &&
        Objects.equals(this.hasAttachments, errorsLatestErrorDetails200Response.hasAttachments) &&
        Objects.equals(this.hasBreadcrumbs, errorsLatestErrorDetails200Response.hasBreadcrumbs) &&
        Objects.equals(this.language, errorsLatestErrorDetails200Response.language) &&
        Objects.equals(this.osType, errorsLatestErrorDetails200Response.osType) &&
        Objects.equals(this.osVersion, errorsLatestErrorDetails200Response.osVersion) &&
        Objects.equals(this.timestamp, errorsLatestErrorDetails200Response.timestamp) &&
        Objects.equals(this.userId, errorsLatestErrorDetails200Response.userId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appLaunchTimestamp, carrierName, jailbreak, name, properties, reasonFrames, country, deviceName, errorId, hasAttachments, hasBreadcrumbs, language, osType, osVersion, timestamp, userId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorsLatestErrorDetails200Response {\n");
    sb.append("    appLaunchTimestamp: ").append(toIndentedString(appLaunchTimestamp)).append("\n");
    sb.append("    carrierName: ").append(toIndentedString(carrierName)).append("\n");
    sb.append("    jailbreak: ").append(toIndentedString(jailbreak)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
    sb.append("    reasonFrames: ").append(toIndentedString(reasonFrames)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    deviceName: ").append(toIndentedString(deviceName)).append("\n");
    sb.append("    errorId: ").append(toIndentedString(errorId)).append("\n");
    sb.append("    hasAttachments: ").append(toIndentedString(hasAttachments)).append("\n");
    sb.append("    hasBreadcrumbs: ").append(toIndentedString(hasBreadcrumbs)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    osType: ").append(toIndentedString(osType)).append("\n");
    sb.append("    osVersion: ").append(toIndentedString(osVersion)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
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
    openapiFields.add("country");
    openapiFields.add("deviceName");
    openapiFields.add("errorId");
    openapiFields.add("hasAttachments");
    openapiFields.add("hasBreadcrumbs");
    openapiFields.add("language");
    openapiFields.add("osType");
    openapiFields.add("osVersion");
    openapiFields.add("timestamp");
    openapiFields.add("userId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorsLatestErrorDetails200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorsLatestErrorDetails200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorsLatestErrorDetails200Response is not found in the empty JSON string", ErrorsLatestErrorDetails200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorsLatestErrorDetails200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorsLatestErrorDetails200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("carrierName") != null && !jsonObj.get("carrierName").isJsonNull()) && !jsonObj.get("carrierName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrierName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrierName").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("reasonFrames") != null && !jsonObj.get("reasonFrames").isJsonNull()) {
        JsonArray jsonArrayreasonFrames = jsonObj.getAsJsonArray("reasonFrames");
        if (jsonArrayreasonFrames != null) {
          // ensure the json data is an array
          if (!jsonObj.get("reasonFrames").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `reasonFrames` to be an array in the JSON string but got `%s`", jsonObj.get("reasonFrames").toString()));
          }

          // validate the optional field `reasonFrames` (array)
          for (int i = 0; i < jsonArrayreasonFrames.size(); i++) {
            ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner.validateJsonElement(jsonArrayreasonFrames.get(i));
          };
        }
      }
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if ((jsonObj.get("deviceName") != null && !jsonObj.get("deviceName").isJsonNull()) && !jsonObj.get("deviceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deviceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deviceName").toString()));
      }
      if ((jsonObj.get("errorId") != null && !jsonObj.get("errorId").isJsonNull()) && !jsonObj.get("errorId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `errorId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("errorId").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if ((jsonObj.get("osType") != null && !jsonObj.get("osType").isJsonNull()) && !jsonObj.get("osType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `osType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("osType").toString()));
      }
      if ((jsonObj.get("osVersion") != null && !jsonObj.get("osVersion").isJsonNull()) && !jsonObj.get("osVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `osVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("osVersion").toString()));
      }
      if ((jsonObj.get("userId") != null && !jsonObj.get("userId").isJsonNull()) && !jsonObj.get("userId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `userId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("userId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ErrorsLatestErrorDetails200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorsLatestErrorDetails200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorsLatestErrorDetails200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorsLatestErrorDetails200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorsLatestErrorDetails200Response>() {
           @Override
           public void write(JsonWriter out, ErrorsLatestErrorDetails200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorsLatestErrorDetails200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorsLatestErrorDetails200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorsLatestErrorDetails200Response
   * @throws IOException if the JSON string is invalid with respect to ErrorsLatestErrorDetails200Response
   */
  public static ErrorsLatestErrorDetails200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorsLatestErrorDetails200Response.class);
  }

  /**
   * Convert an instance of ErrorsLatestErrorDetails200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

