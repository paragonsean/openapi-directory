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
 * Referee
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:19.276097-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Referee {
  public static final String SERIALIZED_NAME_FIRST_NAME = "FirstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_LAST_NAME = "LastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_NATIONALITY = "Nationality";
  @SerializedName(SERIALIZED_NAME_NATIONALITY)
  private String nationality;

  public static final String SERIALIZED_NAME_REFEREE_ID = "RefereeId";
  @SerializedName(SERIALIZED_NAME_REFEREE_ID)
  private Integer refereeId;

  public static final String SERIALIZED_NAME_SHORT_NAME = "ShortName";
  @SerializedName(SERIALIZED_NAME_SHORT_NAME)
  private String shortName;

  public Referee() {
  }

  public Referee firstName(String firstName) {
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


  public Referee lastName(String lastName) {
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


  public Referee nationality(String nationality) {
    this.nationality = nationality;
    return this;
  }

  /**
   * Get nationality
   * @return nationality
   */
  @javax.annotation.Nullable
  public String getNationality() {
    return nationality;
  }

  public void setNationality(String nationality) {
    this.nationality = nationality;
  }


  public Referee refereeId(Integer refereeId) {
    this.refereeId = refereeId;
    return this;
  }

  /**
   * Get refereeId
   * @return refereeId
   */
  @javax.annotation.Nullable
  public Integer getRefereeId() {
    return refereeId;
  }

  public void setRefereeId(Integer refereeId) {
    this.refereeId = refereeId;
  }


  public Referee shortName(String shortName) {
    this.shortName = shortName;
    return this;
  }

  /**
   * Get shortName
   * @return shortName
   */
  @javax.annotation.Nullable
  public String getShortName() {
    return shortName;
  }

  public void setShortName(String shortName) {
    this.shortName = shortName;
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
    return Objects.equals(this.firstName, referee.firstName) &&
        Objects.equals(this.lastName, referee.lastName) &&
        Objects.equals(this.nationality, referee.nationality) &&
        Objects.equals(this.refereeId, referee.refereeId) &&
        Objects.equals(this.shortName, referee.shortName);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(firstName, lastName, nationality, refereeId, shortName);
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
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    nationality: ").append(toIndentedString(nationality)).append("\n");
    sb.append("    refereeId: ").append(toIndentedString(refereeId)).append("\n");
    sb.append("    shortName: ").append(toIndentedString(shortName)).append("\n");
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
    openapiFields.add("FirstName");
    openapiFields.add("LastName");
    openapiFields.add("Nationality");
    openapiFields.add("RefereeId");
    openapiFields.add("ShortName");

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
      if ((jsonObj.get("FirstName") != null && !jsonObj.get("FirstName").isJsonNull()) && !jsonObj.get("FirstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `FirstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("FirstName").toString()));
      }
      if ((jsonObj.get("LastName") != null && !jsonObj.get("LastName").isJsonNull()) && !jsonObj.get("LastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `LastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("LastName").toString()));
      }
      if ((jsonObj.get("Nationality") != null && !jsonObj.get("Nationality").isJsonNull()) && !jsonObj.get("Nationality").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Nationality` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Nationality").toString()));
      }
      if ((jsonObj.get("ShortName") != null && !jsonObj.get("ShortName").isJsonNull()) && !jsonObj.get("ShortName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ShortName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ShortName").toString()));
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

