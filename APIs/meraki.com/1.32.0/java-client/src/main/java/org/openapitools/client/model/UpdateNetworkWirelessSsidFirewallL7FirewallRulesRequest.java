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
import org.openapitools.client.model.UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner;

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
 * UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest {
  public static final String SERIALIZED_NAME_RULES = "rules";
  @SerializedName(SERIALIZED_NAME_RULES)
  private List<UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner> rules = new ArrayList<>();

  public UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest() {
  }

  public UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest rules(List<UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner> rules) {
    this.rules = rules;
    return this;
  }

  public UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest addRulesItem(UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner rulesItem) {
    if (this.rules == null) {
      this.rules = new ArrayList<>();
    }
    this.rules.add(rulesItem);
    return this;
  }

  /**
   * An array of L7 firewall rules for this SSID. Rules will get applied in the same order user has specified in request. Empty array will clear the L7 firewall rule configuration.
   * @return rules
   */
  @javax.annotation.Nullable
  public List<UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner> getRules() {
    return rules;
  }

  public void setRules(List<UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner> rules) {
    this.rules = rules;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest updateNetworkWirelessSsidFirewallL7FirewallRulesRequest = (UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest) o;
    return Objects.equals(this.rules, updateNetworkWirelessSsidFirewallL7FirewallRulesRequest.rules);
  }

  @Override
  public int hashCode() {
    return Objects.hash(rules);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest {\n");
    sb.append("    rules: ").append(toIndentedString(rules)).append("\n");
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
    openapiFields.add("rules");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest is not found in the empty JSON string", UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequestRulesInner.validateJsonElement(jsonArrayrules.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
   */
  public static UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.class);
  }

  /**
   * Convert an instance of UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

