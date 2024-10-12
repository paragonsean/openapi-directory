/*
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-11-01
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
 * Minimum and maximum number of scale units to deploy.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:38.898650-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds {
  public static final String SERIALIZED_NAME_MAX = "max";
  @SerializedName(SERIALIZED_NAME_MAX)
  private Integer max;

  public static final String SERIALIZED_NAME_MIN = "min";
  @SerializedName(SERIALIZED_NAME_MIN)
  private Integer min;

  public ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds() {
  }

  public ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds max(Integer max) {
    this.max = max;
    return this;
  }

  /**
   * Maximum number of scale units deployed for ExpressRoute gateway.
   * @return max
   */
  @javax.annotation.Nullable
  public Integer getMax() {
    return max;
  }

  public void setMax(Integer max) {
    this.max = max;
  }


  public ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds min(Integer min) {
    this.min = min;
    return this;
  }

  /**
   * Minimum number of scale units deployed for ExpressRoute gateway.
   * @return min
   */
  @javax.annotation.Nullable
  public Integer getMin() {
    return min;
  }

  public void setMin(Integer min) {
    this.min = min;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds expressRouteGatewayPropertiesAutoScaleConfigurationBounds = (ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds) o;
    return Objects.equals(this.max, expressRouteGatewayPropertiesAutoScaleConfigurationBounds.max) &&
        Objects.equals(this.min, expressRouteGatewayPropertiesAutoScaleConfigurationBounds.min);
  }

  @Override
  public int hashCode() {
    return Objects.hash(max, min);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds {\n");
    sb.append("    max: ").append(toIndentedString(max)).append("\n");
    sb.append("    min: ").append(toIndentedString(min)).append("\n");
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
    openapiFields.add("max");
    openapiFields.add("min");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds is not found in the empty JSON string", ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.class));

       return (TypeAdapter<T>) new TypeAdapter<ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds>() {
           @Override
           public void write(JsonWriter out, ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds
   * @throws IOException if the JSON string is invalid with respect to ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds
   */
  public static ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.class);
  }

  /**
   * Convert an instance of ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

