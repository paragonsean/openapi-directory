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
 * departure or arrival information
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:18.707859-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FlightEndPoint {
  public static final String SERIALIZED_NAME_IATA_CODE = "iataCode";
  @SerializedName(SERIALIZED_NAME_IATA_CODE)
  private String iataCode;

  public static final String SERIALIZED_NAME_TERMINAL = "terminal";
  @SerializedName(SERIALIZED_NAME_TERMINAL)
  private String terminal;

  public static final String SERIALIZED_NAME_AT = "at";
  @SerializedName(SERIALIZED_NAME_AT)
  private OffsetDateTime at;

  public FlightEndPoint() {
  }

  public FlightEndPoint iataCode(String iataCode) {
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


  public FlightEndPoint terminal(String terminal) {
    this.terminal = terminal;
    return this;
  }

  /**
   * terminal name / number
   * @return terminal
   */
  @javax.annotation.Nullable
  public String getTerminal() {
    return terminal;
  }

  public void setTerminal(String terminal) {
    this.terminal = terminal;
  }


  public FlightEndPoint at(OffsetDateTime at) {
    this.at = at;
    return this;
  }

  /**
   * local date and time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-ddThh:mm:ss format, e.g. 2017-02-10T20:40:00
   * @return at
   */
  @javax.annotation.Nullable
  public OffsetDateTime getAt() {
    return at;
  }

  public void setAt(OffsetDateTime at) {
    this.at = at;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FlightEndPoint flightEndPoint = (FlightEndPoint) o;
    return Objects.equals(this.iataCode, flightEndPoint.iataCode) &&
        Objects.equals(this.terminal, flightEndPoint.terminal) &&
        Objects.equals(this.at, flightEndPoint.at);
  }

  @Override
  public int hashCode() {
    return Objects.hash(iataCode, terminal, at);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FlightEndPoint {\n");
    sb.append("    iataCode: ").append(toIndentedString(iataCode)).append("\n");
    sb.append("    terminal: ").append(toIndentedString(terminal)).append("\n");
    sb.append("    at: ").append(toIndentedString(at)).append("\n");
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
    openapiFields.add("iataCode");
    openapiFields.add("terminal");
    openapiFields.add("at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FlightEndPoint
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FlightEndPoint.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FlightEndPoint is not found in the empty JSON string", FlightEndPoint.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FlightEndPoint.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FlightEndPoint` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("iataCode") != null && !jsonObj.get("iataCode").isJsonNull()) && !jsonObj.get("iataCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `iataCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("iataCode").toString()));
      }
      if ((jsonObj.get("terminal") != null && !jsonObj.get("terminal").isJsonNull()) && !jsonObj.get("terminal").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `terminal` to be a primitive type in the JSON string but got `%s`", jsonObj.get("terminal").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FlightEndPoint.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FlightEndPoint' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FlightEndPoint> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FlightEndPoint.class));

       return (TypeAdapter<T>) new TypeAdapter<FlightEndPoint>() {
           @Override
           public void write(JsonWriter out, FlightEndPoint value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FlightEndPoint read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FlightEndPoint given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FlightEndPoint
   * @throws IOException if the JSON string is invalid with respect to FlightEndPoint
   */
  public static FlightEndPoint fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FlightEndPoint.class);
  }

  /**
   * Convert an instance of FlightEndPoint to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

