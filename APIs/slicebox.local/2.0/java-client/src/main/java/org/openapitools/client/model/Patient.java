/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
import org.openapitools.client.model.DicomPropertyValue;

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
 * Patient
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:37.231084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Patient {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_PATIENT_BIRTH_DATE = "patientBirthDate";
  @SerializedName(SERIALIZED_NAME_PATIENT_BIRTH_DATE)
  private DicomPropertyValue patientBirthDate;

  public static final String SERIALIZED_NAME_PATIENT_I_D = "patientID";
  @SerializedName(SERIALIZED_NAME_PATIENT_I_D)
  private DicomPropertyValue patientID;

  public static final String SERIALIZED_NAME_PATIENT_NAME = "patientName";
  @SerializedName(SERIALIZED_NAME_PATIENT_NAME)
  private DicomPropertyValue patientName;

  public static final String SERIALIZED_NAME_PATIENT_SEX = "patientSex";
  @SerializedName(SERIALIZED_NAME_PATIENT_SEX)
  private DicomPropertyValue patientSex;

  public Patient() {
  }

  public Patient id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public Patient patientBirthDate(DicomPropertyValue patientBirthDate) {
    this.patientBirthDate = patientBirthDate;
    return this;
  }

  /**
   * Get patientBirthDate
   * @return patientBirthDate
   */
  @javax.annotation.Nullable
  public DicomPropertyValue getPatientBirthDate() {
    return patientBirthDate;
  }

  public void setPatientBirthDate(DicomPropertyValue patientBirthDate) {
    this.patientBirthDate = patientBirthDate;
  }


  public Patient patientID(DicomPropertyValue patientID) {
    this.patientID = patientID;
    return this;
  }

  /**
   * Get patientID
   * @return patientID
   */
  @javax.annotation.Nullable
  public DicomPropertyValue getPatientID() {
    return patientID;
  }

  public void setPatientID(DicomPropertyValue patientID) {
    this.patientID = patientID;
  }


  public Patient patientName(DicomPropertyValue patientName) {
    this.patientName = patientName;
    return this;
  }

  /**
   * Get patientName
   * @return patientName
   */
  @javax.annotation.Nullable
  public DicomPropertyValue getPatientName() {
    return patientName;
  }

  public void setPatientName(DicomPropertyValue patientName) {
    this.patientName = patientName;
  }


  public Patient patientSex(DicomPropertyValue patientSex) {
    this.patientSex = patientSex;
    return this;
  }

  /**
   * Get patientSex
   * @return patientSex
   */
  @javax.annotation.Nullable
  public DicomPropertyValue getPatientSex() {
    return patientSex;
  }

  public void setPatientSex(DicomPropertyValue patientSex) {
    this.patientSex = patientSex;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Patient patient = (Patient) o;
    return Objects.equals(this.id, patient.id) &&
        Objects.equals(this.patientBirthDate, patient.patientBirthDate) &&
        Objects.equals(this.patientID, patient.patientID) &&
        Objects.equals(this.patientName, patient.patientName) &&
        Objects.equals(this.patientSex, patient.patientSex);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, patientBirthDate, patientID, patientName, patientSex);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Patient {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    patientBirthDate: ").append(toIndentedString(patientBirthDate)).append("\n");
    sb.append("    patientID: ").append(toIndentedString(patientID)).append("\n");
    sb.append("    patientName: ").append(toIndentedString(patientName)).append("\n");
    sb.append("    patientSex: ").append(toIndentedString(patientSex)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("patientBirthDate");
    openapiFields.add("patientID");
    openapiFields.add("patientName");
    openapiFields.add("patientSex");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Patient
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Patient.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Patient is not found in the empty JSON string", Patient.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Patient.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Patient` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `patientBirthDate`
      if (jsonObj.get("patientBirthDate") != null && !jsonObj.get("patientBirthDate").isJsonNull()) {
        DicomPropertyValue.validateJsonElement(jsonObj.get("patientBirthDate"));
      }
      // validate the optional field `patientID`
      if (jsonObj.get("patientID") != null && !jsonObj.get("patientID").isJsonNull()) {
        DicomPropertyValue.validateJsonElement(jsonObj.get("patientID"));
      }
      // validate the optional field `patientName`
      if (jsonObj.get("patientName") != null && !jsonObj.get("patientName").isJsonNull()) {
        DicomPropertyValue.validateJsonElement(jsonObj.get("patientName"));
      }
      // validate the optional field `patientSex`
      if (jsonObj.get("patientSex") != null && !jsonObj.get("patientSex").isJsonNull()) {
        DicomPropertyValue.validateJsonElement(jsonObj.get("patientSex"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Patient.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Patient' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Patient> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Patient.class));

       return (TypeAdapter<T>) new TypeAdapter<Patient>() {
           @Override
           public void write(JsonWriter out, Patient value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Patient read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Patient given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Patient
   * @throws IOException if the JSON string is invalid with respect to Patient
   */
  public static Patient fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Patient.class);
  }

  /**
   * Convert an instance of Patient to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

