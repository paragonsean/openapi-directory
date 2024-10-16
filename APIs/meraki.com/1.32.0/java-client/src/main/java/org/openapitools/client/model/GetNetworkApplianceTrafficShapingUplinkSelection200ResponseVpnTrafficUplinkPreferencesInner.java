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
import org.openapitools.client.model.GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass;
import org.openapitools.client.model.GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner;

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
 * GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner {
  /**
   * Fail over criterion for uplink preference rule. Must be one of: &#39;poorPerformance&#39; or &#39;uplinkDown&#39;
   */
  @JsonAdapter(FailOverCriterionEnum.Adapter.class)
  public enum FailOverCriterionEnum {
    POOR_PERFORMANCE("poorPerformance"),
    
    UPLINK_DOWN("uplinkDown");

    private String value;

    FailOverCriterionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static FailOverCriterionEnum fromValue(String value) {
      for (FailOverCriterionEnum b : FailOverCriterionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<FailOverCriterionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final FailOverCriterionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public FailOverCriterionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return FailOverCriterionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      FailOverCriterionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_FAIL_OVER_CRITERION = "failOverCriterion";
  @SerializedName(SERIALIZED_NAME_FAIL_OVER_CRITERION)
  private FailOverCriterionEnum failOverCriterion;

  public static final String SERIALIZED_NAME_PERFORMANCE_CLASS = "performanceClass";
  @SerializedName(SERIALIZED_NAME_PERFORMANCE_CLASS)
  private GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass performanceClass;

  /**
   * Preferred uplink for uplink preference rule. Must be one of: &#39;wan1&#39;, &#39;wan2&#39;, &#39;bestForVoIP&#39;, &#39;loadBalancing&#39; or &#39;defaultUplink&#39;
   */
  @JsonAdapter(PreferredUplinkEnum.Adapter.class)
  public enum PreferredUplinkEnum {
    BEST_FOR_VO_IP("bestForVoIP"),
    
    DEFAULT_UPLINK("defaultUplink"),
    
    LOAD_BALANCING("loadBalancing"),
    
    WAN1("wan1"),
    
    WAN2("wan2");

    private String value;

    PreferredUplinkEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PreferredUplinkEnum fromValue(String value) {
      for (PreferredUplinkEnum b : PreferredUplinkEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PreferredUplinkEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PreferredUplinkEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PreferredUplinkEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PreferredUplinkEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PreferredUplinkEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PREFERRED_UPLINK = "preferredUplink";
  @SerializedName(SERIALIZED_NAME_PREFERRED_UPLINK)
  private PreferredUplinkEnum preferredUplink;

  public static final String SERIALIZED_NAME_TRAFFIC_FILTERS = "trafficFilters";
  @SerializedName(SERIALIZED_NAME_TRAFFIC_FILTERS)
  private List<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner> trafficFilters = new ArrayList<>();

  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner() {
  }

  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner failOverCriterion(FailOverCriterionEnum failOverCriterion) {
    this.failOverCriterion = failOverCriterion;
    return this;
  }

  /**
   * Fail over criterion for uplink preference rule. Must be one of: &#39;poorPerformance&#39; or &#39;uplinkDown&#39;
   * @return failOverCriterion
   */
  @javax.annotation.Nullable
  public FailOverCriterionEnum getFailOverCriterion() {
    return failOverCriterion;
  }

  public void setFailOverCriterion(FailOverCriterionEnum failOverCriterion) {
    this.failOverCriterion = failOverCriterion;
  }


  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner performanceClass(GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass performanceClass) {
    this.performanceClass = performanceClass;
    return this;
  }

  /**
   * Get performanceClass
   * @return performanceClass
   */
  @javax.annotation.Nullable
  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass getPerformanceClass() {
    return performanceClass;
  }

  public void setPerformanceClass(GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass performanceClass) {
    this.performanceClass = performanceClass;
  }


  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner preferredUplink(PreferredUplinkEnum preferredUplink) {
    this.preferredUplink = preferredUplink;
    return this;
  }

  /**
   * Preferred uplink for uplink preference rule. Must be one of: &#39;wan1&#39;, &#39;wan2&#39;, &#39;bestForVoIP&#39;, &#39;loadBalancing&#39; or &#39;defaultUplink&#39;
   * @return preferredUplink
   */
  @javax.annotation.Nonnull
  public PreferredUplinkEnum getPreferredUplink() {
    return preferredUplink;
  }

  public void setPreferredUplink(PreferredUplinkEnum preferredUplink) {
    this.preferredUplink = preferredUplink;
  }


  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner trafficFilters(List<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner> trafficFilters) {
    this.trafficFilters = trafficFilters;
    return this;
  }

  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner addTrafficFiltersItem(GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner trafficFiltersItem) {
    if (this.trafficFilters == null) {
      this.trafficFilters = new ArrayList<>();
    }
    this.trafficFilters.add(trafficFiltersItem);
    return this;
  }

  /**
   * Traffic filters
   * @return trafficFilters
   */
  @javax.annotation.Nonnull
  public List<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner> getTrafficFilters() {
    return trafficFilters;
  }

  public void setTrafficFilters(List<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner> trafficFilters) {
    this.trafficFilters = trafficFilters;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner = (GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner) o;
    return Objects.equals(this.failOverCriterion, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.failOverCriterion) &&
        Objects.equals(this.performanceClass, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.performanceClass) &&
        Objects.equals(this.preferredUplink, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.preferredUplink) &&
        Objects.equals(this.trafficFilters, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.trafficFilters);
  }

  @Override
  public int hashCode() {
    return Objects.hash(failOverCriterion, performanceClass, preferredUplink, trafficFilters);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner {\n");
    sb.append("    failOverCriterion: ").append(toIndentedString(failOverCriterion)).append("\n");
    sb.append("    performanceClass: ").append(toIndentedString(performanceClass)).append("\n");
    sb.append("    preferredUplink: ").append(toIndentedString(preferredUplink)).append("\n");
    sb.append("    trafficFilters: ").append(toIndentedString(trafficFilters)).append("\n");
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
    openapiFields.add("failOverCriterion");
    openapiFields.add("performanceClass");
    openapiFields.add("preferredUplink");
    openapiFields.add("trafficFilters");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("preferredUplink");
    openapiRequiredFields.add("trafficFilters");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner is not found in the empty JSON string", GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("failOverCriterion") != null && !jsonObj.get("failOverCriterion").isJsonNull()) && !jsonObj.get("failOverCriterion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `failOverCriterion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("failOverCriterion").toString()));
      }
      // validate the optional field `failOverCriterion`
      if (jsonObj.get("failOverCriterion") != null && !jsonObj.get("failOverCriterion").isJsonNull()) {
        FailOverCriterionEnum.validateJsonElement(jsonObj.get("failOverCriterion"));
      }
      // validate the optional field `performanceClass`
      if (jsonObj.get("performanceClass") != null && !jsonObj.get("performanceClass").isJsonNull()) {
        GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerPerformanceClass.validateJsonElement(jsonObj.get("performanceClass"));
      }
      if (!jsonObj.get("preferredUplink").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preferredUplink` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preferredUplink").toString()));
      }
      // validate the required field `preferredUplink`
      PreferredUplinkEnum.validateJsonElement(jsonObj.get("preferredUplink"));
      // ensure the json data is an array
      if (!jsonObj.get("trafficFilters").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `trafficFilters` to be an array in the JSON string but got `%s`", jsonObj.get("trafficFilters").toString()));
      }

      JsonArray jsonArraytrafficFilters = jsonObj.getAsJsonArray("trafficFilters");
      // validate the required field `trafficFilters` (array)
      for (int i = 0; i < jsonArraytrafficFilters.size(); i++) {
        GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInner.validateJsonElement(jsonArraytrafficFilters.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner>() {
           @Override
           public void write(JsonWriter out, GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner
   * @throws IOException if the JSON string is invalid with respect to GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner
   */
  public static GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner.class);
  }

  /**
   * Convert an instance of GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

