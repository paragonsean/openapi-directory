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
import java.util.Arrays;
import org.openapitools.client.model.CrashGroupsList200ResponseCrashGroupsInnerReasonFrame;

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
 * CrashGroupsList200ResponseCrashGroupsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CrashGroupsList200ResponseCrashGroupsInner {
  public static final String SERIALIZED_NAME_ANNOTATION = "annotation";
  @SerializedName(SERIALIZED_NAME_ANNOTATION)
  private String annotation;

  public static final String SERIALIZED_NAME_APP_VERSION = "app_version";
  @SerializedName(SERIALIZED_NAME_APP_VERSION)
  private String appVersion;

  public static final String SERIALIZED_NAME_BUILD = "build";
  @SerializedName(SERIALIZED_NAME_BUILD)
  private String build;

  public static final String SERIALIZED_NAME_COUNT = "count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Integer count;

  public static final String SERIALIZED_NAME_CRASH_GROUP_ID = "crash_group_id";
  @SerializedName(SERIALIZED_NAME_CRASH_GROUP_ID)
  private String crashGroupId;

  public static final String SERIALIZED_NAME_CRASH_REASON = "crash_reason";
  @SerializedName(SERIALIZED_NAME_CRASH_REASON)
  private String crashReason;

  public static final String SERIALIZED_NAME_DISPLAY_ID = "display_id";
  @SerializedName(SERIALIZED_NAME_DISPLAY_ID)
  private String displayId;

  public static final String SERIALIZED_NAME_EXCEPTION = "exception";
  @SerializedName(SERIALIZED_NAME_EXCEPTION)
  private String exception;

  public static final String SERIALIZED_NAME_FATAL = "fatal";
  @SerializedName(SERIALIZED_NAME_FATAL)
  private Boolean fatal;

  public static final String SERIALIZED_NAME_FIRST_OCCURRENCE = "first_occurrence";
  @SerializedName(SERIALIZED_NAME_FIRST_OCCURRENCE)
  private OffsetDateTime firstOccurrence;

  public static final String SERIALIZED_NAME_IMPACTED_USERS = "impacted_users";
  @SerializedName(SERIALIZED_NAME_IMPACTED_USERS)
  private Integer impactedUsers;

  public static final String SERIALIZED_NAME_LAST_OCCURRENCE = "last_occurrence";
  @SerializedName(SERIALIZED_NAME_LAST_OCCURRENCE)
  private OffsetDateTime lastOccurrence;

  public static final String SERIALIZED_NAME_NEW_CRASH_GROUP_ID = "new_crash_group_id";
  @SerializedName(SERIALIZED_NAME_NEW_CRASH_GROUP_ID)
  private String newCrashGroupId;

  public static final String SERIALIZED_NAME_REASON_FRAME = "reason_frame";
  @SerializedName(SERIALIZED_NAME_REASON_FRAME)
  private CrashGroupsList200ResponseCrashGroupsInnerReasonFrame reasonFrame;

  /**
   * Gets or Sets status
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    OPEN("open"),
    
    CLOSED("closed"),
    
    IGNORED("ignored");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public CrashGroupsList200ResponseCrashGroupsInner() {
  }

  public CrashGroupsList200ResponseCrashGroupsInner annotation(String annotation) {
    this.annotation = annotation;
    return this;
  }

  /**
   * Get annotation
   * @return annotation
   */
  @javax.annotation.Nonnull
  public String getAnnotation() {
    return annotation;
  }

  public void setAnnotation(String annotation) {
    this.annotation = annotation;
  }


  public CrashGroupsList200ResponseCrashGroupsInner appVersion(String appVersion) {
    this.appVersion = appVersion;
    return this;
  }

  /**
   * Get appVersion
   * @return appVersion
   */
  @javax.annotation.Nonnull
  public String getAppVersion() {
    return appVersion;
  }

  public void setAppVersion(String appVersion) {
    this.appVersion = appVersion;
  }


  public CrashGroupsList200ResponseCrashGroupsInner build(String build) {
    this.build = build;
    return this;
  }

  /**
   * Get build
   * @return build
   */
  @javax.annotation.Nonnull
  public String getBuild() {
    return build;
  }

  public void setBuild(String build) {
    this.build = build;
  }


  public CrashGroupsList200ResponseCrashGroupsInner count(Integer count) {
    this.count = count;
    return this;
  }

  /**
   * Get count
   * @return count
   */
  @javax.annotation.Nonnull
  public Integer getCount() {
    return count;
  }

  public void setCount(Integer count) {
    this.count = count;
  }


  public CrashGroupsList200ResponseCrashGroupsInner crashGroupId(String crashGroupId) {
    this.crashGroupId = crashGroupId;
    return this;
  }

  /**
   * Get crashGroupId
   * @return crashGroupId
   */
  @javax.annotation.Nonnull
  public String getCrashGroupId() {
    return crashGroupId;
  }

  public void setCrashGroupId(String crashGroupId) {
    this.crashGroupId = crashGroupId;
  }


  public CrashGroupsList200ResponseCrashGroupsInner crashReason(String crashReason) {
    this.crashReason = crashReason;
    return this;
  }

  /**
   * Get crashReason
   * @return crashReason
   */
  @javax.annotation.Nonnull
  public String getCrashReason() {
    return crashReason;
  }

  public void setCrashReason(String crashReason) {
    this.crashReason = crashReason;
  }


  public CrashGroupsList200ResponseCrashGroupsInner displayId(String displayId) {
    this.displayId = displayId;
    return this;
  }

  /**
   * Get displayId
   * @return displayId
   */
  @javax.annotation.Nonnull
  public String getDisplayId() {
    return displayId;
  }

  public void setDisplayId(String displayId) {
    this.displayId = displayId;
  }


  public CrashGroupsList200ResponseCrashGroupsInner exception(String exception) {
    this.exception = exception;
    return this;
  }

  /**
   * Get exception
   * @return exception
   */
  @javax.annotation.Nullable
  public String getException() {
    return exception;
  }

  public void setException(String exception) {
    this.exception = exception;
  }


  public CrashGroupsList200ResponseCrashGroupsInner fatal(Boolean fatal) {
    this.fatal = fatal;
    return this;
  }

  /**
   * Crash or handled exception
   * @return fatal
   */
  @javax.annotation.Nonnull
  public Boolean getFatal() {
    return fatal;
  }

  public void setFatal(Boolean fatal) {
    this.fatal = fatal;
  }


  public CrashGroupsList200ResponseCrashGroupsInner firstOccurrence(OffsetDateTime firstOccurrence) {
    this.firstOccurrence = firstOccurrence;
    return this;
  }

  /**
   * Get firstOccurrence
   * @return firstOccurrence
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getFirstOccurrence() {
    return firstOccurrence;
  }

  public void setFirstOccurrence(OffsetDateTime firstOccurrence) {
    this.firstOccurrence = firstOccurrence;
  }


  public CrashGroupsList200ResponseCrashGroupsInner impactedUsers(Integer impactedUsers) {
    this.impactedUsers = impactedUsers;
    return this;
  }

  /**
   * Get impactedUsers
   * @return impactedUsers
   */
  @javax.annotation.Nullable
  public Integer getImpactedUsers() {
    return impactedUsers;
  }

  public void setImpactedUsers(Integer impactedUsers) {
    this.impactedUsers = impactedUsers;
  }


  public CrashGroupsList200ResponseCrashGroupsInner lastOccurrence(OffsetDateTime lastOccurrence) {
    this.lastOccurrence = lastOccurrence;
    return this;
  }

  /**
   * Get lastOccurrence
   * @return lastOccurrence
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getLastOccurrence() {
    return lastOccurrence;
  }

  public void setLastOccurrence(OffsetDateTime lastOccurrence) {
    this.lastOccurrence = lastOccurrence;
  }


  public CrashGroupsList200ResponseCrashGroupsInner newCrashGroupId(String newCrashGroupId) {
    this.newCrashGroupId = newCrashGroupId;
    return this;
  }

  /**
   * Get newCrashGroupId
   * @return newCrashGroupId
   */
  @javax.annotation.Nonnull
  public String getNewCrashGroupId() {
    return newCrashGroupId;
  }

  public void setNewCrashGroupId(String newCrashGroupId) {
    this.newCrashGroupId = newCrashGroupId;
  }


  public CrashGroupsList200ResponseCrashGroupsInner reasonFrame(CrashGroupsList200ResponseCrashGroupsInnerReasonFrame reasonFrame) {
    this.reasonFrame = reasonFrame;
    return this;
  }

  /**
   * Get reasonFrame
   * @return reasonFrame
   */
  @javax.annotation.Nullable
  public CrashGroupsList200ResponseCrashGroupsInnerReasonFrame getReasonFrame() {
    return reasonFrame;
  }

  public void setReasonFrame(CrashGroupsList200ResponseCrashGroupsInnerReasonFrame reasonFrame) {
    this.reasonFrame = reasonFrame;
  }


  public CrashGroupsList200ResponseCrashGroupsInner status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CrashGroupsList200ResponseCrashGroupsInner crashGroupsList200ResponseCrashGroupsInner = (CrashGroupsList200ResponseCrashGroupsInner) o;
    return Objects.equals(this.annotation, crashGroupsList200ResponseCrashGroupsInner.annotation) &&
        Objects.equals(this.appVersion, crashGroupsList200ResponseCrashGroupsInner.appVersion) &&
        Objects.equals(this.build, crashGroupsList200ResponseCrashGroupsInner.build) &&
        Objects.equals(this.count, crashGroupsList200ResponseCrashGroupsInner.count) &&
        Objects.equals(this.crashGroupId, crashGroupsList200ResponseCrashGroupsInner.crashGroupId) &&
        Objects.equals(this.crashReason, crashGroupsList200ResponseCrashGroupsInner.crashReason) &&
        Objects.equals(this.displayId, crashGroupsList200ResponseCrashGroupsInner.displayId) &&
        Objects.equals(this.exception, crashGroupsList200ResponseCrashGroupsInner.exception) &&
        Objects.equals(this.fatal, crashGroupsList200ResponseCrashGroupsInner.fatal) &&
        Objects.equals(this.firstOccurrence, crashGroupsList200ResponseCrashGroupsInner.firstOccurrence) &&
        Objects.equals(this.impactedUsers, crashGroupsList200ResponseCrashGroupsInner.impactedUsers) &&
        Objects.equals(this.lastOccurrence, crashGroupsList200ResponseCrashGroupsInner.lastOccurrence) &&
        Objects.equals(this.newCrashGroupId, crashGroupsList200ResponseCrashGroupsInner.newCrashGroupId) &&
        Objects.equals(this.reasonFrame, crashGroupsList200ResponseCrashGroupsInner.reasonFrame) &&
        Objects.equals(this.status, crashGroupsList200ResponseCrashGroupsInner.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(annotation, appVersion, build, count, crashGroupId, crashReason, displayId, exception, fatal, firstOccurrence, impactedUsers, lastOccurrence, newCrashGroupId, reasonFrame, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CrashGroupsList200ResponseCrashGroupsInner {\n");
    sb.append("    annotation: ").append(toIndentedString(annotation)).append("\n");
    sb.append("    appVersion: ").append(toIndentedString(appVersion)).append("\n");
    sb.append("    build: ").append(toIndentedString(build)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    crashGroupId: ").append(toIndentedString(crashGroupId)).append("\n");
    sb.append("    crashReason: ").append(toIndentedString(crashReason)).append("\n");
    sb.append("    displayId: ").append(toIndentedString(displayId)).append("\n");
    sb.append("    exception: ").append(toIndentedString(exception)).append("\n");
    sb.append("    fatal: ").append(toIndentedString(fatal)).append("\n");
    sb.append("    firstOccurrence: ").append(toIndentedString(firstOccurrence)).append("\n");
    sb.append("    impactedUsers: ").append(toIndentedString(impactedUsers)).append("\n");
    sb.append("    lastOccurrence: ").append(toIndentedString(lastOccurrence)).append("\n");
    sb.append("    newCrashGroupId: ").append(toIndentedString(newCrashGroupId)).append("\n");
    sb.append("    reasonFrame: ").append(toIndentedString(reasonFrame)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("annotation");
    openapiFields.add("app_version");
    openapiFields.add("build");
    openapiFields.add("count");
    openapiFields.add("crash_group_id");
    openapiFields.add("crash_reason");
    openapiFields.add("display_id");
    openapiFields.add("exception");
    openapiFields.add("fatal");
    openapiFields.add("first_occurrence");
    openapiFields.add("impacted_users");
    openapiFields.add("last_occurrence");
    openapiFields.add("new_crash_group_id");
    openapiFields.add("reason_frame");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("annotation");
    openapiRequiredFields.add("app_version");
    openapiRequiredFields.add("build");
    openapiRequiredFields.add("count");
    openapiRequiredFields.add("crash_group_id");
    openapiRequiredFields.add("crash_reason");
    openapiRequiredFields.add("display_id");
    openapiRequiredFields.add("fatal");
    openapiRequiredFields.add("first_occurrence");
    openapiRequiredFields.add("last_occurrence");
    openapiRequiredFields.add("new_crash_group_id");
    openapiRequiredFields.add("status");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CrashGroupsList200ResponseCrashGroupsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CrashGroupsList200ResponseCrashGroupsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CrashGroupsList200ResponseCrashGroupsInner is not found in the empty JSON string", CrashGroupsList200ResponseCrashGroupsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CrashGroupsList200ResponseCrashGroupsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CrashGroupsList200ResponseCrashGroupsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CrashGroupsList200ResponseCrashGroupsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("annotation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `annotation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("annotation").toString()));
      }
      if (!jsonObj.get("app_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `app_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("app_version").toString()));
      }
      if (!jsonObj.get("build").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `build` to be a primitive type in the JSON string but got `%s`", jsonObj.get("build").toString()));
      }
      if (!jsonObj.get("crash_group_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `crash_group_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("crash_group_id").toString()));
      }
      if (!jsonObj.get("crash_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `crash_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("crash_reason").toString()));
      }
      if (!jsonObj.get("display_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display_id").toString()));
      }
      if ((jsonObj.get("exception") != null && !jsonObj.get("exception").isJsonNull()) && !jsonObj.get("exception").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exception` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exception").toString()));
      }
      if (!jsonObj.get("new_crash_group_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `new_crash_group_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("new_crash_group_id").toString()));
      }
      // validate the optional field `reason_frame`
      if (jsonObj.get("reason_frame") != null && !jsonObj.get("reason_frame").isJsonNull()) {
        CrashGroupsList200ResponseCrashGroupsInnerReasonFrame.validateJsonElement(jsonObj.get("reason_frame"));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CrashGroupsList200ResponseCrashGroupsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CrashGroupsList200ResponseCrashGroupsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CrashGroupsList200ResponseCrashGroupsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CrashGroupsList200ResponseCrashGroupsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<CrashGroupsList200ResponseCrashGroupsInner>() {
           @Override
           public void write(JsonWriter out, CrashGroupsList200ResponseCrashGroupsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CrashGroupsList200ResponseCrashGroupsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CrashGroupsList200ResponseCrashGroupsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CrashGroupsList200ResponseCrashGroupsInner
   * @throws IOException if the JSON string is invalid with respect to CrashGroupsList200ResponseCrashGroupsInner
   */
  public static CrashGroupsList200ResponseCrashGroupsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CrashGroupsList200ResponseCrashGroupsInner.class);
  }

  /**
   * Convert an instance of CrashGroupsList200ResponseCrashGroupsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

