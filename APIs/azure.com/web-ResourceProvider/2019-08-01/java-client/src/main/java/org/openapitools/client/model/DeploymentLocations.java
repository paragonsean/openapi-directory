/*
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
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
import org.openapitools.client.model.DeploymentLocationsHostingEnvironmentsInner;
import org.openapitools.client.model.GeoRegion;
import org.openapitools.client.model.HostingEnvironmentDeploymentInfo;

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
 * List of available locations (regions or App Service Environments) for deployment of App Service resources.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:47.141391-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeploymentLocations {
  public static final String SERIALIZED_NAME_HOSTING_ENVIRONMENT_DEPLOYMENT_INFOS = "hostingEnvironmentDeploymentInfos";
  @SerializedName(SERIALIZED_NAME_HOSTING_ENVIRONMENT_DEPLOYMENT_INFOS)
  private List<HostingEnvironmentDeploymentInfo> hostingEnvironmentDeploymentInfos = new ArrayList<>();

  public static final String SERIALIZED_NAME_HOSTING_ENVIRONMENTS = "hostingEnvironments";
  @SerializedName(SERIALIZED_NAME_HOSTING_ENVIRONMENTS)
  private List<DeploymentLocationsHostingEnvironmentsInner> hostingEnvironments = new ArrayList<>();

  public static final String SERIALIZED_NAME_LOCATIONS = "locations";
  @SerializedName(SERIALIZED_NAME_LOCATIONS)
  private List<GeoRegion> locations = new ArrayList<>();

  public DeploymentLocations() {
  }

  public DeploymentLocations hostingEnvironmentDeploymentInfos(List<HostingEnvironmentDeploymentInfo> hostingEnvironmentDeploymentInfos) {
    this.hostingEnvironmentDeploymentInfos = hostingEnvironmentDeploymentInfos;
    return this;
  }

  public DeploymentLocations addHostingEnvironmentDeploymentInfosItem(HostingEnvironmentDeploymentInfo hostingEnvironmentDeploymentInfosItem) {
    if (this.hostingEnvironmentDeploymentInfos == null) {
      this.hostingEnvironmentDeploymentInfos = new ArrayList<>();
    }
    this.hostingEnvironmentDeploymentInfos.add(hostingEnvironmentDeploymentInfosItem);
    return this;
  }

  /**
   * Available App Service Environments with basic information.
   * @return hostingEnvironmentDeploymentInfos
   */
  @javax.annotation.Nullable
  public List<HostingEnvironmentDeploymentInfo> getHostingEnvironmentDeploymentInfos() {
    return hostingEnvironmentDeploymentInfos;
  }

  public void setHostingEnvironmentDeploymentInfos(List<HostingEnvironmentDeploymentInfo> hostingEnvironmentDeploymentInfos) {
    this.hostingEnvironmentDeploymentInfos = hostingEnvironmentDeploymentInfos;
  }


  public DeploymentLocations hostingEnvironments(List<DeploymentLocationsHostingEnvironmentsInner> hostingEnvironments) {
    this.hostingEnvironments = hostingEnvironments;
    return this;
  }

  public DeploymentLocations addHostingEnvironmentsItem(DeploymentLocationsHostingEnvironmentsInner hostingEnvironmentsItem) {
    if (this.hostingEnvironments == null) {
      this.hostingEnvironments = new ArrayList<>();
    }
    this.hostingEnvironments.add(hostingEnvironmentsItem);
    return this;
  }

  /**
   * Available App Service Environments with full descriptions of the environments.
   * @return hostingEnvironments
   */
  @javax.annotation.Nullable
  public List<DeploymentLocationsHostingEnvironmentsInner> getHostingEnvironments() {
    return hostingEnvironments;
  }

  public void setHostingEnvironments(List<DeploymentLocationsHostingEnvironmentsInner> hostingEnvironments) {
    this.hostingEnvironments = hostingEnvironments;
  }


  public DeploymentLocations locations(List<GeoRegion> locations) {
    this.locations = locations;
    return this;
  }

  public DeploymentLocations addLocationsItem(GeoRegion locationsItem) {
    if (this.locations == null) {
      this.locations = new ArrayList<>();
    }
    this.locations.add(locationsItem);
    return this;
  }

  /**
   * Available regions.
   * @return locations
   */
  @javax.annotation.Nullable
  public List<GeoRegion> getLocations() {
    return locations;
  }

  public void setLocations(List<GeoRegion> locations) {
    this.locations = locations;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeploymentLocations deploymentLocations = (DeploymentLocations) o;
    return Objects.equals(this.hostingEnvironmentDeploymentInfos, deploymentLocations.hostingEnvironmentDeploymentInfos) &&
        Objects.equals(this.hostingEnvironments, deploymentLocations.hostingEnvironments) &&
        Objects.equals(this.locations, deploymentLocations.locations);
  }

  @Override
  public int hashCode() {
    return Objects.hash(hostingEnvironmentDeploymentInfos, hostingEnvironments, locations);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeploymentLocations {\n");
    sb.append("    hostingEnvironmentDeploymentInfos: ").append(toIndentedString(hostingEnvironmentDeploymentInfos)).append("\n");
    sb.append("    hostingEnvironments: ").append(toIndentedString(hostingEnvironments)).append("\n");
    sb.append("    locations: ").append(toIndentedString(locations)).append("\n");
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
    openapiFields.add("hostingEnvironmentDeploymentInfos");
    openapiFields.add("hostingEnvironments");
    openapiFields.add("locations");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeploymentLocations
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeploymentLocations.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeploymentLocations is not found in the empty JSON string", DeploymentLocations.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeploymentLocations.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeploymentLocations` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("hostingEnvironmentDeploymentInfos") != null && !jsonObj.get("hostingEnvironmentDeploymentInfos").isJsonNull()) {
        JsonArray jsonArrayhostingEnvironmentDeploymentInfos = jsonObj.getAsJsonArray("hostingEnvironmentDeploymentInfos");
        if (jsonArrayhostingEnvironmentDeploymentInfos != null) {
          // ensure the json data is an array
          if (!jsonObj.get("hostingEnvironmentDeploymentInfos").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `hostingEnvironmentDeploymentInfos` to be an array in the JSON string but got `%s`", jsonObj.get("hostingEnvironmentDeploymentInfos").toString()));
          }

          // validate the optional field `hostingEnvironmentDeploymentInfos` (array)
          for (int i = 0; i < jsonArrayhostingEnvironmentDeploymentInfos.size(); i++) {
            HostingEnvironmentDeploymentInfo.validateJsonElement(jsonArrayhostingEnvironmentDeploymentInfos.get(i));
          };
        }
      }
      if (jsonObj.get("hostingEnvironments") != null && !jsonObj.get("hostingEnvironments").isJsonNull()) {
        JsonArray jsonArrayhostingEnvironments = jsonObj.getAsJsonArray("hostingEnvironments");
        if (jsonArrayhostingEnvironments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("hostingEnvironments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `hostingEnvironments` to be an array in the JSON string but got `%s`", jsonObj.get("hostingEnvironments").toString()));
          }

          // validate the optional field `hostingEnvironments` (array)
          for (int i = 0; i < jsonArrayhostingEnvironments.size(); i++) {
            DeploymentLocationsHostingEnvironmentsInner.validateJsonElement(jsonArrayhostingEnvironments.get(i));
          };
        }
      }
      if (jsonObj.get("locations") != null && !jsonObj.get("locations").isJsonNull()) {
        JsonArray jsonArraylocations = jsonObj.getAsJsonArray("locations");
        if (jsonArraylocations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("locations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `locations` to be an array in the JSON string but got `%s`", jsonObj.get("locations").toString()));
          }

          // validate the optional field `locations` (array)
          for (int i = 0; i < jsonArraylocations.size(); i++) {
            GeoRegion.validateJsonElement(jsonArraylocations.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeploymentLocations.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeploymentLocations' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeploymentLocations> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeploymentLocations.class));

       return (TypeAdapter<T>) new TypeAdapter<DeploymentLocations>() {
           @Override
           public void write(JsonWriter out, DeploymentLocations value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeploymentLocations read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeploymentLocations given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeploymentLocations
   * @throws IOException if the JSON string is invalid with respect to DeploymentLocations
   */
  public static DeploymentLocations fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeploymentLocations.class);
  }

  /**
   * Convert an instance of DeploymentLocations to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

