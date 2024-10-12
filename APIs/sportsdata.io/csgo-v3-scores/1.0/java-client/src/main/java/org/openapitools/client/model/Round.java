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
 * Round
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:05.927358-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Round {
  public static final String SERIALIZED_NAME_CURRENT_ROUND = "CurrentRound";
  @SerializedName(SERIALIZED_NAME_CURRENT_ROUND)
  private Boolean currentRound;

  public static final String SERIALIZED_NAME_CURRENT_WEEK = "CurrentWeek";
  @SerializedName(SERIALIZED_NAME_CURRENT_WEEK)
  private Integer currentWeek;

  public static final String SERIALIZED_NAME_END_DATE = "EndDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private String endDate;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ROUND_ID = "RoundId";
  @SerializedName(SERIALIZED_NAME_ROUND_ID)
  private Integer roundId;

  public static final String SERIALIZED_NAME_SEASON = "Season";
  @SerializedName(SERIALIZED_NAME_SEASON)
  private Integer season;

  public static final String SERIALIZED_NAME_SEASON_ID = "SeasonId";
  @SerializedName(SERIALIZED_NAME_SEASON_ID)
  private Integer seasonId;

  public static final String SERIALIZED_NAME_SEASON_TYPE = "SeasonType";
  @SerializedName(SERIALIZED_NAME_SEASON_TYPE)
  private Integer seasonType;

  public static final String SERIALIZED_NAME_START_DATE = "StartDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private String startDate;

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Round() {
  }

  public Round currentRound(Boolean currentRound) {
    this.currentRound = currentRound;
    return this;
  }

  /**
   * Get currentRound
   * @return currentRound
   */
  @javax.annotation.Nullable
  public Boolean getCurrentRound() {
    return currentRound;
  }

  public void setCurrentRound(Boolean currentRound) {
    this.currentRound = currentRound;
  }


  public Round currentWeek(Integer currentWeek) {
    this.currentWeek = currentWeek;
    return this;
  }

  /**
   * Get currentWeek
   * @return currentWeek
   */
  @javax.annotation.Nullable
  public Integer getCurrentWeek() {
    return currentWeek;
  }

  public void setCurrentWeek(Integer currentWeek) {
    this.currentWeek = currentWeek;
  }


  public Round endDate(String endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Get endDate
   * @return endDate
   */
  @javax.annotation.Nullable
  public String getEndDate() {
    return endDate;
  }

  public void setEndDate(String endDate) {
    this.endDate = endDate;
  }


  public Round name(String name) {
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


  public Round roundId(Integer roundId) {
    this.roundId = roundId;
    return this;
  }

  /**
   * Get roundId
   * @return roundId
   */
  @javax.annotation.Nullable
  public Integer getRoundId() {
    return roundId;
  }

  public void setRoundId(Integer roundId) {
    this.roundId = roundId;
  }


  public Round season(Integer season) {
    this.season = season;
    return this;
  }

  /**
   * Get season
   * @return season
   */
  @javax.annotation.Nullable
  public Integer getSeason() {
    return season;
  }

  public void setSeason(Integer season) {
    this.season = season;
  }


  public Round seasonId(Integer seasonId) {
    this.seasonId = seasonId;
    return this;
  }

  /**
   * Get seasonId
   * @return seasonId
   */
  @javax.annotation.Nullable
  public Integer getSeasonId() {
    return seasonId;
  }

  public void setSeasonId(Integer seasonId) {
    this.seasonId = seasonId;
  }


  public Round seasonType(Integer seasonType) {
    this.seasonType = seasonType;
    return this;
  }

  /**
   * Get seasonType
   * @return seasonType
   */
  @javax.annotation.Nullable
  public Integer getSeasonType() {
    return seasonType;
  }

  public void setSeasonType(Integer seasonType) {
    this.seasonType = seasonType;
  }


  public Round startDate(String startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Get startDate
   * @return startDate
   */
  @javax.annotation.Nullable
  public String getStartDate() {
    return startDate;
  }

  public void setStartDate(String startDate) {
    this.startDate = startDate;
  }


  public Round type(String type) {
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
    Round round = (Round) o;
    return Objects.equals(this.currentRound, round.currentRound) &&
        Objects.equals(this.currentWeek, round.currentWeek) &&
        Objects.equals(this.endDate, round.endDate) &&
        Objects.equals(this.name, round.name) &&
        Objects.equals(this.roundId, round.roundId) &&
        Objects.equals(this.season, round.season) &&
        Objects.equals(this.seasonId, round.seasonId) &&
        Objects.equals(this.seasonType, round.seasonType) &&
        Objects.equals(this.startDate, round.startDate) &&
        Objects.equals(this.type, round.type);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(currentRound, currentWeek, endDate, name, roundId, season, seasonId, seasonType, startDate, type);
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
    sb.append("class Round {\n");
    sb.append("    currentRound: ").append(toIndentedString(currentRound)).append("\n");
    sb.append("    currentWeek: ").append(toIndentedString(currentWeek)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    roundId: ").append(toIndentedString(roundId)).append("\n");
    sb.append("    season: ").append(toIndentedString(season)).append("\n");
    sb.append("    seasonId: ").append(toIndentedString(seasonId)).append("\n");
    sb.append("    seasonType: ").append(toIndentedString(seasonType)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
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
    openapiFields.add("CurrentRound");
    openapiFields.add("CurrentWeek");
    openapiFields.add("EndDate");
    openapiFields.add("Name");
    openapiFields.add("RoundId");
    openapiFields.add("Season");
    openapiFields.add("SeasonId");
    openapiFields.add("SeasonType");
    openapiFields.add("StartDate");
    openapiFields.add("Type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Round
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Round.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Round is not found in the empty JSON string", Round.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Round.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Round` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("EndDate") != null && !jsonObj.get("EndDate").isJsonNull()) && !jsonObj.get("EndDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `EndDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("EndDate").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("StartDate") != null && !jsonObj.get("StartDate").isJsonNull()) && !jsonObj.get("StartDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `StartDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("StartDate").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Round.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Round' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Round> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Round.class));

       return (TypeAdapter<T>) new TypeAdapter<Round>() {
           @Override
           public void write(JsonWriter out, Round value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Round read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Round given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Round
   * @throws IOException if the JSON string is invalid with respect to Round
   */
  public static Round fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Round.class);
  }

  /**
   * Convert an instance of Round to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

