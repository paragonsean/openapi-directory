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
 * CPU data for device
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeviceCpu {
  public static final String SERIALIZED_NAME_CORE = "core";
  @SerializedName(SERIALIZED_NAME_CORE)
  private String core;

  public static final String SERIALIZED_NAME_FREQUENCY = "frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private String frequency;

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private String text;

  public DeviceCpu() {
  }

  public DeviceCpu core(String core) {
    this.core = core;
    return this;
  }

  /**
   * Get core
   * @return core
   */
  @javax.annotation.Nullable
  public String getCore() {
    return core;
  }

  public void setCore(String core) {
    this.core = core;
  }


  public DeviceCpu frequency(String frequency) {
    this.frequency = frequency;
    return this;
  }

  /**
   * Get frequency
   * @return frequency
   */
  @javax.annotation.Nullable
  public String getFrequency() {
    return frequency;
  }

  public void setFrequency(String frequency) {
    this.frequency = frequency;
  }


  public DeviceCpu text(String text) {
    this.text = text;
    return this;
  }

  /**
   * Get text
   * @return text
   */
  @javax.annotation.Nullable
  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeviceCpu deviceCpu = (DeviceCpu) o;
    return Objects.equals(this.core, deviceCpu.core) &&
        Objects.equals(this.frequency, deviceCpu.frequency) &&
        Objects.equals(this.text, deviceCpu.text);
  }

  @Override
  public int hashCode() {
    return Objects.hash(core, frequency, text);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeviceCpu {\n");
    sb.append("    core: ").append(toIndentedString(core)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
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
    openapiFields.add("core");
    openapiFields.add("frequency");
    openapiFields.add("text");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeviceCpu
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeviceCpu.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeviceCpu is not found in the empty JSON string", DeviceCpu.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeviceCpu.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeviceCpu` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("core") != null && !jsonObj.get("core").isJsonNull()) && !jsonObj.get("core").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `core` to be a primitive type in the JSON string but got `%s`", jsonObj.get("core").toString()));
      }
      if ((jsonObj.get("frequency") != null && !jsonObj.get("frequency").isJsonNull()) && !jsonObj.get("frequency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `frequency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("frequency").toString()));
      }
      if ((jsonObj.get("text") != null && !jsonObj.get("text").isJsonNull()) && !jsonObj.get("text").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `text` to be a primitive type in the JSON string but got `%s`", jsonObj.get("text").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeviceCpu.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeviceCpu' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeviceCpu> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeviceCpu.class));

       return (TypeAdapter<T>) new TypeAdapter<DeviceCpu>() {
           @Override
           public void write(JsonWriter out, DeviceCpu value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeviceCpu read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeviceCpu given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeviceCpu
   * @throws IOException if the JSON string is invalid with respect to DeviceCpu
   */
  public static DeviceCpu fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeviceCpu.class);
  }

  /**
   * Convert an instance of DeviceCpu to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

