/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-12-01-preview
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
import org.openapitools.client.model.NotificationRecipientUserListByNotification200ResponseValueInnerProperties;

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
 * Recipient User details.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:25.065524-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NotificationRecipientUserListByNotification200ResponseValueInner {
  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private NotificationRecipientUserListByNotification200ResponseValueInnerProperties properties;

  public NotificationRecipientUserListByNotification200ResponseValueInner() {
  }

  public NotificationRecipientUserListByNotification200ResponseValueInner properties(NotificationRecipientUserListByNotification200ResponseValueInnerProperties properties) {
    this.properties = properties;
    return this;
  }

  /**
   * Get properties
   * @return properties
   */
  @javax.annotation.Nullable
  public NotificationRecipientUserListByNotification200ResponseValueInnerProperties getProperties() {
    return properties;
  }

  public void setProperties(NotificationRecipientUserListByNotification200ResponseValueInnerProperties properties) {
    this.properties = properties;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NotificationRecipientUserListByNotification200ResponseValueInner notificationRecipientUserListByNotification200ResponseValueInner = (NotificationRecipientUserListByNotification200ResponseValueInner) o;
    return Objects.equals(this.properties, notificationRecipientUserListByNotification200ResponseValueInner.properties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(properties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NotificationRecipientUserListByNotification200ResponseValueInner {\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
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
    openapiFields.add("properties");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NotificationRecipientUserListByNotification200ResponseValueInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NotificationRecipientUserListByNotification200ResponseValueInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NotificationRecipientUserListByNotification200ResponseValueInner is not found in the empty JSON string", NotificationRecipientUserListByNotification200ResponseValueInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NotificationRecipientUserListByNotification200ResponseValueInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NotificationRecipientUserListByNotification200ResponseValueInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `properties`
      if (jsonObj.get("properties") != null && !jsonObj.get("properties").isJsonNull()) {
        NotificationRecipientUserListByNotification200ResponseValueInnerProperties.validateJsonElement(jsonObj.get("properties"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NotificationRecipientUserListByNotification200ResponseValueInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NotificationRecipientUserListByNotification200ResponseValueInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NotificationRecipientUserListByNotification200ResponseValueInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NotificationRecipientUserListByNotification200ResponseValueInner.class));

       return (TypeAdapter<T>) new TypeAdapter<NotificationRecipientUserListByNotification200ResponseValueInner>() {
           @Override
           public void write(JsonWriter out, NotificationRecipientUserListByNotification200ResponseValueInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NotificationRecipientUserListByNotification200ResponseValueInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NotificationRecipientUserListByNotification200ResponseValueInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NotificationRecipientUserListByNotification200ResponseValueInner
   * @throws IOException if the JSON string is invalid with respect to NotificationRecipientUserListByNotification200ResponseValueInner
   */
  public static NotificationRecipientUserListByNotification200ResponseValueInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NotificationRecipientUserListByNotification200ResponseValueInner.class);
  }

  /**
   * Convert an instance of NotificationRecipientUserListByNotification200ResponseValueInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

