/*
 *  API Client
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
 * Identifier resource specific properties
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:47.141391-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties() {
  }

  public ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties id(String id) {
    this.id = id;
    return this;
  }

  /**
   * String representation of the identity.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties listSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties = (ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties) o;
    return Objects.equals(this.id, listSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.id);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
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

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties is not found in the empty JSON string", ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties>() {
           @Override
           public void write(JsonWriter out, ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties
   * @throws IOException if the JSON string is invalid with respect to ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties
   */
  public static ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.class);
  }

  /**
   * Convert an instance of ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

