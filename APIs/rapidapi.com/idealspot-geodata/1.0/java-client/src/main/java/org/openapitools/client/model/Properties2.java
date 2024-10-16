/*
 * IdealSpot GeoData
 * Hyperlocal Demographics, Vehicle Traffic, Economic, Market Signals, and More. Use this API to request IdealSpot hyperlocal geospatial market insight and geometry data.   ## Detailed Description  Use this API as your **local economy microscope** by querying [IdealSpot](https://www.idealspot.com) hyperlocal market insight and geometry data. We offer the most precise, extensive, and frequently-updated local market data in the US. Our data is available across the entire US and can be queried at geographic scales ranging from the micro (Census block) through the macro (nation).  Better data and analysis leads to a better understanding of local market opportunities and risks. Integrate with your commercial real estate and marketing applications, machine learning workflows, and other investment analytics.  Our goal is to offer the most complete snapshot of the geographically distributed consumer and retail economy. We start with the fundamentals of consumers and business establishments. To connect retailers with consumers, we provide mobility data like vehicle traffic and mobile device data. To describe consumer intent, we provide geolocated digital marketing data.   We believe that accurate capital allocation through reliable local market data is foundational to creating robust, healthy, and livable communities for all. We hope you and your clients find tremendous value in this service.  ## Features  Query data and GeoJSON geometries at these scales for any US latitude and longitude:  * Rings (0.5 km+) * Drive time (1-60 minutes) * Bike time (3-60 minutes) * Walk time (5-60 minutes) * Public transit time (5-60 minutes) * Administrative region (US, states, core-based statistical areas, counties, Census-designated places, Census tracts, zipcodes, Census block groups, opportunity zones)  | Data Feature | Description | | ------- | ------------------------------| | Demographics, Housing, Spending | *Updated Quarterly*.  Current and historical market data including population, spending, and housing. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Labor, Business Establishments, Economic Conditions | *Updated Quarterly*.  Traditional market data including workforce, business establishment counts, and economic conditions like local GDP, unemployment rates. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Consumer segmentation | *Updated Annually*. Demographics grouped into narrative-oriented segments. | | Vehicle Traffic | *Updated semi-annually*. Gold standard in vehicle traffic data from INRIX. Counts by day of week, time of day and side of street. | | Rings and Travel time polygons | *Estimate in Real-time*. Rings alongside drive time, walk time, bike time, and public transit time polygons. Request as GeoJSON geometries for mapping or use with data queries | | Administrative region polygons | *Updated Annually*. GeoJSON administrative regions from US Census Bureau: block groups, tracts, counties, CBSAs, states, opportunity zones, USPS zipcodes | | Internet Search Volumes | 30 day rolling averages for geolocated advertising potential across 450 business categories from major search engines | | Social Media Interest | 30 day rolling average for geolocated advertising potential across 450 business categories from major social networks |  ### Coming Soon!  This API powers our local market research platform at [IdealSpot.com](https://www.idealspot.com). The functionality exposed so far is only a portion of our current capabilities. We will be exposing additional API features in time so watch this space!  | Data Feature | Description | | ------- | ------------------------------| Mobile device visit counts, points of interest, brands | Fresh point of interest data across 3000+ brands, millions of POI, and historical foot traffic counts using mobile data for those points of interest Origin/destination trips from mobile devices | Map origins and destinations of devices visiting an arbitrary catchment area Competition search | Search all major point-of-interest aggregators in one query Environment/climate | Expected weather patterns like temperature and precipitation Filter search API | Query data for all counties in state, all tracts in MSA, etc Road segment tiles | Plot road segments on maps in interactive applications  ## Developer Website  For more detail see https://developer.idealspot.com/
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
import java.util.Arrays;
import org.openapitools.client.model.Location3;

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
 * Properties2
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:58.672234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Properties2 {
  public static final String SERIALIZED_NAME_CALCULATED_AREA_SQ_METERS = "calculated_area_sq_meters";
  @SerializedName(SERIALIZED_NAME_CALCULATED_AREA_SQ_METERS)
  private Double calculatedAreaSqMeters;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private Location3 location;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private Integer status;

  public Properties2() {
  }

  public Properties2 calculatedAreaSqMeters(Double calculatedAreaSqMeters) {
    this.calculatedAreaSqMeters = calculatedAreaSqMeters;
    return this;
  }

  /**
   * Get calculatedAreaSqMeters
   * @return calculatedAreaSqMeters
   */
  @javax.annotation.Nonnull
  public Double getCalculatedAreaSqMeters() {
    return calculatedAreaSqMeters;
  }

  public void setCalculatedAreaSqMeters(Double calculatedAreaSqMeters) {
    this.calculatedAreaSqMeters = calculatedAreaSqMeters;
  }


  public Properties2 location(Location3 location) {
    this.location = location;
    return this;
  }

  /**
   * Get location
   * @return location
   */
  @javax.annotation.Nonnull
  public Location3 getLocation() {
    return location;
  }

  public void setLocation(Location3 location) {
    this.location = location;
  }


  public Properties2 status(Integer status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public Integer getStatus() {
    return status;
  }

  public void setStatus(Integer status) {
    this.status = status;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Properties2 properties2 = (Properties2) o;
    return Objects.equals(this.calculatedAreaSqMeters, properties2.calculatedAreaSqMeters) &&
        Objects.equals(this.location, properties2.location) &&
        Objects.equals(this.status, properties2.status);
  }

  @Override
  public int hashCode() {
    return Objects.hash(calculatedAreaSqMeters, location, status);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Properties2 {\n");
    sb.append("    calculatedAreaSqMeters: ").append(toIndentedString(calculatedAreaSqMeters)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("calculated_area_sq_meters");
    openapiFields.add("location");
    openapiFields.add("status");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("calculated_area_sq_meters");
    openapiRequiredFields.add("location");
    openapiRequiredFields.add("status");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Properties2
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Properties2.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Properties2 is not found in the empty JSON string", Properties2.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Properties2.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Properties2` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Properties2.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `location`
      Location3.validateJsonElement(jsonObj.get("location"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Properties2.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Properties2' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Properties2> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Properties2.class));

       return (TypeAdapter<T>) new TypeAdapter<Properties2>() {
           @Override
           public void write(JsonWriter out, Properties2 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Properties2 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Properties2 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Properties2
   * @throws IOException if the JSON string is invalid with respect to Properties2
   */
  public static Properties2 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Properties2.class);
  }

  /**
   * Convert an instance of Properties2 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

