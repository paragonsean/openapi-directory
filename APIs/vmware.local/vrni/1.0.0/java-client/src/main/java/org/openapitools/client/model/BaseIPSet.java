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
import org.openapitools.client.model.IpAddressRange;
import org.openapitools.client.model.IpNumericRange;
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
 * BaseIPSet
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:28.864194-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BaseIPSet extends BaseEntity {
  public static final String SERIALIZED_NAME_DIRECT_DESTINATION_RULES = "direct_destination_rules";
  @SerializedName(SERIALIZED_NAME_DIRECT_DESTINATION_RULES)
  private List<RuleSet> directDestinationRules = new ArrayList<>();

  public static final String SERIALIZED_NAME_DIRECT_SOURCE_RULES = "direct_source_rules";
  @SerializedName(SERIALIZED_NAME_DIRECT_SOURCE_RULES)
  private List<RuleSet> directSourceRules = new ArrayList<>();

  public static final String SERIALIZED_NAME_INDIRECT_DESTINATION_RULES = "indirect_destination_rules";
  @SerializedName(SERIALIZED_NAME_INDIRECT_DESTINATION_RULES)
  private List<RuleSet> indirectDestinationRules = new ArrayList<>();

  public static final String SERIALIZED_NAME_INDIRECT_SOURCE_RULES = "indirect_source_rules";
  @SerializedName(SERIALIZED_NAME_INDIRECT_SOURCE_RULES)
  private List<RuleSet> indirectSourceRules = new ArrayList<>();

  public static final String SERIALIZED_NAME_IP_ADDRESSES = "ip_addresses";
  @SerializedName(SERIALIZED_NAME_IP_ADDRESSES)
  private List<IpV4Address> ipAddresses = new ArrayList<>();

  public static final String SERIALIZED_NAME_IP_NUMERIC_RANGES = "ip_numeric_ranges";
  @SerializedName(SERIALIZED_NAME_IP_NUMERIC_RANGES)
  private List<IpNumericRange> ipNumericRanges = new ArrayList<>();

  public static final String SERIALIZED_NAME_IP_RANGES = "ip_ranges";
  @SerializedName(SERIALIZED_NAME_IP_RANGES)
  private List<IpAddressRange> ipRanges = new ArrayList<>();

  public static final String SERIALIZED_NAME_PARENT_SECURITY_GROUPS = "parent_security_groups";
  @SerializedName(SERIALIZED_NAME_PARENT_SECURITY_GROUPS)
  private List<Reference> parentSecurityGroups = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRANSLATED_VM_COUNT = "translated_vm_count";
  @SerializedName(SERIALIZED_NAME_TRANSLATED_VM_COUNT)
  private Integer translatedVmCount;

  public static final String SERIALIZED_NAME_VENDOR = "vendor";
  @SerializedName(SERIALIZED_NAME_VENDOR)
  private String vendor;

  public static final String SERIALIZED_NAME_VENDOR_ID = "vendor_id";
  @SerializedName(SERIALIZED_NAME_VENDOR_ID)
  private String vendorId;

  public BaseIPSet() {
    this.entityType = this.getClass().getSimpleName();
  }

  public BaseIPSet directDestinationRules(List<RuleSet> directDestinationRules) {
    this.directDestinationRules = directDestinationRules;
    return this;
  }

  public BaseIPSet addDirectDestinationRulesItem(RuleSet directDestinationRulesItem) {
    if (this.directDestinationRules == null) {
      this.directDestinationRules = new ArrayList<>();
    }
    this.directDestinationRules.add(directDestinationRulesItem);
    return this;
  }

  /**
   * Get directDestinationRules
   * @return directDestinationRules
   */
  @javax.annotation.Nullable
  public List<RuleSet> getDirectDestinationRules() {
    return directDestinationRules;
  }

  public void setDirectDestinationRules(List<RuleSet> directDestinationRules) {
    this.directDestinationRules = directDestinationRules;
  }


  public BaseIPSet directSourceRules(List<RuleSet> directSourceRules) {
    this.directSourceRules = directSourceRules;
    return this;
  }

  public BaseIPSet addDirectSourceRulesItem(RuleSet directSourceRulesItem) {
    if (this.directSourceRules == null) {
      this.directSourceRules = new ArrayList<>();
    }
    this.directSourceRules.add(directSourceRulesItem);
    return this;
  }

  /**
   * Get directSourceRules
   * @return directSourceRules
   */
  @javax.annotation.Nullable
  public List<RuleSet> getDirectSourceRules() {
    return directSourceRules;
  }

  public void setDirectSourceRules(List<RuleSet> directSourceRules) {
    this.directSourceRules = directSourceRules;
  }


  public BaseIPSet indirectDestinationRules(List<RuleSet> indirectDestinationRules) {
    this.indirectDestinationRules = indirectDestinationRules;
    return this;
  }

  public BaseIPSet addIndirectDestinationRulesItem(RuleSet indirectDestinationRulesItem) {
    if (this.indirectDestinationRules == null) {
      this.indirectDestinationRules = new ArrayList<>();
    }
    this.indirectDestinationRules.add(indirectDestinationRulesItem);
    return this;
  }

  /**
   * Get indirectDestinationRules
   * @return indirectDestinationRules
   */
  @javax.annotation.Nullable
  public List<RuleSet> getIndirectDestinationRules() {
    return indirectDestinationRules;
  }

  public void setIndirectDestinationRules(List<RuleSet> indirectDestinationRules) {
    this.indirectDestinationRules = indirectDestinationRules;
  }


  public BaseIPSet indirectSourceRules(List<RuleSet> indirectSourceRules) {
    this.indirectSourceRules = indirectSourceRules;
    return this;
  }

  public BaseIPSet addIndirectSourceRulesItem(RuleSet indirectSourceRulesItem) {
    if (this.indirectSourceRules == null) {
      this.indirectSourceRules = new ArrayList<>();
    }
    this.indirectSourceRules.add(indirectSourceRulesItem);
    return this;
  }

  /**
   * Get indirectSourceRules
   * @return indirectSourceRules
   */
  @javax.annotation.Nullable
  public List<RuleSet> getIndirectSourceRules() {
    return indirectSourceRules;
  }

  public void setIndirectSourceRules(List<RuleSet> indirectSourceRules) {
    this.indirectSourceRules = indirectSourceRules;
  }


  public BaseIPSet ipAddresses(List<IpV4Address> ipAddresses) {
    this.ipAddresses = ipAddresses;
    return this;
  }

  public BaseIPSet addIpAddressesItem(IpV4Address ipAddressesItem) {
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


  public BaseIPSet ipNumericRanges(List<IpNumericRange> ipNumericRanges) {
    this.ipNumericRanges = ipNumericRanges;
    return this;
  }

  public BaseIPSet addIpNumericRangesItem(IpNumericRange ipNumericRangesItem) {
    if (this.ipNumericRanges == null) {
      this.ipNumericRanges = new ArrayList<>();
    }
    this.ipNumericRanges.add(ipNumericRangesItem);
    return this;
  }

  /**
   * Get ipNumericRanges
   * @return ipNumericRanges
   */
  @javax.annotation.Nullable
  public List<IpNumericRange> getIpNumericRanges() {
    return ipNumericRanges;
  }

  public void setIpNumericRanges(List<IpNumericRange> ipNumericRanges) {
    this.ipNumericRanges = ipNumericRanges;
  }


  public BaseIPSet ipRanges(List<IpAddressRange> ipRanges) {
    this.ipRanges = ipRanges;
    return this;
  }

  public BaseIPSet addIpRangesItem(IpAddressRange ipRangesItem) {
    if (this.ipRanges == null) {
      this.ipRanges = new ArrayList<>();
    }
    this.ipRanges.add(ipRangesItem);
    return this;
  }

  /**
   * Get ipRanges
   * @return ipRanges
   */
  @javax.annotation.Nullable
  public List<IpAddressRange> getIpRanges() {
    return ipRanges;
  }

  public void setIpRanges(List<IpAddressRange> ipRanges) {
    this.ipRanges = ipRanges;
  }


  public BaseIPSet parentSecurityGroups(List<Reference> parentSecurityGroups) {
    this.parentSecurityGroups = parentSecurityGroups;
    return this;
  }

  public BaseIPSet addParentSecurityGroupsItem(Reference parentSecurityGroupsItem) {
    if (this.parentSecurityGroups == null) {
      this.parentSecurityGroups = new ArrayList<>();
    }
    this.parentSecurityGroups.add(parentSecurityGroupsItem);
    return this;
  }

  /**
   * Get parentSecurityGroups
   * @return parentSecurityGroups
   */
  @javax.annotation.Nullable
  public List<Reference> getParentSecurityGroups() {
    return parentSecurityGroups;
  }

  public void setParentSecurityGroups(List<Reference> parentSecurityGroups) {
    this.parentSecurityGroups = parentSecurityGroups;
  }


  public BaseIPSet translatedVmCount(Integer translatedVmCount) {
    this.translatedVmCount = translatedVmCount;
    return this;
  }

  /**
   * Get translatedVmCount
   * @return translatedVmCount
   */
  @javax.annotation.Nullable
  public Integer getTranslatedVmCount() {
    return translatedVmCount;
  }

  public void setTranslatedVmCount(Integer translatedVmCount) {
    this.translatedVmCount = translatedVmCount;
  }


  public BaseIPSet vendor(String vendor) {
    this.vendor = vendor;
    return this;
  }

  /**
   * Get vendor
   * @return vendor
   */
  @javax.annotation.Nullable
  public String getVendor() {
    return vendor;
  }

  public void setVendor(String vendor) {
    this.vendor = vendor;
  }


  public BaseIPSet vendorId(String vendorId) {
    this.vendorId = vendorId;
    return this;
  }

  /**
   * Get vendorId
   * @return vendorId
   */
  @javax.annotation.Nullable
  public String getVendorId() {
    return vendorId;
  }

  public void setVendorId(String vendorId) {
    this.vendorId = vendorId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BaseIPSet baseIPSet = (BaseIPSet) o;
    return Objects.equals(this.directDestinationRules, baseIPSet.directDestinationRules) &&
        Objects.equals(this.directSourceRules, baseIPSet.directSourceRules) &&
        Objects.equals(this.indirectDestinationRules, baseIPSet.indirectDestinationRules) &&
        Objects.equals(this.indirectSourceRules, baseIPSet.indirectSourceRules) &&
        Objects.equals(this.ipAddresses, baseIPSet.ipAddresses) &&
        Objects.equals(this.ipNumericRanges, baseIPSet.ipNumericRanges) &&
        Objects.equals(this.ipRanges, baseIPSet.ipRanges) &&
        Objects.equals(this.parentSecurityGroups, baseIPSet.parentSecurityGroups) &&
        Objects.equals(this.translatedVmCount, baseIPSet.translatedVmCount) &&
        Objects.equals(this.vendor, baseIPSet.vendor) &&
        Objects.equals(this.vendorId, baseIPSet.vendorId) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(directDestinationRules, directSourceRules, indirectDestinationRules, indirectSourceRules, ipAddresses, ipNumericRanges, ipRanges, parentSecurityGroups, translatedVmCount, vendor, vendorId, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BaseIPSet {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    directDestinationRules: ").append(toIndentedString(directDestinationRules)).append("\n");
    sb.append("    directSourceRules: ").append(toIndentedString(directSourceRules)).append("\n");
    sb.append("    indirectDestinationRules: ").append(toIndentedString(indirectDestinationRules)).append("\n");
    sb.append("    indirectSourceRules: ").append(toIndentedString(indirectSourceRules)).append("\n");
    sb.append("    ipAddresses: ").append(toIndentedString(ipAddresses)).append("\n");
    sb.append("    ipNumericRanges: ").append(toIndentedString(ipNumericRanges)).append("\n");
    sb.append("    ipRanges: ").append(toIndentedString(ipRanges)).append("\n");
    sb.append("    parentSecurityGroups: ").append(toIndentedString(parentSecurityGroups)).append("\n");
    sb.append("    translatedVmCount: ").append(toIndentedString(translatedVmCount)).append("\n");
    sb.append("    vendor: ").append(toIndentedString(vendor)).append("\n");
    sb.append("    vendorId: ").append(toIndentedString(vendorId)).append("\n");
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
    openapiFields.add("direct_destination_rules");
    openapiFields.add("direct_source_rules");
    openapiFields.add("indirect_destination_rules");
    openapiFields.add("indirect_source_rules");
    openapiFields.add("ip_addresses");
    openapiFields.add("ip_numeric_ranges");
    openapiFields.add("ip_ranges");
    openapiFields.add("parent_security_groups");
    openapiFields.add("translated_vm_count");
    openapiFields.add("vendor");
    openapiFields.add("vendor_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BaseIPSet
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BaseIPSet.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BaseIPSet is not found in the empty JSON string", BaseIPSet.openapiRequiredFields.toString()));
        }
      }

      String discriminatorValue = jsonElement.getAsJsonObject().get("entity_type").getAsString();
      switch (discriminatorValue) {
        case "EC2IPSet":
          EC2IPSet.validateJsonElement(jsonElement);
          break;
        case "NSXIPSet":
          NSXIPSet.validateJsonElement(jsonElement);
          break;
        default:
          throw new IllegalArgumentException(String.format("The value of the `entity_type` field `%s` does not match any key defined in the discriminator's mapping.", discriminatorValue));
      }
  }


  /**
   * Create an instance of BaseIPSet given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BaseIPSet
   * @throws IOException if the JSON string is invalid with respect to BaseIPSet
   */
  public static BaseIPSet fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BaseIPSet.class);
  }

  /**
   * Convert an instance of BaseIPSet to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

