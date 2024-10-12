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
 * PlayerOwnership
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:11.789534-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PlayerOwnership {
  public static final String SERIALIZED_NAME_DELTA_OWNERSHIP_PERCENTAGE = "DeltaOwnershipPercentage";
  @SerializedName(SERIALIZED_NAME_DELTA_OWNERSHIP_PERCENTAGE)
  private BigDecimal deltaOwnershipPercentage;

  public static final String SERIALIZED_NAME_DELTA_START_PERCENTAGE = "DeltaStartPercentage";
  @SerializedName(SERIALIZED_NAME_DELTA_START_PERCENTAGE)
  private BigDecimal deltaStartPercentage;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OWNERSHIP_PERCENTAGE = "OwnershipPercentage";
  @SerializedName(SERIALIZED_NAME_OWNERSHIP_PERCENTAGE)
  private BigDecimal ownershipPercentage;

  public static final String SERIALIZED_NAME_PLAYER_I_D = "PlayerID";
  @SerializedName(SERIALIZED_NAME_PLAYER_I_D)
  private Integer playerID;

  public static final String SERIALIZED_NAME_POSITION = "Position";
  @SerializedName(SERIALIZED_NAME_POSITION)
  private String position;

  public static final String SERIALIZED_NAME_SEASON = "Season";
  @SerializedName(SERIALIZED_NAME_SEASON)
  private Integer season;

  public static final String SERIALIZED_NAME_SEASON_TYPE = "SeasonType";
  @SerializedName(SERIALIZED_NAME_SEASON_TYPE)
  private Integer seasonType;

  public static final String SERIALIZED_NAME_START_PERCENTAGE = "StartPercentage";
  @SerializedName(SERIALIZED_NAME_START_PERCENTAGE)
  private BigDecimal startPercentage;

  public static final String SERIALIZED_NAME_TEAM = "Team";
  @SerializedName(SERIALIZED_NAME_TEAM)
  private String team;

  public static final String SERIALIZED_NAME_TEAM_I_D = "TeamID";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D)
  private Integer teamID;

  public static final String SERIALIZED_NAME_WEEK = "Week";
  @SerializedName(SERIALIZED_NAME_WEEK)
  private Integer week;

  public PlayerOwnership() {
  }

  public PlayerOwnership deltaOwnershipPercentage(BigDecimal deltaOwnershipPercentage) {
    this.deltaOwnershipPercentage = deltaOwnershipPercentage;
    return this;
  }

  /**
   * Get deltaOwnershipPercentage
   * @return deltaOwnershipPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getDeltaOwnershipPercentage() {
    return deltaOwnershipPercentage;
  }

  public void setDeltaOwnershipPercentage(BigDecimal deltaOwnershipPercentage) {
    this.deltaOwnershipPercentage = deltaOwnershipPercentage;
  }


  public PlayerOwnership deltaStartPercentage(BigDecimal deltaStartPercentage) {
    this.deltaStartPercentage = deltaStartPercentage;
    return this;
  }

  /**
   * Get deltaStartPercentage
   * @return deltaStartPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getDeltaStartPercentage() {
    return deltaStartPercentage;
  }

  public void setDeltaStartPercentage(BigDecimal deltaStartPercentage) {
    this.deltaStartPercentage = deltaStartPercentage;
  }


  public PlayerOwnership name(String name) {
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


  public PlayerOwnership ownershipPercentage(BigDecimal ownershipPercentage) {
    this.ownershipPercentage = ownershipPercentage;
    return this;
  }

  /**
   * Get ownershipPercentage
   * @return ownershipPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getOwnershipPercentage() {
    return ownershipPercentage;
  }

  public void setOwnershipPercentage(BigDecimal ownershipPercentage) {
    this.ownershipPercentage = ownershipPercentage;
  }


  public PlayerOwnership playerID(Integer playerID) {
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


  public PlayerOwnership position(String position) {
    this.position = position;
    return this;
  }

  /**
   * Get position
   * @return position
   */
  @javax.annotation.Nullable
  public String getPosition() {
    return position;
  }

  public void setPosition(String position) {
    this.position = position;
  }


  public PlayerOwnership season(Integer season) {
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


  public PlayerOwnership seasonType(Integer seasonType) {
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


  public PlayerOwnership startPercentage(BigDecimal startPercentage) {
    this.startPercentage = startPercentage;
    return this;
  }

  /**
   * Get startPercentage
   * @return startPercentage
   */
  @javax.annotation.Nullable
  public BigDecimal getStartPercentage() {
    return startPercentage;
  }

  public void setStartPercentage(BigDecimal startPercentage) {
    this.startPercentage = startPercentage;
  }


  public PlayerOwnership team(String team) {
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


  public PlayerOwnership teamID(Integer teamID) {
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


  public PlayerOwnership week(Integer week) {
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
    PlayerOwnership playerOwnership = (PlayerOwnership) o;
    return Objects.equals(this.deltaOwnershipPercentage, playerOwnership.deltaOwnershipPercentage) &&
        Objects.equals(this.deltaStartPercentage, playerOwnership.deltaStartPercentage) &&
        Objects.equals(this.name, playerOwnership.name) &&
        Objects.equals(this.ownershipPercentage, playerOwnership.ownershipPercentage) &&
        Objects.equals(this.playerID, playerOwnership.playerID) &&
        Objects.equals(this.position, playerOwnership.position) &&
        Objects.equals(this.season, playerOwnership.season) &&
        Objects.equals(this.seasonType, playerOwnership.seasonType) &&
        Objects.equals(this.startPercentage, playerOwnership.startPercentage) &&
        Objects.equals(this.team, playerOwnership.team) &&
        Objects.equals(this.teamID, playerOwnership.teamID) &&
        Objects.equals(this.week, playerOwnership.week);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(deltaOwnershipPercentage, deltaStartPercentage, name, ownershipPercentage, playerID, position, season, seasonType, startPercentage, team, teamID, week);
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
    sb.append("class PlayerOwnership {\n");
    sb.append("    deltaOwnershipPercentage: ").append(toIndentedString(deltaOwnershipPercentage)).append("\n");
    sb.append("    deltaStartPercentage: ").append(toIndentedString(deltaStartPercentage)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ownershipPercentage: ").append(toIndentedString(ownershipPercentage)).append("\n");
    sb.append("    playerID: ").append(toIndentedString(playerID)).append("\n");
    sb.append("    position: ").append(toIndentedString(position)).append("\n");
    sb.append("    season: ").append(toIndentedString(season)).append("\n");
    sb.append("    seasonType: ").append(toIndentedString(seasonType)).append("\n");
    sb.append("    startPercentage: ").append(toIndentedString(startPercentage)).append("\n");
    sb.append("    team: ").append(toIndentedString(team)).append("\n");
    sb.append("    teamID: ").append(toIndentedString(teamID)).append("\n");
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
    openapiFields.add("DeltaOwnershipPercentage");
    openapiFields.add("DeltaStartPercentage");
    openapiFields.add("Name");
    openapiFields.add("OwnershipPercentage");
    openapiFields.add("PlayerID");
    openapiFields.add("Position");
    openapiFields.add("Season");
    openapiFields.add("SeasonType");
    openapiFields.add("StartPercentage");
    openapiFields.add("Team");
    openapiFields.add("TeamID");
    openapiFields.add("Week");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PlayerOwnership
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PlayerOwnership.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PlayerOwnership is not found in the empty JSON string", PlayerOwnership.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PlayerOwnership.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PlayerOwnership` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Position") != null && !jsonObj.get("Position").isJsonNull()) && !jsonObj.get("Position").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Position` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Position").toString()));
      }
      if ((jsonObj.get("Team") != null && !jsonObj.get("Team").isJsonNull()) && !jsonObj.get("Team").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Team` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Team").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PlayerOwnership.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PlayerOwnership' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PlayerOwnership> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PlayerOwnership.class));

       return (TypeAdapter<T>) new TypeAdapter<PlayerOwnership>() {
           @Override
           public void write(JsonWriter out, PlayerOwnership value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PlayerOwnership read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PlayerOwnership given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PlayerOwnership
   * @throws IOException if the JSON string is invalid with respect to PlayerOwnership
   */
  public static PlayerOwnership fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PlayerOwnership.class);
  }

  /**
   * Convert an instance of PlayerOwnership to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

