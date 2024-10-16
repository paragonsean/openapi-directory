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
import org.openapitools.client.model.CreateDeviceSwitchRoutingInterfaceRequestIpv6;
import org.openapitools.client.model.CreateDeviceSwitchRoutingInterfaceRequestOspfSettings;
import org.openapitools.client.model.CreateDeviceSwitchRoutingInterfaceRequestOspfV3;

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
 * CreateDeviceSwitchRoutingInterfaceRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateDeviceSwitchRoutingInterfaceRequest {
  public static final String SERIALIZED_NAME_DEFAULT_GATEWAY = "defaultGateway";
  @SerializedName(SERIALIZED_NAME_DEFAULT_GATEWAY)
  private String defaultGateway;

  public static final String SERIALIZED_NAME_INTERFACE_IP = "interfaceIp";
  @SerializedName(SERIALIZED_NAME_INTERFACE_IP)
  private String interfaceIp;

  public static final String SERIALIZED_NAME_IPV6 = "ipv6";
  @SerializedName(SERIALIZED_NAME_IPV6)
  private CreateDeviceSwitchRoutingInterfaceRequestIpv6 ipv6;

  /**
   * Enable multicast support if, multicast routing between VLANs is required. Options are:         &#39;disabled&#39;, &#39;enabled&#39; or &#39;IGMP snooping querier&#39;. Default is &#39;disabled&#39;.
   */
  @JsonAdapter(MulticastRoutingEnum.Adapter.class)
  public enum MulticastRoutingEnum {
    IGMP_SNOOPING_QUERIER("IGMP snooping querier"),
    
    DISABLED("disabled"),
    
    ENABLED("enabled");

    private String value;

    MulticastRoutingEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MulticastRoutingEnum fromValue(String value) {
      for (MulticastRoutingEnum b : MulticastRoutingEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MulticastRoutingEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MulticastRoutingEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MulticastRoutingEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MulticastRoutingEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MulticastRoutingEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_MULTICAST_ROUTING = "multicastRouting";
  @SerializedName(SERIALIZED_NAME_MULTICAST_ROUTING)
  private MulticastRoutingEnum multicastRouting;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OSPF_SETTINGS = "ospfSettings";
  @SerializedName(SERIALIZED_NAME_OSPF_SETTINGS)
  private CreateDeviceSwitchRoutingInterfaceRequestOspfSettings ospfSettings;

  public static final String SERIALIZED_NAME_OSPF_V3 = "ospfV3";
  @SerializedName(SERIALIZED_NAME_OSPF_V3)
  private CreateDeviceSwitchRoutingInterfaceRequestOspfV3 ospfV3;

  public static final String SERIALIZED_NAME_SUBNET = "subnet";
  @SerializedName(SERIALIZED_NAME_SUBNET)
  private String subnet;

  public static final String SERIALIZED_NAME_VLAN_ID = "vlanId";
  @SerializedName(SERIALIZED_NAME_VLAN_ID)
  private Integer vlanId;

  public CreateDeviceSwitchRoutingInterfaceRequest() {
  }

  public CreateDeviceSwitchRoutingInterfaceRequest defaultGateway(String defaultGateway) {
    this.defaultGateway = defaultGateway;
    return this;
  }

  /**
   * The next hop for any traffic that isn&#39;t going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a routed interface. Required if this is the first IPv4 interface.
   * @return defaultGateway
   */
  @javax.annotation.Nullable
  public String getDefaultGateway() {
    return defaultGateway;
  }

  public void setDefaultGateway(String defaultGateway) {
    this.defaultGateway = defaultGateway;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest interfaceIp(String interfaceIp) {
    this.interfaceIp = interfaceIp;
    return this;
  }

  /**
   * The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same         as the switch&#39;s management IP.
   * @return interfaceIp
   */
  @javax.annotation.Nullable
  public String getInterfaceIp() {
    return interfaceIp;
  }

  public void setInterfaceIp(String interfaceIp) {
    this.interfaceIp = interfaceIp;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest ipv6(CreateDeviceSwitchRoutingInterfaceRequestIpv6 ipv6) {
    this.ipv6 = ipv6;
    return this;
  }

  /**
   * Get ipv6
   * @return ipv6
   */
  @javax.annotation.Nullable
  public CreateDeviceSwitchRoutingInterfaceRequestIpv6 getIpv6() {
    return ipv6;
  }

  public void setIpv6(CreateDeviceSwitchRoutingInterfaceRequestIpv6 ipv6) {
    this.ipv6 = ipv6;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest multicastRouting(MulticastRoutingEnum multicastRouting) {
    this.multicastRouting = multicastRouting;
    return this;
  }

  /**
   * Enable multicast support if, multicast routing between VLANs is required. Options are:         &#39;disabled&#39;, &#39;enabled&#39; or &#39;IGMP snooping querier&#39;. Default is &#39;disabled&#39;.
   * @return multicastRouting
   */
  @javax.annotation.Nullable
  public MulticastRoutingEnum getMulticastRouting() {
    return multicastRouting;
  }

  public void setMulticastRouting(MulticastRoutingEnum multicastRouting) {
    this.multicastRouting = multicastRouting;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest name(String name) {
    this.name = name;
    return this;
  }

  /**
   * A friendly name or description for the interface or VLAN.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest ospfSettings(CreateDeviceSwitchRoutingInterfaceRequestOspfSettings ospfSettings) {
    this.ospfSettings = ospfSettings;
    return this;
  }

  /**
   * Get ospfSettings
   * @return ospfSettings
   */
  @javax.annotation.Nullable
  public CreateDeviceSwitchRoutingInterfaceRequestOspfSettings getOspfSettings() {
    return ospfSettings;
  }

  public void setOspfSettings(CreateDeviceSwitchRoutingInterfaceRequestOspfSettings ospfSettings) {
    this.ospfSettings = ospfSettings;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest ospfV3(CreateDeviceSwitchRoutingInterfaceRequestOspfV3 ospfV3) {
    this.ospfV3 = ospfV3;
    return this;
  }

  /**
   * Get ospfV3
   * @return ospfV3
   */
  @javax.annotation.Nullable
  public CreateDeviceSwitchRoutingInterfaceRequestOspfV3 getOspfV3() {
    return ospfV3;
  }

  public void setOspfV3(CreateDeviceSwitchRoutingInterfaceRequestOspfV3 ospfV3) {
    this.ospfV3 = ospfV3;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest subnet(String subnet) {
    this.subnet = subnet;
    return this;
  }

  /**
   * The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
   * @return subnet
   */
  @javax.annotation.Nullable
  public String getSubnet() {
    return subnet;
  }

  public void setSubnet(String subnet) {
    this.subnet = subnet;
  }


  public CreateDeviceSwitchRoutingInterfaceRequest vlanId(Integer vlanId) {
    this.vlanId = vlanId;
    return this;
  }

  /**
   * The VLAN this routed interface is on. VLAN must be between 1 and 4094.
   * @return vlanId
   */
  @javax.annotation.Nullable
  public Integer getVlanId() {
    return vlanId;
  }

  public void setVlanId(Integer vlanId) {
    this.vlanId = vlanId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = (CreateDeviceSwitchRoutingInterfaceRequest) o;
    return Objects.equals(this.defaultGateway, createDeviceSwitchRoutingInterfaceRequest.defaultGateway) &&
        Objects.equals(this.interfaceIp, createDeviceSwitchRoutingInterfaceRequest.interfaceIp) &&
        Objects.equals(this.ipv6, createDeviceSwitchRoutingInterfaceRequest.ipv6) &&
        Objects.equals(this.multicastRouting, createDeviceSwitchRoutingInterfaceRequest.multicastRouting) &&
        Objects.equals(this.name, createDeviceSwitchRoutingInterfaceRequest.name) &&
        Objects.equals(this.ospfSettings, createDeviceSwitchRoutingInterfaceRequest.ospfSettings) &&
        Objects.equals(this.ospfV3, createDeviceSwitchRoutingInterfaceRequest.ospfV3) &&
        Objects.equals(this.subnet, createDeviceSwitchRoutingInterfaceRequest.subnet) &&
        Objects.equals(this.vlanId, createDeviceSwitchRoutingInterfaceRequest.vlanId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(defaultGateway, interfaceIp, ipv6, multicastRouting, name, ospfSettings, ospfV3, subnet, vlanId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateDeviceSwitchRoutingInterfaceRequest {\n");
    sb.append("    defaultGateway: ").append(toIndentedString(defaultGateway)).append("\n");
    sb.append("    interfaceIp: ").append(toIndentedString(interfaceIp)).append("\n");
    sb.append("    ipv6: ").append(toIndentedString(ipv6)).append("\n");
    sb.append("    multicastRouting: ").append(toIndentedString(multicastRouting)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ospfSettings: ").append(toIndentedString(ospfSettings)).append("\n");
    sb.append("    ospfV3: ").append(toIndentedString(ospfV3)).append("\n");
    sb.append("    subnet: ").append(toIndentedString(subnet)).append("\n");
    sb.append("    vlanId: ").append(toIndentedString(vlanId)).append("\n");
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
    openapiFields.add("defaultGateway");
    openapiFields.add("interfaceIp");
    openapiFields.add("ipv6");
    openapiFields.add("multicastRouting");
    openapiFields.add("name");
    openapiFields.add("ospfSettings");
    openapiFields.add("ospfV3");
    openapiFields.add("subnet");
    openapiFields.add("vlanId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateDeviceSwitchRoutingInterfaceRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateDeviceSwitchRoutingInterfaceRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateDeviceSwitchRoutingInterfaceRequest is not found in the empty JSON string", CreateDeviceSwitchRoutingInterfaceRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateDeviceSwitchRoutingInterfaceRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateDeviceSwitchRoutingInterfaceRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("defaultGateway") != null && !jsonObj.get("defaultGateway").isJsonNull()) && !jsonObj.get("defaultGateway").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `defaultGateway` to be a primitive type in the JSON string but got `%s`", jsonObj.get("defaultGateway").toString()));
      }
      if ((jsonObj.get("interfaceIp") != null && !jsonObj.get("interfaceIp").isJsonNull()) && !jsonObj.get("interfaceIp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `interfaceIp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("interfaceIp").toString()));
      }
      // validate the optional field `ipv6`
      if (jsonObj.get("ipv6") != null && !jsonObj.get("ipv6").isJsonNull()) {
        CreateDeviceSwitchRoutingInterfaceRequestIpv6.validateJsonElement(jsonObj.get("ipv6"));
      }
      if ((jsonObj.get("multicastRouting") != null && !jsonObj.get("multicastRouting").isJsonNull()) && !jsonObj.get("multicastRouting").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `multicastRouting` to be a primitive type in the JSON string but got `%s`", jsonObj.get("multicastRouting").toString()));
      }
      // validate the optional field `multicastRouting`
      if (jsonObj.get("multicastRouting") != null && !jsonObj.get("multicastRouting").isJsonNull()) {
        MulticastRoutingEnum.validateJsonElement(jsonObj.get("multicastRouting"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `ospfSettings`
      if (jsonObj.get("ospfSettings") != null && !jsonObj.get("ospfSettings").isJsonNull()) {
        CreateDeviceSwitchRoutingInterfaceRequestOspfSettings.validateJsonElement(jsonObj.get("ospfSettings"));
      }
      // validate the optional field `ospfV3`
      if (jsonObj.get("ospfV3") != null && !jsonObj.get("ospfV3").isJsonNull()) {
        CreateDeviceSwitchRoutingInterfaceRequestOspfV3.validateJsonElement(jsonObj.get("ospfV3"));
      }
      if ((jsonObj.get("subnet") != null && !jsonObj.get("subnet").isJsonNull()) && !jsonObj.get("subnet").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subnet` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subnet").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateDeviceSwitchRoutingInterfaceRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateDeviceSwitchRoutingInterfaceRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateDeviceSwitchRoutingInterfaceRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateDeviceSwitchRoutingInterfaceRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateDeviceSwitchRoutingInterfaceRequest>() {
           @Override
           public void write(JsonWriter out, CreateDeviceSwitchRoutingInterfaceRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateDeviceSwitchRoutingInterfaceRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateDeviceSwitchRoutingInterfaceRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateDeviceSwitchRoutingInterfaceRequest
   * @throws IOException if the JSON string is invalid with respect to CreateDeviceSwitchRoutingInterfaceRequest
   */
  public static CreateDeviceSwitchRoutingInterfaceRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateDeviceSwitchRoutingInterfaceRequest.class);
  }

  /**
   * Convert an instance of CreateDeviceSwitchRoutingInterfaceRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

