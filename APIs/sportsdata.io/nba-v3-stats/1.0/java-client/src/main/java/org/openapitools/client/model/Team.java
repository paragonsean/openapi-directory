/*
 * NBA v3 Stats
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
 * Team
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:43.661436-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Team {
  public static final String SERIALIZED_NAME_ACTIVE = "Active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_CITY = "City";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_CONFERENCE = "Conference";
  @SerializedName(SERIALIZED_NAME_CONFERENCE)
  private String conference;

  public static final String SERIALIZED_NAME_DIVISION = "Division";
  @SerializedName(SERIALIZED_NAME_DIVISION)
  private String division;

  public static final String SERIALIZED_NAME_GLOBAL_TEAM_I_D = "GlobalTeamID";
  @SerializedName(SERIALIZED_NAME_GLOBAL_TEAM_I_D)
  private Integer globalTeamID;

  public static final String SERIALIZED_NAME_KEY = "Key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_LEAGUE_I_D = "LeagueID";
  @SerializedName(SERIALIZED_NAME_LEAGUE_I_D)
  private Integer leagueID;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NBA_DOT_COM_TEAM_I_D = "NbaDotComTeamID";
  @SerializedName(SERIALIZED_NAME_NBA_DOT_COM_TEAM_I_D)
  private Integer nbaDotComTeamID;

  public static final String SERIALIZED_NAME_PRIMARY_COLOR = "PrimaryColor";
  @SerializedName(SERIALIZED_NAME_PRIMARY_COLOR)
  private String primaryColor;

  public static final String SERIALIZED_NAME_QUATERNARY_COLOR = "QuaternaryColor";
  @SerializedName(SERIALIZED_NAME_QUATERNARY_COLOR)
  private String quaternaryColor;

  public static final String SERIALIZED_NAME_SECONDARY_COLOR = "SecondaryColor";
  @SerializedName(SERIALIZED_NAME_SECONDARY_COLOR)
  private String secondaryColor;

  public static final String SERIALIZED_NAME_STADIUM_I_D = "StadiumID";
  @SerializedName(SERIALIZED_NAME_STADIUM_I_D)
  private Integer stadiumID;

  public static final String SERIALIZED_NAME_TEAM_I_D = "TeamID";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D)
  private Integer teamID;

  public static final String SERIALIZED_NAME_TERTIARY_COLOR = "TertiaryColor";
  @SerializedName(SERIALIZED_NAME_TERTIARY_COLOR)
  private String tertiaryColor;

  public static final String SERIALIZED_NAME_WIKIPEDIA_LOGO_URL = "WikipediaLogoUrl";
  @SerializedName(SERIALIZED_NAME_WIKIPEDIA_LOGO_URL)
  private String wikipediaLogoUrl;

  public static final String SERIALIZED_NAME_WIKIPEDIA_WORD_MARK_URL = "WikipediaWordMarkUrl";
  @SerializedName(SERIALIZED_NAME_WIKIPEDIA_WORD_MARK_URL)
  private String wikipediaWordMarkUrl;

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


  public Team city(String city) {
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


  public Team division(String division) {
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


  public Team leagueID(Integer leagueID) {
    this.leagueID = leagueID;
    return this;
  }

  /**
   * Get leagueID
   * @return leagueID
   */
  @javax.annotation.Nullable
  public Integer getLeagueID() {
    return leagueID;
  }

  public void setLeagueID(Integer leagueID) {
    this.leagueID = leagueID;
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


  public Team nbaDotComTeamID(Integer nbaDotComTeamID) {
    this.nbaDotComTeamID = nbaDotComTeamID;
    return this;
  }

  /**
   * Get nbaDotComTeamID
   * @return nbaDotComTeamID
   */
  @javax.annotation.Nullable
  public Integer getNbaDotComTeamID() {
    return nbaDotComTeamID;
  }

  public void setNbaDotComTeamID(Integer nbaDotComTeamID) {
    this.nbaDotComTeamID = nbaDotComTeamID;
  }


  public Team primaryColor(String primaryColor) {
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


  public Team quaternaryColor(String quaternaryColor) {
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


  public Team secondaryColor(String secondaryColor) {
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


  public Team stadiumID(Integer stadiumID) {
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


  public Team tertiaryColor(String tertiaryColor) {
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


  public Team wikipediaLogoUrl(String wikipediaLogoUrl) {
    this.wikipediaLogoUrl = wikipediaLogoUrl;
    return this;
  }

  /**
   * Get wikipediaLogoUrl
   * @return wikipediaLogoUrl
   */
  @javax.annotation.Nullable
  public String getWikipediaLogoUrl() {
    return wikipediaLogoUrl;
  }

  public void setWikipediaLogoUrl(String wikipediaLogoUrl) {
    this.wikipediaLogoUrl = wikipediaLogoUrl;
  }


  public Team wikipediaWordMarkUrl(String wikipediaWordMarkUrl) {
    this.wikipediaWordMarkUrl = wikipediaWordMarkUrl;
    return this;
  }

  /**
   * Get wikipediaWordMarkUrl
   * @return wikipediaWordMarkUrl
   */
  @javax.annotation.Nullable
  public String getWikipediaWordMarkUrl() {
    return wikipediaWordMarkUrl;
  }

  public void setWikipediaWordMarkUrl(String wikipediaWordMarkUrl) {
    this.wikipediaWordMarkUrl = wikipediaWordMarkUrl;
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
        Objects.equals(this.city, team.city) &&
        Objects.equals(this.conference, team.conference) &&
        Objects.equals(this.division, team.division) &&
        Objects.equals(this.globalTeamID, team.globalTeamID) &&
        Objects.equals(this.key, team.key) &&
        Objects.equals(this.leagueID, team.leagueID) &&
        Objects.equals(this.name, team.name) &&
        Objects.equals(this.nbaDotComTeamID, team.nbaDotComTeamID) &&
        Objects.equals(this.primaryColor, team.primaryColor) &&
        Objects.equals(this.quaternaryColor, team.quaternaryColor) &&
        Objects.equals(this.secondaryColor, team.secondaryColor) &&
        Objects.equals(this.stadiumID, team.stadiumID) &&
        Objects.equals(this.teamID, team.teamID) &&
        Objects.equals(this.tertiaryColor, team.tertiaryColor) &&
        Objects.equals(this.wikipediaLogoUrl, team.wikipediaLogoUrl) &&
        Objects.equals(this.wikipediaWordMarkUrl, team.wikipediaWordMarkUrl);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, city, conference, division, globalTeamID, key, leagueID, name, nbaDotComTeamID, primaryColor, quaternaryColor, secondaryColor, stadiumID, teamID, tertiaryColor, wikipediaLogoUrl, wikipediaWordMarkUrl);
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
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    conference: ").append(toIndentedString(conference)).append("\n");
    sb.append("    division: ").append(toIndentedString(division)).append("\n");
    sb.append("    globalTeamID: ").append(toIndentedString(globalTeamID)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    leagueID: ").append(toIndentedString(leagueID)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nbaDotComTeamID: ").append(toIndentedString(nbaDotComTeamID)).append("\n");
    sb.append("    primaryColor: ").append(toIndentedString(primaryColor)).append("\n");
    sb.append("    quaternaryColor: ").append(toIndentedString(quaternaryColor)).append("\n");
    sb.append("    secondaryColor: ").append(toIndentedString(secondaryColor)).append("\n");
    sb.append("    stadiumID: ").append(toIndentedString(stadiumID)).append("\n");
    sb.append("    teamID: ").append(toIndentedString(teamID)).append("\n");
    sb.append("    tertiaryColor: ").append(toIndentedString(tertiaryColor)).append("\n");
    sb.append("    wikipediaLogoUrl: ").append(toIndentedString(wikipediaLogoUrl)).append("\n");
    sb.append("    wikipediaWordMarkUrl: ").append(toIndentedString(wikipediaWordMarkUrl)).append("\n");
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
    openapiFields.add("City");
    openapiFields.add("Conference");
    openapiFields.add("Division");
    openapiFields.add("GlobalTeamID");
    openapiFields.add("Key");
    openapiFields.add("LeagueID");
    openapiFields.add("Name");
    openapiFields.add("NbaDotComTeamID");
    openapiFields.add("PrimaryColor");
    openapiFields.add("QuaternaryColor");
    openapiFields.add("SecondaryColor");
    openapiFields.add("StadiumID");
    openapiFields.add("TeamID");
    openapiFields.add("TertiaryColor");
    openapiFields.add("WikipediaLogoUrl");
    openapiFields.add("WikipediaWordMarkUrl");

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
      if ((jsonObj.get("City") != null && !jsonObj.get("City").isJsonNull()) && !jsonObj.get("City").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `City` to be a primitive type in the JSON string but got `%s`", jsonObj.get("City").toString()));
      }
      if ((jsonObj.get("Conference") != null && !jsonObj.get("Conference").isJsonNull()) && !jsonObj.get("Conference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Conference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Conference").toString()));
      }
      if ((jsonObj.get("Division") != null && !jsonObj.get("Division").isJsonNull()) && !jsonObj.get("Division").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Division` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Division").toString()));
      }
      if ((jsonObj.get("Key") != null && !jsonObj.get("Key").isJsonNull()) && !jsonObj.get("Key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Key").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
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
      if ((jsonObj.get("TertiaryColor") != null && !jsonObj.get("TertiaryColor").isJsonNull()) && !jsonObj.get("TertiaryColor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TertiaryColor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TertiaryColor").toString()));
      }
      if ((jsonObj.get("WikipediaLogoUrl") != null && !jsonObj.get("WikipediaLogoUrl").isJsonNull()) && !jsonObj.get("WikipediaLogoUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `WikipediaLogoUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("WikipediaLogoUrl").toString()));
      }
      if ((jsonObj.get("WikipediaWordMarkUrl") != null && !jsonObj.get("WikipediaWordMarkUrl").isJsonNull()) && !jsonObj.get("WikipediaWordMarkUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `WikipediaWordMarkUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("WikipediaWordMarkUrl").toString()));
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

