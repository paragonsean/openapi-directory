/*
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
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
 * Represents a single diary appointment for a staff member.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:12.156803-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DiaryAppointmentModel {
  public static final String SERIALIZED_NAME_APPOINTMENT_TYPE = "AppointmentType";
  @SerializedName(SERIALIZED_NAME_APPOINTMENT_TYPE)
  private String appointmentType;

  public static final String SERIALIZED_NAME_CANCELLED = "Cancelled";
  @SerializedName(SERIALIZED_NAME_CANCELLED)
  private Boolean cancelled;

  public static final String SERIALIZED_NAME_COMMENT = "Comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public static final String SERIALIZED_NAME_CREATED_AT = "CreatedAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATED_BY = "CreatedBy";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private String createdBy;

  public static final String SERIALIZED_NAME_ETAG = "ETag";
  @SerializedName(SERIALIZED_NAME_ETAG)
  private String etag;

  public static final String SERIALIZED_NAME_END = "End";
  @SerializedName(SERIALIZED_NAME_END)
  private OffsetDateTime end;

  public static final String SERIALIZED_NAME_O_I_D = "OID";
  @SerializedName(SERIALIZED_NAME_O_I_D)
  private String OID;

  public static final String SERIALIZED_NAME_REMIND_AT = "RemindAt";
  @SerializedName(SERIALIZED_NAME_REMIND_AT)
  private OffsetDateTime remindAt;

  /**
   * The number of minutes before the appointment start date/time to remind the staff member. -1 means don&#39;t remind.
   */
  @JsonAdapter(RemindBeforeEnum.Adapter.class)
  public enum RemindBeforeEnum {
    MIN("Min"),
    
    MIN2("Min2"),
    
    MIN5("Min5"),
    
    MIN10("Min10"),
    
    MIN15("Min15"),
    
    MIN30("Min30"),
    
    MIN45("Min45"),
    
    HOUR("Hour"),
    
    HOUR2("Hour2"),
    
    HOUR3("Hour3"),
    
    HOUR6("Hour6"),
    
    HOUR12("Hour12"),
    
    DAY("Day"),
    
    DAY2("Day2"),
    
    DAY3("Day3"),
    
    WEEK("Week"),
    
    NO_REMINDER("NoReminder");

    private String value;

    RemindBeforeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RemindBeforeEnum fromValue(String value) {
      for (RemindBeforeEnum b : RemindBeforeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RemindBeforeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RemindBeforeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RemindBeforeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RemindBeforeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RemindBeforeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REMIND_BEFORE = "RemindBefore";
  @SerializedName(SERIALIZED_NAME_REMIND_BEFORE)
  private RemindBeforeEnum remindBefore;

  public static final String SERIALIZED_NAME_STAFF = "Staff";
  @SerializedName(SERIALIZED_NAME_STAFF)
  private String staff;

  public static final String SERIALIZED_NAME_START = "Start";
  @SerializedName(SERIALIZED_NAME_START)
  private OffsetDateTime start;

  public static final String SERIALIZED_NAME_SUBJECT = "Subject";
  @SerializedName(SERIALIZED_NAME_SUBJECT)
  private String subject;

  public DiaryAppointmentModel() {
  }

  public DiaryAppointmentModel appointmentType(String appointmentType) {
    this.appointmentType = appointmentType;
    return this;
  }

  /**
   * The diary appointment type.
   * @return appointmentType
   */
  @javax.annotation.Nullable
  public String getAppointmentType() {
    return appointmentType;
  }

  public void setAppointmentType(String appointmentType) {
    this.appointmentType = appointmentType;
  }


  public DiaryAppointmentModel cancelled(Boolean cancelled) {
    this.cancelled = cancelled;
    return this;
  }

  /**
   * Whether the appointment has been cancelled.
   * @return cancelled
   */
  @javax.annotation.Nullable
  public Boolean getCancelled() {
    return cancelled;
  }

  public void setCancelled(Boolean cancelled) {
    this.cancelled = cancelled;
  }


  public DiaryAppointmentModel comment(String comment) {
    this.comment = comment;
    return this;
  }

  /**
   * The appointment comments text.
   * @return comment
   */
  @javax.annotation.Nullable
  public String getComment() {
    return comment;
  }

  public void setComment(String comment) {
    this.comment = comment;
  }


  public DiaryAppointmentModel createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * The date/time this appointment was created.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public DiaryAppointmentModel createdBy(String createdBy) {
    this.createdBy = createdBy;
    return this;
  }

  /**
   * The staff member that created this appointment.
   * @return createdBy
   */
  @javax.annotation.Nullable
  public String getCreatedBy() {
    return createdBy;
  }

  public void setCreatedBy(String createdBy) {
    this.createdBy = createdBy;
  }


  public DiaryAppointmentModel etag(String etag) {
    this.etag = etag;
    return this;
  }

  /**
   * A unique identifier defining the object and change revision.
   * @return etag
   */
  @javax.annotation.Nullable
  public String getEtag() {
    return etag;
  }

  public void setEtag(String etag) {
    this.etag = etag;
  }


  public DiaryAppointmentModel end(OffsetDateTime end) {
    this.end = end;
    return this;
  }

  /**
   * The end date/time of this appointment.
   * @return end
   */
  @javax.annotation.Nullable
  public OffsetDateTime getEnd() {
    return end;
  }

  public void setEnd(OffsetDateTime end) {
    this.end = end;
  }


  public DiaryAppointmentModel OID(String OID) {
    this.OID = OID;
    return this;
  }

  /**
   * The unique Object ID (OID).
   * @return OID
   */
  @javax.annotation.Nullable
  public String getOID() {
    return OID;
  }

  public void setOID(String OID) {
    this.OID = OID;
  }


  public DiaryAppointmentModel remindAt(OffsetDateTime remindAt) {
    this.remindAt = remindAt;
    return this;
  }

  /**
   * The date/time to remind the staff member of this appointment.
   * @return remindAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getRemindAt() {
    return remindAt;
  }

  public void setRemindAt(OffsetDateTime remindAt) {
    this.remindAt = remindAt;
  }


  public DiaryAppointmentModel remindBefore(RemindBeforeEnum remindBefore) {
    this.remindBefore = remindBefore;
    return this;
  }

  /**
   * The number of minutes before the appointment start date/time to remind the staff member. -1 means don&#39;t remind.
   * @return remindBefore
   */
  @javax.annotation.Nullable
  public RemindBeforeEnum getRemindBefore() {
    return remindBefore;
  }

  public void setRemindBefore(RemindBeforeEnum remindBefore) {
    this.remindBefore = remindBefore;
  }


  public DiaryAppointmentModel staff(String staff) {
    this.staff = staff;
    return this;
  }

  /**
   * The staff member holding this appointment.
   * @return staff
   */
  @javax.annotation.Nullable
  public String getStaff() {
    return staff;
  }

  public void setStaff(String staff) {
    this.staff = staff;
  }


  public DiaryAppointmentModel start(OffsetDateTime start) {
    this.start = start;
    return this;
  }

  /**
   * The start date/time of this appointment.
   * @return start
   */
  @javax.annotation.Nullable
  public OffsetDateTime getStart() {
    return start;
  }

  public void setStart(OffsetDateTime start) {
    this.start = start;
  }


  public DiaryAppointmentModel subject(String subject) {
    this.subject = subject;
    return this;
  }

  /**
   * The appointment subject text.
   * @return subject
   */
  @javax.annotation.Nullable
  public String getSubject() {
    return subject;
  }

  public void setSubject(String subject) {
    this.subject = subject;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DiaryAppointmentModel diaryAppointmentModel = (DiaryAppointmentModel) o;
    return Objects.equals(this.appointmentType, diaryAppointmentModel.appointmentType) &&
        Objects.equals(this.cancelled, diaryAppointmentModel.cancelled) &&
        Objects.equals(this.comment, diaryAppointmentModel.comment) &&
        Objects.equals(this.createdAt, diaryAppointmentModel.createdAt) &&
        Objects.equals(this.createdBy, diaryAppointmentModel.createdBy) &&
        Objects.equals(this.etag, diaryAppointmentModel.etag) &&
        Objects.equals(this.end, diaryAppointmentModel.end) &&
        Objects.equals(this.OID, diaryAppointmentModel.OID) &&
        Objects.equals(this.remindAt, diaryAppointmentModel.remindAt) &&
        Objects.equals(this.remindBefore, diaryAppointmentModel.remindBefore) &&
        Objects.equals(this.staff, diaryAppointmentModel.staff) &&
        Objects.equals(this.start, diaryAppointmentModel.start) &&
        Objects.equals(this.subject, diaryAppointmentModel.subject);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appointmentType, cancelled, comment, createdAt, createdBy, etag, end, OID, remindAt, remindBefore, staff, start, subject);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DiaryAppointmentModel {\n");
    sb.append("    appointmentType: ").append(toIndentedString(appointmentType)).append("\n");
    sb.append("    cancelled: ").append(toIndentedString(cancelled)).append("\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    etag: ").append(toIndentedString(etag)).append("\n");
    sb.append("    end: ").append(toIndentedString(end)).append("\n");
    sb.append("    OID: ").append(toIndentedString(OID)).append("\n");
    sb.append("    remindAt: ").append(toIndentedString(remindAt)).append("\n");
    sb.append("    remindBefore: ").append(toIndentedString(remindBefore)).append("\n");
    sb.append("    staff: ").append(toIndentedString(staff)).append("\n");
    sb.append("    start: ").append(toIndentedString(start)).append("\n");
    sb.append("    subject: ").append(toIndentedString(subject)).append("\n");
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
    openapiFields.add("AppointmentType");
    openapiFields.add("Cancelled");
    openapiFields.add("Comment");
    openapiFields.add("CreatedAt");
    openapiFields.add("CreatedBy");
    openapiFields.add("ETag");
    openapiFields.add("End");
    openapiFields.add("OID");
    openapiFields.add("RemindAt");
    openapiFields.add("RemindBefore");
    openapiFields.add("Staff");
    openapiFields.add("Start");
    openapiFields.add("Subject");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DiaryAppointmentModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DiaryAppointmentModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DiaryAppointmentModel is not found in the empty JSON string", DiaryAppointmentModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DiaryAppointmentModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DiaryAppointmentModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AppointmentType") != null && !jsonObj.get("AppointmentType").isJsonNull()) && !jsonObj.get("AppointmentType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AppointmentType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AppointmentType").toString()));
      }
      if ((jsonObj.get("Comment") != null && !jsonObj.get("Comment").isJsonNull()) && !jsonObj.get("Comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Comment").toString()));
      }
      if ((jsonObj.get("CreatedBy") != null && !jsonObj.get("CreatedBy").isJsonNull()) && !jsonObj.get("CreatedBy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CreatedBy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CreatedBy").toString()));
      }
      if ((jsonObj.get("ETag") != null && !jsonObj.get("ETag").isJsonNull()) && !jsonObj.get("ETag").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ETag` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ETag").toString()));
      }
      if ((jsonObj.get("OID") != null && !jsonObj.get("OID").isJsonNull()) && !jsonObj.get("OID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OID").toString()));
      }
      if ((jsonObj.get("RemindBefore") != null && !jsonObj.get("RemindBefore").isJsonNull()) && !jsonObj.get("RemindBefore").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `RemindBefore` to be a primitive type in the JSON string but got `%s`", jsonObj.get("RemindBefore").toString()));
      }
      // validate the optional field `RemindBefore`
      if (jsonObj.get("RemindBefore") != null && !jsonObj.get("RemindBefore").isJsonNull()) {
        RemindBeforeEnum.validateJsonElement(jsonObj.get("RemindBefore"));
      }
      if ((jsonObj.get("Staff") != null && !jsonObj.get("Staff").isJsonNull()) && !jsonObj.get("Staff").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Staff` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Staff").toString()));
      }
      if ((jsonObj.get("Subject") != null && !jsonObj.get("Subject").isJsonNull()) && !jsonObj.get("Subject").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Subject` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Subject").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DiaryAppointmentModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DiaryAppointmentModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DiaryAppointmentModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DiaryAppointmentModel.class));

       return (TypeAdapter<T>) new TypeAdapter<DiaryAppointmentModel>() {
           @Override
           public void write(JsonWriter out, DiaryAppointmentModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DiaryAppointmentModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DiaryAppointmentModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DiaryAppointmentModel
   * @throws IOException if the JSON string is invalid with respect to DiaryAppointmentModel
   */
  public static DiaryAppointmentModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DiaryAppointmentModel.class);
  }

  /**
   * Convert an instance of DiaryAppointmentModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

