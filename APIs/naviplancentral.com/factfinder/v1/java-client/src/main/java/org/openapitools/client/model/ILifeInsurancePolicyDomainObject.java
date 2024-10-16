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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.LifeInsurancePolicySubaccountDomainObject;

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
 * ILifeInsurancePolicyDomainObject
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ILifeInsurancePolicyDomainObject {
  /**
   * Gets or Sets beneficiary
   */
  @JsonAdapter(BeneficiaryEnum.Adapter.class)
  public enum BeneficiaryEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient"),
    
    DEPENDENT("Dependent"),
    
    OTHER("Other");

    private String value;

    BeneficiaryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static BeneficiaryEnum fromValue(String value) {
      for (BeneficiaryEnum b : BeneficiaryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<BeneficiaryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final BeneficiaryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public BeneficiaryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return BeneficiaryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      BeneficiaryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_BENEFICIARY = "beneficiary";
  @SerializedName(SERIALIZED_NAME_BENEFICIARY)
  private BeneficiaryEnum beneficiary;

  public static final String SERIALIZED_NAME_BENEFICIARY_DEPENDENT_ID = "beneficiaryDependentId";
  @SerializedName(SERIALIZED_NAME_BENEFICIARY_DEPENDENT_ID)
  private Integer beneficiaryDependentId;

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

  public static final String SERIALIZED_NAME_GENERAL_ACCOUNT_MARKET_VALUE = "generalAccountMarketValue";
  @SerializedName(SERIALIZED_NAME_GENERAL_ACCOUNT_MARKET_VALUE)
  private Double generalAccountMarketValue;

  /**
   * Gets or Sets insured
   */
  @JsonAdapter(InsuredEnum.Adapter.class)
  public enum InsuredEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient"),
    
    FIRST_TO_DIE("FirstToDie"),
    
    SECOND_TO_DIE("SecondToDie"),
    
    OTHER("Other");

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

  public static final String SERIALIZED_NAME_LIFE_INSURANCE_POLICY_ID = "lifeInsurancePolicyId";
  @SerializedName(SERIALIZED_NAME_LIFE_INSURANCE_POLICY_ID)
  private Integer lifeInsurancePolicyId;

  /**
   * Gets or Sets payer
   */
  @JsonAdapter(PayerEnum.Adapter.class)
  public enum PayerEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient"),
    
    JOINT("Joint"),
    
    OTHER("Other");

    private String value;

    PayerEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PayerEnum fromValue(String value) {
      for (PayerEnum b : PayerEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PayerEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PayerEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PayerEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PayerEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PayerEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PAYER = "payer";
  @SerializedName(SERIALIZED_NAME_PAYER)
  private PayerEnum payer;

  public static final String SERIALIZED_NAME_POLICY_TYPE = "policyType";
  @SerializedName(SERIALIZED_NAME_POLICY_TYPE)
  private Integer policyType;

  public static final String SERIALIZED_NAME_PREMIUM = "premium";
  @SerializedName(SERIALIZED_NAME_PREMIUM)
  private Double premium;

  public static final String SERIALIZED_NAME_SUBACCOUNTS = "subaccounts";
  @SerializedName(SERIALIZED_NAME_SUBACCOUNTS)
  private List<LifeInsurancePolicySubaccountDomainObject> subaccounts = new ArrayList<>();

  public ILifeInsurancePolicyDomainObject() {
  }

  public ILifeInsurancePolicyDomainObject beneficiary(BeneficiaryEnum beneficiary) {
    this.beneficiary = beneficiary;
    return this;
  }

  /**
   * Get beneficiary
   * @return beneficiary
   */
  @javax.annotation.Nullable
  public BeneficiaryEnum getBeneficiary() {
    return beneficiary;
  }

  public void setBeneficiary(BeneficiaryEnum beneficiary) {
    this.beneficiary = beneficiary;
  }


  public ILifeInsurancePolicyDomainObject beneficiaryDependentId(Integer beneficiaryDependentId) {
    this.beneficiaryDependentId = beneficiaryDependentId;
    return this;
  }

  /**
   * Get beneficiaryDependentId
   * @return beneficiaryDependentId
   */
  @javax.annotation.Nullable
  public Integer getBeneficiaryDependentId() {
    return beneficiaryDependentId;
  }

  public void setBeneficiaryDependentId(Integer beneficiaryDependentId) {
    this.beneficiaryDependentId = beneficiaryDependentId;
  }


  public ILifeInsurancePolicyDomainObject benefit(Double benefit) {
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


  public ILifeInsurancePolicyDomainObject description(String description) {
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


  public ILifeInsurancePolicyDomainObject externalDestinationId(String externalDestinationId) {
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


  public ILifeInsurancePolicyDomainObject factFinderId(Integer factFinderId) {
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


  public ILifeInsurancePolicyDomainObject frequency(Integer frequency) {
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


  public ILifeInsurancePolicyDomainObject generalAccountMarketValue(Double generalAccountMarketValue) {
    this.generalAccountMarketValue = generalAccountMarketValue;
    return this;
  }

  /**
   * Get generalAccountMarketValue
   * @return generalAccountMarketValue
   */
  @javax.annotation.Nullable
  public Double getGeneralAccountMarketValue() {
    return generalAccountMarketValue;
  }

  public void setGeneralAccountMarketValue(Double generalAccountMarketValue) {
    this.generalAccountMarketValue = generalAccountMarketValue;
  }


  public ILifeInsurancePolicyDomainObject insured(InsuredEnum insured) {
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


  public ILifeInsurancePolicyDomainObject lifeInsurancePolicyId(Integer lifeInsurancePolicyId) {
    this.lifeInsurancePolicyId = lifeInsurancePolicyId;
    return this;
  }

  /**
   * Get lifeInsurancePolicyId
   * @return lifeInsurancePolicyId
   */
  @javax.annotation.Nullable
  public Integer getLifeInsurancePolicyId() {
    return lifeInsurancePolicyId;
  }

  public void setLifeInsurancePolicyId(Integer lifeInsurancePolicyId) {
    this.lifeInsurancePolicyId = lifeInsurancePolicyId;
  }


  public ILifeInsurancePolicyDomainObject payer(PayerEnum payer) {
    this.payer = payer;
    return this;
  }

  /**
   * Get payer
   * @return payer
   */
  @javax.annotation.Nullable
  public PayerEnum getPayer() {
    return payer;
  }

  public void setPayer(PayerEnum payer) {
    this.payer = payer;
  }


  public ILifeInsurancePolicyDomainObject policyType(Integer policyType) {
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


  public ILifeInsurancePolicyDomainObject premium(Double premium) {
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


  public ILifeInsurancePolicyDomainObject subaccounts(List<LifeInsurancePolicySubaccountDomainObject> subaccounts) {
    this.subaccounts = subaccounts;
    return this;
  }

  public ILifeInsurancePolicyDomainObject addSubaccountsItem(LifeInsurancePolicySubaccountDomainObject subaccountsItem) {
    if (this.subaccounts == null) {
      this.subaccounts = new ArrayList<>();
    }
    this.subaccounts.add(subaccountsItem);
    return this;
  }

  /**
   * Get subaccounts
   * @return subaccounts
   */
  @javax.annotation.Nullable
  public List<LifeInsurancePolicySubaccountDomainObject> getSubaccounts() {
    return subaccounts;
  }

  public void setSubaccounts(List<LifeInsurancePolicySubaccountDomainObject> subaccounts) {
    this.subaccounts = subaccounts;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ILifeInsurancePolicyDomainObject ilifeInsurancePolicyDomainObject = (ILifeInsurancePolicyDomainObject) o;
    return Objects.equals(this.beneficiary, ilifeInsurancePolicyDomainObject.beneficiary) &&
        Objects.equals(this.beneficiaryDependentId, ilifeInsurancePolicyDomainObject.beneficiaryDependentId) &&
        Objects.equals(this.benefit, ilifeInsurancePolicyDomainObject.benefit) &&
        Objects.equals(this.description, ilifeInsurancePolicyDomainObject.description) &&
        Objects.equals(this.externalDestinationId, ilifeInsurancePolicyDomainObject.externalDestinationId) &&
        Objects.equals(this.factFinderId, ilifeInsurancePolicyDomainObject.factFinderId) &&
        Objects.equals(this.frequency, ilifeInsurancePolicyDomainObject.frequency) &&
        Objects.equals(this.generalAccountMarketValue, ilifeInsurancePolicyDomainObject.generalAccountMarketValue) &&
        Objects.equals(this.insured, ilifeInsurancePolicyDomainObject.insured) &&
        Objects.equals(this.lifeInsurancePolicyId, ilifeInsurancePolicyDomainObject.lifeInsurancePolicyId) &&
        Objects.equals(this.payer, ilifeInsurancePolicyDomainObject.payer) &&
        Objects.equals(this.policyType, ilifeInsurancePolicyDomainObject.policyType) &&
        Objects.equals(this.premium, ilifeInsurancePolicyDomainObject.premium) &&
        Objects.equals(this.subaccounts, ilifeInsurancePolicyDomainObject.subaccounts);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beneficiary, beneficiaryDependentId, benefit, description, externalDestinationId, factFinderId, frequency, generalAccountMarketValue, insured, lifeInsurancePolicyId, payer, policyType, premium, subaccounts);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ILifeInsurancePolicyDomainObject {\n");
    sb.append("    beneficiary: ").append(toIndentedString(beneficiary)).append("\n");
    sb.append("    beneficiaryDependentId: ").append(toIndentedString(beneficiaryDependentId)).append("\n");
    sb.append("    benefit: ").append(toIndentedString(benefit)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    generalAccountMarketValue: ").append(toIndentedString(generalAccountMarketValue)).append("\n");
    sb.append("    insured: ").append(toIndentedString(insured)).append("\n");
    sb.append("    lifeInsurancePolicyId: ").append(toIndentedString(lifeInsurancePolicyId)).append("\n");
    sb.append("    payer: ").append(toIndentedString(payer)).append("\n");
    sb.append("    policyType: ").append(toIndentedString(policyType)).append("\n");
    sb.append("    premium: ").append(toIndentedString(premium)).append("\n");
    sb.append("    subaccounts: ").append(toIndentedString(subaccounts)).append("\n");
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
    openapiFields.add("beneficiary");
    openapiFields.add("beneficiaryDependentId");
    openapiFields.add("benefit");
    openapiFields.add("description");
    openapiFields.add("externalDestinationId");
    openapiFields.add("factFinderId");
    openapiFields.add("frequency");
    openapiFields.add("generalAccountMarketValue");
    openapiFields.add("insured");
    openapiFields.add("lifeInsurancePolicyId");
    openapiFields.add("payer");
    openapiFields.add("policyType");
    openapiFields.add("premium");
    openapiFields.add("subaccounts");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ILifeInsurancePolicyDomainObject
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ILifeInsurancePolicyDomainObject.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ILifeInsurancePolicyDomainObject is not found in the empty JSON string", ILifeInsurancePolicyDomainObject.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ILifeInsurancePolicyDomainObject.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ILifeInsurancePolicyDomainObject` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("beneficiary") != null && !jsonObj.get("beneficiary").isJsonNull()) && !jsonObj.get("beneficiary").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `beneficiary` to be a primitive type in the JSON string but got `%s`", jsonObj.get("beneficiary").toString()));
      }
      // validate the optional field `beneficiary`
      if (jsonObj.get("beneficiary") != null && !jsonObj.get("beneficiary").isJsonNull()) {
        BeneficiaryEnum.validateJsonElement(jsonObj.get("beneficiary"));
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
      if ((jsonObj.get("payer") != null && !jsonObj.get("payer").isJsonNull()) && !jsonObj.get("payer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payer").toString()));
      }
      // validate the optional field `payer`
      if (jsonObj.get("payer") != null && !jsonObj.get("payer").isJsonNull()) {
        PayerEnum.validateJsonElement(jsonObj.get("payer"));
      }
      if (jsonObj.get("subaccounts") != null && !jsonObj.get("subaccounts").isJsonNull()) {
        JsonArray jsonArraysubaccounts = jsonObj.getAsJsonArray("subaccounts");
        if (jsonArraysubaccounts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("subaccounts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `subaccounts` to be an array in the JSON string but got `%s`", jsonObj.get("subaccounts").toString()));
          }

          // validate the optional field `subaccounts` (array)
          for (int i = 0; i < jsonArraysubaccounts.size(); i++) {
            LifeInsurancePolicySubaccountDomainObject.validateJsonElement(jsonArraysubaccounts.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ILifeInsurancePolicyDomainObject.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ILifeInsurancePolicyDomainObject' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ILifeInsurancePolicyDomainObject> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ILifeInsurancePolicyDomainObject.class));

       return (TypeAdapter<T>) new TypeAdapter<ILifeInsurancePolicyDomainObject>() {
           @Override
           public void write(JsonWriter out, ILifeInsurancePolicyDomainObject value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ILifeInsurancePolicyDomainObject read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ILifeInsurancePolicyDomainObject given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ILifeInsurancePolicyDomainObject
   * @throws IOException if the JSON string is invalid with respect to ILifeInsurancePolicyDomainObject
   */
  public static ILifeInsurancePolicyDomainObject fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ILifeInsurancePolicyDomainObject.class);
  }

  /**
   * Convert an instance of ILifeInsurancePolicyDomainObject to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

