/*
 * CS:GO v3 Scores
 * CS:GO v3 Scores
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
 * Venue
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:05.927358-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Venue {
  public static final String SERIALIZED_NAME_ADDRESS = "Address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

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

  public static final String SERIALIZED_NAME_NICKNAME1 = "Nickname1";
  @SerializedName(SERIALIZED_NAME_NICKNAME1)
  private String nickname1;

  public static final String SERIALIZED_NAME_NICKNAME2 = "Nickname2";
  @SerializedName(SERIALIZED_NAME_NICKNAME2)
  private String nickname2;

  public static final String SERIALIZED_NAME_OPEN = "Open";
  @SerializedName(SERIALIZED_NAME_OPEN)
  private Boolean open;

  public static final String SERIALIZED_NAME_OPENED = "Opened";
  @SerializedName(SERIALIZED_NAME_OPENED)
  private Integer opened;

  public static final String SERIALIZED_NAME_VENUE_ID = "VenueId";
  @SerializedName(SERIALIZED_NAME_VENUE_ID)
  private Integer venueId;

  public static final String SERIALIZED_NAME_ZIP = "Zip";
  @SerializedName(SERIALIZED_NAME_ZIP)
  private String zip;

  public Venue() {
  }

  public Venue address(String address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public Venue capacity(Integer capacity) {
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


  public Venue city(String city) {
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


  public Venue country(String country) {
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


  public Venue geoLat(BigDecimal geoLat) {
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


  public Venue geoLong(BigDecimal geoLong) {
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


  public Venue name(String name) {
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


  public Venue nickname1(String nickname1) {
    this.nickname1 = nickname1;
    return this;
  }

  /**
   * Get nickname1
   * @return nickname1
   */
  @javax.annotation.Nullable
  public String getNickname1() {
    return nickname1;
  }

  public void setNickname1(String nickname1) {
    this.nickname1 = nickname1;
  }


  public Venue nickname2(String nickname2) {
    this.nickname2 = nickname2;
    return this;
  }

  /**
   * Get nickname2
   * @return nickname2
   */
  @javax.annotation.Nullable
  public String getNickname2() {
    return nickname2;
  }

  public void setNickname2(String nickname2) {
    this.nickname2 = nickname2;
  }


  public Venue open(Boolean open) {
    this.open = open;
    return this;
  }

  /**
   * Get open
   * @return open
   */
  @javax.annotation.Nullable
  public Boolean getOpen() {
    return open;
  }

  public void setOpen(Boolean open) {
    this.open = open;
  }


  public Venue opened(Integer opened) {
    this.opened = opened;
    return this;
  }

  /**
   * Get opened
   * @return opened
   */
  @javax.annotation.Nullable
  public Integer getOpened() {
    return opened;
  }

  public void setOpened(Integer opened) {
    this.opened = opened;
  }


  public Venue venueId(Integer venueId) {
    this.venueId = venueId;
    return this;
  }

  /**
   * Get venueId
   * @return venueId
   */
  @javax.annotation.Nullable
  public Integer getVenueId() {
    return venueId;
  }

  public void setVenueId(Integer venueId) {
    this.venueId = venueId;
  }


  public Venue zip(String zip) {
    this.zip = zip;
    return this;
  }

  /**
   * Get zip
   * @return zip
   */
  @javax.annotation.Nullable
  public String getZip() {
    return zip;
  }

  public void setZip(String zip) {
    this.zip = zip;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Venue venue = (Venue) o;
    return Objects.equals(this.address, venue.address) &&
        Objects.equals(this.capacity, venue.capacity) &&
        Objects.equals(this.city, venue.city) &&
        Objects.equals(this.country, venue.country) &&
        Objects.equals(this.geoLat, venue.geoLat) &&
        Objects.equals(this.geoLong, venue.geoLong) &&
        Objects.equals(this.name, venue.name) &&
        Objects.equals(this.nickname1, venue.nickname1) &&
        Objects.equals(this.nickname2, venue.nickname2) &&
        Objects.equals(this.open, venue.open) &&
        Objects.equals(this.opened, venue.opened) &&
        Objects.equals(this.venueId, venue.venueId) &&
        Objects.equals(this.zip, venue.zip);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, capacity, city, country, geoLat, geoLong, name, nickname1, nickname2, open, opened, venueId, zip);
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
    sb.append("class Venue {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    capacity: ").append(toIndentedString(capacity)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    geoLat: ").append(toIndentedString(geoLat)).append("\n");
    sb.append("    geoLong: ").append(toIndentedString(geoLong)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nickname1: ").append(toIndentedString(nickname1)).append("\n");
    sb.append("    nickname2: ").append(toIndentedString(nickname2)).append("\n");
    sb.append("    open: ").append(toIndentedString(open)).append("\n");
    sb.append("    opened: ").append(toIndentedString(opened)).append("\n");
    sb.append("    venueId: ").append(toIndentedString(venueId)).append("\n");
    sb.append("    zip: ").append(toIndentedString(zip)).append("\n");
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
    openapiFields.add("Address");
    openapiFields.add("Capacity");
    openapiFields.add("City");
    openapiFields.add("Country");
    openapiFields.add("GeoLat");
    openapiFields.add("GeoLong");
    openapiFields.add("Name");
    openapiFields.add("Nickname1");
    openapiFields.add("Nickname2");
    openapiFields.add("Open");
    openapiFields.add("Opened");
    openapiFields.add("VenueId");
    openapiFields.add("Zip");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Venue
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Venue.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Venue is not found in the empty JSON string", Venue.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Venue.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Venue` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Address") != null && !jsonObj.get("Address").isJsonNull()) && !jsonObj.get("Address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Address").toString()));
      }
      if ((jsonObj.get("City") != null && !jsonObj.get("City").isJsonNull()) && !jsonObj.get("City").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `City` to be a primitive type in the JSON string but got `%s`", jsonObj.get("City").toString()));
      }
      if ((jsonObj.get("Country") != null && !jsonObj.get("Country").isJsonNull()) && !jsonObj.get("Country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Country").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Nickname1") != null && !jsonObj.get("Nickname1").isJsonNull()) && !jsonObj.get("Nickname1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Nickname1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Nickname1").toString()));
      }
      if ((jsonObj.get("Nickname2") != null && !jsonObj.get("Nickname2").isJsonNull()) && !jsonObj.get("Nickname2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Nickname2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Nickname2").toString()));
      }
      if ((jsonObj.get("Zip") != null && !jsonObj.get("Zip").isJsonNull()) && !jsonObj.get("Zip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Zip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Zip").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Venue.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Venue' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Venue> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Venue.class));

       return (TypeAdapter<T>) new TypeAdapter<Venue>() {
           @Override
           public void write(JsonWriter out, Venue value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Venue read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Venue given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Venue
   * @throws IOException if the JSON string is invalid with respect to Venue
   */
  public static Venue fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Venue.class);
  }

  /**
   * Convert an instance of Venue to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

