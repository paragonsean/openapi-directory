/*
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
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
import java.time.OffsetDateTime;
import java.util.Arrays;

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
 * details of stops for direct or change of gauge flights
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:02:43.649656-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FlightStop {
  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private String duration;

  public static final String SERIALIZED_NAME_IATA_CODE = "iataCode";
  @SerializedName(SERIALIZED_NAME_IATA_CODE)
  private String iataCode;

  public static final String SERIALIZED_NAME_ARRIVAL_AT = "arrivalAt";
  @SerializedName(SERIALIZED_NAME_ARRIVAL_AT)
  private OffsetDateTime arrivalAt;

  public static final String SERIALIZED_NAME_DEPARTURE_AT = "departureAt";
  @SerializedName(SERIALIZED_NAME_DEPARTURE_AT)
  private OffsetDateTime departureAt;

  public FlightStop() {
  }

  public FlightStop duration(String duration) {
    this.duration = duration;
    return this;
  }

  /**
   * stop duration in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) PnYnMnDTnHnMnS format, e.g. PT2H10M
   * @return duration
   */
  @javax.annotation.Nullable
  public String getDuration() {
    return duration;
  }

  public void setDuration(String duration) {
    this.duration = duration;
  }


  public FlightStop iataCode(String iataCode) {
    this.iataCode = iataCode;
    return this;
  }

  /**
   * [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx)
   * @return iataCode
   */
  @javax.annotation.Nullable
  public String getIataCode() {
    return iataCode;
  }

  public void setIataCode(String iataCode) {
    this.iataCode = iataCode;
  }


  public FlightStop arrivalAt(OffsetDateTime arrivalAt) {
    this.arrivalAt = arrivalAt;
    return this;
  }

  /**
   * arrival at the stop in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-ddThh:mm:ss format, e.g. 2017-02-10T20:40:00
   * @return arrivalAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getArrivalAt() {
    return arrivalAt;
  }

  public void setArrivalAt(OffsetDateTime arrivalAt) {
    this.arrivalAt = arrivalAt;
  }


  public FlightStop departureAt(OffsetDateTime departureAt) {
    this.departureAt = departureAt;
    return this;
  }

  /**
   * departure from the stop in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-ddThh:mm:ss format, e.g. 2017-02-10T20:40:00
   * @return departureAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDepartureAt() {
    return departureAt;
  }

  public void setDepartureAt(OffsetDateTime departureAt) {
    this.departureAt = departureAt;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FlightStop flightStop = (FlightStop) o;
    return Objects.equals(this.duration, flightStop.duration) &&
        Objects.equals(this.iataCode, flightStop.iataCode) &&
        Objects.equals(this.arrivalAt, flightStop.arrivalAt) &&
        Objects.equals(this.departureAt, flightStop.departureAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(duration, iataCode, arrivalAt, departureAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlightStop {\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    iataCode: ").append(toIndentedString(iataCode)).append("\n");
    sb.append("    arrivalAt: ").append(toIndentedString(arrivalAt)).append("\n");
    sb.append("    departureAt: ").append(toIndentedString(departureAt)).append("\n");
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
    openapiFields.add("duration");
    openapiFields.add("iataCode");
    openapiFields.add("arrivalAt");
    openapiFields.add("departureAt");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FlightStop
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FlightStop.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FlightStop is not found in the empty JSON string", FlightStop.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FlightStop.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FlightStop` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("duration") != null && !jsonObj.get("duration").isJsonNull()) && !jsonObj.get("duration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `duration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("duration").toString()));
      }
      if ((jsonObj.get("iataCode") != null && !jsonObj.get("iataCode").isJsonNull()) && !jsonObj.get("iataCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iataCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iataCode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FlightStop.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FlightStop' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FlightStop> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FlightStop.class));

       return (TypeAdapter<T>) new TypeAdapter<FlightStop>() {
           @Override
           public void write(JsonWriter out, FlightStop value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FlightStop read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FlightStop given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FlightStop
   * @throws IOException if the JSON string is invalid with respect to FlightStop
   */
  public static FlightStop fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FlightStop.class);
  }

  /**
   * Convert an instance of FlightStop to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

