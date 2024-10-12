/*
 * NFL v3 RotoBaller Premium News
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
 * News
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:24.952302-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class News {
  public static final String SERIALIZED_NAME_AUTHOR = "Author";
  @SerializedName(SERIALIZED_NAME_AUTHOR)
  private String author;

  public static final String SERIALIZED_NAME_CATEGORIES = "Categories";
  @SerializedName(SERIALIZED_NAME_CATEGORIES)
  private String categories;

  public static final String SERIALIZED_NAME_CONTENT = "Content";
  @SerializedName(SERIALIZED_NAME_CONTENT)
  private String content;

  public static final String SERIALIZED_NAME_NEWS_I_D = "NewsID";
  @SerializedName(SERIALIZED_NAME_NEWS_I_D)
  private Integer newsID;

  public static final String SERIALIZED_NAME_ORIGINAL_SOURCE = "OriginalSource";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_SOURCE)
  private String originalSource;

  public static final String SERIALIZED_NAME_ORIGINAL_SOURCE_URL = "OriginalSourceUrl";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_SOURCE_URL)
  private String originalSourceUrl;

  public static final String SERIALIZED_NAME_PLAYER_I_D = "PlayerID";
  @SerializedName(SERIALIZED_NAME_PLAYER_I_D)
  private Integer playerID;

  public static final String SERIALIZED_NAME_PLAYER_I_D2 = "PlayerID2";
  @SerializedName(SERIALIZED_NAME_PLAYER_I_D2)
  private Integer playerID2;

  public static final String SERIALIZED_NAME_SOURCE = "Source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public static final String SERIALIZED_NAME_TEAM = "Team";
  @SerializedName(SERIALIZED_NAME_TEAM)
  private String team;

  public static final String SERIALIZED_NAME_TEAM2 = "Team2";
  @SerializedName(SERIALIZED_NAME_TEAM2)
  private String team2;

  public static final String SERIALIZED_NAME_TEAM_I_D = "TeamID";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D)
  private Integer teamID;

  public static final String SERIALIZED_NAME_TEAM_I_D2 = "TeamID2";
  @SerializedName(SERIALIZED_NAME_TEAM_I_D2)
  private Integer teamID2;

  public static final String SERIALIZED_NAME_TERMS_OF_USE = "TermsOfUse";
  @SerializedName(SERIALIZED_NAME_TERMS_OF_USE)
  private String termsOfUse;

  public static final String SERIALIZED_NAME_TIME_AGO = "TimeAgo";
  @SerializedName(SERIALIZED_NAME_TIME_AGO)
  private String timeAgo;

  public static final String SERIALIZED_NAME_TITLE = "Title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATED = "Updated";
  @SerializedName(SERIALIZED_NAME_UPDATED)
  private String updated;

  public static final String SERIALIZED_NAME_URL = "Url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public News() {
  }

  public News author(String author) {
    this.author = author;
    return this;
  }

  /**
   * Get author
   * @return author
   */
  @javax.annotation.Nullable
  public String getAuthor() {
    return author;
  }

  public void setAuthor(String author) {
    this.author = author;
  }


  public News categories(String categories) {
    this.categories = categories;
    return this;
  }

  /**
   * Get categories
   * @return categories
   */
  @javax.annotation.Nullable
  public String getCategories() {
    return categories;
  }

  public void setCategories(String categories) {
    this.categories = categories;
  }


  public News content(String content) {
    this.content = content;
    return this;
  }

  /**
   * Get content
   * @return content
   */
  @javax.annotation.Nullable
  public String getContent() {
    return content;
  }

  public void setContent(String content) {
    this.content = content;
  }


  public News newsID(Integer newsID) {
    this.newsID = newsID;
    return this;
  }

  /**
   * Get newsID
   * @return newsID
   */
  @javax.annotation.Nullable
  public Integer getNewsID() {
    return newsID;
  }

  public void setNewsID(Integer newsID) {
    this.newsID = newsID;
  }


  public News originalSource(String originalSource) {
    this.originalSource = originalSource;
    return this;
  }

  /**
   * Get originalSource
   * @return originalSource
   */
  @javax.annotation.Nullable
  public String getOriginalSource() {
    return originalSource;
  }

  public void setOriginalSource(String originalSource) {
    this.originalSource = originalSource;
  }


  public News originalSourceUrl(String originalSourceUrl) {
    this.originalSourceUrl = originalSourceUrl;
    return this;
  }

  /**
   * Get originalSourceUrl
   * @return originalSourceUrl
   */
  @javax.annotation.Nullable
  public String getOriginalSourceUrl() {
    return originalSourceUrl;
  }

  public void setOriginalSourceUrl(String originalSourceUrl) {
    this.originalSourceUrl = originalSourceUrl;
  }


  public News playerID(Integer playerID) {
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


  public News playerID2(Integer playerID2) {
    this.playerID2 = playerID2;
    return this;
  }

  /**
   * Get playerID2
   * @return playerID2
   */
  @javax.annotation.Nullable
  public Integer getPlayerID2() {
    return playerID2;
  }

  public void setPlayerID2(Integer playerID2) {
    this.playerID2 = playerID2;
  }


  public News source(String source) {
    this.source = source;
    return this;
  }

  /**
   * Get source
   * @return source
   */
  @javax.annotation.Nullable
  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }


  public News team(String team) {
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


  public News team2(String team2) {
    this.team2 = team2;
    return this;
  }

  /**
   * Get team2
   * @return team2
   */
  @javax.annotation.Nullable
  public String getTeam2() {
    return team2;
  }

  public void setTeam2(String team2) {
    this.team2 = team2;
  }


  public News teamID(Integer teamID) {
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


  public News teamID2(Integer teamID2) {
    this.teamID2 = teamID2;
    return this;
  }

  /**
   * Get teamID2
   * @return teamID2
   */
  @javax.annotation.Nullable
  public Integer getTeamID2() {
    return teamID2;
  }

  public void setTeamID2(Integer teamID2) {
    this.teamID2 = teamID2;
  }


  public News termsOfUse(String termsOfUse) {
    this.termsOfUse = termsOfUse;
    return this;
  }

  /**
   * Get termsOfUse
   * @return termsOfUse
   */
  @javax.annotation.Nullable
  public String getTermsOfUse() {
    return termsOfUse;
  }

  public void setTermsOfUse(String termsOfUse) {
    this.termsOfUse = termsOfUse;
  }


  public News timeAgo(String timeAgo) {
    this.timeAgo = timeAgo;
    return this;
  }

  /**
   * Get timeAgo
   * @return timeAgo
   */
  @javax.annotation.Nullable
  public String getTimeAgo() {
    return timeAgo;
  }

  public void setTimeAgo(String timeAgo) {
    this.timeAgo = timeAgo;
  }


  public News title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public News updated(String updated) {
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


  public News url(String url) {
    this.url = url;
    return this;
  }

  /**
   * Get url
   * @return url
   */
  @javax.annotation.Nullable
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    News news = (News) o;
    return Objects.equals(this.author, news.author) &&
        Objects.equals(this.categories, news.categories) &&
        Objects.equals(this.content, news.content) &&
        Objects.equals(this.newsID, news.newsID) &&
        Objects.equals(this.originalSource, news.originalSource) &&
        Objects.equals(this.originalSourceUrl, news.originalSourceUrl) &&
        Objects.equals(this.playerID, news.playerID) &&
        Objects.equals(this.playerID2, news.playerID2) &&
        Objects.equals(this.source, news.source) &&
        Objects.equals(this.team, news.team) &&
        Objects.equals(this.team2, news.team2) &&
        Objects.equals(this.teamID, news.teamID) &&
        Objects.equals(this.teamID2, news.teamID2) &&
        Objects.equals(this.termsOfUse, news.termsOfUse) &&
        Objects.equals(this.timeAgo, news.timeAgo) &&
        Objects.equals(this.title, news.title) &&
        Objects.equals(this.updated, news.updated) &&
        Objects.equals(this.url, news.url);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(author, categories, content, newsID, originalSource, originalSourceUrl, playerID, playerID2, source, team, team2, teamID, teamID2, termsOfUse, timeAgo, title, updated, url);
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
    sb.append("class News {\n");
    sb.append("    author: ").append(toIndentedString(author)).append("\n");
    sb.append("    categories: ").append(toIndentedString(categories)).append("\n");
    sb.append("    content: ").append(toIndentedString(content)).append("\n");
    sb.append("    newsID: ").append(toIndentedString(newsID)).append("\n");
    sb.append("    originalSource: ").append(toIndentedString(originalSource)).append("\n");
    sb.append("    originalSourceUrl: ").append(toIndentedString(originalSourceUrl)).append("\n");
    sb.append("    playerID: ").append(toIndentedString(playerID)).append("\n");
    sb.append("    playerID2: ").append(toIndentedString(playerID2)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    team: ").append(toIndentedString(team)).append("\n");
    sb.append("    team2: ").append(toIndentedString(team2)).append("\n");
    sb.append("    teamID: ").append(toIndentedString(teamID)).append("\n");
    sb.append("    teamID2: ").append(toIndentedString(teamID2)).append("\n");
    sb.append("    termsOfUse: ").append(toIndentedString(termsOfUse)).append("\n");
    sb.append("    timeAgo: ").append(toIndentedString(timeAgo)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updated: ").append(toIndentedString(updated)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("Author");
    openapiFields.add("Categories");
    openapiFields.add("Content");
    openapiFields.add("NewsID");
    openapiFields.add("OriginalSource");
    openapiFields.add("OriginalSourceUrl");
    openapiFields.add("PlayerID");
    openapiFields.add("PlayerID2");
    openapiFields.add("Source");
    openapiFields.add("Team");
    openapiFields.add("Team2");
    openapiFields.add("TeamID");
    openapiFields.add("TeamID2");
    openapiFields.add("TermsOfUse");
    openapiFields.add("TimeAgo");
    openapiFields.add("Title");
    openapiFields.add("Updated");
    openapiFields.add("Url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to News
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!News.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in News is not found in the empty JSON string", News.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!News.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `News` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Author") != null && !jsonObj.get("Author").isJsonNull()) && !jsonObj.get("Author").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Author` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Author").toString()));
      }
      if ((jsonObj.get("Categories") != null && !jsonObj.get("Categories").isJsonNull()) && !jsonObj.get("Categories").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Categories` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Categories").toString()));
      }
      if ((jsonObj.get("Content") != null && !jsonObj.get("Content").isJsonNull()) && !jsonObj.get("Content").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Content` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Content").toString()));
      }
      if ((jsonObj.get("OriginalSource") != null && !jsonObj.get("OriginalSource").isJsonNull()) && !jsonObj.get("OriginalSource").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OriginalSource` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OriginalSource").toString()));
      }
      if ((jsonObj.get("OriginalSourceUrl") != null && !jsonObj.get("OriginalSourceUrl").isJsonNull()) && !jsonObj.get("OriginalSourceUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `OriginalSourceUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("OriginalSourceUrl").toString()));
      }
      if ((jsonObj.get("Source") != null && !jsonObj.get("Source").isJsonNull()) && !jsonObj.get("Source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Source").toString()));
      }
      if ((jsonObj.get("Team") != null && !jsonObj.get("Team").isJsonNull()) && !jsonObj.get("Team").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Team` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Team").toString()));
      }
      if ((jsonObj.get("Team2") != null && !jsonObj.get("Team2").isJsonNull()) && !jsonObj.get("Team2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Team2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Team2").toString()));
      }
      if ((jsonObj.get("TermsOfUse") != null && !jsonObj.get("TermsOfUse").isJsonNull()) && !jsonObj.get("TermsOfUse").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TermsOfUse` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TermsOfUse").toString()));
      }
      if ((jsonObj.get("TimeAgo") != null && !jsonObj.get("TimeAgo").isJsonNull()) && !jsonObj.get("TimeAgo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `TimeAgo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("TimeAgo").toString()));
      }
      if ((jsonObj.get("Title") != null && !jsonObj.get("Title").isJsonNull()) && !jsonObj.get("Title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Title").toString()));
      }
      if ((jsonObj.get("Updated") != null && !jsonObj.get("Updated").isJsonNull()) && !jsonObj.get("Updated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Updated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Updated").toString()));
      }
      if ((jsonObj.get("Url") != null && !jsonObj.get("Url").isJsonNull()) && !jsonObj.get("Url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!News.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'News' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<News> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(News.class));

       return (TypeAdapter<T>) new TypeAdapter<News>() {
           @Override
           public void write(JsonWriter out, News value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public News read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of News given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of News
   * @throws IOException if the JSON string is invalid with respect to News
   */
  public static News fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, News.class);
  }

  /**
   * Convert an instance of News to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

