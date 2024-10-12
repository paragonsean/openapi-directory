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
import org.openapitools.client.model.CareContextRepresentation;
import org.openapitools.client.model.IdentifierType;

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
 * PatientRepresentation
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:41.924748-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientRepresentation {
  public static final String SERIALIZED_NAME_CARE_CONTEXTS = "careContexts";
  @SerializedName(SERIALIZED_NAME_CARE_CONTEXTS)
  private List<CareContextRepresentation> careContexts = new ArrayList<>();

  public static final String SERIALIZED_NAME_DISPLAY = "display";
  @SerializedName(SERIALIZED_NAME_DISPLAY)
  private String display;

  public static final String SERIALIZED_NAME_MATCHED_BY = "matchedBy";
  @SerializedName(SERIALIZED_NAME_MATCHED_BY)
  private List<IdentifierType> matchedBy = new ArrayList<>();

  public static final String SERIALIZED_NAME_REFERENCE_NUMBER = "referenceNumber";
  @SerializedName(SERIALIZED_NAME_REFERENCE_NUMBER)
  private String referenceNumber;

  public PatientRepresentation() {
  }

  public PatientRepresentation careContexts(List<CareContextRepresentation> careContexts) {
    this.careContexts = careContexts;
    return this;
  }

  public PatientRepresentation addCareContextsItem(CareContextRepresentation careContextsItem) {
    if (this.careContexts == null) {
      this.careContexts = new ArrayList<>();
    }
    this.careContexts.add(careContextsItem);
    return this;
  }

  /**
   * Get careContexts
   * @return careContexts
   */
  @javax.annotation.Nonnull
  public List<CareContextRepresentation> getCareContexts() {
    return careContexts;
  }

  public void setCareContexts(List<CareContextRepresentation> careContexts) {
    this.careContexts = careContexts;
  }


  public PatientRepresentation display(String display) {
    this.display = display;
    return this;
  }

  /**
   * Get display
   * @return display
   */
  @javax.annotation.Nonnull
  public String getDisplay() {
    return display;
  }

  public void setDisplay(String display) {
    this.display = display;
  }


  public PatientRepresentation matchedBy(List<IdentifierType> matchedBy) {
    this.matchedBy = matchedBy;
    return this;
  }

  public PatientRepresentation addMatchedByItem(IdentifierType matchedByItem) {
    if (this.matchedBy == null) {
      this.matchedBy = new ArrayList<>();
    }
    this.matchedBy.add(matchedByItem);
    return this;
  }

  /**
   * Get matchedBy
   * @return matchedBy
   */
  @javax.annotation.Nullable
  public List<IdentifierType> getMatchedBy() {
    return matchedBy;
  }

  public void setMatchedBy(List<IdentifierType> matchedBy) {
    this.matchedBy = matchedBy;
  }


  public PatientRepresentation referenceNumber(String referenceNumber) {
    this.referenceNumber = referenceNumber;
    return this;
  }

  /**
   * Get referenceNumber
   * @return referenceNumber
   */
  @javax.annotation.Nonnull
  public String getReferenceNumber() {
    return referenceNumber;
  }

  public void setReferenceNumber(String referenceNumber) {
    this.referenceNumber = referenceNumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientRepresentation patientRepresentation = (PatientRepresentation) o;
    return Objects.equals(this.careContexts, patientRepresentation.careContexts) &&
        Objects.equals(this.display, patientRepresentation.display) &&
        Objects.equals(this.matchedBy, patientRepresentation.matchedBy) &&
        Objects.equals(this.referenceNumber, patientRepresentation.referenceNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(careContexts, display, matchedBy, referenceNumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientRepresentation {\n");
    sb.append("    careContexts: ").append(toIndentedString(careContexts)).append("\n");
    sb.append("    display: ").append(toIndentedString(display)).append("\n");
    sb.append("    matchedBy: ").append(toIndentedString(matchedBy)).append("\n");
    sb.append("    referenceNumber: ").append(toIndentedString(referenceNumber)).append("\n");
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
    openapiFields.add("careContexts");
    openapiFields.add("display");
    openapiFields.add("matchedBy");
    openapiFields.add("referenceNumber");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("careContexts");
    openapiRequiredFields.add("display");
    openapiRequiredFields.add("referenceNumber");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientRepresentation
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientRepresentation.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientRepresentation is not found in the empty JSON string", PatientRepresentation.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientRepresentation.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientRepresentation` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientRepresentation.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("careContexts").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `careContexts` to be an array in the JSON string but got `%s`", jsonObj.get("careContexts").toString()));
      }

      JsonArray jsonArraycareContexts = jsonObj.getAsJsonArray("careContexts");
      // validate the required field `careContexts` (array)
      for (int i = 0; i < jsonArraycareContexts.size(); i++) {
        CareContextRepresentation.validateJsonElement(jsonArraycareContexts.get(i));
      };
      if (!jsonObj.get("display").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `display` to be a primitive type in the JSON string but got `%s`", jsonObj.get("display").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("matchedBy") != null && !jsonObj.get("matchedBy").isJsonNull() && !jsonObj.get("matchedBy").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `matchedBy` to be an array in the JSON string but got `%s`", jsonObj.get("matchedBy").toString()));
      }
      if (!jsonObj.get("referenceNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referenceNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referenceNumber").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientRepresentation.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientRepresentation' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientRepresentation> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientRepresentation.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientRepresentation>() {
           @Override
           public void write(JsonWriter out, PatientRepresentation value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientRepresentation read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientRepresentation given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientRepresentation
   * @throws IOException if the JSON string is invalid with respect to PatientRepresentation
   */
  public static PatientRepresentation fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientRepresentation.class);
  }

  /**
   * Convert an instance of PatientRepresentation to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

