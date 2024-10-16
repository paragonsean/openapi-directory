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
 * TeamBasic
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:21.929041-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TeamBasic {
  public static final String SERIALIZED_NAME_BYE_WEEK = "ByeWeek";
  @SerializedName(SERIALIZED_NAME_BYE_WEEK)
  private Integer byeWeek;

  public static final String SERIALIZED_NAME_CITY = "City";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_CONFERENCE = "Conference";
  @SerializedName(SERIALIZED_NAME_CONFERENCE)
  private String conference;

  public static final String SERIALIZED_NAME_DEFENSIVE_COORDINATOR = "DefensiveCoordinator";
  @SerializedName(SERIALIZED_NAME_DEFENSIVE_COORDINATOR)
  private String defensiveCoordinator;

  public static final String SERIALIZED_NAME_DEFENSIVE_SCHEME = "DefensiveScheme";
  @SerializedName(SERIALIZED_NAME_DEFENSIVE_SCHEME)
  private String defensiveScheme;

  public static final String SERIALIZED_NAME_DIVISION = "Division";
  @SerializedName(SERIALIZED_NAME_DIVISION)
  private String division;

  public static final String SERIALIZED_NAME_FULL_NAME = "FullName";
  @SerializedName(SERIALIZED_NAME_FULL_NAME)
  private String fullName;

  public static final String SERIALIZED_NAME_GLOBAL_TEAM_I_D = "GlobalTeamID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_TEAM_I_D)
  private Integer globalTeamID;

  public static final String SERIALIZED_NAME_HEAD_COACH = "HeadCoach";
  @SerializedName(SERIALIZED_NAME_HEAD_COACH)
  private String headCoach;

  public static final String SERIALIZED_NAME_KEY = "Key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OFFENSIVE_COORDINATOR = "OffensiveCoordinator";
  @SerializedName(SERIALIZED_NAME_OFFENSIVE_COORDINATOR)
  private String offensiveCoordinator;

  public static final String SERIALIZED_NAME_OFFENSIVE_SCHEME = "OffensiveScheme";
  @SerializedName(SERIALIZED_NAME_OFFENSIVE_SCHEME)
  private String offensiveScheme;

  public static final String SERIALIZED_NAME_PLAYER_I_D = "PlayerID";
  @SerializedName(SERIALIZED_NAME_PLAYER_I_D)
  private Integer playerID;

  public static final String SERIALIZED_NAME_PRIMARY_COLOR = "PrimaryColor";
  @SerializedName(SERIALIZED_NAME_PRIMARY_COLOR)
  private String primaryColor;

  public static final String SERIALIZED_NAME_QUATERNARY_COLOR = "QuaternaryColor";
  @SerializedName(SERIALIZED_NAME_QUATERNARY_COLOR)
  private String quaternaryColor;

  public static final String SERIALIZED_NAME_SECONDARY_COLOR = "SecondaryColor";
  @SerializedName(SERIALIZED_NAME_SECONDARY_COLOR)
  private String secondaryColor;

  public static final String SERIALIZED_NAME_SPECIAL_TEAMS_COACH = "SpecialTeamsCoach";
  @SerializedName(SERIALIZED_NAME_SPECIAL_TEAMS_COACH)
  private String specialTeamsCoach;

  public static final String SERIALIZED_NAME_STADIUM_I_D = "StadiumID";
  @SerializedName(SERIALIZED_NAME_STADIUM_I_D)
  private Integer stadiumID;

  public static final String SERIALIZED_NAME_TEAM_I_D = "TeamID";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D)
  private Integer teamID;

  public static final String SERIALIZED_NAME_TERTIARY_COLOR = "TertiaryColor";
  @SerializedName(SERIALIZED_NAME_TERTIARY_COLOR)
  private String tertiaryColor;

  public static final String SERIALIZED_NAME_WIKIPEDIA_LOGO_U_R_L = "WikipediaLogoURL";
  @SerializedName(SERIALIZED_NAME_WIKIPEDIA_LOGO_U_R_L)
  private String wikipediaLogoURL;

  public static final String SERIALIZED_NAME_WIKIPEDIA_WORD_MARK_U_R_L = "WikipediaWordMarkURL";
  @SerializedName(SERIALIZED_NAME_WIKIPEDIA_WORD_MARK_U_R_L)
  private String wikipediaWordMarkURL;

  public TeamBasic() {
  }

  public TeamBasic byeWeek(Integer byeWeek) {
    this.byeWeek = byeWeek;
    return this;
  }

  /**
   * Get byeWeek
   * @return byeWeek
   */
  @javax.annotation.Nullable
  public Integer getByeWeek() {
    return byeWeek;
  }

  public void setByeWeek(Integer byeWeek) {
    this.byeWeek = byeWeek;
  }


  public TeamBasic city(String city) {
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


  public TeamBasic conference(String conference) {
    this.conference = conference;
    return this;
  }

  /**
   * Get conference
   * @return conference
   */
  @javax.annotation.Nullable
  public String getConference() {
    return conference;
  }

  public void setConference(String conference) {
    this.conference = conference;
  }


  public TeamBasic defensiveCoordinator(String defensiveCoordinator) {
    this.defensiveCoordinator = defensiveCoordinator;
    return this;
  }

  /**
   * Get defensiveCoordinator
   * @return defensiveCoordinator
   */
  @javax.annotation.Nullable
  public String getDefensiveCoordinator() {
    return defensiveCoordinator;
  }

  public void setDefensiveCoordinator(String defensiveCoordinator) {
    this.defensiveCoordinator = defensiveCoordinator;
  }


  public TeamBasic defensiveScheme(String defensiveScheme) {
    this.defensiveScheme = defensiveScheme;
    return this;
  }

  /**
   * Get defensiveScheme
   * @return defensiveScheme
   */
  @javax.annotation.Nullable
  public String getDefensiveScheme() {
    return defensiveScheme;
  }

  public void setDefensiveScheme(String defensiveScheme) {
    this.defensiveScheme = defensiveScheme;
  }


  public TeamBasic division(String division) {
    this.division = division;
    return this;
  }

  /**
   * Get division
   * @return division
   */
  @javax.annotation.Nullable
  public String getDivision() {
    return division;
  }

  public void setDivision(String division) {
    this.division = division;
  }


  public TeamBasic fullName(String fullName) {
    this.fullName = fullName;
    return this;
  }

  /**
   * Get fullName
   * @return fullName
   */
  @javax.annotation.Nullable
  public String getFullName() {
    return fullName;
  }

  public void setFullName(String fullName) {
    this.fullName = fullName;
  }


  public TeamBasic globalTeamID(Integer globalTeamID) {
    this.globalTeamID = globalTeamID;
    return this;
  }

  /**
   * Get globalTeamID
   * @return globalTeamID
   */
  @javax.annotation.Nullable
  public Integer getGlobalTeamID() {
    return globalTeamID;
  }

  public void setGlobalTeamID(Integer globalTeamID) {
    this.globalTeamID = globalTeamID;
  }


  public TeamBasic headCoach(String headCoach) {
    this.headCoach = headCoach;
    return this;
  }

  /**
   * Get headCoach
   * @return headCoach
   */
  @javax.annotation.Nullable
  public String getHeadCoach() {
    return headCoach;
  }

  public void setHeadCoach(String headCoach) {
    this.headCoach = headCoach;
  }


  public TeamBasic key(String key) {
    this.key = key;
    return this;
  }

  /**
   * Get key
   * @return key
   */
  @javax.annotation.Nullable
  public String getKey() {
    return key;
  }

  public void setKey(String key) {
    this.key = key;
  }


  public TeamBasic name(String name) {
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


  public TeamBasic offensiveCoordinator(String offensiveCoordinator) {
    this.offensiveCoordinator = offensiveCoordinator;
    return this;
  }

  /**
   * Get offensiveCoordinator
   * @return offensiveCoordinator
   */
  @javax.annotation.Nullable
  public String getOffensiveCoordinator() {
    return offensiveCoordinator;
  }

  public void setOffensiveCoordinator(String offensiveCoordinator) {
    this.offensiveCoordinator = offensiveCoordinator;
  }


  public TeamBasic offensiveScheme(String offensiveScheme) {
    this.offensiveScheme = offensiveScheme;
    return this;
  }

  /**
   * Get offensiveScheme
   * @return offensiveScheme
   */
  @javax.annotation.Nullable
  public String getOffensiveScheme() {
    return offensiveScheme;
  }

  public void setOffensiveScheme(String offensiveScheme) {
    this.offensiveScheme = offensiveScheme;
  }


  public TeamBasic playerID(Integer playerID) {
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


  public TeamBasic primaryColor(String primaryColor) {
    this.primaryColor = primaryColor;
    return this;
  }

  /**
   * Get primaryColor
   * @return primaryColor
   */
  @javax.annotation.Nullable
  public String getPrimaryColor() {
    return primaryColor;
  }

  public void setPrimaryColor(String primaryColor) {
    this.primaryColor = primaryColor;
  }


  public TeamBasic quaternaryColor(String quaternaryColor) {
    this.quaternaryColor = quaternaryColor;
    return this;
  }

  /**
   * Get quaternaryColor
   * @return quaternaryColor
   */
  @javax.annotation.Nullable
  public String getQuaternaryColor() {
    return quaternaryColor;
  }

  public void setQuaternaryColor(String quaternaryColor) {
    this.quaternaryColor = quaternaryColor;
  }


  public TeamBasic secondaryColor(String secondaryColor) {
    this.secondaryColor = secondaryColor;
    return this;
  }

  /**
   * Get secondaryColor
   * @return secondaryColor
   */
  @javax.annotation.Nullable
  public String getSecondaryColor() {
    return secondaryColor;
  }

  public void setSecondaryColor(String secondaryColor) {
    this.secondaryColor = secondaryColor;
  }


  public TeamBasic specialTeamsCoach(String specialTeamsCoach) {
    this.specialTeamsCoach = specialTeamsCoach;
    return this;
  }

  /**
   * Get specialTeamsCoach
   * @return specialTeamsCoach
   */
  @javax.annotation.Nullable
  public String getSpecialTeamsCoach() {
    return specialTeamsCoach;
  }

  public void setSpecialTeamsCoach(String specialTeamsCoach) {
    this.specialTeamsCoach = specialTeamsCoach;
  }


  public TeamBasic stadiumID(Integer stadiumID) {
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


  public TeamBasic teamID(Integer teamID) {
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


  public TeamBasic tertiaryColor(String tertiaryColor) {
    this.tertiaryColor = tertiaryColor;
    return this;
  }

  /**
   * Get tertiaryColor
   * @return tertiaryColor
   */
  @javax.annotation.Nullable
  public String getTertiaryColor() {
    return tertiaryColor;
  }

  public void setTertiaryColor(String tertiaryColor) {
    this.tertiaryColor = tertiaryColor;
  }


  public TeamBasic wikipediaLogoURL(String wikipediaLogoURL) {
    this.wikipediaLogoURL = wikipediaLogoURL;
    return this;
  }

  /**
   * Get wikipediaLogoURL
   * @return wikipediaLogoURL
   */
  @javax.annotation.Nullable
  public String getWikipediaLogoURL() {
    return wikipediaLogoURL;
  }

  public void setWikipediaLogoURL(String wikipediaLogoURL) {
    this.wikipediaLogoURL = wikipediaLogoURL;
  }


  public TeamBasic wikipediaWordMarkURL(String wikipediaWordMarkURL) {
    this.wikipediaWordMarkURL = wikipediaWordMarkURL;
    return this;
  }

  /**
   * Get wikipediaWordMarkURL
   * @return wikipediaWordMarkURL
   */
  @javax.annotation.Nullable
  public String getWikipediaWordMarkURL() {
    return wikipediaWordMarkURL;
  }

  public void setWikipediaWordMarkURL(String wikipediaWordMarkURL) {
    this.wikipediaWordMarkURL = wikipediaWordMarkURL;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TeamBasic teamBasic = (TeamBasic) o;
    return Objects.equals(this.byeWeek, teamBasic.byeWeek) &&
        Objects.equals(this.city, teamBasic.city) &&
        Objects.equals(this.conference, teamBasic.conference) &&
        Objects.equals(this.defensiveCoordinator, teamBasic.defensiveCoordinator) &&
        Objects.equals(this.defensiveScheme, teamBasic.defensiveScheme) &&
        Objects.equals(this.division, teamBasic.division) &&
        Objects.equals(this.fullName, teamBasic.fullName) &&
        Objects.equals(this.globalTeamID, teamBasic.globalTeamID) &&
        Objects.equals(this.headCoach, teamBasic.headCoach) &&
        Objects.equals(this.key, teamBasic.key) &&
        Objects.equals(this.name, teamBasic.name) &&
        Objects.equals(this.offensiveCoordinator, teamBasic.offensiveCoordinator) &&
        Objects.equals(this.offensiveScheme, teamBasic.offensiveScheme) &&
        Objects.equals(this.playerID, teamBasic.playerID) &&
        Objects.equals(this.primaryColor, teamBasic.primaryColor) &&
        Objects.equals(this.quaternaryColor, teamBasic.quaternaryColor) &&
        Objects.equals(this.secondaryColor, teamBasic.secondaryColor) &&
        Objects.equals(this.specialTeamsCoach, teamBasic.specialTeamsCoach) &&
        Objects.equals(this.stadiumID, teamBasic.stadiumID) &&
        Objects.equals(this.teamID, teamBasic.teamID) &&
        Objects.equals(this.tertiaryColor, teamBasic.tertiaryColor) &&
        Objects.equals(this.wikipediaLogoURL, teamBasic.wikipediaLogoURL) &&
        Objects.equals(this.wikipediaWordMarkURL, teamBasic.wikipediaWordMarkURL);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(byeWeek, city, conference, defensiveCoordinator, defensiveScheme, division, fullName, globalTeamID, headCoach, key, name, offensiveCoordinator, offensiveScheme, playerID, primaryColor, quaternaryColor, secondaryColor, specialTeamsCoach, stadiumID, teamID, tertiaryColor, wikipediaLogoURL, wikipediaWordMarkURL);
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
    sb.append("class TeamBasic {\n");
    sb.append("    byeWeek: ").append(toIndentedString(byeWeek)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    conference: ").append(toIndentedString(conference)).append("\n");
    sb.append("    defensiveCoordinator: ").append(toIndentedString(defensiveCoordinator)).append("\n");
    sb.append("    defensiveScheme: ").append(toIndentedString(defensiveScheme)).append("\n");
    sb.append("    division: ").append(toIndentedString(division)).append("\n");
    sb.append("    fullName: ").append(toIndentedString(fullName)).append("\n");
    sb.append("    globalTeamID: ").append(toIndentedString(globalTeamID)).append("\n");
    sb.append("    headCoach: ").append(toIndentedString(headCoach)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    offensiveCoordinator: ").append(toIndentedString(offensiveCoordinator)).append("\n");
    sb.append("    offensiveScheme: ").append(toIndentedString(offensiveScheme)).append("\n");
    sb.append("    playerID: ").append(toIndentedString(playerID)).append("\n");
    sb.append("    primaryColor: ").append(toIndentedString(primaryColor)).append("\n");
    sb.append("    quaternaryColor: ").append(toIndentedString(quaternaryColor)).append("\n");
    sb.append("    secondaryColor: ").append(toIndentedString(secondaryColor)).append("\n");
    sb.append("    specialTeamsCoach: ").append(toIndentedString(specialTeamsCoach)).append("\n");
    sb.append("    stadiumID: ").append(toIndentedString(stadiumID)).append("\n");
    sb.append("    teamID: ").append(toIndentedString(teamID)).append("\n");
    sb.append("    tertiaryColor: ").append(toIndentedString(tertiaryColor)).append("\n");
    sb.append("    wikipediaLogoURL: ").append(toIndentedString(wikipediaLogoURL)).append("\n");
    sb.append("    wikipediaWordMarkURL: ").append(toIndentedString(wikipediaWordMarkURL)).append("\n");
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
    openapiFields.add("ByeWeek");
    openapiFields.add("City");
    openapiFields.add("Conference");
    openapiFields.add("DefensiveCoordinator");
    openapiFields.add("DefensiveScheme");
    openapiFields.add("Division");
    openapiFields.add("FullName");
    openapiFields.add("GlobalTeamID");
    openapiFields.add("HeadCoach");
    openapiFields.add("Key");
    openapiFields.add("Name");
    openapiFields.add("OffensiveCoordinator");
    openapiFields.add("OffensiveScheme");
    openapiFields.add("PlayerID");
    openapiFields.add("PrimaryColor");
    openapiFields.add("QuaternaryColor");
    openapiFields.add("SecondaryColor");
    openapiFields.add("SpecialTeamsCoach");
    openapiFields.add("StadiumID");
    openapiFields.add("TeamID");
    openapiFields.add("TertiaryColor");
    openapiFields.add("WikipediaLogoURL");
    openapiFields.add("WikipediaWordMarkURL");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TeamBasic
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TeamBasic.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TeamBasic is not found in the empty JSON string", TeamBasic.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TeamBasic.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TeamBasic` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("City") != null && !jsonObj.get("City").isJsonNull()) && !jsonObj.get("City").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `City` to be a primitive type in the JSON string but got `%s`", jsonObj.get("City").toString()));
      }
      if ((jsonObj.get("Conference") != null && !jsonObj.get("Conference").isJsonNull()) && !jsonObj.get("Conference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Conference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Conference").toString()));
      }
      if ((jsonObj.get("DefensiveCoordinator") != null && !jsonObj.get("DefensiveCoordinator").isJsonNull()) && !jsonObj.get("DefensiveCoordinator").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DefensiveCoordinator` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DefensiveCoordinator").toString()));
      }
      if ((jsonObj.get("DefensiveScheme") != null && !jsonObj.get("DefensiveScheme").isJsonNull()) && !jsonObj.get("DefensiveScheme").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DefensiveScheme` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DefensiveScheme").toString()));
      }
      if ((jsonObj.get("Division") != null && !jsonObj.get("Division").isJsonNull()) && !jsonObj.get("Division").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Division` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Division").toString()));
      }
      if ((jsonObj.get("FullName") != null && !jsonObj.get("FullName").isJsonNull()) && !jsonObj.get("FullName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FullName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FullName").toString()));
      }
      if ((jsonObj.get("HeadCoach") != null && !jsonObj.get("HeadCoach").isJsonNull()) && !jsonObj.get("HeadCoach").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `HeadCoach` to be a primitive type in the JSON string but got `%s`", jsonObj.get("HeadCoach").toString()));
      }
      if ((jsonObj.get("Key") != null && !jsonObj.get("Key").isJsonNull()) && !jsonObj.get("Key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Key").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("OffensiveCoordinator") != null && !jsonObj.get("OffensiveCoordinator").isJsonNull()) && !jsonObj.get("OffensiveCoordinator").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OffensiveCoordinator` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OffensiveCoordinator").toString()));
      }
      if ((jsonObj.get("OffensiveScheme") != null && !jsonObj.get("OffensiveScheme").isJsonNull()) && !jsonObj.get("OffensiveScheme").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OffensiveScheme` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OffensiveScheme").toString()));
      }
      if ((jsonObj.get("PrimaryColor") != null && !jsonObj.get("PrimaryColor").isJsonNull()) && !jsonObj.get("PrimaryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PrimaryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PrimaryColor").toString()));
      }
      if ((jsonObj.get("QuaternaryColor") != null && !jsonObj.get("QuaternaryColor").isJsonNull()) && !jsonObj.get("QuaternaryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `QuaternaryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("QuaternaryColor").toString()));
      }
      if ((jsonObj.get("SecondaryColor") != null && !jsonObj.get("SecondaryColor").isJsonNull()) && !jsonObj.get("SecondaryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SecondaryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SecondaryColor").toString()));
      }
      if ((jsonObj.get("SpecialTeamsCoach") != null && !jsonObj.get("SpecialTeamsCoach").isJsonNull()) && !jsonObj.get("SpecialTeamsCoach").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SpecialTeamsCoach` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SpecialTeamsCoach").toString()));
      }
      if ((jsonObj.get("TertiaryColor") != null && !jsonObj.get("TertiaryColor").isJsonNull()) && !jsonObj.get("TertiaryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TertiaryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TertiaryColor").toString()));
      }
      if ((jsonObj.get("WikipediaLogoURL") != null && !jsonObj.get("WikipediaLogoURL").isJsonNull()) && !jsonObj.get("WikipediaLogoURL").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `WikipediaLogoURL` to be a primitive type in the JSON string but got `%s`", jsonObj.get("WikipediaLogoURL").toString()));
      }
      if ((jsonObj.get("WikipediaWordMarkURL") != null && !jsonObj.get("WikipediaWordMarkURL").isJsonNull()) && !jsonObj.get("WikipediaWordMarkURL").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `WikipediaWordMarkURL` to be a primitive type in the JSON string but got `%s`", jsonObj.get("WikipediaWordMarkURL").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TeamBasic.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TeamBasic' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TeamBasic> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TeamBasic.class));

       return (TypeAdapter<T>) new TypeAdapter<TeamBasic>() {
           @Override
           public void write(JsonWriter out, TeamBasic value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TeamBasic read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TeamBasic given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TeamBasic
   * @throws IOException if the JSON string is invalid with respect to TeamBasic
   */
  public static TeamBasic fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TeamBasic.class);
  }

  /**
   * Convert an instance of TeamBasic to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

