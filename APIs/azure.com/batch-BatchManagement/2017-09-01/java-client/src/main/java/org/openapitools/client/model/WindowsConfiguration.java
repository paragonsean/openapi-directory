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
 * WindowsConfiguration
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:48:39.479442-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WindowsConfiguration {
  public static final String SERIALIZED_NAME_ENABLE_AUTOMATIC_UPDATES = "enableAutomaticUpdates";
  @SerializedName(SERIALIZED_NAME_ENABLE_AUTOMATIC_UPDATES)
  private Boolean enableAutomaticUpdates;

  public WindowsConfiguration() {
  }

  public WindowsConfiguration enableAutomaticUpdates(Boolean enableAutomaticUpdates) {
    this.enableAutomaticUpdates = enableAutomaticUpdates;
    return this;
  }

  /**
   * If omitted, the default value is true.
   * @return enableAutomaticUpdates
   */
  @javax.annotation.Nullable
  public Boolean getEnableAutomaticUpdates() {
    return enableAutomaticUpdates;
  }

  public void setEnableAutomaticUpdates(Boolean enableAutomaticUpdates) {
    this.enableAutomaticUpdates = enableAutomaticUpdates;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WindowsConfiguration windowsConfiguration = (WindowsConfiguration) o;
    return Objects.equals(this.enableAutomaticUpdates, windowsConfiguration.enableAutomaticUpdates);
  }

  @Override
  public int hashCode() {
    return Objects.hash(enableAutomaticUpdates);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WindowsConfiguration {\n");
    sb.append("    enableAutomaticUpdates: ").append(toIndentedString(enableAutomaticUpdates)).append("\n");
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
    openapiFields.add("enableAutomaticUpdates");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WindowsConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WindowsConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WindowsConfiguration is not found in the empty JSON string", WindowsConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WindowsConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WindowsConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WindowsConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WindowsConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WindowsConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WindowsConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<WindowsConfiguration>() {
           @Override
           public void write(JsonWriter out, WindowsConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WindowsConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WindowsConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WindowsConfiguration
   * @throws IOException if the JSON string is invalid with respect to WindowsConfiguration
   */
  public static WindowsConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WindowsConfiguration.class);
  }

  /**
   * Convert an instance of WindowsConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

