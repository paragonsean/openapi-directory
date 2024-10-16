/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
import java.util.HashMap;
import java.util.Map;

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
 * IdentityProviderRepresentation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IdentityProviderRepresentation {
  public static final String SERIALIZED_NAME_ADD_READ_TOKEN_ROLE_ON_CREATE = "addReadTokenRoleOnCreate";
  @SerializedName(SERIALIZED_NAME_ADD_READ_TOKEN_ROLE_ON_CREATE)
  private Boolean addReadTokenRoleOnCreate;

  public static final String SERIALIZED_NAME_ALIAS = "alias";
  @SerializedName(SERIALIZED_NAME_ALIAS)
  private String alias;

  public static final String SERIALIZED_NAME_CONFIG = "config";
  @SerializedName(SERIALIZED_NAME_CONFIG)
  private Map<String, Object> config = new HashMap<>();

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled;

  public static final String SERIALIZED_NAME_FIRST_BROKER_LOGIN_FLOW_ALIAS = "firstBrokerLoginFlowAlias";
  @SerializedName(SERIALIZED_NAME_FIRST_BROKER_LOGIN_FLOW_ALIAS)
  private String firstBrokerLoginFlowAlias;

  public static final String SERIALIZED_NAME_INTERNAL_ID = "internalId";
  @SerializedName(SERIALIZED_NAME_INTERNAL_ID)
  private String internalId;

  public static final String SERIALIZED_NAME_LINK_ONLY = "linkOnly";
  @SerializedName(SERIALIZED_NAME_LINK_ONLY)
  private Boolean linkOnly;

  public static final String SERIALIZED_NAME_POST_BROKER_LOGIN_FLOW_ALIAS = "postBrokerLoginFlowAlias";
  @SerializedName(SERIALIZED_NAME_POST_BROKER_LOGIN_FLOW_ALIAS)
  private String postBrokerLoginFlowAlias;

  public static final String SERIALIZED_NAME_PROVIDER_ID = "providerId";
  @SerializedName(SERIALIZED_NAME_PROVIDER_ID)
  private String providerId;

  public static final String SERIALIZED_NAME_STORE_TOKEN = "storeToken";
  @SerializedName(SERIALIZED_NAME_STORE_TOKEN)
  private Boolean storeToken;

  public static final String SERIALIZED_NAME_TRUST_EMAIL = "trustEmail";
  @SerializedName(SERIALIZED_NAME_TRUST_EMAIL)
  private Boolean trustEmail;

  public IdentityProviderRepresentation() {
  }

  public IdentityProviderRepresentation addReadTokenRoleOnCreate(Boolean addReadTokenRoleOnCreate) {
    this.addReadTokenRoleOnCreate = addReadTokenRoleOnCreate;
    return this;
  }

  /**
   * Get addReadTokenRoleOnCreate
   * @return addReadTokenRoleOnCreate
   */
  @javax.annotation.Nullable
  public Boolean getAddReadTokenRoleOnCreate() {
    return addReadTokenRoleOnCreate;
  }

  public void setAddReadTokenRoleOnCreate(Boolean addReadTokenRoleOnCreate) {
    this.addReadTokenRoleOnCreate = addReadTokenRoleOnCreate;
  }


  public IdentityProviderRepresentation alias(String alias) {
    this.alias = alias;
    return this;
  }

  /**
   * Get alias
   * @return alias
   */
  @javax.annotation.Nullable
  public String getAlias() {
    return alias;
  }

  public void setAlias(String alias) {
    this.alias = alias;
  }


  public IdentityProviderRepresentation config(Map<String, Object> config) {
    this.config = config;
    return this;
  }

  public IdentityProviderRepresentation putConfigItem(String key, Object configItem) {
    if (this.config == null) {
      this.config = new HashMap<>();
    }
    this.config.put(key, configItem);
    return this;
  }

  /**
   * Get config
   * @return config
   */
  @javax.annotation.Nullable
  public Map<String, Object> getConfig() {
    return config;
  }

  public void setConfig(Map<String, Object> config) {
    this.config = config;
  }


  public IdentityProviderRepresentation displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * Get displayName
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  public IdentityProviderRepresentation enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * Get enabled
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public IdentityProviderRepresentation firstBrokerLoginFlowAlias(String firstBrokerLoginFlowAlias) {
    this.firstBrokerLoginFlowAlias = firstBrokerLoginFlowAlias;
    return this;
  }

  /**
   * Get firstBrokerLoginFlowAlias
   * @return firstBrokerLoginFlowAlias
   */
  @javax.annotation.Nullable
  public String getFirstBrokerLoginFlowAlias() {
    return firstBrokerLoginFlowAlias;
  }

  public void setFirstBrokerLoginFlowAlias(String firstBrokerLoginFlowAlias) {
    this.firstBrokerLoginFlowAlias = firstBrokerLoginFlowAlias;
  }


  public IdentityProviderRepresentation internalId(String internalId) {
    this.internalId = internalId;
    return this;
  }

  /**
   * Get internalId
   * @return internalId
   */
  @javax.annotation.Nullable
  public String getInternalId() {
    return internalId;
  }

  public void setInternalId(String internalId) {
    this.internalId = internalId;
  }


  public IdentityProviderRepresentation linkOnly(Boolean linkOnly) {
    this.linkOnly = linkOnly;
    return this;
  }

  /**
   * Get linkOnly
   * @return linkOnly
   */
  @javax.annotation.Nullable
  public Boolean getLinkOnly() {
    return linkOnly;
  }

  public void setLinkOnly(Boolean linkOnly) {
    this.linkOnly = linkOnly;
  }


  public IdentityProviderRepresentation postBrokerLoginFlowAlias(String postBrokerLoginFlowAlias) {
    this.postBrokerLoginFlowAlias = postBrokerLoginFlowAlias;
    return this;
  }

  /**
   * Get postBrokerLoginFlowAlias
   * @return postBrokerLoginFlowAlias
   */
  @javax.annotation.Nullable
  public String getPostBrokerLoginFlowAlias() {
    return postBrokerLoginFlowAlias;
  }

  public void setPostBrokerLoginFlowAlias(String postBrokerLoginFlowAlias) {
    this.postBrokerLoginFlowAlias = postBrokerLoginFlowAlias;
  }


  public IdentityProviderRepresentation providerId(String providerId) {
    this.providerId = providerId;
    return this;
  }

  /**
   * Get providerId
   * @return providerId
   */
  @javax.annotation.Nullable
  public String getProviderId() {
    return providerId;
  }

  public void setProviderId(String providerId) {
    this.providerId = providerId;
  }


  public IdentityProviderRepresentation storeToken(Boolean storeToken) {
    this.storeToken = storeToken;
    return this;
  }

  /**
   * Get storeToken
   * @return storeToken
   */
  @javax.annotation.Nullable
  public Boolean getStoreToken() {
    return storeToken;
  }

  public void setStoreToken(Boolean storeToken) {
    this.storeToken = storeToken;
  }


  public IdentityProviderRepresentation trustEmail(Boolean trustEmail) {
    this.trustEmail = trustEmail;
    return this;
  }

  /**
   * Get trustEmail
   * @return trustEmail
   */
  @javax.annotation.Nullable
  public Boolean getTrustEmail() {
    return trustEmail;
  }

  public void setTrustEmail(Boolean trustEmail) {
    this.trustEmail = trustEmail;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IdentityProviderRepresentation identityProviderRepresentation = (IdentityProviderRepresentation) o;
    return Objects.equals(this.addReadTokenRoleOnCreate, identityProviderRepresentation.addReadTokenRoleOnCreate) &&
        Objects.equals(this.alias, identityProviderRepresentation.alias) &&
        Objects.equals(this.config, identityProviderRepresentation.config) &&
        Objects.equals(this.displayName, identityProviderRepresentation.displayName) &&
        Objects.equals(this.enabled, identityProviderRepresentation.enabled) &&
        Objects.equals(this.firstBrokerLoginFlowAlias, identityProviderRepresentation.firstBrokerLoginFlowAlias) &&
        Objects.equals(this.internalId, identityProviderRepresentation.internalId) &&
        Objects.equals(this.linkOnly, identityProviderRepresentation.linkOnly) &&
        Objects.equals(this.postBrokerLoginFlowAlias, identityProviderRepresentation.postBrokerLoginFlowAlias) &&
        Objects.equals(this.providerId, identityProviderRepresentation.providerId) &&
        Objects.equals(this.storeToken, identityProviderRepresentation.storeToken) &&
        Objects.equals(this.trustEmail, identityProviderRepresentation.trustEmail);
  }

  @Override
  public int hashCode() {
    return Objects.hash(addReadTokenRoleOnCreate, alias, config, displayName, enabled, firstBrokerLoginFlowAlias, internalId, linkOnly, postBrokerLoginFlowAlias, providerId, storeToken, trustEmail);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IdentityProviderRepresentation {\n");
    sb.append("    addReadTokenRoleOnCreate: ").append(toIndentedString(addReadTokenRoleOnCreate)).append("\n");
    sb.append("    alias: ").append(toIndentedString(alias)).append("\n");
    sb.append("    config: ").append(toIndentedString(config)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    firstBrokerLoginFlowAlias: ").append(toIndentedString(firstBrokerLoginFlowAlias)).append("\n");
    sb.append("    internalId: ").append(toIndentedString(internalId)).append("\n");
    sb.append("    linkOnly: ").append(toIndentedString(linkOnly)).append("\n");
    sb.append("    postBrokerLoginFlowAlias: ").append(toIndentedString(postBrokerLoginFlowAlias)).append("\n");
    sb.append("    providerId: ").append(toIndentedString(providerId)).append("\n");
    sb.append("    storeToken: ").append(toIndentedString(storeToken)).append("\n");
    sb.append("    trustEmail: ").append(toIndentedString(trustEmail)).append("\n");
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
    openapiFields.add("addReadTokenRoleOnCreate");
    openapiFields.add("alias");
    openapiFields.add("config");
    openapiFields.add("displayName");
    openapiFields.add("enabled");
    openapiFields.add("firstBrokerLoginFlowAlias");
    openapiFields.add("internalId");
    openapiFields.add("linkOnly");
    openapiFields.add("postBrokerLoginFlowAlias");
    openapiFields.add("providerId");
    openapiFields.add("storeToken");
    openapiFields.add("trustEmail");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IdentityProviderRepresentation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IdentityProviderRepresentation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IdentityProviderRepresentation is not found in the empty JSON string", IdentityProviderRepresentation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IdentityProviderRepresentation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IdentityProviderRepresentation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("alias") != null && !jsonObj.get("alias").isJsonNull()) && !jsonObj.get("alias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alias").toString()));
      }
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      if ((jsonObj.get("firstBrokerLoginFlowAlias") != null && !jsonObj.get("firstBrokerLoginFlowAlias").isJsonNull()) && !jsonObj.get("firstBrokerLoginFlowAlias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstBrokerLoginFlowAlias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstBrokerLoginFlowAlias").toString()));
      }
      if ((jsonObj.get("internalId") != null && !jsonObj.get("internalId").isJsonNull()) && !jsonObj.get("internalId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `internalId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("internalId").toString()));
      }
      if ((jsonObj.get("postBrokerLoginFlowAlias") != null && !jsonObj.get("postBrokerLoginFlowAlias").isJsonNull()) && !jsonObj.get("postBrokerLoginFlowAlias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `postBrokerLoginFlowAlias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("postBrokerLoginFlowAlias").toString()));
      }
      if ((jsonObj.get("providerId") != null && !jsonObj.get("providerId").isJsonNull()) && !jsonObj.get("providerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `providerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("providerId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IdentityProviderRepresentation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IdentityProviderRepresentation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IdentityProviderRepresentation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IdentityProviderRepresentation.class));

       return (TypeAdapter<T>) new TypeAdapter<IdentityProviderRepresentation>() {
           @Override
           public void write(JsonWriter out, IdentityProviderRepresentation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IdentityProviderRepresentation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IdentityProviderRepresentation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IdentityProviderRepresentation
   * @throws IOException if the JSON string is invalid with respect to IdentityProviderRepresentation
   */
  public static IdentityProviderRepresentation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IdentityProviderRepresentation.class);
  }

  /**
   * Convert an instance of IdentityProviderRepresentation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

