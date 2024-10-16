/*
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
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
import org.openapitools.client.model.NotificationAttributes;
import org.openapitools.client.model.NotificationRelationships;

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
 * Object containing notification properties.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:39.505408-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Notification {
  public static final String SERIALIZED_NAME_ATTRIBUTES = "attributes";
  @SerializedName(SERIALIZED_NAME_ATTRIBUTES)
  private NotificationAttributes attributes;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_RELATIONSHIPS = "relationships";
  @SerializedName(SERIALIZED_NAME_RELATIONSHIPS)
  private NotificationRelationships relationships;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Notification() {
  }

  public Notification attributes(NotificationAttributes attributes) {
    this.attributes = attributes;
    return this;
  }

  /**
   * Get attributes
   * @return attributes
   */
  @javax.annotation.Nullable
  public NotificationAttributes getAttributes() {
    return attributes;
  }

  public void setAttributes(NotificationAttributes attributes) {
    this.attributes = attributes;
  }


  public Notification id(Integer id) {
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


  public Notification relationships(NotificationRelationships relationships) {
    this.relationships = relationships;
    return this;
  }

  /**
   * Get relationships
   * @return relationships
   */
  @javax.annotation.Nullable
  public NotificationRelationships getRelationships() {
    return relationships;
  }

  public void setRelationships(NotificationRelationships relationships) {
    this.relationships = relationships;
  }


  public Notification type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
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
    Notification notification = (Notification) o;
    return Objects.equals(this.attributes, notification.attributes) &&
        Objects.equals(this.id, notification.id) &&
        Objects.equals(this.relationships, notification.relationships) &&
        Objects.equals(this.type, notification.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(attributes, id, relationships, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Notification {\n");
    sb.append("    attributes: ").append(toIndentedString(attributes)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    relationships: ").append(toIndentedString(relationships)).append("\n");
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
    openapiFields.add("attributes");
    openapiFields.add("id");
    openapiFields.add("relationships");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Notification
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Notification.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Notification is not found in the empty JSON string", Notification.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Notification.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Notification` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `attributes`
      if (jsonObj.get("attributes") != null && !jsonObj.get("attributes").isJsonNull()) {
        NotificationAttributes.validateJsonElement(jsonObj.get("attributes"));
      }
      // validate the optional field `relationships`
      if (jsonObj.get("relationships") != null && !jsonObj.get("relationships").isJsonNull()) {
        NotificationRelationships.validateJsonElement(jsonObj.get("relationships"));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Notification.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Notification' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Notification> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Notification.class));

       return (TypeAdapter<T>) new TypeAdapter<Notification>() {
           @Override
           public void write(JsonWriter out, Notification value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Notification read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Notification given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Notification
   * @throws IOException if the JSON string is invalid with respect to Notification
   */
  public static Notification fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Notification.class);
  }

  /**
   * Convert an instance of Notification to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

