/*
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
import org.openapitools.client.model.ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties;

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
 * A domain specific resource identifier.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:50.427441-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ListSiteIdentifiersAssignedToHostName200ResponseValueInner {
  public static final String SERIALIZED_NAME_PROPERTIES = "properties";
  @SerializedName(SERIALIZED_NAME_PROPERTIES)
  private ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties properties;

  public ListSiteIdentifiersAssignedToHostName200ResponseValueInner() {
  }

  public ListSiteIdentifiersAssignedToHostName200ResponseValueInner properties(ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties properties) {
    this.properties = properties;
    return this;
  }

  /**
   * Get properties
   * @return properties
   */
  @javax.annotation.Nullable
  public ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties getProperties() {
    return properties;
  }

  public void setProperties(ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties properties) {
    this.properties = properties;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ListSiteIdentifiersAssignedToHostName200ResponseValueInner listSiteIdentifiersAssignedToHostName200ResponseValueInner = (ListSiteIdentifiersAssignedToHostName200ResponseValueInner) o;
    return Objects.equals(this.properties, listSiteIdentifiersAssignedToHostName200ResponseValueInner.properties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(properties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListSiteIdentifiersAssignedToHostName200ResponseValueInner {\n");
    sb.append("    properties: ").append(toIndentedString(properties)).append("\n");
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
    openapiFields.add("properties");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ListSiteIdentifiersAssignedToHostName200ResponseValueInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ListSiteIdentifiersAssignedToHostName200ResponseValueInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ListSiteIdentifiersAssignedToHostName200ResponseValueInner is not found in the empty JSON string", ListSiteIdentifiersAssignedToHostName200ResponseValueInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ListSiteIdentifiersAssignedToHostName200ResponseValueInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ListSiteIdentifiersAssignedToHostName200ResponseValueInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `properties`
      if (jsonObj.get("properties") != null && !jsonObj.get("properties").isJsonNull()) {
        ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.validateJsonElement(jsonObj.get("properties"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ListSiteIdentifiersAssignedToHostName200ResponseValueInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ListSiteIdentifiersAssignedToHostName200ResponseValueInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ListSiteIdentifiersAssignedToHostName200ResponseValueInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ListSiteIdentifiersAssignedToHostName200ResponseValueInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ListSiteIdentifiersAssignedToHostName200ResponseValueInner>() {
           @Override
           public void write(JsonWriter out, ListSiteIdentifiersAssignedToHostName200ResponseValueInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ListSiteIdentifiersAssignedToHostName200ResponseValueInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ListSiteIdentifiersAssignedToHostName200ResponseValueInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ListSiteIdentifiersAssignedToHostName200ResponseValueInner
   * @throws IOException if the JSON string is invalid with respect to ListSiteIdentifiersAssignedToHostName200ResponseValueInner
   */
  public static ListSiteIdentifiersAssignedToHostName200ResponseValueInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ListSiteIdentifiersAssignedToHostName200ResponseValueInner.class);
  }

  /**
   * Convert an instance of ListSiteIdentifiersAssignedToHostName200ResponseValueInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

