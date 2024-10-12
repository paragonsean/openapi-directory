/*
 * NASCAR v2
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
 * Driver
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:57.642335-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Driver {
  public static final String SERIALIZED_NAME_BIRTH_DATE = "BirthDate";
  @SerializedName(SERIALIZED_NAME_BIRTH_DATE)
  private String birthDate;

  public static final String SERIALIZED_NAME_BIRTH_PLACE = "BirthPlace";
  @SerializedName(SERIALIZED_NAME_BIRTH_PLACE)
  private String birthPlace;

  public static final String SERIALIZED_NAME_CHASSIS = "Chassis";
  @SerializedName(SERIALIZED_NAME_CHASSIS)
  private String chassis;

  public static final String SERIALIZED_NAME_CREATED = "Created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CREW_CHIEF = "CrewChief";
  @SerializedName(SERIALIZED_NAME_CREW_CHIEF)
  private String crewChief;

  public static final String SERIALIZED_NAME_DRIVER_I_D = "DriverID";
  @SerializedName(SERIALIZED_NAME_DRIVER_I_D)
  private Integer driverID;

  public static final String SERIALIZED_NAME_ENGINE = "Engine";
  @SerializedName(SERIALIZED_NAME_ENGINE)
  private String engine;

  public static final String SERIALIZED_NAME_FIRST_NAME = "FirstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_GENDER = "Gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_HEIGHT = "Height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private Integer height;

  public static final String SERIALIZED_NAME_LAST_NAME = "LastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_MANUFACTURER = "Manufacturer";
  @SerializedName(SERIALIZED_NAME_MANUFACTURER)
  private String manufacturer;

  public static final String SERIALIZED_NAME_NUMBER = "Number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private Integer number;

  public static final String SERIALIZED_NAME_NUMBER_DISPLAY = "NumberDisplay";
  @SerializedName(SERIALIZED_NAME_NUMBER_DISPLAY)
  private String numberDisplay;

  public static final String SERIALIZED_NAME_PHOTO_URL = "PhotoUrl";
  @SerializedName(SERIALIZED_NAME_PHOTO_URL)
  private String photoUrl;

  public static final String SERIALIZED_NAME_SPONSORS = "Sponsors";
  @SerializedName(SERIALIZED_NAME_SPONSORS)
  private String sponsors;

  public static final String SERIALIZED_NAME_TEAM = "Team";
  @SerializedName(SERIALIZED_NAME_TEAM)
  private String team;

  public static final String SERIALIZED_NAME_UPDATED = "Updated";
  @SerializedName(SERIALIZED_NAME_UPDATED)
  private String updated;

  public static final String SERIALIZED_NAME_WEIGHT = "Weight";
  @SerializedName(SERIALIZED_NAME_WEIGHT)
  private Integer weight;

  public Driver() {
  }

  public Driver birthDate(String birthDate) {
    this.birthDate = birthDate;
    return this;
  }

  /**
   * Get birthDate
   * @return birthDate
   */
  @javax.annotation.Nullable
  public String getBirthDate() {
    return birthDate;
  }

  public void setBirthDate(String birthDate) {
    this.birthDate = birthDate;
  }


  public Driver birthPlace(String birthPlace) {
    this.birthPlace = birthPlace;
    return this;
  }

  /**
   * Get birthPlace
   * @return birthPlace
   */
  @javax.annotation.Nullable
  public String getBirthPlace() {
    return birthPlace;
  }

  public void setBirthPlace(String birthPlace) {
    this.birthPlace = birthPlace;
  }


  public Driver chassis(String chassis) {
    this.chassis = chassis;
    return this;
  }

  /**
   * Get chassis
   * @return chassis
   */
  @javax.annotation.Nullable
  public String getChassis() {
    return chassis;
  }

  public void setChassis(String chassis) {
    this.chassis = chassis;
  }


  public Driver created(String created) {
    this.created = created;
    return this;
  }

  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }

  public void setCreated(String created) {
    this.created = created;
  }


  public Driver crewChief(String crewChief) {
    this.crewChief = crewChief;
    return this;
  }

  /**
   * Get crewChief
   * @return crewChief
   */
  @javax.annotation.Nullable
  public String getCrewChief() {
    return crewChief;
  }

  public void setCrewChief(String crewChief) {
    this.crewChief = crewChief;
  }


  public Driver driverID(Integer driverID) {
    this.driverID = driverID;
    return this;
  }

  /**
   * Get driverID
   * @return driverID
   */
  @javax.annotation.Nullable
  public Integer getDriverID() {
    return driverID;
  }

  public void setDriverID(Integer driverID) {
    this.driverID = driverID;
  }


  public Driver engine(String engine) {
    this.engine = engine;
    return this;
  }

  /**
   * Get engine
   * @return engine
   */
  @javax.annotation.Nullable
  public String getEngine() {
    return engine;
  }

  public void setEngine(String engine) {
    this.engine = engine;
  }


  public Driver firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * Get firstName
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public Driver gender(String gender) {
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


  public Driver height(Integer height) {
    this.height = height;
    return this;
  }

  /**
   * Get height
   * @return height
   */
  @javax.annotation.Nullable
  public Integer getHeight() {
    return height;
  }

  public void setHeight(Integer height) {
    this.height = height;
  }


  public Driver lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * Get lastName
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public Driver manufacturer(String manufacturer) {
    this.manufacturer = manufacturer;
    return this;
  }

  /**
   * Get manufacturer
   * @return manufacturer
   */
  @javax.annotation.Nullable
  public String getManufacturer() {
    return manufacturer;
  }

  public void setManufacturer(String manufacturer) {
    this.manufacturer = manufacturer;
  }


  public Driver number(Integer number) {
    this.number = number;
    return this;
  }

  /**
   * Get number
   * @return number
   */
  @javax.annotation.Nullable
  public Integer getNumber() {
    return number;
  }

  public void setNumber(Integer number) {
    this.number = number;
  }


  public Driver numberDisplay(String numberDisplay) {
    this.numberDisplay = numberDisplay;
    return this;
  }

  /**
   * Get numberDisplay
   * @return numberDisplay
   */
  @javax.annotation.Nullable
  public String getNumberDisplay() {
    return numberDisplay;
  }

  public void setNumberDisplay(String numberDisplay) {
    this.numberDisplay = numberDisplay;
  }


  public Driver photoUrl(String photoUrl) {
    this.photoUrl = photoUrl;
    return this;
  }

  /**
   * Get photoUrl
   * @return photoUrl
   */
  @javax.annotation.Nullable
  public String getPhotoUrl() {
    return photoUrl;
  }

  public void setPhotoUrl(String photoUrl) {
    this.photoUrl = photoUrl;
  }


  public Driver sponsors(String sponsors) {
    this.sponsors = sponsors;
    return this;
  }

  /**
   * Get sponsors
   * @return sponsors
   */
  @javax.annotation.Nullable
  public String getSponsors() {
    return sponsors;
  }

  public void setSponsors(String sponsors) {
    this.sponsors = sponsors;
  }


  public Driver team(String team) {
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


  public Driver updated(String updated) {
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


  public Driver weight(Integer weight) {
    this.weight = weight;
    return this;
  }

  /**
   * Get weight
   * @return weight
   */
  @javax.annotation.Nullable
  public Integer getWeight() {
    return weight;
  }

  public void setWeight(Integer weight) {
    this.weight = weight;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Driver driver = (Driver) o;
    return Objects.equals(this.birthDate, driver.birthDate) &&
        Objects.equals(this.birthPlace, driver.birthPlace) &&
        Objects.equals(this.chassis, driver.chassis) &&
        Objects.equals(this.created, driver.created) &&
        Objects.equals(this.crewChief, driver.crewChief) &&
        Objects.equals(this.driverID, driver.driverID) &&
        Objects.equals(this.engine, driver.engine) &&
        Objects.equals(this.firstName, driver.firstName) &&
        Objects.equals(this.gender, driver.gender) &&
        Objects.equals(this.height, driver.height) &&
        Objects.equals(this.lastName, driver.lastName) &&
        Objects.equals(this.manufacturer, driver.manufacturer) &&
        Objects.equals(this.number, driver.number) &&
        Objects.equals(this.numberDisplay, driver.numberDisplay) &&
        Objects.equals(this.photoUrl, driver.photoUrl) &&
        Objects.equals(this.sponsors, driver.sponsors) &&
        Objects.equals(this.team, driver.team) &&
        Objects.equals(this.updated, driver.updated) &&
        Objects.equals(this.weight, driver.weight);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(birthDate, birthPlace, chassis, created, crewChief, driverID, engine, firstName, gender, height, lastName, manufacturer, number, numberDisplay, photoUrl, sponsors, team, updated, weight);
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
    sb.append("class Driver {\n");
    sb.append("    birthDate: ").append(toIndentedString(birthDate)).append("\n");
    sb.append("    birthPlace: ").append(toIndentedString(birthPlace)).append("\n");
    sb.append("    chassis: ").append(toIndentedString(chassis)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    crewChief: ").append(toIndentedString(crewChief)).append("\n");
    sb.append("    driverID: ").append(toIndentedString(driverID)).append("\n");
    sb.append("    engine: ").append(toIndentedString(engine)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    manufacturer: ").append(toIndentedString(manufacturer)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    numberDisplay: ").append(toIndentedString(numberDisplay)).append("\n");
    sb.append("    photoUrl: ").append(toIndentedString(photoUrl)).append("\n");
    sb.append("    sponsors: ").append(toIndentedString(sponsors)).append("\n");
    sb.append("    team: ").append(toIndentedString(team)).append("\n");
    sb.append("    updated: ").append(toIndentedString(updated)).append("\n");
    sb.append("    weight: ").append(toIndentedString(weight)).append("\n");
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
    openapiFields.add("BirthDate");
    openapiFields.add("BirthPlace");
    openapiFields.add("Chassis");
    openapiFields.add("Created");
    openapiFields.add("CrewChief");
    openapiFields.add("DriverID");
    openapiFields.add("Engine");
    openapiFields.add("FirstName");
    openapiFields.add("Gender");
    openapiFields.add("Height");
    openapiFields.add("LastName");
    openapiFields.add("Manufacturer");
    openapiFields.add("Number");
    openapiFields.add("NumberDisplay");
    openapiFields.add("PhotoUrl");
    openapiFields.add("Sponsors");
    openapiFields.add("Team");
    openapiFields.add("Updated");
    openapiFields.add("Weight");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Driver
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Driver.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Driver is not found in the empty JSON string", Driver.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Driver.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Driver` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("BirthDate") != null && !jsonObj.get("BirthDate").isJsonNull()) && !jsonObj.get("BirthDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BirthDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BirthDate").toString()));
      }
      if ((jsonObj.get("BirthPlace") != null && !jsonObj.get("BirthPlace").isJsonNull()) && !jsonObj.get("BirthPlace").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BirthPlace` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BirthPlace").toString()));
      }
      if ((jsonObj.get("Chassis") != null && !jsonObj.get("Chassis").isJsonNull()) && !jsonObj.get("Chassis").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Chassis` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Chassis").toString()));
      }
      if ((jsonObj.get("Created") != null && !jsonObj.get("Created").isJsonNull()) && !jsonObj.get("Created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Created").toString()));
      }
      if ((jsonObj.get("CrewChief") != null && !jsonObj.get("CrewChief").isJsonNull()) && !jsonObj.get("CrewChief").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CrewChief` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CrewChief").toString()));
      }
      if ((jsonObj.get("Engine") != null && !jsonObj.get("Engine").isJsonNull()) && !jsonObj.get("Engine").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Engine` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Engine").toString()));
      }
      if ((jsonObj.get("FirstName") != null && !jsonObj.get("FirstName").isJsonNull()) && !jsonObj.get("FirstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FirstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FirstName").toString()));
      }
      if ((jsonObj.get("Gender") != null && !jsonObj.get("Gender").isJsonNull()) && !jsonObj.get("Gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Gender").toString()));
      }
      if ((jsonObj.get("LastName") != null && !jsonObj.get("LastName").isJsonNull()) && !jsonObj.get("LastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LastName").toString()));
      }
      if ((jsonObj.get("Manufacturer") != null && !jsonObj.get("Manufacturer").isJsonNull()) && !jsonObj.get("Manufacturer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Manufacturer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Manufacturer").toString()));
      }
      if ((jsonObj.get("NumberDisplay") != null && !jsonObj.get("NumberDisplay").isJsonNull()) && !jsonObj.get("NumberDisplay").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `NumberDisplay` to be a primitive type in the JSON string but got `%s`", jsonObj.get("NumberDisplay").toString()));
      }
      if ((jsonObj.get("PhotoUrl") != null && !jsonObj.get("PhotoUrl").isJsonNull()) && !jsonObj.get("PhotoUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PhotoUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PhotoUrl").toString()));
      }
      if ((jsonObj.get("Sponsors") != null && !jsonObj.get("Sponsors").isJsonNull()) && !jsonObj.get("Sponsors").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Sponsors` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Sponsors").toString()));
      }
      if ((jsonObj.get("Team") != null && !jsonObj.get("Team").isJsonNull()) && !jsonObj.get("Team").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Team` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Team").toString()));
      }
      if ((jsonObj.get("Updated") != null && !jsonObj.get("Updated").isJsonNull()) && !jsonObj.get("Updated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Updated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Updated").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Driver.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Driver' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Driver> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Driver.class));

       return (TypeAdapter<T>) new TypeAdapter<Driver>() {
           @Override
           public void write(JsonWriter out, Driver value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Driver read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Driver given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Driver
   * @throws IOException if the JSON string is invalid with respect to Driver
   */
  public static Driver fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Driver.class);
  }

  /**
   * Convert an instance of Driver to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

