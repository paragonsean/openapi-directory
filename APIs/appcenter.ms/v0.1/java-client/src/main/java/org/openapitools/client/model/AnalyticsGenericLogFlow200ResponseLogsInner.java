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
import java.time.OffsetDateTime;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import org.openapitools.client.model.AnalyticsGenericLogFlow200ResponseLogsInnerDevice;

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
 * Generic log.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AnalyticsGenericLogFlow200ResponseLogsInner {
  public static final String SERIALIZED_NAME_ACCOUNT_ID = "account_id";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_ID)
  private String accountId;

  public static final String SERIALIZED_NAME_AUTH_PROVIDER = "auth_provider";
  @SerializedName(SERIALIZED_NAME_AUTH_PROVIDER)
  private String authProvider;

  public static final String SERIALIZED_NAME_DEVICE = "device";
  @SerializedName(SERIALIZED_NAME_DEVICE)
  private AnalyticsGenericLogFlow200ResponseLogsInnerDevice device;

  public static final String SERIALIZED_NAME_EVENT_ID = "event_id";
  @SerializedName(SERIALIZED_NAME_EVENT_ID)
  private String eventId;

  public static final String SERIALIZED_NAME_EVENT_NAME = "event_name";
  @SerializedName(SERIALIZED_NAME_EVENT_NAME)
  private String eventName;

  public static final String SERIALIZED_NAME_INSTALL_ID = "install_id";
  @SerializedName(SERIALIZED_NAME_INSTALL_ID)
  private UUID installId;

  public static final String SERIALIZED_NAME_MESSAGE_ID = "message_id";
  @SerializedName(SERIALIZED_NAME_MESSAGE_ID)
  private String messageId;

  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private Map<String, String> properties = new HashMap<>();

  public static final String SERIALIZED_NAME_SESSION_ID = "session_id";
  @SerializedName(SERIALIZED_NAME_SESSION_ID)
  private UUID sessionId;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private OffsetDateTime timestamp;

  /**
   * Log type. 
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    EVENT("event"),
    
    PAGE("page"),
    
    START_SESSION("start_session"),
    
    ERROR("error"),
    
    START_SERVICE("start_service"),
    
    CUSTOM_PROPERTIES("custom_properties");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public AnalyticsGenericLogFlow200ResponseLogsInner() {
  }

  public AnalyticsGenericLogFlow200ResponseLogsInner accountId(String accountId) {
    this.accountId = accountId;
    return this;
  }

  /**
   * Account ID of the authenticated user. 
   * @return accountId
   */
  @javax.annotation.Nullable
  public String getAccountId() {
    return accountId;
  }

  public void setAccountId(String accountId) {
    this.accountId = accountId;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner authProvider(String authProvider) {
    this.authProvider = authProvider;
    return this;
  }

  /**
   * Auth service provider. 
   * @return authProvider
   */
  @javax.annotation.Nullable
  public String getAuthProvider() {
    return authProvider;
  }

  public void setAuthProvider(String authProvider) {
    this.authProvider = authProvider;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner device(AnalyticsGenericLogFlow200ResponseLogsInnerDevice device) {
    this.device = device;
    return this;
  }

  /**
   * Get device
   * @return device
   */
  @javax.annotation.Nonnull
  public AnalyticsGenericLogFlow200ResponseLogsInnerDevice getDevice() {
    return device;
  }

  public void setDevice(AnalyticsGenericLogFlow200ResponseLogsInnerDevice device) {
    this.device = device;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner eventId(String eventId) {
    this.eventId = eventId;
    return this;
  }

  /**
   * Event ID. 
   * @return eventId
   */
  @javax.annotation.Nullable
  public String getEventId() {
    return eventId;
  }

  public void setEventId(String eventId) {
    this.eventId = eventId;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner eventName(String eventName) {
    this.eventName = eventName;
    return this;
  }

  /**
   * Event name. 
   * @return eventName
   */
  @javax.annotation.Nullable
  public String getEventName() {
    return eventName;
  }

  public void setEventName(String eventName) {
    this.eventName = eventName;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner installId(UUID installId) {
    this.installId = installId;
    return this;
  }

  /**
   * Install ID. 
   * @return installId
   */
  @javax.annotation.Nonnull
  public UUID getInstallId() {
    return installId;
  }

  public void setInstallId(UUID installId) {
    this.installId = installId;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner messageId(String messageId) {
    this.messageId = messageId;
    return this;
  }

  /**
   * Message ID. 
   * @return messageId
   */
  @javax.annotation.Nullable
  public String getMessageId() {
    return messageId;
  }

  public void setMessageId(String messageId) {
    this.messageId = messageId;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner properties(Map<String, String> properties) {
    this.properties = properties;
    return this;
  }

  public AnalyticsGenericLogFlow200ResponseLogsInner putPropertiesItem(String key, String propertiesItem) {
    if (this.properties == null) {
      this.properties = new HashMap<>();
    }
    this.properties.put(key, propertiesItem);
    return this;
  }

  /**
   * event specific properties. 
   * @return properties
   */
  @javax.annotation.Nullable
  public Map<String, String> getProperties() {
    return properties;
  }

  public void setProperties(Map<String, String> properties) {
    this.properties = properties;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner sessionId(UUID sessionId) {
    this.sessionId = sessionId;
    return this;
  }

  /**
   * Session ID. 
   * @return sessionId
   */
  @javax.annotation.Nullable
  public UUID getSessionId() {
    return sessionId;
  }

  public void setSessionId(UUID sessionId) {
    this.sessionId = sessionId;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner timestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
    return this;
  }

  /**
   * Log creation timestamp. 
   * @return timestamp
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getTimestamp() {
    return timestamp;
  }

  public void setTimestamp(OffsetDateTime timestamp) {
    this.timestamp = timestamp;
  }


  public AnalyticsGenericLogFlow200ResponseLogsInner type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Log type. 
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnalyticsGenericLogFlow200ResponseLogsInner analyticsGenericLogFlow200ResponseLogsInner = (AnalyticsGenericLogFlow200ResponseLogsInner) o;
    return Objects.equals(this.accountId, analyticsGenericLogFlow200ResponseLogsInner.accountId) &&
        Objects.equals(this.authProvider, analyticsGenericLogFlow200ResponseLogsInner.authProvider) &&
        Objects.equals(this.device, analyticsGenericLogFlow200ResponseLogsInner.device) &&
        Objects.equals(this.eventId, analyticsGenericLogFlow200ResponseLogsInner.eventId) &&
        Objects.equals(this.eventName, analyticsGenericLogFlow200ResponseLogsInner.eventName) &&
        Objects.equals(this.installId, analyticsGenericLogFlow200ResponseLogsInner.installId) &&
        Objects.equals(this.messageId, analyticsGenericLogFlow200ResponseLogsInner.messageId) &&
        Objects.equals(this.properties, analyticsGenericLogFlow200ResponseLogsInner.properties) &&
        Objects.equals(this.sessionId, analyticsGenericLogFlow200ResponseLogsInner.sessionId) &&
        Objects.equals(this.timestamp, analyticsGenericLogFlow200ResponseLogsInner.timestamp) &&
        Objects.equals(this.type, analyticsGenericLogFlow200ResponseLogsInner.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountId, authProvider, device, eventId, eventName, installId, messageId, properties, sessionId, timestamp, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnalyticsGenericLogFlow200ResponseLogsInner {\n");
    sb.append("    accountId: ").append(toIndentedString(accountId)).append("\n");
    sb.append("    authProvider: ").append(toIndentedString(authProvider)).append("\n");
    sb.append("    device: ").append(toIndentedString(device)).append("\n");
    sb.append("    eventId: ").append(toIndentedString(eventId)).append("\n");
    sb.append("    eventName: ").append(toIndentedString(eventName)).append("\n");
    sb.append("    installId: ").append(toIndentedString(installId)).append("\n");
    sb.append("    messageId: ").append(toIndentedString(messageId)).append("\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
    sb.append("    sessionId: ").append(toIndentedString(sessionId)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("account_id");
    openapiFields.add("auth_provider");
    openapiFields.add("device");
    openapiFields.add("event_id");
    openapiFields.add("event_name");
    openapiFields.add("install_id");
    openapiFields.add("message_id");
    openapiFields.add("properties");
    openapiFields.add("session_id");
    openapiFields.add("timestamp");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("device");
    openapiRequiredFields.add("install_id");
    openapiRequiredFields.add("timestamp");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AnalyticsGenericLogFlow200ResponseLogsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AnalyticsGenericLogFlow200ResponseLogsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AnalyticsGenericLogFlow200ResponseLogsInner is not found in the empty JSON string", AnalyticsGenericLogFlow200ResponseLogsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AnalyticsGenericLogFlow200ResponseLogsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AnalyticsGenericLogFlow200ResponseLogsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : AnalyticsGenericLogFlow200ResponseLogsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("account_id") != null && !jsonObj.get("account_id").isJsonNull()) && !jsonObj.get("account_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `account_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("account_id").toString()));
      }
      if ((jsonObj.get("auth_provider") != null && !jsonObj.get("auth_provider").isJsonNull()) && !jsonObj.get("auth_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auth_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auth_provider").toString()));
      }
      // validate the required field `device`
      AnalyticsGenericLogFlow200ResponseLogsInnerDevice.validateJsonElement(jsonObj.get("device"));
      if ((jsonObj.get("event_id") != null && !jsonObj.get("event_id").isJsonNull()) && !jsonObj.get("event_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `event_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("event_id").toString()));
      }
      if ((jsonObj.get("event_name") != null && !jsonObj.get("event_name").isJsonNull()) && !jsonObj.get("event_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `event_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("event_name").toString()));
      }
      if (!jsonObj.get("install_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `install_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("install_id").toString()));
      }
      if ((jsonObj.get("message_id") != null && !jsonObj.get("message_id").isJsonNull()) && !jsonObj.get("message_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message_id").toString()));
      }
      if ((jsonObj.get("session_id") != null && !jsonObj.get("session_id").isJsonNull()) && !jsonObj.get("session_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `session_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("session_id").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AnalyticsGenericLogFlow200ResponseLogsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AnalyticsGenericLogFlow200ResponseLogsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AnalyticsGenericLogFlow200ResponseLogsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AnalyticsGenericLogFlow200ResponseLogsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<AnalyticsGenericLogFlow200ResponseLogsInner>() {
           @Override
           public void write(JsonWriter out, AnalyticsGenericLogFlow200ResponseLogsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AnalyticsGenericLogFlow200ResponseLogsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AnalyticsGenericLogFlow200ResponseLogsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AnalyticsGenericLogFlow200ResponseLogsInner
   * @throws IOException if the JSON string is invalid with respect to AnalyticsGenericLogFlow200ResponseLogsInner
   */
  public static AnalyticsGenericLogFlow200ResponseLogsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AnalyticsGenericLogFlow200ResponseLogsInner.class);
  }

  /**
   * Convert an instance of AnalyticsGenericLogFlow200ResponseLogsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

