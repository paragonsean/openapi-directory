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
 * Secondary VPN concentrator settings. This is only used when two VPN concentrators are configured on the SSID.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkWirelessSsidVpnRequestFailover {
  public static final String SERIALIZED_NAME_HEARTBEAT_INTERVAL = "heartbeatInterval";
  @SerializedName(SERIALIZED_NAME_HEARTBEAT_INTERVAL)
  private Integer heartbeatInterval;

  public static final String SERIALIZED_NAME_IDLE_TIMEOUT = "idleTimeout";
  @SerializedName(SERIALIZED_NAME_IDLE_TIMEOUT)
  private Integer idleTimeout;

  public static final String SERIALIZED_NAME_REQUEST_IP = "requestIp";
  @SerializedName(SERIALIZED_NAME_REQUEST_IP)
  private String requestIp;

  public UpdateNetworkWirelessSsidVpnRequestFailover() {
  }

  public UpdateNetworkWirelessSsidVpnRequestFailover heartbeatInterval(Integer heartbeatInterval) {
    this.heartbeatInterval = heartbeatInterval;
    return this;
  }

  /**
   * Idle timer interval in seconds.
   * @return heartbeatInterval
   */
  @javax.annotation.Nullable
  public Integer getHeartbeatInterval() {
    return heartbeatInterval;
  }

  public void setHeartbeatInterval(Integer heartbeatInterval) {
    this.heartbeatInterval = heartbeatInterval;
  }


  public UpdateNetworkWirelessSsidVpnRequestFailover idleTimeout(Integer idleTimeout) {
    this.idleTimeout = idleTimeout;
    return this;
  }

  /**
   * Idle timer timeout in seconds.
   * @return idleTimeout
   */
  @javax.annotation.Nullable
  public Integer getIdleTimeout() {
    return idleTimeout;
  }

  public void setIdleTimeout(Integer idleTimeout) {
    this.idleTimeout = idleTimeout;
  }


  public UpdateNetworkWirelessSsidVpnRequestFailover requestIp(String requestIp) {
    this.requestIp = requestIp;
    return this;
  }

  /**
   * IP addressed reserved on DHCP server where SSID will terminate.
   * @return requestIp
   */
  @javax.annotation.Nullable
  public String getRequestIp() {
    return requestIp;
  }

  public void setRequestIp(String requestIp) {
    this.requestIp = requestIp;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkWirelessSsidVpnRequestFailover updateNetworkWirelessSsidVpnRequestFailover = (UpdateNetworkWirelessSsidVpnRequestFailover) o;
    return Objects.equals(this.heartbeatInterval, updateNetworkWirelessSsidVpnRequestFailover.heartbeatInterval) &&
        Objects.equals(this.idleTimeout, updateNetworkWirelessSsidVpnRequestFailover.idleTimeout) &&
        Objects.equals(this.requestIp, updateNetworkWirelessSsidVpnRequestFailover.requestIp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(heartbeatInterval, idleTimeout, requestIp);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkWirelessSsidVpnRequestFailover {\n");
    sb.append("    heartbeatInterval: ").append(toIndentedString(heartbeatInterval)).append("\n");
    sb.append("    idleTimeout: ").append(toIndentedString(idleTimeout)).append("\n");
    sb.append("    requestIp: ").append(toIndentedString(requestIp)).append("\n");
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
    openapiFields.add("heartbeatInterval");
    openapiFields.add("idleTimeout");
    openapiFields.add("requestIp");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkWirelessSsidVpnRequestFailover
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkWirelessSsidVpnRequestFailover.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkWirelessSsidVpnRequestFailover is not found in the empty JSON string", UpdateNetworkWirelessSsidVpnRequestFailover.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkWirelessSsidVpnRequestFailover.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkWirelessSsidVpnRequestFailover` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("requestIp") != null && !jsonObj.get("requestIp").isJsonNull()) && !jsonObj.get("requestIp").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `requestIp` to be a primitive type in the JSON string but got `%s`", jsonObj.get("requestIp").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkWirelessSsidVpnRequestFailover.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkWirelessSsidVpnRequestFailover' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkWirelessSsidVpnRequestFailover> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkWirelessSsidVpnRequestFailover.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkWirelessSsidVpnRequestFailover>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkWirelessSsidVpnRequestFailover value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkWirelessSsidVpnRequestFailover read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkWirelessSsidVpnRequestFailover given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkWirelessSsidVpnRequestFailover
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkWirelessSsidVpnRequestFailover
   */
  public static UpdateNetworkWirelessSsidVpnRequestFailover fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkWirelessSsidVpnRequestFailover.class);
  }

  /**
   * Convert an instance of UpdateNetworkWirelessSsidVpnRequestFailover to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

