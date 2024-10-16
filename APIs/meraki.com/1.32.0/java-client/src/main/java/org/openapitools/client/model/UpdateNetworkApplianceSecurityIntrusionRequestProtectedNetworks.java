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
 * Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in &#39;passthrough&#39; mode
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks {
  public static final String SERIALIZED_NAME_EXCLUDED_CIDR = "excludedCidr";
  @SerializedName(SERIALIZED_NAME_EXCLUDED_CIDR)
  private List<String> excludedCidr = new ArrayList<>();

  public static final String SERIALIZED_NAME_INCLUDED_CIDR = "includedCidr";
  @SerializedName(SERIALIZED_NAME_INCLUDED_CIDR)
  private List<String> includedCidr = new ArrayList<>();

  public static final String SERIALIZED_NAME_USE_DEFAULT = "useDefault";
  @SerializedName(SERIALIZED_NAME_USE_DEFAULT)
  private Boolean useDefault;

  public UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks() {
  }

  public UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks excludedCidr(List<String> excludedCidr) {
    this.excludedCidr = excludedCidr;
    return this;
  }

  public UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks addExcludedCidrItem(String excludedCidrItem) {
    if (this.excludedCidr == null) {
      this.excludedCidr = new ArrayList<>();
    }
    this.excludedCidr.add(excludedCidrItem);
    return this;
  }

  /**
   * list of IP addresses or subnets being excluded from protection (required if &#39;useDefault&#39; is false)
   * @return excludedCidr
   */
  @javax.annotation.Nullable
  public List<String> getExcludedCidr() {
    return excludedCidr;
  }

  public void setExcludedCidr(List<String> excludedCidr) {
    this.excludedCidr = excludedCidr;
  }


  public UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks includedCidr(List<String> includedCidr) {
    this.includedCidr = includedCidr;
    return this;
  }

  public UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks addIncludedCidrItem(String includedCidrItem) {
    if (this.includedCidr == null) {
      this.includedCidr = new ArrayList<>();
    }
    this.includedCidr.add(includedCidrItem);
    return this;
  }

  /**
   * list of IP addresses or subnets being protected (required if &#39;useDefault&#39; is false)
   * @return includedCidr
   */
  @javax.annotation.Nullable
  public List<String> getIncludedCidr() {
    return includedCidr;
  }

  public void setIncludedCidr(List<String> includedCidr) {
    this.includedCidr = includedCidr;
  }


  public UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks useDefault(Boolean useDefault) {
    this.useDefault = useDefault;
    return this;
  }

  /**
   * true/false whether to use special IPv4 addresses: https://tools.ietf.org/html/rfc5735 (required). Default value is true if none currently saved
   * @return useDefault
   */
  @javax.annotation.Nullable
  public Boolean getUseDefault() {
    return useDefault;
  }

  public void setUseDefault(Boolean useDefault) {
    this.useDefault = useDefault;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks updateNetworkApplianceSecurityIntrusionRequestProtectedNetworks = (UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks) o;
    return Objects.equals(this.excludedCidr, updateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.excludedCidr) &&
        Objects.equals(this.includedCidr, updateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.includedCidr) &&
        Objects.equals(this.useDefault, updateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.useDefault);
  }

  @Override
  public int hashCode() {
    return Objects.hash(excludedCidr, includedCidr, useDefault);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks {\n");
    sb.append("    excludedCidr: ").append(toIndentedString(excludedCidr)).append("\n");
    sb.append("    includedCidr: ").append(toIndentedString(includedCidr)).append("\n");
    sb.append("    useDefault: ").append(toIndentedString(useDefault)).append("\n");
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
    openapiFields.add("excludedCidr");
    openapiFields.add("includedCidr");
    openapiFields.add("useDefault");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks is not found in the empty JSON string", UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("excludedCidr") != null && !jsonObj.get("excludedCidr").isJsonNull() && !jsonObj.get("excludedCidr").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `excludedCidr` to be an array in the JSON string but got `%s`", jsonObj.get("excludedCidr").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("includedCidr") != null && !jsonObj.get("includedCidr").isJsonNull() && !jsonObj.get("includedCidr").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `includedCidr` to be an array in the JSON string but got `%s`", jsonObj.get("includedCidr").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks
   */
  public static UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks.class);
  }

  /**
   * Convert an instance of UpdateNetworkApplianceSecurityIntrusionRequestProtectedNetworks to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

