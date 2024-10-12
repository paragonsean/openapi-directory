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
import org.openapitools.client.model.Backend;
import org.openapitools.client.model.BackendPoolUpdateParametersHealthProbeSettings;

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
 * A collection of backends that can be routed to.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:16:31.612735-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BackendPoolUpdateParameters {
  public static final String SERIALIZED_NAME_BACKENDS = "backends";
  @SerializedName(SERIALIZED_NAME_BACKENDS)
  private List<Backend> backends = new ArrayList<>();

  public static final String SERIALIZED_NAME_HEALTH_PROBE_SETTINGS = "healthProbeSettings";
  @SerializedName(SERIALIZED_NAME_HEALTH_PROBE_SETTINGS)
  private BackendPoolUpdateParametersHealthProbeSettings healthProbeSettings;

  public static final String SERIALIZED_NAME_LOAD_BALANCING_SETTINGS = "loadBalancingSettings";
  @SerializedName(SERIALIZED_NAME_LOAD_BALANCING_SETTINGS)
  private BackendPoolUpdateParametersHealthProbeSettings loadBalancingSettings;

  public BackendPoolUpdateParameters() {
  }

  public BackendPoolUpdateParameters backends(List<Backend> backends) {
    this.backends = backends;
    return this;
  }

  public BackendPoolUpdateParameters addBackendsItem(Backend backendsItem) {
    if (this.backends == null) {
      this.backends = new ArrayList<>();
    }
    this.backends.add(backendsItem);
    return this;
  }

  /**
   * The set of backends for this pool
   * @return backends
   */
  @javax.annotation.Nullable
  public List<Backend> getBackends() {
    return backends;
  }

  public void setBackends(List<Backend> backends) {
    this.backends = backends;
  }


  public BackendPoolUpdateParameters healthProbeSettings(BackendPoolUpdateParametersHealthProbeSettings healthProbeSettings) {
    this.healthProbeSettings = healthProbeSettings;
    return this;
  }

  /**
   * Get healthProbeSettings
   * @return healthProbeSettings
   */
  @javax.annotation.Nullable
  public BackendPoolUpdateParametersHealthProbeSettings getHealthProbeSettings() {
    return healthProbeSettings;
  }

  public void setHealthProbeSettings(BackendPoolUpdateParametersHealthProbeSettings healthProbeSettings) {
    this.healthProbeSettings = healthProbeSettings;
  }


  public BackendPoolUpdateParameters loadBalancingSettings(BackendPoolUpdateParametersHealthProbeSettings loadBalancingSettings) {
    this.loadBalancingSettings = loadBalancingSettings;
    return this;
  }

  /**
   * Get loadBalancingSettings
   * @return loadBalancingSettings
   */
  @javax.annotation.Nullable
  public BackendPoolUpdateParametersHealthProbeSettings getLoadBalancingSettings() {
    return loadBalancingSettings;
  }

  public void setLoadBalancingSettings(BackendPoolUpdateParametersHealthProbeSettings loadBalancingSettings) {
    this.loadBalancingSettings = loadBalancingSettings;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BackendPoolUpdateParameters backendPoolUpdateParameters = (BackendPoolUpdateParameters) o;
    return Objects.equals(this.backends, backendPoolUpdateParameters.backends) &&
        Objects.equals(this.healthProbeSettings, backendPoolUpdateParameters.healthProbeSettings) &&
        Objects.equals(this.loadBalancingSettings, backendPoolUpdateParameters.loadBalancingSettings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(backends, healthProbeSettings, loadBalancingSettings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BackendPoolUpdateParameters {\n");
    sb.append("    backends: ").append(toIndentedString(backends)).append("\n");
    sb.append("    healthProbeSettings: ").append(toIndentedString(healthProbeSettings)).append("\n");
    sb.append("    loadBalancingSettings: ").append(toIndentedString(loadBalancingSettings)).append("\n");
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
    openapiFields.add("backends");
    openapiFields.add("healthProbeSettings");
    openapiFields.add("loadBalancingSettings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BackendPoolUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BackendPoolUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BackendPoolUpdateParameters is not found in the empty JSON string", BackendPoolUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BackendPoolUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BackendPoolUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("backends") != null && !jsonObj.get("backends").isJsonNull()) {
        JsonArray jsonArraybackends = jsonObj.getAsJsonArray("backends");
        if (jsonArraybackends != null) {
          // ensure the json data is an array
          if (!jsonObj.get("backends").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `backends` to be an array in the JSON string but got `%s`", jsonObj.get("backends").toString()));
          }

          // validate the optional field `backends` (array)
          for (int i = 0; i < jsonArraybackends.size(); i++) {
            Backend.validateJsonElement(jsonArraybackends.get(i));
          };
        }
      }
      // validate the optional field `healthProbeSettings`
      if (jsonObj.get("healthProbeSettings") != null && !jsonObj.get("healthProbeSettings").isJsonNull()) {
        BackendPoolUpdateParametersHealthProbeSettings.validateJsonElement(jsonObj.get("healthProbeSettings"));
      }
      // validate the optional field `loadBalancingSettings`
      if (jsonObj.get("loadBalancingSettings") != null && !jsonObj.get("loadBalancingSettings").isJsonNull()) {
        BackendPoolUpdateParametersHealthProbeSettings.validateJsonElement(jsonObj.get("loadBalancingSettings"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BackendPoolUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BackendPoolUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BackendPoolUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BackendPoolUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<BackendPoolUpdateParameters>() {
           @Override
           public void write(JsonWriter out, BackendPoolUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BackendPoolUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BackendPoolUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BackendPoolUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to BackendPoolUpdateParameters
   */
  public static BackendPoolUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BackendPoolUpdateParameters.class);
  }

  /**
   * Convert an instance of BackendPoolUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

