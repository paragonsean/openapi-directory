/*
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
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
 * Parameters for an update application request.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:39.479442-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApplicationUpdateParameters {
  public static final String SERIALIZED_NAME_ALLOW_UPDATES = "allowUpdates";
  @SerializedName(SERIALIZED_NAME_ALLOW_UPDATES)
  private Boolean allowUpdates;

  public static final String SERIALIZED_NAME_DEFAULT_VERSION = "defaultVersion";
  @SerializedName(SERIALIZED_NAME_DEFAULT_VERSION)
  private String defaultVersion;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public ApplicationUpdateParameters() {
  }

  public ApplicationUpdateParameters allowUpdates(Boolean allowUpdates) {
    this.allowUpdates = allowUpdates;
    return this;
  }

  /**
   * A value indicating whether packages within the application may be overwritten using the same version string.
   * @return allowUpdates
   */
  @javax.annotation.Nullable
  public Boolean getAllowUpdates() {
    return allowUpdates;
  }

  public void setAllowUpdates(Boolean allowUpdates) {
    this.allowUpdates = allowUpdates;
  }


  public ApplicationUpdateParameters defaultVersion(String defaultVersion) {
    this.defaultVersion = defaultVersion;
    return this;
  }

  /**
   * The package to use if a client requests the application but does not specify a version.
   * @return defaultVersion
   */
  @javax.annotation.Nullable
  public String getDefaultVersion() {
    return defaultVersion;
  }

  public void setDefaultVersion(String defaultVersion) {
    this.defaultVersion = defaultVersion;
  }


  public ApplicationUpdateParameters displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * The display name for the application.
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApplicationUpdateParameters applicationUpdateParameters = (ApplicationUpdateParameters) o;
    return Objects.equals(this.allowUpdates, applicationUpdateParameters.allowUpdates) &&
        Objects.equals(this.defaultVersion, applicationUpdateParameters.defaultVersion) &&
        Objects.equals(this.displayName, applicationUpdateParameters.displayName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowUpdates, defaultVersion, displayName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApplicationUpdateParameters {\n");
    sb.append("    allowUpdates: ").append(toIndentedString(allowUpdates)).append("\n");
    sb.append("    defaultVersion: ").append(toIndentedString(defaultVersion)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
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
    openapiFields.add("allowUpdates");
    openapiFields.add("defaultVersion");
    openapiFields.add("displayName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApplicationUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApplicationUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApplicationUpdateParameters is not found in the empty JSON string", ApplicationUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApplicationUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApplicationUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("defaultVersion") != null && !jsonObj.get("defaultVersion").isJsonNull()) && !jsonObj.get("defaultVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `defaultVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("defaultVersion").toString()));
      }
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApplicationUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApplicationUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApplicationUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApplicationUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<ApplicationUpdateParameters>() {
           @Override
           public void write(JsonWriter out, ApplicationUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApplicationUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApplicationUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApplicationUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to ApplicationUpdateParameters
   */
  public static ApplicationUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApplicationUpdateParameters.class);
  }

  /**
   * Convert an instance of ApplicationUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

