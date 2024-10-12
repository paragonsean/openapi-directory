/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
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
import org.openapitools.client.model.AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties;

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
 * Virtual Network route contract used to pass routing information for a Virtual Network.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:54.768221-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansCreateOrUpdateVnetRouteRequest {
  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties properties;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_KIND = "kind";
  @SerializedName(SERIALIZED_NAME_KIND)
  private String kind;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public AppServicePlansCreateOrUpdateVnetRouteRequest() {
  }

  public AppServicePlansCreateOrUpdateVnetRouteRequest(
     String id, 
     String name, 
     String type
  ) {
    this();
    this.id = id;
    this.name = name;
    this.type = type;
  }

  public AppServicePlansCreateOrUpdateVnetRouteRequest properties(AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties properties) {
    this.properties = properties;
    return this;
  }

  /**
   * Get properties
   * @return properties
   */
  @javax.annotation.Nullable
  public AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties getProperties() {
    return properties;
  }

  public void setProperties(AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties properties) {
    this.properties = properties;
  }


  /**
   * Resource Id.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public AppServicePlansCreateOrUpdateVnetRouteRequest kind(String kind) {
    this.kind = kind;
    return this;
  }

  /**
   * Kind of resource.
   * @return kind
   */
  @javax.annotation.Nullable
  public String getKind() {
    return kind;
  }

  public void setKind(String kind) {
    this.kind = kind;
  }


  /**
   * Resource Name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }



  /**
   * Resource type.
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansCreateOrUpdateVnetRouteRequest appServicePlansCreateOrUpdateVnetRouteRequest = (AppServicePlansCreateOrUpdateVnetRouteRequest) o;
    return Objects.equals(this.properties, appServicePlansCreateOrUpdateVnetRouteRequest.properties) &&
        Objects.equals(this.id, appServicePlansCreateOrUpdateVnetRouteRequest.id) &&
        Objects.equals(this.kind, appServicePlansCreateOrUpdateVnetRouteRequest.kind) &&
        Objects.equals(this.name, appServicePlansCreateOrUpdateVnetRouteRequest.name) &&
        Objects.equals(this.type, appServicePlansCreateOrUpdateVnetRouteRequest.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(properties, id, kind, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansCreateOrUpdateVnetRouteRequest {\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("kind");
    openapiFields.add("name");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansCreateOrUpdateVnetRouteRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansCreateOrUpdateVnetRouteRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansCreateOrUpdateVnetRouteRequest is not found in the empty JSON string", AppServicePlansCreateOrUpdateVnetRouteRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansCreateOrUpdateVnetRouteRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansCreateOrUpdateVnetRouteRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `properties`
      if (jsonObj.get("properties") != null && !jsonObj.get("properties").isJsonNull()) {
        AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties.validateJsonElement(jsonObj.get("properties"));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("kind") != null && !jsonObj.get("kind").isJsonNull()) && !jsonObj.get("kind").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `kind` to be a primitive type in the JSON string but got `%s`", jsonObj.get("kind").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansCreateOrUpdateVnetRouteRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansCreateOrUpdateVnetRouteRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansCreateOrUpdateVnetRouteRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansCreateOrUpdateVnetRouteRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansCreateOrUpdateVnetRouteRequest>() {
           @Override
           public void write(JsonWriter out, AppServicePlansCreateOrUpdateVnetRouteRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansCreateOrUpdateVnetRouteRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansCreateOrUpdateVnetRouteRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansCreateOrUpdateVnetRouteRequest
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansCreateOrUpdateVnetRouteRequest
   */
  public static AppServicePlansCreateOrUpdateVnetRouteRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansCreateOrUpdateVnetRouteRequest.class);
  }

  /**
   * Convert an instance of AppServicePlansCreateOrUpdateVnetRouteRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

