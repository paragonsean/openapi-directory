/*
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
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
 * EntityResponseVersion
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:53.720541-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EntityResponseVersion {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NORMALIZED = "normalized";
  @SerializedName(SERIALIZED_NAME_NORMALIZED)
  private String normalized;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public EntityResponseVersion() {
  }

  public EntityResponseVersion id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Unique user entity identifier
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public EntityResponseVersion label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Descriptive label for the entity, e.g. Wikipedia URL
   * @return label
   */
  @javax.annotation.Nonnull
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public EntityResponseVersion modified(String modified) {
    this.modified = modified;
    return this;
  }

  /**
   * The timestamp of the latest update of the record. Creation date of update didn&#39;t occur
   * @return modified
   */
  @javax.annotation.Nonnull
  public String getModified() {
    return modified;
  }

  public void setModified(String modified) {
    this.modified = modified;
  }


  public EntityResponseVersion name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Entity name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public EntityResponseVersion normalized(String normalized) {
    this.normalized = normalized;
    return this;
  }

  /**
   * Normalized form of the entity. Will replace entity name in the output
   * @return normalized
   */
  @javax.annotation.Nonnull
  public String getNormalized() {
    return normalized;
  }

  public void setNormalized(String normalized) {
    this.normalized = normalized;
  }


  public EntityResponseVersion type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Type of the entity (Company, Person, any custom type)
   * @return type
   */
  @javax.annotation.Nonnull
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
    EntityResponseVersion entityResponseVersion = (EntityResponseVersion) o;
    return Objects.equals(this.id, entityResponseVersion.id) &&
        Objects.equals(this.label, entityResponseVersion.label) &&
        Objects.equals(this.modified, entityResponseVersion.modified) &&
        Objects.equals(this.name, entityResponseVersion.name) &&
        Objects.equals(this.normalized, entityResponseVersion.normalized) &&
        Objects.equals(this.type, entityResponseVersion.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, label, modified, name, normalized, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EntityResponseVersion {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    normalized: ").append(toIndentedString(normalized)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("label");
    openapiFields.add("modified");
    openapiFields.add("name");
    openapiFields.add("normalized");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("label");
    openapiRequiredFields.add("modified");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("normalized");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EntityResponseVersion
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EntityResponseVersion.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EntityResponseVersion is not found in the empty JSON string", EntityResponseVersion.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EntityResponseVersion.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EntityResponseVersion` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EntityResponseVersion.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      if (!jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (!jsonObj.get("normalized").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `normalized` to be a primitive type in the JSON string but got `%s`", jsonObj.get("normalized").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EntityResponseVersion.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EntityResponseVersion' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EntityResponseVersion> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EntityResponseVersion.class));

       return (TypeAdapter<T>) new TypeAdapter<EntityResponseVersion>() {
           @Override
           public void write(JsonWriter out, EntityResponseVersion value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EntityResponseVersion read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EntityResponseVersion given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EntityResponseVersion
   * @throws IOException if the JSON string is invalid with respect to EntityResponseVersion
   */
  public static EntityResponseVersion fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EntityResponseVersion.class);
  }

  /**
   * Convert an instance of EntityResponseVersion to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

