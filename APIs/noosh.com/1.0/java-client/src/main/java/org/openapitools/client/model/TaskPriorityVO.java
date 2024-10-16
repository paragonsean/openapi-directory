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
 * Java type: com.noosh.nooshapi.vo.TaskPriorityVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TaskPriorityVO {
  public static final String SERIALIZED_NAME_TASK_PRIORITY_ID = "task_priority_id";
  @SerializedName(SERIALIZED_NAME_TASK_PRIORITY_ID)
  private Long taskPriorityId;

  public static final String SERIALIZED_NAME_TASK_PRIORITY_NAME = "task_priority_name";
  @SerializedName(SERIALIZED_NAME_TASK_PRIORITY_NAME)
  private String taskPriorityName;

  public TaskPriorityVO() {
  }

  public TaskPriorityVO taskPriorityId(Long taskPriorityId) {
    this.taskPriorityId = taskPriorityId;
    return this;
  }

  /**
   * 
   * @return taskPriorityId
   */
  @javax.annotation.Nullable
  public Long getTaskPriorityId() {
    return taskPriorityId;
  }

  public void setTaskPriorityId(Long taskPriorityId) {
    this.taskPriorityId = taskPriorityId;
  }


  public TaskPriorityVO taskPriorityName(String taskPriorityName) {
    this.taskPriorityName = taskPriorityName;
    return this;
  }

  /**
   * 
   * @return taskPriorityName
   */
  @javax.annotation.Nullable
  public String getTaskPriorityName() {
    return taskPriorityName;
  }

  public void setTaskPriorityName(String taskPriorityName) {
    this.taskPriorityName = taskPriorityName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TaskPriorityVO taskPriorityVO = (TaskPriorityVO) o;
    return Objects.equals(this.taskPriorityId, taskPriorityVO.taskPriorityId) &&
        Objects.equals(this.taskPriorityName, taskPriorityVO.taskPriorityName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(taskPriorityId, taskPriorityName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TaskPriorityVO {\n");
    sb.append("    taskPriorityId: ").append(toIndentedString(taskPriorityId)).append("\n");
    sb.append("    taskPriorityName: ").append(toIndentedString(taskPriorityName)).append("\n");
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
    openapiFields.add("task_priority_id");
    openapiFields.add("task_priority_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TaskPriorityVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TaskPriorityVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TaskPriorityVO is not found in the empty JSON string", TaskPriorityVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TaskPriorityVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TaskPriorityVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("task_priority_name") != null && !jsonObj.get("task_priority_name").isJsonNull()) && !jsonObj.get("task_priority_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `task_priority_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("task_priority_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TaskPriorityVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TaskPriorityVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TaskPriorityVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TaskPriorityVO.class));

       return (TypeAdapter<T>) new TypeAdapter<TaskPriorityVO>() {
           @Override
           public void write(JsonWriter out, TaskPriorityVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TaskPriorityVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TaskPriorityVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TaskPriorityVO
   * @throws IOException if the JSON string is invalid with respect to TaskPriorityVO
   */
  public static TaskPriorityVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TaskPriorityVO.class);
  }

  /**
   * Convert an instance of TaskPriorityVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

