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
import org.openapitools.client.model.ProjectTimeCardVO;
import org.openapitools.client.model.TaskTimeCardVO;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * Java type: com.noosh.nooshapi.vo.TimeCardLineVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TimeCardLineVO {
  public static final String SERIALIZED_NAME_ACTIVITY_NAME = "activity_name";
  @SerializedName(SERIALIZED_NAME_ACTIVITY_NAME)
  private String activityName;

  public static final String SERIALIZED_NAME_DAY1_HOURS_SPENT = "day1_hours_spent";
  @SerializedName(SERIALIZED_NAME_DAY1_HOURS_SPENT)
  private Object day1HoursSpent = null;

  public static final String SERIALIZED_NAME_DAY2_HOURS_SPENT = "day2_hours_spent";
  @SerializedName(SERIALIZED_NAME_DAY2_HOURS_SPENT)
  private Object day2HoursSpent = null;

  public static final String SERIALIZED_NAME_DAY3_HOURS_SPENT = "day3_hours_spent";
  @SerializedName(SERIALIZED_NAME_DAY3_HOURS_SPENT)
  private Object day3HoursSpent = null;

  public static final String SERIALIZED_NAME_DAY4_HOURS_SPENT = "day4_hours_spent";
  @SerializedName(SERIALIZED_NAME_DAY4_HOURS_SPENT)
  private Object day4HoursSpent = null;

  public static final String SERIALIZED_NAME_DAY5_HOURS_SPENT = "day5_hours_spent";
  @SerializedName(SERIALIZED_NAME_DAY5_HOURS_SPENT)
  private Object day5HoursSpent = null;

  public static final String SERIALIZED_NAME_DAY6_HOURS_SPENT = "day6_hours_spent";
  @SerializedName(SERIALIZED_NAME_DAY6_HOURS_SPENT)
  private Object day6HoursSpent = null;

  public static final String SERIALIZED_NAME_DAY7_HOURS_SPENT = "day7_hours_spent";
  @SerializedName(SERIALIZED_NAME_DAY7_HOURS_SPENT)
  private Object day7HoursSpent = null;

  public static final String SERIALIZED_NAME_PROJECT = "project";
  @SerializedName(SERIALIZED_NAME_PROJECT)
  private ProjectTimeCardVO project;

  public static final String SERIALIZED_NAME_TASK = "task";
  @SerializedName(SERIALIZED_NAME_TASK)
  private TaskTimeCardVO task;

  public static final String SERIALIZED_NAME_TIME_CARD_LINE_ID = "time_card_line_id";
  @SerializedName(SERIALIZED_NAME_TIME_CARD_LINE_ID)
  private Long timeCardLineId;

  public static final String SERIALIZED_NAME_TOTAL_HOURS_SPENT = "total_hours_spent";
  @SerializedName(SERIALIZED_NAME_TOTAL_HOURS_SPENT)
  private Object totalHoursSpent = null;

  public TimeCardLineVO() {
  }

  public TimeCardLineVO activityName(String activityName) {
    this.activityName = activityName;
    return this;
  }

  /**
   * 
   * @return activityName
   */
  @javax.annotation.Nullable
  public String getActivityName() {
    return activityName;
  }

  public void setActivityName(String activityName) {
    this.activityName = activityName;
  }


  public TimeCardLineVO day1HoursSpent(Object day1HoursSpent) {
    this.day1HoursSpent = day1HoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return day1HoursSpent
   */
  @javax.annotation.Nullable
  public Object getDay1HoursSpent() {
    return day1HoursSpent;
  }

  public void setDay1HoursSpent(Object day1HoursSpent) {
    this.day1HoursSpent = day1HoursSpent;
  }


  public TimeCardLineVO day2HoursSpent(Object day2HoursSpent) {
    this.day2HoursSpent = day2HoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return day2HoursSpent
   */
  @javax.annotation.Nullable
  public Object getDay2HoursSpent() {
    return day2HoursSpent;
  }

  public void setDay2HoursSpent(Object day2HoursSpent) {
    this.day2HoursSpent = day2HoursSpent;
  }


  public TimeCardLineVO day3HoursSpent(Object day3HoursSpent) {
    this.day3HoursSpent = day3HoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return day3HoursSpent
   */
  @javax.annotation.Nullable
  public Object getDay3HoursSpent() {
    return day3HoursSpent;
  }

  public void setDay3HoursSpent(Object day3HoursSpent) {
    this.day3HoursSpent = day3HoursSpent;
  }


  public TimeCardLineVO day4HoursSpent(Object day4HoursSpent) {
    this.day4HoursSpent = day4HoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return day4HoursSpent
   */
  @javax.annotation.Nullable
  public Object getDay4HoursSpent() {
    return day4HoursSpent;
  }

  public void setDay4HoursSpent(Object day4HoursSpent) {
    this.day4HoursSpent = day4HoursSpent;
  }


  public TimeCardLineVO day5HoursSpent(Object day5HoursSpent) {
    this.day5HoursSpent = day5HoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return day5HoursSpent
   */
  @javax.annotation.Nullable
  public Object getDay5HoursSpent() {
    return day5HoursSpent;
  }

  public void setDay5HoursSpent(Object day5HoursSpent) {
    this.day5HoursSpent = day5HoursSpent;
  }


  public TimeCardLineVO day6HoursSpent(Object day6HoursSpent) {
    this.day6HoursSpent = day6HoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return day6HoursSpent
   */
  @javax.annotation.Nullable
  public Object getDay6HoursSpent() {
    return day6HoursSpent;
  }

  public void setDay6HoursSpent(Object day6HoursSpent) {
    this.day6HoursSpent = day6HoursSpent;
  }


  public TimeCardLineVO day7HoursSpent(Object day7HoursSpent) {
    this.day7HoursSpent = day7HoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return day7HoursSpent
   */
  @javax.annotation.Nullable
  public Object getDay7HoursSpent() {
    return day7HoursSpent;
  }

  public void setDay7HoursSpent(Object day7HoursSpent) {
    this.day7HoursSpent = day7HoursSpent;
  }


  public TimeCardLineVO project(ProjectTimeCardVO project) {
    this.project = project;
    return this;
  }

  /**
   * Get project
   * @return project
   */
  @javax.annotation.Nullable
  public ProjectTimeCardVO getProject() {
    return project;
  }

  public void setProject(ProjectTimeCardVO project) {
    this.project = project;
  }


  public TimeCardLineVO task(TaskTimeCardVO task) {
    this.task = task;
    return this;
  }

  /**
   * Get task
   * @return task
   */
  @javax.annotation.Nullable
  public TaskTimeCardVO getTask() {
    return task;
  }

  public void setTask(TaskTimeCardVO task) {
    this.task = task;
  }


  public TimeCardLineVO timeCardLineId(Long timeCardLineId) {
    this.timeCardLineId = timeCardLineId;
    return this;
  }

  /**
   * 
   * @return timeCardLineId
   */
  @javax.annotation.Nullable
  public Long getTimeCardLineId() {
    return timeCardLineId;
  }

  public void setTimeCardLineId(Long timeCardLineId) {
    this.timeCardLineId = timeCardLineId;
  }


  public TimeCardLineVO totalHoursSpent(Object totalHoursSpent) {
    this.totalHoursSpent = totalHoursSpent;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return totalHoursSpent
   */
  @javax.annotation.Nullable
  public Object getTotalHoursSpent() {
    return totalHoursSpent;
  }

  public void setTotalHoursSpent(Object totalHoursSpent) {
    this.totalHoursSpent = totalHoursSpent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TimeCardLineVO timeCardLineVO = (TimeCardLineVO) o;
    return Objects.equals(this.activityName, timeCardLineVO.activityName) &&
        Objects.equals(this.day1HoursSpent, timeCardLineVO.day1HoursSpent) &&
        Objects.equals(this.day2HoursSpent, timeCardLineVO.day2HoursSpent) &&
        Objects.equals(this.day3HoursSpent, timeCardLineVO.day3HoursSpent) &&
        Objects.equals(this.day4HoursSpent, timeCardLineVO.day4HoursSpent) &&
        Objects.equals(this.day5HoursSpent, timeCardLineVO.day5HoursSpent) &&
        Objects.equals(this.day6HoursSpent, timeCardLineVO.day6HoursSpent) &&
        Objects.equals(this.day7HoursSpent, timeCardLineVO.day7HoursSpent) &&
        Objects.equals(this.project, timeCardLineVO.project) &&
        Objects.equals(this.task, timeCardLineVO.task) &&
        Objects.equals(this.timeCardLineId, timeCardLineVO.timeCardLineId) &&
        Objects.equals(this.totalHoursSpent, timeCardLineVO.totalHoursSpent);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(activityName, day1HoursSpent, day2HoursSpent, day3HoursSpent, day4HoursSpent, day5HoursSpent, day6HoursSpent, day7HoursSpent, project, task, timeCardLineId, totalHoursSpent);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TimeCardLineVO {\n");
    sb.append("    activityName: ").append(toIndentedString(activityName)).append("\n");
    sb.append("    day1HoursSpent: ").append(toIndentedString(day1HoursSpent)).append("\n");
    sb.append("    day2HoursSpent: ").append(toIndentedString(day2HoursSpent)).append("\n");
    sb.append("    day3HoursSpent: ").append(toIndentedString(day3HoursSpent)).append("\n");
    sb.append("    day4HoursSpent: ").append(toIndentedString(day4HoursSpent)).append("\n");
    sb.append("    day5HoursSpent: ").append(toIndentedString(day5HoursSpent)).append("\n");
    sb.append("    day6HoursSpent: ").append(toIndentedString(day6HoursSpent)).append("\n");
    sb.append("    day7HoursSpent: ").append(toIndentedString(day7HoursSpent)).append("\n");
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
    sb.append("    task: ").append(toIndentedString(task)).append("\n");
    sb.append("    timeCardLineId: ").append(toIndentedString(timeCardLineId)).append("\n");
    sb.append("    totalHoursSpent: ").append(toIndentedString(totalHoursSpent)).append("\n");
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
    openapiFields.add("activity_name");
    openapiFields.add("day1_hours_spent");
    openapiFields.add("day2_hours_spent");
    openapiFields.add("day3_hours_spent");
    openapiFields.add("day4_hours_spent");
    openapiFields.add("day5_hours_spent");
    openapiFields.add("day6_hours_spent");
    openapiFields.add("day7_hours_spent");
    openapiFields.add("project");
    openapiFields.add("task");
    openapiFields.add("time_card_line_id");
    openapiFields.add("total_hours_spent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TimeCardLineVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TimeCardLineVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TimeCardLineVO is not found in the empty JSON string", TimeCardLineVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TimeCardLineVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TimeCardLineVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("activity_name") != null && !jsonObj.get("activity_name").isJsonNull()) && !jsonObj.get("activity_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `activity_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("activity_name").toString()));
      }
      // validate the optional field `project`
      if (jsonObj.get("project") != null && !jsonObj.get("project").isJsonNull()) {
        ProjectTimeCardVO.validateJsonElement(jsonObj.get("project"));
      }
      // validate the optional field `task`
      if (jsonObj.get("task") != null && !jsonObj.get("task").isJsonNull()) {
        TaskTimeCardVO.validateJsonElement(jsonObj.get("task"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TimeCardLineVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TimeCardLineVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TimeCardLineVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TimeCardLineVO.class));

       return (TypeAdapter<T>) new TypeAdapter<TimeCardLineVO>() {
           @Override
           public void write(JsonWriter out, TimeCardLineVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TimeCardLineVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TimeCardLineVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TimeCardLineVO
   * @throws IOException if the JSON string is invalid with respect to TimeCardLineVO
   */
  public static TimeCardLineVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TimeCardLineVO.class);
  }

  /**
   * Convert an instance of TimeCardLineVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

