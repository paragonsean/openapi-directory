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
import org.openapitools.client.model.GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies;

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
 * UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner {
  /**
   * [optional] The IKE version to be used for the IPsec VPN peer configuration. Defaults to &#39;1&#39; when omitted.
   */
  @JsonAdapter(IkeVersionEnum.Adapter.class)
  public enum IkeVersionEnum {
    _1("1"),
    
    _2("2");

    private String value;

    IkeVersionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static IkeVersionEnum fromValue(String value) {
      for (IkeVersionEnum b : IkeVersionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<IkeVersionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final IkeVersionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public IkeVersionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return IkeVersionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      IkeVersionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_IKE_VERSION = "ikeVersion";
  @SerializedName(SERIALIZED_NAME_IKE_VERSION)
  private IkeVersionEnum ikeVersion = IkeVersionEnum._1;

  public static final String SERIALIZED_NAME_IPSEC_POLICIES = "ipsecPolicies";
  @SerializedName(SERIALIZED_NAME_IPSEC_POLICIES)
  private GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies ipsecPolicies;

  public static final String SERIALIZED_NAME_IPSEC_POLICIES_PRESET = "ipsecPoliciesPreset";
  @SerializedName(SERIALIZED_NAME_IPSEC_POLICIES_PRESET)
  private String ipsecPoliciesPreset;

  public static final String SERIALIZED_NAME_LOCAL_ID = "localId";
  @SerializedName(SERIALIZED_NAME_LOCAL_ID)
  private String localId;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NETWORK_TAGS = "networkTags";
  @SerializedName(SERIALIZED_NAME_NETWORK_TAGS)
  private List<String> networkTags = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRIVATE_SUBNETS = "privateSubnets";
  @SerializedName(SERIALIZED_NAME_PRIVATE_SUBNETS)
  private List<String> privateSubnets = new ArrayList<>();

  public static final String SERIALIZED_NAME_PUBLIC_IP = "publicIp";
  @SerializedName(SERIALIZED_NAME_PUBLIC_IP)
  private String publicIp;

  public static final String SERIALIZED_NAME_REMOTE_ID = "remoteId";
  @SerializedName(SERIALIZED_NAME_REMOTE_ID)
  private String remoteId;

  public static final String SERIALIZED_NAME_SECRET = "secret";
  @SerializedName(SERIALIZED_NAME_SECRET)
  private String secret;

  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner() {
  }

  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner ikeVersion(IkeVersionEnum ikeVersion) {
    this.ikeVersion = ikeVersion;
    return this;
  }

  /**
   * [optional] The IKE version to be used for the IPsec VPN peer configuration. Defaults to &#39;1&#39; when omitted.
   * @return ikeVersion
   */
  @javax.annotation.Nullable
  public IkeVersionEnum getIkeVersion() {
    return ikeVersion;
  }

  public void setIkeVersion(IkeVersionEnum ikeVersion) {
    this.ikeVersion = ikeVersion;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner ipsecPolicies(GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies ipsecPolicies) {
    this.ipsecPolicies = ipsecPolicies;
    return this;
  }

  /**
   * Get ipsecPolicies
   * @return ipsecPolicies
   */
  @javax.annotation.Nullable
  public GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies getIpsecPolicies() {
    return ipsecPolicies;
  }

  public void setIpsecPolicies(GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies ipsecPolicies) {
    this.ipsecPolicies = ipsecPolicies;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner ipsecPoliciesPreset(String ipsecPoliciesPreset) {
    this.ipsecPoliciesPreset = ipsecPoliciesPreset;
    return this;
  }

  /**
   * One of the following available presets: &#39;default&#39;, &#39;aws&#39;, &#39;azure&#39;. If this is provided, the &#39;ipsecPolicies&#39; parameter is ignored.
   * @return ipsecPoliciesPreset
   */
  @javax.annotation.Nullable
  public String getIpsecPoliciesPreset() {
    return ipsecPoliciesPreset;
  }

  public void setIpsecPoliciesPreset(String ipsecPoliciesPreset) {
    this.ipsecPoliciesPreset = ipsecPoliciesPreset;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner localId(String localId) {
    this.localId = localId;
    return this;
  }

  /**
   * [optional] The local ID is used to identify the MX to the peer. This will apply to all MXs this peer applies to.
   * @return localId
   */
  @javax.annotation.Nullable
  public String getLocalId() {
    return localId;
  }

  public void setLocalId(String localId) {
    this.localId = localId;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the VPN peer
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner networkTags(List<String> networkTags) {
    this.networkTags = networkTags;
    return this;
  }

  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner addNetworkTagsItem(String networkTagsItem) {
    if (this.networkTags == null) {
      this.networkTags = new ArrayList<>();
    }
    this.networkTags.add(networkTagsItem);
    return this;
  }

  /**
   * A list of network tags that will connect with this peer. Use [&#39;all&#39;] for all networks. Use [&#39;none&#39;] for no networks. If not included, the default is [&#39;all&#39;].
   * @return networkTags
   */
  @javax.annotation.Nullable
  public List<String> getNetworkTags() {
    return networkTags;
  }

  public void setNetworkTags(List<String> networkTags) {
    this.networkTags = networkTags;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner privateSubnets(List<String> privateSubnets) {
    this.privateSubnets = privateSubnets;
    return this;
  }

  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner addPrivateSubnetsItem(String privateSubnetsItem) {
    if (this.privateSubnets == null) {
      this.privateSubnets = new ArrayList<>();
    }
    this.privateSubnets.add(privateSubnetsItem);
    return this;
  }

  /**
   * The list of the private subnets of the VPN peer
   * @return privateSubnets
   */
  @javax.annotation.Nonnull
  public List<String> getPrivateSubnets() {
    return privateSubnets;
  }

  public void setPrivateSubnets(List<String> privateSubnets) {
    this.privateSubnets = privateSubnets;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner publicIp(String publicIp) {
    this.publicIp = publicIp;
    return this;
  }

  /**
   * [optional] The public IP of the VPN peer
   * @return publicIp
   */
  @javax.annotation.Nullable
  public String getPublicIp() {
    return publicIp;
  }

  public void setPublicIp(String publicIp) {
    this.publicIp = publicIp;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner remoteId(String remoteId) {
    this.remoteId = remoteId;
    return this;
  }

  /**
   * [optional] The remote ID is used to identify the connecting VPN peer. This can either be a valid IPv4 Address, FQDN or User FQDN.
   * @return remoteId
   */
  @javax.annotation.Nullable
  public String getRemoteId() {
    return remoteId;
  }

  public void setRemoteId(String remoteId) {
    this.remoteId = remoteId;
  }


  public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner secret(String secret) {
    this.secret = secret;
    return this;
  }

  /**
   * The shared secret with the VPN peer
   * @return secret
   */
  @javax.annotation.Nonnull
  public String getSecret() {
    return secret;
  }

  public void setSecret(String secret) {
    this.secret = secret;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner = (UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner) o;
    return Objects.equals(this.ikeVersion, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.ikeVersion) &&
        Objects.equals(this.ipsecPolicies, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.ipsecPolicies) &&
        Objects.equals(this.ipsecPoliciesPreset, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.ipsecPoliciesPreset) &&
        Objects.equals(this.localId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.localId) &&
        Objects.equals(this.name, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.name) &&
        Objects.equals(this.networkTags, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.networkTags) &&
        Objects.equals(this.privateSubnets, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.privateSubnets) &&
        Objects.equals(this.publicIp, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.publicIp) &&
        Objects.equals(this.remoteId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.remoteId) &&
        Objects.equals(this.secret, updateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.secret);
  }

  @Override
  public int hashCode() {
    return Objects.hash(ikeVersion, ipsecPolicies, ipsecPoliciesPreset, localId, name, networkTags, privateSubnets, publicIp, remoteId, secret);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner {\n");
    sb.append("    ikeVersion: ").append(toIndentedString(ikeVersion)).append("\n");
    sb.append("    ipsecPolicies: ").append(toIndentedString(ipsecPolicies)).append("\n");
    sb.append("    ipsecPoliciesPreset: ").append(toIndentedString(ipsecPoliciesPreset)).append("\n");
    sb.append("    localId: ").append(toIndentedString(localId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    networkTags: ").append(toIndentedString(networkTags)).append("\n");
    sb.append("    privateSubnets: ").append(toIndentedString(privateSubnets)).append("\n");
    sb.append("    publicIp: ").append(toIndentedString(publicIp)).append("\n");
    sb.append("    remoteId: ").append(toIndentedString(remoteId)).append("\n");
    sb.append("    secret: ").append(toIndentedString(secret)).append("\n");
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
    openapiFields.add("ikeVersion");
    openapiFields.add("ipsecPolicies");
    openapiFields.add("ipsecPoliciesPreset");
    openapiFields.add("localId");
    openapiFields.add("name");
    openapiFields.add("networkTags");
    openapiFields.add("privateSubnets");
    openapiFields.add("publicIp");
    openapiFields.add("remoteId");
    openapiFields.add("secret");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("privateSubnets");
    openapiRequiredFields.add("secret");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner is not found in the empty JSON string", UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ikeVersion") != null && !jsonObj.get("ikeVersion").isJsonNull()) && !jsonObj.get("ikeVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ikeVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ikeVersion").toString()));
      }
      // validate the optional field `ikeVersion`
      if (jsonObj.get("ikeVersion") != null && !jsonObj.get("ikeVersion").isJsonNull()) {
        IkeVersionEnum.validateJsonElement(jsonObj.get("ikeVersion"));
      }
      // validate the optional field `ipsecPolicies`
      if (jsonObj.get("ipsecPolicies") != null && !jsonObj.get("ipsecPolicies").isJsonNull()) {
        GetOrganizationApplianceVpnThirdPartyVPNPeers200ResponsePeersInnerIpsecPolicies.validateJsonElement(jsonObj.get("ipsecPolicies"));
      }
      if ((jsonObj.get("ipsecPoliciesPreset") != null && !jsonObj.get("ipsecPoliciesPreset").isJsonNull()) && !jsonObj.get("ipsecPoliciesPreset").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ipsecPoliciesPreset` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ipsecPoliciesPreset").toString()));
      }
      if ((jsonObj.get("localId") != null && !jsonObj.get("localId").isJsonNull()) && !jsonObj.get("localId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `localId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("localId").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("networkTags") != null && !jsonObj.get("networkTags").isJsonNull() && !jsonObj.get("networkTags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `networkTags` to be an array in the JSON string but got `%s`", jsonObj.get("networkTags").toString()));
      }
      // ensure the required json array is present
      if (jsonObj.get("privateSubnets") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("privateSubnets").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `privateSubnets` to be an array in the JSON string but got `%s`", jsonObj.get("privateSubnets").toString()));
      }
      if ((jsonObj.get("publicIp") != null && !jsonObj.get("publicIp").isJsonNull()) && !jsonObj.get("publicIp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publicIp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publicIp").toString()));
      }
      if ((jsonObj.get("remoteId") != null && !jsonObj.get("remoteId").isJsonNull()) && !jsonObj.get("remoteId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `remoteId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("remoteId").toString()));
      }
      if (!jsonObj.get("secret").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secret` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secret").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner>() {
           @Override
           public void write(JsonWriter out, UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner
   * @throws IOException if the JSON string is invalid with respect to UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner
   */
  public static UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner.class);
  }

  /**
   * Convert an instance of UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequestPeersInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

