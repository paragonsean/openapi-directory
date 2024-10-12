/*
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
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
 * Represents the relationship between accounts, such as following / blocking / muting / etc.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:57.300255-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Relationship {
  public static final String SERIALIZED_NAME_BLOCKED_BY = "blocked_by";
  @SerializedName(SERIALIZED_NAME_BLOCKED_BY)
  private Boolean blockedBy;

  public static final String SERIALIZED_NAME_BLOCKING = "blocking";
  @SerializedName(SERIALIZED_NAME_BLOCKING)
  private Boolean blocking;

  public static final String SERIALIZED_NAME_DOMAIN_BLOCKING = "domain_blocking";
  @SerializedName(SERIALIZED_NAME_DOMAIN_BLOCKING)
  private Boolean domainBlocking;

  public static final String SERIALIZED_NAME_ENDORSED = "endorsed";
  @SerializedName(SERIALIZED_NAME_ENDORSED)
  private Boolean endorsed;

  public static final String SERIALIZED_NAME_FOLLOWED_BY = "followed_by";
  @SerializedName(SERIALIZED_NAME_FOLLOWED_BY)
  private Boolean followedBy;

  public static final String SERIALIZED_NAME_FOLLOWING = "following";
  @SerializedName(SERIALIZED_NAME_FOLLOWING)
  private Boolean following;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MUTING = "muting";
  @SerializedName(SERIALIZED_NAME_MUTING)
  private Boolean muting;

  public static final String SERIALIZED_NAME_MUTING_NOTIFICATIONS = "muting_notifications";
  @SerializedName(SERIALIZED_NAME_MUTING_NOTIFICATIONS)
  private Boolean mutingNotifications;

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public static final String SERIALIZED_NAME_NOTIFYING = "notifying";
  @SerializedName(SERIALIZED_NAME_NOTIFYING)
  private Boolean notifying;

  public static final String SERIALIZED_NAME_REQUESTED = "requested";
  @SerializedName(SERIALIZED_NAME_REQUESTED)
  private Boolean requested;

  public static final String SERIALIZED_NAME_SHOWING_REBLOGS = "showing_reblogs";
  @SerializedName(SERIALIZED_NAME_SHOWING_REBLOGS)
  private Boolean showingReblogs;

  public Relationship() {
  }

  public Relationship blockedBy(Boolean blockedBy) {
    this.blockedBy = blockedBy;
    return this;
  }

  /**
   * Is this user blocking you?
   * @return blockedBy
   */
  @javax.annotation.Nonnull
  public Boolean getBlockedBy() {
    return blockedBy;
  }

  public void setBlockedBy(Boolean blockedBy) {
    this.blockedBy = blockedBy;
  }


  public Relationship blocking(Boolean blocking) {
    this.blocking = blocking;
    return this;
  }

  /**
   * Are you blocking this user?
   * @return blocking
   */
  @javax.annotation.Nonnull
  public Boolean getBlocking() {
    return blocking;
  }

  public void setBlocking(Boolean blocking) {
    this.blocking = blocking;
  }


  public Relationship domainBlocking(Boolean domainBlocking) {
    this.domainBlocking = domainBlocking;
    return this;
  }

  /**
   * Are you blocking this user&#39;s domain?
   * @return domainBlocking
   */
  @javax.annotation.Nonnull
  public Boolean getDomainBlocking() {
    return domainBlocking;
  }

  public void setDomainBlocking(Boolean domainBlocking) {
    this.domainBlocking = domainBlocking;
  }


  public Relationship endorsed(Boolean endorsed) {
    this.endorsed = endorsed;
    return this;
  }

  /**
   * Are you featuring this user on your profile?
   * @return endorsed
   */
  @javax.annotation.Nonnull
  public Boolean getEndorsed() {
    return endorsed;
  }

  public void setEndorsed(Boolean endorsed) {
    this.endorsed = endorsed;
  }


  public Relationship followedBy(Boolean followedBy) {
    this.followedBy = followedBy;
    return this;
  }

  /**
   * Are you followed by this user?
   * @return followedBy
   */
  @javax.annotation.Nonnull
  public Boolean getFollowedBy() {
    return followedBy;
  }

  public void setFollowedBy(Boolean followedBy) {
    this.followedBy = followedBy;
  }


  public Relationship following(Boolean following) {
    this.following = following;
    return this;
  }

  /**
   * Are you following this user?
   * @return following
   */
  @javax.annotation.Nonnull
  public Boolean getFollowing() {
    return following;
  }

  public void setFollowing(Boolean following) {
    this.following = following;
  }


  public Relationship id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The account id. Cast from an integer, but not guaranteed to be a number.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Relationship muting(Boolean muting) {
    this.muting = muting;
    return this;
  }

  /**
   * Are you muting this user?
   * @return muting
   */
  @javax.annotation.Nonnull
  public Boolean getMuting() {
    return muting;
  }

  public void setMuting(Boolean muting) {
    this.muting = muting;
  }


  public Relationship mutingNotifications(Boolean mutingNotifications) {
    this.mutingNotifications = mutingNotifications;
    return this;
  }

  /**
   * Are you muting notifications from this user?
   * @return mutingNotifications
   */
  @javax.annotation.Nonnull
  public Boolean getMutingNotifications() {
    return mutingNotifications;
  }

  public void setMutingNotifications(Boolean mutingNotifications) {
    this.mutingNotifications = mutingNotifications;
  }


  public Relationship note(String note) {
    this.note = note;
    return this;
  }

  /**
   * This user&#39;s profile bio
   * @return note
   */
  @javax.annotation.Nonnull
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }


  public Relationship notifying(Boolean notifying) {
    this.notifying = notifying;
    return this;
  }

  /**
   * Have you enabled notifications for this user?
   * @return notifying
   */
  @javax.annotation.Nonnull
  public Boolean getNotifying() {
    return notifying;
  }

  public void setNotifying(Boolean notifying) {
    this.notifying = notifying;
  }


  public Relationship requested(Boolean requested) {
    this.requested = requested;
    return this;
  }

  /**
   * Do you have a pending follow request for this user?
   * @return requested
   */
  @javax.annotation.Nonnull
  public Boolean getRequested() {
    return requested;
  }

  public void setRequested(Boolean requested) {
    this.requested = requested;
  }


  public Relationship showingReblogs(Boolean showingReblogs) {
    this.showingReblogs = showingReblogs;
    return this;
  }

  /**
   * Are you receiving this user&#39;s boosts in your home timeline?
   * @return showingReblogs
   */
  @javax.annotation.Nonnull
  public Boolean getShowingReblogs() {
    return showingReblogs;
  }

  public void setShowingReblogs(Boolean showingReblogs) {
    this.showingReblogs = showingReblogs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Relationship relationship = (Relationship) o;
    return Objects.equals(this.blockedBy, relationship.blockedBy) &&
        Objects.equals(this.blocking, relationship.blocking) &&
        Objects.equals(this.domainBlocking, relationship.domainBlocking) &&
        Objects.equals(this.endorsed, relationship.endorsed) &&
        Objects.equals(this.followedBy, relationship.followedBy) &&
        Objects.equals(this.following, relationship.following) &&
        Objects.equals(this.id, relationship.id) &&
        Objects.equals(this.muting, relationship.muting) &&
        Objects.equals(this.mutingNotifications, relationship.mutingNotifications) &&
        Objects.equals(this.note, relationship.note) &&
        Objects.equals(this.notifying, relationship.notifying) &&
        Objects.equals(this.requested, relationship.requested) &&
        Objects.equals(this.showingReblogs, relationship.showingReblogs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(blockedBy, blocking, domainBlocking, endorsed, followedBy, following, id, muting, mutingNotifications, note, notifying, requested, showingReblogs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Relationship {\n");
    sb.append("    blockedBy: ").append(toIndentedString(blockedBy)).append("\n");
    sb.append("    blocking: ").append(toIndentedString(blocking)).append("\n");
    sb.append("    domainBlocking: ").append(toIndentedString(domainBlocking)).append("\n");
    sb.append("    endorsed: ").append(toIndentedString(endorsed)).append("\n");
    sb.append("    followedBy: ").append(toIndentedString(followedBy)).append("\n");
    sb.append("    following: ").append(toIndentedString(following)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    muting: ").append(toIndentedString(muting)).append("\n");
    sb.append("    mutingNotifications: ").append(toIndentedString(mutingNotifications)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
    sb.append("    notifying: ").append(toIndentedString(notifying)).append("\n");
    sb.append("    requested: ").append(toIndentedString(requested)).append("\n");
    sb.append("    showingReblogs: ").append(toIndentedString(showingReblogs)).append("\n");
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
    openapiFields.add("blocked_by");
    openapiFields.add("blocking");
    openapiFields.add("domain_blocking");
    openapiFields.add("endorsed");
    openapiFields.add("followed_by");
    openapiFields.add("following");
    openapiFields.add("id");
    openapiFields.add("muting");
    openapiFields.add("muting_notifications");
    openapiFields.add("note");
    openapiFields.add("notifying");
    openapiFields.add("requested");
    openapiFields.add("showing_reblogs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("blocked_by");
    openapiRequiredFields.add("blocking");
    openapiRequiredFields.add("domain_blocking");
    openapiRequiredFields.add("endorsed");
    openapiRequiredFields.add("followed_by");
    openapiRequiredFields.add("following");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("muting");
    openapiRequiredFields.add("muting_notifications");
    openapiRequiredFields.add("note");
    openapiRequiredFields.add("notifying");
    openapiRequiredFields.add("requested");
    openapiRequiredFields.add("showing_reblogs");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Relationship
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Relationship.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Relationship is not found in the empty JSON string", Relationship.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Relationship.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Relationship` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Relationship.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Relationship.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Relationship' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Relationship> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Relationship.class));

       return (TypeAdapter<T>) new TypeAdapter<Relationship>() {
           @Override
           public void write(JsonWriter out, Relationship value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Relationship read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Relationship given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Relationship
   * @throws IOException if the JSON string is invalid with respect to Relationship
   */
  public static Relationship fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Relationship.class);
  }

  /**
   * Convert an instance of Relationship to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

