/*
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
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
import org.openapitools.client.model.ExtendedOriginDestinationLight;
import org.openapitools.client.model.ExtendedSearchCriteria;
import org.openapitools.client.model.FlightOfferSource;
import org.openapitools.client.model.TravelerInfo;

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
 * GetFlightAvailabilitiesQuery
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:18.707859-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetFlightAvailabilitiesQuery {
  public static final String SERIALIZED_NAME_ORIGIN_DESTINATIONS = "originDestinations";
  @SerializedName(SERIALIZED_NAME_ORIGIN_DESTINATIONS)
  private List<ExtendedOriginDestinationLight> originDestinations = new ArrayList<>();

  public static final String SERIALIZED_NAME_SEARCH_CRITERIA = "searchCriteria";
  @SerializedName(SERIALIZED_NAME_SEARCH_CRITERIA)
  private ExtendedSearchCriteria searchCriteria;

  public static final String SERIALIZED_NAME_SOURCES = "sources";
  @SerializedName(SERIALIZED_NAME_SOURCES)
  private List<FlightOfferSource> sources = new ArrayList<>();

  public static final String SERIALIZED_NAME_TRAVELERS = "travelers";
  @SerializedName(SERIALIZED_NAME_TRAVELERS)
  private List<TravelerInfo> travelers = new ArrayList<>();

  public GetFlightAvailabilitiesQuery() {
  }

  public GetFlightAvailabilitiesQuery originDestinations(List<ExtendedOriginDestinationLight> originDestinations) {
    this.originDestinations = originDestinations;
    return this;
  }

  public GetFlightAvailabilitiesQuery addOriginDestinationsItem(ExtendedOriginDestinationLight originDestinationsItem) {
    if (this.originDestinations == null) {
      this.originDestinations = new ArrayList<>();
    }
    this.originDestinations.add(originDestinationsItem);
    return this;
  }

  /**
   * Origins and Destinations must be properly ordered in time (chronological order in accordance with the timezone of each location) to describe the journey consistently. Dates and times must not be past nor more than 365 days in the future, according to provider settings.Number of Origins and Destinations must not exceed the limit defined in provider settings.
   * @return originDestinations
   */
  @javax.annotation.Nonnull
  public List<ExtendedOriginDestinationLight> getOriginDestinations() {
    return originDestinations;
  }

  public void setOriginDestinations(List<ExtendedOriginDestinationLight> originDestinations) {
    this.originDestinations = originDestinations;
  }


  public GetFlightAvailabilitiesQuery searchCriteria(ExtendedSearchCriteria searchCriteria) {
    this.searchCriteria = searchCriteria;
    return this;
  }

  /**
   * Get searchCriteria
   * @return searchCriteria
   */
  @javax.annotation.Nullable
  public ExtendedSearchCriteria getSearchCriteria() {
    return searchCriteria;
  }

  public void setSearchCriteria(ExtendedSearchCriteria searchCriteria) {
    this.searchCriteria = searchCriteria;
  }


  public GetFlightAvailabilitiesQuery sources(List<FlightOfferSource> sources) {
    this.sources = sources;
    return this;
  }

  public GetFlightAvailabilitiesQuery addSourcesItem(FlightOfferSource sourcesItem) {
    if (this.sources == null) {
      this.sources = new ArrayList<>();
    }
    this.sources.add(sourcesItem);
    return this;
  }

  /**
   * Allows enable one or more sources. If present in the list, these sources will be called by the system.  GDS : Full service carriers
   * @return sources
   */
  @javax.annotation.Nonnull
  public List<FlightOfferSource> getSources() {
    return sources;
  }

  public void setSources(List<FlightOfferSource> sources) {
    this.sources = sources;
  }


  public GetFlightAvailabilitiesQuery travelers(List<TravelerInfo> travelers) {
    this.travelers = travelers;
    return this;
  }

  public GetFlightAvailabilitiesQuery addTravelersItem(TravelerInfo travelersItem) {
    if (this.travelers == null) {
      this.travelers = new ArrayList<>();
    }
    this.travelers.add(travelersItem);
    return this;
  }

  /**
   * List of travelers composing the travel
   * @return travelers
   */
  @javax.annotation.Nonnull
  public List<TravelerInfo> getTravelers() {
    return travelers;
  }

  public void setTravelers(List<TravelerInfo> travelers) {
    this.travelers = travelers;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetFlightAvailabilitiesQuery getFlightAvailabilitiesQuery = (GetFlightAvailabilitiesQuery) o;
    return Objects.equals(this.originDestinations, getFlightAvailabilitiesQuery.originDestinations) &&
        Objects.equals(this.searchCriteria, getFlightAvailabilitiesQuery.searchCriteria) &&
        Objects.equals(this.sources, getFlightAvailabilitiesQuery.sources) &&
        Objects.equals(this.travelers, getFlightAvailabilitiesQuery.travelers);
  }

  @Override
  public int hashCode() {
    return Objects.hash(originDestinations, searchCriteria, sources, travelers);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetFlightAvailabilitiesQuery {\n");
    sb.append("    originDestinations: ").append(toIndentedString(originDestinations)).append("\n");
    sb.append("    searchCriteria: ").append(toIndentedString(searchCriteria)).append("\n");
    sb.append("    sources: ").append(toIndentedString(sources)).append("\n");
    sb.append("    travelers: ").append(toIndentedString(travelers)).append("\n");
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
    openapiFields.add("originDestinations");
    openapiFields.add("searchCriteria");
    openapiFields.add("sources");
    openapiFields.add("travelers");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("originDestinations");
    openapiRequiredFields.add("sources");
    openapiRequiredFields.add("travelers");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetFlightAvailabilitiesQuery
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetFlightAvailabilitiesQuery.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetFlightAvailabilitiesQuery is not found in the empty JSON string", GetFlightAvailabilitiesQuery.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetFlightAvailabilitiesQuery.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetFlightAvailabilitiesQuery` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GetFlightAvailabilitiesQuery.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("originDestinations").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `originDestinations` to be an array in the JSON string but got `%s`", jsonObj.get("originDestinations").toString()));
      }

      JsonArray jsonArrayoriginDestinations = jsonObj.getAsJsonArray("originDestinations");
      // validate the required field `originDestinations` (array)
      for (int i = 0; i < jsonArrayoriginDestinations.size(); i++) {
        ExtendedOriginDestinationLight.validateJsonElement(jsonArrayoriginDestinations.get(i));
      };
      // validate the optional field `searchCriteria`
      if (jsonObj.get("searchCriteria") != null && !jsonObj.get("searchCriteria").isJsonNull()) {
        ExtendedSearchCriteria.validateJsonElement(jsonObj.get("searchCriteria"));
      }
      // ensure the required json array is present
      if (jsonObj.get("sources") == null) {
        throw new IllegalArgumentException("Expected the field `linkedContent` to be an array in the JSON string but got `null`");
      } else if (!jsonObj.get("sources").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `sources` to be an array in the JSON string but got `%s`", jsonObj.get("sources").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("travelers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `travelers` to be an array in the JSON string but got `%s`", jsonObj.get("travelers").toString()));
      }

      JsonArray jsonArraytravelers = jsonObj.getAsJsonArray("travelers");
      // validate the required field `travelers` (array)
      for (int i = 0; i < jsonArraytravelers.size(); i++) {
        TravelerInfo.validateJsonElement(jsonArraytravelers.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetFlightAvailabilitiesQuery.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetFlightAvailabilitiesQuery' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetFlightAvailabilitiesQuery> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetFlightAvailabilitiesQuery.class));

       return (TypeAdapter<T>) new TypeAdapter<GetFlightAvailabilitiesQuery>() {
           @Override
           public void write(JsonWriter out, GetFlightAvailabilitiesQuery value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetFlightAvailabilitiesQuery read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetFlightAvailabilitiesQuery given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetFlightAvailabilitiesQuery
   * @throws IOException if the JSON string is invalid with respect to GetFlightAvailabilitiesQuery
   */
  public static GetFlightAvailabilitiesQuery fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetFlightAvailabilitiesQuery.class);
  }

  /**
   * Convert an instance of GetFlightAvailabilitiesQuery to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

