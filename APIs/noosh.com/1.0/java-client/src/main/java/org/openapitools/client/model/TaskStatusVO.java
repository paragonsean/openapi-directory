/*
 * Noosh API application
 * Full description of Noosh API
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
 * Java type: com.noosh.nooshapi.vo.TaskStatusVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TaskStatusVO {
  public static final String SERIALIZED_NAME_TASK_STATUS_ID = "task_status_id";
  @SerializedName(SERIALIZED_NAME_TASK_STATUS_ID)
  private Long taskStatusId;

  public static final String SERIALIZED_NAME_TASK_STATUS_NAME = "task_status_name";
  @SerializedName(SERIALIZED_NAME_TASK_STATUS_NAME)
  private String taskStatusName;

  public TaskStatusVO() {
  }

  public TaskStatusVO taskStatusId(Long taskStatusId) {
    this.taskStatusId = taskStatusId;
    return this;
  }

  /**
   * 
   * @return taskStatusId
   */
  @javax.annotation.Nullable
  public Long getTaskStatusId() {
    return taskStatusId;
  }

  public void setTaskStatusId(Long taskStatusId) {
    this.taskStatusId = taskStatusId;
  }


  public TaskStatusVO taskStatusName(String taskStatusName) {
    this.taskStatusName = taskStatusName;
    return this;
  }

  /**
   * 
   * @return taskStatusName
   */
  @javax.annotation.Nullable
  public String getTaskStatusName() {
    return taskStatusName;
  }

  public void setTaskStatusName(String taskStatusName) {
    this.taskStatusName = taskStatusName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TaskStatusVO taskStatusVO = (TaskStatusVO) o;
    return Objects.equals(this.taskStatusId, taskStatusVO.taskStatusId) &&
        Objects.equals(this.taskStatusName, taskStatusVO.taskStatusName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(taskStatusId, taskStatusName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TaskStatusVO {\n");
    sb.append("    taskStatusId: ").append(toIndentedString(taskStatusId)).append("\n");
    sb.append("    taskStatusName: ").append(toIndentedString(taskStatusName)).append("\n");
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
    openapiFields.add("task_status_id");
    openapiFields.add("task_status_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TaskStatusVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TaskStatusVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TaskStatusVO is not found in the empty JSON string", TaskStatusVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TaskStatusVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TaskStatusVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("task_status_name") != null && !jsonObj.get("task_status_name").isJsonNull()) && !jsonObj.get("task_status_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `task_status_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("task_status_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TaskStatusVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TaskStatusVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TaskStatusVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TaskStatusVO.class));

       return (TypeAdapter<T>) new TypeAdapter<TaskStatusVO>() {
           @Override
           public void write(JsonWriter out, TaskStatusVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TaskStatusVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TaskStatusVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TaskStatusVO
   * @throws IOException if the JSON string is invalid with respect to TaskStatusVO
   */
  public static TaskStatusVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TaskStatusVO.class);
  }

  /**
   * Convert an instance of TaskStatusVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

