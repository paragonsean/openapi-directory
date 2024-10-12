/*
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-08-01
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
import org.openapitools.client.model.ExpressRouteCircuitPeeringId;

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
 * Properties of the ExpressRouteConnection subresource.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:40.470200-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExpressRouteConnectionProperties {
  public static final String SERIALIZED_NAME_AUTHORIZATION_KEY = "authorizationKey";
  @SerializedName(SERIALIZED_NAME_AUTHORIZATION_KEY)
  private String authorizationKey;

  public static final String SERIALIZED_NAME_EXPRESS_ROUTE_CIRCUIT_PEERING = "expressRouteCircuitPeering";
  @SerializedName(SERIALIZED_NAME_EXPRESS_ROUTE_CIRCUIT_PEERING)
  private ExpressRouteCircuitPeeringId expressRouteCircuitPeering;

  /**
   * The provisioning state of the resource.
   */
  @JsonAdapter(ProvisioningStateEnum.Adapter.class)
  public enum ProvisioningStateEnum {
    SUCCEEDED("Succeeded"),
    
    UPDATING("Updating"),
    
    DELETING("Deleting"),
    
    FAILED("Failed");

    private String value;

    ProvisioningStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProvisioningStateEnum fromValue(String value) {
      for (ProvisioningStateEnum b : ProvisioningStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProvisioningStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProvisioningStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProvisioningStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProvisioningStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProvisioningStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROVISIONING_STATE = "provisioningState";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_STATE)
  private ProvisioningStateEnum provisioningState;

  public static final String SERIALIZED_NAME_ROUTING_WEIGHT = "routingWeight";
  @SerializedName(SERIALIZED_NAME_ROUTING_WEIGHT)
  private Integer routingWeight;

  public ExpressRouteConnectionProperties() {
  }

  public ExpressRouteConnectionProperties(
     ProvisioningStateEnum provisioningState
  ) {
    this();
    this.provisioningState = provisioningState;
  }

  public ExpressRouteConnectionProperties authorizationKey(String authorizationKey) {
    this.authorizationKey = authorizationKey;
    return this;
  }

  /**
   * Authorization key to establish the connection.
   * @return authorizationKey
   */
  @javax.annotation.Nullable
  public String getAuthorizationKey() {
    return authorizationKey;
  }

  public void setAuthorizationKey(String authorizationKey) {
    this.authorizationKey = authorizationKey;
  }


  public ExpressRouteConnectionProperties expressRouteCircuitPeering(ExpressRouteCircuitPeeringId expressRouteCircuitPeering) {
    this.expressRouteCircuitPeering = expressRouteCircuitPeering;
    return this;
  }

  /**
   * Get expressRouteCircuitPeering
   * @return expressRouteCircuitPeering
   */
  @javax.annotation.Nonnull
  public ExpressRouteCircuitPeeringId getExpressRouteCircuitPeering() {
    return expressRouteCircuitPeering;
  }

  public void setExpressRouteCircuitPeering(ExpressRouteCircuitPeeringId expressRouteCircuitPeering) {
    this.expressRouteCircuitPeering = expressRouteCircuitPeering;
  }


  /**
   * The provisioning state of the resource.
   * @return provisioningState
   */
  @javax.annotation.Nullable
  public ProvisioningStateEnum getProvisioningState() {
    return provisioningState;
  }



  public ExpressRouteConnectionProperties routingWeight(Integer routingWeight) {
    this.routingWeight = routingWeight;
    return this;
  }

  /**
   * The routing weight associated to the connection.
   * @return routingWeight
   */
  @javax.annotation.Nullable
  public Integer getRoutingWeight() {
    return routingWeight;
  }

  public void setRoutingWeight(Integer routingWeight) {
    this.routingWeight = routingWeight;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExpressRouteConnectionProperties expressRouteConnectionProperties = (ExpressRouteConnectionProperties) o;
    return Objects.equals(this.authorizationKey, expressRouteConnectionProperties.authorizationKey) &&
        Objects.equals(this.expressRouteCircuitPeering, expressRouteConnectionProperties.expressRouteCircuitPeering) &&
        Objects.equals(this.provisioningState, expressRouteConnectionProperties.provisioningState) &&
        Objects.equals(this.routingWeight, expressRouteConnectionProperties.routingWeight);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authorizationKey, expressRouteCircuitPeering, provisioningState, routingWeight);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExpressRouteConnectionProperties {\n");
    sb.append("    authorizationKey: ").append(toIndentedString(authorizationKey)).append("\n");
    sb.append("    expressRouteCircuitPeering: ").append(toIndentedString(expressRouteCircuitPeering)).append("\n");
    sb.append("    provisioningState: ").append(toIndentedString(provisioningState)).append("\n");
    sb.append("    routingWeight: ").append(toIndentedString(routingWeight)).append("\n");
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
    openapiFields.add("authorizationKey");
    openapiFields.add("expressRouteCircuitPeering");
    openapiFields.add("provisioningState");
    openapiFields.add("routingWeight");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("expressRouteCircuitPeering");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExpressRouteConnectionProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExpressRouteConnectionProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExpressRouteConnectionProperties is not found in the empty JSON string", ExpressRouteConnectionProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExpressRouteConnectionProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExpressRouteConnectionProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ExpressRouteConnectionProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("authorizationKey") != null && !jsonObj.get("authorizationKey").isJsonNull()) && !jsonObj.get("authorizationKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authorizationKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authorizationKey").toString()));
      }
      // validate the required field `expressRouteCircuitPeering`
      ExpressRouteCircuitPeeringId.validateJsonElement(jsonObj.get("expressRouteCircuitPeering"));
      if ((jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) && !jsonObj.get("provisioningState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provisioningState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provisioningState").toString()));
      }
      // validate the optional field `provisioningState`
      if (jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) {
        ProvisioningStateEnum.validateJsonElement(jsonObj.get("provisioningState"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExpressRouteConnectionProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExpressRouteConnectionProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExpressRouteConnectionProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExpressRouteConnectionProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<ExpressRouteConnectionProperties>() {
           @Override
           public void write(JsonWriter out, ExpressRouteConnectionProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExpressRouteConnectionProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExpressRouteConnectionProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExpressRouteConnectionProperties
   * @throws IOException if the JSON string is invalid with respect to ExpressRouteConnectionProperties
   */
  public static ExpressRouteConnectionProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExpressRouteConnectionProperties.class);
  }

  /**
   * Convert an instance of ExpressRouteConnectionProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

