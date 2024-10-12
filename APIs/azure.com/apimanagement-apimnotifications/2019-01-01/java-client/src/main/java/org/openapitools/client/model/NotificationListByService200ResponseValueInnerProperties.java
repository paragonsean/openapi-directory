/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
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
import org.openapitools.client.model.NotificationListByService200ResponseValueInnerPropertiesRecipients;

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
 * Notification Contract properties.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:29.856167-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NotificationListByService200ResponseValueInnerProperties {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_RECIPIENTS = "recipients";
  @SerializedName(SERIALIZED_NAME_RECIPIENTS)
  private NotificationListByService200ResponseValueInnerPropertiesRecipients recipients;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public NotificationListByService200ResponseValueInnerProperties() {
  }

  public NotificationListByService200ResponseValueInnerProperties description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description of the Notification.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public NotificationListByService200ResponseValueInnerProperties recipients(NotificationListByService200ResponseValueInnerPropertiesRecipients recipients) {
    this.recipients = recipients;
    return this;
  }

  /**
   * Get recipients
   * @return recipients
   */
  @javax.annotation.Nullable
  public NotificationListByService200ResponseValueInnerPropertiesRecipients getRecipients() {
    return recipients;
  }

  public void setRecipients(NotificationListByService200ResponseValueInnerPropertiesRecipients recipients) {
    this.recipients = recipients;
  }


  public NotificationListByService200ResponseValueInnerProperties title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Title of the Notification.
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NotificationListByService200ResponseValueInnerProperties notificationListByService200ResponseValueInnerProperties = (NotificationListByService200ResponseValueInnerProperties) o;
    return Objects.equals(this.description, notificationListByService200ResponseValueInnerProperties.description) &&
        Objects.equals(this.recipients, notificationListByService200ResponseValueInnerProperties.recipients) &&
        Objects.equals(this.title, notificationListByService200ResponseValueInnerProperties.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, recipients, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NotificationListByService200ResponseValueInnerProperties {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    recipients: ").append(toIndentedString(recipients)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("recipients");
    openapiFields.add("title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("title");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NotificationListByService200ResponseValueInnerProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NotificationListByService200ResponseValueInnerProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NotificationListByService200ResponseValueInnerProperties is not found in the empty JSON string", NotificationListByService200ResponseValueInnerProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NotificationListByService200ResponseValueInnerProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NotificationListByService200ResponseValueInnerProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : NotificationListByService200ResponseValueInnerProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      // validate the optional field `recipients`
      if (jsonObj.get("recipients") != null && !jsonObj.get("recipients").isJsonNull()) {
        NotificationListByService200ResponseValueInnerPropertiesRecipients.validateJsonElement(jsonObj.get("recipients"));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NotificationListByService200ResponseValueInnerProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NotificationListByService200ResponseValueInnerProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NotificationListByService200ResponseValueInnerProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NotificationListByService200ResponseValueInnerProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<NotificationListByService200ResponseValueInnerProperties>() {
           @Override
           public void write(JsonWriter out, NotificationListByService200ResponseValueInnerProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NotificationListByService200ResponseValueInnerProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NotificationListByService200ResponseValueInnerProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NotificationListByService200ResponseValueInnerProperties
   * @throws IOException if the JSON string is invalid with respect to NotificationListByService200ResponseValueInnerProperties
   */
  public static NotificationListByService200ResponseValueInnerProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NotificationListByService200ResponseValueInnerProperties.class);
  }

  /**
   * Convert an instance of NotificationListByService200ResponseValueInnerProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

