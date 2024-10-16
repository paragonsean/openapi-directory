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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.StepReportDeviceScreenshotsInnerScreenshot;

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
 * StepReportDeviceScreenshotsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StepReportDeviceScreenshotsInner {
  public static final String SERIALIZED_NAME_APPIUM_LOG_FILE = "appium_log_file";
  @SerializedName(SERIALIZED_NAME_APPIUM_LOG_FILE)
  private String appiumLogFile;

  public static final String SERIALIZED_NAME_CRASH_DATA = "crash_data";
  @SerializedName(SERIALIZED_NAME_CRASH_DATA)
  private List<String> crashData = new ArrayList<>();

  public static final String SERIALIZED_NAME_DEVICE_SNAPSHOT_ID = "device_snapshot_id";
  @SerializedName(SERIALIZED_NAME_DEVICE_SNAPSHOT_ID)
  private String deviceSnapshotId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LOG_FILE = "log_file";
  @SerializedName(SERIALIZED_NAME_LOG_FILE)
  private String logFile;

  public static final String SERIALIZED_NAME_RAW_CRASH_DATA = "raw_crash_data";
  @SerializedName(SERIALIZED_NAME_RAW_CRASH_DATA)
  private List<String> rawCrashData = new ArrayList<>();

  public static final String SERIALIZED_NAME_SCREENSHOT = "screenshot";
  @SerializedName(SERIALIZED_NAME_SCREENSHOT)
  private StepReportDeviceScreenshotsInnerScreenshot screenshot;

  public static final String SERIALIZED_NAME_STACKTRACE = "stacktrace";
  @SerializedName(SERIALIZED_NAME_STACKTRACE)
  private List<String> stacktrace = new ArrayList<>();

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public StepReportDeviceScreenshotsInner() {
  }

  public StepReportDeviceScreenshotsInner appiumLogFile(String appiumLogFile) {
    this.appiumLogFile = appiumLogFile;
    return this;
  }

  /**
   * Get appiumLogFile
   * @return appiumLogFile
   */
  @javax.annotation.Nullable
  public String getAppiumLogFile() {
    return appiumLogFile;
  }

  public void setAppiumLogFile(String appiumLogFile) {
    this.appiumLogFile = appiumLogFile;
  }


  public StepReportDeviceScreenshotsInner crashData(List<String> crashData) {
    this.crashData = crashData;
    return this;
  }

  public StepReportDeviceScreenshotsInner addCrashDataItem(String crashDataItem) {
    if (this.crashData == null) {
      this.crashData = new ArrayList<>();
    }
    this.crashData.add(crashDataItem);
    return this;
  }

  /**
   * Get crashData
   * @return crashData
   */
  @javax.annotation.Nullable
  public List<String> getCrashData() {
    return crashData;
  }

  public void setCrashData(List<String> crashData) {
    this.crashData = crashData;
  }


  public StepReportDeviceScreenshotsInner deviceSnapshotId(String deviceSnapshotId) {
    this.deviceSnapshotId = deviceSnapshotId;
    return this;
  }

  /**
   * Get deviceSnapshotId
   * @return deviceSnapshotId
   */
  @javax.annotation.Nullable
  public String getDeviceSnapshotId() {
    return deviceSnapshotId;
  }

  public void setDeviceSnapshotId(String deviceSnapshotId) {
    this.deviceSnapshotId = deviceSnapshotId;
  }


  public StepReportDeviceScreenshotsInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public StepReportDeviceScreenshotsInner logFile(String logFile) {
    this.logFile = logFile;
    return this;
  }

  /**
   * Get logFile
   * @return logFile
   */
  @javax.annotation.Nullable
  public String getLogFile() {
    return logFile;
  }

  public void setLogFile(String logFile) {
    this.logFile = logFile;
  }


  public StepReportDeviceScreenshotsInner rawCrashData(List<String> rawCrashData) {
    this.rawCrashData = rawCrashData;
    return this;
  }

  public StepReportDeviceScreenshotsInner addRawCrashDataItem(String rawCrashDataItem) {
    if (this.rawCrashData == null) {
      this.rawCrashData = new ArrayList<>();
    }
    this.rawCrashData.add(rawCrashDataItem);
    return this;
  }

  /**
   * Get rawCrashData
   * @return rawCrashData
   */
  @javax.annotation.Nullable
  public List<String> getRawCrashData() {
    return rawCrashData;
  }

  public void setRawCrashData(List<String> rawCrashData) {
    this.rawCrashData = rawCrashData;
  }


  public StepReportDeviceScreenshotsInner screenshot(StepReportDeviceScreenshotsInnerScreenshot screenshot) {
    this.screenshot = screenshot;
    return this;
  }

  /**
   * Get screenshot
   * @return screenshot
   */
  @javax.annotation.Nullable
  public StepReportDeviceScreenshotsInnerScreenshot getScreenshot() {
    return screenshot;
  }

  public void setScreenshot(StepReportDeviceScreenshotsInnerScreenshot screenshot) {
    this.screenshot = screenshot;
  }


  public StepReportDeviceScreenshotsInner stacktrace(List<String> stacktrace) {
    this.stacktrace = stacktrace;
    return this;
  }

  public StepReportDeviceScreenshotsInner addStacktraceItem(String stacktraceItem) {
    if (this.stacktrace == null) {
      this.stacktrace = new ArrayList<>();
    }
    this.stacktrace.add(stacktraceItem);
    return this;
  }

  /**
   * Get stacktrace
   * @return stacktrace
   */
  @javax.annotation.Nullable
  public List<String> getStacktrace() {
    return stacktrace;
  }

  public void setStacktrace(List<String> stacktrace) {
    this.stacktrace = stacktrace;
  }


  public StepReportDeviceScreenshotsInner status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public StepReportDeviceScreenshotsInner title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StepReportDeviceScreenshotsInner stepReportDeviceScreenshotsInner = (StepReportDeviceScreenshotsInner) o;
    return Objects.equals(this.appiumLogFile, stepReportDeviceScreenshotsInner.appiumLogFile) &&
        Objects.equals(this.crashData, stepReportDeviceScreenshotsInner.crashData) &&
        Objects.equals(this.deviceSnapshotId, stepReportDeviceScreenshotsInner.deviceSnapshotId) &&
        Objects.equals(this.id, stepReportDeviceScreenshotsInner.id) &&
        Objects.equals(this.logFile, stepReportDeviceScreenshotsInner.logFile) &&
        Objects.equals(this.rawCrashData, stepReportDeviceScreenshotsInner.rawCrashData) &&
        Objects.equals(this.screenshot, stepReportDeviceScreenshotsInner.screenshot) &&
        Objects.equals(this.stacktrace, stepReportDeviceScreenshotsInner.stacktrace) &&
        Objects.equals(this.status, stepReportDeviceScreenshotsInner.status) &&
        Objects.equals(this.title, stepReportDeviceScreenshotsInner.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appiumLogFile, crashData, deviceSnapshotId, id, logFile, rawCrashData, screenshot, stacktrace, status, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StepReportDeviceScreenshotsInner {\n");
    sb.append("    appiumLogFile: ").append(toIndentedString(appiumLogFile)).append("\n");
    sb.append("    crashData: ").append(toIndentedString(crashData)).append("\n");
    sb.append("    deviceSnapshotId: ").append(toIndentedString(deviceSnapshotId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    logFile: ").append(toIndentedString(logFile)).append("\n");
    sb.append("    rawCrashData: ").append(toIndentedString(rawCrashData)).append("\n");
    sb.append("    screenshot: ").append(toIndentedString(screenshot)).append("\n");
    sb.append("    stacktrace: ").append(toIndentedString(stacktrace)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("appium_log_file");
    openapiFields.add("crash_data");
    openapiFields.add("device_snapshot_id");
    openapiFields.add("id");
    openapiFields.add("log_file");
    openapiFields.add("raw_crash_data");
    openapiFields.add("screenshot");
    openapiFields.add("stacktrace");
    openapiFields.add("status");
    openapiFields.add("title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StepReportDeviceScreenshotsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StepReportDeviceScreenshotsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StepReportDeviceScreenshotsInner is not found in the empty JSON string", StepReportDeviceScreenshotsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StepReportDeviceScreenshotsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StepReportDeviceScreenshotsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appium_log_file") != null && !jsonObj.get("appium_log_file").isJsonNull()) && !jsonObj.get("appium_log_file").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appium_log_file` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appium_log_file").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("crash_data") != null && !jsonObj.get("crash_data").isJsonNull() && !jsonObj.get("crash_data").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `crash_data` to be an array in the JSON string but got `%s`", jsonObj.get("crash_data").toString()));
      }
      if ((jsonObj.get("device_snapshot_id") != null && !jsonObj.get("device_snapshot_id").isJsonNull()) && !jsonObj.get("device_snapshot_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `device_snapshot_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("device_snapshot_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("log_file") != null && !jsonObj.get("log_file").isJsonNull()) && !jsonObj.get("log_file").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `log_file` to be a primitive type in the JSON string but got `%s`", jsonObj.get("log_file").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("raw_crash_data") != null && !jsonObj.get("raw_crash_data").isJsonNull() && !jsonObj.get("raw_crash_data").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `raw_crash_data` to be an array in the JSON string but got `%s`", jsonObj.get("raw_crash_data").toString()));
      }
      // validate the optional field `screenshot`
      if (jsonObj.get("screenshot") != null && !jsonObj.get("screenshot").isJsonNull()) {
        StepReportDeviceScreenshotsInnerScreenshot.validateJsonElement(jsonObj.get("screenshot"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("stacktrace") != null && !jsonObj.get("stacktrace").isJsonNull() && !jsonObj.get("stacktrace").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `stacktrace` to be an array in the JSON string but got `%s`", jsonObj.get("stacktrace").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StepReportDeviceScreenshotsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StepReportDeviceScreenshotsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StepReportDeviceScreenshotsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StepReportDeviceScreenshotsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<StepReportDeviceScreenshotsInner>() {
           @Override
           public void write(JsonWriter out, StepReportDeviceScreenshotsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StepReportDeviceScreenshotsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StepReportDeviceScreenshotsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StepReportDeviceScreenshotsInner
   * @throws IOException if the JSON string is invalid with respect to StepReportDeviceScreenshotsInner
   */
  public static StepReportDeviceScreenshotsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StepReportDeviceScreenshotsInner.class);
  }

  /**
   * Convert an instance of StepReportDeviceScreenshotsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

