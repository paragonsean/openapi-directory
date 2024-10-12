/*
 * CBB v3 Scores
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
 * Team
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:10.258689-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Team {
  public static final String SERIALIZED_NAME_ACTIVE = "Active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_AP_RANK = "ApRank";
  @SerializedName(SERIALIZED_NAME_AP_RANK)
  private Integer apRank;

  public static final String SERIALIZED_NAME_CONFERENCE = "Conference";
  @SerializedName(SERIALIZED_NAME_CONFERENCE)
  private String conference;

  public static final String SERIALIZED_NAME_CONFERENCE_I_D = "ConferenceID";
  @SerializedName(SERIALIZED_NAME_CONFERENCE_I_D)
  private Integer conferenceID;

  public static final String SERIALIZED_NAME_CONFERENCE_LOSSES = "ConferenceLosses";
  @SerializedName(SERIALIZED_NAME_CONFERENCE_LOSSES)
  private Integer conferenceLosses;

  public static final String SERIALIZED_NAME_CONFERENCE_WINS = "ConferenceWins";
  @SerializedName(SERIALIZED_NAME_CONFERENCE_WINS)
  private Integer conferenceWins;

  public static final String SERIALIZED_NAME_GLOBAL_TEAM_I_D = "GlobalTeamID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_TEAM_I_D)
  private Integer globalTeamID;

  public static final String SERIALIZED_NAME_KEY = "Key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_LOSSES = "Losses";
  @SerializedName(SERIALIZED_NAME_LOSSES)
  private Integer losses;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SCHOOL = "School";
  @SerializedName(SERIALIZED_NAME_SCHOOL)
  private String school;

  public static final String SERIALIZED_NAME_SHORT_DISPLAY_NAME = "ShortDisplayName";
  @SerializedName(SERIALIZED_NAME_SHORT_DISPLAY_NAME)
  private String shortDisplayName;

  public static final String SERIALIZED_NAME_STADIUM = "Stadium";
  @SerializedName(SERIALIZED_NAME_STADIUM)
  private Stadium stadium;

  public static final String SERIALIZED_NAME_TEAM_I_D = "TeamID";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D)
  private Integer teamID;

  public static final String SERIALIZED_NAME_TEAM_LOGO_URL = "TeamLogoUrl";
  @SerializedName(SERIALIZED_NAME_TEAM_LOGO_URL)
  private String teamLogoUrl;

  public static final String SERIALIZED_NAME_WINS = "Wins";
  @SerializedName(SERIALIZED_NAME_WINS)
  private Integer wins;

  public Team() {
  }

  public Team active(Boolean active) {
    this.active = active;
    return this;
  }

  /**
   * Get active
   * @return active
   */
  @javax.annotation.Nullable
  public Boolean getActive() {
    return active;
  }

  public void setActive(Boolean active) {
    this.active = active;
  }


  public Team apRank(Integer apRank) {
    this.apRank = apRank;
    return this;
  }

  /**
   * Get apRank
   * @return apRank
   */
  @javax.annotation.Nullable
  public Integer getApRank() {
    return apRank;
  }

  public void setApRank(Integer apRank) {
    this.apRank = apRank;
  }


  public Team conference(String conference) {
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


  public Team conferenceID(Integer conferenceID) {
    this.conferenceID = conferenceID;
    return this;
  }

  /**
   * Get conferenceID
   * @return conferenceID
   */
  @javax.annotation.Nullable
  public Integer getConferenceID() {
    return conferenceID;
  }

  public void setConferenceID(Integer conferenceID) {
    this.conferenceID = conferenceID;
  }


  public Team conferenceLosses(Integer conferenceLosses) {
    this.conferenceLosses = conferenceLosses;
    return this;
  }

  /**
   * Get conferenceLosses
   * @return conferenceLosses
   */
  @javax.annotation.Nullable
  public Integer getConferenceLosses() {
    return conferenceLosses;
  }

  public void setConferenceLosses(Integer conferenceLosses) {
    this.conferenceLosses = conferenceLosses;
  }


  public Team conferenceWins(Integer conferenceWins) {
    this.conferenceWins = conferenceWins;
    return this;
  }

  /**
   * Get conferenceWins
   * @return conferenceWins
   */
  @javax.annotation.Nullable
  public Integer getConferenceWins() {
    return conferenceWins;
  }

  public void setConferenceWins(Integer conferenceWins) {
    this.conferenceWins = conferenceWins;
  }


  public Team globalTeamID(Integer globalTeamID) {
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


  public Team key(String key) {
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


  public Team losses(Integer losses) {
    this.losses = losses;
    return this;
  }

  /**
   * Get losses
   * @return losses
   */
  @javax.annotation.Nullable
  public Integer getLosses() {
    return losses;
  }

  public void setLosses(Integer losses) {
    this.losses = losses;
  }


  public Team name(String name) {
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


  public Team school(String school) {
    this.school = school;
    return this;
  }

  /**
   * Get school
   * @return school
   */
  @javax.annotation.Nullable
  public String getSchool() {
    return school;
  }

  public void setSchool(String school) {
    this.school = school;
  }


  public Team shortDisplayName(String shortDisplayName) {
    this.shortDisplayName = shortDisplayName;
    return this;
  }

  /**
   * Get shortDisplayName
   * @return shortDisplayName
   */
  @javax.annotation.Nullable
  public String getShortDisplayName() {
    return shortDisplayName;
  }

  public void setShortDisplayName(String shortDisplayName) {
    this.shortDisplayName = shortDisplayName;
  }


  public Team stadium(Stadium stadium) {
    this.stadium = stadium;
    return this;
  }

  /**
   * Get stadium
   * @return stadium
   */
  @javax.annotation.Nullable
  public Stadium getStadium() {
    return stadium;
  }

  public void setStadium(Stadium stadium) {
    this.stadium = stadium;
  }


  public Team teamID(Integer teamID) {
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


  public Team teamLogoUrl(String teamLogoUrl) {
    this.teamLogoUrl = teamLogoUrl;
    return this;
  }

  /**
   * Get teamLogoUrl
   * @return teamLogoUrl
   */
  @javax.annotation.Nullable
  public String getTeamLogoUrl() {
    return teamLogoUrl;
  }

  public void setTeamLogoUrl(String teamLogoUrl) {
    this.teamLogoUrl = teamLogoUrl;
  }


  public Team wins(Integer wins) {
    this.wins = wins;
    return this;
  }

  /**
   * Get wins
   * @return wins
   */
  @javax.annotation.Nullable
  public Integer getWins() {
    return wins;
  }

  public void setWins(Integer wins) {
    this.wins = wins;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Team team = (Team) o;
    return Objects.equals(this.active, team.active) &&
        Objects.equals(this.apRank, team.apRank) &&
        Objects.equals(this.conference, team.conference) &&
        Objects.equals(this.conferenceID, team.conferenceID) &&
        Objects.equals(this.conferenceLosses, team.conferenceLosses) &&
        Objects.equals(this.conferenceWins, team.conferenceWins) &&
        Objects.equals(this.globalTeamID, team.globalTeamID) &&
        Objects.equals(this.key, team.key) &&
        Objects.equals(this.losses, team.losses) &&
        Objects.equals(this.name, team.name) &&
        Objects.equals(this.school, team.school) &&
        Objects.equals(this.shortDisplayName, team.shortDisplayName) &&
        Objects.equals(this.stadium, team.stadium) &&
        Objects.equals(this.teamID, team.teamID) &&
        Objects.equals(this.teamLogoUrl, team.teamLogoUrl) &&
        Objects.equals(this.wins, team.wins);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, apRank, conference, conferenceID, conferenceLosses, conferenceWins, globalTeamID, key, losses, name, school, shortDisplayName, stadium, teamID, teamLogoUrl, wins);
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
    sb.append("class Team {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    apRank: ").append(toIndentedString(apRank)).append("\n");
    sb.append("    conference: ").append(toIndentedString(conference)).append("\n");
    sb.append("    conferenceID: ").append(toIndentedString(conferenceID)).append("\n");
    sb.append("    conferenceLosses: ").append(toIndentedString(conferenceLosses)).append("\n");
    sb.append("    conferenceWins: ").append(toIndentedString(conferenceWins)).append("\n");
    sb.append("    globalTeamID: ").append(toIndentedString(globalTeamID)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    losses: ").append(toIndentedString(losses)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    school: ").append(toIndentedString(school)).append("\n");
    sb.append("    shortDisplayName: ").append(toIndentedString(shortDisplayName)).append("\n");
    sb.append("    stadium: ").append(toIndentedString(stadium)).append("\n");
    sb.append("    teamID: ").append(toIndentedString(teamID)).append("\n");
    sb.append("    teamLogoUrl: ").append(toIndentedString(teamLogoUrl)).append("\n");
    sb.append("    wins: ").append(toIndentedString(wins)).append("\n");
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
    openapiFields.add("Active");
    openapiFields.add("ApRank");
    openapiFields.add("Conference");
    openapiFields.add("ConferenceID");
    openapiFields.add("ConferenceLosses");
    openapiFields.add("ConferenceWins");
    openapiFields.add("GlobalTeamID");
    openapiFields.add("Key");
    openapiFields.add("Losses");
    openapiFields.add("Name");
    openapiFields.add("School");
    openapiFields.add("ShortDisplayName");
    openapiFields.add("Stadium");
    openapiFields.add("TeamID");
    openapiFields.add("TeamLogoUrl");
    openapiFields.add("Wins");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Team
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Team.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Team is not found in the empty JSON string", Team.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Team.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Team` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Conference") != null && !jsonObj.get("Conference").isJsonNull()) && !jsonObj.get("Conference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Conference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Conference").toString()));
      }
      if ((jsonObj.get("Key") != null && !jsonObj.get("Key").isJsonNull()) && !jsonObj.get("Key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Key").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("School") != null && !jsonObj.get("School").isJsonNull()) && !jsonObj.get("School").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `School` to be a primitive type in the JSON string but got `%s`", jsonObj.get("School").toString()));
      }
      if ((jsonObj.get("ShortDisplayName") != null && !jsonObj.get("ShortDisplayName").isJsonNull()) && !jsonObj.get("ShortDisplayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ShortDisplayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ShortDisplayName").toString()));
      }
      // validate the optional field `Stadium`
      if (jsonObj.get("Stadium") != null && !jsonObj.get("Stadium").isJsonNull()) {
        Stadium.validateJsonElement(jsonObj.get("Stadium"));
      }
      if ((jsonObj.get("TeamLogoUrl") != null && !jsonObj.get("TeamLogoUrl").isJsonNull()) && !jsonObj.get("TeamLogoUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TeamLogoUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TeamLogoUrl").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Team.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Team' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Team> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Team.class));

       return (TypeAdapter<T>) new TypeAdapter<Team>() {
           @Override
           public void write(JsonWriter out, Team value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Team read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Team given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Team
   * @throws IOException if the JSON string is invalid with respect to Team
   */
  public static Team fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Team.class);
  }

  /**
   * Convert an instance of Team to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

