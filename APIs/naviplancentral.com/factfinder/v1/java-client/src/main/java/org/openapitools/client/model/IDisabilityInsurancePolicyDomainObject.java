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
 * IDisabilityInsurancePolicyDomainObject
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IDisabilityInsurancePolicyDomainObject {
  public static final String SERIALIZED_NAME_BENEFIT = "benefit";
  @SerializedName(SERIALIZED_NAME_BENEFIT)
  private Double benefit;

  public static final String SERIALIZED_NAME_BENEFIT_FREQUENCY = "benefitFrequency";
  @SerializedName(SERIALIZED_NAME_BENEFIT_FREQUENCY)
  private Integer benefitFrequency;

  /**
   * Gets or Sets benefitType
   */
  @JsonAdapter(BenefitTypeEnum.Adapter.class)
  public enum BenefitTypeEnum {
    DOLLAR("Dollar"),
    
    PERCENT("Percent");

    private String value;

    BenefitTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BenefitTypeEnum fromValue(String value) {
      for (BenefitTypeEnum b : BenefitTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BenefitTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BenefitTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BenefitTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BenefitTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BenefitTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BENEFIT_TYPE = "benefitType";
  @SerializedName(SERIALIZED_NAME_BENEFIT_TYPE)
  private BenefitTypeEnum benefitType;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISABILITY_INSURANCE_POLICY_ID = "disabilityInsurancePolicyId";
  @SerializedName(SERIALIZED_NAME_DISABILITY_INSURANCE_POLICY_ID)
  private Integer disabilityInsurancePolicyId;

  public static final String SERIALIZED_NAME_EXTERNAL_DESTINATION_ID = "externalDestinationId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DESTINATION_ID)
  private String externalDestinationId;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

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

  public static final String SERIALIZED_NAME_PREMIUM_FREQUENCY = "premiumFrequency";
  @SerializedName(SERIALIZED_NAME_PREMIUM_FREQUENCY)
  private Integer premiumFrequency;

  public IDisabilityInsurancePolicyDomainObject() {
  }

  public IDisabilityInsurancePolicyDomainObject benefit(Double benefit) {
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


  public IDisabilityInsurancePolicyDomainObject benefitFrequency(Integer benefitFrequency) {
    this.benefitFrequency = benefitFrequency;
    return this;
  }

  /**
   * Get benefitFrequency
   * @return benefitFrequency
   */
  @javax.annotation.Nullable
  public Integer getBenefitFrequency() {
    return benefitFrequency;
  }

  public void setBenefitFrequency(Integer benefitFrequency) {
    this.benefitFrequency = benefitFrequency;
  }


  public IDisabilityInsurancePolicyDomainObject benefitType(BenefitTypeEnum benefitType) {
    this.benefitType = benefitType;
    return this;
  }

  /**
   * Get benefitType
   * @return benefitType
   */
  @javax.annotation.Nullable
  public BenefitTypeEnum getBenefitType() {
    return benefitType;
  }

  public void setBenefitType(BenefitTypeEnum benefitType) {
    this.benefitType = benefitType;
  }


  public IDisabilityInsurancePolicyDomainObject description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public IDisabilityInsurancePolicyDomainObject disabilityInsurancePolicyId(Integer disabilityInsurancePolicyId) {
    this.disabilityInsurancePolicyId = disabilityInsurancePolicyId;
    return this;
  }

  /**
   * Get disabilityInsurancePolicyId
   * @return disabilityInsurancePolicyId
   */
  @javax.annotation.Nullable
  public Integer getDisabilityInsurancePolicyId() {
    return disabilityInsurancePolicyId;
  }

  public void setDisabilityInsurancePolicyId(Integer disabilityInsurancePolicyId) {
    this.disabilityInsurancePolicyId = disabilityInsurancePolicyId;
  }


  public IDisabilityInsurancePolicyDomainObject externalDestinationId(String externalDestinationId) {
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


  public IDisabilityInsurancePolicyDomainObject factFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
    return this;
  }

  /**
   * Get factFinderId
   * @return factFinderId
   */
  @javax.annotation.Nullable
  public Integer getFactFinderId() {
    return factFinderId;
  }

  public void setFactFinderId(Integer factFinderId) {
    this.factFinderId = factFinderId;
  }


  public IDisabilityInsurancePolicyDomainObject insured(InsuredEnum insured) {
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


  public IDisabilityInsurancePolicyDomainObject policyType(Integer policyType) {
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


  public IDisabilityInsurancePolicyDomainObject premium(Double premium) {
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


  public IDisabilityInsurancePolicyDomainObject premiumFrequency(Integer premiumFrequency) {
    this.premiumFrequency = premiumFrequency;
    return this;
  }

  /**
   * Get premiumFrequency
   * @return premiumFrequency
   */
  @javax.annotation.Nullable
  public Integer getPremiumFrequency() {
    return premiumFrequency;
  }

  public void setPremiumFrequency(Integer premiumFrequency) {
    this.premiumFrequency = premiumFrequency;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    IDisabilityInsurancePolicyDomainObject idisabilityInsurancePolicyDomainObject = (IDisabilityInsurancePolicyDomainObject) o;
    return Objects.equals(this.benefit, idisabilityInsurancePolicyDomainObject.benefit) &&
        Objects.equals(this.benefitFrequency, idisabilityInsurancePolicyDomainObject.benefitFrequency) &&
        Objects.equals(this.benefitType, idisabilityInsurancePolicyDomainObject.benefitType) &&
        Objects.equals(this.description, idisabilityInsurancePolicyDomainObject.description) &&
        Objects.equals(this.disabilityInsurancePolicyId, idisabilityInsurancePolicyDomainObject.disabilityInsurancePolicyId) &&
        Objects.equals(this.externalDestinationId, idisabilityInsurancePolicyDomainObject.externalDestinationId) &&
        Objects.equals(this.factFinderId, idisabilityInsurancePolicyDomainObject.factFinderId) &&
        Objects.equals(this.insured, idisabilityInsurancePolicyDomainObject.insured) &&
        Objects.equals(this.policyType, idisabilityInsurancePolicyDomainObject.policyType) &&
        Objects.equals(this.premium, idisabilityInsurancePolicyDomainObject.premium) &&
        Objects.equals(this.premiumFrequency, idisabilityInsurancePolicyDomainObject.premiumFrequency);
  }

  @Override
  public int hashCode() {
    return Objects.hash(benefit, benefitFrequency, benefitType, description, disabilityInsurancePolicyId, externalDestinationId, factFinderId, insured, policyType, premium, premiumFrequency);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IDisabilityInsurancePolicyDomainObject {\n");
    sb.append("    benefit: ").append(toIndentedString(benefit)).append("\n");
    sb.append("    benefitFrequency: ").append(toIndentedString(benefitFrequency)).append("\n");
    sb.append("    benefitType: ").append(toIndentedString(benefitType)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    disabilityInsurancePolicyId: ").append(toIndentedString(disabilityInsurancePolicyId)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    insured: ").append(toIndentedString(insured)).append("\n");
    sb.append("    policyType: ").append(toIndentedString(policyType)).append("\n");
    sb.append("    premium: ").append(toIndentedString(premium)).append("\n");
    sb.append("    premiumFrequency: ").append(toIndentedString(premiumFrequency)).append("\n");
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
    openapiFields.add("benefitFrequency");
    openapiFields.add("benefitType");
    openapiFields.add("description");
    openapiFields.add("disabilityInsurancePolicyId");
    openapiFields.add("externalDestinationId");
    openapiFields.add("factFinderId");
    openapiFields.add("insured");
    openapiFields.add("policyType");
    openapiFields.add("premium");
    openapiFields.add("premiumFrequency");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IDisabilityInsurancePolicyDomainObject
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IDisabilityInsurancePolicyDomainObject.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IDisabilityInsurancePolicyDomainObject is not found in the empty JSON string", IDisabilityInsurancePolicyDomainObject.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IDisabilityInsurancePolicyDomainObject.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IDisabilityInsurancePolicyDomainObject` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("benefitType") != null && !jsonObj.get("benefitType").isJsonNull()) && !jsonObj.get("benefitType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `benefitType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("benefitType").toString()));
      }
      // validate the optional field `benefitType`
      if (jsonObj.get("benefitType") != null && !jsonObj.get("benefitType").isJsonNull()) {
        BenefitTypeEnum.validateJsonElement(jsonObj.get("benefitType"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
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
       if (!IDisabilityInsurancePolicyDomainObject.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IDisabilityInsurancePolicyDomainObject' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IDisabilityInsurancePolicyDomainObject> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IDisabilityInsurancePolicyDomainObject.class));

       return (TypeAdapter<T>) new TypeAdapter<IDisabilityInsurancePolicyDomainObject>() {
           @Override
           public void write(JsonWriter out, IDisabilityInsurancePolicyDomainObject value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IDisabilityInsurancePolicyDomainObject read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IDisabilityInsurancePolicyDomainObject given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IDisabilityInsurancePolicyDomainObject
   * @throws IOException if the JSON string is invalid with respect to IDisabilityInsurancePolicyDomainObject
   */
  public static IDisabilityInsurancePolicyDomainObject fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IDisabilityInsurancePolicyDomainObject.class);
  }

  /**
   * Convert an instance of IDisabilityInsurancePolicyDomainObject to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

