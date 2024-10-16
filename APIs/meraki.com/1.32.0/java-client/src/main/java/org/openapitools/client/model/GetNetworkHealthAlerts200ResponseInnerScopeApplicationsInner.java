/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner {
  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner() {
  }

  public GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the application
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner url(String url) {
    this.url = url;
    return this;
  }

  /**
   * URL to the application
   * @return url
   */
  @javax.annotation.Nullable
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner getNetworkHealthAlerts200ResponseInnerScopeApplicationsInner = (GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner) o;
    return Objects.equals(this.name, getNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.name) &&
        Objects.equals(this.url, getNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner {\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("name");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner is not found in the empty JSON string", GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) && !jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner>() {
           @Override
           public void write(JsonWriter out, GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner
   * @throws IOException if the JSON string is invalid with respect to GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner
   */
  public static GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner.class);
  }

  /**
   * Convert an instance of GetNetworkHealthAlerts200ResponseInnerScopeApplicationsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

