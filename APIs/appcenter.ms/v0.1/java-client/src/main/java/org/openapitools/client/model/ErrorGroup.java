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
 * ErrorGroup
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ErrorGroup {
  public static final String SERIALIZED_NAME_APP_BUILD = "appBuild";
  @SerializedName(SERIALIZED_NAME_APP_BUILD)
  private String appBuild;

  public static final String SERIALIZED_NAME_APP_VERSION = "appVersion";
  @SerializedName(SERIALIZED_NAME_APP_VERSION)
  private String appVersion;

  public static final String SERIALIZED_NAME_CODE_RAW = "codeRaw";
  @SerializedName(SERIALIZED_NAME_CODE_RAW)
  private String codeRaw;

  public static final String SERIALIZED_NAME_COUNT = "count";
  @SerializedName(SERIALIZED_NAME_COUNT)
  private Long count;

  public static final String SERIALIZED_NAME_DEVICE_COUNT = "deviceCount";
  @SerializedName(SERIALIZED_NAME_DEVICE_COUNT)
  private Long deviceCount;

  public static final String SERIALIZED_NAME_ERROR_GROUP_ID = "errorGroupId";
  @SerializedName(SERIALIZED_NAME_ERROR_GROUP_ID)
  private String errorGroupId;

  public static final String SERIALIZED_NAME_EXCEPTION_APP_CODE = "exceptionAppCode";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_APP_CODE)
  private Boolean exceptionAppCode;

  public static final String SERIALIZED_NAME_EXCEPTION_CLASS_METHOD = "exceptionClassMethod";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_CLASS_METHOD)
  private Boolean exceptionClassMethod;

  public static final String SERIALIZED_NAME_EXCEPTION_CLASS_NAME = "exceptionClassName";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_CLASS_NAME)
  private String exceptionClassName;

  public static final String SERIALIZED_NAME_EXCEPTION_FILE = "exceptionFile";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_FILE)
  private String exceptionFile;

  public static final String SERIALIZED_NAME_EXCEPTION_LINE = "exceptionLine";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_LINE)
  private String exceptionLine;

  public static final String SERIALIZED_NAME_EXCEPTION_MESSAGE = "exceptionMessage";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_MESSAGE)
  private String exceptionMessage;

  public static final String SERIALIZED_NAME_EXCEPTION_METHOD = "exceptionMethod";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_METHOD)
  private String exceptionMethod;

  public static final String SERIALIZED_NAME_EXCEPTION_TYPE = "exceptionType";
  @SerializedName(SERIALIZED_NAME_EXCEPTION_TYPE)
  private String exceptionType;

  public static final String SERIALIZED_NAME_FIRST_OCCURRENCE = "firstOccurrence";
  @SerializedName(SERIALIZED_NAME_FIRST_OCCURRENCE)
  private OffsetDateTime firstOccurrence;

  public static final String SERIALIZED_NAME_HIDDEN = "hidden";
  @SerializedName(SERIALIZED_NAME_HIDDEN)
  private Boolean hidden;

  public static final String SERIALIZED_NAME_LAST_OCCURRENCE = "lastOccurrence";
  @SerializedName(SERIALIZED_NAME_LAST_OCCURRENCE)
  private OffsetDateTime lastOccurrence;

  public static final String SERIALIZED_NAME_REASON_FRAMES = "reasonFrames";
  @SerializedName(SERIALIZED_NAME_REASON_FRAMES)
  private List<Object> reasonFrames = new ArrayList<>();

  public static final String SERIALIZED_NAME_ANNOTATION = "annotation";
  @SerializedName(SERIALIZED_NAME_ANNOTATION)
  private String annotation;

  /**
   * Gets or Sets state
   */
  @JsonAdapter(StateEnum.Adapter.class)
  public enum StateEnum {
    OPEN("open"),
    
    CLOSED("closed"),
    
    IGNORED("ignored");

    private String value;

    StateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StateEnum fromValue(String value) {
      for (StateEnum b : StateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private StateEnum state;

  public ErrorGroup() {
  }

  public ErrorGroup appBuild(String appBuild) {
    this.appBuild = appBuild;
    return this;
  }

  /**
   * Get appBuild
   * @return appBuild
   */
  @javax.annotation.Nullable
  public String getAppBuild() {
    return appBuild;
  }

  public void setAppBuild(String appBuild) {
    this.appBuild = appBuild;
  }


  public ErrorGroup appVersion(String appVersion) {
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


  public ErrorGroup codeRaw(String codeRaw) {
    this.codeRaw = codeRaw;
    return this;
  }

  /**
   * Get codeRaw
   * @return codeRaw
   */
  @javax.annotation.Nullable
  public String getCodeRaw() {
    return codeRaw;
  }

  public void setCodeRaw(String codeRaw) {
    this.codeRaw = codeRaw;
  }


  public ErrorGroup count(Long count) {
    this.count = count;
    return this;
  }

  /**
   * Get count
   * @return count
   */
  @javax.annotation.Nonnull
  public Long getCount() {
    return count;
  }

  public void setCount(Long count) {
    this.count = count;
  }


  public ErrorGroup deviceCount(Long deviceCount) {
    this.deviceCount = deviceCount;
    return this;
  }

  /**
   * Get deviceCount
   * @return deviceCount
   */
  @javax.annotation.Nonnull
  public Long getDeviceCount() {
    return deviceCount;
  }

  public void setDeviceCount(Long deviceCount) {
    this.deviceCount = deviceCount;
  }


  public ErrorGroup errorGroupId(String errorGroupId) {
    this.errorGroupId = errorGroupId;
    return this;
  }

  /**
   * Get errorGroupId
   * @return errorGroupId
   */
  @javax.annotation.Nonnull
  public String getErrorGroupId() {
    return errorGroupId;
  }

  public void setErrorGroupId(String errorGroupId) {
    this.errorGroupId = errorGroupId;
  }


  public ErrorGroup exceptionAppCode(Boolean exceptionAppCode) {
    this.exceptionAppCode = exceptionAppCode;
    return this;
  }

  /**
   * Get exceptionAppCode
   * @return exceptionAppCode
   */
  @javax.annotation.Nullable
  public Boolean getExceptionAppCode() {
    return exceptionAppCode;
  }

  public void setExceptionAppCode(Boolean exceptionAppCode) {
    this.exceptionAppCode = exceptionAppCode;
  }


  public ErrorGroup exceptionClassMethod(Boolean exceptionClassMethod) {
    this.exceptionClassMethod = exceptionClassMethod;
    return this;
  }

  /**
   * Get exceptionClassMethod
   * @return exceptionClassMethod
   */
  @javax.annotation.Nullable
  public Boolean getExceptionClassMethod() {
    return exceptionClassMethod;
  }

  public void setExceptionClassMethod(Boolean exceptionClassMethod) {
    this.exceptionClassMethod = exceptionClassMethod;
  }


  public ErrorGroup exceptionClassName(String exceptionClassName) {
    this.exceptionClassName = exceptionClassName;
    return this;
  }

  /**
   * Get exceptionClassName
   * @return exceptionClassName
   */
  @javax.annotation.Nullable
  public String getExceptionClassName() {
    return exceptionClassName;
  }

  public void setExceptionClassName(String exceptionClassName) {
    this.exceptionClassName = exceptionClassName;
  }


  public ErrorGroup exceptionFile(String exceptionFile) {
    this.exceptionFile = exceptionFile;
    return this;
  }

  /**
   * Get exceptionFile
   * @return exceptionFile
   */
  @javax.annotation.Nullable
  public String getExceptionFile() {
    return exceptionFile;
  }

  public void setExceptionFile(String exceptionFile) {
    this.exceptionFile = exceptionFile;
  }


  public ErrorGroup exceptionLine(String exceptionLine) {
    this.exceptionLine = exceptionLine;
    return this;
  }

  /**
   * Get exceptionLine
   * @return exceptionLine
   */
  @javax.annotation.Nullable
  public String getExceptionLine() {
    return exceptionLine;
  }

  public void setExceptionLine(String exceptionLine) {
    this.exceptionLine = exceptionLine;
  }


  public ErrorGroup exceptionMessage(String exceptionMessage) {
    this.exceptionMessage = exceptionMessage;
    return this;
  }

  /**
   * Get exceptionMessage
   * @return exceptionMessage
   */
  @javax.annotation.Nullable
  public String getExceptionMessage() {
    return exceptionMessage;
  }

  public void setExceptionMessage(String exceptionMessage) {
    this.exceptionMessage = exceptionMessage;
  }


  public ErrorGroup exceptionMethod(String exceptionMethod) {
    this.exceptionMethod = exceptionMethod;
    return this;
  }

  /**
   * Get exceptionMethod
   * @return exceptionMethod
   */
  @javax.annotation.Nullable
  public String getExceptionMethod() {
    return exceptionMethod;
  }

  public void setExceptionMethod(String exceptionMethod) {
    this.exceptionMethod = exceptionMethod;
  }


  public ErrorGroup exceptionType(String exceptionType) {
    this.exceptionType = exceptionType;
    return this;
  }

  /**
   * Get exceptionType
   * @return exceptionType
   */
  @javax.annotation.Nullable
  public String getExceptionType() {
    return exceptionType;
  }

  public void setExceptionType(String exceptionType) {
    this.exceptionType = exceptionType;
  }


  public ErrorGroup firstOccurrence(OffsetDateTime firstOccurrence) {
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


  public ErrorGroup hidden(Boolean hidden) {
    this.hidden = hidden;
    return this;
  }

  /**
   * Get hidden
   * @return hidden
   */
  @javax.annotation.Nullable
  public Boolean getHidden() {
    return hidden;
  }

  public void setHidden(Boolean hidden) {
    this.hidden = hidden;
  }


  public ErrorGroup lastOccurrence(OffsetDateTime lastOccurrence) {
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


  public ErrorGroup reasonFrames(List<Object> reasonFrames) {
    this.reasonFrames = reasonFrames;
    return this;
  }

  public ErrorGroup addReasonFramesItem(Object reasonFramesItem) {
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
  public List<Object> getReasonFrames() {
    return reasonFrames;
  }

  public void setReasonFrames(List<Object> reasonFrames) {
    this.reasonFrames = reasonFrames;
  }


  public ErrorGroup annotation(String annotation) {
    this.annotation = annotation;
    return this;
  }

  /**
   * Get annotation
   * @return annotation
   */
  @javax.annotation.Nullable
  public String getAnnotation() {
    return annotation;
  }

  public void setAnnotation(String annotation) {
    this.annotation = annotation;
  }


  public ErrorGroup state(StateEnum state) {
    this.state = state;
    return this;
  }

  /**
   * Get state
   * @return state
   */
  @javax.annotation.Nonnull
  public StateEnum getState() {
    return state;
  }

  public void setState(StateEnum state) {
    this.state = state;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ErrorGroup errorGroup = (ErrorGroup) o;
    return Objects.equals(this.appBuild, errorGroup.appBuild) &&
        Objects.equals(this.appVersion, errorGroup.appVersion) &&
        Objects.equals(this.codeRaw, errorGroup.codeRaw) &&
        Objects.equals(this.count, errorGroup.count) &&
        Objects.equals(this.deviceCount, errorGroup.deviceCount) &&
        Objects.equals(this.errorGroupId, errorGroup.errorGroupId) &&
        Objects.equals(this.exceptionAppCode, errorGroup.exceptionAppCode) &&
        Objects.equals(this.exceptionClassMethod, errorGroup.exceptionClassMethod) &&
        Objects.equals(this.exceptionClassName, errorGroup.exceptionClassName) &&
        Objects.equals(this.exceptionFile, errorGroup.exceptionFile) &&
        Objects.equals(this.exceptionLine, errorGroup.exceptionLine) &&
        Objects.equals(this.exceptionMessage, errorGroup.exceptionMessage) &&
        Objects.equals(this.exceptionMethod, errorGroup.exceptionMethod) &&
        Objects.equals(this.exceptionType, errorGroup.exceptionType) &&
        Objects.equals(this.firstOccurrence, errorGroup.firstOccurrence) &&
        Objects.equals(this.hidden, errorGroup.hidden) &&
        Objects.equals(this.lastOccurrence, errorGroup.lastOccurrence) &&
        Objects.equals(this.reasonFrames, errorGroup.reasonFrames) &&
        Objects.equals(this.annotation, errorGroup.annotation) &&
        Objects.equals(this.state, errorGroup.state);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appBuild, appVersion, codeRaw, count, deviceCount, errorGroupId, exceptionAppCode, exceptionClassMethod, exceptionClassName, exceptionFile, exceptionLine, exceptionMessage, exceptionMethod, exceptionType, firstOccurrence, hidden, lastOccurrence, reasonFrames, annotation, state);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ErrorGroup {\n");
    sb.append("    appBuild: ").append(toIndentedString(appBuild)).append("\n");
    sb.append("    appVersion: ").append(toIndentedString(appVersion)).append("\n");
    sb.append("    codeRaw: ").append(toIndentedString(codeRaw)).append("\n");
    sb.append("    count: ").append(toIndentedString(count)).append("\n");
    sb.append("    deviceCount: ").append(toIndentedString(deviceCount)).append("\n");
    sb.append("    errorGroupId: ").append(toIndentedString(errorGroupId)).append("\n");
    sb.append("    exceptionAppCode: ").append(toIndentedString(exceptionAppCode)).append("\n");
    sb.append("    exceptionClassMethod: ").append(toIndentedString(exceptionClassMethod)).append("\n");
    sb.append("    exceptionClassName: ").append(toIndentedString(exceptionClassName)).append("\n");
    sb.append("    exceptionFile: ").append(toIndentedString(exceptionFile)).append("\n");
    sb.append("    exceptionLine: ").append(toIndentedString(exceptionLine)).append("\n");
    sb.append("    exceptionMessage: ").append(toIndentedString(exceptionMessage)).append("\n");
    sb.append("    exceptionMethod: ").append(toIndentedString(exceptionMethod)).append("\n");
    sb.append("    exceptionType: ").append(toIndentedString(exceptionType)).append("\n");
    sb.append("    firstOccurrence: ").append(toIndentedString(firstOccurrence)).append("\n");
    sb.append("    hidden: ").append(toIndentedString(hidden)).append("\n");
    sb.append("    lastOccurrence: ").append(toIndentedString(lastOccurrence)).append("\n");
    sb.append("    reasonFrames: ").append(toIndentedString(reasonFrames)).append("\n");
    sb.append("    annotation: ").append(toIndentedString(annotation)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
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
    openapiFields.add("state");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("appVersion");
    openapiRequiredFields.add("count");
    openapiRequiredFields.add("deviceCount");
    openapiRequiredFields.add("errorGroupId");
    openapiRequiredFields.add("firstOccurrence");
    openapiRequiredFields.add("lastOccurrence");
    openapiRequiredFields.add("state");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ErrorGroup
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ErrorGroup.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ErrorGroup is not found in the empty JSON string", ErrorGroup.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ErrorGroup.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ErrorGroup` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ErrorGroup.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appBuild") != null && !jsonObj.get("appBuild").isJsonNull()) && !jsonObj.get("appBuild").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appBuild` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appBuild").toString()));
      }
      if (!jsonObj.get("appVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appVersion").toString()));
      }
      if ((jsonObj.get("codeRaw") != null && !jsonObj.get("codeRaw").isJsonNull()) && !jsonObj.get("codeRaw").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `codeRaw` to be a primitive type in the JSON string but got `%s`", jsonObj.get("codeRaw").toString()));
      }
      if (!jsonObj.get("errorGroupId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `errorGroupId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("errorGroupId").toString()));
      }
      if ((jsonObj.get("exceptionClassName") != null && !jsonObj.get("exceptionClassName").isJsonNull()) && !jsonObj.get("exceptionClassName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exceptionClassName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exceptionClassName").toString()));
      }
      if ((jsonObj.get("exceptionFile") != null && !jsonObj.get("exceptionFile").isJsonNull()) && !jsonObj.get("exceptionFile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exceptionFile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exceptionFile").toString()));
      }
      if ((jsonObj.get("exceptionLine") != null && !jsonObj.get("exceptionLine").isJsonNull()) && !jsonObj.get("exceptionLine").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exceptionLine` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exceptionLine").toString()));
      }
      if ((jsonObj.get("exceptionMessage") != null && !jsonObj.get("exceptionMessage").isJsonNull()) && !jsonObj.get("exceptionMessage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exceptionMessage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exceptionMessage").toString()));
      }
      if ((jsonObj.get("exceptionMethod") != null && !jsonObj.get("exceptionMethod").isJsonNull()) && !jsonObj.get("exceptionMethod").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exceptionMethod` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exceptionMethod").toString()));
      }
      if ((jsonObj.get("exceptionType") != null && !jsonObj.get("exceptionType").isJsonNull()) && !jsonObj.get("exceptionType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exceptionType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exceptionType").toString()));
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
            Object.validateJsonElement(jsonArrayreasonFrames.get(i));
          };
        }
      }
      if ((jsonObj.get("annotation") != null && !jsonObj.get("annotation").isJsonNull()) && !jsonObj.get("annotation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `annotation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("annotation").toString()));
      }
      if (!jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      // validate the required field `state`
      StateEnum.validateJsonElement(jsonObj.get("state"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ErrorGroup.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ErrorGroup' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ErrorGroup> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ErrorGroup.class));

       return (TypeAdapter<T>) new TypeAdapter<ErrorGroup>() {
           @Override
           public void write(JsonWriter out, ErrorGroup value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ErrorGroup read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ErrorGroup given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ErrorGroup
   * @throws IOException if the JSON string is invalid with respect to ErrorGroup
   */
  public static ErrorGroup fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ErrorGroup.class);
  }

  /**
   * Convert an instance of ErrorGroup to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

