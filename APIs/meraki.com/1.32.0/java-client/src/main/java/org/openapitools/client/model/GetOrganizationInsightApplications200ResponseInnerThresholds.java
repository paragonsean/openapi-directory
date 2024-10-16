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
import org.openapitools.client.model.GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner;

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
 * Thresholds defined by a user or Meraki models for each application
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationInsightApplications200ResponseInnerThresholds {
  public static final String SERIALIZED_NAME_BY_NETWORK = "byNetwork";
  @SerializedName(SERIALIZED_NAME_BY_NETWORK)
  private List<GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner> byNetwork = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public GetOrganizationInsightApplications200ResponseInnerThresholds() {
  }

  public GetOrganizationInsightApplications200ResponseInnerThresholds byNetwork(List<GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner> byNetwork) {
    this.byNetwork = byNetwork;
    return this;
  }

  public GetOrganizationInsightApplications200ResponseInnerThresholds addByNetworkItem(GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner byNetworkItem) {
    if (this.byNetwork == null) {
      this.byNetwork = new ArrayList<>();
    }
    this.byNetwork.add(byNetworkItem);
    return this;
  }

  /**
   * Threshold for each network
   * @return byNetwork
   */
  @javax.annotation.Nullable
  public List<GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner> getByNetwork() {
    return byNetwork;
  }

  public void setByNetwork(List<GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner> byNetwork) {
    this.byNetwork = byNetwork;
  }


  public GetOrganizationInsightApplications200ResponseInnerThresholds type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Threshold type (static or smart)
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationInsightApplications200ResponseInnerThresholds getOrganizationInsightApplications200ResponseInnerThresholds = (GetOrganizationInsightApplications200ResponseInnerThresholds) o;
    return Objects.equals(this.byNetwork, getOrganizationInsightApplications200ResponseInnerThresholds.byNetwork) &&
        Objects.equals(this.type, getOrganizationInsightApplications200ResponseInnerThresholds.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(byNetwork, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationInsightApplications200ResponseInnerThresholds {\n");
    sb.append("    byNetwork: ").append(toIndentedString(byNetwork)).append("\n");
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
    openapiFields.add("byNetwork");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationInsightApplications200ResponseInnerThresholds
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationInsightApplications200ResponseInnerThresholds.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationInsightApplications200ResponseInnerThresholds is not found in the empty JSON string", GetOrganizationInsightApplications200ResponseInnerThresholds.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationInsightApplications200ResponseInnerThresholds.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationInsightApplications200ResponseInnerThresholds` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("byNetwork") != null && !jsonObj.get("byNetwork").isJsonNull()) {
        JsonArray jsonArraybyNetwork = jsonObj.getAsJsonArray("byNetwork");
        if (jsonArraybyNetwork != null) {
          // ensure the json data is an array
          if (!jsonObj.get("byNetwork").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `byNetwork` to be an array in the JSON string but got `%s`", jsonObj.get("byNetwork").toString()));
          }

          // validate the optional field `byNetwork` (array)
          for (int i = 0; i < jsonArraybyNetwork.size(); i++) {
            GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.validateJsonElement(jsonArraybyNetwork.get(i));
          };
        }
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationInsightApplications200ResponseInnerThresholds.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationInsightApplications200ResponseInnerThresholds' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationInsightApplications200ResponseInnerThresholds> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationInsightApplications200ResponseInnerThresholds.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationInsightApplications200ResponseInnerThresholds>() {
           @Override
           public void write(JsonWriter out, GetOrganizationInsightApplications200ResponseInnerThresholds value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationInsightApplications200ResponseInnerThresholds read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationInsightApplications200ResponseInnerThresholds given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationInsightApplications200ResponseInnerThresholds
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationInsightApplications200ResponseInnerThresholds
   */
  public static GetOrganizationInsightApplications200ResponseInnerThresholds fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationInsightApplications200ResponseInnerThresholds.class);
  }

  /**
   * Convert an instance of GetOrganizationInsightApplications200ResponseInnerThresholds to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

