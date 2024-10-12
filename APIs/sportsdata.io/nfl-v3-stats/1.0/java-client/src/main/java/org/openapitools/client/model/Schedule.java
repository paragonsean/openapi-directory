/*
 * NFL v3 Stats
 * NFL rosters, player stats, team stats, and fantasy stats API.
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
import org.openapitools.client.model.Stadium;
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
 * Schedule
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:11.789534-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Schedule {
  public static final String SERIALIZED_NAME_AWAY_TEAM = "AwayTeam";
  @SerializedName(SERIALIZED_NAME_AWAY_TEAM)
  private String awayTeam;

  public static final String SERIALIZED_NAME_AWAY_TEAM_MONEY_LINE = "AwayTeamMoneyLine";
  @SerializedName(SERIALIZED_NAME_AWAY_TEAM_MONEY_LINE)
  private Integer awayTeamMoneyLine;

  public static final String SERIALIZED_NAME_CANCELED = "Canceled";
  @SerializedName(SERIALIZED_NAME_CANCELED)
  private Boolean canceled;

  public static final String SERIALIZED_NAME_CHANNEL = "Channel";
  @SerializedName(SERIALIZED_NAME_CHANNEL)
  private String channel;

  public static final String SERIALIZED_NAME_DATE = "Date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_DATE_TIME = "DateTime";
  @SerializedName(SERIALIZED_NAME_DATE_TIME)
  private String dateTime;

  public static final String SERIALIZED_NAME_DAY = "Day";
  @SerializedName(SERIALIZED_NAME_DAY)
  private String day;

  public static final String SERIALIZED_NAME_FORECAST_DESCRIPTION = "ForecastDescription";
  @SerializedName(SERIALIZED_NAME_FORECAST_DESCRIPTION)
  private String forecastDescription;

  public static final String SERIALIZED_NAME_FORECAST_TEMP_HIGH = "ForecastTempHigh";
  @SerializedName(SERIALIZED_NAME_FORECAST_TEMP_HIGH)
  private Integer forecastTempHigh;

  public static final String SERIALIZED_NAME_FORECAST_TEMP_LOW = "ForecastTempLow";
  @SerializedName(SERIALIZED_NAME_FORECAST_TEMP_LOW)
  private Integer forecastTempLow;

  public static final String SERIALIZED_NAME_FORECAST_WIND_CHILL = "ForecastWindChill";
  @SerializedName(SERIALIZED_NAME_FORECAST_WIND_CHILL)
  private Integer forecastWindChill;

  public static final String SERIALIZED_NAME_FORECAST_WIND_SPEED = "ForecastWindSpeed";
  @SerializedName(SERIALIZED_NAME_FORECAST_WIND_SPEED)
  private Integer forecastWindSpeed;

  public static final String SERIALIZED_NAME_GAME_KEY = "GameKey";
  @SerializedName(SERIALIZED_NAME_GAME_KEY)
  private String gameKey;

  public static final String SERIALIZED_NAME_GEO_LAT = "GeoLat";
  @SerializedName(SERIALIZED_NAME_GEO_LAT)
  private BigDecimal geoLat;

  public static final String SERIALIZED_NAME_GEO_LONG = "GeoLong";
  @SerializedName(SERIALIZED_NAME_GEO_LONG)
  private BigDecimal geoLong;

  public static final String SERIALIZED_NAME_GLOBAL_AWAY_TEAM_I_D = "GlobalAwayTeamID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_AWAY_TEAM_I_D)
  private Integer globalAwayTeamID;

  public static final String SERIALIZED_NAME_GLOBAL_GAME_I_D = "GlobalGameID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_GAME_I_D)
  private Integer globalGameID;

  public static final String SERIALIZED_NAME_GLOBAL_HOME_TEAM_I_D = "GlobalHomeTeamID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_HOME_TEAM_I_D)
  private Integer globalHomeTeamID;

  public static final String SERIALIZED_NAME_HOME_TEAM = "HomeTeam";
  @SerializedName(SERIALIZED_NAME_HOME_TEAM)
  private String homeTeam;

  public static final String SERIALIZED_NAME_HOME_TEAM_MONEY_LINE = "HomeTeamMoneyLine";
  @SerializedName(SERIALIZED_NAME_HOME_TEAM_MONEY_LINE)
  private Integer homeTeamMoneyLine;

  public static final String SERIALIZED_NAME_OVER_UNDER = "OverUnder";
  @SerializedName(SERIALIZED_NAME_OVER_UNDER)
  private BigDecimal overUnder;

  public static final String SERIALIZED_NAME_POINT_SPREAD = "PointSpread";
  @SerializedName(SERIALIZED_NAME_POINT_SPREAD)
  private BigDecimal pointSpread;

  public static final String SERIALIZED_NAME_SCORE_I_D = "ScoreID";
  @SerializedName(SERIALIZED_NAME_SCORE_I_D)
  private Integer scoreID;

  public static final String SERIALIZED_NAME_SEASON = "Season";
  @SerializedName(SERIALIZED_NAME_SEASON)
  private Integer season;

  public static final String SERIALIZED_NAME_SEASON_TYPE = "SeasonType";
  @SerializedName(SERIALIZED_NAME_SEASON_TYPE)
  private Integer seasonType;

  public static final String SERIALIZED_NAME_STADIUM_DETAILS = "StadiumDetails";
  @SerializedName(SERIALIZED_NAME_STADIUM_DETAILS)
  private Stadium stadiumDetails;

  public static final String SERIALIZED_NAME_STADIUM_I_D = "StadiumID";
  @SerializedName(SERIALIZED_NAME_STADIUM_I_D)
  private Integer stadiumID;

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_WEEK = "Week";
  @SerializedName(SERIALIZED_NAME_WEEK)
  private Integer week;

  public Schedule() {
  }

  public Schedule awayTeam(String awayTeam) {
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


  public Schedule awayTeamMoneyLine(Integer awayTeamMoneyLine) {
    this.awayTeamMoneyLine = awayTeamMoneyLine;
    return this;
  }

  /**
   * Get awayTeamMoneyLine
   * @return awayTeamMoneyLine
   */
  @javax.annotation.Nullable
  public Integer getAwayTeamMoneyLine() {
    return awayTeamMoneyLine;
  }

  public void setAwayTeamMoneyLine(Integer awayTeamMoneyLine) {
    this.awayTeamMoneyLine = awayTeamMoneyLine;
  }


  public Schedule canceled(Boolean canceled) {
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


  public Schedule channel(String channel) {
    this.channel = channel;
    return this;
  }

  /**
   * Get channel
   * @return channel
   */
  @javax.annotation.Nullable
  public String getChannel() {
    return channel;
  }

  public void setChannel(String channel) {
    this.channel = channel;
  }


  public Schedule date(String date) {
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


  public Schedule dateTime(String dateTime) {
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


  public Schedule day(String day) {
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


  public Schedule forecastDescription(String forecastDescription) {
    this.forecastDescription = forecastDescription;
    return this;
  }

  /**
   * Get forecastDescription
   * @return forecastDescription
   */
  @javax.annotation.Nullable
  public String getForecastDescription() {
    return forecastDescription;
  }

  public void setForecastDescription(String forecastDescription) {
    this.forecastDescription = forecastDescription;
  }


  public Schedule forecastTempHigh(Integer forecastTempHigh) {
    this.forecastTempHigh = forecastTempHigh;
    return this;
  }

  /**
   * Get forecastTempHigh
   * @return forecastTempHigh
   */
  @javax.annotation.Nullable
  public Integer getForecastTempHigh() {
    return forecastTempHigh;
  }

  public void setForecastTempHigh(Integer forecastTempHigh) {
    this.forecastTempHigh = forecastTempHigh;
  }


  public Schedule forecastTempLow(Integer forecastTempLow) {
    this.forecastTempLow = forecastTempLow;
    return this;
  }

  /**
   * Get forecastTempLow
   * @return forecastTempLow
   */
  @javax.annotation.Nullable
  public Integer getForecastTempLow() {
    return forecastTempLow;
  }

  public void setForecastTempLow(Integer forecastTempLow) {
    this.forecastTempLow = forecastTempLow;
  }


  public Schedule forecastWindChill(Integer forecastWindChill) {
    this.forecastWindChill = forecastWindChill;
    return this;
  }

  /**
   * Get forecastWindChill
   * @return forecastWindChill
   */
  @javax.annotation.Nullable
  public Integer getForecastWindChill() {
    return forecastWindChill;
  }

  public void setForecastWindChill(Integer forecastWindChill) {
    this.forecastWindChill = forecastWindChill;
  }


  public Schedule forecastWindSpeed(Integer forecastWindSpeed) {
    this.forecastWindSpeed = forecastWindSpeed;
    return this;
  }

  /**
   * Get forecastWindSpeed
   * @return forecastWindSpeed
   */
  @javax.annotation.Nullable
  public Integer getForecastWindSpeed() {
    return forecastWindSpeed;
  }

  public void setForecastWindSpeed(Integer forecastWindSpeed) {
    this.forecastWindSpeed = forecastWindSpeed;
  }


  public Schedule gameKey(String gameKey) {
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


  public Schedule geoLat(BigDecimal geoLat) {
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


  public Schedule geoLong(BigDecimal geoLong) {
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


  public Schedule globalAwayTeamID(Integer globalAwayTeamID) {
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


  public Schedule globalGameID(Integer globalGameID) {
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


  public Schedule globalHomeTeamID(Integer globalHomeTeamID) {
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


  public Schedule homeTeam(String homeTeam) {
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


  public Schedule homeTeamMoneyLine(Integer homeTeamMoneyLine) {
    this.homeTeamMoneyLine = homeTeamMoneyLine;
    return this;
  }

  /**
   * Get homeTeamMoneyLine
   * @return homeTeamMoneyLine
   */
  @javax.annotation.Nullable
  public Integer getHomeTeamMoneyLine() {
    return homeTeamMoneyLine;
  }

  public void setHomeTeamMoneyLine(Integer homeTeamMoneyLine) {
    this.homeTeamMoneyLine = homeTeamMoneyLine;
  }


  public Schedule overUnder(BigDecimal overUnder) {
    this.overUnder = overUnder;
    return this;
  }

  /**
   * Get overUnder
   * @return overUnder
   */
  @javax.annotation.Nullable
  public BigDecimal getOverUnder() {
    return overUnder;
  }

  public void setOverUnder(BigDecimal overUnder) {
    this.overUnder = overUnder;
  }


  public Schedule pointSpread(BigDecimal pointSpread) {
    this.pointSpread = pointSpread;
    return this;
  }

  /**
   * Get pointSpread
   * @return pointSpread
   */
  @javax.annotation.Nullable
  public BigDecimal getPointSpread() {
    return pointSpread;
  }

  public void setPointSpread(BigDecimal pointSpread) {
    this.pointSpread = pointSpread;
  }


  public Schedule scoreID(Integer scoreID) {
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


  public Schedule season(Integer season) {
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


  public Schedule seasonType(Integer seasonType) {
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


  public Schedule stadiumDetails(Stadium stadiumDetails) {
    this.stadiumDetails = stadiumDetails;
    return this;
  }

  /**
   * Get stadiumDetails
   * @return stadiumDetails
   */
  @javax.annotation.Nullable
  public Stadium getStadiumDetails() {
    return stadiumDetails;
  }

  public void setStadiumDetails(Stadium stadiumDetails) {
    this.stadiumDetails = stadiumDetails;
  }


  public Schedule stadiumID(Integer stadiumID) {
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


  public Schedule status(String status) {
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


  public Schedule week(Integer week) {
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
    Schedule schedule = (Schedule) o;
    return Objects.equals(this.awayTeam, schedule.awayTeam) &&
        Objects.equals(this.awayTeamMoneyLine, schedule.awayTeamMoneyLine) &&
        Objects.equals(this.canceled, schedule.canceled) &&
        Objects.equals(this.channel, schedule.channel) &&
        Objects.equals(this.date, schedule.date) &&
        Objects.equals(this.dateTime, schedule.dateTime) &&
        Objects.equals(this.day, schedule.day) &&
        Objects.equals(this.forecastDescription, schedule.forecastDescription) &&
        Objects.equals(this.forecastTempHigh, schedule.forecastTempHigh) &&
        Objects.equals(this.forecastTempLow, schedule.forecastTempLow) &&
        Objects.equals(this.forecastWindChill, schedule.forecastWindChill) &&
        Objects.equals(this.forecastWindSpeed, schedule.forecastWindSpeed) &&
        Objects.equals(this.gameKey, schedule.gameKey) &&
        Objects.equals(this.geoLat, schedule.geoLat) &&
        Objects.equals(this.geoLong, schedule.geoLong) &&
        Objects.equals(this.globalAwayTeamID, schedule.globalAwayTeamID) &&
        Objects.equals(this.globalGameID, schedule.globalGameID) &&
        Objects.equals(this.globalHomeTeamID, schedule.globalHomeTeamID) &&
        Objects.equals(this.homeTeam, schedule.homeTeam) &&
        Objects.equals(this.homeTeamMoneyLine, schedule.homeTeamMoneyLine) &&
        Objects.equals(this.overUnder, schedule.overUnder) &&
        Objects.equals(this.pointSpread, schedule.pointSpread) &&
        Objects.equals(this.scoreID, schedule.scoreID) &&
        Objects.equals(this.season, schedule.season) &&
        Objects.equals(this.seasonType, schedule.seasonType) &&
        Objects.equals(this.stadiumDetails, schedule.stadiumDetails) &&
        Objects.equals(this.stadiumID, schedule.stadiumID) &&
        Objects.equals(this.status, schedule.status) &&
        Objects.equals(this.week, schedule.week);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(awayTeam, awayTeamMoneyLine, canceled, channel, date, dateTime, day, forecastDescription, forecastTempHigh, forecastTempLow, forecastWindChill, forecastWindSpeed, gameKey, geoLat, geoLong, globalAwayTeamID, globalGameID, globalHomeTeamID, homeTeam, homeTeamMoneyLine, overUnder, pointSpread, scoreID, season, seasonType, stadiumDetails, stadiumID, status, week);
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
    sb.append("class Schedule {\n");
    sb.append("    awayTeam: ").append(toIndentedString(awayTeam)).append("\n");
    sb.append("    awayTeamMoneyLine: ").append(toIndentedString(awayTeamMoneyLine)).append("\n");
    sb.append("    canceled: ").append(toIndentedString(canceled)).append("\n");
    sb.append("    channel: ").append(toIndentedString(channel)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    dateTime: ").append(toIndentedString(dateTime)).append("\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    forecastDescription: ").append(toIndentedString(forecastDescription)).append("\n");
    sb.append("    forecastTempHigh: ").append(toIndentedString(forecastTempHigh)).append("\n");
    sb.append("    forecastTempLow: ").append(toIndentedString(forecastTempLow)).append("\n");
    sb.append("    forecastWindChill: ").append(toIndentedString(forecastWindChill)).append("\n");
    sb.append("    forecastWindSpeed: ").append(toIndentedString(forecastWindSpeed)).append("\n");
    sb.append("    gameKey: ").append(toIndentedString(gameKey)).append("\n");
    sb.append("    geoLat: ").append(toIndentedString(geoLat)).append("\n");
    sb.append("    geoLong: ").append(toIndentedString(geoLong)).append("\n");
    sb.append("    globalAwayTeamID: ").append(toIndentedString(globalAwayTeamID)).append("\n");
    sb.append("    globalGameID: ").append(toIndentedString(globalGameID)).append("\n");
    sb.append("    globalHomeTeamID: ").append(toIndentedString(globalHomeTeamID)).append("\n");
    sb.append("    homeTeam: ").append(toIndentedString(homeTeam)).append("\n");
    sb.append("    homeTeamMoneyLine: ").append(toIndentedString(homeTeamMoneyLine)).append("\n");
    sb.append("    overUnder: ").append(toIndentedString(overUnder)).append("\n");
    sb.append("    pointSpread: ").append(toIndentedString(pointSpread)).append("\n");
    sb.append("    scoreID: ").append(toIndentedString(scoreID)).append("\n");
    sb.append("    season: ").append(toIndentedString(season)).append("\n");
    sb.append("    seasonType: ").append(toIndentedString(seasonType)).append("\n");
    sb.append("    stadiumDetails: ").append(toIndentedString(stadiumDetails)).append("\n");
    sb.append("    stadiumID: ").append(toIndentedString(stadiumID)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
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
    openapiFields.add("AwayTeam");
    openapiFields.add("AwayTeamMoneyLine");
    openapiFields.add("Canceled");
    openapiFields.add("Channel");
    openapiFields.add("Date");
    openapiFields.add("DateTime");
    openapiFields.add("Day");
    openapiFields.add("ForecastDescription");
    openapiFields.add("ForecastTempHigh");
    openapiFields.add("ForecastTempLow");
    openapiFields.add("ForecastWindChill");
    openapiFields.add("ForecastWindSpeed");
    openapiFields.add("GameKey");
    openapiFields.add("GeoLat");
    openapiFields.add("GeoLong");
    openapiFields.add("GlobalAwayTeamID");
    openapiFields.add("GlobalGameID");
    openapiFields.add("GlobalHomeTeamID");
    openapiFields.add("HomeTeam");
    openapiFields.add("HomeTeamMoneyLine");
    openapiFields.add("OverUnder");
    openapiFields.add("PointSpread");
    openapiFields.add("ScoreID");
    openapiFields.add("Season");
    openapiFields.add("SeasonType");
    openapiFields.add("StadiumDetails");
    openapiFields.add("StadiumID");
    openapiFields.add("Status");
    openapiFields.add("Week");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Schedule
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Schedule.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Schedule is not found in the empty JSON string", Schedule.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Schedule.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Schedule` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AwayTeam") != null && !jsonObj.get("AwayTeam").isJsonNull()) && !jsonObj.get("AwayTeam").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AwayTeam` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AwayTeam").toString()));
      }
      if ((jsonObj.get("Channel") != null && !jsonObj.get("Channel").isJsonNull()) && !jsonObj.get("Channel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Channel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Channel").toString()));
      }
      if ((jsonObj.get("Date") != null && !jsonObj.get("Date").isJsonNull()) && !jsonObj.get("Date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Date").toString()));
      }
      if ((jsonObj.get("DateTime") != null && !jsonObj.get("DateTime").isJsonNull()) && !jsonObj.get("DateTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DateTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DateTime").toString()));
      }
      if ((jsonObj.get("Day") != null && !jsonObj.get("Day").isJsonNull()) && !jsonObj.get("Day").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Day` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Day").toString()));
      }
      if ((jsonObj.get("ForecastDescription") != null && !jsonObj.get("ForecastDescription").isJsonNull()) && !jsonObj.get("ForecastDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ForecastDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ForecastDescription").toString()));
      }
      if ((jsonObj.get("GameKey") != null && !jsonObj.get("GameKey").isJsonNull()) && !jsonObj.get("GameKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `GameKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("GameKey").toString()));
      }
      if ((jsonObj.get("HomeTeam") != null && !jsonObj.get("HomeTeam").isJsonNull()) && !jsonObj.get("HomeTeam").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `HomeTeam` to be a primitive type in the JSON string but got `%s`", jsonObj.get("HomeTeam").toString()));
      }
      // validate the optional field `StadiumDetails`
      if (jsonObj.get("StadiumDetails") != null && !jsonObj.get("StadiumDetails").isJsonNull()) {
        Stadium.validateJsonElement(jsonObj.get("StadiumDetails"));
      }
      if ((jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) && !jsonObj.get("Status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Schedule.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Schedule' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Schedule> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Schedule.class));

       return (TypeAdapter<T>) new TypeAdapter<Schedule>() {
           @Override
           public void write(JsonWriter out, Schedule value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Schedule read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Schedule given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Schedule
   * @throws IOException if the JSON string is invalid with respect to Schedule
   */
  public static Schedule fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Schedule.class);
  }

  /**
   * Convert an instance of Schedule to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

