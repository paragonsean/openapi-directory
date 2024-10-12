/*
 * FaSta - Station Facilities Status
 * A RESTful webservice to retrieve data about the operational state of public elevators and escalators in german railway stations.
 *
 * The version of the OpenAPI document: 2.1
 * Contact: michael.binzen@deutschebahn.com
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
import org.openapitools.client.model.Facility;

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
 * Station
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:24.514116-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Station {
  public static final String SERIALIZED_NAME_FACILITIES = "facilities";
  @SerializedName(SERIALIZED_NAME_FACILITIES)
  private List<Facility> facilities = new ArrayList<>();

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_STATIONNUMBER = "stationnumber";
  @SerializedName(SERIALIZED_NAME_STATIONNUMBER)
  private Long stationnumber;

  public Station() {
  }

  public Station facilities(List<Facility> facilities) {
    this.facilities = facilities;
    return this;
  }

  public Station addFacilitiesItem(Facility facilitiesItem) {
    if (this.facilities == null) {
      this.facilities = new ArrayList<>();
    }
    this.facilities.add(facilitiesItem);
    return this;
  }

  /**
   * Get facilities
   * @return facilities
   */
  @javax.annotation.Nullable
  public List<Facility> getFacilities() {
    return facilities;
  }

  public void setFacilities(List<Facility> facilities) {
    this.facilities = facilities;
  }


  public Station name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the station.
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Station stationnumber(Long stationnumber) {
    this.stationnumber = stationnumber;
    return this;
  }

  /**
   * Unique identifier of the station.
   * @return stationnumber
   */
  @javax.annotation.Nonnull
  public Long getStationnumber() {
    return stationnumber;
  }

  public void setStationnumber(Long stationnumber) {
    this.stationnumber = stationnumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Station station = (Station) o;
    return Objects.equals(this.facilities, station.facilities) &&
        Objects.equals(this.name, station.name) &&
        Objects.equals(this.stationnumber, station.stationnumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(facilities, name, stationnumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Station {\n");
    sb.append("    facilities: ").append(toIndentedString(facilities)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    stationnumber: ").append(toIndentedString(stationnumber)).append("\n");
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
    openapiFields.add("facilities");
    openapiFields.add("name");
    openapiFields.add("stationnumber");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("stationnumber");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Station
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Station.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Station is not found in the empty JSON string", Station.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Station.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Station` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Station.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("facilities") != null && !jsonObj.get("facilities").isJsonNull()) {
        JsonArray jsonArrayfacilities = jsonObj.getAsJsonArray("facilities");
        if (jsonArrayfacilities != null) {
          // ensure the json data is an array
          if (!jsonObj.get("facilities").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `facilities` to be an array in the JSON string but got `%s`", jsonObj.get("facilities").toString()));
          }

          // validate the optional field `facilities` (array)
          for (int i = 0; i < jsonArrayfacilities.size(); i++) {
            Facility.validateJsonElement(jsonArrayfacilities.get(i));
          };
        }
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Station.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Station' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Station> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Station.class));

       return (TypeAdapter<T>) new TypeAdapter<Station>() {
           @Override
           public void write(JsonWriter out, Station value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Station read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Station given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Station
   * @throws IOException if the JSON string is invalid with respect to Station
   */
  public static Station fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Station.class);
  }

  /**
   * Convert an instance of Station to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

