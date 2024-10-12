/*
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
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
import org.openapitools.client.model.BackendPoolUpdateParametersHealthProbeSettings;
import org.openapitools.client.model.RouteConfiguration;

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
 * Routing rules to apply to an endpoint
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:16:31.612735-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RoutingRuleUpdateParameters {
  /**
   * Accepted protocol schemes.
   */
  @JsonAdapter(AcceptedProtocolsEnum.Adapter.class)
  public enum AcceptedProtocolsEnum {
    HTTP("Http"),
    
    HTTPS("Https");

    private String value;

    AcceptedProtocolsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AcceptedProtocolsEnum fromValue(String value) {
      for (AcceptedProtocolsEnum b : AcceptedProtocolsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AcceptedProtocolsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AcceptedProtocolsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AcceptedProtocolsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AcceptedProtocolsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AcceptedProtocolsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACCEPTED_PROTOCOLS = "acceptedProtocols";
  @SerializedName(SERIALIZED_NAME_ACCEPTED_PROTOCOLS)
  private List<AcceptedProtocolsEnum> acceptedProtocols = new ArrayList<>();

  /**
   * Whether to enable use of this rule. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39;
   */
  @JsonAdapter(EnabledStateEnum.Adapter.class)
  public enum EnabledStateEnum {
    ENABLED("Enabled"),
    
    DISABLED("Disabled");

    private String value;

    EnabledStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnabledStateEnum fromValue(String value) {
      for (EnabledStateEnum b : EnabledStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EnabledStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnabledStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnabledStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EnabledStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EnabledStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ENABLED_STATE = "enabledState";
  @SerializedName(SERIALIZED_NAME_ENABLED_STATE)
  private EnabledStateEnum enabledState;

  public static final String SERIALIZED_NAME_FRONTEND_ENDPOINTS = "frontendEndpoints";
  @SerializedName(SERIALIZED_NAME_FRONTEND_ENDPOINTS)
  private List<BackendPoolUpdateParametersHealthProbeSettings> frontendEndpoints = new ArrayList<>();

  public static final String SERIALIZED_NAME_PATTERNS_TO_MATCH = "patternsToMatch";
  @SerializedName(SERIALIZED_NAME_PATTERNS_TO_MATCH)
  private List<String> patternsToMatch = new ArrayList<>();

  public static final String SERIALIZED_NAME_ROUTE_CONFIGURATION = "routeConfiguration";
  @SerializedName(SERIALIZED_NAME_ROUTE_CONFIGURATION)
  private RouteConfiguration routeConfiguration;

  public RoutingRuleUpdateParameters() {
  }

  public RoutingRuleUpdateParameters acceptedProtocols(List<AcceptedProtocolsEnum> acceptedProtocols) {
    this.acceptedProtocols = acceptedProtocols;
    return this;
  }

  public RoutingRuleUpdateParameters addAcceptedProtocolsItem(AcceptedProtocolsEnum acceptedProtocolsItem) {
    if (this.acceptedProtocols == null) {
      this.acceptedProtocols = new ArrayList<>();
    }
    this.acceptedProtocols.add(acceptedProtocolsItem);
    return this;
  }

  /**
   * Protocol schemes to match for this rule
   * @return acceptedProtocols
   */
  @javax.annotation.Nullable
  public List<AcceptedProtocolsEnum> getAcceptedProtocols() {
    return acceptedProtocols;
  }

  public void setAcceptedProtocols(List<AcceptedProtocolsEnum> acceptedProtocols) {
    this.acceptedProtocols = acceptedProtocols;
  }


  public RoutingRuleUpdateParameters enabledState(EnabledStateEnum enabledState) {
    this.enabledState = enabledState;
    return this;
  }

  /**
   * Whether to enable use of this rule. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39;
   * @return enabledState
   */
  @javax.annotation.Nullable
  public EnabledStateEnum getEnabledState() {
    return enabledState;
  }

  public void setEnabledState(EnabledStateEnum enabledState) {
    this.enabledState = enabledState;
  }


  public RoutingRuleUpdateParameters frontendEndpoints(List<BackendPoolUpdateParametersHealthProbeSettings> frontendEndpoints) {
    this.frontendEndpoints = frontendEndpoints;
    return this;
  }

  public RoutingRuleUpdateParameters addFrontendEndpointsItem(BackendPoolUpdateParametersHealthProbeSettings frontendEndpointsItem) {
    if (this.frontendEndpoints == null) {
      this.frontendEndpoints = new ArrayList<>();
    }
    this.frontendEndpoints.add(frontendEndpointsItem);
    return this;
  }

  /**
   * Frontend endpoints associated with this rule
   * @return frontendEndpoints
   */
  @javax.annotation.Nullable
  public List<BackendPoolUpdateParametersHealthProbeSettings> getFrontendEndpoints() {
    return frontendEndpoints;
  }

  public void setFrontendEndpoints(List<BackendPoolUpdateParametersHealthProbeSettings> frontendEndpoints) {
    this.frontendEndpoints = frontendEndpoints;
  }


  public RoutingRuleUpdateParameters patternsToMatch(List<String> patternsToMatch) {
    this.patternsToMatch = patternsToMatch;
    return this;
  }

  public RoutingRuleUpdateParameters addPatternsToMatchItem(String patternsToMatchItem) {
    if (this.patternsToMatch == null) {
      this.patternsToMatch = new ArrayList<>();
    }
    this.patternsToMatch.add(patternsToMatchItem);
    return this;
  }

  /**
   * The route patterns of the rule.
   * @return patternsToMatch
   */
  @javax.annotation.Nullable
  public List<String> getPatternsToMatch() {
    return patternsToMatch;
  }

  public void setPatternsToMatch(List<String> patternsToMatch) {
    this.patternsToMatch = patternsToMatch;
  }


  public RoutingRuleUpdateParameters routeConfiguration(RouteConfiguration routeConfiguration) {
    this.routeConfiguration = routeConfiguration;
    return this;
  }

  /**
   * Get routeConfiguration
   * @return routeConfiguration
   */
  @javax.annotation.Nullable
  public RouteConfiguration getRouteConfiguration() {
    return routeConfiguration;
  }

  public void setRouteConfiguration(RouteConfiguration routeConfiguration) {
    this.routeConfiguration = routeConfiguration;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RoutingRuleUpdateParameters routingRuleUpdateParameters = (RoutingRuleUpdateParameters) o;
    return Objects.equals(this.acceptedProtocols, routingRuleUpdateParameters.acceptedProtocols) &&
        Objects.equals(this.enabledState, routingRuleUpdateParameters.enabledState) &&
        Objects.equals(this.frontendEndpoints, routingRuleUpdateParameters.frontendEndpoints) &&
        Objects.equals(this.patternsToMatch, routingRuleUpdateParameters.patternsToMatch) &&
        Objects.equals(this.routeConfiguration, routingRuleUpdateParameters.routeConfiguration);
  }

  @Override
  public int hashCode() {
    return Objects.hash(acceptedProtocols, enabledState, frontendEndpoints, patternsToMatch, routeConfiguration);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RoutingRuleUpdateParameters {\n");
    sb.append("    acceptedProtocols: ").append(toIndentedString(acceptedProtocols)).append("\n");
    sb.append("    enabledState: ").append(toIndentedString(enabledState)).append("\n");
    sb.append("    frontendEndpoints: ").append(toIndentedString(frontendEndpoints)).append("\n");
    sb.append("    patternsToMatch: ").append(toIndentedString(patternsToMatch)).append("\n");
    sb.append("    routeConfiguration: ").append(toIndentedString(routeConfiguration)).append("\n");
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
    openapiFields.add("acceptedProtocols");
    openapiFields.add("enabledState");
    openapiFields.add("frontendEndpoints");
    openapiFields.add("patternsToMatch");
    openapiFields.add("routeConfiguration");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RoutingRuleUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RoutingRuleUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RoutingRuleUpdateParameters is not found in the empty JSON string", RoutingRuleUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RoutingRuleUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RoutingRuleUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("acceptedProtocols") != null && !jsonObj.get("acceptedProtocols").isJsonNull() && !jsonObj.get("acceptedProtocols").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `acceptedProtocols` to be an array in the JSON string but got `%s`", jsonObj.get("acceptedProtocols").toString()));
      }
      if ((jsonObj.get("enabledState") != null && !jsonObj.get("enabledState").isJsonNull()) && !jsonObj.get("enabledState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `enabledState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("enabledState").toString()));
      }
      // validate the optional field `enabledState`
      if (jsonObj.get("enabledState") != null && !jsonObj.get("enabledState").isJsonNull()) {
        EnabledStateEnum.validateJsonElement(jsonObj.get("enabledState"));
      }
      if (jsonObj.get("frontendEndpoints") != null && !jsonObj.get("frontendEndpoints").isJsonNull()) {
        JsonArray jsonArrayfrontendEndpoints = jsonObj.getAsJsonArray("frontendEndpoints");
        if (jsonArrayfrontendEndpoints != null) {
          // ensure the json data is an array
          if (!jsonObj.get("frontendEndpoints").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `frontendEndpoints` to be an array in the JSON string but got `%s`", jsonObj.get("frontendEndpoints").toString()));
          }

          // validate the optional field `frontendEndpoints` (array)
          for (int i = 0; i < jsonArrayfrontendEndpoints.size(); i++) {
            BackendPoolUpdateParametersHealthProbeSettings.validateJsonElement(jsonArrayfrontendEndpoints.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("patternsToMatch") != null && !jsonObj.get("patternsToMatch").isJsonNull() && !jsonObj.get("patternsToMatch").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `patternsToMatch` to be an array in the JSON string but got `%s`", jsonObj.get("patternsToMatch").toString()));
      }
      // validate the optional field `routeConfiguration`
      if (jsonObj.get("routeConfiguration") != null && !jsonObj.get("routeConfiguration").isJsonNull()) {
        RouteConfiguration.validateJsonElement(jsonObj.get("routeConfiguration"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RoutingRuleUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RoutingRuleUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RoutingRuleUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RoutingRuleUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<RoutingRuleUpdateParameters>() {
           @Override
           public void write(JsonWriter out, RoutingRuleUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RoutingRuleUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RoutingRuleUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RoutingRuleUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to RoutingRuleUpdateParameters
   */
  public static RoutingRuleUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RoutingRuleUpdateParameters.class);
  }

  /**
   * Convert an instance of RoutingRuleUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

