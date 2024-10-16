/*
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.DistrictRankingEventPointsInner;

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
 * Rank of a team in a district.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:47.661723-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DistrictRanking {
  public static final String SERIALIZED_NAME_EVENT_POINTS = "event_points";
  @SerializedName(SERIALIZED_NAME_EVENT_POINTS)
  private List<DistrictRankingEventPointsInner> eventPoints = new ArrayList<>();

  public static final String SERIALIZED_NAME_POINT_TOTAL = "point_total";
  @SerializedName(SERIALIZED_NAME_POINT_TOTAL)
  private Integer pointTotal;

  public static final String SERIALIZED_NAME_RANK = "rank";
  @SerializedName(SERIALIZED_NAME_RANK)
  private Integer rank;

  public static final String SERIALIZED_NAME_ROOKIE_BONUS = "rookie_bonus";
  @SerializedName(SERIALIZED_NAME_ROOKIE_BONUS)
  private Integer rookieBonus;

  public static final String SERIALIZED_NAME_TEAM_KEY = "team_key";
  @SerializedName(SERIALIZED_NAME_TEAM_KEY)
  private String teamKey;

  public DistrictRanking() {
  }

  public DistrictRanking eventPoints(List<DistrictRankingEventPointsInner> eventPoints) {
    this.eventPoints = eventPoints;
    return this;
  }

  public DistrictRanking addEventPointsItem(DistrictRankingEventPointsInner eventPointsItem) {
    if (this.eventPoints == null) {
      this.eventPoints = new ArrayList<>();
    }
    this.eventPoints.add(eventPointsItem);
    return this;
  }

  /**
   * List of events that contributed to the point total for the team.
   * @return eventPoints
   */
  @javax.annotation.Nullable
  public List<DistrictRankingEventPointsInner> getEventPoints() {
    return eventPoints;
  }

  public void setEventPoints(List<DistrictRankingEventPointsInner> eventPoints) {
    this.eventPoints = eventPoints;
  }


  public DistrictRanking pointTotal(Integer pointTotal) {
    this.pointTotal = pointTotal;
    return this;
  }

  /**
   * Total district points for the team.
   * @return pointTotal
   */
  @javax.annotation.Nonnull
  public Integer getPointTotal() {
    return pointTotal;
  }

  public void setPointTotal(Integer pointTotal) {
    this.pointTotal = pointTotal;
  }


  public DistrictRanking rank(Integer rank) {
    this.rank = rank;
    return this;
  }

  /**
   * Numerical rank of the team, 1 being top rank.
   * @return rank
   */
  @javax.annotation.Nonnull
  public Integer getRank() {
    return rank;
  }

  public void setRank(Integer rank) {
    this.rank = rank;
  }


  public DistrictRanking rookieBonus(Integer rookieBonus) {
    this.rookieBonus = rookieBonus;
    return this;
  }

  /**
   * Any points added to a team as a result of the rookie bonus.
   * @return rookieBonus
   */
  @javax.annotation.Nullable
  public Integer getRookieBonus() {
    return rookieBonus;
  }

  public void setRookieBonus(Integer rookieBonus) {
    this.rookieBonus = rookieBonus;
  }


  public DistrictRanking teamKey(String teamKey) {
    this.teamKey = teamKey;
    return this;
  }

  /**
   * TBA team key for the team.
   * @return teamKey
   */
  @javax.annotation.Nonnull
  public String getTeamKey() {
    return teamKey;
  }

  public void setTeamKey(String teamKey) {
    this.teamKey = teamKey;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DistrictRanking districtRanking = (DistrictRanking) o;
    return Objects.equals(this.eventPoints, districtRanking.eventPoints) &&
        Objects.equals(this.pointTotal, districtRanking.pointTotal) &&
        Objects.equals(this.rank, districtRanking.rank) &&
        Objects.equals(this.rookieBonus, districtRanking.rookieBonus) &&
        Objects.equals(this.teamKey, districtRanking.teamKey);
  }

  @Override
  public int hashCode() {
    return Objects.hash(eventPoints, pointTotal, rank, rookieBonus, teamKey);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DistrictRanking {\n");
    sb.append("    eventPoints: ").append(toIndentedString(eventPoints)).append("\n");
    sb.append("    pointTotal: ").append(toIndentedString(pointTotal)).append("\n");
    sb.append("    rank: ").append(toIndentedString(rank)).append("\n");
    sb.append("    rookieBonus: ").append(toIndentedString(rookieBonus)).append("\n");
    sb.append("    teamKey: ").append(toIndentedString(teamKey)).append("\n");
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
    openapiFields.add("event_points");
    openapiFields.add("point_total");
    openapiFields.add("rank");
    openapiFields.add("rookie_bonus");
    openapiFields.add("team_key");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("point_total");
    openapiRequiredFields.add("rank");
    openapiRequiredFields.add("team_key");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DistrictRanking
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DistrictRanking.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DistrictRanking is not found in the empty JSON string", DistrictRanking.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DistrictRanking.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DistrictRanking` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DistrictRanking.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("event_points") != null && !jsonObj.get("event_points").isJsonNull()) {
        JsonArray jsonArrayeventPoints = jsonObj.getAsJsonArray("event_points");
        if (jsonArrayeventPoints != null) {
          // ensure the json data is an array
          if (!jsonObj.get("event_points").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `event_points` to be an array in the JSON string but got `%s`", jsonObj.get("event_points").toString()));
          }

          // validate the optional field `event_points` (array)
          for (int i = 0; i < jsonArrayeventPoints.size(); i++) {
            DistrictRankingEventPointsInner.validateJsonElement(jsonArrayeventPoints.get(i));
          };
        }
      }
      if (!jsonObj.get("team_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `team_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("team_key").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DistrictRanking.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DistrictRanking' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DistrictRanking> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DistrictRanking.class));

       return (TypeAdapter<T>) new TypeAdapter<DistrictRanking>() {
           @Override
           public void write(JsonWriter out, DistrictRanking value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DistrictRanking read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DistrictRanking given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DistrictRanking
   * @throws IOException if the JSON string is invalid with respect to DistrictRanking
   */
  public static DistrictRanking fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DistrictRanking.class);
  }

  /**
   * Convert an instance of DistrictRanking to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

