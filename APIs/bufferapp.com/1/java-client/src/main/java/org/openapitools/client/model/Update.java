/*
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.client.model.UpdateStatistics;

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
 * Update
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:44.110075-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Update {
  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private BigDecimal createdAt;

  public static final String SERIALIZED_NAME_DAY = "day";
  @SerializedName(SERIALIZED_NAME_DAY)
  private String day;

  public static final String SERIALIZED_NAME_DUE_AT = "due_at";
  @SerializedName(SERIALIZED_NAME_DUE_AT)
  private BigDecimal dueAt;

  public static final String SERIALIZED_NAME_DUE_TIME = "due_time";
  @SerializedName(SERIALIZED_NAME_DUE_TIME)
  private String dueTime;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_PROFILE_ID = "profile_id";
  @SerializedName(SERIALIZED_NAME_PROFILE_ID)
  private String profileId;

  public static final String SERIALIZED_NAME_PROFILE_SERVICE = "profile_service";
  @SerializedName(SERIALIZED_NAME_PROFILE_SERVICE)
  private String profileService;

  public static final String SERIALIZED_NAME_SENT_AT = "sent_at";
  @SerializedName(SERIALIZED_NAME_SENT_AT)
  private BigDecimal sentAt;

  public static final String SERIALIZED_NAME_SERVICE_UPDATE_ID = "service_update_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_UPDATE_ID)
  private String serviceUpdateId;

  public static final String SERIALIZED_NAME_STATISTICS = "statistics";
  @SerializedName(SERIALIZED_NAME_STATISTICS)
  private UpdateStatistics statistics;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public static final String SERIALIZED_NAME_TEXT_FORMATTED = "text_formatted";
  @SerializedName(SERIALIZED_NAME_TEXT_FORMATTED)
  private String textFormatted;

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public static final String SERIALIZED_NAME_VIA = "via";
  @SerializedName(SERIALIZED_NAME_VIA)
  private String via;

  public Update() {
  }

  public Update createdAt(BigDecimal createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public BigDecimal getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(BigDecimal createdAt) {
    this.createdAt = createdAt;
  }


  public Update day(String day) {
    this.day = day;
    return this;
  }

  /**
   * Get day
   * @return day
   */
  @javax.annotation.Nullable
  public String getDay() {
    return day;
  }

  public void setDay(String day) {
    this.day = day;
  }


  public Update dueAt(BigDecimal dueAt) {
    this.dueAt = dueAt;
    return this;
  }

  /**
   * Get dueAt
   * @return dueAt
   */
  @javax.annotation.Nullable
  public BigDecimal getDueAt() {
    return dueAt;
  }

  public void setDueAt(BigDecimal dueAt) {
    this.dueAt = dueAt;
  }


  public Update dueTime(String dueTime) {
    this.dueTime = dueTime;
    return this;
  }

  /**
   * Get dueTime
   * @return dueTime
   */
  @javax.annotation.Nullable
  public String getDueTime() {
    return dueTime;
  }

  public void setDueTime(String dueTime) {
    this.dueTime = dueTime;
  }


  public Update id(String id) {
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


  public Update profileId(String profileId) {
    this.profileId = profileId;
    return this;
  }

  /**
   * Get profileId
   * @return profileId
   */
  @javax.annotation.Nullable
  public String getProfileId() {
    return profileId;
  }

  public void setProfileId(String profileId) {
    this.profileId = profileId;
  }


  public Update profileService(String profileService) {
    this.profileService = profileService;
    return this;
  }

  /**
   * Get profileService
   * @return profileService
   */
  @javax.annotation.Nullable
  public String getProfileService() {
    return profileService;
  }

  public void setProfileService(String profileService) {
    this.profileService = profileService;
  }


  public Update sentAt(BigDecimal sentAt) {
    this.sentAt = sentAt;
    return this;
  }

  /**
   * Get sentAt
   * @return sentAt
   */
  @javax.annotation.Nullable
  public BigDecimal getSentAt() {
    return sentAt;
  }

  public void setSentAt(BigDecimal sentAt) {
    this.sentAt = sentAt;
  }


  public Update serviceUpdateId(String serviceUpdateId) {
    this.serviceUpdateId = serviceUpdateId;
    return this;
  }

  /**
   * Get serviceUpdateId
   * @return serviceUpdateId
   */
  @javax.annotation.Nullable
  public String getServiceUpdateId() {
    return serviceUpdateId;
  }

  public void setServiceUpdateId(String serviceUpdateId) {
    this.serviceUpdateId = serviceUpdateId;
  }


  public Update statistics(UpdateStatistics statistics) {
    this.statistics = statistics;
    return this;
  }

  /**
   * Get statistics
   * @return statistics
   */
  @javax.annotation.Nullable
  public UpdateStatistics getStatistics() {
    return statistics;
  }

  public void setStatistics(UpdateStatistics statistics) {
    this.statistics = statistics;
  }


  public Update status(String status) {
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


  public Update text(String text) {
    this.text = text;
    return this;
  }

  /**
   * Get text
   * @return text
   */
  @javax.annotation.Nullable
  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }


  public Update textFormatted(String textFormatted) {
    this.textFormatted = textFormatted;
    return this;
  }

  /**
   * Get textFormatted
   * @return textFormatted
   */
  @javax.annotation.Nullable
  public String getTextFormatted() {
    return textFormatted;
  }

  public void setTextFormatted(String textFormatted) {
    this.textFormatted = textFormatted;
  }


  public Update userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * Get userId
   * @return userId
   */
  @javax.annotation.Nullable
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }


  public Update via(String via) {
    this.via = via;
    return this;
  }

  /**
   * Get via
   * @return via
   */
  @javax.annotation.Nullable
  public String getVia() {
    return via;
  }

  public void setVia(String via) {
    this.via = via;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Update update = (Update) o;
    return Objects.equals(this.createdAt, update.createdAt) &&
        Objects.equals(this.day, update.day) &&
        Objects.equals(this.dueAt, update.dueAt) &&
        Objects.equals(this.dueTime, update.dueTime) &&
        Objects.equals(this.id, update.id) &&
        Objects.equals(this.profileId, update.profileId) &&
        Objects.equals(this.profileService, update.profileService) &&
        Objects.equals(this.sentAt, update.sentAt) &&
        Objects.equals(this.serviceUpdateId, update.serviceUpdateId) &&
        Objects.equals(this.statistics, update.statistics) &&
        Objects.equals(this.status, update.status) &&
        Objects.equals(this.text, update.text) &&
        Objects.equals(this.textFormatted, update.textFormatted) &&
        Objects.equals(this.userId, update.userId) &&
        Objects.equals(this.via, update.via);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, day, dueAt, dueTime, id, profileId, profileService, sentAt, serviceUpdateId, statistics, status, text, textFormatted, userId, via);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Update {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    dueAt: ").append(toIndentedString(dueAt)).append("\n");
    sb.append("    dueTime: ").append(toIndentedString(dueTime)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    profileId: ").append(toIndentedString(profileId)).append("\n");
    sb.append("    profileService: ").append(toIndentedString(profileService)).append("\n");
    sb.append("    sentAt: ").append(toIndentedString(sentAt)).append("\n");
    sb.append("    serviceUpdateId: ").append(toIndentedString(serviceUpdateId)).append("\n");
    sb.append("    statistics: ").append(toIndentedString(statistics)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
    sb.append("    textFormatted: ").append(toIndentedString(textFormatted)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    via: ").append(toIndentedString(via)).append("\n");
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
    openapiFields.add("day");
    openapiFields.add("due_at");
    openapiFields.add("due_time");
    openapiFields.add("id");
    openapiFields.add("profile_id");
    openapiFields.add("profile_service");
    openapiFields.add("sent_at");
    openapiFields.add("service_update_id");
    openapiFields.add("statistics");
    openapiFields.add("status");
    openapiFields.add("text");
    openapiFields.add("text_formatted");
    openapiFields.add("user_id");
    openapiFields.add("via");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Update
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Update.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Update is not found in the empty JSON string", Update.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Update.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Update` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("day") != null && !jsonObj.get("day").isJsonNull()) && !jsonObj.get("day").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `day` to be a primitive type in the JSON string but got `%s`", jsonObj.get("day").toString()));
      }
      if ((jsonObj.get("due_time") != null && !jsonObj.get("due_time").isJsonNull()) && !jsonObj.get("due_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `due_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("due_time").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("profile_id") != null && !jsonObj.get("profile_id").isJsonNull()) && !jsonObj.get("profile_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profile_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profile_id").toString()));
      }
      if ((jsonObj.get("profile_service") != null && !jsonObj.get("profile_service").isJsonNull()) && !jsonObj.get("profile_service").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profile_service` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profile_service").toString()));
      }
      if ((jsonObj.get("service_update_id") != null && !jsonObj.get("service_update_id").isJsonNull()) && !jsonObj.get("service_update_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_update_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_update_id").toString()));
      }
      // validate the optional field `statistics`
      if (jsonObj.get("statistics") != null && !jsonObj.get("statistics").isJsonNull()) {
        UpdateStatistics.validateJsonElement(jsonObj.get("statistics"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      if ((jsonObj.get("text") != null && !jsonObj.get("text").isJsonNull()) && !jsonObj.get("text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("text").toString()));
      }
      if ((jsonObj.get("text_formatted") != null && !jsonObj.get("text_formatted").isJsonNull()) && !jsonObj.get("text_formatted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `text_formatted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("text_formatted").toString()));
      }
      if ((jsonObj.get("user_id") != null && !jsonObj.get("user_id").isJsonNull()) && !jsonObj.get("user_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_id").toString()));
      }
      if ((jsonObj.get("via") != null && !jsonObj.get("via").isJsonNull()) && !jsonObj.get("via").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `via` to be a primitive type in the JSON string but got `%s`", jsonObj.get("via").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Update.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Update' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Update> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Update.class));

       return (TypeAdapter<T>) new TypeAdapter<Update>() {
           @Override
           public void write(JsonWriter out, Update value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Update read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Update given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Update
   * @throws IOException if the JSON string is invalid with respect to Update
   */
  public static Update fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Update.class);
  }

  /**
   * Convert an instance of Update to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

