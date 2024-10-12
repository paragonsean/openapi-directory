/*
 *  API Client
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
import org.openapitools.client.model.GlobalCsmSkuDescriptionCapabilitiesInner;
import org.openapitools.client.model.GlobalCsmSkuDescriptionCapacity;

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
 * A Global SKU Description.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:50.427441-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GlobalCsmSkuDescription {
  public static final String SERIALIZED_NAME_CAPABILITIES = "capabilities";
  @SerializedName(SERIALIZED_NAME_CAPABILITIES)
  private List<GlobalCsmSkuDescriptionCapabilitiesInner> capabilities = new ArrayList<>();

  public static final String SERIALIZED_NAME_CAPACITY = "capacity";
  @SerializedName(SERIALIZED_NAME_CAPACITY)
  private GlobalCsmSkuDescriptionCapacity capacity;

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

  public static final String SERIALIZED_NAME_TIER = "tier";
  @SerializedName(SERIALIZED_NAME_TIER)
  private String tier;

  public GlobalCsmSkuDescription() {
  }

  public GlobalCsmSkuDescription capabilities(List<GlobalCsmSkuDescriptionCapabilitiesInner> capabilities) {
    this.capabilities = capabilities;
    return this;
  }

  public GlobalCsmSkuDescription addCapabilitiesItem(GlobalCsmSkuDescriptionCapabilitiesInner capabilitiesItem) {
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
  public List<GlobalCsmSkuDescriptionCapabilitiesInner> getCapabilities() {
    return capabilities;
  }

  public void setCapabilities(List<GlobalCsmSkuDescriptionCapabilitiesInner> capabilities) {
    this.capabilities = capabilities;
  }


  public GlobalCsmSkuDescription capacity(GlobalCsmSkuDescriptionCapacity capacity) {
    this.capacity = capacity;
    return this;
  }

  /**
   * Get capacity
   * @return capacity
   */
  @javax.annotation.Nullable
  public GlobalCsmSkuDescriptionCapacity getCapacity() {
    return capacity;
  }

  public void setCapacity(GlobalCsmSkuDescriptionCapacity capacity) {
    this.capacity = capacity;
  }


  public GlobalCsmSkuDescription family(String family) {
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


  public GlobalCsmSkuDescription locations(List<String> locations) {
    this.locations = locations;
    return this;
  }

  public GlobalCsmSkuDescription addLocationsItem(String locationsItem) {
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


  public GlobalCsmSkuDescription name(String name) {
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


  public GlobalCsmSkuDescription size(String size) {
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


  public GlobalCsmSkuDescription tier(String tier) {
    this.tier = tier;
    return this;
  }

  /**
   * Service Tier of the resource SKU.
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
    GlobalCsmSkuDescription globalCsmSkuDescription = (GlobalCsmSkuDescription) o;
    return Objects.equals(this.capabilities, globalCsmSkuDescription.capabilities) &&
        Objects.equals(this.capacity, globalCsmSkuDescription.capacity) &&
        Objects.equals(this.family, globalCsmSkuDescription.family) &&
        Objects.equals(this.locations, globalCsmSkuDescription.locations) &&
        Objects.equals(this.name, globalCsmSkuDescription.name) &&
        Objects.equals(this.size, globalCsmSkuDescription.size) &&
        Objects.equals(this.tier, globalCsmSkuDescription.tier);
  }

  @Override
  public int hashCode() {
    return Objects.hash(capabilities, capacity, family, locations, name, size, tier);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GlobalCsmSkuDescription {\n");
    sb.append("    capabilities: ").append(toIndentedString(capabilities)).append("\n");
    sb.append("    capacity: ").append(toIndentedString(capacity)).append("\n");
    sb.append("    family: ").append(toIndentedString(family)).append("\n");
    sb.append("    locations: ").append(toIndentedString(locations)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
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
    openapiFields.add("tier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GlobalCsmSkuDescription
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GlobalCsmSkuDescription.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GlobalCsmSkuDescription is not found in the empty JSON string", GlobalCsmSkuDescription.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GlobalCsmSkuDescription.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GlobalCsmSkuDescription` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            GlobalCsmSkuDescriptionCapabilitiesInner.validateJsonElement(jsonArraycapabilities.get(i));
          };
        }
      }
      // validate the optional field `capacity`
      if (jsonObj.get("capacity") != null && !jsonObj.get("capacity").isJsonNull()) {
        GlobalCsmSkuDescriptionCapacity.validateJsonElement(jsonObj.get("capacity"));
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
      if ((jsonObj.get("tier") != null && !jsonObj.get("tier").isJsonNull()) && !jsonObj.get("tier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tier").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GlobalCsmSkuDescription.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GlobalCsmSkuDescription' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GlobalCsmSkuDescription> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GlobalCsmSkuDescription.class));

       return (TypeAdapter<T>) new TypeAdapter<GlobalCsmSkuDescription>() {
           @Override
           public void write(JsonWriter out, GlobalCsmSkuDescription value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GlobalCsmSkuDescription read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GlobalCsmSkuDescription given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GlobalCsmSkuDescription
   * @throws IOException if the JSON string is invalid with respect to GlobalCsmSkuDescription
   */
  public static GlobalCsmSkuDescription fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GlobalCsmSkuDescription.class);
  }

  /**
   * Convert an instance of GlobalCsmSkuDescription to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

