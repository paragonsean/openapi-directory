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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BaseImageTrigger;
import org.openapitools.client.model.SourceTrigger;
import org.openapitools.client.model.TimerTrigger;

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
 * The properties of a trigger.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:25:02.709621-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TriggerProperties {
  public static final String SERIALIZED_NAME_BASE_IMAGE_TRIGGER = "baseImageTrigger";
  @SerializedName(SERIALIZED_NAME_BASE_IMAGE_TRIGGER)
  private BaseImageTrigger baseImageTrigger;

  public static final String SERIALIZED_NAME_SOURCE_TRIGGERS = "sourceTriggers";
  @SerializedName(SERIALIZED_NAME_SOURCE_TRIGGERS)
  private List<SourceTrigger> sourceTriggers = new ArrayList<>();

  public static final String SERIALIZED_NAME_TIMER_TRIGGERS = "timerTriggers";
  @SerializedName(SERIALIZED_NAME_TIMER_TRIGGERS)
  private List<TimerTrigger> timerTriggers = new ArrayList<>();

  public TriggerProperties() {
  }

  public TriggerProperties baseImageTrigger(BaseImageTrigger baseImageTrigger) {
    this.baseImageTrigger = baseImageTrigger;
    return this;
  }

  /**
   * Get baseImageTrigger
   * @return baseImageTrigger
   */
  @javax.annotation.Nullable
  public BaseImageTrigger getBaseImageTrigger() {
    return baseImageTrigger;
  }

  public void setBaseImageTrigger(BaseImageTrigger baseImageTrigger) {
    this.baseImageTrigger = baseImageTrigger;
  }


  public TriggerProperties sourceTriggers(List<SourceTrigger> sourceTriggers) {
    this.sourceTriggers = sourceTriggers;
    return this;
  }

  public TriggerProperties addSourceTriggersItem(SourceTrigger sourceTriggersItem) {
    if (this.sourceTriggers == null) {
      this.sourceTriggers = new ArrayList<>();
    }
    this.sourceTriggers.add(sourceTriggersItem);
    return this;
  }

  /**
   * The collection of triggers based on source code repository.
   * @return sourceTriggers
   */
  @javax.annotation.Nullable
  public List<SourceTrigger> getSourceTriggers() {
    return sourceTriggers;
  }

  public void setSourceTriggers(List<SourceTrigger> sourceTriggers) {
    this.sourceTriggers = sourceTriggers;
  }


  public TriggerProperties timerTriggers(List<TimerTrigger> timerTriggers) {
    this.timerTriggers = timerTriggers;
    return this;
  }

  public TriggerProperties addTimerTriggersItem(TimerTrigger timerTriggersItem) {
    if (this.timerTriggers == null) {
      this.timerTriggers = new ArrayList<>();
    }
    this.timerTriggers.add(timerTriggersItem);
    return this;
  }

  /**
   * The collection of timer triggers.
   * @return timerTriggers
   */
  @javax.annotation.Nullable
  public List<TimerTrigger> getTimerTriggers() {
    return timerTriggers;
  }

  public void setTimerTriggers(List<TimerTrigger> timerTriggers) {
    this.timerTriggers = timerTriggers;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TriggerProperties triggerProperties = (TriggerProperties) o;
    return Objects.equals(this.baseImageTrigger, triggerProperties.baseImageTrigger) &&
        Objects.equals(this.sourceTriggers, triggerProperties.sourceTriggers) &&
        Objects.equals(this.timerTriggers, triggerProperties.timerTriggers);
  }

  @Override
  public int hashCode() {
    return Objects.hash(baseImageTrigger, sourceTriggers, timerTriggers);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TriggerProperties {\n");
    sb.append("    baseImageTrigger: ").append(toIndentedString(baseImageTrigger)).append("\n");
    sb.append("    sourceTriggers: ").append(toIndentedString(sourceTriggers)).append("\n");
    sb.append("    timerTriggers: ").append(toIndentedString(timerTriggers)).append("\n");
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
    openapiFields.add("baseImageTrigger");
    openapiFields.add("sourceTriggers");
    openapiFields.add("timerTriggers");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TriggerProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TriggerProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TriggerProperties is not found in the empty JSON string", TriggerProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TriggerProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TriggerProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `baseImageTrigger`
      if (jsonObj.get("baseImageTrigger") != null && !jsonObj.get("baseImageTrigger").isJsonNull()) {
        BaseImageTrigger.validateJsonElement(jsonObj.get("baseImageTrigger"));
      }
      if (jsonObj.get("sourceTriggers") != null && !jsonObj.get("sourceTriggers").isJsonNull()) {
        JsonArray jsonArraysourceTriggers = jsonObj.getAsJsonArray("sourceTriggers");
        if (jsonArraysourceTriggers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("sourceTriggers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `sourceTriggers` to be an array in the JSON string but got `%s`", jsonObj.get("sourceTriggers").toString()));
          }

          // validate the optional field `sourceTriggers` (array)
          for (int i = 0; i < jsonArraysourceTriggers.size(); i++) {
            SourceTrigger.validateJsonElement(jsonArraysourceTriggers.get(i));
          };
        }
      }
      if (jsonObj.get("timerTriggers") != null && !jsonObj.get("timerTriggers").isJsonNull()) {
        JsonArray jsonArraytimerTriggers = jsonObj.getAsJsonArray("timerTriggers");
        if (jsonArraytimerTriggers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("timerTriggers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `timerTriggers` to be an array in the JSON string but got `%s`", jsonObj.get("timerTriggers").toString()));
          }

          // validate the optional field `timerTriggers` (array)
          for (int i = 0; i < jsonArraytimerTriggers.size(); i++) {
            TimerTrigger.validateJsonElement(jsonArraytimerTriggers.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TriggerProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TriggerProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TriggerProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TriggerProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<TriggerProperties>() {
           @Override
           public void write(JsonWriter out, TriggerProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TriggerProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TriggerProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TriggerProperties
   * @throws IOException if the JSON string is invalid with respect to TriggerProperties
   */
  public static TriggerProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TriggerProperties.class);
  }

  /**
   * Convert an instance of TriggerProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

