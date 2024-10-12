/*
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
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
 * GetUserExternalId200ResponseUserUserNotificationSchedule
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:34.324076-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetUserExternalId200ResponseUserUserNotificationSchedule {
  public static final String SERIALIZED_NAME_DAY0_END_TIME = "day_0_end_time";
  @SerializedName(SERIALIZED_NAME_DAY0_END_TIME)
  private Integer day0EndTime;

  public static final String SERIALIZED_NAME_DAY0_START_TIME = "day_0_start_time";
  @SerializedName(SERIALIZED_NAME_DAY0_START_TIME)
  private Integer day0StartTime;

  public static final String SERIALIZED_NAME_DAY1_END_TIME = "day_1_end_time";
  @SerializedName(SERIALIZED_NAME_DAY1_END_TIME)
  private Integer day1EndTime;

  public static final String SERIALIZED_NAME_DAY1_START_TIME = "day_1_start_time";
  @SerializedName(SERIALIZED_NAME_DAY1_START_TIME)
  private Integer day1StartTime;

  public static final String SERIALIZED_NAME_DAY2_END_TIME = "day_2_end_time";
  @SerializedName(SERIALIZED_NAME_DAY2_END_TIME)
  private Integer day2EndTime;

  public static final String SERIALIZED_NAME_DAY2_START_TIME = "day_2_start_time";
  @SerializedName(SERIALIZED_NAME_DAY2_START_TIME)
  private Integer day2StartTime;

  public static final String SERIALIZED_NAME_DAY3_END_TIME = "day_3_end_time";
  @SerializedName(SERIALIZED_NAME_DAY3_END_TIME)
  private Integer day3EndTime;

  public static final String SERIALIZED_NAME_DAY3_START_TIME = "day_3_start_time";
  @SerializedName(SERIALIZED_NAME_DAY3_START_TIME)
  private Integer day3StartTime;

  public static final String SERIALIZED_NAME_DAY4_END_TIME = "day_4_end_time";
  @SerializedName(SERIALIZED_NAME_DAY4_END_TIME)
  private Integer day4EndTime;

  public static final String SERIALIZED_NAME_DAY4_START_TIME = "day_4_start_time";
  @SerializedName(SERIALIZED_NAME_DAY4_START_TIME)
  private Integer day4StartTime;

  public static final String SERIALIZED_NAME_DAY5_END_TIME = "day_5_end_time";
  @SerializedName(SERIALIZED_NAME_DAY5_END_TIME)
  private Integer day5EndTime;

  public static final String SERIALIZED_NAME_DAY5_START_TIME = "day_5_start_time";
  @SerializedName(SERIALIZED_NAME_DAY5_START_TIME)
  private Integer day5StartTime;

  public static final String SERIALIZED_NAME_DAY6_END_TIME = "day_6_end_time";
  @SerializedName(SERIALIZED_NAME_DAY6_END_TIME)
  private Integer day6EndTime;

  public static final String SERIALIZED_NAME_DAY6_START_TIME = "day_6_start_time";
  @SerializedName(SERIALIZED_NAME_DAY6_START_TIME)
  private Integer day6StartTime;

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public GetUserExternalId200ResponseUserUserNotificationSchedule() {
  }

  public GetUserExternalId200ResponseUserUserNotificationSchedule day0EndTime(Integer day0EndTime) {
    this.day0EndTime = day0EndTime;
    return this;
  }

  /**
   * Get day0EndTime
   * @return day0EndTime
   */
  @javax.annotation.Nonnull
  public Integer getDay0EndTime() {
    return day0EndTime;
  }

  public void setDay0EndTime(Integer day0EndTime) {
    this.day0EndTime = day0EndTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day0StartTime(Integer day0StartTime) {
    this.day0StartTime = day0StartTime;
    return this;
  }

  /**
   * Get day0StartTime
   * @return day0StartTime
   */
  @javax.annotation.Nonnull
  public Integer getDay0StartTime() {
    return day0StartTime;
  }

  public void setDay0StartTime(Integer day0StartTime) {
    this.day0StartTime = day0StartTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day1EndTime(Integer day1EndTime) {
    this.day1EndTime = day1EndTime;
    return this;
  }

  /**
   * Get day1EndTime
   * @return day1EndTime
   */
  @javax.annotation.Nonnull
  public Integer getDay1EndTime() {
    return day1EndTime;
  }

  public void setDay1EndTime(Integer day1EndTime) {
    this.day1EndTime = day1EndTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day1StartTime(Integer day1StartTime) {
    this.day1StartTime = day1StartTime;
    return this;
  }

  /**
   * Get day1StartTime
   * @return day1StartTime
   */
  @javax.annotation.Nonnull
  public Integer getDay1StartTime() {
    return day1StartTime;
  }

  public void setDay1StartTime(Integer day1StartTime) {
    this.day1StartTime = day1StartTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day2EndTime(Integer day2EndTime) {
    this.day2EndTime = day2EndTime;
    return this;
  }

  /**
   * Get day2EndTime
   * @return day2EndTime
   */
  @javax.annotation.Nonnull
  public Integer getDay2EndTime() {
    return day2EndTime;
  }

  public void setDay2EndTime(Integer day2EndTime) {
    this.day2EndTime = day2EndTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day2StartTime(Integer day2StartTime) {
    this.day2StartTime = day2StartTime;
    return this;
  }

  /**
   * Get day2StartTime
   * @return day2StartTime
   */
  @javax.annotation.Nonnull
  public Integer getDay2StartTime() {
    return day2StartTime;
  }

  public void setDay2StartTime(Integer day2StartTime) {
    this.day2StartTime = day2StartTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day3EndTime(Integer day3EndTime) {
    this.day3EndTime = day3EndTime;
    return this;
  }

  /**
   * Get day3EndTime
   * @return day3EndTime
   */
  @javax.annotation.Nonnull
  public Integer getDay3EndTime() {
    return day3EndTime;
  }

  public void setDay3EndTime(Integer day3EndTime) {
    this.day3EndTime = day3EndTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day3StartTime(Integer day3StartTime) {
    this.day3StartTime = day3StartTime;
    return this;
  }

  /**
   * Get day3StartTime
   * @return day3StartTime
   */
  @javax.annotation.Nonnull
  public Integer getDay3StartTime() {
    return day3StartTime;
  }

  public void setDay3StartTime(Integer day3StartTime) {
    this.day3StartTime = day3StartTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day4EndTime(Integer day4EndTime) {
    this.day4EndTime = day4EndTime;
    return this;
  }

  /**
   * Get day4EndTime
   * @return day4EndTime
   */
  @javax.annotation.Nonnull
  public Integer getDay4EndTime() {
    return day4EndTime;
  }

  public void setDay4EndTime(Integer day4EndTime) {
    this.day4EndTime = day4EndTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day4StartTime(Integer day4StartTime) {
    this.day4StartTime = day4StartTime;
    return this;
  }

  /**
   * Get day4StartTime
   * @return day4StartTime
   */
  @javax.annotation.Nonnull
  public Integer getDay4StartTime() {
    return day4StartTime;
  }

  public void setDay4StartTime(Integer day4StartTime) {
    this.day4StartTime = day4StartTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day5EndTime(Integer day5EndTime) {
    this.day5EndTime = day5EndTime;
    return this;
  }

  /**
   * Get day5EndTime
   * @return day5EndTime
   */
  @javax.annotation.Nonnull
  public Integer getDay5EndTime() {
    return day5EndTime;
  }

  public void setDay5EndTime(Integer day5EndTime) {
    this.day5EndTime = day5EndTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day5StartTime(Integer day5StartTime) {
    this.day5StartTime = day5StartTime;
    return this;
  }

  /**
   * Get day5StartTime
   * @return day5StartTime
   */
  @javax.annotation.Nonnull
  public Integer getDay5StartTime() {
    return day5StartTime;
  }

  public void setDay5StartTime(Integer day5StartTime) {
    this.day5StartTime = day5StartTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day6EndTime(Integer day6EndTime) {
    this.day6EndTime = day6EndTime;
    return this;
  }

  /**
   * Get day6EndTime
   * @return day6EndTime
   */
  @javax.annotation.Nonnull
  public Integer getDay6EndTime() {
    return day6EndTime;
  }

  public void setDay6EndTime(Integer day6EndTime) {
    this.day6EndTime = day6EndTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule day6StartTime(Integer day6StartTime) {
    this.day6StartTime = day6StartTime;
    return this;
  }

  /**
   * Get day6StartTime
   * @return day6StartTime
   */
  @javax.annotation.Nonnull
  public Integer getDay6StartTime() {
    return day6StartTime;
  }

  public void setDay6StartTime(Integer day6StartTime) {
    this.day6StartTime = day6StartTime;
  }


  public GetUserExternalId200ResponseUserUserNotificationSchedule enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Get enabled
   * @return enabled
   */
  @javax.annotation.Nonnull
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }

  /**
   * A container for additional, undeclared properties.
   * This is a holder for any undeclared properties as specified with
   * the 'additionalProperties' keyword in the OAS document.
   */
  private Map<String, Object> additionalProperties;

  /**
   * Set the additional (undeclared) property with the specified name and value.
   * If the property does not already exist, create it otherwise replace it.
   *
   * @param key name of the property
   * @param value value of the property
   * @return the GetUserExternalId200ResponseUserUserNotificationSchedule instance itself
   */
  public GetUserExternalId200ResponseUserUserNotificationSchedule putAdditionalProperty(String key, Object value) {
    if (this.additionalProperties == null) {
        this.additionalProperties = new HashMap<String, Object>();
    }
    this.additionalProperties.put(key, value);
    return this;
  }

  /**
   * Return the additional (undeclared) property.
   *
   * @return a map of objects
   */
  public Map<String, Object> getAdditionalProperties() {
    return additionalProperties;
  }

  /**
   * Return the additional (undeclared) property with the specified name.
   *
   * @param key name of the property
   * @return an object
   */
  public Object getAdditionalProperty(String key) {
    if (this.additionalProperties == null) {
        return null;
    }
    return this.additionalProperties.get(key);
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetUserExternalId200ResponseUserUserNotificationSchedule getUserExternalId200ResponseUserUserNotificationSchedule = (GetUserExternalId200ResponseUserUserNotificationSchedule) o;
    return Objects.equals(this.day0EndTime, getUserExternalId200ResponseUserUserNotificationSchedule.day0EndTime) &&
        Objects.equals(this.day0StartTime, getUserExternalId200ResponseUserUserNotificationSchedule.day0StartTime) &&
        Objects.equals(this.day1EndTime, getUserExternalId200ResponseUserUserNotificationSchedule.day1EndTime) &&
        Objects.equals(this.day1StartTime, getUserExternalId200ResponseUserUserNotificationSchedule.day1StartTime) &&
        Objects.equals(this.day2EndTime, getUserExternalId200ResponseUserUserNotificationSchedule.day2EndTime) &&
        Objects.equals(this.day2StartTime, getUserExternalId200ResponseUserUserNotificationSchedule.day2StartTime) &&
        Objects.equals(this.day3EndTime, getUserExternalId200ResponseUserUserNotificationSchedule.day3EndTime) &&
        Objects.equals(this.day3StartTime, getUserExternalId200ResponseUserUserNotificationSchedule.day3StartTime) &&
        Objects.equals(this.day4EndTime, getUserExternalId200ResponseUserUserNotificationSchedule.day4EndTime) &&
        Objects.equals(this.day4StartTime, getUserExternalId200ResponseUserUserNotificationSchedule.day4StartTime) &&
        Objects.equals(this.day5EndTime, getUserExternalId200ResponseUserUserNotificationSchedule.day5EndTime) &&
        Objects.equals(this.day5StartTime, getUserExternalId200ResponseUserUserNotificationSchedule.day5StartTime) &&
        Objects.equals(this.day6EndTime, getUserExternalId200ResponseUserUserNotificationSchedule.day6EndTime) &&
        Objects.equals(this.day6StartTime, getUserExternalId200ResponseUserUserNotificationSchedule.day6StartTime) &&
        Objects.equals(this.enabled, getUserExternalId200ResponseUserUserNotificationSchedule.enabled)&&
        Objects.equals(this.additionalProperties, getUserExternalId200ResponseUserUserNotificationSchedule.additionalProperties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(day0EndTime, day0StartTime, day1EndTime, day1StartTime, day2EndTime, day2StartTime, day3EndTime, day3StartTime, day4EndTime, day4StartTime, day5EndTime, day5StartTime, day6EndTime, day6StartTime, enabled, additionalProperties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetUserExternalId200ResponseUserUserNotificationSchedule {\n");
    sb.append("    day0EndTime: ").append(toIndentedString(day0EndTime)).append("\n");
    sb.append("    day0StartTime: ").append(toIndentedString(day0StartTime)).append("\n");
    sb.append("    day1EndTime: ").append(toIndentedString(day1EndTime)).append("\n");
    sb.append("    day1StartTime: ").append(toIndentedString(day1StartTime)).append("\n");
    sb.append("    day2EndTime: ").append(toIndentedString(day2EndTime)).append("\n");
    sb.append("    day2StartTime: ").append(toIndentedString(day2StartTime)).append("\n");
    sb.append("    day3EndTime: ").append(toIndentedString(day3EndTime)).append("\n");
    sb.append("    day3StartTime: ").append(toIndentedString(day3StartTime)).append("\n");
    sb.append("    day4EndTime: ").append(toIndentedString(day4EndTime)).append("\n");
    sb.append("    day4StartTime: ").append(toIndentedString(day4StartTime)).append("\n");
    sb.append("    day5EndTime: ").append(toIndentedString(day5EndTime)).append("\n");
    sb.append("    day5StartTime: ").append(toIndentedString(day5StartTime)).append("\n");
    sb.append("    day6EndTime: ").append(toIndentedString(day6EndTime)).append("\n");
    sb.append("    day6StartTime: ").append(toIndentedString(day6StartTime)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    additionalProperties: ").append(toIndentedString(additionalProperties)).append("\n");
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
    openapiFields.add("day_0_end_time");
    openapiFields.add("day_0_start_time");
    openapiFields.add("day_1_end_time");
    openapiFields.add("day_1_start_time");
    openapiFields.add("day_2_end_time");
    openapiFields.add("day_2_start_time");
    openapiFields.add("day_3_end_time");
    openapiFields.add("day_3_start_time");
    openapiFields.add("day_4_end_time");
    openapiFields.add("day_4_start_time");
    openapiFields.add("day_5_end_time");
    openapiFields.add("day_5_start_time");
    openapiFields.add("day_6_end_time");
    openapiFields.add("day_6_start_time");
    openapiFields.add("enabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("day_0_end_time");
    openapiRequiredFields.add("day_0_start_time");
    openapiRequiredFields.add("day_1_end_time");
    openapiRequiredFields.add("day_1_start_time");
    openapiRequiredFields.add("day_2_end_time");
    openapiRequiredFields.add("day_2_start_time");
    openapiRequiredFields.add("day_3_end_time");
    openapiRequiredFields.add("day_3_start_time");
    openapiRequiredFields.add("day_4_end_time");
    openapiRequiredFields.add("day_4_start_time");
    openapiRequiredFields.add("day_5_end_time");
    openapiRequiredFields.add("day_5_start_time");
    openapiRequiredFields.add("day_6_end_time");
    openapiRequiredFields.add("day_6_start_time");
    openapiRequiredFields.add("enabled");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetUserExternalId200ResponseUserUserNotificationSchedule
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetUserExternalId200ResponseUserUserNotificationSchedule.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetUserExternalId200ResponseUserUserNotificationSchedule is not found in the empty JSON string", GetUserExternalId200ResponseUserUserNotificationSchedule.openapiRequiredFields.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetUserExternalId200ResponseUserUserNotificationSchedule.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetUserExternalId200ResponseUserUserNotificationSchedule.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetUserExternalId200ResponseUserUserNotificationSchedule' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetUserExternalId200ResponseUserUserNotificationSchedule> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetUserExternalId200ResponseUserUserNotificationSchedule.class));

       return (TypeAdapter<T>) new TypeAdapter<GetUserExternalId200ResponseUserUserNotificationSchedule>() {
           @Override
           public void write(JsonWriter out, GetUserExternalId200ResponseUserUserNotificationSchedule value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             obj.remove("additionalProperties");
             // serialize additional properties
             if (value.getAdditionalProperties() != null) {
               for (Map.Entry<String, Object> entry : value.getAdditionalProperties().entrySet()) {
                 if (entry.getValue() instanceof String)
                   obj.addProperty(entry.getKey(), (String) entry.getValue());
                 else if (entry.getValue() instanceof Number)
                   obj.addProperty(entry.getKey(), (Number) entry.getValue());
                 else if (entry.getValue() instanceof Boolean)
                   obj.addProperty(entry.getKey(), (Boolean) entry.getValue());
                 else if (entry.getValue() instanceof Character)
                   obj.addProperty(entry.getKey(), (Character) entry.getValue());
                 else {
                   JsonElement jsonElement = gson.toJsonTree(entry.getValue());
                   if (jsonElement.isJsonArray()) {
                     obj.add(entry.getKey(), jsonElement.getAsJsonArray());
                   } else {
                     obj.add(entry.getKey(), jsonElement.getAsJsonObject());
                   }
                 }
               }
             }
             elementAdapter.write(out, obj);
           }

           @Override
           public GetUserExternalId200ResponseUserUserNotificationSchedule read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             JsonObject jsonObj = jsonElement.getAsJsonObject();
             // store additional fields in the deserialized instance
             GetUserExternalId200ResponseUserUserNotificationSchedule instance = thisAdapter.fromJsonTree(jsonObj);
             for (Map.Entry<String, JsonElement> entry : jsonObj.entrySet()) {
               if (!openapiFields.contains(entry.getKey())) {
                 if (entry.getValue().isJsonPrimitive()) { // primitive type
                   if (entry.getValue().getAsJsonPrimitive().isString())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsString());
                   else if (entry.getValue().getAsJsonPrimitive().isNumber())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsNumber());
                   else if (entry.getValue().getAsJsonPrimitive().isBoolean())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsBoolean());
                   else
                     throw new IllegalArgumentException(String.format("The field `%s` has unknown primitive type. Value: %s", entry.getKey(), entry.getValue().toString()));
                 } else if (entry.getValue().isJsonArray()) {
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), List.class));
                 } else { // JSON object
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), HashMap.class));
                 }
               }
             }
             return instance;
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetUserExternalId200ResponseUserUserNotificationSchedule given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetUserExternalId200ResponseUserUserNotificationSchedule
   * @throws IOException if the JSON string is invalid with respect to GetUserExternalId200ResponseUserUserNotificationSchedule
   */
  public static GetUserExternalId200ResponseUserUserNotificationSchedule fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetUserExternalId200ResponseUserUserNotificationSchedule.class);
  }

  /**
   * Convert an instance of GetUserExternalId200ResponseUserUserNotificationSchedule to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

