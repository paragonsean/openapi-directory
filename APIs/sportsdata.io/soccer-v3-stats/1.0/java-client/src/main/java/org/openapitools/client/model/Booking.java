/*
 * Soccer v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
 * Booking
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:19.276097-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Booking {
  public static final String SERIALIZED_NAME_BOOKING_ID = "BookingId";
  @SerializedName(SERIALIZED_NAME_BOOKING_ID)
  private Integer bookingId;

  public static final String SERIALIZED_NAME_GAME_ID = "GameId";
  @SerializedName(SERIALIZED_NAME_GAME_ID)
  private Integer gameId;

  public static final String SERIALIZED_NAME_GAME_MINUTE = "GameMinute";
  @SerializedName(SERIALIZED_NAME_GAME_MINUTE)
  private Integer gameMinute;

  public static final String SERIALIZED_NAME_GAME_MINUTE_EXTRA = "GameMinuteExtra";
  @SerializedName(SERIALIZED_NAME_GAME_MINUTE_EXTRA)
  private Integer gameMinuteExtra;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PLAYER_ID = "PlayerId";
  @SerializedName(SERIALIZED_NAME_PLAYER_ID)
  private Integer playerId;

  public static final String SERIALIZED_NAME_TEAM_ID = "TeamId";
  @SerializedName(SERIALIZED_NAME_TEAM_ID)
  private Integer teamId;

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Booking() {
  }

  public Booking bookingId(Integer bookingId) {
    this.bookingId = bookingId;
    return this;
  }

  /**
   * Get bookingId
   * @return bookingId
   */
  @javax.annotation.Nullable
  public Integer getBookingId() {
    return bookingId;
  }

  public void setBookingId(Integer bookingId) {
    this.bookingId = bookingId;
  }


  public Booking gameId(Integer gameId) {
    this.gameId = gameId;
    return this;
  }

  /**
   * Get gameId
   * @return gameId
   */
  @javax.annotation.Nullable
  public Integer getGameId() {
    return gameId;
  }

  public void setGameId(Integer gameId) {
    this.gameId = gameId;
  }


  public Booking gameMinute(Integer gameMinute) {
    this.gameMinute = gameMinute;
    return this;
  }

  /**
   * Get gameMinute
   * @return gameMinute
   */
  @javax.annotation.Nullable
  public Integer getGameMinute() {
    return gameMinute;
  }

  public void setGameMinute(Integer gameMinute) {
    this.gameMinute = gameMinute;
  }


  public Booking gameMinuteExtra(Integer gameMinuteExtra) {
    this.gameMinuteExtra = gameMinuteExtra;
    return this;
  }

  /**
   * Get gameMinuteExtra
   * @return gameMinuteExtra
   */
  @javax.annotation.Nullable
  public Integer getGameMinuteExtra() {
    return gameMinuteExtra;
  }

  public void setGameMinuteExtra(Integer gameMinuteExtra) {
    this.gameMinuteExtra = gameMinuteExtra;
  }


  public Booking name(String name) {
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


  public Booking playerId(Integer playerId) {
    this.playerId = playerId;
    return this;
  }

  /**
   * Get playerId
   * @return playerId
   */
  @javax.annotation.Nullable
  public Integer getPlayerId() {
    return playerId;
  }

  public void setPlayerId(Integer playerId) {
    this.playerId = playerId;
  }


  public Booking teamId(Integer teamId) {
    this.teamId = teamId;
    return this;
  }

  /**
   * Get teamId
   * @return teamId
   */
  @javax.annotation.Nullable
  public Integer getTeamId() {
    return teamId;
  }

  public void setTeamId(Integer teamId) {
    this.teamId = teamId;
  }


  public Booking type(String type) {
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
    Booking booking = (Booking) o;
    return Objects.equals(this.bookingId, booking.bookingId) &&
        Objects.equals(this.gameId, booking.gameId) &&
        Objects.equals(this.gameMinute, booking.gameMinute) &&
        Objects.equals(this.gameMinuteExtra, booking.gameMinuteExtra) &&
        Objects.equals(this.name, booking.name) &&
        Objects.equals(this.playerId, booking.playerId) &&
        Objects.equals(this.teamId, booking.teamId) &&
        Objects.equals(this.type, booking.type);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(bookingId, gameId, gameMinute, gameMinuteExtra, name, playerId, teamId, type);
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
    sb.append("class Booking {\n");
    sb.append("    bookingId: ").append(toIndentedString(bookingId)).append("\n");
    sb.append("    gameId: ").append(toIndentedString(gameId)).append("\n");
    sb.append("    gameMinute: ").append(toIndentedString(gameMinute)).append("\n");
    sb.append("    gameMinuteExtra: ").append(toIndentedString(gameMinuteExtra)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    playerId: ").append(toIndentedString(playerId)).append("\n");
    sb.append("    teamId: ").append(toIndentedString(teamId)).append("\n");
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
    openapiFields.add("BookingId");
    openapiFields.add("GameId");
    openapiFields.add("GameMinute");
    openapiFields.add("GameMinuteExtra");
    openapiFields.add("Name");
    openapiFields.add("PlayerId");
    openapiFields.add("TeamId");
    openapiFields.add("Type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Booking
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Booking.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Booking is not found in the empty JSON string", Booking.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Booking.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Booking` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Booking.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Booking' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Booking> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Booking.class));

       return (TypeAdapter<T>) new TypeAdapter<Booking>() {
           @Override
           public void write(JsonWriter out, Booking value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Booking read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Booking given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Booking
   * @throws IOException if the JSON string is invalid with respect to Booking
   */
  public static Booking fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Booking.class);
  }

  /**
   * Convert an instance of Booking to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

