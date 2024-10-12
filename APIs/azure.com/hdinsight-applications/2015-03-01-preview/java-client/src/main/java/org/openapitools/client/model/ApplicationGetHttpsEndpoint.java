/*
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
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
 * Gets the application HTTP endpoints.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:19:25.528717-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ApplicationGetHttpsEndpoint {
  public static final String SERIALIZED_NAME_ACCESS_MODES = "accessModes";
  @SerializedName(SERIALIZED_NAME_ACCESS_MODES)
  private List<String> accessModes = new ArrayList<>();

  public static final String SERIALIZED_NAME_DESTINATION_PORT = "destinationPort";
  @SerializedName(SERIALIZED_NAME_DESTINATION_PORT)
  private Integer destinationPort;

  public static final String SERIALIZED_NAME_DISABLE_GATEWAY_AUTH = "disableGatewayAuth";
  @SerializedName(SERIALIZED_NAME_DISABLE_GATEWAY_AUTH)
  private Boolean disableGatewayAuth;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private String location;

  public static final String SERIALIZED_NAME_PUBLIC_PORT = "publicPort";
  @SerializedName(SERIALIZED_NAME_PUBLIC_PORT)
  private Integer publicPort;

  public static final String SERIALIZED_NAME_SUB_DOMAIN_SUFFIX = "subDomainSuffix";
  @SerializedName(SERIALIZED_NAME_SUB_DOMAIN_SUFFIX)
  private String subDomainSuffix;

  public ApplicationGetHttpsEndpoint() {
  }

  public ApplicationGetHttpsEndpoint accessModes(List<String> accessModes) {
    this.accessModes = accessModes;
    return this;
  }

  public ApplicationGetHttpsEndpoint addAccessModesItem(String accessModesItem) {
    if (this.accessModes == null) {
      this.accessModes = new ArrayList<>();
    }
    this.accessModes.add(accessModesItem);
    return this;
  }

  /**
   * The list of access modes for the application.
   * @return accessModes
   */
  @javax.annotation.Nullable
  public List<String> getAccessModes() {
    return accessModes;
  }

  public void setAccessModes(List<String> accessModes) {
    this.accessModes = accessModes;
  }


  public ApplicationGetHttpsEndpoint destinationPort(Integer destinationPort) {
    this.destinationPort = destinationPort;
    return this;
  }

  /**
   * The destination port to connect to.
   * @return destinationPort
   */
  @javax.annotation.Nullable
  public Integer getDestinationPort() {
    return destinationPort;
  }

  public void setDestinationPort(Integer destinationPort) {
    this.destinationPort = destinationPort;
  }


  public ApplicationGetHttpsEndpoint disableGatewayAuth(Boolean disableGatewayAuth) {
    this.disableGatewayAuth = disableGatewayAuth;
    return this;
  }

  /**
   * Disable gateway authentication.
   * @return disableGatewayAuth
   */
  @javax.annotation.Nullable
  public Boolean getDisableGatewayAuth() {
    return disableGatewayAuth;
  }

  public void setDisableGatewayAuth(Boolean disableGatewayAuth) {
    this.disableGatewayAuth = disableGatewayAuth;
  }


  public ApplicationGetHttpsEndpoint location(String location) {
    this.location = location;
    return this;
  }

  /**
   * The location of the endpoint.
   * @return location
   */
  @javax.annotation.Nullable
  public String getLocation() {
    return location;
  }

  public void setLocation(String location) {
    this.location = location;
  }


  public ApplicationGetHttpsEndpoint publicPort(Integer publicPort) {
    this.publicPort = publicPort;
    return this;
  }

  /**
   * The public port to connect to.
   * @return publicPort
   */
  @javax.annotation.Nullable
  public Integer getPublicPort() {
    return publicPort;
  }

  public void setPublicPort(Integer publicPort) {
    this.publicPort = publicPort;
  }


  public ApplicationGetHttpsEndpoint subDomainSuffix(String subDomainSuffix) {
    this.subDomainSuffix = subDomainSuffix;
    return this;
  }

  /**
   * The subdomain suffix of the application.
   * @return subDomainSuffix
   */
  @javax.annotation.Nullable
  public String getSubDomainSuffix() {
    return subDomainSuffix;
  }

  public void setSubDomainSuffix(String subDomainSuffix) {
    this.subDomainSuffix = subDomainSuffix;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ApplicationGetHttpsEndpoint applicationGetHttpsEndpoint = (ApplicationGetHttpsEndpoint) o;
    return Objects.equals(this.accessModes, applicationGetHttpsEndpoint.accessModes) &&
        Objects.equals(this.destinationPort, applicationGetHttpsEndpoint.destinationPort) &&
        Objects.equals(this.disableGatewayAuth, applicationGetHttpsEndpoint.disableGatewayAuth) &&
        Objects.equals(this.location, applicationGetHttpsEndpoint.location) &&
        Objects.equals(this.publicPort, applicationGetHttpsEndpoint.publicPort) &&
        Objects.equals(this.subDomainSuffix, applicationGetHttpsEndpoint.subDomainSuffix);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accessModes, destinationPort, disableGatewayAuth, location, publicPort, subDomainSuffix);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ApplicationGetHttpsEndpoint {\n");
    sb.append("    accessModes: ").append(toIndentedString(accessModes)).append("\n");
    sb.append("    destinationPort: ").append(toIndentedString(destinationPort)).append("\n");
    sb.append("    disableGatewayAuth: ").append(toIndentedString(disableGatewayAuth)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    publicPort: ").append(toIndentedString(publicPort)).append("\n");
    sb.append("    subDomainSuffix: ").append(toIndentedString(subDomainSuffix)).append("\n");
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
    openapiFields.add("accessModes");
    openapiFields.add("destinationPort");
    openapiFields.add("disableGatewayAuth");
    openapiFields.add("location");
    openapiFields.add("publicPort");
    openapiFields.add("subDomainSuffix");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ApplicationGetHttpsEndpoint
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ApplicationGetHttpsEndpoint.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ApplicationGetHttpsEndpoint is not found in the empty JSON string", ApplicationGetHttpsEndpoint.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ApplicationGetHttpsEndpoint.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ApplicationGetHttpsEndpoint` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("accessModes") != null && !jsonObj.get("accessModes").isJsonNull() && !jsonObj.get("accessModes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `accessModes` to be an array in the JSON string but got `%s`", jsonObj.get("accessModes").toString()));
      }
      if ((jsonObj.get("location") != null && !jsonObj.get("location").isJsonNull()) && !jsonObj.get("location").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `location` to be a primitive type in the JSON string but got `%s`", jsonObj.get("location").toString()));
      }
      if ((jsonObj.get("subDomainSuffix") != null && !jsonObj.get("subDomainSuffix").isJsonNull()) && !jsonObj.get("subDomainSuffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subDomainSuffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subDomainSuffix").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ApplicationGetHttpsEndpoint.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ApplicationGetHttpsEndpoint' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ApplicationGetHttpsEndpoint> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ApplicationGetHttpsEndpoint.class));

       return (TypeAdapter<T>) new TypeAdapter<ApplicationGetHttpsEndpoint>() {
           @Override
           public void write(JsonWriter out, ApplicationGetHttpsEndpoint value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ApplicationGetHttpsEndpoint read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ApplicationGetHttpsEndpoint given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ApplicationGetHttpsEndpoint
   * @throws IOException if the JSON string is invalid with respect to ApplicationGetHttpsEndpoint
   */
  public static ApplicationGetHttpsEndpoint fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ApplicationGetHttpsEndpoint.class);
  }

  /**
   * Convert an instance of ApplicationGetHttpsEndpoint to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

