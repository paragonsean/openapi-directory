/*
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
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
import org.openapitools.client.model.ProfilesInnerCounts;
import org.openapitools.client.model.ProfilesInnerSchedulesInner;
import org.openapitools.client.model.ProfilesInnerShortener;
import org.openapitools.client.model.ProfilesInnerStatistics;

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
 * ProfilesInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:44.110075-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProfilesInner {
  public static final String SERIALIZED_NAME_ID = "_id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_AVATAR = "avatar";
  @SerializedName(SERIALIZED_NAME_AVATAR)
  private String avatar;

  public static final String SERIALIZED_NAME_AVATAR_HTTPS = "avatar_https";
  @SerializedName(SERIALIZED_NAME_AVATAR_HTTPS)
  private String avatarHttps;

  public static final String SERIALIZED_NAME_COUNTS = "counts";
  @SerializedName(SERIALIZED_NAME_COUNTS)
  private ProfilesInnerCounts counts;

  public static final String SERIALIZED_NAME_COVER_PHOTO = "cover_photo";
  @SerializedName(SERIALIZED_NAME_COVER_PHOTO)
  private String coverPhoto;

  public static final String SERIALIZED_NAME_DEFAULT = "default";
  @SerializedName(SERIALIZED_NAME_DEFAULT)
  private Boolean _default;

  public static final String SERIALIZED_NAME_DISABLED_FEATURES = "disabled_features";
  @SerializedName(SERIALIZED_NAME_DISABLED_FEATURES)
  private List<Object> disabledFeatures = new ArrayList<>();

  public static final String SERIALIZED_NAME_DISCONNECTED = "disconnected";
  @SerializedName(SERIALIZED_NAME_DISCONNECTED)
  private String disconnected;

  public static final String SERIALIZED_NAME_FORMATTED_SERVICE = "formatted_service";
  @SerializedName(SERIALIZED_NAME_FORMATTED_SERVICE)
  private String formattedService;

  public static final String SERIALIZED_NAME_FORMATTED_USERNAME = "formatted_username";
  @SerializedName(SERIALIZED_NAME_FORMATTED_USERNAME)
  private String formattedUsername;

  public static final String SERIALIZED_NAME_HAS_USED_SUGGESTIONS = "has_used_suggestions";
  @SerializedName(SERIALIZED_NAME_HAS_USED_SUGGESTIONS)
  private Boolean hasUsedSuggestions;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_SCHEDULES = "schedules";
  @SerializedName(SERIALIZED_NAME_SCHEDULES)
  private List<ProfilesInnerSchedulesInner> schedules = new ArrayList<>();

  public static final String SERIALIZED_NAME_SERVICE = "service";
  @SerializedName(SERIALIZED_NAME_SERVICE)
  private String service;

  public static final String SERIALIZED_NAME_SERVICE_ID = "service_id";
  @SerializedName(SERIALIZED_NAME_SERVICE_ID)
  private String serviceId;

  public static final String SERIALIZED_NAME_SERVICE_TYPE = "service_type";
  @SerializedName(SERIALIZED_NAME_SERVICE_TYPE)
  private String serviceType;

  public static final String SERIALIZED_NAME_SERVICE_USERNAME = "service_username";
  @SerializedName(SERIALIZED_NAME_SERVICE_USERNAME)
  private String serviceUsername;

  public static final String SERIALIZED_NAME_SHORTENER = "shortener";
  @SerializedName(SERIALIZED_NAME_SHORTENER)
  private ProfilesInnerShortener shortener;

  public static final String SERIALIZED_NAME_STATISTICS = "statistics";
  @SerializedName(SERIALIZED_NAME_STATISTICS)
  private ProfilesInnerStatistics statistics;

  public static final String SERIALIZED_NAME_TIMEZONE = "timezone";
  @SerializedName(SERIALIZED_NAME_TIMEZONE)
  private String timezone;

  public static final String SERIALIZED_NAME_USER_ID = "user_id";
  @SerializedName(SERIALIZED_NAME_USER_ID)
  private String userId;

  public static final String SERIALIZED_NAME_UTM_TRACKING = "utm_tracking";
  @SerializedName(SERIALIZED_NAME_UTM_TRACKING)
  private String utmTracking;

  public static final String SERIALIZED_NAME_VERB = "verb";
  @SerializedName(SERIALIZED_NAME_VERB)
  private String verb;

  public ProfilesInner() {
  }

  public ProfilesInner id(String id) {
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


  public ProfilesInner avatar(String avatar) {
    this.avatar = avatar;
    return this;
  }

  /**
   * Get avatar
   * @return avatar
   */
  @javax.annotation.Nullable
  public String getAvatar() {
    return avatar;
  }

  public void setAvatar(String avatar) {
    this.avatar = avatar;
  }


  public ProfilesInner avatarHttps(String avatarHttps) {
    this.avatarHttps = avatarHttps;
    return this;
  }

  /**
   * Get avatarHttps
   * @return avatarHttps
   */
  @javax.annotation.Nullable
  public String getAvatarHttps() {
    return avatarHttps;
  }

  public void setAvatarHttps(String avatarHttps) {
    this.avatarHttps = avatarHttps;
  }


  public ProfilesInner counts(ProfilesInnerCounts counts) {
    this.counts = counts;
    return this;
  }

  /**
   * Get counts
   * @return counts
   */
  @javax.annotation.Nullable
  public ProfilesInnerCounts getCounts() {
    return counts;
  }

  public void setCounts(ProfilesInnerCounts counts) {
    this.counts = counts;
  }


  public ProfilesInner coverPhoto(String coverPhoto) {
    this.coverPhoto = coverPhoto;
    return this;
  }

  /**
   * Get coverPhoto
   * @return coverPhoto
   */
  @javax.annotation.Nullable
  public String getCoverPhoto() {
    return coverPhoto;
  }

  public void setCoverPhoto(String coverPhoto) {
    this.coverPhoto = coverPhoto;
  }


  public ProfilesInner _default(Boolean _default) {
    this._default = _default;
    return this;
  }

  /**
   * Get _default
   * @return _default
   */
  @javax.annotation.Nullable
  public Boolean getDefault() {
    return _default;
  }

  public void setDefault(Boolean _default) {
    this._default = _default;
  }


  public ProfilesInner disabledFeatures(List<Object> disabledFeatures) {
    this.disabledFeatures = disabledFeatures;
    return this;
  }

  public ProfilesInner addDisabledFeaturesItem(Object disabledFeaturesItem) {
    if (this.disabledFeatures == null) {
      this.disabledFeatures = new ArrayList<>();
    }
    this.disabledFeatures.add(disabledFeaturesItem);
    return this;
  }

  /**
   * Get disabledFeatures
   * @return disabledFeatures
   */
  @javax.annotation.Nullable
  public List<Object> getDisabledFeatures() {
    return disabledFeatures;
  }

  public void setDisabledFeatures(List<Object> disabledFeatures) {
    this.disabledFeatures = disabledFeatures;
  }


  public ProfilesInner disconnected(String disconnected) {
    this.disconnected = disconnected;
    return this;
  }

  /**
   * Get disconnected
   * @return disconnected
   */
  @javax.annotation.Nullable
  public String getDisconnected() {
    return disconnected;
  }

  public void setDisconnected(String disconnected) {
    this.disconnected = disconnected;
  }


  public ProfilesInner formattedService(String formattedService) {
    this.formattedService = formattedService;
    return this;
  }

  /**
   * Get formattedService
   * @return formattedService
   */
  @javax.annotation.Nullable
  public String getFormattedService() {
    return formattedService;
  }

  public void setFormattedService(String formattedService) {
    this.formattedService = formattedService;
  }


  public ProfilesInner formattedUsername(String formattedUsername) {
    this.formattedUsername = formattedUsername;
    return this;
  }

  /**
   * Get formattedUsername
   * @return formattedUsername
   */
  @javax.annotation.Nullable
  public String getFormattedUsername() {
    return formattedUsername;
  }

  public void setFormattedUsername(String formattedUsername) {
    this.formattedUsername = formattedUsername;
  }


  public ProfilesInner hasUsedSuggestions(Boolean hasUsedSuggestions) {
    this.hasUsedSuggestions = hasUsedSuggestions;
    return this;
  }

  /**
   * Get hasUsedSuggestions
   * @return hasUsedSuggestions
   */
  @javax.annotation.Nullable
  public Boolean getHasUsedSuggestions() {
    return hasUsedSuggestions;
  }

  public void setHasUsedSuggestions(Boolean hasUsedSuggestions) {
    this.hasUsedSuggestions = hasUsedSuggestions;
  }


  public ProfilesInner id(String id) {
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


  public ProfilesInner schedules(List<ProfilesInnerSchedulesInner> schedules) {
    this.schedules = schedules;
    return this;
  }

  public ProfilesInner addSchedulesItem(ProfilesInnerSchedulesInner schedulesItem) {
    if (this.schedules == null) {
      this.schedules = new ArrayList<>();
    }
    this.schedules.add(schedulesItem);
    return this;
  }

  /**
   * Get schedules
   * @return schedules
   */
  @javax.annotation.Nullable
  public List<ProfilesInnerSchedulesInner> getSchedules() {
    return schedules;
  }

  public void setSchedules(List<ProfilesInnerSchedulesInner> schedules) {
    this.schedules = schedules;
  }


  public ProfilesInner service(String service) {
    this.service = service;
    return this;
  }

  /**
   * Get service
   * @return service
   */
  @javax.annotation.Nullable
  public String getService() {
    return service;
  }

  public void setService(String service) {
    this.service = service;
  }


  public ProfilesInner serviceId(String serviceId) {
    this.serviceId = serviceId;
    return this;
  }

  /**
   * Get serviceId
   * @return serviceId
   */
  @javax.annotation.Nullable
  public String getServiceId() {
    return serviceId;
  }

  public void setServiceId(String serviceId) {
    this.serviceId = serviceId;
  }


  public ProfilesInner serviceType(String serviceType) {
    this.serviceType = serviceType;
    return this;
  }

  /**
   * Get serviceType
   * @return serviceType
   */
  @javax.annotation.Nullable
  public String getServiceType() {
    return serviceType;
  }

  public void setServiceType(String serviceType) {
    this.serviceType = serviceType;
  }


  public ProfilesInner serviceUsername(String serviceUsername) {
    this.serviceUsername = serviceUsername;
    return this;
  }

  /**
   * Get serviceUsername
   * @return serviceUsername
   */
  @javax.annotation.Nullable
  public String getServiceUsername() {
    return serviceUsername;
  }

  public void setServiceUsername(String serviceUsername) {
    this.serviceUsername = serviceUsername;
  }


  public ProfilesInner shortener(ProfilesInnerShortener shortener) {
    this.shortener = shortener;
    return this;
  }

  /**
   * Get shortener
   * @return shortener
   */
  @javax.annotation.Nullable
  public ProfilesInnerShortener getShortener() {
    return shortener;
  }

  public void setShortener(ProfilesInnerShortener shortener) {
    this.shortener = shortener;
  }


  public ProfilesInner statistics(ProfilesInnerStatistics statistics) {
    this.statistics = statistics;
    return this;
  }

  /**
   * Get statistics
   * @return statistics
   */
  @javax.annotation.Nullable
  public ProfilesInnerStatistics getStatistics() {
    return statistics;
  }

  public void setStatistics(ProfilesInnerStatistics statistics) {
    this.statistics = statistics;
  }


  public ProfilesInner timezone(String timezone) {
    this.timezone = timezone;
    return this;
  }

  /**
   * Get timezone
   * @return timezone
   */
  @javax.annotation.Nullable
  public String getTimezone() {
    return timezone;
  }

  public void setTimezone(String timezone) {
    this.timezone = timezone;
  }


  public ProfilesInner userId(String userId) {
    this.userId = userId;
    return this;
  }

  /**
   * Get userId
   * @return userId
   */
  @javax.annotation.Nullable
  public String getUserId() {
    return userId;
  }

  public void setUserId(String userId) {
    this.userId = userId;
  }


  public ProfilesInner utmTracking(String utmTracking) {
    this.utmTracking = utmTracking;
    return this;
  }

  /**
   * Get utmTracking
   * @return utmTracking
   */
  @javax.annotation.Nullable
  public String getUtmTracking() {
    return utmTracking;
  }

  public void setUtmTracking(String utmTracking) {
    this.utmTracking = utmTracking;
  }


  public ProfilesInner verb(String verb) {
    this.verb = verb;
    return this;
  }

  /**
   * Get verb
   * @return verb
   */
  @javax.annotation.Nullable
  public String getVerb() {
    return verb;
  }

  public void setVerb(String verb) {
    this.verb = verb;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProfilesInner profilesInner = (ProfilesInner) o;
    return Objects.equals(this.id, profilesInner.id) &&
        Objects.equals(this.avatar, profilesInner.avatar) &&
        Objects.equals(this.avatarHttps, profilesInner.avatarHttps) &&
        Objects.equals(this.counts, profilesInner.counts) &&
        Objects.equals(this.coverPhoto, profilesInner.coverPhoto) &&
        Objects.equals(this._default, profilesInner._default) &&
        Objects.equals(this.disabledFeatures, profilesInner.disabledFeatures) &&
        Objects.equals(this.disconnected, profilesInner.disconnected) &&
        Objects.equals(this.formattedService, profilesInner.formattedService) &&
        Objects.equals(this.formattedUsername, profilesInner.formattedUsername) &&
        Objects.equals(this.hasUsedSuggestions, profilesInner.hasUsedSuggestions) &&
        Objects.equals(this.id, profilesInner.id) &&
        Objects.equals(this.schedules, profilesInner.schedules) &&
        Objects.equals(this.service, profilesInner.service) &&
        Objects.equals(this.serviceId, profilesInner.serviceId) &&
        Objects.equals(this.serviceType, profilesInner.serviceType) &&
        Objects.equals(this.serviceUsername, profilesInner.serviceUsername) &&
        Objects.equals(this.shortener, profilesInner.shortener) &&
        Objects.equals(this.statistics, profilesInner.statistics) &&
        Objects.equals(this.timezone, profilesInner.timezone) &&
        Objects.equals(this.userId, profilesInner.userId) &&
        Objects.equals(this.utmTracking, profilesInner.utmTracking) &&
        Objects.equals(this.verb, profilesInner.verb);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, avatar, avatarHttps, counts, coverPhoto, _default, disabledFeatures, disconnected, formattedService, formattedUsername, hasUsedSuggestions, id, schedules, service, serviceId, serviceType, serviceUsername, shortener, statistics, timezone, userId, utmTracking, verb);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProfilesInner {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    avatar: ").append(toIndentedString(avatar)).append("\n");
    sb.append("    avatarHttps: ").append(toIndentedString(avatarHttps)).append("\n");
    sb.append("    counts: ").append(toIndentedString(counts)).append("\n");
    sb.append("    coverPhoto: ").append(toIndentedString(coverPhoto)).append("\n");
    sb.append("    _default: ").append(toIndentedString(_default)).append("\n");
    sb.append("    disabledFeatures: ").append(toIndentedString(disabledFeatures)).append("\n");
    sb.append("    disconnected: ").append(toIndentedString(disconnected)).append("\n");
    sb.append("    formattedService: ").append(toIndentedString(formattedService)).append("\n");
    sb.append("    formattedUsername: ").append(toIndentedString(formattedUsername)).append("\n");
    sb.append("    hasUsedSuggestions: ").append(toIndentedString(hasUsedSuggestions)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    schedules: ").append(toIndentedString(schedules)).append("\n");
    sb.append("    service: ").append(toIndentedString(service)).append("\n");
    sb.append("    serviceId: ").append(toIndentedString(serviceId)).append("\n");
    sb.append("    serviceType: ").append(toIndentedString(serviceType)).append("\n");
    sb.append("    serviceUsername: ").append(toIndentedString(serviceUsername)).append("\n");
    sb.append("    shortener: ").append(toIndentedString(shortener)).append("\n");
    sb.append("    statistics: ").append(toIndentedString(statistics)).append("\n");
    sb.append("    timezone: ").append(toIndentedString(timezone)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    utmTracking: ").append(toIndentedString(utmTracking)).append("\n");
    sb.append("    verb: ").append(toIndentedString(verb)).append("\n");
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
    openapiFields.add("_id");
    openapiFields.add("avatar");
    openapiFields.add("avatar_https");
    openapiFields.add("counts");
    openapiFields.add("cover_photo");
    openapiFields.add("default");
    openapiFields.add("disabled_features");
    openapiFields.add("disconnected");
    openapiFields.add("formatted_service");
    openapiFields.add("formatted_username");
    openapiFields.add("has_used_suggestions");
    openapiFields.add("id");
    openapiFields.add("schedules");
    openapiFields.add("service");
    openapiFields.add("service_id");
    openapiFields.add("service_type");
    openapiFields.add("service_username");
    openapiFields.add("shortener");
    openapiFields.add("statistics");
    openapiFields.add("timezone");
    openapiFields.add("user_id");
    openapiFields.add("utm_tracking");
    openapiFields.add("verb");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProfilesInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProfilesInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProfilesInner is not found in the empty JSON string", ProfilesInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProfilesInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProfilesInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("_id") != null && !jsonObj.get("_id").isJsonNull()) && !jsonObj.get("_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("_id").toString()));
      }
      if ((jsonObj.get("avatar") != null && !jsonObj.get("avatar").isJsonNull()) && !jsonObj.get("avatar").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `avatar` to be a primitive type in the JSON string but got `%s`", jsonObj.get("avatar").toString()));
      }
      if ((jsonObj.get("avatar_https") != null && !jsonObj.get("avatar_https").isJsonNull()) && !jsonObj.get("avatar_https").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `avatar_https` to be a primitive type in the JSON string but got `%s`", jsonObj.get("avatar_https").toString()));
      }
      // validate the optional field `counts`
      if (jsonObj.get("counts") != null && !jsonObj.get("counts").isJsonNull()) {
        ProfilesInnerCounts.validateJsonElement(jsonObj.get("counts"));
      }
      if ((jsonObj.get("cover_photo") != null && !jsonObj.get("cover_photo").isJsonNull()) && !jsonObj.get("cover_photo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cover_photo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cover_photo").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("disabled_features") != null && !jsonObj.get("disabled_features").isJsonNull() && !jsonObj.get("disabled_features").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `disabled_features` to be an array in the JSON string but got `%s`", jsonObj.get("disabled_features").toString()));
      }
      if ((jsonObj.get("disconnected") != null && !jsonObj.get("disconnected").isJsonNull()) && !jsonObj.get("disconnected").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `disconnected` to be a primitive type in the JSON string but got `%s`", jsonObj.get("disconnected").toString()));
      }
      if ((jsonObj.get("formatted_service") != null && !jsonObj.get("formatted_service").isJsonNull()) && !jsonObj.get("formatted_service").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formatted_service` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formatted_service").toString()));
      }
      if ((jsonObj.get("formatted_username") != null && !jsonObj.get("formatted_username").isJsonNull()) && !jsonObj.get("formatted_username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `formatted_username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("formatted_username").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (jsonObj.get("schedules") != null && !jsonObj.get("schedules").isJsonNull()) {
        JsonArray jsonArrayschedules = jsonObj.getAsJsonArray("schedules");
        if (jsonArrayschedules != null) {
          // ensure the json data is an array
          if (!jsonObj.get("schedules").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `schedules` to be an array in the JSON string but got `%s`", jsonObj.get("schedules").toString()));
          }

          // validate the optional field `schedules` (array)
          for (int i = 0; i < jsonArrayschedules.size(); i++) {
            ProfilesInnerSchedulesInner.validateJsonElement(jsonArrayschedules.get(i));
          };
        }
      }
      if ((jsonObj.get("service") != null && !jsonObj.get("service").isJsonNull()) && !jsonObj.get("service").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service").toString()));
      }
      if ((jsonObj.get("service_id") != null && !jsonObj.get("service_id").isJsonNull()) && !jsonObj.get("service_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_id").toString()));
      }
      if ((jsonObj.get("service_type") != null && !jsonObj.get("service_type").isJsonNull()) && !jsonObj.get("service_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_type").toString()));
      }
      if ((jsonObj.get("service_username") != null && !jsonObj.get("service_username").isJsonNull()) && !jsonObj.get("service_username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_username").toString()));
      }
      // validate the optional field `shortener`
      if (jsonObj.get("shortener") != null && !jsonObj.get("shortener").isJsonNull()) {
        ProfilesInnerShortener.validateJsonElement(jsonObj.get("shortener"));
      }
      // validate the optional field `statistics`
      if (jsonObj.get("statistics") != null && !jsonObj.get("statistics").isJsonNull()) {
        ProfilesInnerStatistics.validateJsonElement(jsonObj.get("statistics"));
      }
      if ((jsonObj.get("timezone") != null && !jsonObj.get("timezone").isJsonNull()) && !jsonObj.get("timezone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timezone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timezone").toString()));
      }
      if ((jsonObj.get("user_id") != null && !jsonObj.get("user_id").isJsonNull()) && !jsonObj.get("user_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_id").toString()));
      }
      if ((jsonObj.get("utm_tracking") != null && !jsonObj.get("utm_tracking").isJsonNull()) && !jsonObj.get("utm_tracking").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `utm_tracking` to be a primitive type in the JSON string but got `%s`", jsonObj.get("utm_tracking").toString()));
      }
      if ((jsonObj.get("verb") != null && !jsonObj.get("verb").isJsonNull()) && !jsonObj.get("verb").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `verb` to be a primitive type in the JSON string but got `%s`", jsonObj.get("verb").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProfilesInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProfilesInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProfilesInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProfilesInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ProfilesInner>() {
           @Override
           public void write(JsonWriter out, ProfilesInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProfilesInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProfilesInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProfilesInner
   * @throws IOException if the JSON string is invalid with respect to ProfilesInner
   */
  public static ProfilesInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProfilesInner.class);
  }

  /**
   * Convert an instance of ProfilesInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

