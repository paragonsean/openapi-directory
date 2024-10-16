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
 * PoE details object for the port
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe {
  public static final String SERIALIZED_NAME_STANDARD = "standard";
  @SerializedName(SERIALIZED_NAME_STANDARD)
  private String standard;

  public GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe() {
  }

  public GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe standard(String standard) {
    this.standard = standard;
    return this;
  }

  /**
   * The PoE Standard for the port. Can be &#39;802.3at&#39;, &#39;802.3af&#39;, &#39;802.3bt&#39;, or null
   * @return standard
   */
  @javax.annotation.Nullable
  public String getStandard() {
    return standard;
  }

  public void setStandard(String standard) {
    this.standard = standard;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe getOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe = (GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe) o;
    return Objects.equals(this.standard, getOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe.standard);
  }

  @Override
  public int hashCode() {
    return Objects.hash(standard);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe {\n");
    sb.append("    standard: ").append(toIndentedString(standard)).append("\n");
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
    openapiFields.add("standard");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe is not found in the empty JSON string", GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("standard") != null && !jsonObj.get("standard").isJsonNull()) && !jsonObj.get("standard").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `standard` to be a primitive type in the JSON string but got `%s`", jsonObj.get("standard").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe>() {
           @Override
           public void write(JsonWriter out, GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe
   */
  public static GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe.class);
  }

  /**
   * Convert an instance of GetOrganizationWirelessDevicesEthernetStatuses200ResponseInnerPortsInnerPoe to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

