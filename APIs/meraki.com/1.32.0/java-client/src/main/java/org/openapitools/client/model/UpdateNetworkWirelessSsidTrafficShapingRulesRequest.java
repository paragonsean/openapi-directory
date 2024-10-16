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
import org.openapitools.client.model.UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner;

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
 * UpdateNetworkWirelessSsidTrafficShapingRulesRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkWirelessSsidTrafficShapingRulesRequest {
  public static final String SERIALIZED_NAME_DEFAULT_RULES_ENABLED = "defaultRulesEnabled";
  @SerializedName(SERIALIZED_NAME_DEFAULT_RULES_ENABLED)
  private Boolean defaultRulesEnabled;

  public static final String SERIALIZED_NAME_RULES = "rules";
  @SerializedName(SERIALIZED_NAME_RULES)
  private List<UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner> rules = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRAFFIC_SHAPING_ENABLED = "trafficShapingEnabled";
  @SerializedName(SERIALIZED_NAME_TRAFFIC_SHAPING_ENABLED)
  private Boolean trafficShapingEnabled;

  public UpdateNetworkWirelessSsidTrafficShapingRulesRequest() {
  }

  public UpdateNetworkWirelessSsidTrafficShapingRulesRequest defaultRulesEnabled(Boolean defaultRulesEnabled) {
    this.defaultRulesEnabled = defaultRulesEnabled;
    return this;
  }

  /**
   * Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network&#39;s traffic shaping page. Note that default rules count against the rule limit of 8.
   * @return defaultRulesEnabled
   */
  @javax.annotation.Nullable
  public Boolean getDefaultRulesEnabled() {
    return defaultRulesEnabled;
  }

  public void setDefaultRulesEnabled(Boolean defaultRulesEnabled) {
    this.defaultRulesEnabled = defaultRulesEnabled;
  }


  public UpdateNetworkWirelessSsidTrafficShapingRulesRequest rules(List<UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner> rules) {
    this.rules = rules;
    return this;
  }

  public UpdateNetworkWirelessSsidTrafficShapingRulesRequest addRulesItem(UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner rulesItem) {
    if (this.rules == null) {
      this.rules = new ArrayList<>();
    }
    this.rules.add(rulesItem);
    return this;
  }

  /**
   *     An array of traffic shaping rules. Rules are applied in the order that     they are specified in. An empty list (or null) means no rules. Note that     you are allowed a maximum of 8 rules. 
   * @return rules
   */
  @javax.annotation.Nullable
  public List<UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner> getRules() {
    return rules;
  }

  public void setRules(List<UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner> rules) {
    this.rules = rules;
  }


  public UpdateNetworkWirelessSsidTrafficShapingRulesRequest trafficShapingEnabled(Boolean trafficShapingEnabled) {
    this.trafficShapingEnabled = trafficShapingEnabled;
    return this;
  }

  /**
   * Whether traffic shaping rules are applied to clients on your SSID.
   * @return trafficShapingEnabled
   */
  @javax.annotation.Nullable
  public Boolean getTrafficShapingEnabled() {
    return trafficShapingEnabled;
  }

  public void setTrafficShapingEnabled(Boolean trafficShapingEnabled) {
    this.trafficShapingEnabled = trafficShapingEnabled;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkWirelessSsidTrafficShapingRulesRequest updateNetworkWirelessSsidTrafficShapingRulesRequest = (UpdateNetworkWirelessSsidTrafficShapingRulesRequest) o;
    return Objects.equals(this.defaultRulesEnabled, updateNetworkWirelessSsidTrafficShapingRulesRequest.defaultRulesEnabled) &&
        Objects.equals(this.rules, updateNetworkWirelessSsidTrafficShapingRulesRequest.rules) &&
        Objects.equals(this.trafficShapingEnabled, updateNetworkWirelessSsidTrafficShapingRulesRequest.trafficShapingEnabled);
  }

  @Override
  public int hashCode() {
    return Objects.hash(defaultRulesEnabled, rules, trafficShapingEnabled);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkWirelessSsidTrafficShapingRulesRequest {\n");
    sb.append("    defaultRulesEnabled: ").append(toIndentedString(defaultRulesEnabled)).append("\n");
    sb.append("    rules: ").append(toIndentedString(rules)).append("\n");
    sb.append("    trafficShapingEnabled: ").append(toIndentedString(trafficShapingEnabled)).append("\n");
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
    openapiFields.add("defaultRulesEnabled");
    openapiFields.add("rules");
    openapiFields.add("trafficShapingEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkWirelessSsidTrafficShapingRulesRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkWirelessSsidTrafficShapingRulesRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkWirelessSsidTrafficShapingRulesRequest is not found in the empty JSON string", UpdateNetworkWirelessSsidTrafficShapingRulesRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkWirelessSsidTrafficShapingRulesRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkWirelessSsidTrafficShapingRulesRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("rules") != null && !jsonObj.get("rules").isJsonNull()) {
        JsonArray jsonArrayrules = jsonObj.getAsJsonArray("rules");
        if (jsonArrayrules != null) {
          // ensure the json data is an array
          if (!jsonObj.get("rules").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `rules` to be an array in the JSON string but got `%s`", jsonObj.get("rules").toString()));
          }

          // validate the optional field `rules` (array)
          for (int i = 0; i < jsonArrayrules.size(); i++) {
            UpdateNetworkWirelessSsidTrafficShapingRulesRequestRulesInner.validateJsonElement(jsonArrayrules.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkWirelessSsidTrafficShapingRulesRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkWirelessSsidTrafficShapingRulesRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkWirelessSsidTrafficShapingRulesRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkWirelessSsidTrafficShapingRulesRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkWirelessSsidTrafficShapingRulesRequest>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkWirelessSsidTrafficShapingRulesRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkWirelessSsidTrafficShapingRulesRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkWirelessSsidTrafficShapingRulesRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkWirelessSsidTrafficShapingRulesRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkWirelessSsidTrafficShapingRulesRequest
   */
  public static UpdateNetworkWirelessSsidTrafficShapingRulesRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkWirelessSsidTrafficShapingRulesRequest.class);
  }

  /**
   * Convert an instance of UpdateNetworkWirelessSsidTrafficShapingRulesRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

