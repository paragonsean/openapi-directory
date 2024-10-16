/*
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
 * CriticalIllnessInsurancePolicyModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CriticalIllnessInsurancePolicyModel {
  public static final String SERIALIZED_NAME_BENEFIT = "benefit";
  @SerializedName(SERIALIZED_NAME_BENEFIT)
  private Double benefit;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXTERNAL_DESTINATION_ID = "externalDestinationId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DESTINATION_ID)
  private String externalDestinationId;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

  public static final String SERIALIZED_NAME_FREQUENCY = "frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private Integer frequency;

  /**
   * Gets or Sets insured
   */
  @JsonAdapter(InsuredEnum.Adapter.class)
  public enum InsuredEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient");

    private String value;

    InsuredEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static InsuredEnum fromValue(String value) {
      for (InsuredEnum b : InsuredEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<InsuredEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final InsuredEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public InsuredEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return InsuredEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      InsuredEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_INSURED = "insured";
  @SerializedName(SERIALIZED_NAME_INSURED)
  private InsuredEnum insured;

  public static final String SERIALIZED_NAME_POLICY_TYPE = "policyType";
  @SerializedName(SERIALIZED_NAME_POLICY_TYPE)
  private Integer policyType;

  public static final String SERIALIZED_NAME_PREMIUM = "premium";
  @SerializedName(SERIALIZED_NAME_PREMIUM)
  private Double premium;

  public CriticalIllnessInsurancePolicyModel() {
  }

  public CriticalIllnessInsurancePolicyModel benefit(Double benefit) {
    this.benefit = benefit;
    return this;
  }

  /**
   * Get benefit
   * @return benefit
   */
  @javax.annotation.Nullable
  public Double getBenefit() {
    return benefit;
  }

  public void setBenefit(Double benefit) {
    this.benefit = benefit;
  }


  public CriticalIllnessInsurancePolicyModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nonnull
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public CriticalIllnessInsurancePolicyModel externalDestinationId(String externalDestinationId) {
    this.externalDestinationId = externalDestinationId;
    return this;
  }

  /**
   * Get externalDestinationId
   * @return externalDestinationId
   */
  @javax.annotation.Nullable
  public String getExternalDestinationId() {
    return externalDestinationId;
  }

  public void setExternalDestinationId(String externalDestinationId) {
    this.externalDestinationId = externalDestinationId;
  }


  public CriticalIllnessInsurancePolicyModel factFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
    return this;
  }

  /**
   * Get factFinderId
   * @return factFinderId
   */
  @javax.annotation.Nonnull
  public Integer getFactFinderId() {
    return factFinderId;
  }

  public void setFactFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
  }


  public CriticalIllnessInsurancePolicyModel frequency(Integer frequency) {
    this.frequency = frequency;
    return this;
  }

  /**
   * Get frequency
   * @return frequency
   */
  @javax.annotation.Nullable
  public Integer getFrequency() {
    return frequency;
  }

  public void setFrequency(Integer frequency) {
    this.frequency = frequency;
  }


  public CriticalIllnessInsurancePolicyModel insured(InsuredEnum insured) {
    this.insured = insured;
    return this;
  }

  /**
   * Get insured
   * @return insured
   */
  @javax.annotation.Nullable
  public InsuredEnum getInsured() {
    return insured;
  }

  public void setInsured(InsuredEnum insured) {
    this.insured = insured;
  }


  public CriticalIllnessInsurancePolicyModel policyType(Integer policyType) {
    this.policyType = policyType;
    return this;
  }

  /**
   * Get policyType
   * @return policyType
   */
  @javax.annotation.Nullable
  public Integer getPolicyType() {
    return policyType;
  }

  public void setPolicyType(Integer policyType) {
    this.policyType = policyType;
  }


  public CriticalIllnessInsurancePolicyModel premium(Double premium) {
    this.premium = premium;
    return this;
  }

  /**
   * Get premium
   * @return premium
   */
  @javax.annotation.Nullable
  public Double getPremium() {
    return premium;
  }

  public void setPremium(Double premium) {
    this.premium = premium;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CriticalIllnessInsurancePolicyModel criticalIllnessInsurancePolicyModel = (CriticalIllnessInsurancePolicyModel) o;
    return Objects.equals(this.benefit, criticalIllnessInsurancePolicyModel.benefit) &&
        Objects.equals(this.description, criticalIllnessInsurancePolicyModel.description) &&
        Objects.equals(this.externalDestinationId, criticalIllnessInsurancePolicyModel.externalDestinationId) &&
        Objects.equals(this.factFinderId, criticalIllnessInsurancePolicyModel.factFinderId) &&
        Objects.equals(this.frequency, criticalIllnessInsurancePolicyModel.frequency) &&
        Objects.equals(this.insured, criticalIllnessInsurancePolicyModel.insured) &&
        Objects.equals(this.policyType, criticalIllnessInsurancePolicyModel.policyType) &&
        Objects.equals(this.premium, criticalIllnessInsurancePolicyModel.premium);
  }

  @Override
  public int hashCode() {
    return Objects.hash(benefit, description, externalDestinationId, factFinderId, frequency, insured, policyType, premium);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CriticalIllnessInsurancePolicyModel {\n");
    sb.append("    benefit: ").append(toIndentedString(benefit)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    insured: ").append(toIndentedString(insured)).append("\n");
    sb.append("    policyType: ").append(toIndentedString(policyType)).append("\n");
    sb.append("    premium: ").append(toIndentedString(premium)).append("\n");
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
    openapiFields.add("benefit");
    openapiFields.add("description");
    openapiFields.add("externalDestinationId");
    openapiFields.add("factFinderId");
    openapiFields.add("frequency");
    openapiFields.add("insured");
    openapiFields.add("policyType");
    openapiFields.add("premium");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("factFinderId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CriticalIllnessInsurancePolicyModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CriticalIllnessInsurancePolicyModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CriticalIllnessInsurancePolicyModel is not found in the empty JSON string", CriticalIllnessInsurancePolicyModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CriticalIllnessInsurancePolicyModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CriticalIllnessInsurancePolicyModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CriticalIllnessInsurancePolicyModel.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("externalDestinationId") != null && !jsonObj.get("externalDestinationId").isJsonNull()) && !jsonObj.get("externalDestinationId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalDestinationId").toString()));
      }
      if ((jsonObj.get("insured") != null && !jsonObj.get("insured").isJsonNull()) && !jsonObj.get("insured").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insured` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insured").toString()));
      }
      // validate the optional field `insured`
      if (jsonObj.get("insured") != null && !jsonObj.get("insured").isJsonNull()) {
        InsuredEnum.validateJsonElement(jsonObj.get("insured"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CriticalIllnessInsurancePolicyModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CriticalIllnessInsurancePolicyModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CriticalIllnessInsurancePolicyModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CriticalIllnessInsurancePolicyModel.class));

       return (TypeAdapter<T>) new TypeAdapter<CriticalIllnessInsurancePolicyModel>() {
           @Override
           public void write(JsonWriter out, CriticalIllnessInsurancePolicyModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CriticalIllnessInsurancePolicyModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CriticalIllnessInsurancePolicyModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CriticalIllnessInsurancePolicyModel
   * @throws IOException if the JSON string is invalid with respect to CriticalIllnessInsurancePolicyModel
   */
  public static CriticalIllnessInsurancePolicyModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CriticalIllnessInsurancePolicyModel.class);
  }

  /**
   * Convert an instance of CriticalIllnessInsurancePolicyModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

