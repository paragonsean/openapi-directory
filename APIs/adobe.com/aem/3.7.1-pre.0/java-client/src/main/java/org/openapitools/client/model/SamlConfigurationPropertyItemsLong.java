/*
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.7.1-pre.0
 * Contact: opensource@shinesolutions.com
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
 * SamlConfigurationPropertyItemsLong
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:15.153992-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SamlConfigurationPropertyItemsLong {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_IS_SET = "is_set";
  @SerializedName(SERIALIZED_NAME_IS_SET)
  private Boolean isSet;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OPTIONAL = "optional";
  @SerializedName(SERIALIZED_NAME_OPTIONAL)
  private Boolean optional;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private Integer type;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private Integer value;

  public SamlConfigurationPropertyItemsLong() {
  }

  public SamlConfigurationPropertyItemsLong description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Property description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public SamlConfigurationPropertyItemsLong isSet(Boolean isSet) {
    this.isSet = isSet;
    return this;
  }

  /**
   * True if property is set
   * @return isSet
   */
  @javax.annotation.Nullable
  public Boolean getIsSet() {
    return isSet;
  }

  public void setIsSet(Boolean isSet) {
    this.isSet = isSet;
  }


  public SamlConfigurationPropertyItemsLong name(String name) {
    this.name = name;
    return this;
  }

  /**
   * property name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public SamlConfigurationPropertyItemsLong optional(Boolean optional) {
    this.optional = optional;
    return this;
  }

  /**
   * True if optional
   * @return optional
   */
  @javax.annotation.Nullable
  public Boolean getOptional() {
    return optional;
  }

  public void setOptional(Boolean optional) {
    this.optional = optional;
  }


  public SamlConfigurationPropertyItemsLong type(Integer type) {
    this.type = type;
    return this;
  }

  /**
   * Property type, 1&#x3D;String, 3&#x3D;long, 11&#x3D;boolean, 12&#x3D;Password
   * @return type
   */
  @javax.annotation.Nullable
  public Integer getType() {
    return type;
  }

  public void setType(Integer type) {
    this.type = type;
  }


  public SamlConfigurationPropertyItemsLong value(Integer value) {
    this.value = value;
    return this;
  }

  /**
   * Property value
   * @return value
   */
  @javax.annotation.Nullable
  public Integer getValue() {
    return value;
  }

  public void setValue(Integer value) {
    this.value = value;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SamlConfigurationPropertyItemsLong samlConfigurationPropertyItemsLong = (SamlConfigurationPropertyItemsLong) o;
    return Objects.equals(this.description, samlConfigurationPropertyItemsLong.description) &&
        Objects.equals(this.isSet, samlConfigurationPropertyItemsLong.isSet) &&
        Objects.equals(this.name, samlConfigurationPropertyItemsLong.name) &&
        Objects.equals(this.optional, samlConfigurationPropertyItemsLong.optional) &&
        Objects.equals(this.type, samlConfigurationPropertyItemsLong.type) &&
        Objects.equals(this.value, samlConfigurationPropertyItemsLong.value);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, isSet, name, optional, type, value);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SamlConfigurationPropertyItemsLong {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    isSet: ").append(toIndentedString(isSet)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    optional: ").append(toIndentedString(optional)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
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
    openapiFields.add("is_set");
    openapiFields.add("name");
    openapiFields.add("optional");
    openapiFields.add("type");
    openapiFields.add("value");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SamlConfigurationPropertyItemsLong
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SamlConfigurationPropertyItemsLong.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SamlConfigurationPropertyItemsLong is not found in the empty JSON string", SamlConfigurationPropertyItemsLong.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SamlConfigurationPropertyItemsLong.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SamlConfigurationPropertyItemsLong` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SamlConfigurationPropertyItemsLong.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SamlConfigurationPropertyItemsLong' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SamlConfigurationPropertyItemsLong> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SamlConfigurationPropertyItemsLong.class));

       return (TypeAdapter<T>) new TypeAdapter<SamlConfigurationPropertyItemsLong>() {
           @Override
           public void write(JsonWriter out, SamlConfigurationPropertyItemsLong value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SamlConfigurationPropertyItemsLong read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SamlConfigurationPropertyItemsLong given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SamlConfigurationPropertyItemsLong
   * @throws IOException if the JSON string is invalid with respect to SamlConfigurationPropertyItemsLong
   */
  public static SamlConfigurationPropertyItemsLong fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SamlConfigurationPropertyItemsLong.class);
  }

  /**
   * Convert an instance of SamlConfigurationPropertyItemsLong to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

