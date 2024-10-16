/*
 * LoL v3 Stats
 * LoL v3 Stats
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
import org.openapitools.client.model.Team;
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
 * SeasonTeam
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:14.423769-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SeasonTeam {
  public static final String SERIALIZED_NAME_ACTIVE = "Active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_GENDER = "Gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_SEASON_ID = "SeasonId";
  @SerializedName(SERIALIZED_NAME_SEASON_ID)
  private Integer seasonId;

  public static final String SERIALIZED_NAME_SEASON_TEAM_ID = "SeasonTeamId";
  @SerializedName(SERIALIZED_NAME_SEASON_TEAM_ID)
  private Integer seasonTeamId;

  public static final String SERIALIZED_NAME_TEAM = "Team";
  @SerializedName(SERIALIZED_NAME_TEAM)
  private Team team;

  public static final String SERIALIZED_NAME_TEAM_ID = "TeamId";
  @SerializedName(SERIALIZED_NAME_TEAM_ID)
  private Integer teamId;

  public static final String SERIALIZED_NAME_TEAM_NAME = "TeamName";
  @SerializedName(SERIALIZED_NAME_TEAM_NAME)
  private String teamName;

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public SeasonTeam() {
  }

  public SeasonTeam active(Boolean active) {
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


  public SeasonTeam gender(String gender) {
    this.gender = gender;
    return this;
  }

  /**
   * Get gender
   * @return gender
   */
  @javax.annotation.Nullable
  public String getGender() {
    return gender;
  }

  public void setGender(String gender) {
    this.gender = gender;
  }


  public SeasonTeam seasonId(Integer seasonId) {
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


  public SeasonTeam seasonTeamId(Integer seasonTeamId) {
    this.seasonTeamId = seasonTeamId;
    return this;
  }

  /**
   * Get seasonTeamId
   * @return seasonTeamId
   */
  @javax.annotation.Nullable
  public Integer getSeasonTeamId() {
    return seasonTeamId;
  }

  public void setSeasonTeamId(Integer seasonTeamId) {
    this.seasonTeamId = seasonTeamId;
  }


  public SeasonTeam team(Team team) {
    this.team = team;
    return this;
  }

  /**
   * Get team
   * @return team
   */
  @javax.annotation.Nullable
  public Team getTeam() {
    return team;
  }

  public void setTeam(Team team) {
    this.team = team;
  }


  public SeasonTeam teamId(Integer teamId) {
    this.teamId = teamId;
    return this;
  }

  /**
   * Get teamId
   * @return teamId
   */
  @javax.annotation.Nullable
  public Integer getTeamId() {
    return teamId;
  }

  public void setTeamId(Integer teamId) {
    this.teamId = teamId;
  }


  public SeasonTeam teamName(String teamName) {
    this.teamName = teamName;
    return this;
  }

  /**
   * Get teamName
   * @return teamName
   */
  @javax.annotation.Nullable
  public String getTeamName() {
    return teamName;
  }

  public void setTeamName(String teamName) {
    this.teamName = teamName;
  }


  public SeasonTeam type(String type) {
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
    SeasonTeam seasonTeam = (SeasonTeam) o;
    return Objects.equals(this.active, seasonTeam.active) &&
        Objects.equals(this.gender, seasonTeam.gender) &&
        Objects.equals(this.seasonId, seasonTeam.seasonId) &&
        Objects.equals(this.seasonTeamId, seasonTeam.seasonTeamId) &&
        Objects.equals(this.team, seasonTeam.team) &&
        Objects.equals(this.teamId, seasonTeam.teamId) &&
        Objects.equals(this.teamName, seasonTeam.teamName) &&
        Objects.equals(this.type, seasonTeam.type);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, gender, seasonId, seasonTeamId, team, teamId, teamName, type);
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
    sb.append("class SeasonTeam {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    seasonId: ").append(toIndentedString(seasonId)).append("\n");
    sb.append("    seasonTeamId: ").append(toIndentedString(seasonTeamId)).append("\n");
    sb.append("    team: ").append(toIndentedString(team)).append("\n");
    sb.append("    teamId: ").append(toIndentedString(teamId)).append("\n");
    sb.append("    teamName: ").append(toIndentedString(teamName)).append("\n");
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
    openapiFields.add("Active");
    openapiFields.add("Gender");
    openapiFields.add("SeasonId");
    openapiFields.add("SeasonTeamId");
    openapiFields.add("Team");
    openapiFields.add("TeamId");
    openapiFields.add("TeamName");
    openapiFields.add("Type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SeasonTeam
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SeasonTeam.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SeasonTeam is not found in the empty JSON string", SeasonTeam.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SeasonTeam.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SeasonTeam` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Gender") != null && !jsonObj.get("Gender").isJsonNull()) && !jsonObj.get("Gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Gender").toString()));
      }
      // validate the optional field `Team`
      if (jsonObj.get("Team") != null && !jsonObj.get("Team").isJsonNull()) {
        Team.validateJsonElement(jsonObj.get("Team"));
      }
      if ((jsonObj.get("TeamName") != null && !jsonObj.get("TeamName").isJsonNull()) && !jsonObj.get("TeamName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TeamName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TeamName").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SeasonTeam.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SeasonTeam' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SeasonTeam> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SeasonTeam.class));

       return (TypeAdapter<T>) new TypeAdapter<SeasonTeam>() {
           @Override
           public void write(JsonWriter out, SeasonTeam value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SeasonTeam read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SeasonTeam given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SeasonTeam
   * @throws IOException if the JSON string is invalid with respect to SeasonTeam
   */
  public static SeasonTeam fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SeasonTeam.class);
  }

  /**
   * Convert an instance of SeasonTeam to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

