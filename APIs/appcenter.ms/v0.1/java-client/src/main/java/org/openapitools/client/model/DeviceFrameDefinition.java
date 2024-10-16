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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * DeviceFrameDefinition
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeviceFrameDefinition {
  public static final String SERIALIZED_NAME_FRAME_URL = "frameUrl";
  @SerializedName(SERIALIZED_NAME_FRAME_URL)
  private String frameUrl;

  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private BigDecimal height;

  public static final String SERIALIZED_NAME_SCREEN = "screen";
  @SerializedName(SERIALIZED_NAME_SCREEN)
  private List<BigDecimal> screen = new ArrayList<>();

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private BigDecimal width;

  public DeviceFrameDefinition() {
  }

  public DeviceFrameDefinition frameUrl(String frameUrl) {
    this.frameUrl = frameUrl;
    return this;
  }

  /**
   * Get frameUrl
   * @return frameUrl
   */
  @javax.annotation.Nullable
  public String getFrameUrl() {
    return frameUrl;
  }

  public void setFrameUrl(String frameUrl) {
    this.frameUrl = frameUrl;
  }


  public DeviceFrameDefinition height(BigDecimal height) {
    this.height = height;
    return this;
  }

  /**
   * Get height
   * @return height
   */
  @javax.annotation.Nullable
  public BigDecimal getHeight() {
    return height;
  }

  public void setHeight(BigDecimal height) {
    this.height = height;
  }


  public DeviceFrameDefinition screen(List<BigDecimal> screen) {
    this.screen = screen;
    return this;
  }

  public DeviceFrameDefinition addScreenItem(BigDecimal screenItem) {
    if (this.screen == null) {
      this.screen = new ArrayList<>();
    }
    this.screen.add(screenItem);
    return this;
  }

  /**
   * Get screen
   * @return screen
   */
  @javax.annotation.Nullable
  public List<BigDecimal> getScreen() {
    return screen;
  }

  public void setScreen(List<BigDecimal> screen) {
    this.screen = screen;
  }


  public DeviceFrameDefinition width(BigDecimal width) {
    this.width = width;
    return this;
  }

  /**
   * Get width
   * @return width
   */
  @javax.annotation.Nullable
  public BigDecimal getWidth() {
    return width;
  }

  public void setWidth(BigDecimal width) {
    this.width = width;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeviceFrameDefinition deviceFrameDefinition = (DeviceFrameDefinition) o;
    return Objects.equals(this.frameUrl, deviceFrameDefinition.frameUrl) &&
        Objects.equals(this.height, deviceFrameDefinition.height) &&
        Objects.equals(this.screen, deviceFrameDefinition.screen) &&
        Objects.equals(this.width, deviceFrameDefinition.width);
  }

  @Override
  public int hashCode() {
    return Objects.hash(frameUrl, height, screen, width);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeviceFrameDefinition {\n");
    sb.append("    frameUrl: ").append(toIndentedString(frameUrl)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    screen: ").append(toIndentedString(screen)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
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
    openapiFields.add("frameUrl");
    openapiFields.add("height");
    openapiFields.add("screen");
    openapiFields.add("width");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeviceFrameDefinition
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeviceFrameDefinition.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeviceFrameDefinition is not found in the empty JSON string", DeviceFrameDefinition.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeviceFrameDefinition.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeviceFrameDefinition` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("frameUrl") != null && !jsonObj.get("frameUrl").isJsonNull()) && !jsonObj.get("frameUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `frameUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("frameUrl").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("screen") != null && !jsonObj.get("screen").isJsonNull() && !jsonObj.get("screen").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `screen` to be an array in the JSON string but got `%s`", jsonObj.get("screen").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeviceFrameDefinition.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeviceFrameDefinition' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeviceFrameDefinition> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeviceFrameDefinition.class));

       return (TypeAdapter<T>) new TypeAdapter<DeviceFrameDefinition>() {
           @Override
           public void write(JsonWriter out, DeviceFrameDefinition value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeviceFrameDefinition read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeviceFrameDefinition given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeviceFrameDefinition
   * @throws IOException if the JSON string is invalid with respect to DeviceFrameDefinition
   */
  public static DeviceFrameDefinition fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeviceFrameDefinition.class);
  }

  /**
   * Convert an instance of DeviceFrameDefinition to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

