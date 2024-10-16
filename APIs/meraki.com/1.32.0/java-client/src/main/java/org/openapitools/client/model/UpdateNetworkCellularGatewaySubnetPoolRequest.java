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
 * UpdateNetworkCellularGatewaySubnetPoolRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateNetworkCellularGatewaySubnetPoolRequest {
  public static final String SERIALIZED_NAME_CIDR = "cidr";
  @SerializedName(SERIALIZED_NAME_CIDR)
  private String cidr;

  public static final String SERIALIZED_NAME_MASK = "mask";
  @SerializedName(SERIALIZED_NAME_MASK)
  private Integer mask;

  public UpdateNetworkCellularGatewaySubnetPoolRequest() {
  }

  public UpdateNetworkCellularGatewaySubnetPoolRequest cidr(String cidr) {
    this.cidr = cidr;
    return this;
  }

  /**
   * CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.
   * @return cidr
   */
  @javax.annotation.Nullable
  public String getCidr() {
    return cidr;
  }

  public void setCidr(String cidr) {
    this.cidr = cidr;
  }


  public UpdateNetworkCellularGatewaySubnetPoolRequest mask(Integer mask) {
    this.mask = mask;
    return this;
  }

  /**
   * Mask used for the subnet of all MGs in  this network.
   * @return mask
   */
  @javax.annotation.Nullable
  public Integer getMask() {
    return mask;
  }

  public void setMask(Integer mask) {
    this.mask = mask;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateNetworkCellularGatewaySubnetPoolRequest updateNetworkCellularGatewaySubnetPoolRequest = (UpdateNetworkCellularGatewaySubnetPoolRequest) o;
    return Objects.equals(this.cidr, updateNetworkCellularGatewaySubnetPoolRequest.cidr) &&
        Objects.equals(this.mask, updateNetworkCellularGatewaySubnetPoolRequest.mask);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cidr, mask);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateNetworkCellularGatewaySubnetPoolRequest {\n");
    sb.append("    cidr: ").append(toIndentedString(cidr)).append("\n");
    sb.append("    mask: ").append(toIndentedString(mask)).append("\n");
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
    openapiFields.add("cidr");
    openapiFields.add("mask");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateNetworkCellularGatewaySubnetPoolRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateNetworkCellularGatewaySubnetPoolRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateNetworkCellularGatewaySubnetPoolRequest is not found in the empty JSON string", UpdateNetworkCellularGatewaySubnetPoolRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateNetworkCellularGatewaySubnetPoolRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateNetworkCellularGatewaySubnetPoolRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("cidr") != null && !jsonObj.get("cidr").isJsonNull()) && !jsonObj.get("cidr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cidr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cidr").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateNetworkCellularGatewaySubnetPoolRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateNetworkCellularGatewaySubnetPoolRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateNetworkCellularGatewaySubnetPoolRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateNetworkCellularGatewaySubnetPoolRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateNetworkCellularGatewaySubnetPoolRequest>() {
           @Override
           public void write(JsonWriter out, UpdateNetworkCellularGatewaySubnetPoolRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateNetworkCellularGatewaySubnetPoolRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateNetworkCellularGatewaySubnetPoolRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateNetworkCellularGatewaySubnetPoolRequest
   * @throws IOException if the JSON string is invalid with respect to UpdateNetworkCellularGatewaySubnetPoolRequest
   */
  public static UpdateNetworkCellularGatewaySubnetPoolRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateNetworkCellularGatewaySubnetPoolRequest.class);
  }

  /**
   * Convert an instance of UpdateNetworkCellularGatewaySubnetPoolRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

