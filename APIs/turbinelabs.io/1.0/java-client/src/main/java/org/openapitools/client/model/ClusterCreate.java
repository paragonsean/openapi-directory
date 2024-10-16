/*
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
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
import org.openapitools.client.model.CircuitBreakers;
import org.openapitools.client.model.HealthCheck;
import org.openapitools.client.model.Instance;
import org.openapitools.client.model.OutlierDetection;

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
 * ClusterCreate
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:51.953320-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ClusterCreate {
  public static final String SERIALIZED_NAME_CIRCUIT_BREAKERS = "circuit_breakers";
  @SerializedName(SERIALIZED_NAME_CIRCUIT_BREAKERS)
  private CircuitBreakers circuitBreakers;

  public static final String SERIALIZED_NAME_HEALTH_CHECKS = "health_checks";
  @SerializedName(SERIALIZED_NAME_HEALTH_CHECKS)
  private List<HealthCheck> healthChecks = new ArrayList<>();

  public static final String SERIALIZED_NAME_INSTANCES = "instances";
  @SerializedName(SERIALIZED_NAME_INSTANCES)
  private List<Instance> instances = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OUTLIER_DETECTION = "outlier_detection";
  @SerializedName(SERIALIZED_NAME_OUTLIER_DETECTION)
  private OutlierDetection outlierDetection;

  public static final String SERIALIZED_NAME_REQUIRE_TLS = "require_tls";
  @SerializedName(SERIALIZED_NAME_REQUIRE_TLS)
  private Boolean requireTls;

  public static final String SERIALIZED_NAME_ZONE_KEY = "zone_key";
  @SerializedName(SERIALIZED_NAME_ZONE_KEY)
  private String zoneKey;

  public ClusterCreate() {
  }

  public ClusterCreate circuitBreakers(CircuitBreakers circuitBreakers) {
    this.circuitBreakers = circuitBreakers;
    return this;
  }

  /**
   * Get circuitBreakers
   * @return circuitBreakers
   */
  @javax.annotation.Nullable
  public CircuitBreakers getCircuitBreakers() {
    return circuitBreakers;
  }

  public void setCircuitBreakers(CircuitBreakers circuitBreakers) {
    this.circuitBreakers = circuitBreakers;
  }


  public ClusterCreate healthChecks(List<HealthCheck> healthChecks) {
    this.healthChecks = healthChecks;
    return this;
  }

  public ClusterCreate addHealthChecksItem(HealthCheck healthChecksItem) {
    if (this.healthChecks == null) {
      this.healthChecks = new ArrayList<>();
    }
    this.healthChecks.add(healthChecksItem);
    return this;
  }

  /**
   * Get healthChecks
   * @return healthChecks
   */
  @javax.annotation.Nullable
  public List<HealthCheck> getHealthChecks() {
    return healthChecks;
  }

  public void setHealthChecks(List<HealthCheck> healthChecks) {
    this.healthChecks = healthChecks;
  }


  public ClusterCreate instances(List<Instance> instances) {
    this.instances = instances;
    return this;
  }

  public ClusterCreate addInstancesItem(Instance instancesItem) {
    if (this.instances == null) {
      this.instances = new ArrayList<>();
    }
    this.instances.add(instancesItem);
    return this;
  }

  /**
   * Get instances
   * @return instances
   */
  @javax.annotation.Nullable
  public List<Instance> getInstances() {
    return instances;
  }

  public void setInstances(List<Instance> instances) {
    this.instances = instances;
  }


  public ClusterCreate name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ClusterCreate outlierDetection(OutlierDetection outlierDetection) {
    this.outlierDetection = outlierDetection;
    return this;
  }

  /**
   * Get outlierDetection
   * @return outlierDetection
   */
  @javax.annotation.Nullable
  public OutlierDetection getOutlierDetection() {
    return outlierDetection;
  }

  public void setOutlierDetection(OutlierDetection outlierDetection) {
    this.outlierDetection = outlierDetection;
  }


  public ClusterCreate requireTls(Boolean requireTls) {
    this.requireTls = requireTls;
    return this;
  }

  /**
   * If set, requests to this collection of hosts will be made via HTTPS. At this time neither certificate validation and certificate pinning are supported for proxy clients of this cluster. 
   * @return requireTls
   */
  @javax.annotation.Nullable
  public Boolean getRequireTls() {
    return requireTls;
  }

  public void setRequireTls(Boolean requireTls) {
    this.requireTls = requireTls;
  }


  public ClusterCreate zoneKey(String zoneKey) {
    this.zoneKey = zoneKey;
    return this;
  }

  /**
   * Get zoneKey
   * @return zoneKey
   */
  @javax.annotation.Nonnull
  public String getZoneKey() {
    return zoneKey;
  }

  public void setZoneKey(String zoneKey) {
    this.zoneKey = zoneKey;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ClusterCreate clusterCreate = (ClusterCreate) o;
    return Objects.equals(this.circuitBreakers, clusterCreate.circuitBreakers) &&
        Objects.equals(this.healthChecks, clusterCreate.healthChecks) &&
        Objects.equals(this.instances, clusterCreate.instances) &&
        Objects.equals(this.name, clusterCreate.name) &&
        Objects.equals(this.outlierDetection, clusterCreate.outlierDetection) &&
        Objects.equals(this.requireTls, clusterCreate.requireTls) &&
        Objects.equals(this.zoneKey, clusterCreate.zoneKey);
  }

  @Override
  public int hashCode() {
    return Objects.hash(circuitBreakers, healthChecks, instances, name, outlierDetection, requireTls, zoneKey);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ClusterCreate {\n");
    sb.append("    circuitBreakers: ").append(toIndentedString(circuitBreakers)).append("\n");
    sb.append("    healthChecks: ").append(toIndentedString(healthChecks)).append("\n");
    sb.append("    instances: ").append(toIndentedString(instances)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    outlierDetection: ").append(toIndentedString(outlierDetection)).append("\n");
    sb.append("    requireTls: ").append(toIndentedString(requireTls)).append("\n");
    sb.append("    zoneKey: ").append(toIndentedString(zoneKey)).append("\n");
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
    openapiFields.add("circuit_breakers");
    openapiFields.add("health_checks");
    openapiFields.add("instances");
    openapiFields.add("name");
    openapiFields.add("outlier_detection");
    openapiFields.add("require_tls");
    openapiFields.add("zone_key");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("zone_key");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ClusterCreate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ClusterCreate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ClusterCreate is not found in the empty JSON string", ClusterCreate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ClusterCreate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ClusterCreate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ClusterCreate.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `circuit_breakers`
      if (jsonObj.get("circuit_breakers") != null && !jsonObj.get("circuit_breakers").isJsonNull()) {
        CircuitBreakers.validateJsonElement(jsonObj.get("circuit_breakers"));
      }
      if (jsonObj.get("health_checks") != null && !jsonObj.get("health_checks").isJsonNull()) {
        JsonArray jsonArrayhealthChecks = jsonObj.getAsJsonArray("health_checks");
        if (jsonArrayhealthChecks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("health_checks").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `health_checks` to be an array in the JSON string but got `%s`", jsonObj.get("health_checks").toString()));
          }

          // validate the optional field `health_checks` (array)
          for (int i = 0; i < jsonArrayhealthChecks.size(); i++) {
            HealthCheck.validateJsonElement(jsonArrayhealthChecks.get(i));
          };
        }
      }
      if (jsonObj.get("instances") != null && !jsonObj.get("instances").isJsonNull()) {
        JsonArray jsonArrayinstances = jsonObj.getAsJsonArray("instances");
        if (jsonArrayinstances != null) {
          // ensure the json data is an array
          if (!jsonObj.get("instances").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `instances` to be an array in the JSON string but got `%s`", jsonObj.get("instances").toString()));
          }

          // validate the optional field `instances` (array)
          for (int i = 0; i < jsonArrayinstances.size(); i++) {
            Instance.validateJsonElement(jsonArrayinstances.get(i));
          };
        }
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `outlier_detection`
      if (jsonObj.get("outlier_detection") != null && !jsonObj.get("outlier_detection").isJsonNull()) {
        OutlierDetection.validateJsonElement(jsonObj.get("outlier_detection"));
      }
      if (!jsonObj.get("zone_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `zone_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("zone_key").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ClusterCreate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ClusterCreate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ClusterCreate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ClusterCreate.class));

       return (TypeAdapter<T>) new TypeAdapter<ClusterCreate>() {
           @Override
           public void write(JsonWriter out, ClusterCreate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ClusterCreate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ClusterCreate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ClusterCreate
   * @throws IOException if the JSON string is invalid with respect to ClusterCreate
   */
  public static ClusterCreate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ClusterCreate.class);
  }

  /**
   * Convert an instance of ClusterCreate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

