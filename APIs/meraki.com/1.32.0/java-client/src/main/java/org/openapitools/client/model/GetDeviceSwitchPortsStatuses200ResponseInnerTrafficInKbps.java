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
 * A breakdown of the average speed of data that has passed through this port during the timespan.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps {
  public static final String SERIALIZED_NAME_RECV = "recv";
  @SerializedName(SERIALIZED_NAME_RECV)
  private Float recv;

  public static final String SERIALIZED_NAME_SENT = "sent";
  @SerializedName(SERIALIZED_NAME_SENT)
  private Float sent;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Float total;

  public GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps() {
  }

  public GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps recv(Float recv) {
    this.recv = recv;
    return this;
  }

  /**
   * The average speed of the data received (in kilobits-per-second).
   * @return recv
   */
  @javax.annotation.Nullable
  public Float getRecv() {
    return recv;
  }

  public void setRecv(Float recv) {
    this.recv = recv;
  }


  public GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps sent(Float sent) {
    this.sent = sent;
    return this;
  }

  /**
   * The average speed of the data sent (in kilobits-per-second).
   * @return sent
   */
  @javax.annotation.Nullable
  public Float getSent() {
    return sent;
  }

  public void setSent(Float sent) {
    this.sent = sent;
  }


  public GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps total(Float total) {
    this.total = total;
    return this;
  }

  /**
   * The average speed of the data sent and received (in kilobits-per-second).
   * @return total
   */
  @javax.annotation.Nullable
  public Float getTotal() {
    return total;
  }

  public void setTotal(Float total) {
    this.total = total;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps getDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps = (GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps) o;
    return Objects.equals(this.recv, getDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.recv) &&
        Objects.equals(this.sent, getDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.sent) &&
        Objects.equals(this.total, getDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.total);
  }

  @Override
  public int hashCode() {
    return Objects.hash(recv, sent, total);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps {\n");
    sb.append("    recv: ").append(toIndentedString(recv)).append("\n");
    sb.append("    sent: ").append(toIndentedString(sent)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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
    openapiFields.add("recv");
    openapiFields.add("sent");
    openapiFields.add("total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps is not found in the empty JSON string", GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.class));

       return (TypeAdapter<T>) new TypeAdapter<GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps>() {
           @Override
           public void write(JsonWriter out, GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps
   * @throws IOException if the JSON string is invalid with respect to GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps
   */
  public static GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps.class);
  }

  /**
   * Convert an instance of GetDeviceSwitchPortsStatuses200ResponseInnerTrafficInKbps to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

