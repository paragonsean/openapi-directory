/*
 * NFL v3 Projections
 * NFL projected stats API.
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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * Stadium
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:29.432938-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Stadium {
  public static final String SERIALIZED_NAME_CAPACITY = "Capacity";
  @SerializedName(SERIALIZED_NAME_CAPACITY)
  private Integer capacity;

  public static final String SERIALIZED_NAME_CITY = "City";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COUNTRY = "Country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_GEO_LAT = "GeoLat";
  @SerializedName(SERIALIZED_NAME_GEO_LAT)
  private BigDecimal geoLat;

  public static final String SERIALIZED_NAME_GEO_LONG = "GeoLong";
  @SerializedName(SERIALIZED_NAME_GEO_LONG)
  private BigDecimal geoLong;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PLAYING_SURFACE = "PlayingSurface";
  @SerializedName(SERIALIZED_NAME_PLAYING_SURFACE)
  private String playingSurface;

  public static final String SERIALIZED_NAME_STADIUM_I_D = "StadiumID";
  @SerializedName(SERIALIZED_NAME_STADIUM_I_D)
  private Integer stadiumID;

  public static final String SERIALIZED_NAME_STATE = "State";
  @SerializedName(SERIALIZED_NAME_STATE)
  private String state;

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Stadium() {
  }

  public Stadium capacity(Integer capacity) {
    this.capacity = capacity;
    return this;
  }

  /**
   * Get capacity
   * @return capacity
   */
  @javax.annotation.Nullable
  public Integer getCapacity() {
    return capacity;
  }

  public void setCapacity(Integer capacity) {
    this.capacity = capacity;
  }


  public Stadium city(String city) {
    this.city = city;
    return this;
  }

  /**
   * Get city
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public Stadium country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Get country
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public Stadium geoLat(BigDecimal geoLat) {
    this.geoLat = geoLat;
    return this;
  }

  /**
   * Get geoLat
   * @return geoLat
   */
  @javax.annotation.Nullable
  public BigDecimal getGeoLat() {
    return geoLat;
  }

  public void setGeoLat(BigDecimal geoLat) {
    this.geoLat = geoLat;
  }


  public Stadium geoLong(BigDecimal geoLong) {
    this.geoLong = geoLong;
    return this;
  }

  /**
   * Get geoLong
   * @return geoLong
   */
  @javax.annotation.Nullable
  public BigDecimal getGeoLong() {
    return geoLong;
  }

  public void setGeoLong(BigDecimal geoLong) {
    this.geoLong = geoLong;
  }


  public Stadium name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Stadium playingSurface(String playingSurface) {
    this.playingSurface = playingSurface;
    return this;
  }

  /**
   * Get playingSurface
   * @return playingSurface
   */
  @javax.annotation.Nullable
  public String getPlayingSurface() {
    return playingSurface;
  }

  public void setPlayingSurface(String playingSurface) {
    this.playingSurface = playingSurface;
  }


  public Stadium stadiumID(Integer stadiumID) {
    this.stadiumID = stadiumID;
    return this;
  }

  /**
   * Get stadiumID
   * @return stadiumID
   */
  @javax.annotation.Nullable
  public Integer getStadiumID() {
    return stadiumID;
  }

  public void setStadiumID(Integer stadiumID) {
    this.stadiumID = stadiumID;
  }


  public Stadium state(String state) {
    this.state = state;
    return this;
  }

  /**
   * Get state
   * @return state
   */
  @javax.annotation.Nullable
  public String getState() {
    return state;
  }

  public void setState(String state) {
    this.state = state;
  }


  public Stadium type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Stadium stadium = (Stadium) o;
    return Objects.equals(this.capacity, stadium.capacity) &&
        Objects.equals(this.city, stadium.city) &&
        Objects.equals(this.country, stadium.country) &&
        Objects.equals(this.geoLat, stadium.geoLat) &&
        Objects.equals(this.geoLong, stadium.geoLong) &&
        Objects.equals(this.name, stadium.name) &&
        Objects.equals(this.playingSurface, stadium.playingSurface) &&
        Objects.equals(this.stadiumID, stadium.stadiumID) &&
        Objects.equals(this.state, stadium.state) &&
        Objects.equals(this.type, stadium.type);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(capacity, city, country, geoLat, geoLong, name, playingSurface, stadiumID, state, type);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Stadium {\n");
    sb.append("    capacity: ").append(toIndentedString(capacity)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    geoLat: ").append(toIndentedString(geoLat)).append("\n");
    sb.append("    geoLong: ").append(toIndentedString(geoLong)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    playingSurface: ").append(toIndentedString(playingSurface)).append("\n");
    sb.append("    stadiumID: ").append(toIndentedString(stadiumID)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("Capacity");
    openapiFields.add("City");
    openapiFields.add("Country");
    openapiFields.add("GeoLat");
    openapiFields.add("GeoLong");
    openapiFields.add("Name");
    openapiFields.add("PlayingSurface");
    openapiFields.add("StadiumID");
    openapiFields.add("State");
    openapiFields.add("Type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Stadium
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Stadium.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Stadium is not found in the empty JSON string", Stadium.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Stadium.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Stadium` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("City") != null && !jsonObj.get("City").isJsonNull()) && !jsonObj.get("City").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `City` to be a primitive type in the JSON string but got `%s`", jsonObj.get("City").toString()));
      }
      if ((jsonObj.get("Country") != null && !jsonObj.get("Country").isJsonNull()) && !jsonObj.get("Country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Country").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("PlayingSurface") != null && !jsonObj.get("PlayingSurface").isJsonNull()) && !jsonObj.get("PlayingSurface").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PlayingSurface` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PlayingSurface").toString()));
      }
      if ((jsonObj.get("State") != null && !jsonObj.get("State").isJsonNull()) && !jsonObj.get("State").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `State` to be a primitive type in the JSON string but got `%s`", jsonObj.get("State").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Stadium.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Stadium' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Stadium> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Stadium.class));

       return (TypeAdapter<T>) new TypeAdapter<Stadium>() {
           @Override
           public void write(JsonWriter out, Stadium value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Stadium read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Stadium given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Stadium
   * @throws IOException if the JSON string is invalid with respect to Stadium
   */
  public static Stadium fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Stadium.class);
  }

  /**
   * Convert an instance of Stadium to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

