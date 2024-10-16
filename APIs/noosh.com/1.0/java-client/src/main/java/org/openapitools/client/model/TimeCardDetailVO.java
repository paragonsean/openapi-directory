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
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.TimeCardLineVO;
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
 * Java type: com.noosh.nooshapi.vo.TimeCardDetailVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TimeCardDetailVO {
  public static final String SERIALIZED_NAME_BILLABLE_HOURS = "billable_hours";
  @SerializedName(SERIALIZED_NAME_BILLABLE_HOURS)
  private Object billableHours = null;

  public static final String SERIALIZED_NAME_IS_SUBMIT = "is_submit";
  @SerializedName(SERIALIZED_NAME_IS_SUBMIT)
  private Boolean isSubmit;

  public static final String SERIALIZED_NAME_LAST_UPDATED_DATE = "last_updated_date";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED_DATE)
  private LocalDate lastUpdatedDate;

  public static final String SERIALIZED_NAME_NO_OF_WORKDAYS = "no_of_workdays";
  @SerializedName(SERIALIZED_NAME_NO_OF_WORKDAYS)
  private Integer noOfWorkdays;

  public static final String SERIALIZED_NAME_NONBILLABLE_HOURS = "nonbillable_hours";
  @SerializedName(SERIALIZED_NAME_NONBILLABLE_HOURS)
  private Object nonbillableHours = null;

  public static final String SERIALIZED_NAME_SUBMIT_DATE = "submit_date";
  @SerializedName(SERIALIZED_NAME_SUBMIT_DATE)
  private LocalDate submitDate;

  public static final String SERIALIZED_NAME_TIME_CARD_LINE = "time_card_line";
  @SerializedName(SERIALIZED_NAME_TIME_CARD_LINE)
  private List<TimeCardLineVO> timeCardLine = new ArrayList<>();

  public static final String SERIALIZED_NAME_TIMECARD_ID = "timecard_id";
  @SerializedName(SERIALIZED_NAME_TIMECARD_ID)
  private Long timecardId;

  public static final String SERIALIZED_NAME_TOTAL_HOURS = "total_hours";
  @SerializedName(SERIALIZED_NAME_TOTAL_HOURS)
  private Object totalHours = null;

  public static final String SERIALIZED_NAME_WEEK_BEGINNING = "week_beginning";
  @SerializedName(SERIALIZED_NAME_WEEK_BEGINNING)
  private LocalDate weekBeginning;

  public TimeCardDetailVO() {
  }

  public TimeCardDetailVO billableHours(Object billableHours) {
    this.billableHours = billableHours;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return billableHours
   */
  @javax.annotation.Nullable
  public Object getBillableHours() {
    return billableHours;
  }

  public void setBillableHours(Object billableHours) {
    this.billableHours = billableHours;
  }


  public TimeCardDetailVO isSubmit(Boolean isSubmit) {
    this.isSubmit = isSubmit;
    return this;
  }

  /**
   * 
   * @return isSubmit
   */
  @javax.annotation.Nullable
  public Boolean getIsSubmit() {
    return isSubmit;
  }

  public void setIsSubmit(Boolean isSubmit) {
    this.isSubmit = isSubmit;
  }


  public TimeCardDetailVO lastUpdatedDate(LocalDate lastUpdatedDate) {
    this.lastUpdatedDate = lastUpdatedDate;
    return this;
  }

  /**
   * 
   * @return lastUpdatedDate
   */
  @javax.annotation.Nullable
  public LocalDate getLastUpdatedDate() {
    return lastUpdatedDate;
  }

  public void setLastUpdatedDate(LocalDate lastUpdatedDate) {
    this.lastUpdatedDate = lastUpdatedDate;
  }


  public TimeCardDetailVO noOfWorkdays(Integer noOfWorkdays) {
    this.noOfWorkdays = noOfWorkdays;
    return this;
  }

  /**
   * 
   * @return noOfWorkdays
   */
  @javax.annotation.Nullable
  public Integer getNoOfWorkdays() {
    return noOfWorkdays;
  }

  public void setNoOfWorkdays(Integer noOfWorkdays) {
    this.noOfWorkdays = noOfWorkdays;
  }


  public TimeCardDetailVO nonbillableHours(Object nonbillableHours) {
    this.nonbillableHours = nonbillableHours;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return nonbillableHours
   */
  @javax.annotation.Nullable
  public Object getNonbillableHours() {
    return nonbillableHours;
  }

  public void setNonbillableHours(Object nonbillableHours) {
    this.nonbillableHours = nonbillableHours;
  }


  public TimeCardDetailVO submitDate(LocalDate submitDate) {
    this.submitDate = submitDate;
    return this;
  }

  /**
   * 
   * @return submitDate
   */
  @javax.annotation.Nullable
  public LocalDate getSubmitDate() {
    return submitDate;
  }

  public void setSubmitDate(LocalDate submitDate) {
    this.submitDate = submitDate;
  }


  public TimeCardDetailVO timeCardLine(List<TimeCardLineVO> timeCardLine) {
    this.timeCardLine = timeCardLine;
    return this;
  }

  public TimeCardDetailVO addTimeCardLineItem(TimeCardLineVO timeCardLineItem) {
    if (this.timeCardLine == null) {
      this.timeCardLine = new ArrayList<>();
    }
    this.timeCardLine.add(timeCardLineItem);
    return this;
  }

  /**
   * 
   * @return timeCardLine
   */
  @javax.annotation.Nullable
  public List<TimeCardLineVO> getTimeCardLine() {
    return timeCardLine;
  }

  public void setTimeCardLine(List<TimeCardLineVO> timeCardLine) {
    this.timeCardLine = timeCardLine;
  }


  public TimeCardDetailVO timecardId(Long timecardId) {
    this.timecardId = timecardId;
    return this;
  }

  /**
   * 
   * @return timecardId
   */
  @javax.annotation.Nullable
  public Long getTimecardId() {
    return timecardId;
  }

  public void setTimecardId(Long timecardId) {
    this.timecardId = timecardId;
  }


  public TimeCardDetailVO totalHours(Object totalHours) {
    this.totalHours = totalHours;
    return this;
  }

  /**
   * Java type: java.math.BigDecimal
   * @return totalHours
   */
  @javax.annotation.Nullable
  public Object getTotalHours() {
    return totalHours;
  }

  public void setTotalHours(Object totalHours) {
    this.totalHours = totalHours;
  }


  public TimeCardDetailVO weekBeginning(LocalDate weekBeginning) {
    this.weekBeginning = weekBeginning;
    return this;
  }

  /**
   * 
   * @return weekBeginning
   */
  @javax.annotation.Nullable
  public LocalDate getWeekBeginning() {
    return weekBeginning;
  }

  public void setWeekBeginning(LocalDate weekBeginning) {
    this.weekBeginning = weekBeginning;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TimeCardDetailVO timeCardDetailVO = (TimeCardDetailVO) o;
    return Objects.equals(this.billableHours, timeCardDetailVO.billableHours) &&
        Objects.equals(this.isSubmit, timeCardDetailVO.isSubmit) &&
        Objects.equals(this.lastUpdatedDate, timeCardDetailVO.lastUpdatedDate) &&
        Objects.equals(this.noOfWorkdays, timeCardDetailVO.noOfWorkdays) &&
        Objects.equals(this.nonbillableHours, timeCardDetailVO.nonbillableHours) &&
        Objects.equals(this.submitDate, timeCardDetailVO.submitDate) &&
        Objects.equals(this.timeCardLine, timeCardDetailVO.timeCardLine) &&
        Objects.equals(this.timecardId, timeCardDetailVO.timecardId) &&
        Objects.equals(this.totalHours, timeCardDetailVO.totalHours) &&
        Objects.equals(this.weekBeginning, timeCardDetailVO.weekBeginning);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(billableHours, isSubmit, lastUpdatedDate, noOfWorkdays, nonbillableHours, submitDate, timeCardLine, timecardId, totalHours, weekBeginning);
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
    sb.append("class TimeCardDetailVO {\n");
    sb.append("    billableHours: ").append(toIndentedString(billableHours)).append("\n");
    sb.append("    isSubmit: ").append(toIndentedString(isSubmit)).append("\n");
    sb.append("    lastUpdatedDate: ").append(toIndentedString(lastUpdatedDate)).append("\n");
    sb.append("    noOfWorkdays: ").append(toIndentedString(noOfWorkdays)).append("\n");
    sb.append("    nonbillableHours: ").append(toIndentedString(nonbillableHours)).append("\n");
    sb.append("    submitDate: ").append(toIndentedString(submitDate)).append("\n");
    sb.append("    timeCardLine: ").append(toIndentedString(timeCardLine)).append("\n");
    sb.append("    timecardId: ").append(toIndentedString(timecardId)).append("\n");
    sb.append("    totalHours: ").append(toIndentedString(totalHours)).append("\n");
    sb.append("    weekBeginning: ").append(toIndentedString(weekBeginning)).append("\n");
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
    openapiFields.add("billable_hours");
    openapiFields.add("is_submit");
    openapiFields.add("last_updated_date");
    openapiFields.add("no_of_workdays");
    openapiFields.add("nonbillable_hours");
    openapiFields.add("submit_date");
    openapiFields.add("time_card_line");
    openapiFields.add("timecard_id");
    openapiFields.add("total_hours");
    openapiFields.add("week_beginning");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TimeCardDetailVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TimeCardDetailVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TimeCardDetailVO is not found in the empty JSON string", TimeCardDetailVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TimeCardDetailVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TimeCardDetailVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("time_card_line") != null && !jsonObj.get("time_card_line").isJsonNull()) {
        JsonArray jsonArraytimeCardLine = jsonObj.getAsJsonArray("time_card_line");
        if (jsonArraytimeCardLine != null) {
          // ensure the json data is an array
          if (!jsonObj.get("time_card_line").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `time_card_line` to be an array in the JSON string but got `%s`", jsonObj.get("time_card_line").toString()));
          }

          // validate the optional field `time_card_line` (array)
          for (int i = 0; i < jsonArraytimeCardLine.size(); i++) {
            TimeCardLineVO.validateJsonElement(jsonArraytimeCardLine.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TimeCardDetailVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TimeCardDetailVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TimeCardDetailVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TimeCardDetailVO.class));

       return (TypeAdapter<T>) new TypeAdapter<TimeCardDetailVO>() {
           @Override
           public void write(JsonWriter out, TimeCardDetailVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TimeCardDetailVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TimeCardDetailVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TimeCardDetailVO
   * @throws IOException if the JSON string is invalid with respect to TimeCardDetailVO
   */
  public static TimeCardDetailVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TimeCardDetailVO.class);
  }

  /**
   * Convert an instance of TimeCardDetailVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

