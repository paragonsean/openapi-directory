/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
import org.openapitools.client.model.AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner;
import org.openapitools.client.model.AppServicePlansList200ResponseValueInnerSkuSkuCapacity;

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
 * Description of a SKU for a scalable resource.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:50.309367-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansList200ResponseValueInnerSku {
  public static final String SERIALIZED_NAME_CAPABILITIES = "capabilities";
  @SerializedName(SERIALIZED_NAME_CAPABILITIES)
  private List<AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner> capabilities = new ArrayList<>();

  public static final String SERIALIZED_NAME_CAPACITY = "capacity";
  @SerializedName(SERIALIZED_NAME_CAPACITY)
  private Integer capacity;

  public static final String SERIALIZED_NAME_FAMILY = "family";
  @SerializedName(SERIALIZED_NAME_FAMILY)
  private String family;

  public static final String SERIALIZED_NAME_LOCATIONS = "locations";
  @SerializedName(SERIALIZED_NAME_LOCATIONS)
  private List<String> locations = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private String size;

  public static final String SERIALIZED_NAME_SKU_CAPACITY = "skuCapacity";
  @SerializedName(SERIALIZED_NAME_SKU_CAPACITY)
  private AppServicePlansList200ResponseValueInnerSkuSkuCapacity skuCapacity;

  public static final String SERIALIZED_NAME_TIER = "tier";
  @SerializedName(SERIALIZED_NAME_TIER)
  private String tier;

  public AppServicePlansList200ResponseValueInnerSku() {
  }

  public AppServicePlansList200ResponseValueInnerSku capabilities(List<AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner> capabilities) {
    this.capabilities = capabilities;
    return this;
  }

  public AppServicePlansList200ResponseValueInnerSku addCapabilitiesItem(AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner capabilitiesItem) {
    if (this.capabilities == null) {
      this.capabilities = new ArrayList<>();
    }
    this.capabilities.add(capabilitiesItem);
    return this;
  }

  /**
   * Capabilities of the SKU, e.g., is traffic manager enabled?
   * @return capabilities
   */
  @javax.annotation.Nullable
  public List<AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner> getCapabilities() {
    return capabilities;
  }

  public void setCapabilities(List<AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner> capabilities) {
    this.capabilities = capabilities;
  }


  public AppServicePlansList200ResponseValueInnerSku capacity(Integer capacity) {
    this.capacity = capacity;
    return this;
  }

  /**
   * Current number of instances assigned to the resource.
   * @return capacity
   */
  @javax.annotation.Nullable
  public Integer getCapacity() {
    return capacity;
  }

  public void setCapacity(Integer capacity) {
    this.capacity = capacity;
  }


  public AppServicePlansList200ResponseValueInnerSku family(String family) {
    this.family = family;
    return this;
  }

  /**
   * Family code of the resource SKU.
   * @return family
   */
  @javax.annotation.Nullable
  public String getFamily() {
    return family;
  }

  public void setFamily(String family) {
    this.family = family;
  }


  public AppServicePlansList200ResponseValueInnerSku locations(List<String> locations) {
    this.locations = locations;
    return this;
  }

  public AppServicePlansList200ResponseValueInnerSku addLocationsItem(String locationsItem) {
    if (this.locations == null) {
      this.locations = new ArrayList<>();
    }
    this.locations.add(locationsItem);
    return this;
  }

  /**
   * Locations of the SKU.
   * @return locations
   */
  @javax.annotation.Nullable
  public List<String> getLocations() {
    return locations;
  }

  public void setLocations(List<String> locations) {
    this.locations = locations;
  }


  public AppServicePlansList200ResponseValueInnerSku name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the resource SKU.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public AppServicePlansList200ResponseValueInnerSku size(String size) {
    this.size = size;
    return this;
  }

  /**
   * Size specifier of the resource SKU.
   * @return size
   */
  @javax.annotation.Nullable
  public String getSize() {
    return size;
  }

  public void setSize(String size) {
    this.size = size;
  }


  public AppServicePlansList200ResponseValueInnerSku skuCapacity(AppServicePlansList200ResponseValueInnerSkuSkuCapacity skuCapacity) {
    this.skuCapacity = skuCapacity;
    return this;
  }

  /**
   * Get skuCapacity
   * @return skuCapacity
   */
  @javax.annotation.Nullable
  public AppServicePlansList200ResponseValueInnerSkuSkuCapacity getSkuCapacity() {
    return skuCapacity;
  }

  public void setSkuCapacity(AppServicePlansList200ResponseValueInnerSkuSkuCapacity skuCapacity) {
    this.skuCapacity = skuCapacity;
  }


  public AppServicePlansList200ResponseValueInnerSku tier(String tier) {
    this.tier = tier;
    return this;
  }

  /**
   * Service tier of the resource SKU.
   * @return tier
   */
  @javax.annotation.Nullable
  public String getTier() {
    return tier;
  }

  public void setTier(String tier) {
    this.tier = tier;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansList200ResponseValueInnerSku appServicePlansList200ResponseValueInnerSku = (AppServicePlansList200ResponseValueInnerSku) o;
    return Objects.equals(this.capabilities, appServicePlansList200ResponseValueInnerSku.capabilities) &&
        Objects.equals(this.capacity, appServicePlansList200ResponseValueInnerSku.capacity) &&
        Objects.equals(this.family, appServicePlansList200ResponseValueInnerSku.family) &&
        Objects.equals(this.locations, appServicePlansList200ResponseValueInnerSku.locations) &&
        Objects.equals(this.name, appServicePlansList200ResponseValueInnerSku.name) &&
        Objects.equals(this.size, appServicePlansList200ResponseValueInnerSku.size) &&
        Objects.equals(this.skuCapacity, appServicePlansList200ResponseValueInnerSku.skuCapacity) &&
        Objects.equals(this.tier, appServicePlansList200ResponseValueInnerSku.tier);
  }

  @Override
  public int hashCode() {
    return Objects.hash(capabilities, capacity, family, locations, name, size, skuCapacity, tier);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansList200ResponseValueInnerSku {\n");
    sb.append("    capabilities: ").append(toIndentedString(capabilities)).append("\n");
    sb.append("    capacity: ").append(toIndentedString(capacity)).append("\n");
    sb.append("    family: ").append(toIndentedString(family)).append("\n");
    sb.append("    locations: ").append(toIndentedString(locations)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    skuCapacity: ").append(toIndentedString(skuCapacity)).append("\n");
    sb.append("    tier: ").append(toIndentedString(tier)).append("\n");
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
    openapiFields.add("capabilities");
    openapiFields.add("capacity");
    openapiFields.add("family");
    openapiFields.add("locations");
    openapiFields.add("name");
    openapiFields.add("size");
    openapiFields.add("skuCapacity");
    openapiFields.add("tier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansList200ResponseValueInnerSku
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansList200ResponseValueInnerSku.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansList200ResponseValueInnerSku is not found in the empty JSON string", AppServicePlansList200ResponseValueInnerSku.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansList200ResponseValueInnerSku.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansList200ResponseValueInnerSku` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("capabilities") != null && !jsonObj.get("capabilities").isJsonNull()) {
        JsonArray jsonArraycapabilities = jsonObj.getAsJsonArray("capabilities");
        if (jsonArraycapabilities != null) {
          // ensure the json data is an array
          if (!jsonObj.get("capabilities").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `capabilities` to be an array in the JSON string but got `%s`", jsonObj.get("capabilities").toString()));
          }

          // validate the optional field `capabilities` (array)
          for (int i = 0; i < jsonArraycapabilities.size(); i++) {
            AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner.validateJsonElement(jsonArraycapabilities.get(i));
          };
        }
      }
      if ((jsonObj.get("family") != null && !jsonObj.get("family").isJsonNull()) && !jsonObj.get("family").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `family` to be a primitive type in the JSON string but got `%s`", jsonObj.get("family").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("locations") != null && !jsonObj.get("locations").isJsonNull() && !jsonObj.get("locations").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `locations` to be an array in the JSON string but got `%s`", jsonObj.get("locations").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("size") != null && !jsonObj.get("size").isJsonNull()) && !jsonObj.get("size").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `size` to be a primitive type in the JSON string but got `%s`", jsonObj.get("size").toString()));
      }
      // validate the optional field `skuCapacity`
      if (jsonObj.get("skuCapacity") != null && !jsonObj.get("skuCapacity").isJsonNull()) {
        AppServicePlansList200ResponseValueInnerSkuSkuCapacity.validateJsonElement(jsonObj.get("skuCapacity"));
      }
      if ((jsonObj.get("tier") != null && !jsonObj.get("tier").isJsonNull()) && !jsonObj.get("tier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tier").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansList200ResponseValueInnerSku.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansList200ResponseValueInnerSku' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansList200ResponseValueInnerSku> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansList200ResponseValueInnerSku.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansList200ResponseValueInnerSku>() {
           @Override
           public void write(JsonWriter out, AppServicePlansList200ResponseValueInnerSku value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansList200ResponseValueInnerSku read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansList200ResponseValueInnerSku given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansList200ResponseValueInnerSku
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansList200ResponseValueInnerSku
   */
  public static AppServicePlansList200ResponseValueInnerSku fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansList200ResponseValueInnerSku.class);
  }

  /**
   * Convert an instance of AppServicePlansList200ResponseValueInnerSku to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

