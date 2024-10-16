/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
 * Alerting webhook
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WebhooksList200ResponseValuesInner {
  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  /**
   * Alerting EventTypes enum
   */
  @JsonAdapter(EventTypesEnum.Adapter.class)
  public enum EventTypesEnum {
    NEW_CRASH_GROUP_CREATED("newCrashGroupCreated"),
    
    NEW_APP_RELEASED("newAppReleased");

    private String value;

    EventTypesEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EventTypesEnum fromValue(String value) {
      for (EventTypesEnum b : EventTypesEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EventTypesEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EventTypesEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EventTypesEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EventTypesEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EventTypesEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_EVENT_TYPES = "event_types";
  @SerializedName(SERIALIZED_NAME_EVENT_TYPES)
  private List<EventTypesEnum> eventTypes = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public WebhooksList200ResponseValuesInner() {
  }

  public WebhooksList200ResponseValuesInner enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Allows eanble/disable webhook
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public WebhooksList200ResponseValuesInner eventTypes(List<EventTypesEnum> eventTypes) {
    this.eventTypes = eventTypes;
    return this;
  }

  public WebhooksList200ResponseValuesInner addEventTypesItem(EventTypesEnum eventTypesItem) {
    if (this.eventTypes == null) {
      this.eventTypes = new ArrayList<>();
    }
    this.eventTypes.add(eventTypesItem);
    return this;
  }

  /**
   * Event types enabled for webhook
   * @return eventTypes
   */
  @javax.annotation.Nonnull
  public List<EventTypesEnum> getEventTypes() {
    return eventTypes;
  }

  public void setEventTypes(List<EventTypesEnum> eventTypes) {
    this.eventTypes = eventTypes;
  }


  public WebhooksList200ResponseValuesInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The unique id (UUID) of the webhook
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public WebhooksList200ResponseValuesInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * display name of the webhook
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public WebhooksList200ResponseValuesInner url(String url) {
    this.url = url;
    return this;
  }

  /**
   * target url of the webhook
   * @return url
   */
  @javax.annotation.Nonnull
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebhooksList200ResponseValuesInner webhooksList200ResponseValuesInner = (WebhooksList200ResponseValuesInner) o;
    return Objects.equals(this.enabled, webhooksList200ResponseValuesInner.enabled) &&
        Objects.equals(this.eventTypes, webhooksList200ResponseValuesInner.eventTypes) &&
        Objects.equals(this.id, webhooksList200ResponseValuesInner.id) &&
        Objects.equals(this.name, webhooksList200ResponseValuesInner.name) &&
        Objects.equals(this.url, webhooksList200ResponseValuesInner.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(enabled, eventTypes, id, name, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebhooksList200ResponseValuesInner {\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    eventTypes: ").append(toIndentedString(eventTypes)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("enabled");
    openapiFields.add("event_types");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("event_types");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WebhooksList200ResponseValuesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WebhooksList200ResponseValuesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WebhooksList200ResponseValuesInner is not found in the empty JSON string", WebhooksList200ResponseValuesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WebhooksList200ResponseValuesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WebhooksList200ResponseValuesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : WebhooksList200ResponseValuesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the required json array is present
      if (jsonObj.get("event_types") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("event_types").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `event_types` to be an array in the JSON string but got `%s`", jsonObj.get("event_types").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WebhooksList200ResponseValuesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WebhooksList200ResponseValuesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WebhooksList200ResponseValuesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WebhooksList200ResponseValuesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<WebhooksList200ResponseValuesInner>() {
           @Override
           public void write(JsonWriter out, WebhooksList200ResponseValuesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WebhooksList200ResponseValuesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WebhooksList200ResponseValuesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WebhooksList200ResponseValuesInner
   * @throws IOException if the JSON string is invalid with respect to WebhooksList200ResponseValuesInner
   */
  public static WebhooksList200ResponseValuesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WebhooksList200ResponseValuesInner.class);
  }

  /**
   * Convert an instance of WebhooksList200ResponseValuesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

