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
import java.util.Arrays;
import org.openapitools.client.model.CiscoSwitchType;
import org.openapitools.client.model.PasswordCredentials;

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
 * CiscoSwitchDataSourceRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:28.864194-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CiscoSwitchDataSourceRequest {
  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled = true;

  public static final String SERIALIZED_NAME_FQDN = "fqdn";
  @SerializedName(SERIALIZED_NAME_FQDN)
  private String fqdn;

  public static final String SERIALIZED_NAME_IP = "ip";
  @SerializedName(SERIALIZED_NAME_IP)
  private String ip;

  public static final String SERIALIZED_NAME_NICKNAME = "nickname";
  @SerializedName(SERIALIZED_NAME_NICKNAME)
  private String nickname;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_PROXY_ID = "proxy_id";
  @SerializedName(SERIALIZED_NAME_PROXY_ID)
  private String proxyId;

  public static final String SERIALIZED_NAME_CREDENTIALS = "credentials";
  @SerializedName(SERIALIZED_NAME_CREDENTIALS)
  private PasswordCredentials credentials;

  public static final String SERIALIZED_NAME_SWITCH_TYPE = "switch_type";
  @SerializedName(SERIALIZED_NAME_SWITCH_TYPE)
  private CiscoSwitchType switchType;

  public CiscoSwitchDataSourceRequest() {
  }

  public CiscoSwitchDataSourceRequest enabled(Boolean enabled) {
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


  public CiscoSwitchDataSourceRequest fqdn(String fqdn) {
    this.fqdn = fqdn;
    return this;
  }

  /**
   * Get fqdn
   * @return fqdn
   */
  @javax.annotation.Nullable
  public String getFqdn() {
    return fqdn;
  }

  public void setFqdn(String fqdn) {
    this.fqdn = fqdn;
  }


  public CiscoSwitchDataSourceRequest ip(String ip) {
    this.ip = ip;
    return this;
  }

  /**
   * Get ip
   * @return ip
   */
  @javax.annotation.Nullable
  public String getIp() {
    return ip;
  }

  public void setIp(String ip) {
    this.ip = ip;
  }


  public CiscoSwitchDataSourceRequest nickname(String nickname) {
    this.nickname = nickname;
    return this;
  }

  /**
   * Get nickname
   * @return nickname
   */
  @javax.annotation.Nonnull
  public String getNickname() {
    return nickname;
  }

  public void setNickname(String nickname) {
    this.nickname = nickname;
  }


  public CiscoSwitchDataSourceRequest notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * Get notes
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public CiscoSwitchDataSourceRequest proxyId(String proxyId) {
    this.proxyId = proxyId;
    return this;
  }

  /**
   * proxy vm which should register this vcenter
   * @return proxyId
   */
  @javax.annotation.Nonnull
  public String getProxyId() {
    return proxyId;
  }

  public void setProxyId(String proxyId) {
    this.proxyId = proxyId;
  }


  public CiscoSwitchDataSourceRequest credentials(PasswordCredentials credentials) {
    this.credentials = credentials;
    return this;
  }

  /**
   * Get credentials
   * @return credentials
   */
  @javax.annotation.Nullable
  public PasswordCredentials getCredentials() {
    return credentials;
  }

  public void setCredentials(PasswordCredentials credentials) {
    this.credentials = credentials;
  }


  public CiscoSwitchDataSourceRequest switchType(CiscoSwitchType switchType) {
    this.switchType = switchType;
    return this;
  }

  /**
   * Get switchType
   * @return switchType
   */
  @javax.annotation.Nullable
  public CiscoSwitchType getSwitchType() {
    return switchType;
  }

  public void setSwitchType(CiscoSwitchType switchType) {
    this.switchType = switchType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CiscoSwitchDataSourceRequest ciscoSwitchDataSourceRequest = (CiscoSwitchDataSourceRequest) o;
    return Objects.equals(this.enabled, ciscoSwitchDataSourceRequest.enabled) &&
        Objects.equals(this.fqdn, ciscoSwitchDataSourceRequest.fqdn) &&
        Objects.equals(this.ip, ciscoSwitchDataSourceRequest.ip) &&
        Objects.equals(this.nickname, ciscoSwitchDataSourceRequest.nickname) &&
        Objects.equals(this.notes, ciscoSwitchDataSourceRequest.notes) &&
        Objects.equals(this.proxyId, ciscoSwitchDataSourceRequest.proxyId) &&
        Objects.equals(this.credentials, ciscoSwitchDataSourceRequest.credentials) &&
        Objects.equals(this.switchType, ciscoSwitchDataSourceRequest.switchType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(enabled, fqdn, ip, nickname, notes, proxyId, credentials, switchType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CiscoSwitchDataSourceRequest {\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    fqdn: ").append(toIndentedString(fqdn)).append("\n");
    sb.append("    ip: ").append(toIndentedString(ip)).append("\n");
    sb.append("    nickname: ").append(toIndentedString(nickname)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    proxyId: ").append(toIndentedString(proxyId)).append("\n");
    sb.append("    credentials: ").append(toIndentedString(credentials)).append("\n");
    sb.append("    switchType: ").append(toIndentedString(switchType)).append("\n");
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
    openapiFields.add("enabled");
    openapiFields.add("fqdn");
    openapiFields.add("ip");
    openapiFields.add("nickname");
    openapiFields.add("notes");
    openapiFields.add("proxy_id");
    openapiFields.add("credentials");
    openapiFields.add("switch_type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("nickname");
    openapiRequiredFields.add("proxy_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CiscoSwitchDataSourceRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CiscoSwitchDataSourceRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CiscoSwitchDataSourceRequest is not found in the empty JSON string", CiscoSwitchDataSourceRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CiscoSwitchDataSourceRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CiscoSwitchDataSourceRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CiscoSwitchDataSourceRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("fqdn") != null && !jsonObj.get("fqdn").isJsonNull()) && !jsonObj.get("fqdn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fqdn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fqdn").toString()));
      }
      if ((jsonObj.get("ip") != null && !jsonObj.get("ip").isJsonNull()) && !jsonObj.get("ip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ip").toString()));
      }
      if (!jsonObj.get("nickname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nickname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nickname").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if (!jsonObj.get("proxy_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `proxy_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("proxy_id").toString()));
      }
      // validate the optional field `credentials`
      if (jsonObj.get("credentials") != null && !jsonObj.get("credentials").isJsonNull()) {
        PasswordCredentials.validateJsonElement(jsonObj.get("credentials"));
      }
      // validate the optional field `switch_type`
      if (jsonObj.get("switch_type") != null && !jsonObj.get("switch_type").isJsonNull()) {
        CiscoSwitchType.validateJsonElement(jsonObj.get("switch_type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CiscoSwitchDataSourceRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CiscoSwitchDataSourceRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CiscoSwitchDataSourceRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CiscoSwitchDataSourceRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CiscoSwitchDataSourceRequest>() {
           @Override
           public void write(JsonWriter out, CiscoSwitchDataSourceRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CiscoSwitchDataSourceRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CiscoSwitchDataSourceRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CiscoSwitchDataSourceRequest
   * @throws IOException if the JSON string is invalid with respect to CiscoSwitchDataSourceRequest
   */
  public static CiscoSwitchDataSourceRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CiscoSwitchDataSourceRequest.class);
  }

  /**
   * Convert an instance of CiscoSwitchDataSourceRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

