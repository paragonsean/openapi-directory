/*
 * LoL v3 Scores
 * LoL v3 Scores
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
 * Game
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:25.501979-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Game {
  public static final String SERIALIZED_NAME_BEST_OF = "BestOf";
  @SerializedName(SERIALIZED_NAME_BEST_OF)
  private String bestOf;

  public static final String SERIALIZED_NAME_DATE_TIME = "DateTime";
  @SerializedName(SERIALIZED_NAME_DATE_TIME)
  private String dateTime;

  public static final String SERIALIZED_NAME_DAY = "Day";
  @SerializedName(SERIALIZED_NAME_DAY)
  private String day;

  public static final String SERIALIZED_NAME_DRAW_MONEY_LINE = "DrawMoneyLine";
  @SerializedName(SERIALIZED_NAME_DRAW_MONEY_LINE)
  private Integer drawMoneyLine;

  public static final String SERIALIZED_NAME_GAME_ID = "GameId";
  @SerializedName(SERIALIZED_NAME_GAME_ID)
  private Integer gameId;

  public static final String SERIALIZED_NAME_GROUP = "Group";
  @SerializedName(SERIALIZED_NAME_GROUP)
  private String group;

  public static final String SERIALIZED_NAME_IS_CLOSED = "IsClosed";
  @SerializedName(SERIALIZED_NAME_IS_CLOSED)
  private Boolean isClosed;

  public static final String SERIALIZED_NAME_POINT_SPREAD = "PointSpread";
  @SerializedName(SERIALIZED_NAME_POINT_SPREAD)
  private BigDecimal pointSpread;

  public static final String SERIALIZED_NAME_ROUND_ID = "RoundId";
  @SerializedName(SERIALIZED_NAME_ROUND_ID)
  private Integer roundId;

  public static final String SERIALIZED_NAME_SEASON = "Season";
  @SerializedName(SERIALIZED_NAME_SEASON)
  private Integer season;

  public static final String SERIALIZED_NAME_SEASON_TYPE = "SeasonType";
  @SerializedName(SERIALIZED_NAME_SEASON_TYPE)
  private Integer seasonType;

  public static final String SERIALIZED_NAME_STATUS = "Status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TEAM_A_ID = "TeamAId";
  @SerializedName(SERIALIZED_NAME_TEAM_A_ID)
  private Integer teamAId;

  public static final String SERIALIZED_NAME_TEAM_A_KEY = "TeamAKey";
  @SerializedName(SERIALIZED_NAME_TEAM_A_KEY)
  private String teamAKey;

  public static final String SERIALIZED_NAME_TEAM_A_MONEY_LINE = "TeamAMoneyLine";
  @SerializedName(SERIALIZED_NAME_TEAM_A_MONEY_LINE)
  private Integer teamAMoneyLine;

  public static final String SERIALIZED_NAME_TEAM_A_NAME = "TeamAName";
  @SerializedName(SERIALIZED_NAME_TEAM_A_NAME)
  private String teamAName;

  public static final String SERIALIZED_NAME_TEAM_A_POINT_SPREAD_PAYOUT = "TeamAPointSpreadPayout";
  @SerializedName(SERIALIZED_NAME_TEAM_A_POINT_SPREAD_PAYOUT)
  private Integer teamAPointSpreadPayout;

  public static final String SERIALIZED_NAME_TEAM_A_SCORE = "TeamAScore";
  @SerializedName(SERIALIZED_NAME_TEAM_A_SCORE)
  private Integer teamAScore;

  public static final String SERIALIZED_NAME_TEAM_B_ID = "TeamBId";
  @SerializedName(SERIALIZED_NAME_TEAM_B_ID)
  private Integer teamBId;

  public static final String SERIALIZED_NAME_TEAM_B_KEY = "TeamBKey";
  @SerializedName(SERIALIZED_NAME_TEAM_B_KEY)
  private String teamBKey;

  public static final String SERIALIZED_NAME_TEAM_B_MONEY_LINE = "TeamBMoneyLine";
  @SerializedName(SERIALIZED_NAME_TEAM_B_MONEY_LINE)
  private Integer teamBMoneyLine;

  public static final String SERIALIZED_NAME_TEAM_B_NAME = "TeamBName";
  @SerializedName(SERIALIZED_NAME_TEAM_B_NAME)
  private String teamBName;

  public static final String SERIALIZED_NAME_TEAM_B_POINT_SPREAD_PAYOUT = "TeamBPointSpreadPayout";
  @SerializedName(SERIALIZED_NAME_TEAM_B_POINT_SPREAD_PAYOUT)
  private Integer teamBPointSpreadPayout;

  public static final String SERIALIZED_NAME_TEAM_B_SCORE = "TeamBScore";
  @SerializedName(SERIALIZED_NAME_TEAM_B_SCORE)
  private Integer teamBScore;

  public static final String SERIALIZED_NAME_UPDATED = "Updated";
  @SerializedName(SERIALIZED_NAME_UPDATED)
  private String updated;

  public static final String SERIALIZED_NAME_UPDATED_UTC = "UpdatedUtc";
  @SerializedName(SERIALIZED_NAME_UPDATED_UTC)
  private String updatedUtc;

  public static final String SERIALIZED_NAME_VENUE_ID = "VenueId";
  @SerializedName(SERIALIZED_NAME_VENUE_ID)
  private Integer venueId;

  public static final String SERIALIZED_NAME_VENUE_TYPE = "VenueType";
  @SerializedName(SERIALIZED_NAME_VENUE_TYPE)
  private String venueType;

  public static final String SERIALIZED_NAME_WEEK = "Week";
  @SerializedName(SERIALIZED_NAME_WEEK)
  private Integer week;

  public static final String SERIALIZED_NAME_WINNER = "Winner";
  @SerializedName(SERIALIZED_NAME_WINNER)
  private String winner;

  public Game() {
  }

  public Game bestOf(String bestOf) {
    this.bestOf = bestOf;
    return this;
  }

  /**
   * Get bestOf
   * @return bestOf
   */
  @javax.annotation.Nullable
  public String getBestOf() {
    return bestOf;
  }

  public void setBestOf(String bestOf) {
    this.bestOf = bestOf;
  }


  public Game dateTime(String dateTime) {
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


  public Game day(String day) {
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


  public Game drawMoneyLine(Integer drawMoneyLine) {
    this.drawMoneyLine = drawMoneyLine;
    return this;
  }

  /**
   * Get drawMoneyLine
   * @return drawMoneyLine
   */
  @javax.annotation.Nullable
  public Integer getDrawMoneyLine() {
    return drawMoneyLine;
  }

  public void setDrawMoneyLine(Integer drawMoneyLine) {
    this.drawMoneyLine = drawMoneyLine;
  }


  public Game gameId(Integer gameId) {
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


  public Game group(String group) {
    this.group = group;
    return this;
  }

  /**
   * Get group
   * @return group
   */
  @javax.annotation.Nullable
  public String getGroup() {
    return group;
  }

  public void setGroup(String group) {
    this.group = group;
  }


  public Game isClosed(Boolean isClosed) {
    this.isClosed = isClosed;
    return this;
  }

  /**
   * Get isClosed
   * @return isClosed
   */
  @javax.annotation.Nullable
  public Boolean getIsClosed() {
    return isClosed;
  }

  public void setIsClosed(Boolean isClosed) {
    this.isClosed = isClosed;
  }


  public Game pointSpread(BigDecimal pointSpread) {
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


  public Game roundId(Integer roundId) {
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


  public Game season(Integer season) {
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


  public Game seasonType(Integer seasonType) {
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


  public Game status(String status) {
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


  public Game teamAId(Integer teamAId) {
    this.teamAId = teamAId;
    return this;
  }

  /**
   * Get teamAId
   * @return teamAId
   */
  @javax.annotation.Nullable
  public Integer getTeamAId() {
    return teamAId;
  }

  public void setTeamAId(Integer teamAId) {
    this.teamAId = teamAId;
  }


  public Game teamAKey(String teamAKey) {
    this.teamAKey = teamAKey;
    return this;
  }

  /**
   * Get teamAKey
   * @return teamAKey
   */
  @javax.annotation.Nullable
  public String getTeamAKey() {
    return teamAKey;
  }

  public void setTeamAKey(String teamAKey) {
    this.teamAKey = teamAKey;
  }


  public Game teamAMoneyLine(Integer teamAMoneyLine) {
    this.teamAMoneyLine = teamAMoneyLine;
    return this;
  }

  /**
   * Get teamAMoneyLine
   * @return teamAMoneyLine
   */
  @javax.annotation.Nullable
  public Integer getTeamAMoneyLine() {
    return teamAMoneyLine;
  }

  public void setTeamAMoneyLine(Integer teamAMoneyLine) {
    this.teamAMoneyLine = teamAMoneyLine;
  }


  public Game teamAName(String teamAName) {
    this.teamAName = teamAName;
    return this;
  }

  /**
   * Get teamAName
   * @return teamAName
   */
  @javax.annotation.Nullable
  public String getTeamAName() {
    return teamAName;
  }

  public void setTeamAName(String teamAName) {
    this.teamAName = teamAName;
  }


  public Game teamAPointSpreadPayout(Integer teamAPointSpreadPayout) {
    this.teamAPointSpreadPayout = teamAPointSpreadPayout;
    return this;
  }

  /**
   * Get teamAPointSpreadPayout
   * @return teamAPointSpreadPayout
   */
  @javax.annotation.Nullable
  public Integer getTeamAPointSpreadPayout() {
    return teamAPointSpreadPayout;
  }

  public void setTeamAPointSpreadPayout(Integer teamAPointSpreadPayout) {
    this.teamAPointSpreadPayout = teamAPointSpreadPayout;
  }


  public Game teamAScore(Integer teamAScore) {
    this.teamAScore = teamAScore;
    return this;
  }

  /**
   * Get teamAScore
   * @return teamAScore
   */
  @javax.annotation.Nullable
  public Integer getTeamAScore() {
    return teamAScore;
  }

  public void setTeamAScore(Integer teamAScore) {
    this.teamAScore = teamAScore;
  }


  public Game teamBId(Integer teamBId) {
    this.teamBId = teamBId;
    return this;
  }

  /**
   * Get teamBId
   * @return teamBId
   */
  @javax.annotation.Nullable
  public Integer getTeamBId() {
    return teamBId;
  }

  public void setTeamBId(Integer teamBId) {
    this.teamBId = teamBId;
  }


  public Game teamBKey(String teamBKey) {
    this.teamBKey = teamBKey;
    return this;
  }

  /**
   * Get teamBKey
   * @return teamBKey
   */
  @javax.annotation.Nullable
  public String getTeamBKey() {
    return teamBKey;
  }

  public void setTeamBKey(String teamBKey) {
    this.teamBKey = teamBKey;
  }


  public Game teamBMoneyLine(Integer teamBMoneyLine) {
    this.teamBMoneyLine = teamBMoneyLine;
    return this;
  }

  /**
   * Get teamBMoneyLine
   * @return teamBMoneyLine
   */
  @javax.annotation.Nullable
  public Integer getTeamBMoneyLine() {
    return teamBMoneyLine;
  }

  public void setTeamBMoneyLine(Integer teamBMoneyLine) {
    this.teamBMoneyLine = teamBMoneyLine;
  }


  public Game teamBName(String teamBName) {
    this.teamBName = teamBName;
    return this;
  }

  /**
   * Get teamBName
   * @return teamBName
   */
  @javax.annotation.Nullable
  public String getTeamBName() {
    return teamBName;
  }

  public void setTeamBName(String teamBName) {
    this.teamBName = teamBName;
  }


  public Game teamBPointSpreadPayout(Integer teamBPointSpreadPayout) {
    this.teamBPointSpreadPayout = teamBPointSpreadPayout;
    return this;
  }

  /**
   * Get teamBPointSpreadPayout
   * @return teamBPointSpreadPayout
   */
  @javax.annotation.Nullable
  public Integer getTeamBPointSpreadPayout() {
    return teamBPointSpreadPayout;
  }

  public void setTeamBPointSpreadPayout(Integer teamBPointSpreadPayout) {
    this.teamBPointSpreadPayout = teamBPointSpreadPayout;
  }


  public Game teamBScore(Integer teamBScore) {
    this.teamBScore = teamBScore;
    return this;
  }

  /**
   * Get teamBScore
   * @return teamBScore
   */
  @javax.annotation.Nullable
  public Integer getTeamBScore() {
    return teamBScore;
  }

  public void setTeamBScore(Integer teamBScore) {
    this.teamBScore = teamBScore;
  }


  public Game updated(String updated) {
    this.updated = updated;
    return this;
  }

  /**
   * Get updated
   * @return updated
   */
  @javax.annotation.Nullable
  public String getUpdated() {
    return updated;
  }

  public void setUpdated(String updated) {
    this.updated = updated;
  }


  public Game updatedUtc(String updatedUtc) {
    this.updatedUtc = updatedUtc;
    return this;
  }

  /**
   * Get updatedUtc
   * @return updatedUtc
   */
  @javax.annotation.Nullable
  public String getUpdatedUtc() {
    return updatedUtc;
  }

  public void setUpdatedUtc(String updatedUtc) {
    this.updatedUtc = updatedUtc;
  }


  public Game venueId(Integer venueId) {
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


  public Game venueType(String venueType) {
    this.venueType = venueType;
    return this;
  }

  /**
   * Get venueType
   * @return venueType
   */
  @javax.annotation.Nullable
  public String getVenueType() {
    return venueType;
  }

  public void setVenueType(String venueType) {
    this.venueType = venueType;
  }


  public Game week(Integer week) {
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


  public Game winner(String winner) {
    this.winner = winner;
    return this;
  }

  /**
   * Get winner
   * @return winner
   */
  @javax.annotation.Nullable
  public String getWinner() {
    return winner;
  }

  public void setWinner(String winner) {
    this.winner = winner;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Game game = (Game) o;
    return Objects.equals(this.bestOf, game.bestOf) &&
        Objects.equals(this.dateTime, game.dateTime) &&
        Objects.equals(this.day, game.day) &&
        Objects.equals(this.drawMoneyLine, game.drawMoneyLine) &&
        Objects.equals(this.gameId, game.gameId) &&
        Objects.equals(this.group, game.group) &&
        Objects.equals(this.isClosed, game.isClosed) &&
        Objects.equals(this.pointSpread, game.pointSpread) &&
        Objects.equals(this.roundId, game.roundId) &&
        Objects.equals(this.season, game.season) &&
        Objects.equals(this.seasonType, game.seasonType) &&
        Objects.equals(this.status, game.status) &&
        Objects.equals(this.teamAId, game.teamAId) &&
        Objects.equals(this.teamAKey, game.teamAKey) &&
        Objects.equals(this.teamAMoneyLine, game.teamAMoneyLine) &&
        Objects.equals(this.teamAName, game.teamAName) &&
        Objects.equals(this.teamAPointSpreadPayout, game.teamAPointSpreadPayout) &&
        Objects.equals(this.teamAScore, game.teamAScore) &&
        Objects.equals(this.teamBId, game.teamBId) &&
        Objects.equals(this.teamBKey, game.teamBKey) &&
        Objects.equals(this.teamBMoneyLine, game.teamBMoneyLine) &&
        Objects.equals(this.teamBName, game.teamBName) &&
        Objects.equals(this.teamBPointSpreadPayout, game.teamBPointSpreadPayout) &&
        Objects.equals(this.teamBScore, game.teamBScore) &&
        Objects.equals(this.updated, game.updated) &&
        Objects.equals(this.updatedUtc, game.updatedUtc) &&
        Objects.equals(this.venueId, game.venueId) &&
        Objects.equals(this.venueType, game.venueType) &&
        Objects.equals(this.week, game.week) &&
        Objects.equals(this.winner, game.winner);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(bestOf, dateTime, day, drawMoneyLine, gameId, group, isClosed, pointSpread, roundId, season, seasonType, status, teamAId, teamAKey, teamAMoneyLine, teamAName, teamAPointSpreadPayout, teamAScore, teamBId, teamBKey, teamBMoneyLine, teamBName, teamBPointSpreadPayout, teamBScore, updated, updatedUtc, venueId, venueType, week, winner);
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
    sb.append("class Game {\n");
    sb.append("    bestOf: ").append(toIndentedString(bestOf)).append("\n");
    sb.append("    dateTime: ").append(toIndentedString(dateTime)).append("\n");
    sb.append("    day: ").append(toIndentedString(day)).append("\n");
    sb.append("    drawMoneyLine: ").append(toIndentedString(drawMoneyLine)).append("\n");
    sb.append("    gameId: ").append(toIndentedString(gameId)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    isClosed: ").append(toIndentedString(isClosed)).append("\n");
    sb.append("    pointSpread: ").append(toIndentedString(pointSpread)).append("\n");
    sb.append("    roundId: ").append(toIndentedString(roundId)).append("\n");
    sb.append("    season: ").append(toIndentedString(season)).append("\n");
    sb.append("    seasonType: ").append(toIndentedString(seasonType)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    teamAId: ").append(toIndentedString(teamAId)).append("\n");
    sb.append("    teamAKey: ").append(toIndentedString(teamAKey)).append("\n");
    sb.append("    teamAMoneyLine: ").append(toIndentedString(teamAMoneyLine)).append("\n");
    sb.append("    teamAName: ").append(toIndentedString(teamAName)).append("\n");
    sb.append("    teamAPointSpreadPayout: ").append(toIndentedString(teamAPointSpreadPayout)).append("\n");
    sb.append("    teamAScore: ").append(toIndentedString(teamAScore)).append("\n");
    sb.append("    teamBId: ").append(toIndentedString(teamBId)).append("\n");
    sb.append("    teamBKey: ").append(toIndentedString(teamBKey)).append("\n");
    sb.append("    teamBMoneyLine: ").append(toIndentedString(teamBMoneyLine)).append("\n");
    sb.append("    teamBName: ").append(toIndentedString(teamBName)).append("\n");
    sb.append("    teamBPointSpreadPayout: ").append(toIndentedString(teamBPointSpreadPayout)).append("\n");
    sb.append("    teamBScore: ").append(toIndentedString(teamBScore)).append("\n");
    sb.append("    updated: ").append(toIndentedString(updated)).append("\n");
    sb.append("    updatedUtc: ").append(toIndentedString(updatedUtc)).append("\n");
    sb.append("    venueId: ").append(toIndentedString(venueId)).append("\n");
    sb.append("    venueType: ").append(toIndentedString(venueType)).append("\n");
    sb.append("    week: ").append(toIndentedString(week)).append("\n");
    sb.append("    winner: ").append(toIndentedString(winner)).append("\n");
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
    openapiFields.add("BestOf");
    openapiFields.add("DateTime");
    openapiFields.add("Day");
    openapiFields.add("DrawMoneyLine");
    openapiFields.add("GameId");
    openapiFields.add("Group");
    openapiFields.add("IsClosed");
    openapiFields.add("PointSpread");
    openapiFields.add("RoundId");
    openapiFields.add("Season");
    openapiFields.add("SeasonType");
    openapiFields.add("Status");
    openapiFields.add("TeamAId");
    openapiFields.add("TeamAKey");
    openapiFields.add("TeamAMoneyLine");
    openapiFields.add("TeamAName");
    openapiFields.add("TeamAPointSpreadPayout");
    openapiFields.add("TeamAScore");
    openapiFields.add("TeamBId");
    openapiFields.add("TeamBKey");
    openapiFields.add("TeamBMoneyLine");
    openapiFields.add("TeamBName");
    openapiFields.add("TeamBPointSpreadPayout");
    openapiFields.add("TeamBScore");
    openapiFields.add("Updated");
    openapiFields.add("UpdatedUtc");
    openapiFields.add("VenueId");
    openapiFields.add("VenueType");
    openapiFields.add("Week");
    openapiFields.add("Winner");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Game
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Game.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Game is not found in the empty JSON string", Game.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Game.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Game` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("BestOf") != null && !jsonObj.get("BestOf").isJsonNull()) && !jsonObj.get("BestOf").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BestOf` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BestOf").toString()));
      }
      if ((jsonObj.get("DateTime") != null && !jsonObj.get("DateTime").isJsonNull()) && !jsonObj.get("DateTime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DateTime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DateTime").toString()));
      }
      if ((jsonObj.get("Day") != null && !jsonObj.get("Day").isJsonNull()) && !jsonObj.get("Day").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Day` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Day").toString()));
      }
      if ((jsonObj.get("Group") != null && !jsonObj.get("Group").isJsonNull()) && !jsonObj.get("Group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Group").toString()));
      }
      if ((jsonObj.get("Status") != null && !jsonObj.get("Status").isJsonNull()) && !jsonObj.get("Status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Status").toString()));
      }
      if ((jsonObj.get("TeamAKey") != null && !jsonObj.get("TeamAKey").isJsonNull()) && !jsonObj.get("TeamAKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TeamAKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TeamAKey").toString()));
      }
      if ((jsonObj.get("TeamAName") != null && !jsonObj.get("TeamAName").isJsonNull()) && !jsonObj.get("TeamAName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TeamAName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TeamAName").toString()));
      }
      if ((jsonObj.get("TeamBKey") != null && !jsonObj.get("TeamBKey").isJsonNull()) && !jsonObj.get("TeamBKey").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TeamBKey` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TeamBKey").toString()));
      }
      if ((jsonObj.get("TeamBName") != null && !jsonObj.get("TeamBName").isJsonNull()) && !jsonObj.get("TeamBName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TeamBName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TeamBName").toString()));
      }
      if ((jsonObj.get("Updated") != null && !jsonObj.get("Updated").isJsonNull()) && !jsonObj.get("Updated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Updated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Updated").toString()));
      }
      if ((jsonObj.get("UpdatedUtc") != null && !jsonObj.get("UpdatedUtc").isJsonNull()) && !jsonObj.get("UpdatedUtc").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `UpdatedUtc` to be a primitive type in the JSON string but got `%s`", jsonObj.get("UpdatedUtc").toString()));
      }
      if ((jsonObj.get("VenueType") != null && !jsonObj.get("VenueType").isJsonNull()) && !jsonObj.get("VenueType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `VenueType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("VenueType").toString()));
      }
      if ((jsonObj.get("Winner") != null && !jsonObj.get("Winner").isJsonNull()) && !jsonObj.get("Winner").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Winner` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Winner").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Game.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Game' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Game> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Game.class));

       return (TypeAdapter<T>) new TypeAdapter<Game>() {
           @Override
           public void write(JsonWriter out, Game value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Game read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Game given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Game
   * @throws IOException if the JSON string is invalid with respect to Game
   */
  public static Game fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Game.class);
  }

  /**
   * Convert an instance of Game to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

