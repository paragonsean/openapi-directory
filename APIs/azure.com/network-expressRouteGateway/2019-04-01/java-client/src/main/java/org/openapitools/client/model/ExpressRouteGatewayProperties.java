/*
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-04-01
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
import org.openapitools.client.model.ExpressRouteConnection;
import org.openapitools.client.model.ExpressRouteGatewayPropertiesAutoScaleConfiguration;
import org.openapitools.client.model.VirtualHubId;

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
 * ExpressRoute gateway resource properties.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:36.979477-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ExpressRouteGatewayProperties {
  public static final String SERIALIZED_NAME_AUTO_SCALE_CONFIGURATION = "autoScaleConfiguration";
  @SerializedName(SERIALIZED_NAME_AUTO_SCALE_CONFIGURATION)
  private ExpressRouteGatewayPropertiesAutoScaleConfiguration autoScaleConfiguration;

  public static final String SERIALIZED_NAME_EXPRESS_ROUTE_CONNECTIONS = "expressRouteConnections";
  @SerializedName(SERIALIZED_NAME_EXPRESS_ROUTE_CONNECTIONS)
  private List<ExpressRouteConnection> expressRouteConnections = new ArrayList<>();

  /**
   * The current provisioning state.
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

  public static final String SERIALIZED_NAME_VIRTUAL_HUB = "virtualHub";
  @SerializedName(SERIALIZED_NAME_VIRTUAL_HUB)
  private VirtualHubId virtualHub;

  public ExpressRouteGatewayProperties() {
  }

  public ExpressRouteGatewayProperties(
     List<ExpressRouteConnection> expressRouteConnections, 
     ProvisioningStateEnum provisioningState
  ) {
    this();
    this.expressRouteConnections = expressRouteConnections;
    this.provisioningState = provisioningState;
  }

  public ExpressRouteGatewayProperties autoScaleConfiguration(ExpressRouteGatewayPropertiesAutoScaleConfiguration autoScaleConfiguration) {
    this.autoScaleConfiguration = autoScaleConfiguration;
    return this;
  }

  /**
   * Get autoScaleConfiguration
   * @return autoScaleConfiguration
   */
  @javax.annotation.Nullable
  public ExpressRouteGatewayPropertiesAutoScaleConfiguration getAutoScaleConfiguration() {
    return autoScaleConfiguration;
  }

  public void setAutoScaleConfiguration(ExpressRouteGatewayPropertiesAutoScaleConfiguration autoScaleConfiguration) {
    this.autoScaleConfiguration = autoScaleConfiguration;
  }


  /**
   * List of ExpressRoute connections to the ExpressRoute gateway.
   * @return expressRouteConnections
   */
  @javax.annotation.Nullable
  public List<ExpressRouteConnection> getExpressRouteConnections() {
    return expressRouteConnections;
  }



  /**
   * The current provisioning state.
   * @return provisioningState
   */
  @javax.annotation.Nullable
  public ProvisioningStateEnum getProvisioningState() {
    return provisioningState;
  }



  public ExpressRouteGatewayProperties virtualHub(VirtualHubId virtualHub) {
    this.virtualHub = virtualHub;
    return this;
  }

  /**
   * Get virtualHub
   * @return virtualHub
   */
  @javax.annotation.Nonnull
  public VirtualHubId getVirtualHub() {
    return virtualHub;
  }

  public void setVirtualHub(VirtualHubId virtualHub) {
    this.virtualHub = virtualHub;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ExpressRouteGatewayProperties expressRouteGatewayProperties = (ExpressRouteGatewayProperties) o;
    return Objects.equals(this.autoScaleConfiguration, expressRouteGatewayProperties.autoScaleConfiguration) &&
        Objects.equals(this.expressRouteConnections, expressRouteGatewayProperties.expressRouteConnections) &&
        Objects.equals(this.provisioningState, expressRouteGatewayProperties.provisioningState) &&
        Objects.equals(this.virtualHub, expressRouteGatewayProperties.virtualHub);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoScaleConfiguration, expressRouteConnections, provisioningState, virtualHub);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ExpressRouteGatewayProperties {\n");
    sb.append("    autoScaleConfiguration: ").append(toIndentedString(autoScaleConfiguration)).append("\n");
    sb.append("    expressRouteConnections: ").append(toIndentedString(expressRouteConnections)).append("\n");
    sb.append("    provisioningState: ").append(toIndentedString(provisioningState)).append("\n");
    sb.append("    virtualHub: ").append(toIndentedString(virtualHub)).append("\n");
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
    openapiFields.add("autoScaleConfiguration");
    openapiFields.add("expressRouteConnections");
    openapiFields.add("provisioningState");
    openapiFields.add("virtualHub");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("virtualHub");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ExpressRouteGatewayProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ExpressRouteGatewayProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ExpressRouteGatewayProperties is not found in the empty JSON string", ExpressRouteGatewayProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ExpressRouteGatewayProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ExpressRouteGatewayProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ExpressRouteGatewayProperties.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `autoScaleConfiguration`
      if (jsonObj.get("autoScaleConfiguration") != null && !jsonObj.get("autoScaleConfiguration").isJsonNull()) {
        ExpressRouteGatewayPropertiesAutoScaleConfiguration.validateJsonElement(jsonObj.get("autoScaleConfiguration"));
      }
      if (jsonObj.get("expressRouteConnections") != null && !jsonObj.get("expressRouteConnections").isJsonNull()) {
        JsonArray jsonArrayexpressRouteConnections = jsonObj.getAsJsonArray("expressRouteConnections");
        if (jsonArrayexpressRouteConnections != null) {
          // ensure the json data is an array
          if (!jsonObj.get("expressRouteConnections").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `expressRouteConnections` to be an array in the JSON string but got `%s`", jsonObj.get("expressRouteConnections").toString()));
          }

          // validate the optional field `expressRouteConnections` (array)
          for (int i = 0; i < jsonArrayexpressRouteConnections.size(); i++) {
            ExpressRouteConnection.validateJsonElement(jsonArrayexpressRouteConnections.get(i));
          };
        }
      }
      if ((jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) && !jsonObj.get("provisioningState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provisioningState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provisioningState").toString()));
      }
      // validate the optional field `provisioningState`
      if (jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) {
        ProvisioningStateEnum.validateJsonElement(jsonObj.get("provisioningState"));
      }
      // validate the required field `virtualHub`
      VirtualHubId.validateJsonElement(jsonObj.get("virtualHub"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ExpressRouteGatewayProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ExpressRouteGatewayProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ExpressRouteGatewayProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ExpressRouteGatewayProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<ExpressRouteGatewayProperties>() {
           @Override
           public void write(JsonWriter out, ExpressRouteGatewayProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ExpressRouteGatewayProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ExpressRouteGatewayProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ExpressRouteGatewayProperties
   * @throws IOException if the JSON string is invalid with respect to ExpressRouteGatewayProperties
   */
  public static ExpressRouteGatewayProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ExpressRouteGatewayProperties.class);
  }

  /**
   * Convert an instance of ExpressRouteGatewayProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

