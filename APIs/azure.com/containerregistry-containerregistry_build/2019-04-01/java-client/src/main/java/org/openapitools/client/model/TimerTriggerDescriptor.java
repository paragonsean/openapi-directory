/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-04-01
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
 * TimerTriggerDescriptor
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TimerTriggerDescriptor {
  public static final String SERIALIZED_NAME_SCHEDULE_OCCURRENCE = "scheduleOccurrence";
  @SerializedName(SERIALIZED_NAME_SCHEDULE_OCCURRENCE)
  private String scheduleOccurrence;

  public static final String SERIALIZED_NAME_TIMER_TRIGGER_NAME = "timerTriggerName";
  @SerializedName(SERIALIZED_NAME_TIMER_TRIGGER_NAME)
  private String timerTriggerName;

  public TimerTriggerDescriptor() {
  }

  public TimerTriggerDescriptor scheduleOccurrence(String scheduleOccurrence) {
    this.scheduleOccurrence = scheduleOccurrence;
    return this;
  }

  /**
   * The occurrence that triggered the run.
   * @return scheduleOccurrence
   */
  @javax.annotation.Nullable
  public String getScheduleOccurrence() {
    return scheduleOccurrence;
  }

  public void setScheduleOccurrence(String scheduleOccurrence) {
    this.scheduleOccurrence = scheduleOccurrence;
  }


  public TimerTriggerDescriptor timerTriggerName(String timerTriggerName) {
    this.timerTriggerName = timerTriggerName;
    return this;
  }

  /**
   * The timer trigger name that caused the run.
   * @return timerTriggerName
   */
  @javax.annotation.Nullable
  public String getTimerTriggerName() {
    return timerTriggerName;
  }

  public void setTimerTriggerName(String timerTriggerName) {
    this.timerTriggerName = timerTriggerName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TimerTriggerDescriptor timerTriggerDescriptor = (TimerTriggerDescriptor) o;
    return Objects.equals(this.scheduleOccurrence, timerTriggerDescriptor.scheduleOccurrence) &&
        Objects.equals(this.timerTriggerName, timerTriggerDescriptor.timerTriggerName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(scheduleOccurrence, timerTriggerName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TimerTriggerDescriptor {\n");
    sb.append("    scheduleOccurrence: ").append(toIndentedString(scheduleOccurrence)).append("\n");
    sb.append("    timerTriggerName: ").append(toIndentedString(timerTriggerName)).append("\n");
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
    openapiFields.add("scheduleOccurrence");
    openapiFields.add("timerTriggerName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TimerTriggerDescriptor
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TimerTriggerDescriptor.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TimerTriggerDescriptor is not found in the empty JSON string", TimerTriggerDescriptor.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TimerTriggerDescriptor.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TimerTriggerDescriptor` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("scheduleOccurrence") != null && !jsonObj.get("scheduleOccurrence").isJsonNull()) && !jsonObj.get("scheduleOccurrence").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scheduleOccurrence` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scheduleOccurrence").toString()));
      }
      if ((jsonObj.get("timerTriggerName") != null && !jsonObj.get("timerTriggerName").isJsonNull()) && !jsonObj.get("timerTriggerName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timerTriggerName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timerTriggerName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TimerTriggerDescriptor.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TimerTriggerDescriptor' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TimerTriggerDescriptor> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TimerTriggerDescriptor.class));

       return (TypeAdapter<T>) new TypeAdapter<TimerTriggerDescriptor>() {
           @Override
           public void write(JsonWriter out, TimerTriggerDescriptor value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TimerTriggerDescriptor read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TimerTriggerDescriptor given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TimerTriggerDescriptor
   * @throws IOException if the JSON string is invalid with respect to TimerTriggerDescriptor
   */
  public static TimerTriggerDescriptor fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TimerTriggerDescriptor.class);
  }

  /**
   * Convert an instance of TimerTriggerDescriptor to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

