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
import org.openapitools.client.model.GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys;

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
 * Details for indicating whether organization will restrict access to API (but not Dashboard) to certain IP addresses.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationLoginSecurity200ResponseApiAuthentication {
  public static final String SERIALIZED_NAME_IP_RESTRICTIONS_FOR_KEYS = "ipRestrictionsForKeys";
  @SerializedName(SERIALIZED_NAME_IP_RESTRICTIONS_FOR_KEYS)
  private GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys ipRestrictionsForKeys;

  public GetOrganizationLoginSecurity200ResponseApiAuthentication() {
  }

  public GetOrganizationLoginSecurity200ResponseApiAuthentication ipRestrictionsForKeys(GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys ipRestrictionsForKeys) {
    this.ipRestrictionsForKeys = ipRestrictionsForKeys;
    return this;
  }

  /**
   * Get ipRestrictionsForKeys
   * @return ipRestrictionsForKeys
   */
  @javax.annotation.Nullable
  public GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys getIpRestrictionsForKeys() {
    return ipRestrictionsForKeys;
  }

  public void setIpRestrictionsForKeys(GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys ipRestrictionsForKeys) {
    this.ipRestrictionsForKeys = ipRestrictionsForKeys;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationLoginSecurity200ResponseApiAuthentication getOrganizationLoginSecurity200ResponseApiAuthentication = (GetOrganizationLoginSecurity200ResponseApiAuthentication) o;
    return Objects.equals(this.ipRestrictionsForKeys, getOrganizationLoginSecurity200ResponseApiAuthentication.ipRestrictionsForKeys);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ipRestrictionsForKeys);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationLoginSecurity200ResponseApiAuthentication {\n");
    sb.append("    ipRestrictionsForKeys: ").append(toIndentedString(ipRestrictionsForKeys)).append("\n");
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
    openapiFields.add("ipRestrictionsForKeys");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationLoginSecurity200ResponseApiAuthentication
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationLoginSecurity200ResponseApiAuthentication.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationLoginSecurity200ResponseApiAuthentication is not found in the empty JSON string", GetOrganizationLoginSecurity200ResponseApiAuthentication.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationLoginSecurity200ResponseApiAuthentication.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationLoginSecurity200ResponseApiAuthentication` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `ipRestrictionsForKeys`
      if (jsonObj.get("ipRestrictionsForKeys") != null && !jsonObj.get("ipRestrictionsForKeys").isJsonNull()) {
        GetOrganizationLoginSecurity200ResponseApiAuthenticationIpRestrictionsForKeys.validateJsonElement(jsonObj.get("ipRestrictionsForKeys"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationLoginSecurity200ResponseApiAuthentication.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationLoginSecurity200ResponseApiAuthentication' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationLoginSecurity200ResponseApiAuthentication> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationLoginSecurity200ResponseApiAuthentication.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationLoginSecurity200ResponseApiAuthentication>() {
           @Override
           public void write(JsonWriter out, GetOrganizationLoginSecurity200ResponseApiAuthentication value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationLoginSecurity200ResponseApiAuthentication read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationLoginSecurity200ResponseApiAuthentication given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationLoginSecurity200ResponseApiAuthentication
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationLoginSecurity200ResponseApiAuthentication
   */
  public static GetOrganizationLoginSecurity200ResponseApiAuthentication fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationLoginSecurity200ResponseApiAuthentication.class);
  }

  /**
   * Convert an instance of GetOrganizationLoginSecurity200ResponseApiAuthentication to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

