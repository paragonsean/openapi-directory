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
 * Reading for the &#39;door&#39; metric. This will only be present if the &#39;metric&#39; property equals &#39;door&#39;.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationSensorReadingsHistory200ResponseInnerDoor {
  public static final String SERIALIZED_NAME_OPEN = "open";
  @SerializedName(SERIALIZED_NAME_OPEN)
  private Boolean open;

  public GetOrganizationSensorReadingsHistory200ResponseInnerDoor() {
  }

  public GetOrganizationSensorReadingsHistory200ResponseInnerDoor open(Boolean open) {
    this.open = open;
    return this;
  }

  /**
   * True if the door is open.
   * @return open
   */
  @javax.annotation.Nullable
  public Boolean getOpen() {
    return open;
  }

  public void setOpen(Boolean open) {
    this.open = open;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationSensorReadingsHistory200ResponseInnerDoor getOrganizationSensorReadingsHistory200ResponseInnerDoor = (GetOrganizationSensorReadingsHistory200ResponseInnerDoor) o;
    return Objects.equals(this.open, getOrganizationSensorReadingsHistory200ResponseInnerDoor.open);
  }

  @Override
  public int hashCode() {
    return Objects.hash(open);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationSensorReadingsHistory200ResponseInnerDoor {\n");
    sb.append("    open: ").append(toIndentedString(open)).append("\n");
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
    openapiFields.add("open");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationSensorReadingsHistory200ResponseInnerDoor
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationSensorReadingsHistory200ResponseInnerDoor.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationSensorReadingsHistory200ResponseInnerDoor is not found in the empty JSON string", GetOrganizationSensorReadingsHistory200ResponseInnerDoor.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationSensorReadingsHistory200ResponseInnerDoor.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationSensorReadingsHistory200ResponseInnerDoor` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationSensorReadingsHistory200ResponseInnerDoor.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationSensorReadingsHistory200ResponseInnerDoor' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationSensorReadingsHistory200ResponseInnerDoor> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationSensorReadingsHistory200ResponseInnerDoor.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationSensorReadingsHistory200ResponseInnerDoor>() {
           @Override
           public void write(JsonWriter out, GetOrganizationSensorReadingsHistory200ResponseInnerDoor value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationSensorReadingsHistory200ResponseInnerDoor read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationSensorReadingsHistory200ResponseInnerDoor given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationSensorReadingsHistory200ResponseInnerDoor
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationSensorReadingsHistory200ResponseInnerDoor
   */
  public static GetOrganizationSensorReadingsHistory200ResponseInnerDoor fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationSensorReadingsHistory200ResponseInnerDoor.class);
  }

  /**
   * Convert an instance of GetOrganizationSensorReadingsHistory200ResponseInnerDoor to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

