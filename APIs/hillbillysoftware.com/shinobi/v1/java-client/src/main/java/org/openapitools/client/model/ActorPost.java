/*
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
 * ActorPost
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:59.717792-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ActorPost {
  public static final String SERIALIZED_NAME_ACCESS_TOKEN = "AccessToken";
  @SerializedName(SERIALIZED_NAME_ACCESS_TOKEN)
  private String accessToken;

  public static final String SERIALIZED_NAME_BIO = "Bio";
  @SerializedName(SERIALIZED_NAME_BIO)
  private String bio;

  public static final String SERIALIZED_NAME_BIRTH_YEAR = "BirthYear";
  @SerializedName(SERIALIZED_NAME_BIRTH_YEAR)
  private String birthYear;

  public static final String SERIALIZED_NAME_DEATH_YEAR = "DeathYear";
  @SerializedName(SERIALIZED_NAME_DEATH_YEAR)
  private String deathYear;

  public static final String SERIALIZED_NAME_GENDER = "Gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_POPULARITY_INDEX = "PopularityIndex";
  @SerializedName(SERIALIZED_NAME_POPULARITY_INDEX)
  private String popularityIndex;

  public static final String SERIALIZED_NAME_PROFILE_IMAGE = "ProfileImage";
  @SerializedName(SERIALIZED_NAME_PROFILE_IMAGE)
  private String profileImage;

  public ActorPost() {
  }

  public ActorPost accessToken(String accessToken) {
    this.accessToken = accessToken;
    return this;
  }

  /**
   * Get accessToken
   * @return accessToken
   */
  @javax.annotation.Nullable
  public String getAccessToken() {
    return accessToken;
  }

  public void setAccessToken(String accessToken) {
    this.accessToken = accessToken;
  }


  public ActorPost bio(String bio) {
    this.bio = bio;
    return this;
  }

  /**
   * Get bio
   * @return bio
   */
  @javax.annotation.Nullable
  public String getBio() {
    return bio;
  }

  public void setBio(String bio) {
    this.bio = bio;
  }


  public ActorPost birthYear(String birthYear) {
    this.birthYear = birthYear;
    return this;
  }

  /**
   * Get birthYear
   * @return birthYear
   */
  @javax.annotation.Nullable
  public String getBirthYear() {
    return birthYear;
  }

  public void setBirthYear(String birthYear) {
    this.birthYear = birthYear;
  }


  public ActorPost deathYear(String deathYear) {
    this.deathYear = deathYear;
    return this;
  }

  /**
   * Get deathYear
   * @return deathYear
   */
  @javax.annotation.Nullable
  public String getDeathYear() {
    return deathYear;
  }

  public void setDeathYear(String deathYear) {
    this.deathYear = deathYear;
  }


  public ActorPost gender(String gender) {
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


  public ActorPost name(String name) {
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


  public ActorPost popularityIndex(String popularityIndex) {
    this.popularityIndex = popularityIndex;
    return this;
  }

  /**
   * Get popularityIndex
   * @return popularityIndex
   */
  @javax.annotation.Nullable
  public String getPopularityIndex() {
    return popularityIndex;
  }

  public void setPopularityIndex(String popularityIndex) {
    this.popularityIndex = popularityIndex;
  }


  public ActorPost profileImage(String profileImage) {
    this.profileImage = profileImage;
    return this;
  }

  /**
   * Get profileImage
   * @return profileImage
   */
  @javax.annotation.Nullable
  public String getProfileImage() {
    return profileImage;
  }

  public void setProfileImage(String profileImage) {
    this.profileImage = profileImage;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ActorPost actorPost = (ActorPost) o;
    return Objects.equals(this.accessToken, actorPost.accessToken) &&
        Objects.equals(this.bio, actorPost.bio) &&
        Objects.equals(this.birthYear, actorPost.birthYear) &&
        Objects.equals(this.deathYear, actorPost.deathYear) &&
        Objects.equals(this.gender, actorPost.gender) &&
        Objects.equals(this.name, actorPost.name) &&
        Objects.equals(this.popularityIndex, actorPost.popularityIndex) &&
        Objects.equals(this.profileImage, actorPost.profileImage);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accessToken, bio, birthYear, deathYear, gender, name, popularityIndex, profileImage);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ActorPost {\n");
    sb.append("    accessToken: ").append(toIndentedString(accessToken)).append("\n");
    sb.append("    bio: ").append(toIndentedString(bio)).append("\n");
    sb.append("    birthYear: ").append(toIndentedString(birthYear)).append("\n");
    sb.append("    deathYear: ").append(toIndentedString(deathYear)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    popularityIndex: ").append(toIndentedString(popularityIndex)).append("\n");
    sb.append("    profileImage: ").append(toIndentedString(profileImage)).append("\n");
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
    openapiFields.add("AccessToken");
    openapiFields.add("Bio");
    openapiFields.add("BirthYear");
    openapiFields.add("DeathYear");
    openapiFields.add("Gender");
    openapiFields.add("Name");
    openapiFields.add("PopularityIndex");
    openapiFields.add("ProfileImage");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ActorPost
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ActorPost.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ActorPost is not found in the empty JSON string", ActorPost.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ActorPost.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ActorPost` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("AccessToken") != null && !jsonObj.get("AccessToken").isJsonNull()) && !jsonObj.get("AccessToken").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AccessToken` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AccessToken").toString()));
      }
      if ((jsonObj.get("Bio") != null && !jsonObj.get("Bio").isJsonNull()) && !jsonObj.get("Bio").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Bio` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Bio").toString()));
      }
      if ((jsonObj.get("BirthYear") != null && !jsonObj.get("BirthYear").isJsonNull()) && !jsonObj.get("BirthYear").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BirthYear` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BirthYear").toString()));
      }
      if ((jsonObj.get("DeathYear") != null && !jsonObj.get("DeathYear").isJsonNull()) && !jsonObj.get("DeathYear").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DeathYear` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DeathYear").toString()));
      }
      if ((jsonObj.get("Gender") != null && !jsonObj.get("Gender").isJsonNull()) && !jsonObj.get("Gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Gender").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("PopularityIndex") != null && !jsonObj.get("PopularityIndex").isJsonNull()) && !jsonObj.get("PopularityIndex").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PopularityIndex` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PopularityIndex").toString()));
      }
      if ((jsonObj.get("ProfileImage") != null && !jsonObj.get("ProfileImage").isJsonNull()) && !jsonObj.get("ProfileImage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ProfileImage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ProfileImage").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ActorPost.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ActorPost' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ActorPost> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ActorPost.class));

       return (TypeAdapter<T>) new TypeAdapter<ActorPost>() {
           @Override
           public void write(JsonWriter out, ActorPost value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ActorPost read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ActorPost given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ActorPost
   * @throws IOException if the JSON string is invalid with respect to ActorPost
   */
  public static ActorPost fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ActorPost.class);
  }

  /**
   * Convert an instance of ActorPost to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

