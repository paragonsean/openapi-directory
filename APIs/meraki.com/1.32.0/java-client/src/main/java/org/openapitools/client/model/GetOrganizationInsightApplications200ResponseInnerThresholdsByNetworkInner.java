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
 * GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner {
  public static final String SERIALIZED_NAME_GOODPUT = "goodput";
  @SerializedName(SERIALIZED_NAME_GOODPUT)
  private Integer goodput;

  public static final String SERIALIZED_NAME_NETWORK_ID = "networkId";
  @SerializedName(SERIALIZED_NAME_NETWORK_ID)
  private String networkId;

  public static final String SERIALIZED_NAME_RESPONSE_DURATION = "responseDuration";
  @SerializedName(SERIALIZED_NAME_RESPONSE_DURATION)
  private Integer responseDuration;

  public GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner() {
  }

  public GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner goodput(Integer goodput) {
    this.goodput = goodput;
    return this;
  }

  /**
   * Number of useful information bits delivered over a network per unit of time
   * @return goodput
   */
  @javax.annotation.Nullable
  public Integer getGoodput() {
    return goodput;
  }

  public void setGoodput(Integer goodput) {
    this.goodput = goodput;
  }


  public GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner networkId(String networkId) {
    this.networkId = networkId;
    return this;
  }

  /**
   * Network identifier
   * @return networkId
   */
  @javax.annotation.Nullable
  public String getNetworkId() {
    return networkId;
  }

  public void setNetworkId(String networkId) {
    this.networkId = networkId;
  }


  public GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner responseDuration(Integer responseDuration) {
    this.responseDuration = responseDuration;
    return this;
  }

  /**
   * Duration of the response, in milliseconds
   * @return responseDuration
   */
  @javax.annotation.Nullable
  public Integer getResponseDuration() {
    return responseDuration;
  }

  public void setResponseDuration(Integer responseDuration) {
    this.responseDuration = responseDuration;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner getOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner = (GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner) o;
    return Objects.equals(this.goodput, getOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.goodput) &&
        Objects.equals(this.networkId, getOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.networkId) &&
        Objects.equals(this.responseDuration, getOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.responseDuration);
  }

  @Override
  public int hashCode() {
    return Objects.hash(goodput, networkId, responseDuration);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner {\n");
    sb.append("    goodput: ").append(toIndentedString(goodput)).append("\n");
    sb.append("    networkId: ").append(toIndentedString(networkId)).append("\n");
    sb.append("    responseDuration: ").append(toIndentedString(responseDuration)).append("\n");
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
    openapiFields.add("goodput");
    openapiFields.add("networkId");
    openapiFields.add("responseDuration");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner is not found in the empty JSON string", GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("networkId") != null && !jsonObj.get("networkId").isJsonNull()) && !jsonObj.get("networkId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `networkId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("networkId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner>() {
           @Override
           public void write(JsonWriter out, GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner
   */
  public static GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner.class);
  }

  /**
   * Convert an instance of GetOrganizationInsightApplications200ResponseInnerThresholdsByNetworkInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

