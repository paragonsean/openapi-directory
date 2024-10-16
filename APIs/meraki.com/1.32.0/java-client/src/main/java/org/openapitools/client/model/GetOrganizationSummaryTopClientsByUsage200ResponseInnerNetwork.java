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
 * 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork() {
  }

  public GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork id(String id) {
    this.id = id;
    return this;
  }

  /**
   * ID of network
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of network
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork getOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork = (GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork) o;
    return Objects.equals(this.id, getOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.id) &&
        Objects.equals(this.name, getOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, name);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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
    openapiFields.add("name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork is not found in the empty JSON string", GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork>() {
           @Override
           public void write(JsonWriter out, GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork
   */
  public static GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork.class);
  }

  /**
   * Convert an instance of GetOrganizationSummaryTopClientsByUsage200ResponseInnerNetwork to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

