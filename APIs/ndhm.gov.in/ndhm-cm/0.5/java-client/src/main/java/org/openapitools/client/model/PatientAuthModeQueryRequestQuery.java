/*
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
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
import java.util.Arrays;
import org.openapitools.client.model.PatientAuthModeQueryRequestQueryRequester;
import org.openapitools.client.model.PatientAuthPurpose;

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
 * PatientAuthModeQueryRequestQuery
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:38.835611-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientAuthModeQueryRequestQuery {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_PURPOSE = "purpose";
  @SerializedName(SERIALIZED_NAME_PURPOSE)
  private PatientAuthPurpose purpose;

  public static final String SERIALIZED_NAME_REQUESTER = "requester";
  @SerializedName(SERIALIZED_NAME_REQUESTER)
  private PatientAuthModeQueryRequestQueryRequester requester;

  public PatientAuthModeQueryRequestQuery() {
  }

  public PatientAuthModeQueryRequestQuery id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public PatientAuthModeQueryRequestQuery purpose(PatientAuthPurpose purpose) {
    this.purpose = purpose;
    return this;
  }

  /**
   * Get purpose
   * @return purpose
   */
  @javax.annotation.Nonnull
  public PatientAuthPurpose getPurpose() {
    return purpose;
  }

  public void setPurpose(PatientAuthPurpose purpose) {
    this.purpose = purpose;
  }


  public PatientAuthModeQueryRequestQuery requester(PatientAuthModeQueryRequestQueryRequester requester) {
    this.requester = requester;
    return this;
  }

  /**
   * Get requester
   * @return requester
   */
  @javax.annotation.Nonnull
  public PatientAuthModeQueryRequestQueryRequester getRequester() {
    return requester;
  }

  public void setRequester(PatientAuthModeQueryRequestQueryRequester requester) {
    this.requester = requester;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientAuthModeQueryRequestQuery patientAuthModeQueryRequestQuery = (PatientAuthModeQueryRequestQuery) o;
    return Objects.equals(this.id, patientAuthModeQueryRequestQuery.id) &&
        Objects.equals(this.purpose, patientAuthModeQueryRequestQuery.purpose) &&
        Objects.equals(this.requester, patientAuthModeQueryRequestQuery.requester);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, purpose, requester);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientAuthModeQueryRequestQuery {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    purpose: ").append(toIndentedString(purpose)).append("\n");
    sb.append("    requester: ").append(toIndentedString(requester)).append("\n");
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
    openapiFields.add("purpose");
    openapiFields.add("requester");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("purpose");
    openapiRequiredFields.add("requester");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientAuthModeQueryRequestQuery
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientAuthModeQueryRequestQuery.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientAuthModeQueryRequestQuery is not found in the empty JSON string", PatientAuthModeQueryRequestQuery.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientAuthModeQueryRequestQuery.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientAuthModeQueryRequestQuery` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientAuthModeQueryRequestQuery.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the required field `purpose`
      PatientAuthPurpose.validateJsonElement(jsonObj.get("purpose"));
      // validate the required field `requester`
      PatientAuthModeQueryRequestQueryRequester.validateJsonElement(jsonObj.get("requester"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientAuthModeQueryRequestQuery.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientAuthModeQueryRequestQuery' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientAuthModeQueryRequestQuery> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientAuthModeQueryRequestQuery.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientAuthModeQueryRequestQuery>() {
           @Override
           public void write(JsonWriter out, PatientAuthModeQueryRequestQuery value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientAuthModeQueryRequestQuery read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientAuthModeQueryRequestQuery given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientAuthModeQueryRequestQuery
   * @throws IOException if the JSON string is invalid with respect to PatientAuthModeQueryRequestQuery
   */
  public static PatientAuthModeQueryRequestQuery fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientAuthModeQueryRequestQuery.class);
  }

  /**
   * Convert an instance of PatientAuthModeQueryRequestQuery to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

