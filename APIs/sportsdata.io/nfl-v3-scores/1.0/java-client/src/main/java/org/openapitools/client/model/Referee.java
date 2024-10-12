/*
 * NFL v3 Scores
 * NFL schedules, scores, odds, weather, and news API.
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
 * Referee
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:21.929041-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Referee {
  public static final String SERIALIZED_NAME_COLLEGE = "College";
  @SerializedName(SERIALIZED_NAME_COLLEGE)
  private String college;

  public static final String SERIALIZED_NAME_EXPERIENCE = "Experience";
  @SerializedName(SERIALIZED_NAME_EXPERIENCE)
  private Integer experience;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NUMBER = "Number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private Integer number;

  public static final String SERIALIZED_NAME_POSITION = "Position";
  @SerializedName(SERIALIZED_NAME_POSITION)
  private String position;

  public static final String SERIALIZED_NAME_REFEREE_I_D = "RefereeID";
  @SerializedName(SERIALIZED_NAME_REFEREE_I_D)
  private Integer refereeID;

  public Referee() {
  }

  public Referee college(String college) {
    this.college = college;
    return this;
  }

  /**
   * Get college
   * @return college
   */
  @javax.annotation.Nullable
  public String getCollege() {
    return college;
  }

  public void setCollege(String college) {
    this.college = college;
  }


  public Referee experience(Integer experience) {
    this.experience = experience;
    return this;
  }

  /**
   * Get experience
   * @return experience
   */
  @javax.annotation.Nullable
  public Integer getExperience() {
    return experience;
  }

  public void setExperience(Integer experience) {
    this.experience = experience;
  }


  public Referee name(String name) {
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


  public Referee number(Integer number) {
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


  public Referee position(String position) {
    this.position = position;
    return this;
  }

  /**
   * Get position
   * @return position
   */
  @javax.annotation.Nullable
  public String getPosition() {
    return position;
  }

  public void setPosition(String position) {
    this.position = position;
  }


  public Referee refereeID(Integer refereeID) {
    this.refereeID = refereeID;
    return this;
  }

  /**
   * Get refereeID
   * @return refereeID
   */
  @javax.annotation.Nullable
  public Integer getRefereeID() {
    return refereeID;
  }

  public void setRefereeID(Integer refereeID) {
    this.refereeID = refereeID;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Referee referee = (Referee) o;
    return Objects.equals(this.college, referee.college) &&
        Objects.equals(this.experience, referee.experience) &&
        Objects.equals(this.name, referee.name) &&
        Objects.equals(this.number, referee.number) &&
        Objects.equals(this.position, referee.position) &&
        Objects.equals(this.refereeID, referee.refereeID);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(college, experience, name, number, position, refereeID);
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
    sb.append("class Referee {\n");
    sb.append("    college: ").append(toIndentedString(college)).append("\n");
    sb.append("    experience: ").append(toIndentedString(experience)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    position: ").append(toIndentedString(position)).append("\n");
    sb.append("    refereeID: ").append(toIndentedString(refereeID)).append("\n");
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
    openapiFields.add("College");
    openapiFields.add("Experience");
    openapiFields.add("Name");
    openapiFields.add("Number");
    openapiFields.add("Position");
    openapiFields.add("RefereeID");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Referee
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Referee.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Referee is not found in the empty JSON string", Referee.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Referee.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Referee` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("College") != null && !jsonObj.get("College").isJsonNull()) && !jsonObj.get("College").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `College` to be a primitive type in the JSON string but got `%s`", jsonObj.get("College").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("Position") != null && !jsonObj.get("Position").isJsonNull()) && !jsonObj.get("Position").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Position` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Position").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Referee.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Referee' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Referee> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Referee.class));

       return (TypeAdapter<T>) new TypeAdapter<Referee>() {
           @Override
           public void write(JsonWriter out, Referee value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Referee read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Referee given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Referee
   * @throws IOException if the JSON string is invalid with respect to Referee
   */
  public static Referee fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Referee.class);
  }

  /**
   * Convert an instance of Referee to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

