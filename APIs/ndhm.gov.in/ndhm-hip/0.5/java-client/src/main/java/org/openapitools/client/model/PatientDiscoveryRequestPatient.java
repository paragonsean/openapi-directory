/*
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
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
import org.openapitools.client.model.Identifier;

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
 * PatientDiscoveryRequestPatient
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:41.924748-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientDiscoveryRequestPatient {
  /**
   * Gets or Sets gender
   */
  @JsonAdapter(GenderEnum.Adapter.class)
  public enum GenderEnum {
    M("M"),
    
    F("F"),
    
    O("O"),
    
    U("U");

    private String value;

    GenderEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GenderEnum fromValue(String value) {
      for (GenderEnum b : GenderEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<GenderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GenderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GenderEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GenderEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GenderEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private GenderEnum gender;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_UNVERIFIED_IDENTIFIERS = "unverifiedIdentifiers";
  @SerializedName(SERIALIZED_NAME_UNVERIFIED_IDENTIFIERS)
  private List<Identifier> unverifiedIdentifiers = new ArrayList<>();

  public static final String SERIALIZED_NAME_VERIFIED_IDENTIFIERS = "verifiedIdentifiers";
  @SerializedName(SERIALIZED_NAME_VERIFIED_IDENTIFIERS)
  private List<Identifier> verifiedIdentifiers = new ArrayList<>();

  public static final String SERIALIZED_NAME_YEAR_OF_BIRTH = "yearOfBirth";
  @SerializedName(SERIALIZED_NAME_YEAR_OF_BIRTH)
  private Integer yearOfBirth;

  public PatientDiscoveryRequestPatient() {
  }

  public PatientDiscoveryRequestPatient gender(GenderEnum gender) {
    this.gender = gender;
    return this;
  }

  /**
   * Get gender
   * @return gender
   */
  @javax.annotation.Nonnull
  public GenderEnum getGender() {
    return gender;
  }

  public void setGender(GenderEnum gender) {
    this.gender = gender;
  }


  public PatientDiscoveryRequestPatient id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Identifier of patient at consent manager
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public PatientDiscoveryRequestPatient name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PatientDiscoveryRequestPatient unverifiedIdentifiers(List<Identifier> unverifiedIdentifiers) {
    this.unverifiedIdentifiers = unverifiedIdentifiers;
    return this;
  }

  public PatientDiscoveryRequestPatient addUnverifiedIdentifiersItem(Identifier unverifiedIdentifiersItem) {
    if (this.unverifiedIdentifiers == null) {
      this.unverifiedIdentifiers = new ArrayList<>();
    }
    this.unverifiedIdentifiers.add(unverifiedIdentifiersItem);
    return this;
  }

  /**
   * Get unverifiedIdentifiers
   * @return unverifiedIdentifiers
   */
  @javax.annotation.Nullable
  public List<Identifier> getUnverifiedIdentifiers() {
    return unverifiedIdentifiers;
  }

  public void setUnverifiedIdentifiers(List<Identifier> unverifiedIdentifiers) {
    this.unverifiedIdentifiers = unverifiedIdentifiers;
  }


  public PatientDiscoveryRequestPatient verifiedIdentifiers(List<Identifier> verifiedIdentifiers) {
    this.verifiedIdentifiers = verifiedIdentifiers;
    return this;
  }

  public PatientDiscoveryRequestPatient addVerifiedIdentifiersItem(Identifier verifiedIdentifiersItem) {
    if (this.verifiedIdentifiers == null) {
      this.verifiedIdentifiers = new ArrayList<>();
    }
    this.verifiedIdentifiers.add(verifiedIdentifiersItem);
    return this;
  }

  /**
   * Get verifiedIdentifiers
   * @return verifiedIdentifiers
   */
  @javax.annotation.Nonnull
  public List<Identifier> getVerifiedIdentifiers() {
    return verifiedIdentifiers;
  }

  public void setVerifiedIdentifiers(List<Identifier> verifiedIdentifiers) {
    this.verifiedIdentifiers = verifiedIdentifiers;
  }


  public PatientDiscoveryRequestPatient yearOfBirth(Integer yearOfBirth) {
    this.yearOfBirth = yearOfBirth;
    return this;
  }

  /**
   * Get yearOfBirth
   * @return yearOfBirth
   */
  @javax.annotation.Nonnull
  public Integer getYearOfBirth() {
    return yearOfBirth;
  }

  public void setYearOfBirth(Integer yearOfBirth) {
    this.yearOfBirth = yearOfBirth;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientDiscoveryRequestPatient patientDiscoveryRequestPatient = (PatientDiscoveryRequestPatient) o;
    return Objects.equals(this.gender, patientDiscoveryRequestPatient.gender) &&
        Objects.equals(this.id, patientDiscoveryRequestPatient.id) &&
        Objects.equals(this.name, patientDiscoveryRequestPatient.name) &&
        Objects.equals(this.unverifiedIdentifiers, patientDiscoveryRequestPatient.unverifiedIdentifiers) &&
        Objects.equals(this.verifiedIdentifiers, patientDiscoveryRequestPatient.verifiedIdentifiers) &&
        Objects.equals(this.yearOfBirth, patientDiscoveryRequestPatient.yearOfBirth);
  }

  @Override
  public int hashCode() {
    return Objects.hash(gender, id, name, unverifiedIdentifiers, verifiedIdentifiers, yearOfBirth);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientDiscoveryRequestPatient {\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    unverifiedIdentifiers: ").append(toIndentedString(unverifiedIdentifiers)).append("\n");
    sb.append("    verifiedIdentifiers: ").append(toIndentedString(verifiedIdentifiers)).append("\n");
    sb.append("    yearOfBirth: ").append(toIndentedString(yearOfBirth)).append("\n");
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
    openapiFields.add("gender");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("unverifiedIdentifiers");
    openapiFields.add("verifiedIdentifiers");
    openapiFields.add("yearOfBirth");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("gender");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("verifiedIdentifiers");
    openapiRequiredFields.add("yearOfBirth");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientDiscoveryRequestPatient
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientDiscoveryRequestPatient.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientDiscoveryRequestPatient is not found in the empty JSON string", PatientDiscoveryRequestPatient.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientDiscoveryRequestPatient.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientDiscoveryRequestPatient` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientDiscoveryRequestPatient.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      // validate the required field `gender`
      GenderEnum.validateJsonElement(jsonObj.get("gender"));
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("unverifiedIdentifiers") != null && !jsonObj.get("unverifiedIdentifiers").isJsonNull()) {
        JsonArray jsonArrayunverifiedIdentifiers = jsonObj.getAsJsonArray("unverifiedIdentifiers");
        if (jsonArrayunverifiedIdentifiers != null) {
          // ensure the json data is an array
          if (!jsonObj.get("unverifiedIdentifiers").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `unverifiedIdentifiers` to be an array in the JSON string but got `%s`", jsonObj.get("unverifiedIdentifiers").toString()));
          }

          // validate the optional field `unverifiedIdentifiers` (array)
          for (int i = 0; i < jsonArrayunverifiedIdentifiers.size(); i++) {
            Identifier.validateJsonElement(jsonArrayunverifiedIdentifiers.get(i));
          };
        }
      }
      // ensure the json data is an array
      if (!jsonObj.get("verifiedIdentifiers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `verifiedIdentifiers` to be an array in the JSON string but got `%s`", jsonObj.get("verifiedIdentifiers").toString()));
      }

      JsonArray jsonArrayverifiedIdentifiers = jsonObj.getAsJsonArray("verifiedIdentifiers");
      // validate the required field `verifiedIdentifiers` (array)
      for (int i = 0; i < jsonArrayverifiedIdentifiers.size(); i++) {
        Identifier.validateJsonElement(jsonArrayverifiedIdentifiers.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientDiscoveryRequestPatient.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientDiscoveryRequestPatient' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientDiscoveryRequestPatient> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientDiscoveryRequestPatient.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientDiscoveryRequestPatient>() {
           @Override
           public void write(JsonWriter out, PatientDiscoveryRequestPatient value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientDiscoveryRequestPatient read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientDiscoveryRequestPatient given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientDiscoveryRequestPatient
   * @throws IOException if the JSON string is invalid with respect to PatientDiscoveryRequestPatient
   */
  public static PatientDiscoveryRequestPatient fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientDiscoveryRequestPatient.class);
  }

  /**
   * Convert an instance of PatientDiscoveryRequestPatient to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

