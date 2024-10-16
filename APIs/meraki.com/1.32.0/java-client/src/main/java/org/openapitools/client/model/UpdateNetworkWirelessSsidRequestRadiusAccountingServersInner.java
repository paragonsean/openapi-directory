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
 * UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner {
  public static final String SERIALIZED_NAME_CA_CERTIFICATE = "caCertificate";
  @SerializedName(SERIALIZED_NAME_CA_CERTIFICATE)
  private String caCertificate;

  public static final String SERIALIZED_NAME_HOST = "host";
  @SerializedName(SERIALIZED_NAME_HOST)
  private String host;

  public static final String SERIALIZED_NAME_PORT = "port";
  @SerializedName(SERIALIZED_NAME_PORT)
  private Integer port;

  public static final String SERIALIZED_NAME_RADSEC_ENABLED = "radsecEnabled";
  @SerializedName(SERIALIZED_NAME_RADSEC_ENABLED)
  private Boolean radsecEnabled;

  public static final String SERIALIZED_NAME_SECRET = "secret";
  @SerializedName(SERIALIZED_NAME_SECRET)
  private String secret;

  public UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner() {
  }

  public UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner caCertificate(String caCertificate) {
    this.caCertificate = caCertificate;
    return this;
  }

  /**
   * Certificate used for authorization for the RADSEC Server
   * @return caCertificate
   */
  @javax.annotation.Nullable
  public String getCaCertificate() {
    return caCertificate;
  }

  public void setCaCertificate(String caCertificate) {
    this.caCertificate = caCertificate;
  }


  public UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner host(String host) {
    this.host = host;
    return this;
  }

  /**
   * IP address to which the APs will send RADIUS accounting messages
   * @return host
   */
  @javax.annotation.Nonnull
  public String getHost() {
    return host;
  }

  public void setHost(String host) {
    this.host = host;
  }


  public UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner port(Integer port) {
    this.port = port;
    return this;
  }

  /**
   * Port on the RADIUS server that is listening for accounting messages
   * @return port
   */
  @javax.annotation.Nullable
  public Integer getPort() {
    return port;
  }

  public void setPort(Integer port) {
    this.port = port;
  }


  public UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner radsecEnabled(Boolean radsecEnabled) {
    this.radsecEnabled = radsecEnabled;
    return this;
  }

  /**
   * Use RADSEC (TLS over TCP) to connect to this RADIUS accounting server. Requires radiusProxyEnabled.
   * @return radsecEnabled
   */
  @javax.annotation.Nullable
  public Boolean getRadsecEnabled() {
    return radsecEnabled;
  }

  public void setRadsecEnabled(Boolean radsecEnabled) {
    this.radsecEnabled = radsecEnabled;
  }


  public UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner secret(String secret) {
    this.secret = secret;
    return this;
  }

  /**
   * Shared key used to authenticate messages between the APs and RADIUS server
   * @return secret
   */
  @javax.annotation.Nullable
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
    UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner updateNetworkWirelessSsidRequestRadiusAccountingServersInner = (UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner) o;
    return Objects.equals(this.caCertificate, updateNetworkWirelessSsidRequestRadiusAccountingServersInner.caCertificate) &&
        Objects.equals(this.host, updateNetworkWirelessSsidRequestRadiusAccountingServersInner.host) &&
        Objects.equals(this.port, updateNetworkWirelessSsidRequestRadiusAccountingServersInner.port) &&
        Objects.equals(this.radsecEnabled, updateNetworkWirelessSsidRequestRadiusAccountingServersInner.radsecEnabled) &&
        Objects.equals(this.secret, updateNetworkWirelessSsidRequestRadiusAccountingServersInner.secret);
  }

  @Override
  public int hashCode() {
    return Objects.hash(caCertificate, host, port, radsecEnabled, secret);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner {\n");
    sb.append("    caCertificate: ").append(toIndentedString(caCertificate)).append("\n");
    sb.append("    host: ").append(toIndentedString(host)).append("\n");
    sb.append("    port: ").append(toIndentedString(port)).append("\n");
    sb.append("    radsecEnabled: ").append(toIndentedString(radsecEnabled)).append("\n");
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
    openapiFields.add("caCertificate");
    openapiFields.add("host");
    openapiFields.add("port");
    openapiFields.add("radsecEnabled");
    openapiFields.add("secret");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("host");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner is not found in the empty JSON string", UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("caCertificate") != null && !jsonObj.get("caCertificate").isJsonNull()) && !jsonObj.get("caCertificate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `caCertificate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("caCertificate").toString()));
      }
      if (!jsonObj.get("host").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `host` to be a primitive type in the JSON string but got `%s`", jsonObj.get("host").toString()));
      }
      if ((jsonObj.get("secret") != null && !jsonObj.get("secret").isJsonNull()) && !jsonObj.get("secret").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secret` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secret").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner
   */
  public static UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner.class);
  }

  /**
   * Convert an instance of UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

