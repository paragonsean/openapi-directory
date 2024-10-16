/*
 * NHL v3 Play-by-Play
 * NHL play-by-play API.
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
 * Play
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:33.746200-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Play {
  public static final String SERIALIZED_NAME_AWAY_TEAM_SCORE = "AwayTeamScore";
  @SerializedName(SERIALIZED_NAME_AWAY_TEAM_SCORE)
  private Integer awayTeamScore;

  public static final String SERIALIZED_NAME_CATEGORY = "Category";
  @SerializedName(SERIALIZED_NAME_CATEGORY)
  private String category;

  public static final String SERIALIZED_NAME_CLOCK_MINUTES = "ClockMinutes";
  @SerializedName(SERIALIZED_NAME_CLOCK_MINUTES)
  private Integer clockMinutes;

  public static final String SERIALIZED_NAME_CLOCK_SECONDS = "ClockSeconds";
  @SerializedName(SERIALIZED_NAME_CLOCK_SECONDS)
  private Integer clockSeconds;

  public static final String SERIALIZED_NAME_CREATED = "Created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FIRST_ASSISTED_BY_PLAYER_I_D = "FirstAssistedByPlayerID";
  @SerializedName(SERIALIZED_NAME_FIRST_ASSISTED_BY_PLAYER_I_D)
  private Integer firstAssistedByPlayerID;

  public static final String SERIALIZED_NAME_HOME_TEAM_SCORE = "HomeTeamScore";
  @SerializedName(SERIALIZED_NAME_HOME_TEAM_SCORE)
  private Integer homeTeamScore;

  public static final String SERIALIZED_NAME_OPPONENT = "Opponent";
  @SerializedName(SERIALIZED_NAME_OPPONENT)
  private String opponent;

  public static final String SERIALIZED_NAME_OPPONENT_I_D = "OpponentID";
  @SerializedName(SERIALIZED_NAME_OPPONENT_I_D)
  private Integer opponentID;

  public static final String SERIALIZED_NAME_OPPOSING_PLAYER_I_D = "OpposingPlayerID";
  @SerializedName(SERIALIZED_NAME_OPPOSING_PLAYER_I_D)
  private Integer opposingPlayerID;

  public static final String SERIALIZED_NAME_PERIOD_I_D = "PeriodID";
  @SerializedName(SERIALIZED_NAME_PERIOD_I_D)
  private Integer periodID;

  public static final String SERIALIZED_NAME_PERIOD_NAME = "PeriodName";
  @SerializedName(SERIALIZED_NAME_PERIOD_NAME)
  private String periodName;

  public static final String SERIALIZED_NAME_PLAY_I_D = "PlayID";
  @SerializedName(SERIALIZED_NAME_PLAY_I_D)
  private Integer playID;

  public static final String SERIALIZED_NAME_PLAYER_I_D = "PlayerID";
  @SerializedName(SERIALIZED_NAME_PLAYER_I_D)
  private Integer playerID;

  public static final String SERIALIZED_NAME_POWER_PLAY_TEAM = "PowerPlayTeam";
  @SerializedName(SERIALIZED_NAME_POWER_PLAY_TEAM)
  private String powerPlayTeam;

  public static final String SERIALIZED_NAME_POWER_PLAY_TEAM_I_D = "PowerPlayTeamID";
  @SerializedName(SERIALIZED_NAME_POWER_PLAY_TEAM_I_D)
  private Integer powerPlayTeamID;

  public static final String SERIALIZED_NAME_SECOND_ASSISTED_BY_PLAYER_I_D = "SecondAssistedByPlayerID";
  @SerializedName(SERIALIZED_NAME_SECOND_ASSISTED_BY_PLAYER_I_D)
  private Integer secondAssistedByPlayerID;

  public static final String SERIALIZED_NAME_SEQUENCE = "Sequence";
  @SerializedName(SERIALIZED_NAME_SEQUENCE)
  private Integer sequence;

  public static final String SERIALIZED_NAME_TEAM = "Team";
  @SerializedName(SERIALIZED_NAME_TEAM)
  private String team;

  public static final String SERIALIZED_NAME_TEAM_I_D = "TeamID";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D)
  private Integer teamID;

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_UPDATED = "Updated";
  @SerializedName(SERIALIZED_NAME_UPDATED)
  private String updated;

  public Play() {
  }

  public Play awayTeamScore(Integer awayTeamScore) {
    this.awayTeamScore = awayTeamScore;
    return this;
  }

  /**
   * Get awayTeamScore
   * @return awayTeamScore
   */
  @javax.annotation.Nullable
  public Integer getAwayTeamScore() {
    return awayTeamScore;
  }

  public void setAwayTeamScore(Integer awayTeamScore) {
    this.awayTeamScore = awayTeamScore;
  }


  public Play category(String category) {
    this.category = category;
    return this;
  }

  /**
   * Get category
   * @return category
   */
  @javax.annotation.Nullable
  public String getCategory() {
    return category;
  }

  public void setCategory(String category) {
    this.category = category;
  }


  public Play clockMinutes(Integer clockMinutes) {
    this.clockMinutes = clockMinutes;
    return this;
  }

  /**
   * Get clockMinutes
   * @return clockMinutes
   */
  @javax.annotation.Nullable
  public Integer getClockMinutes() {
    return clockMinutes;
  }

  public void setClockMinutes(Integer clockMinutes) {
    this.clockMinutes = clockMinutes;
  }


  public Play clockSeconds(Integer clockSeconds) {
    this.clockSeconds = clockSeconds;
    return this;
  }

  /**
   * Get clockSeconds
   * @return clockSeconds
   */
  @javax.annotation.Nullable
  public Integer getClockSeconds() {
    return clockSeconds;
  }

  public void setClockSeconds(Integer clockSeconds) {
    this.clockSeconds = clockSeconds;
  }


  public Play created(String created) {
    this.created = created;
    return this;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }

  public void setCreated(String created) {
    this.created = created;
  }


  public Play description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Play firstAssistedByPlayerID(Integer firstAssistedByPlayerID) {
    this.firstAssistedByPlayerID = firstAssistedByPlayerID;
    return this;
  }

  /**
   * Get firstAssistedByPlayerID
   * @return firstAssistedByPlayerID
   */
  @javax.annotation.Nullable
  public Integer getFirstAssistedByPlayerID() {
    return firstAssistedByPlayerID;
  }

  public void setFirstAssistedByPlayerID(Integer firstAssistedByPlayerID) {
    this.firstAssistedByPlayerID = firstAssistedByPlayerID;
  }


  public Play homeTeamScore(Integer homeTeamScore) {
    this.homeTeamScore = homeTeamScore;
    return this;
  }

  /**
   * Get homeTeamScore
   * @return homeTeamScore
   */
  @javax.annotation.Nullable
  public Integer getHomeTeamScore() {
    return homeTeamScore;
  }

  public void setHomeTeamScore(Integer homeTeamScore) {
    this.homeTeamScore = homeTeamScore;
  }


  public Play opponent(String opponent) {
    this.opponent = opponent;
    return this;
  }

  /**
   * Get opponent
   * @return opponent
   */
  @javax.annotation.Nullable
  public String getOpponent() {
    return opponent;
  }

  public void setOpponent(String opponent) {
    this.opponent = opponent;
  }


  public Play opponentID(Integer opponentID) {
    this.opponentID = opponentID;
    return this;
  }

  /**
   * Get opponentID
   * @return opponentID
   */
  @javax.annotation.Nullable
  public Integer getOpponentID() {
    return opponentID;
  }

  public void setOpponentID(Integer opponentID) {
    this.opponentID = opponentID;
  }


  public Play opposingPlayerID(Integer opposingPlayerID) {
    this.opposingPlayerID = opposingPlayerID;
    return this;
  }

  /**
   * Get opposingPlayerID
   * @return opposingPlayerID
   */
  @javax.annotation.Nullable
  public Integer getOpposingPlayerID() {
    return opposingPlayerID;
  }

  public void setOpposingPlayerID(Integer opposingPlayerID) {
    this.opposingPlayerID = opposingPlayerID;
  }


  public Play periodID(Integer periodID) {
    this.periodID = periodID;
    return this;
  }

  /**
   * Get periodID
   * @return periodID
   */
  @javax.annotation.Nullable
  public Integer getPeriodID() {
    return periodID;
  }

  public void setPeriodID(Integer periodID) {
    this.periodID = periodID;
  }


  public Play periodName(String periodName) {
    this.periodName = periodName;
    return this;
  }

  /**
   * Get periodName
   * @return periodName
   */
  @javax.annotation.Nullable
  public String getPeriodName() {
    return periodName;
  }

  public void setPeriodName(String periodName) {
    this.periodName = periodName;
  }


  public Play playID(Integer playID) {
    this.playID = playID;
    return this;
  }

  /**
   * Get playID
   * @return playID
   */
  @javax.annotation.Nullable
  public Integer getPlayID() {
    return playID;
  }

  public void setPlayID(Integer playID) {
    this.playID = playID;
  }


  public Play playerID(Integer playerID) {
    this.playerID = playerID;
    return this;
  }

  /**
   * Get playerID
   * @return playerID
   */
  @javax.annotation.Nullable
  public Integer getPlayerID() {
    return playerID;
  }

  public void setPlayerID(Integer playerID) {
    this.playerID = playerID;
  }


  public Play powerPlayTeam(String powerPlayTeam) {
    this.powerPlayTeam = powerPlayTeam;
    return this;
  }

  /**
   * Get powerPlayTeam
   * @return powerPlayTeam
   */
  @javax.annotation.Nullable
  public String getPowerPlayTeam() {
    return powerPlayTeam;
  }

  public void setPowerPlayTeam(String powerPlayTeam) {
    this.powerPlayTeam = powerPlayTeam;
  }


  public Play powerPlayTeamID(Integer powerPlayTeamID) {
    this.powerPlayTeamID = powerPlayTeamID;
    return this;
  }

  /**
   * Get powerPlayTeamID
   * @return powerPlayTeamID
   */
  @javax.annotation.Nullable
  public Integer getPowerPlayTeamID() {
    return powerPlayTeamID;
  }

  public void setPowerPlayTeamID(Integer powerPlayTeamID) {
    this.powerPlayTeamID = powerPlayTeamID;
  }


  public Play secondAssistedByPlayerID(Integer secondAssistedByPlayerID) {
    this.secondAssistedByPlayerID = secondAssistedByPlayerID;
    return this;
  }

  /**
   * Get secondAssistedByPlayerID
   * @return secondAssistedByPlayerID
   */
  @javax.annotation.Nullable
  public Integer getSecondAssistedByPlayerID() {
    return secondAssistedByPlayerID;
  }

  public void setSecondAssistedByPlayerID(Integer secondAssistedByPlayerID) {
    this.secondAssistedByPlayerID = secondAssistedByPlayerID;
  }


  public Play sequence(Integer sequence) {
    this.sequence = sequence;
    return this;
  }

  /**
   * Get sequence
   * @return sequence
   */
  @javax.annotation.Nullable
  public Integer getSequence() {
    return sequence;
  }

  public void setSequence(Integer sequence) {
    this.sequence = sequence;
  }


  public Play team(String team) {
    this.team = team;
    return this;
  }

  /**
   * Get team
   * @return team
   */
  @javax.annotation.Nullable
  public String getTeam() {
    return team;
  }

  public void setTeam(String team) {
    this.team = team;
  }


  public Play teamID(Integer teamID) {
    this.teamID = teamID;
    return this;
  }

  /**
   * Get teamID
   * @return teamID
   */
  @javax.annotation.Nullable
  public Integer getTeamID() {
    return teamID;
  }

  public void setTeamID(Integer teamID) {
    this.teamID = teamID;
  }


  public Play type(String type) {
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


  public Play updated(String updated) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Play play = (Play) o;
    return Objects.equals(this.awayTeamScore, play.awayTeamScore) &&
        Objects.equals(this.category, play.category) &&
        Objects.equals(this.clockMinutes, play.clockMinutes) &&
        Objects.equals(this.clockSeconds, play.clockSeconds) &&
        Objects.equals(this.created, play.created) &&
        Objects.equals(this.description, play.description) &&
        Objects.equals(this.firstAssistedByPlayerID, play.firstAssistedByPlayerID) &&
        Objects.equals(this.homeTeamScore, play.homeTeamScore) &&
        Objects.equals(this.opponent, play.opponent) &&
        Objects.equals(this.opponentID, play.opponentID) &&
        Objects.equals(this.opposingPlayerID, play.opposingPlayerID) &&
        Objects.equals(this.periodID, play.periodID) &&
        Objects.equals(this.periodName, play.periodName) &&
        Objects.equals(this.playID, play.playID) &&
        Objects.equals(this.playerID, play.playerID) &&
        Objects.equals(this.powerPlayTeam, play.powerPlayTeam) &&
        Objects.equals(this.powerPlayTeamID, play.powerPlayTeamID) &&
        Objects.equals(this.secondAssistedByPlayerID, play.secondAssistedByPlayerID) &&
        Objects.equals(this.sequence, play.sequence) &&
        Objects.equals(this.team, play.team) &&
        Objects.equals(this.teamID, play.teamID) &&
        Objects.equals(this.type, play.type) &&
        Objects.equals(this.updated, play.updated);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(awayTeamScore, category, clockMinutes, clockSeconds, created, description, firstAssistedByPlayerID, homeTeamScore, opponent, opponentID, opposingPlayerID, periodID, periodName, playID, playerID, powerPlayTeam, powerPlayTeamID, secondAssistedByPlayerID, sequence, team, teamID, type, updated);
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
    sb.append("class Play {\n");
    sb.append("    awayTeamScore: ").append(toIndentedString(awayTeamScore)).append("\n");
    sb.append("    category: ").append(toIndentedString(category)).append("\n");
    sb.append("    clockMinutes: ").append(toIndentedString(clockMinutes)).append("\n");
    sb.append("    clockSeconds: ").append(toIndentedString(clockSeconds)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    firstAssistedByPlayerID: ").append(toIndentedString(firstAssistedByPlayerID)).append("\n");
    sb.append("    homeTeamScore: ").append(toIndentedString(homeTeamScore)).append("\n");
    sb.append("    opponent: ").append(toIndentedString(opponent)).append("\n");
    sb.append("    opponentID: ").append(toIndentedString(opponentID)).append("\n");
    sb.append("    opposingPlayerID: ").append(toIndentedString(opposingPlayerID)).append("\n");
    sb.append("    periodID: ").append(toIndentedString(periodID)).append("\n");
    sb.append("    periodName: ").append(toIndentedString(periodName)).append("\n");
    sb.append("    playID: ").append(toIndentedString(playID)).append("\n");
    sb.append("    playerID: ").append(toIndentedString(playerID)).append("\n");
    sb.append("    powerPlayTeam: ").append(toIndentedString(powerPlayTeam)).append("\n");
    sb.append("    powerPlayTeamID: ").append(toIndentedString(powerPlayTeamID)).append("\n");
    sb.append("    secondAssistedByPlayerID: ").append(toIndentedString(secondAssistedByPlayerID)).append("\n");
    sb.append("    sequence: ").append(toIndentedString(sequence)).append("\n");
    sb.append("    team: ").append(toIndentedString(team)).append("\n");
    sb.append("    teamID: ").append(toIndentedString(teamID)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updated: ").append(toIndentedString(updated)).append("\n");
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
    openapiFields.add("AwayTeamScore");
    openapiFields.add("Category");
    openapiFields.add("ClockMinutes");
    openapiFields.add("ClockSeconds");
    openapiFields.add("Created");
    openapiFields.add("Description");
    openapiFields.add("FirstAssistedByPlayerID");
    openapiFields.add("HomeTeamScore");
    openapiFields.add("Opponent");
    openapiFields.add("OpponentID");
    openapiFields.add("OpposingPlayerID");
    openapiFields.add("PeriodID");
    openapiFields.add("PeriodName");
    openapiFields.add("PlayID");
    openapiFields.add("PlayerID");
    openapiFields.add("PowerPlayTeam");
    openapiFields.add("PowerPlayTeamID");
    openapiFields.add("SecondAssistedByPlayerID");
    openapiFields.add("Sequence");
    openapiFields.add("Team");
    openapiFields.add("TeamID");
    openapiFields.add("Type");
    openapiFields.add("Updated");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Play
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Play.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Play is not found in the empty JSON string", Play.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Play.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Play` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Category") != null && !jsonObj.get("Category").isJsonNull()) && !jsonObj.get("Category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Category").toString()));
      }
      if ((jsonObj.get("Created") != null && !jsonObj.get("Created").isJsonNull()) && !jsonObj.get("Created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Created").toString()));
      }
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if ((jsonObj.get("Opponent") != null && !jsonObj.get("Opponent").isJsonNull()) && !jsonObj.get("Opponent").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Opponent` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Opponent").toString()));
      }
      if ((jsonObj.get("PeriodName") != null && !jsonObj.get("PeriodName").isJsonNull()) && !jsonObj.get("PeriodName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PeriodName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PeriodName").toString()));
      }
      if ((jsonObj.get("PowerPlayTeam") != null && !jsonObj.get("PowerPlayTeam").isJsonNull()) && !jsonObj.get("PowerPlayTeam").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PowerPlayTeam` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PowerPlayTeam").toString()));
      }
      if ((jsonObj.get("Team") != null && !jsonObj.get("Team").isJsonNull()) && !jsonObj.get("Team").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Team` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Team").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
      if ((jsonObj.get("Updated") != null && !jsonObj.get("Updated").isJsonNull()) && !jsonObj.get("Updated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Updated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Updated").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Play.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Play' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Play> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Play.class));

       return (TypeAdapter<T>) new TypeAdapter<Play>() {
           @Override
           public void write(JsonWriter out, Play value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Play read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Play given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Play
   * @throws IOException if the JSON string is invalid with respect to Play
   */
  public static Play fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Play.class);
  }

  /**
   * Convert an instance of Play to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

