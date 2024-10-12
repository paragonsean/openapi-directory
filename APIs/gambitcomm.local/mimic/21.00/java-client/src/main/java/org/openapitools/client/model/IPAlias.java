/*
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
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
 * IPAlias
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:08.940356-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IPAlias {
  public static final String SERIALIZED_NAME_I_P = "IP";
  @SerializedName(SERIALIZED_NAME_I_P)
  private String IP;

  public static final String SERIALIZED_NAME_INTERFACE = "interface";
  @SerializedName(SERIALIZED_NAME_INTERFACE)
  private String _interface;

  public static final String SERIALIZED_NAME_MASK = "mask";
  @SerializedName(SERIALIZED_NAME_MASK)
  private String mask;

  public static final String SERIALIZED_NAME_PORT = "port";
  @SerializedName(SERIALIZED_NAME_PORT)
  private Integer port;

  public IPAlias() {
  }

  public IPAlias IP(String IP) {
    this.IP = IP;
    return this;
  }

  /**
   * Get IP
   * @return IP
   */
  @javax.annotation.Nullable
  public String getIP() {
    return IP;
  }

  public void setIP(String IP) {
    this.IP = IP;
  }


  public IPAlias _interface(String _interface) {
    this._interface = _interface;
    return this;
  }

  /**
   * Get _interface
   * @return _interface
   */
  @javax.annotation.Nullable
  public String getInterface() {
    return _interface;
  }

  public void setInterface(String _interface) {
    this._interface = _interface;
  }


  public IPAlias mask(String mask) {
    this.mask = mask;
    return this;
  }

  /**
   * Get mask
   * @return mask
   */
  @javax.annotation.Nullable
  public String getMask() {
    return mask;
  }

  public void setMask(String mask) {
    this.mask = mask;
  }


  public IPAlias port(Integer port) {
    this.port = port;
    return this;
  }

  /**
   * Get port
   * @return port
   */
  @javax.annotation.Nullable
  public Integer getPort() {
    return port;
  }

  public void setPort(Integer port) {
    this.port = port;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IPAlias ipAlias = (IPAlias) o;
    return Objects.equals(this.IP, ipAlias.IP) &&
        Objects.equals(this._interface, ipAlias._interface) &&
        Objects.equals(this.mask, ipAlias.mask) &&
        Objects.equals(this.port, ipAlias.port);
  }

  @Override
  public int hashCode() {
    return Objects.hash(IP, _interface, mask, port);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IPAlias {\n");
    sb.append("    IP: ").append(toIndentedString(IP)).append("\n");
    sb.append("    _interface: ").append(toIndentedString(_interface)).append("\n");
    sb.append("    mask: ").append(toIndentedString(mask)).append("\n");
    sb.append("    port: ").append(toIndentedString(port)).append("\n");
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
    openapiFields.add("IP");
    openapiFields.add("interface");
    openapiFields.add("mask");
    openapiFields.add("port");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IPAlias
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IPAlias.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IPAlias is not found in the empty JSON string", IPAlias.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IPAlias.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IPAlias` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("IP") != null && !jsonObj.get("IP").isJsonNull()) && !jsonObj.get("IP").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `IP` to be a primitive type in the JSON string but got `%s`", jsonObj.get("IP").toString()));
      }
      if ((jsonObj.get("interface") != null && !jsonObj.get("interface").isJsonNull()) && !jsonObj.get("interface").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `interface` to be a primitive type in the JSON string but got `%s`", jsonObj.get("interface").toString()));
      }
      if ((jsonObj.get("mask") != null && !jsonObj.get("mask").isJsonNull()) && !jsonObj.get("mask").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mask` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mask").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IPAlias.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IPAlias' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IPAlias> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IPAlias.class));

       return (TypeAdapter<T>) new TypeAdapter<IPAlias>() {
           @Override
           public void write(JsonWriter out, IPAlias value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IPAlias read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IPAlias given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IPAlias
   * @throws IOException if the JSON string is invalid with respect to IPAlias
   */
  public static IPAlias fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IPAlias.class);
  }

  /**
   * Convert an instance of IPAlias to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

