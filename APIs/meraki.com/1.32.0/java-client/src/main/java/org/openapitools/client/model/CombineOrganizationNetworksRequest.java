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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * CombineOrganizationNetworksRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CombineOrganizationNetworksRequest {
  public static final String SERIALIZED_NAME_ENROLLMENT_STRING = "enrollmentString";
  @SerializedName(SERIALIZED_NAME_ENROLLMENT_STRING)
  private String enrollmentString;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NETWORK_IDS = "networkIds";
  @SerializedName(SERIALIZED_NAME_NETWORK_IDS)
  private List<String> networkIds = new ArrayList<>();

  public CombineOrganizationNetworksRequest() {
  }

  public CombineOrganizationNetworksRequest enrollmentString(String enrollmentString) {
    this.enrollmentString = enrollmentString;
    return this;
  }

  /**
   * A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by &#39;-network_type&#39;. If left empty, all exisitng enrollment strings will be deleted.
   * @return enrollmentString
   */
  @javax.annotation.Nullable
  public String getEnrollmentString() {
    return enrollmentString;
  }

  public void setEnrollmentString(String enrollmentString) {
    this.enrollmentString = enrollmentString;
  }


  public CombineOrganizationNetworksRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the combined network
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CombineOrganizationNetworksRequest networkIds(List<String> networkIds) {
    this.networkIds = networkIds;
    return this;
  }

  public CombineOrganizationNetworksRequest addNetworkIdsItem(String networkIdsItem) {
    if (this.networkIds == null) {
      this.networkIds = new ArrayList<>();
    }
    this.networkIds.add(networkIdsItem);
    return this;
  }

  /**
   * A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
   * @return networkIds
   */
  @javax.annotation.Nonnull
  public List<String> getNetworkIds() {
    return networkIds;
  }

  public void setNetworkIds(List<String> networkIds) {
    this.networkIds = networkIds;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CombineOrganizationNetworksRequest combineOrganizationNetworksRequest = (CombineOrganizationNetworksRequest) o;
    return Objects.equals(this.enrollmentString, combineOrganizationNetworksRequest.enrollmentString) &&
        Objects.equals(this.name, combineOrganizationNetworksRequest.name) &&
        Objects.equals(this.networkIds, combineOrganizationNetworksRequest.networkIds);
  }

  @Override
  public int hashCode() {
    return Objects.hash(enrollmentString, name, networkIds);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CombineOrganizationNetworksRequest {\n");
    sb.append("    enrollmentString: ").append(toIndentedString(enrollmentString)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    networkIds: ").append(toIndentedString(networkIds)).append("\n");
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
    openapiFields.add("enrollmentString");
    openapiFields.add("name");
    openapiFields.add("networkIds");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("networkIds");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CombineOrganizationNetworksRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CombineOrganizationNetworksRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CombineOrganizationNetworksRequest is not found in the empty JSON string", CombineOrganizationNetworksRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CombineOrganizationNetworksRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CombineOrganizationNetworksRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CombineOrganizationNetworksRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("enrollmentString") != null && !jsonObj.get("enrollmentString").isJsonNull()) && !jsonObj.get("enrollmentString").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `enrollmentString` to be a primitive type in the JSON string but got `%s`", jsonObj.get("enrollmentString").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("networkIds") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("networkIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `networkIds` to be an array in the JSON string but got `%s`", jsonObj.get("networkIds").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CombineOrganizationNetworksRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CombineOrganizationNetworksRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CombineOrganizationNetworksRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CombineOrganizationNetworksRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CombineOrganizationNetworksRequest>() {
           @Override
           public void write(JsonWriter out, CombineOrganizationNetworksRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CombineOrganizationNetworksRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CombineOrganizationNetworksRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CombineOrganizationNetworksRequest
   * @throws IOException if the JSON string is invalid with respect to CombineOrganizationNetworksRequest
   */
  public static CombineOrganizationNetworksRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CombineOrganizationNetworksRequest.class);
  }

  /**
   * Convert an instance of CombineOrganizationNetworksRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

