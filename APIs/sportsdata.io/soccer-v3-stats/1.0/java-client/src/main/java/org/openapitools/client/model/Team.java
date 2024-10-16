/*
 * Soccer v3 Stats
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:19.276097-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Team {
  public static final String SERIALIZED_NAME_ACTIVE = "Active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private Boolean active;

  public static final String SERIALIZED_NAME_ADDRESS = "Address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_AREA_ID = "AreaId";
  @SerializedName(SERIALIZED_NAME_AREA_ID)
  private Integer areaId;

  public static final String SERIALIZED_NAME_AREA_NAME = "AreaName";
  @SerializedName(SERIALIZED_NAME_AREA_NAME)
  private String areaName;

  public static final String SERIALIZED_NAME_CITY = "City";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_CLUB_COLOR1 = "ClubColor1";
  @SerializedName(SERIALIZED_NAME_CLUB_COLOR1)
  private String clubColor1;

  public static final String SERIALIZED_NAME_CLUB_COLOR2 = "ClubColor2";
  @SerializedName(SERIALIZED_NAME_CLUB_COLOR2)
  private String clubColor2;

  public static final String SERIALIZED_NAME_CLUB_COLOR3 = "ClubColor3";
  @SerializedName(SERIALIZED_NAME_CLUB_COLOR3)
  private String clubColor3;

  public static final String SERIALIZED_NAME_EMAIL = "Email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_FAX = "Fax";
  @SerializedName(SERIALIZED_NAME_FAX)
  private String fax;

  public static final String SERIALIZED_NAME_FOUNDED = "Founded";
  @SerializedName(SERIALIZED_NAME_FOUNDED)
  private Integer founded;

  public static final String SERIALIZED_NAME_FULL_NAME = "FullName";
  @SerializedName(SERIALIZED_NAME_FULL_NAME)
  private String fullName;

  public static final String SERIALIZED_NAME_GENDER = "Gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_GLOBAL_TEAM_ID = "GlobalTeamId";
  @SerializedName(SERIALIZED_NAME_GLOBAL_TEAM_ID)
  private Integer globalTeamId;

  public static final String SERIALIZED_NAME_KEY = "Key";
  @SerializedName(SERIALIZED_NAME_KEY)
  private String key;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NICKNAME1 = "Nickname1";
  @SerializedName(SERIALIZED_NAME_NICKNAME1)
  private String nickname1;

  public static final String SERIALIZED_NAME_NICKNAME2 = "Nickname2";
  @SerializedName(SERIALIZED_NAME_NICKNAME2)
  private String nickname2;

  public static final String SERIALIZED_NAME_NICKNAME3 = "Nickname3";
  @SerializedName(SERIALIZED_NAME_NICKNAME3)
  private String nickname3;

  public static final String SERIALIZED_NAME_PHONE = "Phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_TEAM_ID = "TeamId";
  @SerializedName(SERIALIZED_NAME_TEAM_ID)
  private Integer teamId;

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_VENUE_ID = "VenueId";
  @SerializedName(SERIALIZED_NAME_VENUE_ID)
  private Integer venueId;

  public static final String SERIALIZED_NAME_VENUE_NAME = "VenueName";
  @SerializedName(SERIALIZED_NAME_VENUE_NAME)
  private String venueName;

  public static final String SERIALIZED_NAME_WEBSITE = "Website";
  @SerializedName(SERIALIZED_NAME_WEBSITE)
  private String website;

  public static final String SERIALIZED_NAME_WIKIPEDIA_LOGO_URL = "WikipediaLogoUrl";
  @SerializedName(SERIALIZED_NAME_WIKIPEDIA_LOGO_URL)
  private String wikipediaLogoUrl;

  public static final String SERIALIZED_NAME_WIKIPEDIA_WORD_MARK_URL = "WikipediaWordMarkUrl";
  @SerializedName(SERIALIZED_NAME_WIKIPEDIA_WORD_MARK_URL)
  private String wikipediaWordMarkUrl;

  public static final String SERIALIZED_NAME_ZIP = "Zip";
  @SerializedName(SERIALIZED_NAME_ZIP)
  private String zip;

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


  public Team address(String address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public Team areaId(Integer areaId) {
    this.areaId = areaId;
    return this;
  }

  /**
   * Get areaId
   * @return areaId
   */
  @javax.annotation.Nullable
  public Integer getAreaId() {
    return areaId;
  }

  public void setAreaId(Integer areaId) {
    this.areaId = areaId;
  }


  public Team areaName(String areaName) {
    this.areaName = areaName;
    return this;
  }

  /**
   * Get areaName
   * @return areaName
   */
  @javax.annotation.Nullable
  public String getAreaName() {
    return areaName;
  }

  public void setAreaName(String areaName) {
    this.areaName = areaName;
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


  public Team clubColor1(String clubColor1) {
    this.clubColor1 = clubColor1;
    return this;
  }

  /**
   * Get clubColor1
   * @return clubColor1
   */
  @javax.annotation.Nullable
  public String getClubColor1() {
    return clubColor1;
  }

  public void setClubColor1(String clubColor1) {
    this.clubColor1 = clubColor1;
  }


  public Team clubColor2(String clubColor2) {
    this.clubColor2 = clubColor2;
    return this;
  }

  /**
   * Get clubColor2
   * @return clubColor2
   */
  @javax.annotation.Nullable
  public String getClubColor2() {
    return clubColor2;
  }

  public void setClubColor2(String clubColor2) {
    this.clubColor2 = clubColor2;
  }


  public Team clubColor3(String clubColor3) {
    this.clubColor3 = clubColor3;
    return this;
  }

  /**
   * Get clubColor3
   * @return clubColor3
   */
  @javax.annotation.Nullable
  public String getClubColor3() {
    return clubColor3;
  }

  public void setClubColor3(String clubColor3) {
    this.clubColor3 = clubColor3;
  }


  public Team email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public Team fax(String fax) {
    this.fax = fax;
    return this;
  }

  /**
   * Get fax
   * @return fax
   */
  @javax.annotation.Nullable
  public String getFax() {
    return fax;
  }

  public void setFax(String fax) {
    this.fax = fax;
  }


  public Team founded(Integer founded) {
    this.founded = founded;
    return this;
  }

  /**
   * Get founded
   * @return founded
   */
  @javax.annotation.Nullable
  public Integer getFounded() {
    return founded;
  }

  public void setFounded(Integer founded) {
    this.founded = founded;
  }


  public Team fullName(String fullName) {
    this.fullName = fullName;
    return this;
  }

  /**
   * Get fullName
   * @return fullName
   */
  @javax.annotation.Nullable
  public String getFullName() {
    return fullName;
  }

  public void setFullName(String fullName) {
    this.fullName = fullName;
  }


  public Team gender(String gender) {
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


  public Team globalTeamId(Integer globalTeamId) {
    this.globalTeamId = globalTeamId;
    return this;
  }

  /**
   * Get globalTeamId
   * @return globalTeamId
   */
  @javax.annotation.Nullable
  public Integer getGlobalTeamId() {
    return globalTeamId;
  }

  public void setGlobalTeamId(Integer globalTeamId) {
    this.globalTeamId = globalTeamId;
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


  public Team nickname1(String nickname1) {
    this.nickname1 = nickname1;
    return this;
  }

  /**
   * Get nickname1
   * @return nickname1
   */
  @javax.annotation.Nullable
  public String getNickname1() {
    return nickname1;
  }

  public void setNickname1(String nickname1) {
    this.nickname1 = nickname1;
  }


  public Team nickname2(String nickname2) {
    this.nickname2 = nickname2;
    return this;
  }

  /**
   * Get nickname2
   * @return nickname2
   */
  @javax.annotation.Nullable
  public String getNickname2() {
    return nickname2;
  }

  public void setNickname2(String nickname2) {
    this.nickname2 = nickname2;
  }


  public Team nickname3(String nickname3) {
    this.nickname3 = nickname3;
    return this;
  }

  /**
   * Get nickname3
   * @return nickname3
   */
  @javax.annotation.Nullable
  public String getNickname3() {
    return nickname3;
  }

  public void setNickname3(String nickname3) {
    this.nickname3 = nickname3;
  }


  public Team phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Get phone
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public Team teamId(Integer teamId) {
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


  public Team type(String type) {
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


  public Team venueId(Integer venueId) {
    this.venueId = venueId;
    return this;
  }

  /**
   * Get venueId
   * @return venueId
   */
  @javax.annotation.Nullable
  public Integer getVenueId() {
    return venueId;
  }

  public void setVenueId(Integer venueId) {
    this.venueId = venueId;
  }


  public Team venueName(String venueName) {
    this.venueName = venueName;
    return this;
  }

  /**
   * Get venueName
   * @return venueName
   */
  @javax.annotation.Nullable
  public String getVenueName() {
    return venueName;
  }

  public void setVenueName(String venueName) {
    this.venueName = venueName;
  }


  public Team website(String website) {
    this.website = website;
    return this;
  }

  /**
   * Get website
   * @return website
   */
  @javax.annotation.Nullable
  public String getWebsite() {
    return website;
  }

  public void setWebsite(String website) {
    this.website = website;
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


  public Team zip(String zip) {
    this.zip = zip;
    return this;
  }

  /**
   * Get zip
   * @return zip
   */
  @javax.annotation.Nullable
  public String getZip() {
    return zip;
  }

  public void setZip(String zip) {
    this.zip = zip;
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
        Objects.equals(this.address, team.address) &&
        Objects.equals(this.areaId, team.areaId) &&
        Objects.equals(this.areaName, team.areaName) &&
        Objects.equals(this.city, team.city) &&
        Objects.equals(this.clubColor1, team.clubColor1) &&
        Objects.equals(this.clubColor2, team.clubColor2) &&
        Objects.equals(this.clubColor3, team.clubColor3) &&
        Objects.equals(this.email, team.email) &&
        Objects.equals(this.fax, team.fax) &&
        Objects.equals(this.founded, team.founded) &&
        Objects.equals(this.fullName, team.fullName) &&
        Objects.equals(this.gender, team.gender) &&
        Objects.equals(this.globalTeamId, team.globalTeamId) &&
        Objects.equals(this.key, team.key) &&
        Objects.equals(this.name, team.name) &&
        Objects.equals(this.nickname1, team.nickname1) &&
        Objects.equals(this.nickname2, team.nickname2) &&
        Objects.equals(this.nickname3, team.nickname3) &&
        Objects.equals(this.phone, team.phone) &&
        Objects.equals(this.teamId, team.teamId) &&
        Objects.equals(this.type, team.type) &&
        Objects.equals(this.venueId, team.venueId) &&
        Objects.equals(this.venueName, team.venueName) &&
        Objects.equals(this.website, team.website) &&
        Objects.equals(this.wikipediaLogoUrl, team.wikipediaLogoUrl) &&
        Objects.equals(this.wikipediaWordMarkUrl, team.wikipediaWordMarkUrl) &&
        Objects.equals(this.zip, team.zip);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, address, areaId, areaName, city, clubColor1, clubColor2, clubColor3, email, fax, founded, fullName, gender, globalTeamId, key, name, nickname1, nickname2, nickname3, phone, teamId, type, venueId, venueName, website, wikipediaLogoUrl, wikipediaWordMarkUrl, zip);
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
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    areaId: ").append(toIndentedString(areaId)).append("\n");
    sb.append("    areaName: ").append(toIndentedString(areaName)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    clubColor1: ").append(toIndentedString(clubColor1)).append("\n");
    sb.append("    clubColor2: ").append(toIndentedString(clubColor2)).append("\n");
    sb.append("    clubColor3: ").append(toIndentedString(clubColor3)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    fax: ").append(toIndentedString(fax)).append("\n");
    sb.append("    founded: ").append(toIndentedString(founded)).append("\n");
    sb.append("    fullName: ").append(toIndentedString(fullName)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    globalTeamId: ").append(toIndentedString(globalTeamId)).append("\n");
    sb.append("    key: ").append(toIndentedString(key)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nickname1: ").append(toIndentedString(nickname1)).append("\n");
    sb.append("    nickname2: ").append(toIndentedString(nickname2)).append("\n");
    sb.append("    nickname3: ").append(toIndentedString(nickname3)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    teamId: ").append(toIndentedString(teamId)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    venueId: ").append(toIndentedString(venueId)).append("\n");
    sb.append("    venueName: ").append(toIndentedString(venueName)).append("\n");
    sb.append("    website: ").append(toIndentedString(website)).append("\n");
    sb.append("    wikipediaLogoUrl: ").append(toIndentedString(wikipediaLogoUrl)).append("\n");
    sb.append("    wikipediaWordMarkUrl: ").append(toIndentedString(wikipediaWordMarkUrl)).append("\n");
    sb.append("    zip: ").append(toIndentedString(zip)).append("\n");
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
    openapiFields.add("Address");
    openapiFields.add("AreaId");
    openapiFields.add("AreaName");
    openapiFields.add("City");
    openapiFields.add("ClubColor1");
    openapiFields.add("ClubColor2");
    openapiFields.add("ClubColor3");
    openapiFields.add("Email");
    openapiFields.add("Fax");
    openapiFields.add("Founded");
    openapiFields.add("FullName");
    openapiFields.add("Gender");
    openapiFields.add("GlobalTeamId");
    openapiFields.add("Key");
    openapiFields.add("Name");
    openapiFields.add("Nickname1");
    openapiFields.add("Nickname2");
    openapiFields.add("Nickname3");
    openapiFields.add("Phone");
    openapiFields.add("TeamId");
    openapiFields.add("Type");
    openapiFields.add("VenueId");
    openapiFields.add("VenueName");
    openapiFields.add("Website");
    openapiFields.add("WikipediaLogoUrl");
    openapiFields.add("WikipediaWordMarkUrl");
    openapiFields.add("Zip");

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
      if ((jsonObj.get("Address") != null && !jsonObj.get("Address").isJsonNull()) && !jsonObj.get("Address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Address").toString()));
      }
      if ((jsonObj.get("AreaName") != null && !jsonObj.get("AreaName").isJsonNull()) && !jsonObj.get("AreaName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `AreaName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("AreaName").toString()));
      }
      if ((jsonObj.get("City") != null && !jsonObj.get("City").isJsonNull()) && !jsonObj.get("City").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `City` to be a primitive type in the JSON string but got `%s`", jsonObj.get("City").toString()));
      }
      if ((jsonObj.get("ClubColor1") != null && !jsonObj.get("ClubColor1").isJsonNull()) && !jsonObj.get("ClubColor1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ClubColor1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ClubColor1").toString()));
      }
      if ((jsonObj.get("ClubColor2") != null && !jsonObj.get("ClubColor2").isJsonNull()) && !jsonObj.get("ClubColor2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ClubColor2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ClubColor2").toString()));
      }
      if ((jsonObj.get("ClubColor3") != null && !jsonObj.get("ClubColor3").isJsonNull()) && !jsonObj.get("ClubColor3").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ClubColor3` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ClubColor3").toString()));
      }
      if ((jsonObj.get("Email") != null && !jsonObj.get("Email").isJsonNull()) && !jsonObj.get("Email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Email").toString()));
      }
      if ((jsonObj.get("Fax") != null && !jsonObj.get("Fax").isJsonNull()) && !jsonObj.get("Fax").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Fax` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Fax").toString()));
      }
      if ((jsonObj.get("FullName") != null && !jsonObj.get("FullName").isJsonNull()) && !jsonObj.get("FullName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FullName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FullName").toString()));
      }
      if ((jsonObj.get("Gender") != null && !jsonObj.get("Gender").isJsonNull()) && !jsonObj.get("Gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Gender").toString()));
      }
      if ((jsonObj.get("Key") != null && !jsonObj.get("Key").isJsonNull()) && !jsonObj.get("Key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Key").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Nickname1") != null && !jsonObj.get("Nickname1").isJsonNull()) && !jsonObj.get("Nickname1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Nickname1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Nickname1").toString()));
      }
      if ((jsonObj.get("Nickname2") != null && !jsonObj.get("Nickname2").isJsonNull()) && !jsonObj.get("Nickname2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Nickname2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Nickname2").toString()));
      }
      if ((jsonObj.get("Nickname3") != null && !jsonObj.get("Nickname3").isJsonNull()) && !jsonObj.get("Nickname3").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Nickname3` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Nickname3").toString()));
      }
      if ((jsonObj.get("Phone") != null && !jsonObj.get("Phone").isJsonNull()) && !jsonObj.get("Phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Phone").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
      if ((jsonObj.get("VenueName") != null && !jsonObj.get("VenueName").isJsonNull()) && !jsonObj.get("VenueName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `VenueName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("VenueName").toString()));
      }
      if ((jsonObj.get("Website") != null && !jsonObj.get("Website").isJsonNull()) && !jsonObj.get("Website").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Website` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Website").toString()));
      }
      if ((jsonObj.get("WikipediaLogoUrl") != null && !jsonObj.get("WikipediaLogoUrl").isJsonNull()) && !jsonObj.get("WikipediaLogoUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `WikipediaLogoUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("WikipediaLogoUrl").toString()));
      }
      if ((jsonObj.get("WikipediaWordMarkUrl") != null && !jsonObj.get("WikipediaWordMarkUrl").isJsonNull()) && !jsonObj.get("WikipediaWordMarkUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `WikipediaWordMarkUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("WikipediaWordMarkUrl").toString()));
      }
      if ((jsonObj.get("Zip") != null && !jsonObj.get("Zip").isJsonNull()) && !jsonObj.get("Zip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Zip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Zip").toString()));
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

