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
 * UDP attributes of the packet.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp {
  public static final String SERIALIZED_NAME_CHECKSUM = "checksum";
  @SerializedName(SERIALIZED_NAME_CHECKSUM)
  private String checksum;

  public static final String SERIALIZED_NAME_LENGTH = "length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private Integer length;

  public GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp() {
  }

  public GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp checksum(String checksum) {
    this.checksum = checksum;
    return this;
  }

  /**
   * UDP checksum of the packet.
   * @return checksum
   */
  @javax.annotation.Nullable
  public String getChecksum() {
    return checksum;
  }

  public void setChecksum(String checksum) {
    this.checksum = checksum;
  }


  public GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp length(Integer length) {
    this.length = length;
    return this;
  }

  /**
   * UDP length of the packet.
   * @return length
   */
  @javax.annotation.Nullable
  public Integer getLength() {
    return length;
  }

  public void setLength(Integer length) {
    this.length = length;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp getNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp = (GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp) o;
    return Objects.equals(this.checksum, getNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.checksum) &&
        Objects.equals(this.length, getNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.length);
  }

  @Override
  public int hashCode() {
    return Objects.hash(checksum, length);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp {\n");
    sb.append("    checksum: ").append(toIndentedString(checksum)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
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
    openapiFields.add("checksum");
    openapiFields.add("length");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp is not found in the empty JSON string", GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("checksum") != null && !jsonObj.get("checksum").isJsonNull()) && !jsonObj.get("checksum").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checksum` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checksum").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp>() {
           @Override
           public void write(JsonWriter out, GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
   * @throws IOException if the JSON string is invalid with respect to GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp
   */
  public static GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp.class);
  }

  /**
   * Convert an instance of GetNetworkSwitchDhcpV4ServersSeen200ResponseInnerLastPacketUdp to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

