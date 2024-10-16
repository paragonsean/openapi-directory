/*
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
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
 * DetailedErrorResponseErrorDetailedMessageInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:33.166267-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DetailedErrorResponseErrorDetailedMessageInner {
  public static final String SERIALIZED_NAME_BREAK = "break";
  @SerializedName(SERIALIZED_NAME_BREAK)
  private Integer _break;

  public static final String SERIALIZED_NAME_COMMENT = "comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_EMPLOYEE = "employee";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE)
  private Integer employee;

  public static final String SERIALIZED_NAME_END_TIME = "end_time";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private String endTime;

  public static final String SERIALIZED_NAME_ERROR_MSG = "error_msg";
  @SerializedName(SERIALIZED_NAME_ERROR_MSG)
  private String errorMsg;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_START_TIME = "start_time";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private String startTime;

  public static final String SERIALIZED_NAME_SUCCESS = "success";
  @SerializedName(SERIALIZED_NAME_SUCCESS)
  private Boolean success;

  public DetailedErrorResponseErrorDetailedMessageInner() {
  }

  public DetailedErrorResponseErrorDetailedMessageInner _break(Integer _break) {
    this._break = _break;
    return this;
  }

  /**
   * Get _break
   * @return _break
   */
  @javax.annotation.Nullable
  public Integer getBreak() {
    return _break;
  }

  public void setBreak(Integer _break) {
    this._break = _break;
  }


  public DetailedErrorResponseErrorDetailedMessageInner comment(String comment) {
    this.comment = comment;
    return this;
  }

  /**
   * Get comment
   * @return comment
   */
  @javax.annotation.Nullable
  public String getComment() {
    return comment;
  }

  public void setComment(String comment) {
    this.comment = comment;
  }


  public DetailedErrorResponseErrorDetailedMessageInner date(String date) {
    this.date = date;
    return this;
  }

  /**
   * Get date
   * @return date
   */
  @javax.annotation.Nullable
  public String getDate() {
    return date;
  }

  public void setDate(String date) {
    this.date = date;
  }


  public DetailedErrorResponseErrorDetailedMessageInner employee(Integer employee) {
    this.employee = employee;
    return this;
  }

  /**
   * Get employee
   * @return employee
   */
  @javax.annotation.Nullable
  public Integer getEmployee() {
    return employee;
  }

  public void setEmployee(Integer employee) {
    this.employee = employee;
  }


  public DetailedErrorResponseErrorDetailedMessageInner endTime(String endTime) {
    this.endTime = endTime;
    return this;
  }

  /**
   * Get endTime
   * @return endTime
   */
  @javax.annotation.Nullable
  public String getEndTime() {
    return endTime;
  }

  public void setEndTime(String endTime) {
    this.endTime = endTime;
  }


  public DetailedErrorResponseErrorDetailedMessageInner errorMsg(String errorMsg) {
    this.errorMsg = errorMsg;
    return this;
  }

  /**
   * Get errorMsg
   * @return errorMsg
   */
  @javax.annotation.Nullable
  public String getErrorMsg() {
    return errorMsg;
  }

  public void setErrorMsg(String errorMsg) {
    this.errorMsg = errorMsg;
  }


  public DetailedErrorResponseErrorDetailedMessageInner id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public DetailedErrorResponseErrorDetailedMessageInner startTime(String startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Get startTime
   * @return startTime
   */
  @javax.annotation.Nullable
  public String getStartTime() {
    return startTime;
  }

  public void setStartTime(String startTime) {
    this.startTime = startTime;
  }


  public DetailedErrorResponseErrorDetailedMessageInner success(Boolean success) {
    this.success = success;
    return this;
  }

  /**
   * Get success
   * @return success
   */
  @javax.annotation.Nullable
  public Boolean getSuccess() {
    return success;
  }

  public void setSuccess(Boolean success) {
    this.success = success;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DetailedErrorResponseErrorDetailedMessageInner detailedErrorResponseErrorDetailedMessageInner = (DetailedErrorResponseErrorDetailedMessageInner) o;
    return Objects.equals(this._break, detailedErrorResponseErrorDetailedMessageInner._break) &&
        Objects.equals(this.comment, detailedErrorResponseErrorDetailedMessageInner.comment) &&
        Objects.equals(this.date, detailedErrorResponseErrorDetailedMessageInner.date) &&
        Objects.equals(this.employee, detailedErrorResponseErrorDetailedMessageInner.employee) &&
        Objects.equals(this.endTime, detailedErrorResponseErrorDetailedMessageInner.endTime) &&
        Objects.equals(this.errorMsg, detailedErrorResponseErrorDetailedMessageInner.errorMsg) &&
        Objects.equals(this.id, detailedErrorResponseErrorDetailedMessageInner.id) &&
        Objects.equals(this.startTime, detailedErrorResponseErrorDetailedMessageInner.startTime) &&
        Objects.equals(this.success, detailedErrorResponseErrorDetailedMessageInner.success);
  }

  @Override
  public int hashCode() {
    return Objects.hash(_break, comment, date, employee, endTime, errorMsg, id, startTime, success);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DetailedErrorResponseErrorDetailedMessageInner {\n");
    sb.append("    _break: ").append(toIndentedString(_break)).append("\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    employee: ").append(toIndentedString(employee)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    errorMsg: ").append(toIndentedString(errorMsg)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    success: ").append(toIndentedString(success)).append("\n");
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
    openapiFields.add("break");
    openapiFields.add("comment");
    openapiFields.add("date");
    openapiFields.add("employee");
    openapiFields.add("end_time");
    openapiFields.add("error_msg");
    openapiFields.add("id");
    openapiFields.add("start_time");
    openapiFields.add("success");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DetailedErrorResponseErrorDetailedMessageInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DetailedErrorResponseErrorDetailedMessageInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DetailedErrorResponseErrorDetailedMessageInner is not found in the empty JSON string", DetailedErrorResponseErrorDetailedMessageInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DetailedErrorResponseErrorDetailedMessageInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DetailedErrorResponseErrorDetailedMessageInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comment") != null && !jsonObj.get("comment").isJsonNull()) && !jsonObj.get("comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment").toString()));
      }
      if ((jsonObj.get("date") != null && !jsonObj.get("date").isJsonNull()) && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      if ((jsonObj.get("end_time") != null && !jsonObj.get("end_time").isJsonNull()) && !jsonObj.get("end_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("end_time").toString()));
      }
      if ((jsonObj.get("error_msg") != null && !jsonObj.get("error_msg").isJsonNull()) && !jsonObj.get("error_msg").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `error_msg` to be a primitive type in the JSON string but got `%s`", jsonObj.get("error_msg").toString()));
      }
      if ((jsonObj.get("start_time") != null && !jsonObj.get("start_time").isJsonNull()) && !jsonObj.get("start_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `start_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("start_time").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DetailedErrorResponseErrorDetailedMessageInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DetailedErrorResponseErrorDetailedMessageInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DetailedErrorResponseErrorDetailedMessageInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DetailedErrorResponseErrorDetailedMessageInner.class));

       return (TypeAdapter<T>) new TypeAdapter<DetailedErrorResponseErrorDetailedMessageInner>() {
           @Override
           public void write(JsonWriter out, DetailedErrorResponseErrorDetailedMessageInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DetailedErrorResponseErrorDetailedMessageInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DetailedErrorResponseErrorDetailedMessageInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DetailedErrorResponseErrorDetailedMessageInner
   * @throws IOException if the JSON string is invalid with respect to DetailedErrorResponseErrorDetailedMessageInner
   */
  public static DetailedErrorResponseErrorDetailedMessageInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DetailedErrorResponseErrorDetailedMessageInner.class);
  }

  /**
   * Convert an instance of DetailedErrorResponseErrorDetailedMessageInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

