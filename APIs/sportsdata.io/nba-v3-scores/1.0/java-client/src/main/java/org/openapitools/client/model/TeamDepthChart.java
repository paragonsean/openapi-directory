/*
 * NBA v3 Scores
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.DepthChart;

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
 * TeamDepthChart
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:02.009960-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TeamDepthChart {
  public static final String SERIALIZED_NAME_DEPTH_CHARTS = "DepthCharts";
  @SerializedName(SERIALIZED_NAME_DEPTH_CHARTS)
  private List<DepthChart> depthCharts = new ArrayList<>();

  public static final String SERIALIZED_NAME_TEAM_I_D = "TeamID";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D)
  private Integer teamID;

  public TeamDepthChart() {
  }

  public TeamDepthChart depthCharts(List<DepthChart> depthCharts) {
    this.depthCharts = depthCharts;
    return this;
  }

  public TeamDepthChart addDepthChartsItem(DepthChart depthChartsItem) {
    if (this.depthCharts == null) {
      this.depthCharts = new ArrayList<>();
    }
    this.depthCharts.add(depthChartsItem);
    return this;
  }

  /**
   * Get depthCharts
   * @return depthCharts
   */
  @javax.annotation.Nullable
  public List<DepthChart> getDepthCharts() {
    return depthCharts;
  }

  public void setDepthCharts(List<DepthChart> depthCharts) {
    this.depthCharts = depthCharts;
  }


  public TeamDepthChart teamID(Integer teamID) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TeamDepthChart teamDepthChart = (TeamDepthChart) o;
    return Objects.equals(this.depthCharts, teamDepthChart.depthCharts) &&
        Objects.equals(this.teamID, teamDepthChart.teamID);
  }

  @Override
  public int hashCode() {
    return Objects.hash(depthCharts, teamID);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TeamDepthChart {\n");
    sb.append("    depthCharts: ").append(toIndentedString(depthCharts)).append("\n");
    sb.append("    teamID: ").append(toIndentedString(teamID)).append("\n");
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
    openapiFields.add("DepthCharts");
    openapiFields.add("TeamID");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TeamDepthChart
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TeamDepthChart.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TeamDepthChart is not found in the empty JSON string", TeamDepthChart.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TeamDepthChart.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TeamDepthChart` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("DepthCharts") != null && !jsonObj.get("DepthCharts").isJsonNull()) {
        JsonArray jsonArraydepthCharts = jsonObj.getAsJsonArray("DepthCharts");
        if (jsonArraydepthCharts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("DepthCharts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `DepthCharts` to be an array in the JSON string but got `%s`", jsonObj.get("DepthCharts").toString()));
          }

          // validate the optional field `DepthCharts` (array)
          for (int i = 0; i < jsonArraydepthCharts.size(); i++) {
            DepthChart.validateJsonElement(jsonArraydepthCharts.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TeamDepthChart.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TeamDepthChart' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TeamDepthChart> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TeamDepthChart.class));

       return (TypeAdapter<T>) new TypeAdapter<TeamDepthChart>() {
           @Override
           public void write(JsonWriter out, TeamDepthChart value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TeamDepthChart read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TeamDepthChart given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TeamDepthChart
   * @throws IOException if the JSON string is invalid with respect to TeamDepthChart
   */
  public static TeamDepthChart fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TeamDepthChart.class);
  }

  /**
   * Convert an instance of TeamDepthChart to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

