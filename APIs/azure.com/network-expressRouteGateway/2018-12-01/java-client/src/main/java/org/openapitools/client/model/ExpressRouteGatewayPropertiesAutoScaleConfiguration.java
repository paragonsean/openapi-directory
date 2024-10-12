/*
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-12-01
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
import org.openapitools.client.model.ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds;

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
 * Configuration for auto scaling.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:34.548657-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExpressRouteGatewayPropertiesAutoScaleConfiguration {
  public static final String SERIALIZED_NAME_BOUNDS = "bounds";
  @SerializedName(SERIALIZED_NAME_BOUNDS)
  private ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds bounds;

  public ExpressRouteGatewayPropertiesAutoScaleConfiguration() {
  }

  public ExpressRouteGatewayPropertiesAutoScaleConfiguration bounds(ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds bounds) {
    this.bounds = bounds;
    return this;
  }

  /**
   * Get bounds
   * @return bounds
   */
  @javax.annotation.Nullable
  public ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds getBounds() {
    return bounds;
  }

  public void setBounds(ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds bounds) {
    this.bounds = bounds;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExpressRouteGatewayPropertiesAutoScaleConfiguration expressRouteGatewayPropertiesAutoScaleConfiguration = (ExpressRouteGatewayPropertiesAutoScaleConfiguration) o;
    return Objects.equals(this.bounds, expressRouteGatewayPropertiesAutoScaleConfiguration.bounds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bounds);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExpressRouteGatewayPropertiesAutoScaleConfiguration {\n");
    sb.append("    bounds: ").append(toIndentedString(bounds)).append("\n");
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
    openapiFields.add("bounds");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExpressRouteGatewayPropertiesAutoScaleConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExpressRouteGatewayPropertiesAutoScaleConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExpressRouteGatewayPropertiesAutoScaleConfiguration is not found in the empty JSON string", ExpressRouteGatewayPropertiesAutoScaleConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExpressRouteGatewayPropertiesAutoScaleConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExpressRouteGatewayPropertiesAutoScaleConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `bounds`
      if (jsonObj.get("bounds") != null && !jsonObj.get("bounds").isJsonNull()) {
        ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.validateJsonElement(jsonObj.get("bounds"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExpressRouteGatewayPropertiesAutoScaleConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExpressRouteGatewayPropertiesAutoScaleConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExpressRouteGatewayPropertiesAutoScaleConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExpressRouteGatewayPropertiesAutoScaleConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<ExpressRouteGatewayPropertiesAutoScaleConfiguration>() {
           @Override
           public void write(JsonWriter out, ExpressRouteGatewayPropertiesAutoScaleConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExpressRouteGatewayPropertiesAutoScaleConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExpressRouteGatewayPropertiesAutoScaleConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExpressRouteGatewayPropertiesAutoScaleConfiguration
   * @throws IOException if the JSON string is invalid with respect to ExpressRouteGatewayPropertiesAutoScaleConfiguration
   */
  public static ExpressRouteGatewayPropertiesAutoScaleConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExpressRouteGatewayPropertiesAutoScaleConfiguration.class);
  }

  /**
   * Convert an instance of ExpressRouteGatewayPropertiesAutoScaleConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

