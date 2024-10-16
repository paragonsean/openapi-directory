/*
 * Runscope API
 * Manage Runscope programmatically.
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Environment;
import org.openapitools.client.model.Schedule;
import org.openapitools.client.model.TestCreatedBy;

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
 * TestDetail
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:55.705127-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TestDetail {
  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private Integer createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private TestCreatedBy createdBy;

  public static final String SERIALIZED_NAME_DEFAULT_ENVIRONMENT_ID = "default_environment_id";
  @SerializedName(SERIALIZED_NAME_DEFAULT_ENVIRONMENT_ID)
  private String defaultEnvironmentId;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LAST_RUN = "last_run";
  @SerializedName(SERIALIZED_NAME_LAST_RUN)
  private Object lastRun;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TRIGGER_URL = "trigger_url";
  @SerializedName(SERIALIZED_NAME_TRIGGER_URL)
  private String triggerUrl;

  public static final String SERIALIZED_NAME_ENVIRONMENTS = "environments";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENTS)
  private Environment environments;

  public static final String SERIALIZED_NAME_EXPORTED_AT = "exported_at";
  @SerializedName(SERIALIZED_NAME_EXPORTED_AT)
  private Integer exportedAt;

  public static final String SERIALIZED_NAME_SCHEDULES = "schedules";
  @SerializedName(SERIALIZED_NAME_SCHEDULES)
  private List<Schedule> schedules = new ArrayList<>();

  public static final String SERIALIZED_NAME_STEPS = "steps";
  @SerializedName(SERIALIZED_NAME_STEPS)
  private List<Object> steps = new ArrayList<>();

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private String version;

  public TestDetail() {
  }

  public TestDetail createdAt(Integer createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * The date the test was created in seconds (Unix time stamp format).
   * @return createdAt
   */
  @javax.annotation.Nullable
  public Integer getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(Integer createdAt) {
    this.createdAt = createdAt;
  }


  public TestDetail createdBy(TestCreatedBy createdBy) {
    this.createdBy = createdBy;
    return this;
  }

  /**
   * Get createdBy
   * @return createdBy
   */
  @javax.annotation.Nullable
  public TestCreatedBy getCreatedBy() {
    return createdBy;
  }

  public void setCreatedBy(TestCreatedBy createdBy) {
    this.createdBy = createdBy;
  }


  public TestDetail defaultEnvironmentId(String defaultEnvironmentId) {
    this.defaultEnvironmentId = defaultEnvironmentId;
    return this;
  }

  /**
   * Get defaultEnvironmentId
   * @return defaultEnvironmentId
   */
  @javax.annotation.Nullable
  public String getDefaultEnvironmentId() {
    return defaultEnvironmentId;
  }

  public void setDefaultEnvironmentId(String defaultEnvironmentId) {
    this.defaultEnvironmentId = defaultEnvironmentId;
  }


  public TestDetail description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The description for the test.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public TestDetail id(String id) {
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


  public TestDetail lastRun(Object lastRun) {
    this.lastRun = lastRun;
    return this;
  }

  /**
   * Get lastRun
   * @return lastRun
   */
  @javax.annotation.Nullable
  public Object getLastRun() {
    return lastRun;
  }

  public void setLastRun(Object lastRun) {
    this.lastRun = lastRun;
  }


  public TestDetail name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name for the test.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public TestDetail triggerUrl(String triggerUrl) {
    this.triggerUrl = triggerUrl;
    return this;
  }

  /**
   * Get triggerUrl
   * @return triggerUrl
   */
  @javax.annotation.Nullable
  public String getTriggerUrl() {
    return triggerUrl;
  }

  public void setTriggerUrl(String triggerUrl) {
    this.triggerUrl = triggerUrl;
  }


  public TestDetail environments(Environment environments) {
    this.environments = environments;
    return this;
  }

  /**
   * Get environments
   * @return environments
   */
  @javax.annotation.Nullable
  public Environment getEnvironments() {
    return environments;
  }

  public void setEnvironments(Environment environments) {
    this.environments = environments;
  }


  public TestDetail exportedAt(Integer exportedAt) {
    this.exportedAt = exportedAt;
    return this;
  }

  /**
   * Get exportedAt
   * @return exportedAt
   */
  @javax.annotation.Nullable
  public Integer getExportedAt() {
    return exportedAt;
  }

  public void setExportedAt(Integer exportedAt) {
    this.exportedAt = exportedAt;
  }


  public TestDetail schedules(List<Schedule> schedules) {
    this.schedules = schedules;
    return this;
  }

  public TestDetail addSchedulesItem(Schedule schedulesItem) {
    if (this.schedules == null) {
      this.schedules = new ArrayList<>();
    }
    this.schedules.add(schedulesItem);
    return this;
  }

  /**
   * Get schedules
   * @return schedules
   */
  @javax.annotation.Nullable
  public List<Schedule> getSchedules() {
    return schedules;
  }

  public void setSchedules(List<Schedule> schedules) {
    this.schedules = schedules;
  }


  public TestDetail steps(List<Object> steps) {
    this.steps = steps;
    return this;
  }

  public TestDetail addStepsItem(Object stepsItem) {
    if (this.steps == null) {
      this.steps = new ArrayList<>();
    }
    this.steps.add(stepsItem);
    return this;
  }

  /**
   * Get steps
   * @return steps
   */
  @javax.annotation.Nullable
  public List<Object> getSteps() {
    return steps;
  }

  public void setSteps(List<Object> steps) {
    this.steps = steps;
  }


  public TestDetail version(String version) {
    this.version = version;
    return this;
  }

  /**
   * Get version
   * @return version
   */
  @javax.annotation.Nullable
  public String getVersion() {
    return version;
  }

  public void setVersion(String version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TestDetail testDetail = (TestDetail) o;
    return Objects.equals(this.createdAt, testDetail.createdAt) &&
        Objects.equals(this.createdBy, testDetail.createdBy) &&
        Objects.equals(this.defaultEnvironmentId, testDetail.defaultEnvironmentId) &&
        Objects.equals(this.description, testDetail.description) &&
        Objects.equals(this.id, testDetail.id) &&
        Objects.equals(this.lastRun, testDetail.lastRun) &&
        Objects.equals(this.name, testDetail.name) &&
        Objects.equals(this.triggerUrl, testDetail.triggerUrl) &&
        Objects.equals(this.environments, testDetail.environments) &&
        Objects.equals(this.exportedAt, testDetail.exportedAt) &&
        Objects.equals(this.schedules, testDetail.schedules) &&
        Objects.equals(this.steps, testDetail.steps) &&
        Objects.equals(this.version, testDetail.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, createdBy, defaultEnvironmentId, description, id, lastRun, name, triggerUrl, environments, exportedAt, schedules, steps, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TestDetail {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    defaultEnvironmentId: ").append(toIndentedString(defaultEnvironmentId)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastRun: ").append(toIndentedString(lastRun)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    triggerUrl: ").append(toIndentedString(triggerUrl)).append("\n");
    sb.append("    environments: ").append(toIndentedString(environments)).append("\n");
    sb.append("    exportedAt: ").append(toIndentedString(exportedAt)).append("\n");
    sb.append("    schedules: ").append(toIndentedString(schedules)).append("\n");
    sb.append("    steps: ").append(toIndentedString(steps)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("created_at");
    openapiFields.add("created_by");
    openapiFields.add("default_environment_id");
    openapiFields.add("description");
    openapiFields.add("id");
    openapiFields.add("last_run");
    openapiFields.add("name");
    openapiFields.add("trigger_url");
    openapiFields.add("environments");
    openapiFields.add("exported_at");
    openapiFields.add("schedules");
    openapiFields.add("steps");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TestDetail
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TestDetail.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TestDetail is not found in the empty JSON string", TestDetail.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TestDetail.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TestDetail` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : TestDetail.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `created_by`
      if (jsonObj.get("created_by") != null && !jsonObj.get("created_by").isJsonNull()) {
        TestCreatedBy.validateJsonElement(jsonObj.get("created_by"));
      }
      if ((jsonObj.get("default_environment_id") != null && !jsonObj.get("default_environment_id").isJsonNull()) && !jsonObj.get("default_environment_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `default_environment_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("default_environment_id").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("trigger_url") != null && !jsonObj.get("trigger_url").isJsonNull()) && !jsonObj.get("trigger_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `trigger_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("trigger_url").toString()));
      }
      // validate the optional field `environments`
      if (jsonObj.get("environments") != null && !jsonObj.get("environments").isJsonNull()) {
        Environment.validateJsonElement(jsonObj.get("environments"));
      }
      if (jsonObj.get("schedules") != null && !jsonObj.get("schedules").isJsonNull()) {
        JsonArray jsonArrayschedules = jsonObj.getAsJsonArray("schedules");
        if (jsonArrayschedules != null) {
          // ensure the json data is an array
          if (!jsonObj.get("schedules").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `schedules` to be an array in the JSON string but got `%s`", jsonObj.get("schedules").toString()));
          }

          // validate the optional field `schedules` (array)
          for (int i = 0; i < jsonArrayschedules.size(); i++) {
            Schedule.validateJsonElement(jsonArrayschedules.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("steps") != null && !jsonObj.get("steps").isJsonNull() && !jsonObj.get("steps").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `steps` to be an array in the JSON string but got `%s`", jsonObj.get("steps").toString()));
      }
      if ((jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TestDetail.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TestDetail' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TestDetail> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TestDetail.class));

       return (TypeAdapter<T>) new TypeAdapter<TestDetail>() {
           @Override
           public void write(JsonWriter out, TestDetail value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TestDetail read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TestDetail given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TestDetail
   * @throws IOException if the JSON string is invalid with respect to TestDetail
   */
  public static TestDetail fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TestDetail.class);
  }

  /**
   * Convert an instance of TestDetail to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

