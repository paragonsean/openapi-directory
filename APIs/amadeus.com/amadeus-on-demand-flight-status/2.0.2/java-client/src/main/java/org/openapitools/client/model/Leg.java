/*
 * On-Demand Flight Status
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
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
import java.util.Arrays;
import org.openapitools.client.model.AircraftEquipment;

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
 * Leg
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:22.700449-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Leg {
  public static final String SERIALIZED_NAME_AIRCRAFT_EQUIPMENT = "aircraftEquipment";
  @SerializedName(SERIALIZED_NAME_AIRCRAFT_EQUIPMENT)
  private AircraftEquipment aircraftEquipment;

  public static final String SERIALIZED_NAME_BOARD_POINT_IATA_CODE = "boardPointIataCode";
  @SerializedName(SERIALIZED_NAME_BOARD_POINT_IATA_CODE)
  private String boardPointIataCode;

  public static final String SERIALIZED_NAME_OFF_POINT_IATA_CODE = "offPointIataCode";
  @SerializedName(SERIALIZED_NAME_OFF_POINT_IATA_CODE)
  private String offPointIataCode;

  public static final String SERIALIZED_NAME_SCHEDULED_LEG_DURATION = "scheduledLegDuration";
  @SerializedName(SERIALIZED_NAME_SCHEDULED_LEG_DURATION)
  private String scheduledLegDuration;

  public Leg() {
  }

  public Leg aircraftEquipment(AircraftEquipment aircraftEquipment) {
    this.aircraftEquipment = aircraftEquipment;
    return this;
  }

  /**
   * Get aircraftEquipment
   * @return aircraftEquipment
   */
  @javax.annotation.Nullable
  public AircraftEquipment getAircraftEquipment() {
    return aircraftEquipment;
  }

  public void setAircraftEquipment(AircraftEquipment aircraftEquipment) {
    this.aircraftEquipment = aircraftEquipment;
  }


  public Leg boardPointIataCode(String boardPointIataCode) {
    this.boardPointIataCode = boardPointIataCode;
    return this;
  }

  /**
   * 3-letter IATA code of the departure airport. e.g. LHR
   * @return boardPointIataCode
   */
  @javax.annotation.Nullable
  public String getBoardPointIataCode() {
    return boardPointIataCode;
  }

  public void setBoardPointIataCode(String boardPointIataCode) {
    this.boardPointIataCode = boardPointIataCode;
  }


  public Leg offPointIataCode(String offPointIataCode) {
    this.offPointIataCode = offPointIataCode;
    return this;
  }

  /**
   * 3-letter IATA code of the arrival airport. e.g. BKK
   * @return offPointIataCode
   */
  @javax.annotation.Nullable
  public String getOffPointIataCode() {
    return offPointIataCode;
  }

  public void setOffPointIataCode(String offPointIataCode) {
    this.offPointIataCode = offPointIataCode;
  }


  public Leg scheduledLegDuration(String scheduledLegDuration) {
    this.scheduledLegDuration = scheduledLegDuration;
    return this;
  }

  /**
   * duration of the leg following standard [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations)
   * @return scheduledLegDuration
   */
  @javax.annotation.Nullable
  public String getScheduledLegDuration() {
    return scheduledLegDuration;
  }

  public void setScheduledLegDuration(String scheduledLegDuration) {
    this.scheduledLegDuration = scheduledLegDuration;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Leg leg = (Leg) o;
    return Objects.equals(this.aircraftEquipment, leg.aircraftEquipment) &&
        Objects.equals(this.boardPointIataCode, leg.boardPointIataCode) &&
        Objects.equals(this.offPointIataCode, leg.offPointIataCode) &&
        Objects.equals(this.scheduledLegDuration, leg.scheduledLegDuration);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aircraftEquipment, boardPointIataCode, offPointIataCode, scheduledLegDuration);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Leg {\n");
    sb.append("    aircraftEquipment: ").append(toIndentedString(aircraftEquipment)).append("\n");
    sb.append("    boardPointIataCode: ").append(toIndentedString(boardPointIataCode)).append("\n");
    sb.append("    offPointIataCode: ").append(toIndentedString(offPointIataCode)).append("\n");
    sb.append("    scheduledLegDuration: ").append(toIndentedString(scheduledLegDuration)).append("\n");
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
    openapiFields.add("aircraftEquipment");
    openapiFields.add("boardPointIataCode");
    openapiFields.add("offPointIataCode");
    openapiFields.add("scheduledLegDuration");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Leg
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Leg.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Leg is not found in the empty JSON string", Leg.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Leg.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Leg` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `aircraftEquipment`
      if (jsonObj.get("aircraftEquipment") != null && !jsonObj.get("aircraftEquipment").isJsonNull()) {
        AircraftEquipment.validateJsonElement(jsonObj.get("aircraftEquipment"));
      }
      if ((jsonObj.get("boardPointIataCode") != null && !jsonObj.get("boardPointIataCode").isJsonNull()) && !jsonObj.get("boardPointIataCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `boardPointIataCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("boardPointIataCode").toString()));
      }
      if ((jsonObj.get("offPointIataCode") != null && !jsonObj.get("offPointIataCode").isJsonNull()) && !jsonObj.get("offPointIataCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `offPointIataCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("offPointIataCode").toString()));
      }
      if ((jsonObj.get("scheduledLegDuration") != null && !jsonObj.get("scheduledLegDuration").isJsonNull()) && !jsonObj.get("scheduledLegDuration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scheduledLegDuration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scheduledLegDuration").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Leg.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Leg' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Leg> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Leg.class));

       return (TypeAdapter<T>) new TypeAdapter<Leg>() {
           @Override
           public void write(JsonWriter out, Leg value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Leg read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Leg given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Leg
   * @throws IOException if the JSON string is invalid with respect to Leg
   */
  public static Leg fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Leg.class);
  }

  /**
   * Convert an instance of Leg to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

