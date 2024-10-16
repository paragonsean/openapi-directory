/*
 * Noosh API application
 * Full description of Noosh API
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
import org.openapitools.client.model.TeamTemplateItemVO;

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
 * Java type: com.noosh.nooshapi.vo.TeamTemplateDetailVO
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:23.742517-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TeamTemplateDetailVO {
  public static final String SERIALIZED_NAME_TEAM_TEAMPLE_ITEM = "team_teample_item";
  @SerializedName(SERIALIZED_NAME_TEAM_TEAMPLE_ITEM)
  private List<TeamTemplateItemVO> teamTeampleItem = new ArrayList<>();

  public static final String SERIALIZED_NAME_TEAM_TEMPLATE_ID = "team_template_id";
  @SerializedName(SERIALIZED_NAME_TEAM_TEMPLATE_ID)
  private Long teamTemplateId;

  public static final String SERIALIZED_NAME_TEAM_TEMPLATE_NAME = "team_template_name";
  @SerializedName(SERIALIZED_NAME_TEAM_TEMPLATE_NAME)
  private String teamTemplateName;

  public TeamTemplateDetailVO() {
  }

  public TeamTemplateDetailVO teamTeampleItem(List<TeamTemplateItemVO> teamTeampleItem) {
    this.teamTeampleItem = teamTeampleItem;
    return this;
  }

  public TeamTemplateDetailVO addTeamTeampleItemItem(TeamTemplateItemVO teamTeampleItemItem) {
    if (this.teamTeampleItem == null) {
      this.teamTeampleItem = new ArrayList<>();
    }
    this.teamTeampleItem.add(teamTeampleItemItem);
    return this;
  }

  /**
   * 
   * @return teamTeampleItem
   */
  @javax.annotation.Nullable
  public List<TeamTemplateItemVO> getTeamTeampleItem() {
    return teamTeampleItem;
  }

  public void setTeamTeampleItem(List<TeamTemplateItemVO> teamTeampleItem) {
    this.teamTeampleItem = teamTeampleItem;
  }


  public TeamTemplateDetailVO teamTemplateId(Long teamTemplateId) {
    this.teamTemplateId = teamTemplateId;
    return this;
  }

  /**
   * 
   * @return teamTemplateId
   */
  @javax.annotation.Nullable
  public Long getTeamTemplateId() {
    return teamTemplateId;
  }

  public void setTeamTemplateId(Long teamTemplateId) {
    this.teamTemplateId = teamTemplateId;
  }


  public TeamTemplateDetailVO teamTemplateName(String teamTemplateName) {
    this.teamTemplateName = teamTemplateName;
    return this;
  }

  /**
   * 
   * @return teamTemplateName
   */
  @javax.annotation.Nullable
  public String getTeamTemplateName() {
    return teamTemplateName;
  }

  public void setTeamTemplateName(String teamTemplateName) {
    this.teamTemplateName = teamTemplateName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TeamTemplateDetailVO teamTemplateDetailVO = (TeamTemplateDetailVO) o;
    return Objects.equals(this.teamTeampleItem, teamTemplateDetailVO.teamTeampleItem) &&
        Objects.equals(this.teamTemplateId, teamTemplateDetailVO.teamTemplateId) &&
        Objects.equals(this.teamTemplateName, teamTemplateDetailVO.teamTemplateName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(teamTeampleItem, teamTemplateId, teamTemplateName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TeamTemplateDetailVO {\n");
    sb.append("    teamTeampleItem: ").append(toIndentedString(teamTeampleItem)).append("\n");
    sb.append("    teamTemplateId: ").append(toIndentedString(teamTemplateId)).append("\n");
    sb.append("    teamTemplateName: ").append(toIndentedString(teamTemplateName)).append("\n");
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
    openapiFields.add("team_teample_item");
    openapiFields.add("team_template_id");
    openapiFields.add("team_template_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TeamTemplateDetailVO
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TeamTemplateDetailVO.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TeamTemplateDetailVO is not found in the empty JSON string", TeamTemplateDetailVO.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TeamTemplateDetailVO.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TeamTemplateDetailVO` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("team_teample_item") != null && !jsonObj.get("team_teample_item").isJsonNull()) {
        JsonArray jsonArrayteamTeampleItem = jsonObj.getAsJsonArray("team_teample_item");
        if (jsonArrayteamTeampleItem != null) {
          // ensure the json data is an array
          if (!jsonObj.get("team_teample_item").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `team_teample_item` to be an array in the JSON string but got `%s`", jsonObj.get("team_teample_item").toString()));
          }

          // validate the optional field `team_teample_item` (array)
          for (int i = 0; i < jsonArrayteamTeampleItem.size(); i++) {
            TeamTemplateItemVO.validateJsonElement(jsonArrayteamTeampleItem.get(i));
          };
        }
      }
      if ((jsonObj.get("team_template_name") != null && !jsonObj.get("team_template_name").isJsonNull()) && !jsonObj.get("team_template_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `team_template_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("team_template_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TeamTemplateDetailVO.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TeamTemplateDetailVO' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TeamTemplateDetailVO> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TeamTemplateDetailVO.class));

       return (TypeAdapter<T>) new TypeAdapter<TeamTemplateDetailVO>() {
           @Override
           public void write(JsonWriter out, TeamTemplateDetailVO value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TeamTemplateDetailVO read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TeamTemplateDetailVO given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TeamTemplateDetailVO
   * @throws IOException if the JSON string is invalid with respect to TeamTemplateDetailVO
   */
  public static TeamTemplateDetailVO fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TeamTemplateDetailVO.class);
  }

  /**
   * Convert an instance of TeamTemplateDetailVO to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

