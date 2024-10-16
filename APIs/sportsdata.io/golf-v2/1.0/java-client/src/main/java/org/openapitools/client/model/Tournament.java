/*
 * Golf v2
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Round;
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
 * Tournament
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:32.114934-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Tournament {
  public static final String SERIALIZED_NAME_CANCELED = "Canceled";
  @SerializedName(SERIALIZED_NAME_CANCELED)
  private Boolean canceled;

  public static final String SERIALIZED_NAME_CITY = "City";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COUNTRY = "Country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_COVERED = "Covered";
  @SerializedName(SERIALIZED_NAME_COVERED)
  private Boolean covered;

  public static final String SERIALIZED_NAME_END_DATE = "EndDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private String endDate;

  public static final String SERIALIZED_NAME_FORMAT = "Format";
  @SerializedName(SERIALIZED_NAME_FORMAT)
  private String format;

  public static final String SERIALIZED_NAME_IS_IN_PROGRESS = "IsInProgress";
  @SerializedName(SERIALIZED_NAME_IS_IN_PROGRESS)
  private Boolean isInProgress;

  public static final String SERIALIZED_NAME_IS_OVER = "IsOver";
  @SerializedName(SERIALIZED_NAME_IS_OVER)
  private Boolean isOver;

  public static final String SERIALIZED_NAME_LOCATION = "Location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private String location;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ODDS_COVERAGE = "OddsCoverage";
  @SerializedName(SERIALIZED_NAME_ODDS_COVERAGE)
  private String oddsCoverage;

  public static final String SERIALIZED_NAME_PAR = "Par";
  @SerializedName(SERIALIZED_NAME_PAR)
  private Integer par;

  public static final String SERIALIZED_NAME_PURSE = "Purse";
  @SerializedName(SERIALIZED_NAME_PURSE)
  private BigDecimal purse;

  public static final String SERIALIZED_NAME_ROUNDS = "Rounds";
  @SerializedName(SERIALIZED_NAME_ROUNDS)
  private List<Round> rounds = new ArrayList<>();

  public static final String SERIALIZED_NAME_SPORT_RADAR_TOURNAMENT_I_D = "SportRadarTournamentID";
  @SerializedName(SERIALIZED_NAME_SPORT_RADAR_TOURNAMENT_I_D)
  private String sportRadarTournamentID;

  public static final String SERIALIZED_NAME_START_DATE = "StartDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private String startDate;

  public static final String SERIALIZED_NAME_START_DATE_TIME = "StartDateTime";
  @SerializedName(SERIALIZED_NAME_START_DATE_TIME)
  private String startDateTime;

  public static final String SERIALIZED_NAME_STATE = "State";
  @SerializedName(SERIALIZED_NAME_STATE)
  private String state;

  public static final String SERIALIZED_NAME_TIME_ZONE = "TimeZone";
  @SerializedName(SERIALIZED_NAME_TIME_ZONE)
  private String timeZone;

  public static final String SERIALIZED_NAME_TOURNAMENT_I_D = "TournamentID";
  @SerializedName(SERIALIZED_NAME_TOURNAMENT_I_D)
  private Integer tournamentID;

  public static final String SERIALIZED_NAME_VENUE = "Venue";
  @SerializedName(SERIALIZED_NAME_VENUE)
  private String venue;

  public static final String SERIALIZED_NAME_YARDS = "Yards";
  @SerializedName(SERIALIZED_NAME_YARDS)
  private Integer yards;

  public static final String SERIALIZED_NAME_ZIP_CODE = "ZipCode";
  @SerializedName(SERIALIZED_NAME_ZIP_CODE)
  private String zipCode;

  public Tournament() {
  }

  public Tournament canceled(Boolean canceled) {
    this.canceled = canceled;
    return this;
  }

  /**
   * Get canceled
   * @return canceled
   */
  @javax.annotation.Nullable
  public Boolean getCanceled() {
    return canceled;
  }

  public void setCanceled(Boolean canceled) {
    this.canceled = canceled;
  }


  public Tournament city(String city) {
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


  public Tournament country(String country) {
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


  public Tournament covered(Boolean covered) {
    this.covered = covered;
    return this;
  }

  /**
   * Get covered
   * @return covered
   */
  @javax.annotation.Nullable
  public Boolean getCovered() {
    return covered;
  }

  public void setCovered(Boolean covered) {
    this.covered = covered;
  }


  public Tournament endDate(String endDate) {
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


  public Tournament format(String format) {
    this.format = format;
    return this;
  }

  /**
   * Get format
   * @return format
   */
  @javax.annotation.Nullable
  public String getFormat() {
    return format;
  }

  public void setFormat(String format) {
    this.format = format;
  }


  public Tournament isInProgress(Boolean isInProgress) {
    this.isInProgress = isInProgress;
    return this;
  }

  /**
   * Get isInProgress
   * @return isInProgress
   */
  @javax.annotation.Nullable
  public Boolean getIsInProgress() {
    return isInProgress;
  }

  public void setIsInProgress(Boolean isInProgress) {
    this.isInProgress = isInProgress;
  }


  public Tournament isOver(Boolean isOver) {
    this.isOver = isOver;
    return this;
  }

  /**
   * Get isOver
   * @return isOver
   */
  @javax.annotation.Nullable
  public Boolean getIsOver() {
    return isOver;
  }

  public void setIsOver(Boolean isOver) {
    this.isOver = isOver;
  }


  public Tournament location(String location) {
    this.location = location;
    return this;
  }

  /**
   * Get location
   * @return location
   */
  @javax.annotation.Nullable
  public String getLocation() {
    return location;
  }

  public void setLocation(String location) {
    this.location = location;
  }


  public Tournament name(String name) {
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


  public Tournament oddsCoverage(String oddsCoverage) {
    this.oddsCoverage = oddsCoverage;
    return this;
  }

  /**
   * Get oddsCoverage
   * @return oddsCoverage
   */
  @javax.annotation.Nullable
  public String getOddsCoverage() {
    return oddsCoverage;
  }

  public void setOddsCoverage(String oddsCoverage) {
    this.oddsCoverage = oddsCoverage;
  }


  public Tournament par(Integer par) {
    this.par = par;
    return this;
  }

  /**
   * Get par
   * @return par
   */
  @javax.annotation.Nullable
  public Integer getPar() {
    return par;
  }

  public void setPar(Integer par) {
    this.par = par;
  }


  public Tournament purse(BigDecimal purse) {
    this.purse = purse;
    return this;
  }

  /**
   * Get purse
   * @return purse
   */
  @javax.annotation.Nullable
  public BigDecimal getPurse() {
    return purse;
  }

  public void setPurse(BigDecimal purse) {
    this.purse = purse;
  }


  public Tournament rounds(List<Round> rounds) {
    this.rounds = rounds;
    return this;
  }

  public Tournament addRoundsItem(Round roundsItem) {
    if (this.rounds == null) {
      this.rounds = new ArrayList<>();
    }
    this.rounds.add(roundsItem);
    return this;
  }

  /**
   * Get rounds
   * @return rounds
   */
  @javax.annotation.Nullable
  public List<Round> getRounds() {
    return rounds;
  }

  public void setRounds(List<Round> rounds) {
    this.rounds = rounds;
  }


  public Tournament sportRadarTournamentID(String sportRadarTournamentID) {
    this.sportRadarTournamentID = sportRadarTournamentID;
    return this;
  }

  /**
   * Get sportRadarTournamentID
   * @return sportRadarTournamentID
   */
  @javax.annotation.Nullable
  public String getSportRadarTournamentID() {
    return sportRadarTournamentID;
  }

  public void setSportRadarTournamentID(String sportRadarTournamentID) {
    this.sportRadarTournamentID = sportRadarTournamentID;
  }


  public Tournament startDate(String startDate) {
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


  public Tournament startDateTime(String startDateTime) {
    this.startDateTime = startDateTime;
    return this;
  }

  /**
   * Get startDateTime
   * @return startDateTime
   */
  @javax.annotation.Nullable
  public String getStartDateTime() {
    return startDateTime;
  }

  public void setStartDateTime(String startDateTime) {
    this.startDateTime = startDateTime;
  }


  public Tournament state(String state) {
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


  public Tournament timeZone(String timeZone) {
    this.timeZone = timeZone;
    return this;
  }

  /**
   * Get timeZone
   * @return timeZone
   */
  @javax.annotation.Nullable
  public String getTimeZone() {
    return timeZone;
  }

  public void setTimeZone(String timeZone) {
    this.timeZone = timeZone;
  }


  public Tournament tournamentID(Integer tournamentID) {
    this.tournamentID = tournamentID;
    return this;
  }

  /**
   * Get tournamentID
   * @return tournamentID
   */
  @javax.annotation.Nullable
  public Integer getTournamentID() {
    return tournamentID;
  }

  public void setTournamentID(Integer tournamentID) {
    this.tournamentID = tournamentID;
  }


  public Tournament venue(String venue) {
    this.venue = venue;
    return this;
  }

  /**
   * Get venue
   * @return venue
   */
  @javax.annotation.Nullable
  public String getVenue() {
    return venue;
  }

  public void setVenue(String venue) {
    this.venue = venue;
  }


  public Tournament yards(Integer yards) {
    this.yards = yards;
    return this;
  }

  /**
   * Get yards
   * @return yards
   */
  @javax.annotation.Nullable
  public Integer getYards() {
    return yards;
  }

  public void setYards(Integer yards) {
    this.yards = yards;
  }


  public Tournament zipCode(String zipCode) {
    this.zipCode = zipCode;
    return this;
  }

  /**
   * Get zipCode
   * @return zipCode
   */
  @javax.annotation.Nullable
  public String getZipCode() {
    return zipCode;
  }

  public void setZipCode(String zipCode) {
    this.zipCode = zipCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Tournament tournament = (Tournament) o;
    return Objects.equals(this.canceled, tournament.canceled) &&
        Objects.equals(this.city, tournament.city) &&
        Objects.equals(this.country, tournament.country) &&
        Objects.equals(this.covered, tournament.covered) &&
        Objects.equals(this.endDate, tournament.endDate) &&
        Objects.equals(this.format, tournament.format) &&
        Objects.equals(this.isInProgress, tournament.isInProgress) &&
        Objects.equals(this.isOver, tournament.isOver) &&
        Objects.equals(this.location, tournament.location) &&
        Objects.equals(this.name, tournament.name) &&
        Objects.equals(this.oddsCoverage, tournament.oddsCoverage) &&
        Objects.equals(this.par, tournament.par) &&
        Objects.equals(this.purse, tournament.purse) &&
        Objects.equals(this.rounds, tournament.rounds) &&
        Objects.equals(this.sportRadarTournamentID, tournament.sportRadarTournamentID) &&
        Objects.equals(this.startDate, tournament.startDate) &&
        Objects.equals(this.startDateTime, tournament.startDateTime) &&
        Objects.equals(this.state, tournament.state) &&
        Objects.equals(this.timeZone, tournament.timeZone) &&
        Objects.equals(this.tournamentID, tournament.tournamentID) &&
        Objects.equals(this.venue, tournament.venue) &&
        Objects.equals(this.yards, tournament.yards) &&
        Objects.equals(this.zipCode, tournament.zipCode);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(canceled, city, country, covered, endDate, format, isInProgress, isOver, location, name, oddsCoverage, par, purse, rounds, sportRadarTournamentID, startDate, startDateTime, state, timeZone, tournamentID, venue, yards, zipCode);
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
    sb.append("class Tournament {\n");
    sb.append("    canceled: ").append(toIndentedString(canceled)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    covered: ").append(toIndentedString(covered)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    format: ").append(toIndentedString(format)).append("\n");
    sb.append("    isInProgress: ").append(toIndentedString(isInProgress)).append("\n");
    sb.append("    isOver: ").append(toIndentedString(isOver)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    oddsCoverage: ").append(toIndentedString(oddsCoverage)).append("\n");
    sb.append("    par: ").append(toIndentedString(par)).append("\n");
    sb.append("    purse: ").append(toIndentedString(purse)).append("\n");
    sb.append("    rounds: ").append(toIndentedString(rounds)).append("\n");
    sb.append("    sportRadarTournamentID: ").append(toIndentedString(sportRadarTournamentID)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
    sb.append("    startDateTime: ").append(toIndentedString(startDateTime)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    timeZone: ").append(toIndentedString(timeZone)).append("\n");
    sb.append("    tournamentID: ").append(toIndentedString(tournamentID)).append("\n");
    sb.append("    venue: ").append(toIndentedString(venue)).append("\n");
    sb.append("    yards: ").append(toIndentedString(yards)).append("\n");
    sb.append("    zipCode: ").append(toIndentedString(zipCode)).append("\n");
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
    openapiFields.add("Canceled");
    openapiFields.add("City");
    openapiFields.add("Country");
    openapiFields.add("Covered");
    openapiFields.add("EndDate");
    openapiFields.add("Format");
    openapiFields.add("IsInProgress");
    openapiFields.add("IsOver");
    openapiFields.add("Location");
    openapiFields.add("Name");
    openapiFields.add("OddsCoverage");
    openapiFields.add("Par");
    openapiFields.add("Purse");
    openapiFields.add("Rounds");
    openapiFields.add("SportRadarTournamentID");
    openapiFields.add("StartDate");
    openapiFields.add("StartDateTime");
    openapiFields.add("State");
    openapiFields.add("TimeZone");
    openapiFields.add("TournamentID");
    openapiFields.add("Venue");
    openapiFields.add("Yards");
    openapiFields.add("ZipCode");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Tournament
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Tournament.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Tournament is not found in the empty JSON string", Tournament.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Tournament.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Tournament` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("City") != null && !jsonObj.get("City").isJsonNull()) && !jsonObj.get("City").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `City` to be a primitive type in the JSON string but got `%s`", jsonObj.get("City").toString()));
      }
      if ((jsonObj.get("Country") != null && !jsonObj.get("Country").isJsonNull()) && !jsonObj.get("Country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Country").toString()));
      }
      if ((jsonObj.get("EndDate") != null && !jsonObj.get("EndDate").isJsonNull()) && !jsonObj.get("EndDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `EndDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("EndDate").toString()));
      }
      if ((jsonObj.get("Format") != null && !jsonObj.get("Format").isJsonNull()) && !jsonObj.get("Format").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Format` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Format").toString()));
      }
      if ((jsonObj.get("Location") != null && !jsonObj.get("Location").isJsonNull()) && !jsonObj.get("Location").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Location` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Location").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("OddsCoverage") != null && !jsonObj.get("OddsCoverage").isJsonNull()) && !jsonObj.get("OddsCoverage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OddsCoverage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OddsCoverage").toString()));
      }
      if (jsonObj.get("Rounds") != null && !jsonObj.get("Rounds").isJsonNull()) {
        JsonArray jsonArrayrounds = jsonObj.getAsJsonArray("Rounds");
        if (jsonArrayrounds != null) {
          // ensure the json data is an array
          if (!jsonObj.get("Rounds").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `Rounds` to be an array in the JSON string but got `%s`", jsonObj.get("Rounds").toString()));
          }

          // validate the optional field `Rounds` (array)
          for (int i = 0; i < jsonArrayrounds.size(); i++) {
            Round.validateJsonElement(jsonArrayrounds.get(i));
          };
        }
      }
      if ((jsonObj.get("SportRadarTournamentID") != null && !jsonObj.get("SportRadarTournamentID").isJsonNull()) && !jsonObj.get("SportRadarTournamentID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SportRadarTournamentID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SportRadarTournamentID").toString()));
      }
      if ((jsonObj.get("StartDate") != null && !jsonObj.get("StartDate").isJsonNull()) && !jsonObj.get("StartDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `StartDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("StartDate").toString()));
      }
      if ((jsonObj.get("StartDateTime") != null && !jsonObj.get("StartDateTime").isJsonNull()) && !jsonObj.get("StartDateTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `StartDateTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("StartDateTime").toString()));
      }
      if ((jsonObj.get("State") != null && !jsonObj.get("State").isJsonNull()) && !jsonObj.get("State").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `State` to be a primitive type in the JSON string but got `%s`", jsonObj.get("State").toString()));
      }
      if ((jsonObj.get("TimeZone") != null && !jsonObj.get("TimeZone").isJsonNull()) && !jsonObj.get("TimeZone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TimeZone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TimeZone").toString()));
      }
      if ((jsonObj.get("Venue") != null && !jsonObj.get("Venue").isJsonNull()) && !jsonObj.get("Venue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Venue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Venue").toString()));
      }
      if ((jsonObj.get("ZipCode") != null && !jsonObj.get("ZipCode").isJsonNull()) && !jsonObj.get("ZipCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ZipCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ZipCode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Tournament.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Tournament' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Tournament> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Tournament.class));

       return (TypeAdapter<T>) new TypeAdapter<Tournament>() {
           @Override
           public void write(JsonWriter out, Tournament value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Tournament read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Tournament given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Tournament
   * @throws IOException if the JSON string is invalid with respect to Tournament
   */
  public static Tournament fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Tournament.class);
  }

  /**
   * Convert an instance of Tournament to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

