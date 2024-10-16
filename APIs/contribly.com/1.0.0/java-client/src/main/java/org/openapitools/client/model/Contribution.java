/*
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Assignment;
import org.openapitools.client.model.MediaUsage;
import org.openapitools.client.model.ModerationHistoryItem;
import org.openapitools.client.model.Place;
import org.openapitools.client.model.Via;

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
 * Contribution
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:26.140477-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Contribution {
  public static final String SERIALIZED_NAME_ASSIGNMENT = "assignment";
  @SerializedName(SERIALIZED_NAME_ASSIGNMENT)
  private Assignment assignment;

  public static final String SERIALIZED_NAME_ATTRIBUTION = "attribution";
  @SerializedName(SERIALIZED_NAME_ATTRIBUTION)
  private String attribution;

  public static final String SERIALIZED_NAME_BODY = "body";
  @SerializedName(SERIALIZED_NAME_BODY)
  private String body;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private OffsetDateTime created;

  public static final String SERIALIZED_NAME_HEADLINE = "headline";
  @SerializedName(SERIALIZED_NAME_HEADLINE)
  private String headline;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MEDIA_USAGES = "mediaUsages";
  @SerializedName(SERIALIZED_NAME_MEDIA_USAGES)
  private List<MediaUsage> mediaUsages = new ArrayList<>();

  public static final String SERIALIZED_NAME_MODERATION_HISTORY = "moderationHistory";
  @SerializedName(SERIALIZED_NAME_MODERATION_HISTORY)
  private List<ModerationHistoryItem> moderationHistory = new ArrayList<>();

  public static final String SERIALIZED_NAME_PLACE = "place";
  @SerializedName(SERIALIZED_NAME_PLACE)
  private Place place;

  public static final String SERIALIZED_NAME_URL_WORDS = "urlWords";
  @SerializedName(SERIALIZED_NAME_URL_WORDS)
  private String urlWords;

  public static final String SERIALIZED_NAME_VIA = "via";
  @SerializedName(SERIALIZED_NAME_VIA)
  private Via via;

  public Contribution() {
  }

  public Contribution assignment(Assignment assignment) {
    this.assignment = assignment;
    return this;
  }

  /**
   * Get assignment
   * @return assignment
   */
  @javax.annotation.Nullable
  public Assignment getAssignment() {
    return assignment;
  }

  public void setAssignment(Assignment assignment) {
    this.assignment = assignment;
  }


  public Contribution attribution(String attribution) {
    this.attribution = attribution;
    return this;
  }

  /**
   * The public attribution for this contribution. This will be the display name of the registered user or the contributor&#39;s first and last name if they provided them while making a non authenticated contribution. A blank attribution field indicates and anonymous contribution.
   * @return attribution
   */
  @javax.annotation.Nullable
  public String getAttribution() {
    return attribution;
  }

  public void setAttribution(String attribution) {
    this.attribution = attribution;
  }


  public Contribution body(String body) {
    this.body = body;
    return this;
  }

  /**
   * Get body
   * @return body
   */
  @javax.annotation.Nullable
  public String getBody() {
    return body;
  }

  public void setBody(String body) {
    this.body = body;
  }


  public Contribution created(OffsetDateTime created) {
    this.created = created;
    return this;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreated() {
    return created;
  }

  public void setCreated(OffsetDateTime created) {
    this.created = created;
  }


  public Contribution headline(String headline) {
    this.headline = headline;
    return this;
  }

  /**
   * Get headline
   * @return headline
   */
  @javax.annotation.Nullable
  public String getHeadline() {
    return headline;
  }

  public void setHeadline(String headline) {
    this.headline = headline;
  }


  public Contribution id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Contribution mediaUsages(List<MediaUsage> mediaUsages) {
    this.mediaUsages = mediaUsages;
    return this;
  }

  public Contribution addMediaUsagesItem(MediaUsage mediaUsagesItem) {
    if (this.mediaUsages == null) {
      this.mediaUsages = new ArrayList<>();
    }
    this.mediaUsages.add(mediaUsagesItem);
    return this;
  }

  /**
   * Get mediaUsages
   * @return mediaUsages
   */
  @javax.annotation.Nullable
  public List<MediaUsage> getMediaUsages() {
    return mediaUsages;
  }

  public void setMediaUsages(List<MediaUsage> mediaUsages) {
    this.mediaUsages = mediaUsages;
  }


  public Contribution moderationHistory(List<ModerationHistoryItem> moderationHistory) {
    this.moderationHistory = moderationHistory;
    return this;
  }

  public Contribution addModerationHistoryItem(ModerationHistoryItem moderationHistoryItem) {
    if (this.moderationHistory == null) {
      this.moderationHistory = new ArrayList<>();
    }
    this.moderationHistory.add(moderationHistoryItem);
    return this;
  }

  /**
   * Get moderationHistory
   * @return moderationHistory
   */
  @javax.annotation.Nullable
  public List<ModerationHistoryItem> getModerationHistory() {
    return moderationHistory;
  }

  public void setModerationHistory(List<ModerationHistoryItem> moderationHistory) {
    this.moderationHistory = moderationHistory;
  }


  public Contribution place(Place place) {
    this.place = place;
    return this;
  }

  /**
   * Get place
   * @return place
   */
  @javax.annotation.Nullable
  public Place getPlace() {
    return place;
  }

  public void setPlace(Place place) {
    this.place = place;
  }


  public Contribution urlWords(String urlWords) {
    this.urlWords = urlWords;
    return this;
  }

  /**
   * Get urlWords
   * @return urlWords
   */
  @javax.annotation.Nullable
  public String getUrlWords() {
    return urlWords;
  }

  public void setUrlWords(String urlWords) {
    this.urlWords = urlWords;
  }


  public Contribution via(Via via) {
    this.via = via;
    return this;
  }

  /**
   * Get via
   * @return via
   */
  @javax.annotation.Nullable
  public Via getVia() {
    return via;
  }

  public void setVia(Via via) {
    this.via = via;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Contribution contribution = (Contribution) o;
    return Objects.equals(this.assignment, contribution.assignment) &&
        Objects.equals(this.attribution, contribution.attribution) &&
        Objects.equals(this.body, contribution.body) &&
        Objects.equals(this.created, contribution.created) &&
        Objects.equals(this.headline, contribution.headline) &&
        Objects.equals(this.id, contribution.id) &&
        Objects.equals(this.mediaUsages, contribution.mediaUsages) &&
        Objects.equals(this.moderationHistory, contribution.moderationHistory) &&
        Objects.equals(this.place, contribution.place) &&
        Objects.equals(this.urlWords, contribution.urlWords) &&
        Objects.equals(this.via, contribution.via);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assignment, attribution, body, created, headline, id, mediaUsages, moderationHistory, place, urlWords, via);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Contribution {\n");
    sb.append("    assignment: ").append(toIndentedString(assignment)).append("\n");
    sb.append("    attribution: ").append(toIndentedString(attribution)).append("\n");
    sb.append("    body: ").append(toIndentedString(body)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    headline: ").append(toIndentedString(headline)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    mediaUsages: ").append(toIndentedString(mediaUsages)).append("\n");
    sb.append("    moderationHistory: ").append(toIndentedString(moderationHistory)).append("\n");
    sb.append("    place: ").append(toIndentedString(place)).append("\n");
    sb.append("    urlWords: ").append(toIndentedString(urlWords)).append("\n");
    sb.append("    via: ").append(toIndentedString(via)).append("\n");
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
    openapiFields.add("assignment");
    openapiFields.add("attribution");
    openapiFields.add("body");
    openapiFields.add("created");
    openapiFields.add("headline");
    openapiFields.add("id");
    openapiFields.add("mediaUsages");
    openapiFields.add("moderationHistory");
    openapiFields.add("place");
    openapiFields.add("urlWords");
    openapiFields.add("via");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Contribution
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Contribution.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Contribution is not found in the empty JSON string", Contribution.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Contribution.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Contribution` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `assignment`
      if (jsonObj.get("assignment") != null && !jsonObj.get("assignment").isJsonNull()) {
        Assignment.validateJsonElement(jsonObj.get("assignment"));
      }
      if ((jsonObj.get("attribution") != null && !jsonObj.get("attribution").isJsonNull()) && !jsonObj.get("attribution").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `attribution` to be a primitive type in the JSON string but got `%s`", jsonObj.get("attribution").toString()));
      }
      if ((jsonObj.get("body") != null && !jsonObj.get("body").isJsonNull()) && !jsonObj.get("body").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `body` to be a primitive type in the JSON string but got `%s`", jsonObj.get("body").toString()));
      }
      if ((jsonObj.get("headline") != null && !jsonObj.get("headline").isJsonNull()) && !jsonObj.get("headline").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `headline` to be a primitive type in the JSON string but got `%s`", jsonObj.get("headline").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("mediaUsages") != null && !jsonObj.get("mediaUsages").isJsonNull()) {
        JsonArray jsonArraymediaUsages = jsonObj.getAsJsonArray("mediaUsages");
        if (jsonArraymediaUsages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("mediaUsages").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `mediaUsages` to be an array in the JSON string but got `%s`", jsonObj.get("mediaUsages").toString()));
          }

          // validate the optional field `mediaUsages` (array)
          for (int i = 0; i < jsonArraymediaUsages.size(); i++) {
            MediaUsage.validateJsonElement(jsonArraymediaUsages.get(i));
          };
        }
      }
      if (jsonObj.get("moderationHistory") != null && !jsonObj.get("moderationHistory").isJsonNull()) {
        JsonArray jsonArraymoderationHistory = jsonObj.getAsJsonArray("moderationHistory");
        if (jsonArraymoderationHistory != null) {
          // ensure the json data is an array
          if (!jsonObj.get("moderationHistory").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `moderationHistory` to be an array in the JSON string but got `%s`", jsonObj.get("moderationHistory").toString()));
          }

          // validate the optional field `moderationHistory` (array)
          for (int i = 0; i < jsonArraymoderationHistory.size(); i++) {
            ModerationHistoryItem.validateJsonElement(jsonArraymoderationHistory.get(i));
          };
        }
      }
      // validate the optional field `place`
      if (jsonObj.get("place") != null && !jsonObj.get("place").isJsonNull()) {
        Place.validateJsonElement(jsonObj.get("place"));
      }
      if ((jsonObj.get("urlWords") != null && !jsonObj.get("urlWords").isJsonNull()) && !jsonObj.get("urlWords").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `urlWords` to be a primitive type in the JSON string but got `%s`", jsonObj.get("urlWords").toString()));
      }
      // validate the optional field `via`
      if (jsonObj.get("via") != null && !jsonObj.get("via").isJsonNull()) {
        Via.validateJsonElement(jsonObj.get("via"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Contribution.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Contribution' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Contribution> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Contribution.class));

       return (TypeAdapter<T>) new TypeAdapter<Contribution>() {
           @Override
           public void write(JsonWriter out, Contribution value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Contribution read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Contribution given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Contribution
   * @throws IOException if the JSON string is invalid with respect to Contribution
   */
  public static Contribution fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Contribution.class);
  }

  /**
   * Convert an instance of Contribution to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

