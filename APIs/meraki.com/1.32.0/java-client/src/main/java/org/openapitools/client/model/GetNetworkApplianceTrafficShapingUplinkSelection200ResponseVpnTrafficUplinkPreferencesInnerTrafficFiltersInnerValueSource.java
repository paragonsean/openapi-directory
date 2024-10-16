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
 * Source of &#39;custom&#39; type traffic filter
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource {
  public static final String SERIALIZED_NAME_CIDR = "cidr";
  @SerializedName(SERIALIZED_NAME_CIDR)
  private String cidr;

  public static final String SERIALIZED_NAME_HOST = "host";
  @SerializedName(SERIALIZED_NAME_HOST)
  private Integer host;

  public static final String SERIALIZED_NAME_NETWORK = "network";
  @SerializedName(SERIALIZED_NAME_NETWORK)
  private String network;

  public static final String SERIALIZED_NAME_PORT = "port";
  @SerializedName(SERIALIZED_NAME_PORT)
  private String port;

  public static final String SERIALIZED_NAME_VLAN = "vlan";
  @SerializedName(SERIALIZED_NAME_VLAN)
  private Integer vlan;

  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource() {
  }

  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource cidr(String cidr) {
    this.cidr = cidr;
    return this;
  }

  /**
   * CIDR format address (e.g.\&quot;192.168.10.1\&quot;, which is the same as \&quot;192.168.10.1/32\&quot;), or \&quot;any\&quot;. Cannot be used in combination with the \&quot;vlan\&quot; property
   * @return cidr
   */
  @javax.annotation.Nullable
  public String getCidr() {
    return cidr;
  }

  public void setCidr(String cidr) {
    this.cidr = cidr;
  }


  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource host(Integer host) {
    this.host = host;
    return this;
  }

  /**
   * Host ID in the VLAN. Should not exceed the VLAN subnet capacity. Must be used along with the \&quot;vlan\&quot; property and is currently only available under a template network.
   * @return host
   */
  @javax.annotation.Nullable
  public Integer getHost() {
    return host;
  }

  public void setHost(Integer host) {
    this.host = host;
  }


  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource network(String network) {
    this.network = network;
    return this;
  }

  /**
   * Meraki network ID. Currently only available under a template network, and the value should be ID of either same template network, or another template network currently. E.g.: \&quot;L_12345678\&quot;.
   * @return network
   */
  @javax.annotation.Nullable
  public String getNetwork() {
    return network;
  }

  public void setNetwork(String network) {
    this.network = network;
  }


  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource port(String port) {
    this.port = port;
    return this;
  }

  /**
   * E.g.: \&quot;any\&quot;, \&quot;0\&quot; (also means \&quot;any\&quot;), \&quot;8080\&quot;, \&quot;1-1024\&quot;
   * @return port
   */
  @javax.annotation.Nullable
  public String getPort() {
    return port;
  }

  public void setPort(String port) {
    this.port = port;
  }


  public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource vlan(Integer vlan) {
    this.vlan = vlan;
    return this;
  }

  /**
   * VLAN ID of the configured VLAN in the Meraki network. Cannot be used in combination with the \&quot;cidr\&quot; property and is currently only available under a template network.
   * @return vlan
   */
  @javax.annotation.Nullable
  public Integer getVlan() {
    return vlan;
  }

  public void setVlan(Integer vlan) {
    this.vlan = vlan;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource = (GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource) o;
    return Objects.equals(this.cidr, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.cidr) &&
        Objects.equals(this.host, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.host) &&
        Objects.equals(this.network, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.network) &&
        Objects.equals(this.port, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.port) &&
        Objects.equals(this.vlan, getNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.vlan);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cidr, host, network, port, vlan);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource {\n");
    sb.append("    cidr: ").append(toIndentedString(cidr)).append("\n");
    sb.append("    host: ").append(toIndentedString(host)).append("\n");
    sb.append("    network: ").append(toIndentedString(network)).append("\n");
    sb.append("    port: ").append(toIndentedString(port)).append("\n");
    sb.append("    vlan: ").append(toIndentedString(vlan)).append("\n");
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
    openapiFields.add("cidr");
    openapiFields.add("host");
    openapiFields.add("network");
    openapiFields.add("port");
    openapiFields.add("vlan");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource is not found in the empty JSON string", GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("cidr") != null && !jsonObj.get("cidr").isJsonNull()) && !jsonObj.get("cidr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cidr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cidr").toString()));
      }
      if ((jsonObj.get("network") != null && !jsonObj.get("network").isJsonNull()) && !jsonObj.get("network").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `network` to be a primitive type in the JSON string but got `%s`", jsonObj.get("network").toString()));
      }
      if ((jsonObj.get("port") != null && !jsonObj.get("port").isJsonNull()) && !jsonObj.get("port").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `port` to be a primitive type in the JSON string but got `%s`", jsonObj.get("port").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource>() {
           @Override
           public void write(JsonWriter out, GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource
   * @throws IOException if the JSON string is invalid with respect to GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource
   */
  public static GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource.class);
  }

  /**
   * Convert an instance of GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueSource to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

