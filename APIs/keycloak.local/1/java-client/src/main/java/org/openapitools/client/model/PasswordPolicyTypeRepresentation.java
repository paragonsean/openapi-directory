/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
 * PasswordPolicyTypeRepresentation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PasswordPolicyTypeRepresentation {
  public static final String SERIALIZED_NAME_CONFIG_TYPE = "configType";
  @SerializedName(SERIALIZED_NAME_CONFIG_TYPE)
  private String configType;

  public static final String SERIALIZED_NAME_DEFAULT_VALUE = "defaultValue";
  @SerializedName(SERIALIZED_NAME_DEFAULT_VALUE)
  private String defaultValue;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MULTIPLE_SUPPORTED = "multipleSupported";
  @SerializedName(SERIALIZED_NAME_MULTIPLE_SUPPORTED)
  private Boolean multipleSupported;

  public PasswordPolicyTypeRepresentation() {
  }

  public PasswordPolicyTypeRepresentation configType(String configType) {
    this.configType = configType;
    return this;
  }

  /**
   * Get configType
   * @return configType
   */
  @javax.annotation.Nullable
  public String getConfigType() {
    return configType;
  }

  public void setConfigType(String configType) {
    this.configType = configType;
  }


  public PasswordPolicyTypeRepresentation defaultValue(String defaultValue) {
    this.defaultValue = defaultValue;
    return this;
  }

  /**
   * Get defaultValue
   * @return defaultValue
   */
  @javax.annotation.Nullable
  public String getDefaultValue() {
    return defaultValue;
  }

  public void setDefaultValue(String defaultValue) {
    this.defaultValue = defaultValue;
  }


  public PasswordPolicyTypeRepresentation displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * Get displayName
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public PasswordPolicyTypeRepresentation id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public PasswordPolicyTypeRepresentation multipleSupported(Boolean multipleSupported) {
    this.multipleSupported = multipleSupported;
    return this;
  }

  /**
   * Get multipleSupported
   * @return multipleSupported
   */
  @javax.annotation.Nullable
  public Boolean getMultipleSupported() {
    return multipleSupported;
  }

  public void setMultipleSupported(Boolean multipleSupported) {
    this.multipleSupported = multipleSupported;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PasswordPolicyTypeRepresentation passwordPolicyTypeRepresentation = (PasswordPolicyTypeRepresentation) o;
    return Objects.equals(this.configType, passwordPolicyTypeRepresentation.configType) &&
        Objects.equals(this.defaultValue, passwordPolicyTypeRepresentation.defaultValue) &&
        Objects.equals(this.displayName, passwordPolicyTypeRepresentation.displayName) &&
        Objects.equals(this.id, passwordPolicyTypeRepresentation.id) &&
        Objects.equals(this.multipleSupported, passwordPolicyTypeRepresentation.multipleSupported);
  }

  @Override
  public int hashCode() {
    return Objects.hash(configType, defaultValue, displayName, id, multipleSupported);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PasswordPolicyTypeRepresentation {\n");
    sb.append("    configType: ").append(toIndentedString(configType)).append("\n");
    sb.append("    defaultValue: ").append(toIndentedString(defaultValue)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    multipleSupported: ").append(toIndentedString(multipleSupported)).append("\n");
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
    openapiFields.add("configType");
    openapiFields.add("defaultValue");
    openapiFields.add("displayName");
    openapiFields.add("id");
    openapiFields.add("multipleSupported");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PasswordPolicyTypeRepresentation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PasswordPolicyTypeRepresentation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PasswordPolicyTypeRepresentation is not found in the empty JSON string", PasswordPolicyTypeRepresentation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PasswordPolicyTypeRepresentation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PasswordPolicyTypeRepresentation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("configType") != null && !jsonObj.get("configType").isJsonNull()) && !jsonObj.get("configType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `configType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("configType").toString()));
      }
      if ((jsonObj.get("defaultValue") != null && !jsonObj.get("defaultValue").isJsonNull()) && !jsonObj.get("defaultValue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `defaultValue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("defaultValue").toString()));
      }
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PasswordPolicyTypeRepresentation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PasswordPolicyTypeRepresentation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PasswordPolicyTypeRepresentation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PasswordPolicyTypeRepresentation.class));

       return (TypeAdapter<T>) new TypeAdapter<PasswordPolicyTypeRepresentation>() {
           @Override
           public void write(JsonWriter out, PasswordPolicyTypeRepresentation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PasswordPolicyTypeRepresentation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PasswordPolicyTypeRepresentation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PasswordPolicyTypeRepresentation
   * @throws IOException if the JSON string is invalid with respect to PasswordPolicyTypeRepresentation
   */
  public static PasswordPolicyTypeRepresentation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PasswordPolicyTypeRepresentation.class);
  }

  /**
   * Convert an instance of PasswordPolicyTypeRepresentation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

