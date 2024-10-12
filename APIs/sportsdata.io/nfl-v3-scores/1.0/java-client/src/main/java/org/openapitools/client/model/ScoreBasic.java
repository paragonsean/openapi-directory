/*
 * NFL v3 Scores
 * NFL schedules, scores, odds, weather, and news API.
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
 * ScoreBasic
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:21.929041-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ScoreBasic {
  public static final String SERIALIZED_NAME_AWAY_SCORE = "AwayScore";
  @SerializedName(SERIALIZED_NAME_AWAY_SCORE)
  private Integer awayScore;

  public static final String SERIALIZED_NAME_AWAY_TEAM = "AwayTeam";
  @SerializedName(SERIALIZED_NAME_AWAY_TEAM)
  private String awayTeam;

  public static final String SERIALIZED_NAME_AWAY_TEAM_I_D = "AwayTeamID";
  @SerializedName(SERIALIZED_NAME_AWAY_TEAM_I_D)
  private Integer awayTeamID;

  public static final String SERIALIZED_NAME_CANCELED = "Canceled";
  @SerializedName(SERIALIZED_NAME_CANCELED)
  private Boolean canceled;

  public static final String SERIALIZED_NAME_CLOSED = "Closed";
  @SerializedName(SERIALIZED_NAME_CLOSED)
  private Boolean closed;

  public static final String SERIALIZED_NAME_DATE = "Date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_DATE_TIME = "DateTime";
  @SerializedName(SERIALIZED_NAME_DATE_TIME)
  private String dateTime;

  public static final String SERIALIZED_NAME_DATE_TIME_U_T_C = "DateTimeUTC";
  @SerializedName(SERIALIZED_NAME_DATE_TIME_U_T_C)
  private String dateTimeUTC;

  public static final String SERIALIZED_NAME_DAY = "Day";
  @SerializedName(SERIALIZED_NAME_DAY)
  private String day;

  public static final String SERIALIZED_NAME_GAME_END_DATE_TIME = "GameEndDateTime";
  @SerializedName(SERIALIZED_NAME_GAME_END_DATE_TIME)
  private String gameEndDateTime;

  public static final String SERIALIZED_NAME_GAME_I_D = "GameID";
  @SerializedName(SERIALIZED_NAME_GAME_I_D)
  private Integer gameID;

  public static final String SERIALIZED_NAME_GAME_KEY = "GameKey";
  @SerializedName(SERIALIZED_NAME_GAME_KEY)
  private String gameKey;

  public static final String SERIALIZED_NAME_GLOBAL_AWAY_TEAM_I_D = "GlobalAwayTeamID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_AWAY_TEAM_I_D)
  private Integer globalAwayTeamID;

  public static final String SERIALIZED_NAME_GLOBAL_GAME_I_D = "GlobalGameID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_GAME_I_D)
  private Integer globalGameID;

  public static final String SERIALIZED_NAME_GLOBAL_HOME_TEAM_I_D = "GlobalHomeTeamID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_HOME_TEAM_I_D)
  private Integer globalHomeTeamID;

  public static final String SERIALIZED_NAME_HOME_SCORE = "HomeScore";
  @SerializedName(SERIALIZED_NAME_HOME_SCORE)
  private Integer homeScore;

  public static final String SERIALIZED_NAME_HOME_TEAM = "HomeTeam";
  @SerializedName(SERIALIZED_NAME_HOME_TEAM)
  private String homeTeam;

  public static final String SERIALIZED_NAME_HOME_TEAM_I_D = "HomeTeamID";
  @SerializedName(SERIALIZED_NAME_HOME_TEAM_I_D)
  private Integer homeTeamID;

  public static final String SERIALIZED_NAME_LAST_UPDATED = "LastUpdated";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED)
  private String lastUpdated;

  public static final String SERIALIZED_NAME_QUARTER = "Quarter";
  @SerializedName(SERIALIZED_NAME_QUARTER)
  private String quarter;

  public static final String SERIALIZED_NAME_QUARTER_DESCRIPTION = "QuarterDescription";
  @SerializedName(SERIALIZED_NAME_QUARTER_DESCRIPTION)
  private String quarterDescription;

  public static final String SERIALIZED_NAME_SCORE_I_D = "ScoreID";
  @SerializedName(SERIALIZED_NAME_SCORE_I_D)
  private Integer scoreID;

  public static final String SERIALIZED_NAME_SEASON = "Season";
  @SerializedName(SERIALIZED_NAME_SEASON)
  private Integer season;

  public static final String SERIALIZED_NAME_SEASON_TYPE = "SeasonType";
  @SerializedName(SERIALIZED_NAME_SEASON_TYPE)
  private Integer seasonType;

  public static final String SERIALIZED_NAME_STADIUM_I_D = "StadiumID";
  @SerializedName(SERIALIZED_NAME_STADIUM_I_D)
  private Integer stadiumID;

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TIME_REMAINING = "TimeRemaining";
  @SerializedName(SERIALIZED_NAME_TIME_REMAINING)
  private String timeRemaining;

  public static final String SERIALIZED_NAME_WEEK = "Week";
  @SerializedName(SERIALIZED_NAME_WEEK)
  private Integer week;

  public ScoreBasic() {
  }

  public ScoreBasic awayScore(Integer awayScore) {
    this.awayScore = awayScore;
    return this;
  }

  /**
   * Get awayScore
   * @return awayScore
   */
  @javax.annotation.Nullable
  public Integer getAwayScore() {
    return awayScore;
  }

  public void setAwayScore(Integer awayScore) {
    this.awayScore = awayScore;
  }


  public ScoreBasic awayTeam(String awayTeam) {
    this.awayTeam = awayTeam;
    return this;
  }

  /**
   * Get awayTeam
   * @return awayTeam
   */
  @javax.annotation.Nullable
  public String getAwayTeam() {
    return awayTeam;
  }

  public void setAwayTeam(String awayTeam) {
    this.awayTeam = awayTeam;
  }


  public ScoreBasic awayTeamID(Integer awayTeamID) {
    this.awayTeamID = awayTeamID;
    return this;
  }

  /**
   * Get awayTeamID
   * @return awayTeamID
   */
  @javax.annotation.Nullable
  public Integer getAwayTeamID() {
    return awayTeamID;
  }

  public void setAwayTeamID(Integer awayTeamID) {
    this.awayTeamID = awayTeamID;
  }


  public ScoreBasic canceled(Boolean canceled) {
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


  public ScoreBasic closed(Boolean closed) {
    this.closed = closed;
    return this;
  }

  /**
   * Get closed
   * @return closed
   */
  @javax.annotation.Nullable
  public Boolean getClosed() {
    return closed;
  }

  public void setClosed(Boolean closed) {
    this.closed = closed;
  }


  public ScoreBasic date(String date) {
    this.date = date;
    return this;
  }

  /**
   * Get date
   * @return date
   */
  @javax.annotation.Nullable
  public String getDate() {
    return date;
  }

  public void setDate(String date) {
    this.date = date;
  }


  public ScoreBasic dateTime(String dateTime) {
    this.dateTime = dateTime;
    return this;
  }

  /**
   * Get dateTime
   * @return dateTime
   */
  @javax.annotation.Nullable
  public String getDateTime() {
    return dateTime;
  }

  public void setDateTime(String dateTime) {
    this.dateTime = dateTime;
  }


  public ScoreBasic dateTimeUTC(String dateTimeUTC) {
    this.dateTimeUTC = dateTimeUTC;
    return this;
  }

  /**
   * Get dateTimeUTC
   * @return dateTimeUTC
   */
  @javax.annotation.Nullable
  public String getDateTimeUTC() {
    return dateTimeUTC;
  }

  public void setDateTimeUTC(String dateTimeUTC) {
    this.dateTimeUTC = dateTimeUTC;
  }


  public ScoreBasic day(String day) {
    this.day = day;
    return this;
  }

  /**
   * Get day
   * @return day
   */
  @javax.annotation.Nullable
  public String getDay() {
    return day;
  }

  public void setDay(String day) {
    this.day = day;
  }


  public ScoreBasic gameEndDateTime(String gameEndDateTime) {
    this.gameEndDateTime = gameEndDateTime;
    return this;
  }

  /**
   * Get gameEndDateTime
   * @return gameEndDateTime
   */
  @javax.annotation.Nullable
  public String getGameEndDateTime() {
    return gameEndDateTime;
  }

  public void setGameEndDateTime(String gameEndDateTime) {
    this.gameEndDateTime = gameEndDateTime;
  }


  public ScoreBasic gameID(Integer gameID) {
    this.gameID = gameID;
    return this;
  }

  /**
   * Get gameID
   * @return gameID
   */
  @javax.annotation.Nullable
  public Integer getGameID() {
    return gameID;
  }

  public void setGameID(Integer gameID) {
    this.gameID = gameID;
  }


  public ScoreBasic gameKey(String gameKey) {
    this.gameKey = gameKey;
    return this;
  }

  /**
   * Get gameKey
   * @return gameKey
   */
  @javax.annotation.Nullable
  public String getGameKey() {
    return gameKey;
  }

  public void setGameKey(String gameKey) {
    this.gameKey = gameKey;
  }


  public ScoreBasic globalAwayTeamID(Integer globalAwayTeamID) {
    this.globalAwayTeamID = globalAwayTeamID;
    return this;
  }

  /**
   * Get globalAwayTeamID
   * @return globalAwayTeamID
   */
  @javax.annotation.Nullable
  public Integer getGlobalAwayTeamID() {
    return globalAwayTeamID;
  }

  public void setGlobalAwayTeamID(Integer globalAwayTeamID) {
    this.globalAwayTeamID = globalAwayTeamID;
  }


  public ScoreBasic globalGameID(Integer globalGameID) {
    this.globalGameID = globalGameID;
    return this;
  }

  /**
   * Get globalGameID
   * @return globalGameID
   */
  @javax.annotation.Nullable
  public Integer getGlobalGameID() {
    return globalGameID;
  }

  public void setGlobalGameID(Integer globalGameID) {
    this.globalGameID = globalGameID;
  }


  public ScoreBasic globalHomeTeamID(Integer globalHomeTeamID) {
    this.globalHomeTeamID = globalHomeTeamID;
    return this;
  }

  /**
   * Get globalHomeTeamID
   * @return globalHomeTeamID
   */
  @javax.annotation.Nullable
  public Integer getGlobalHomeTeamID() {
    return globalHomeTeamID;
  }

  public void setGlobalHomeTeamID(Integer globalHomeTeamID) {
    this.globalHomeTeamID = globalHomeTeamID;
  }


  public ScoreBasic homeScore(Integer homeScore) {
    this.homeScore = homeScore;
    return this;
  }

  /**
   * Get homeScore
   * @return homeScore
   */
  @javax.annotation.Nullable
  public Integer getHomeScore() {
    return homeScore;
  }

  public void setHomeScore(Integer homeScore) {
    this.homeScore = homeScore;
  }


  public ScoreBasic homeTeam(String homeTeam) {
    this.homeTeam = homeTeam;
    return this;
  }

  /**
   * Get homeTeam
   * @return homeTeam
   */
  @javax.annotation.Nullable
  public String getHomeTeam() {
    return homeTeam;
  }

  public void setHomeTeam(String homeTeam) {
    this.homeTeam = homeTeam;
  }


  public ScoreBasic homeTeamID(Integer homeTeamID) {
    this.homeTeamID = homeTeamID;
    return this;
  }

  /**
   * Get homeTeamID
   * @return homeTeamID
   */
  @javax.annotation.Nullable
  public Integer getHomeTeamID() {
    return homeTeamID;
  }

  public void setHomeTeamID(Integer homeTeamID) {
    this.homeTeamID = homeTeamID;
  }


  public ScoreBasic lastUpdated(String lastUpdated) {
    this.lastUpdated = lastUpdated;
    return this;
  }

  /**
   * Get lastUpdated
   * @return lastUpdated
   */
  @javax.annotation.Nullable
  public String getLastUpdated() {
    return lastUpdated;
  }

  public void setLastUpdated(String lastUpdated) {
    this.lastUpdated = lastUpdated;
  }


  public ScoreBasic quarter(String quarter) {
    this.quarter = quarter;
    return this;
  }

  /**
   * Get quarter
   * @return quarter
   */
  @javax.annotation.Nullable
  public String getQuarter() {
    return quarter;
  }

  public void setQuarter(String quarter) {
    this.quarter = quarter;
  }


  public ScoreBasic quarterDescription(String quarterDescription) {
    this.quarterDescription = quarterDescription;
    return this;
  }

  /**
   * Get quarterDescription
   * @return quarterDescription
   */
  @javax.annotation.Nullable
  public String getQuarterDescription() {
    return quarterDescription;
  }

  public void setQuarterDescription(String quarterDescription) {
    this.quarterDescription = quarterDescription;
  }


  public ScoreBasic scoreID(Integer scoreID) {
    this.scoreID = scoreID;
    return this;
  }

  /**
   * Get scoreID
   * @return scoreID
   */
  @javax.annotation.Nullable
  public Integer getScoreID() {
    return scoreID;
  }

  public void setScoreID(Integer scoreID) {
    this.scoreID = scoreID;
  }


  public ScoreBasic season(Integer season) {
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


  public ScoreBasic seasonType(Integer seasonType) {
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


  public ScoreBasic stadiumID(Integer stadiumID) {
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


  public ScoreBasic status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public ScoreBasic timeRemaining(String timeRemaining) {
    this.timeRemaining = timeRemaining;
    return this;
  }

  /**
   * Get timeRemaining
   * @return timeRemaining
   */
  @javax.annotation.Nullable
  public String getTimeRemaining() {
    return timeRemaining;
  }

  public void setTimeRemaining(String timeRemaining) {
    this.timeRemaining = timeRemaining;
  }


  public ScoreBasic week(Integer week) {
    this.week = week;
    return this;
  }

  /**
   * Get week
   * @return week
   */
  @javax.annotation.Nullable
  public Integer getWeek() {
    return week;
  }

  public void setWeek(Integer week) {
    this.week = week;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ScoreBasic scoreBasic = (ScoreBasic) o;
    return Objects.equals(this.awayScore, scoreBasic.awayScore) &&
        Objects.equals(this.awayTeam, scoreBasic.awayTeam) &&
        Objects.equals(this.awayTeamID, scoreBasic.awayTeamID) &&
        Objects.equals(this.canceled, scoreBasic.canceled) &&
        Objects.equals(this.closed, scoreBasic.closed) &&
        Objects.equals(this.date, scoreBasic.date) &&
        Objects.equals(this.dateTime, scoreBasic.dateTime) &&
        Objects.equals(this.dateTimeUTC, scoreBasic.dateTimeUTC) &&
        Objects.equals(this.day, scoreBasic.day) &&
        Objects.equals(this.gameEndDateTime, scoreBasic.gameEndDateTime) &&
        Objects.equals(this.gameID, scoreBasic.gameID) &&
        Objects.equals(this.gameKey, scoreBasic.gameKey) &&
        Objects.equals(this.globalAwayTeamID, scoreBasic.globalAwayTeamID) &&
        Objects.equals(this.globalGameID, scoreBasic.globalGameID) &&
        Objects.equals(this.globalHomeTeamID, scoreBasic.globalHomeTeamID) &&
        Objects.equals(this.homeScore, scoreBasic.homeScore) &&
        Objects.equals(this.homeTeam, scoreBasic.homeTeam) &&
        Objects.equals(this.homeTeamID, scoreBasic.homeTeamID) &&
        Objects.equals(this.lastUpdated, scoreBasic.lastUpdated) &&
        Objects.equals(this.quarter, scoreBasic.quarter) &&
        Objects.equals(this.quarterDescription, scoreBasic.quarterDescription) &&
        Objects.equals(this.scoreID, scoreBasic.scoreID) &&
        Objects.equals(this.season, scoreBasic.season) &&
        Objects.equals(this.seasonType, scoreBasic.seasonType) &&
        Objects.equals(this.stadiumID, scoreBasic.stadiumID) &&
        Objects.equals(this.status, scoreBasic.status) &&
        Objects.equals(this.timeRemaining, scoreBasic.timeRemaining) &&
        Objects.equals(this.week, scoreBasic.week);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(awayScore, awayTeam, awayTeamID, canceled, closed, date, dateTime, dateTimeUTC, day, gameEndDateTime, gameID, gameKey, globalAwayTeamID, globalGameID, globalHomeTeamID, homeScore, homeTeam, homeTeamID, lastUpdated, quarter, quarterDescription, scoreID, season, seasonType, stadiumID, status, timeRemaining, week);
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
    sb.append("class ScoreBasic {\n");
    sb.append("    awayScore: ").append(toIndentedString(awayScore)).append("\n");
    sb.append("    awayTeam: ").append(toIndentedString(awayTeam)).append("\n");
    sb.append("    awayTeamID: ").append(toIndentedString(awayTeamID)).append("\n");
    sb.append("    canceled: ").append(toIndentedString(canceled)).append("\n");
    sb.append("    closed: ").append(toIndentedString(closed)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    dateTime: ").append(toIndentedString(dateTime)).append("\n");
    sb.append("    dateTimeUTC: ").append(toIndentedString(dateTimeUTC)).append("\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    gameEndDateTime: ").append(toIndentedString(gameEndDateTime)).append("\n");
    sb.append("    gameID: ").append(toIndentedString(gameID)).append("\n");
    sb.append("    gameKey: ").append(toIndentedString(gameKey)).append("\n");
    sb.append("    globalAwayTeamID: ").append(toIndentedString(globalAwayTeamID)).append("\n");
    sb.append("    globalGameID: ").append(toIndentedString(globalGameID)).append("\n");
    sb.append("    globalHomeTeamID: ").append(toIndentedString(globalHomeTeamID)).append("\n");
    sb.append("    homeScore: ").append(toIndentedString(homeScore)).append("\n");
    sb.append("    homeTeam: ").append(toIndentedString(homeTeam)).append("\n");
    sb.append("    homeTeamID: ").append(toIndentedString(homeTeamID)).append("\n");
    sb.append("    lastUpdated: ").append(toIndentedString(lastUpdated)).append("\n");
    sb.append("    quarter: ").append(toIndentedString(quarter)).append("\n");
    sb.append("    quarterDescription: ").append(toIndentedString(quarterDescription)).append("\n");
    sb.append("    scoreID: ").append(toIndentedString(scoreID)).append("\n");
    sb.append("    season: ").append(toIndentedString(season)).append("\n");
    sb.append("    seasonType: ").append(toIndentedString(seasonType)).append("\n");
    sb.append("    stadiumID: ").append(toIndentedString(stadiumID)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    timeRemaining: ").append(toIndentedString(timeRemaining)).append("\n");
    sb.append("    week: ").append(toIndentedString(week)).append("\n");
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
    openapiFields.add("AwayScore");
    openapiFields.add("AwayTeam");
    openapiFields.add("AwayTeamID");
    openapiFields.add("Canceled");
    openapiFields.add("Closed");
    openapiFields.add("Date");
    openapiFields.add("DateTime");
    openapiFields.add("DateTimeUTC");
    openapiFields.add("Day");
    openapiFields.add("GameEndDateTime");
    openapiFields.add("GameID");
    openapiFields.add("GameKey");
    openapiFields.add("GlobalAwayTeamID");
    openapiFields.add("GlobalGameID");
    openapiFields.add("GlobalHomeTeamID");
    openapiFields.add("HomeScore");
    openapiFields.add("HomeTeam");
    openapiFields.add("HomeTeamID");
    openapiFields.add("LastUpdated");
    openapiFields.add("Quarter");
    openapiFields.add("QuarterDescription");
    openapiFields.add("ScoreID");
    openapiFields.add("Season");
    openapiFields.add("SeasonType");
    openapiFields.add("StadiumID");
    openapiFields.add("Status");
    openapiFields.add("TimeRemaining");
    openapiFields.add("Week");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ScoreBasic
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ScoreBasic.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ScoreBasic is not found in the empty JSON string", ScoreBasic.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ScoreBasic.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ScoreBasic` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AwayTeam") != null && !jsonObj.get("AwayTeam").isJsonNull()) && !jsonObj.get("AwayTeam").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AwayTeam` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AwayTeam").toString()));
      }
      if ((jsonObj.get("Date") != null && !jsonObj.get("Date").isJsonNull()) && !jsonObj.get("Date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Date").toString()));
      }
      if ((jsonObj.get("DateTime") != null && !jsonObj.get("DateTime").isJsonNull()) && !jsonObj.get("DateTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DateTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DateTime").toString()));
      }
      if ((jsonObj.get("DateTimeUTC") != null && !jsonObj.get("DateTimeUTC").isJsonNull()) && !jsonObj.get("DateTimeUTC").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DateTimeUTC` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DateTimeUTC").toString()));
      }
      if ((jsonObj.get("Day") != null && !jsonObj.get("Day").isJsonNull()) && !jsonObj.get("Day").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Day` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Day").toString()));
      }
      if ((jsonObj.get("GameEndDateTime") != null && !jsonObj.get("GameEndDateTime").isJsonNull()) && !jsonObj.get("GameEndDateTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `GameEndDateTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("GameEndDateTime").toString()));
      }
      if ((jsonObj.get("GameKey") != null && !jsonObj.get("GameKey").isJsonNull()) && !jsonObj.get("GameKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `GameKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("GameKey").toString()));
      }
      if ((jsonObj.get("HomeTeam") != null && !jsonObj.get("HomeTeam").isJsonNull()) && !jsonObj.get("HomeTeam").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `HomeTeam` to be a primitive type in the JSON string but got `%s`", jsonObj.get("HomeTeam").toString()));
      }
      if ((jsonObj.get("LastUpdated") != null && !jsonObj.get("LastUpdated").isJsonNull()) && !jsonObj.get("LastUpdated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LastUpdated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LastUpdated").toString()));
      }
      if ((jsonObj.get("Quarter") != null && !jsonObj.get("Quarter").isJsonNull()) && !jsonObj.get("Quarter").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Quarter` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Quarter").toString()));
      }
      if ((jsonObj.get("QuarterDescription") != null && !jsonObj.get("QuarterDescription").isJsonNull()) && !jsonObj.get("QuarterDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `QuarterDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("QuarterDescription").toString()));
      }
      if ((jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) && !jsonObj.get("Status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Status").toString()));
      }
      if ((jsonObj.get("TimeRemaining") != null && !jsonObj.get("TimeRemaining").isJsonNull()) && !jsonObj.get("TimeRemaining").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TimeRemaining` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TimeRemaining").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ScoreBasic.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ScoreBasic' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ScoreBasic> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ScoreBasic.class));

       return (TypeAdapter<T>) new TypeAdapter<ScoreBasic>() {
           @Override
           public void write(JsonWriter out, ScoreBasic value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ScoreBasic read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ScoreBasic given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ScoreBasic
   * @throws IOException if the JSON string is invalid with respect to ScoreBasic
   */
  public static ScoreBasic fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ScoreBasic.class);
  }

  /**
   * Convert an instance of ScoreBasic to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

