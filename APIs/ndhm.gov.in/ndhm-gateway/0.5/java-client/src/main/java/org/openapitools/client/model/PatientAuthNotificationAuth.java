/*
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
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
import org.openapitools.client.model.AccessTokenValidity;
import org.openapitools.client.model.PatientDemographicResponse;

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
 * depending on the purpose of auth, as specified in /auth/init, the response may include the following    1. LINK - only returns **accessToken**   2. KYC - only returns **patient**   3. KYC_AND_LINK - returns both **accessToken** and **patient** 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:45.290770-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientAuthNotificationAuth {
  public static final String SERIALIZED_NAME_ACCESS_TOKEN = "accessToken";
  @SerializedName(SERIALIZED_NAME_ACCESS_TOKEN)
  private String accessToken;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private PatientDemographicResponse patient;

  /**
   * Gets or Sets status
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    GRANTED("GRANTED"),
    
    DENIED("DENIED");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_TRANSACTION_ID = "transactionId";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_ID)
  private String transactionId;

  public static final String SERIALIZED_NAME_VALIDITY = "validity";
  @SerializedName(SERIALIZED_NAME_VALIDITY)
  private AccessTokenValidity validity;

  public PatientAuthNotificationAuth() {
  }

  public PatientAuthNotificationAuth accessToken(String accessToken) {
    this.accessToken = accessToken;
    return this;
  }

  /**
   * access token for initialization of subsequent action.
   * @return accessToken
   */
  @javax.annotation.Nullable
  public String getAccessToken() {
    return accessToken;
  }

  public void setAccessToken(String accessToken) {
    this.accessToken = accessToken;
  }


  public PatientAuthNotificationAuth patient(PatientDemographicResponse patient) {
    this.patient = patient;
    return this;
  }

  /**
   * Get patient
   * @return patient
   */
  @javax.annotation.Nullable
  public PatientDemographicResponse getPatient() {
    return patient;
  }

  public void setPatient(PatientDemographicResponse patient) {
    this.patient = patient;
  }


  public PatientAuthNotificationAuth status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public PatientAuthNotificationAuth transactionId(String transactionId) {
    this.transactionId = transactionId;
    return this;
  }

  /**
   * transaction id for auth session
   * @return transactionId
   */
  @javax.annotation.Nonnull
  public String getTransactionId() {
    return transactionId;
  }

  public void setTransactionId(String transactionId) {
    this.transactionId = transactionId;
  }


  public PatientAuthNotificationAuth validity(AccessTokenValidity validity) {
    this.validity = validity;
    return this;
  }

  /**
   * Get validity
   * @return validity
   */
  @javax.annotation.Nullable
  public AccessTokenValidity getValidity() {
    return validity;
  }

  public void setValidity(AccessTokenValidity validity) {
    this.validity = validity;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientAuthNotificationAuth patientAuthNotificationAuth = (PatientAuthNotificationAuth) o;
    return Objects.equals(this.accessToken, patientAuthNotificationAuth.accessToken) &&
        Objects.equals(this.patient, patientAuthNotificationAuth.patient) &&
        Objects.equals(this.status, patientAuthNotificationAuth.status) &&
        Objects.equals(this.transactionId, patientAuthNotificationAuth.transactionId) &&
        Objects.equals(this.validity, patientAuthNotificationAuth.validity);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accessToken, patient, status, transactionId, validity);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientAuthNotificationAuth {\n");
    sb.append("    accessToken: ").append(toIndentedString(accessToken)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
    sb.append("    validity: ").append(toIndentedString(validity)).append("\n");
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
    openapiFields.add("accessToken");
    openapiFields.add("patient");
    openapiFields.add("status");
    openapiFields.add("transactionId");
    openapiFields.add("validity");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("transactionId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientAuthNotificationAuth
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientAuthNotificationAuth.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientAuthNotificationAuth is not found in the empty JSON string", PatientAuthNotificationAuth.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientAuthNotificationAuth.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientAuthNotificationAuth` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientAuthNotificationAuth.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("accessToken") != null && !jsonObj.get("accessToken").isJsonNull()) && !jsonObj.get("accessToken").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accessToken` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accessToken").toString()));
      }
      // validate the optional field `patient`
      if (jsonObj.get("patient") != null && !jsonObj.get("patient").isJsonNull()) {
        PatientDemographicResponse.validateJsonElement(jsonObj.get("patient"));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      if (!jsonObj.get("transactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactionId").toString()));
      }
      // validate the optional field `validity`
      if (jsonObj.get("validity") != null && !jsonObj.get("validity").isJsonNull()) {
        AccessTokenValidity.validateJsonElement(jsonObj.get("validity"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientAuthNotificationAuth.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientAuthNotificationAuth' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientAuthNotificationAuth> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientAuthNotificationAuth.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientAuthNotificationAuth>() {
           @Override
           public void write(JsonWriter out, PatientAuthNotificationAuth value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientAuthNotificationAuth read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientAuthNotificationAuth given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientAuthNotificationAuth
   * @throws IOException if the JSON string is invalid with respect to PatientAuthNotificationAuth
   */
  public static PatientAuthNotificationAuth fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientAuthNotificationAuth.class);
  }

  /**
   * Convert an instance of PatientAuthNotificationAuth to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

