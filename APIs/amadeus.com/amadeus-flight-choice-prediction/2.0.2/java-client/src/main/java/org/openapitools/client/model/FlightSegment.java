/*
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
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
import org.openapitools.client.model.AircraftEquipment;
import org.openapitools.client.model.FlightEndPoint;
import org.openapitools.client.model.FlightStop;
import org.openapitools.client.model.OperatingFlight;

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
 * defining a flight segment; including both operating and marketing details when applicable
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:40.682879-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FlightSegment {
  public static final String SERIALIZED_NAME_AIRCRAFT = "aircraft";
  @SerializedName(SERIALIZED_NAME_AIRCRAFT)
  private AircraftEquipment aircraft;

  public static final String SERIALIZED_NAME_ARRIVAL = "arrival";
  @SerializedName(SERIALIZED_NAME_ARRIVAL)
  private FlightEndPoint arrival;

  public static final String SERIALIZED_NAME_CABIN = "cabin";
  @SerializedName(SERIALIZED_NAME_CABIN)
  private String cabin;

  public static final String SERIALIZED_NAME_CARRIER_CODE = "carrierCode";
  @SerializedName(SERIALIZED_NAME_CARRIER_CODE)
  private String carrierCode;

  public static final String SERIALIZED_NAME_PROPERTY_CLASS = "class";
  @SerializedName(SERIALIZED_NAME_PROPERTY_CLASS)
  private String propertyClass;

  public static final String SERIALIZED_NAME_DEPARTURE = "departure";
  @SerializedName(SERIALIZED_NAME_DEPARTURE)
  private FlightEndPoint departure;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private String duration;

  public static final String SERIALIZED_NAME_NUMBER = "number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private String number;

  public static final String SERIALIZED_NAME_OPERATING = "operating";
  @SerializedName(SERIALIZED_NAME_OPERATING)
  private OperatingFlight operating;

  public static final String SERIALIZED_NAME_STOPS = "stops";
  @SerializedName(SERIALIZED_NAME_STOPS)
  private List<FlightStop> stops = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUFFIX = "suffix";
  @SerializedName(SERIALIZED_NAME_SUFFIX)
  private String suffix;

  public FlightSegment() {
  }

  public FlightSegment aircraft(AircraftEquipment aircraft) {
    this.aircraft = aircraft;
    return this;
  }

  /**
   * Get aircraft
   * @return aircraft
   */
  @javax.annotation.Nullable
  public AircraftEquipment getAircraft() {
    return aircraft;
  }

  public void setAircraft(AircraftEquipment aircraft) {
    this.aircraft = aircraft;
  }


  public FlightSegment arrival(FlightEndPoint arrival) {
    this.arrival = arrival;
    return this;
  }

  /**
   * Get arrival
   * @return arrival
   */
  @javax.annotation.Nullable
  public FlightEndPoint getArrival() {
    return arrival;
  }

  public void setArrival(FlightEndPoint arrival) {
    this.arrival = arrival;
  }


  public FlightSegment cabin(String cabin) {
    this.cabin = cabin;
    return this;
  }

  /**
   * booking cabin / class of service of the carrier
   * @return cabin
   */
  @javax.annotation.Nullable
  public String getCabin() {
    return cabin;
  }

  public void setCabin(String cabin) {
    this.cabin = cabin;
  }


  public FlightSegment carrierCode(String carrierCode) {
    this.carrierCode = carrierCode;
    return this;
  }

  /**
   * providing the airline / carrier code
   * @return carrierCode
   */
  @javax.annotation.Nullable
  public String getCarrierCode() {
    return carrierCode;
  }

  public void setCarrierCode(String carrierCode) {
    this.carrierCode = carrierCode;
  }


  public FlightSegment propertyClass(String propertyClass) {
    this.propertyClass = propertyClass;
    return this;
  }

  /**
   * reservation booking designator (RBD) of the carrier
   * @return propertyClass
   */
  @javax.annotation.Nullable
  public String getPropertyClass() {
    return propertyClass;
  }

  public void setPropertyClass(String propertyClass) {
    this.propertyClass = propertyClass;
  }


  public FlightSegment departure(FlightEndPoint departure) {
    this.departure = departure;
    return this;
  }

  /**
   * Get departure
   * @return departure
   */
  @javax.annotation.Nullable
  public FlightEndPoint getDeparture() {
    return departure;
  }

  public void setDeparture(FlightEndPoint departure) {
    this.departure = departure;
  }


  public FlightSegment duration(String duration) {
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


  public FlightSegment number(String number) {
    this.number = number;
    return this;
  }

  /**
   * the flight number as assigned by the carrier
   * @return number
   */
  @javax.annotation.Nullable
  public String getNumber() {
    return number;
  }

  public void setNumber(String number) {
    this.number = number;
  }


  public FlightSegment operating(OperatingFlight operating) {
    this.operating = operating;
    return this;
  }

  /**
   * Get operating
   * @return operating
   */
  @javax.annotation.Nullable
  public OperatingFlight getOperating() {
    return operating;
  }

  public void setOperating(OperatingFlight operating) {
    this.operating = operating;
  }


  public FlightSegment stops(List<FlightStop> stops) {
    this.stops = stops;
    return this;
  }

  public FlightSegment addStopsItem(FlightStop stopsItem) {
    if (this.stops == null) {
      this.stops = new ArrayList<>();
    }
    this.stops.add(stopsItem);
    return this;
  }

  /**
   * information regarding the different stops composing the flight segment. E.g. technical stop, change of gauge...
   * @return stops
   */
  @javax.annotation.Nullable
  public List<FlightStop> getStops() {
    return stops;
  }

  public void setStops(List<FlightStop> stops) {
    this.stops = stops;
  }


  public FlightSegment suffix(String suffix) {
    this.suffix = suffix;
    return this;
  }

  /**
   * the flight number suffix as assigned by the carrier
   * @return suffix
   */
  @javax.annotation.Nullable
  public String getSuffix() {
    return suffix;
  }

  public void setSuffix(String suffix) {
    this.suffix = suffix;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FlightSegment flightSegment = (FlightSegment) o;
    return Objects.equals(this.aircraft, flightSegment.aircraft) &&
        Objects.equals(this.arrival, flightSegment.arrival) &&
        Objects.equals(this.cabin, flightSegment.cabin) &&
        Objects.equals(this.carrierCode, flightSegment.carrierCode) &&
        Objects.equals(this.propertyClass, flightSegment.propertyClass) &&
        Objects.equals(this.departure, flightSegment.departure) &&
        Objects.equals(this.duration, flightSegment.duration) &&
        Objects.equals(this.number, flightSegment.number) &&
        Objects.equals(this.operating, flightSegment.operating) &&
        Objects.equals(this.stops, flightSegment.stops) &&
        Objects.equals(this.suffix, flightSegment.suffix);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aircraft, arrival, cabin, carrierCode, propertyClass, departure, duration, number, operating, stops, suffix);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlightSegment {\n");
    sb.append("    aircraft: ").append(toIndentedString(aircraft)).append("\n");
    sb.append("    arrival: ").append(toIndentedString(arrival)).append("\n");
    sb.append("    cabin: ").append(toIndentedString(cabin)).append("\n");
    sb.append("    carrierCode: ").append(toIndentedString(carrierCode)).append("\n");
    sb.append("    propertyClass: ").append(toIndentedString(propertyClass)).append("\n");
    sb.append("    departure: ").append(toIndentedString(departure)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    operating: ").append(toIndentedString(operating)).append("\n");
    sb.append("    stops: ").append(toIndentedString(stops)).append("\n");
    sb.append("    suffix: ").append(toIndentedString(suffix)).append("\n");
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
    openapiFields.add("aircraft");
    openapiFields.add("arrival");
    openapiFields.add("cabin");
    openapiFields.add("carrierCode");
    openapiFields.add("class");
    openapiFields.add("departure");
    openapiFields.add("duration");
    openapiFields.add("number");
    openapiFields.add("operating");
    openapiFields.add("stops");
    openapiFields.add("suffix");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FlightSegment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FlightSegment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FlightSegment is not found in the empty JSON string", FlightSegment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FlightSegment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FlightSegment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `aircraft`
      if (jsonObj.get("aircraft") != null && !jsonObj.get("aircraft").isJsonNull()) {
        AircraftEquipment.validateJsonElement(jsonObj.get("aircraft"));
      }
      // validate the optional field `arrival`
      if (jsonObj.get("arrival") != null && !jsonObj.get("arrival").isJsonNull()) {
        FlightEndPoint.validateJsonElement(jsonObj.get("arrival"));
      }
      if ((jsonObj.get("cabin") != null && !jsonObj.get("cabin").isJsonNull()) && !jsonObj.get("cabin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cabin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cabin").toString()));
      }
      if ((jsonObj.get("carrierCode") != null && !jsonObj.get("carrierCode").isJsonNull()) && !jsonObj.get("carrierCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrierCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrierCode").toString()));
      }
      if ((jsonObj.get("class") != null && !jsonObj.get("class").isJsonNull()) && !jsonObj.get("class").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `class` to be a primitive type in the JSON string but got `%s`", jsonObj.get("class").toString()));
      }
      // validate the optional field `departure`
      if (jsonObj.get("departure") != null && !jsonObj.get("departure").isJsonNull()) {
        FlightEndPoint.validateJsonElement(jsonObj.get("departure"));
      }
      if ((jsonObj.get("duration") != null && !jsonObj.get("duration").isJsonNull()) && !jsonObj.get("duration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `duration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("duration").toString()));
      }
      if ((jsonObj.get("number") != null && !jsonObj.get("number").isJsonNull()) && !jsonObj.get("number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number").toString()));
      }
      // validate the optional field `operating`
      if (jsonObj.get("operating") != null && !jsonObj.get("operating").isJsonNull()) {
        OperatingFlight.validateJsonElement(jsonObj.get("operating"));
      }
      if (jsonObj.get("stops") != null && !jsonObj.get("stops").isJsonNull()) {
        JsonArray jsonArraystops = jsonObj.getAsJsonArray("stops");
        if (jsonArraystops != null) {
          // ensure the json data is an array
          if (!jsonObj.get("stops").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `stops` to be an array in the JSON string but got `%s`", jsonObj.get("stops").toString()));
          }

          // validate the optional field `stops` (array)
          for (int i = 0; i < jsonArraystops.size(); i++) {
            FlightStop.validateJsonElement(jsonArraystops.get(i));
          };
        }
      }
      if ((jsonObj.get("suffix") != null && !jsonObj.get("suffix").isJsonNull()) && !jsonObj.get("suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suffix").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FlightSegment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FlightSegment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FlightSegment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FlightSegment.class));

       return (TypeAdapter<T>) new TypeAdapter<FlightSegment>() {
           @Override
           public void write(JsonWriter out, FlightSegment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FlightSegment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FlightSegment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FlightSegment
   * @throws IOException if the JSON string is invalid with respect to FlightSegment
   */
  public static FlightSegment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FlightSegment.class);
  }

  /**
   * Convert an instance of FlightSegment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

