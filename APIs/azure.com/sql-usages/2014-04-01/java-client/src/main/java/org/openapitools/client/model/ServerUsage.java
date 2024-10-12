/*
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including servers, databases, elastic pools, recommendations, operations, and usage metrics.
 *
 * The version of the OpenAPI document: 2014-04-01
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
import java.time.OffsetDateTime;
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
 * Represents server metrics.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:46.154261-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerUsage {
  public static final String SERIALIZED_NAME_CURRENT_VALUE = "currentValue";
  @SerializedName(SERIALIZED_NAME_CURRENT_VALUE)
  private Double currentValue;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_LIMIT = "limit";
  @SerializedName(SERIALIZED_NAME_LIMIT)
  private Double limit;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NEXT_RESET_TIME = "nextResetTime";
  @SerializedName(SERIALIZED_NAME_NEXT_RESET_TIME)
  private OffsetDateTime nextResetTime;

  public static final String SERIALIZED_NAME_RESOURCE_NAME = "resourceName";
  @SerializedName(SERIALIZED_NAME_RESOURCE_NAME)
  private String resourceName;

  public static final String SERIALIZED_NAME_UNIT = "unit";
  @SerializedName(SERIALIZED_NAME_UNIT)
  private String unit;

  public ServerUsage() {
  }

  public ServerUsage(
     Double currentValue, 
     String displayName, 
     Double limit, 
     String name, 
     OffsetDateTime nextResetTime, 
     String resourceName, 
     String unit
  ) {
    this();
    this.currentValue = currentValue;
    this.displayName = displayName;
    this.limit = limit;
    this.name = name;
    this.nextResetTime = nextResetTime;
    this.resourceName = resourceName;
    this.unit = unit;
  }

  /**
   * The current value of the metric.
   * @return currentValue
   */
  @javax.annotation.Nullable
  public Double getCurrentValue() {
    return currentValue;
  }



  /**
   * The metric display name.
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }



  /**
   * The current limit of the metric.
   * @return limit
   */
  @javax.annotation.Nullable
  public Double getLimit() {
    return limit;
  }



  /**
   * Name of the server usage metric.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }



  /**
   * The next reset time for the metric (ISO8601 format).
   * @return nextResetTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getNextResetTime() {
    return nextResetTime;
  }



  /**
   * The name of the resource.
   * @return resourceName
   */
  @javax.annotation.Nullable
  public String getResourceName() {
    return resourceName;
  }



  /**
   * The units of the metric.
   * @return unit
   */
  @javax.annotation.Nullable
  public String getUnit() {
    return unit;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerUsage serverUsage = (ServerUsage) o;
    return Objects.equals(this.currentValue, serverUsage.currentValue) &&
        Objects.equals(this.displayName, serverUsage.displayName) &&
        Objects.equals(this.limit, serverUsage.limit) &&
        Objects.equals(this.name, serverUsage.name) &&
        Objects.equals(this.nextResetTime, serverUsage.nextResetTime) &&
        Objects.equals(this.resourceName, serverUsage.resourceName) &&
        Objects.equals(this.unit, serverUsage.unit);
  }

  @Override
  public int hashCode() {
    return Objects.hash(currentValue, displayName, limit, name, nextResetTime, resourceName, unit);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerUsage {\n");
    sb.append("    currentValue: ").append(toIndentedString(currentValue)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    limit: ").append(toIndentedString(limit)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nextResetTime: ").append(toIndentedString(nextResetTime)).append("\n");
    sb.append("    resourceName: ").append(toIndentedString(resourceName)).append("\n");
    sb.append("    unit: ").append(toIndentedString(unit)).append("\n");
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
    openapiFields.add("currentValue");
    openapiFields.add("displayName");
    openapiFields.add("limit");
    openapiFields.add("name");
    openapiFields.add("nextResetTime");
    openapiFields.add("resourceName");
    openapiFields.add("unit");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerUsage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerUsage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerUsage is not found in the empty JSON string", ServerUsage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerUsage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerUsage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("resourceName") != null && !jsonObj.get("resourceName").isJsonNull()) && !jsonObj.get("resourceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceName").toString()));
      }
      if ((jsonObj.get("unit") != null && !jsonObj.get("unit").isJsonNull()) && !jsonObj.get("unit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unit").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerUsage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerUsage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerUsage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerUsage.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerUsage>() {
           @Override
           public void write(JsonWriter out, ServerUsage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerUsage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerUsage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerUsage
   * @throws IOException if the JSON string is invalid with respect to ServerUsage
   */
  public static ServerUsage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerUsage.class);
  }

  /**
   * Convert an instance of ServerUsage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

