/*
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.BaseEntity;
import org.openapitools.client.model.EntityType;
import org.openapitools.client.model.IpV4Address;
import org.openapitools.client.model.Reference;
import org.openapitools.client.model.RuleSet;

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
 * BaseVirtualMachine
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:28.864194-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BaseVirtualMachine extends BaseEntity {
  public static final String SERIALIZED_NAME_DEFAULT_GATEWAY = "default_gateway";
  @SerializedName(SERIALIZED_NAME_DEFAULT_GATEWAY)
  private String defaultGateway;

  public static final String SERIALIZED_NAME_DESTINATION_FIREWALL_RULES = "destination_firewall_rules";
  @SerializedName(SERIALIZED_NAME_DESTINATION_FIREWALL_RULES)
  private List<RuleSet> destinationFirewallRules = new ArrayList<>();

  public static final String SERIALIZED_NAME_IP_ADDRESSES = "ip_addresses";
  @SerializedName(SERIALIZED_NAME_IP_ADDRESSES)
  private List<IpV4Address> ipAddresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_IP_SETS = "ip_sets";
  @SerializedName(SERIALIZED_NAME_IP_SETS)
  private List<Reference> ipSets = new ArrayList<>();

  public static final String SERIALIZED_NAME_SECURITY_GROUPS = "security_groups";
  @SerializedName(SERIALIZED_NAME_SECURITY_GROUPS)
  private List<Reference> securityGroups = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOURCE_FIREWALL_RULES = "source_firewall_rules";
  @SerializedName(SERIALIZED_NAME_SOURCE_FIREWALL_RULES)
  private List<RuleSet> sourceFirewallRules = new ArrayList<>();

  public static final String SERIALIZED_NAME_VNICS = "vnics";
  @SerializedName(SERIALIZED_NAME_VNICS)
  private List<Reference> vnics = new ArrayList<>();

  public BaseVirtualMachine() {
    this.entityType = this.getClass().getSimpleName();
  }

  public BaseVirtualMachine defaultGateway(String defaultGateway) {
    this.defaultGateway = defaultGateway;
    return this;
  }

  /**
   * Get defaultGateway
   * @return defaultGateway
   */
  @javax.annotation.Nullable
  public String getDefaultGateway() {
    return defaultGateway;
  }

  public void setDefaultGateway(String defaultGateway) {
    this.defaultGateway = defaultGateway;
  }


  public BaseVirtualMachine destinationFirewallRules(List<RuleSet> destinationFirewallRules) {
    this.destinationFirewallRules = destinationFirewallRules;
    return this;
  }

  public BaseVirtualMachine addDestinationFirewallRulesItem(RuleSet destinationFirewallRulesItem) {
    if (this.destinationFirewallRules == null) {
      this.destinationFirewallRules = new ArrayList<>();
    }
    this.destinationFirewallRules.add(destinationFirewallRulesItem);
    return this;
  }

  /**
   * Get destinationFirewallRules
   * @return destinationFirewallRules
   */
  @javax.annotation.Nullable
  public List<RuleSet> getDestinationFirewallRules() {
    return destinationFirewallRules;
  }

  public void setDestinationFirewallRules(List<RuleSet> destinationFirewallRules) {
    this.destinationFirewallRules = destinationFirewallRules;
  }


  public BaseVirtualMachine ipAddresses(List<IpV4Address> ipAddresses) {
    this.ipAddresses = ipAddresses;
    return this;
  }

  public BaseVirtualMachine addIpAddressesItem(IpV4Address ipAddressesItem) {
    if (this.ipAddresses == null) {
      this.ipAddresses = new ArrayList<>();
    }
    this.ipAddresses.add(ipAddressesItem);
    return this;
  }

  /**
   * Get ipAddresses
   * @return ipAddresses
   */
  @javax.annotation.Nullable
  public List<IpV4Address> getIpAddresses() {
    return ipAddresses;
  }

  public void setIpAddresses(List<IpV4Address> ipAddresses) {
    this.ipAddresses = ipAddresses;
  }


  public BaseVirtualMachine ipSets(List<Reference> ipSets) {
    this.ipSets = ipSets;
    return this;
  }

  public BaseVirtualMachine addIpSetsItem(Reference ipSetsItem) {
    if (this.ipSets == null) {
      this.ipSets = new ArrayList<>();
    }
    this.ipSets.add(ipSetsItem);
    return this;
  }

  /**
   * Get ipSets
   * @return ipSets
   */
  @javax.annotation.Nullable
  public List<Reference> getIpSets() {
    return ipSets;
  }

  public void setIpSets(List<Reference> ipSets) {
    this.ipSets = ipSets;
  }


  public BaseVirtualMachine securityGroups(List<Reference> securityGroups) {
    this.securityGroups = securityGroups;
    return this;
  }

  public BaseVirtualMachine addSecurityGroupsItem(Reference securityGroupsItem) {
    if (this.securityGroups == null) {
      this.securityGroups = new ArrayList<>();
    }
    this.securityGroups.add(securityGroupsItem);
    return this;
  }

  /**
   * Get securityGroups
   * @return securityGroups
   */
  @javax.annotation.Nullable
  public List<Reference> getSecurityGroups() {
    return securityGroups;
  }

  public void setSecurityGroups(List<Reference> securityGroups) {
    this.securityGroups = securityGroups;
  }


  public BaseVirtualMachine sourceFirewallRules(List<RuleSet> sourceFirewallRules) {
    this.sourceFirewallRules = sourceFirewallRules;
    return this;
  }

  public BaseVirtualMachine addSourceFirewallRulesItem(RuleSet sourceFirewallRulesItem) {
    if (this.sourceFirewallRules == null) {
      this.sourceFirewallRules = new ArrayList<>();
    }
    this.sourceFirewallRules.add(sourceFirewallRulesItem);
    return this;
  }

  /**
   * Get sourceFirewallRules
   * @return sourceFirewallRules
   */
  @javax.annotation.Nullable
  public List<RuleSet> getSourceFirewallRules() {
    return sourceFirewallRules;
  }

  public void setSourceFirewallRules(List<RuleSet> sourceFirewallRules) {
    this.sourceFirewallRules = sourceFirewallRules;
  }


  public BaseVirtualMachine vnics(List<Reference> vnics) {
    this.vnics = vnics;
    return this;
  }

  public BaseVirtualMachine addVnicsItem(Reference vnicsItem) {
    if (this.vnics == null) {
      this.vnics = new ArrayList<>();
    }
    this.vnics.add(vnicsItem);
    return this;
  }

  /**
   * Get vnics
   * @return vnics
   */
  @javax.annotation.Nullable
  public List<Reference> getVnics() {
    return vnics;
  }

  public void setVnics(List<Reference> vnics) {
    this.vnics = vnics;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BaseVirtualMachine baseVirtualMachine = (BaseVirtualMachine) o;
    return Objects.equals(this.defaultGateway, baseVirtualMachine.defaultGateway) &&
        Objects.equals(this.destinationFirewallRules, baseVirtualMachine.destinationFirewallRules) &&
        Objects.equals(this.ipAddresses, baseVirtualMachine.ipAddresses) &&
        Objects.equals(this.ipSets, baseVirtualMachine.ipSets) &&
        Objects.equals(this.securityGroups, baseVirtualMachine.securityGroups) &&
        Objects.equals(this.sourceFirewallRules, baseVirtualMachine.sourceFirewallRules) &&
        Objects.equals(this.vnics, baseVirtualMachine.vnics) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(defaultGateway, destinationFirewallRules, ipAddresses, ipSets, securityGroups, sourceFirewallRules, vnics, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BaseVirtualMachine {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    defaultGateway: ").append(toIndentedString(defaultGateway)).append("\n");
    sb.append("    destinationFirewallRules: ").append(toIndentedString(destinationFirewallRules)).append("\n");
    sb.append("    ipAddresses: ").append(toIndentedString(ipAddresses)).append("\n");
    sb.append("    ipSets: ").append(toIndentedString(ipSets)).append("\n");
    sb.append("    securityGroups: ").append(toIndentedString(securityGroups)).append("\n");
    sb.append("    sourceFirewallRules: ").append(toIndentedString(sourceFirewallRules)).append("\n");
    sb.append("    vnics: ").append(toIndentedString(vnics)).append("\n");
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
    openapiFields.add("entity_id");
    openapiFields.add("entity_type");
    openapiFields.add("name");
    openapiFields.add("default_gateway");
    openapiFields.add("destination_firewall_rules");
    openapiFields.add("ip_addresses");
    openapiFields.add("ip_sets");
    openapiFields.add("security_groups");
    openapiFields.add("source_firewall_rules");
    openapiFields.add("vnics");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BaseVirtualMachine
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BaseVirtualMachine.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BaseVirtualMachine is not found in the empty JSON string", BaseVirtualMachine.openapiRequiredFields.toString()));
        }
      }

      String discriminatorValue = jsonElement.getAsJsonObject().get("entity_type").getAsString();
      switch (discriminatorValue) {
        case "EC2Instance":
          EC2Instance.validateJsonElement(jsonElement);
          break;
        case "VirtualMachine":
          VirtualMachine.validateJsonElement(jsonElement);
          break;
        default:
          throw new IllegalArgumentException(String.format("The value of the `entity_type` field `%s` does not match any key defined in the discriminator's mapping.", discriminatorValue));
      }
  }


  /**
   * Create an instance of BaseVirtualMachine given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BaseVirtualMachine
   * @throws IOException if the JSON string is invalid with respect to BaseVirtualMachine
   */
  public static BaseVirtualMachine fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BaseVirtualMachine.class);
  }

  /**
   * Convert an instance of BaseVirtualMachine to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

