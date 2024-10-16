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
 * UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner {
  public static final String SERIALIZED_NAME_COMMENT = "comment";
  @SerializedName(SERIALIZED_NAME_COMMENT)
  private String comment;

  public static final String SERIALIZED_NAME_DEST_CIDR = "destCidr";
  @SerializedName(SERIALIZED_NAME_DEST_CIDR)
  private String destCidr;

  public static final String SERIALIZED_NAME_DEST_PORT = "destPort";
  @SerializedName(SERIALIZED_NAME_DEST_PORT)
  private String destPort;

  /**
   * &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule
   */
  @JsonAdapter(PolicyEnum.Adapter.class)
  public enum PolicyEnum {
    ALLOW("allow"),
    
    DENY("deny");

    private String value;

    PolicyEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PolicyEnum fromValue(String value) {
      for (PolicyEnum b : PolicyEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PolicyEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PolicyEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PolicyEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PolicyEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PolicyEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_POLICY = "policy";
  @SerializedName(SERIALIZED_NAME_POLICY)
  private PolicyEnum policy;

  /**
   * The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39;, &#39;icmp6&#39; or &#39;any&#39;)
   */
  @JsonAdapter(ProtocolEnum.Adapter.class)
  public enum ProtocolEnum {
    ANY("any"),
    
    ICMP("icmp"),
    
    ICMP6("icmp6"),
    
    TCP("tcp"),
    
    UDP("udp");

    private String value;

    ProtocolEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProtocolEnum fromValue(String value) {
      for (ProtocolEnum b : ProtocolEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProtocolEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProtocolEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProtocolEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProtocolEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProtocolEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROTOCOL = "protocol";
  @SerializedName(SERIALIZED_NAME_PROTOCOL)
  private ProtocolEnum protocol;

  public static final String SERIALIZED_NAME_SRC_CIDR = "srcCidr";
  @SerializedName(SERIALIZED_NAME_SRC_CIDR)
  private String srcCidr;

  public static final String SERIALIZED_NAME_SRC_PORT = "srcPort";
  @SerializedName(SERIALIZED_NAME_SRC_PORT)
  private String srcPort;

  public static final String SERIALIZED_NAME_SYSLOG_ENABLED = "syslogEnabled";
  @SerializedName(SERIALIZED_NAME_SYSLOG_ENABLED)
  private Boolean syslogEnabled;

  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner() {
  }

  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner comment(String comment) {
    this.comment = comment;
    return this;
  }

  /**
   * Description of the rule (optional)
   * @return comment
   */
  @javax.annotation.Nullable
  public String getComment() {
    return comment;
  }

  public void setComment(String comment) {
    this.comment = comment;
  }


  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner destCidr(String destCidr) {
    this.destCidr = destCidr;
    return this;
  }

  /**
   * Comma-separated list of destination IP address(es) (in IP or CIDR notation), fully-qualified domain names (FQDN) or &#39;any&#39;
   * @return destCidr
   */
  @javax.annotation.Nonnull
  public String getDestCidr() {
    return destCidr;
  }

  public void setDestCidr(String destCidr) {
    this.destCidr = destCidr;
  }


  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner destPort(String destPort) {
    this.destPort = destPort;
    return this;
  }

  /**
   * Comma-separated list of destination port(s) (integer in the range 1-65535), or &#39;any&#39;
   * @return destPort
   */
  @javax.annotation.Nullable
  public String getDestPort() {
    return destPort;
  }

  public void setDestPort(String destPort) {
    this.destPort = destPort;
  }


  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner policy(PolicyEnum policy) {
    this.policy = policy;
    return this;
  }

  /**
   * &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule
   * @return policy
   */
  @javax.annotation.Nonnull
  public PolicyEnum getPolicy() {
    return policy;
  }

  public void setPolicy(PolicyEnum policy) {
    this.policy = policy;
  }


  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner protocol(ProtocolEnum protocol) {
    this.protocol = protocol;
    return this;
  }

  /**
   * The type of protocol (must be &#39;tcp&#39;, &#39;udp&#39;, &#39;icmp&#39;, &#39;icmp6&#39; or &#39;any&#39;)
   * @return protocol
   */
  @javax.annotation.Nonnull
  public ProtocolEnum getProtocol() {
    return protocol;
  }

  public void setProtocol(ProtocolEnum protocol) {
    this.protocol = protocol;
  }


  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner srcCidr(String srcCidr) {
    this.srcCidr = srcCidr;
    return this;
  }

  /**
   * Comma-separated list of source IP address(es) (in IP or CIDR notation), or &#39;any&#39; (note: FQDN not supported for source addresses)
   * @return srcCidr
   */
  @javax.annotation.Nonnull
  public String getSrcCidr() {
    return srcCidr;
  }

  public void setSrcCidr(String srcCidr) {
    this.srcCidr = srcCidr;
  }


  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner srcPort(String srcPort) {
    this.srcPort = srcPort;
    return this;
  }

  /**
   * Comma-separated list of source port(s) (integer in the range 1-65535), or &#39;any&#39;
   * @return srcPort
   */
  @javax.annotation.Nullable
  public String getSrcPort() {
    return srcPort;
  }

  public void setSrcPort(String srcPort) {
    this.srcPort = srcPort;
  }


  public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner syslogEnabled(Boolean syslogEnabled) {
    this.syslogEnabled = syslogEnabled;
    return this;
  }

  /**
   * Log this rule to syslog (true or false, boolean value) - only applicable if a syslog has been configured (optional)
   * @return syslogEnabled
   */
  @javax.annotation.Nullable
  public Boolean getSyslogEnabled() {
    return syslogEnabled;
  }

  public void setSyslogEnabled(Boolean syslogEnabled) {
    this.syslogEnabled = syslogEnabled;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner = (UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner) o;
    return Objects.equals(this.comment, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.comment) &&
        Objects.equals(this.destCidr, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.destCidr) &&
        Objects.equals(this.destPort, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.destPort) &&
        Objects.equals(this.policy, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.policy) &&
        Objects.equals(this.protocol, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.protocol) &&
        Objects.equals(this.srcCidr, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.srcCidr) &&
        Objects.equals(this.srcPort, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.srcPort) &&
        Objects.equals(this.syslogEnabled, updateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.syslogEnabled);
  }

  @Override
  public int hashCode() {
    return Objects.hash(comment, destCidr, destPort, policy, protocol, srcCidr, srcPort, syslogEnabled);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner {\n");
    sb.append("    comment: ").append(toIndentedString(comment)).append("\n");
    sb.append("    destCidr: ").append(toIndentedString(destCidr)).append("\n");
    sb.append("    destPort: ").append(toIndentedString(destPort)).append("\n");
    sb.append("    policy: ").append(toIndentedString(policy)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
    sb.append("    srcCidr: ").append(toIndentedString(srcCidr)).append("\n");
    sb.append("    srcPort: ").append(toIndentedString(srcPort)).append("\n");
    sb.append("    syslogEnabled: ").append(toIndentedString(syslogEnabled)).append("\n");
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
    openapiFields.add("comment");
    openapiFields.add("destCidr");
    openapiFields.add("destPort");
    openapiFields.add("policy");
    openapiFields.add("protocol");
    openapiFields.add("srcCidr");
    openapiFields.add("srcPort");
    openapiFields.add("syslogEnabled");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("destCidr");
    openapiRequiredFields.add("policy");
    openapiRequiredFields.add("protocol");
    openapiRequiredFields.add("srcCidr");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner is not found in the empty JSON string", UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("comment") != null && !jsonObj.get("comment").isJsonNull()) && !jsonObj.get("comment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comment").toString()));
      }
      if (!jsonObj.get("destCidr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `destCidr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("destCidr").toString()));
      }
      if ((jsonObj.get("destPort") != null && !jsonObj.get("destPort").isJsonNull()) && !jsonObj.get("destPort").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `destPort` to be a primitive type in the JSON string but got `%s`", jsonObj.get("destPort").toString()));
      }
      if (!jsonObj.get("policy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `policy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("policy").toString()));
      }
      // validate the required field `policy`
      PolicyEnum.validateJsonElement(jsonObj.get("policy"));
      if (!jsonObj.get("protocol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `protocol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("protocol").toString()));
      }
      // validate the required field `protocol`
      ProtocolEnum.validateJsonElement(jsonObj.get("protocol"));
      if (!jsonObj.get("srcCidr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `srcCidr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("srcCidr").toString()));
      }
      if ((jsonObj.get("srcPort") != null && !jsonObj.get("srcPort").isJsonNull()) && !jsonObj.get("srcPort").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `srcPort` to be a primitive type in the JSON string but got `%s`", jsonObj.get("srcPort").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner
   */
  public static UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner.class);
  }

  /**
   * Convert an instance of UpdateNetworkApplianceFirewallCellularFirewallRulesRequestRulesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

