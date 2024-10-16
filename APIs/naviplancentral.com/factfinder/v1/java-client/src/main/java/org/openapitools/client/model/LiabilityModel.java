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
import java.time.OffsetDateTime;
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
 * LiabilityModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:23.008234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LiabilityModel {
  public static final String SERIALIZED_NAME_BALANCE = "balance";
  @SerializedName(SERIALIZED_NAME_BALANCE)
  private Double balance;

  public static final String SERIALIZED_NAME_BALANCE_AS_OF_DATE = "balanceAsOfDate";
  @SerializedName(SERIALIZED_NAME_BALANCE_AS_OF_DATE)
  private OffsetDateTime balanceAsOfDate;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXTERNAL_DESTINATION_ID = "externalDestinationId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_DESTINATION_ID)
  private String externalDestinationId;

  public static final String SERIALIZED_NAME_EXTERNAL_SOURCE_ID = "externalSourceId";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_SOURCE_ID)
  private String externalSourceId;

  public static final String SERIALIZED_NAME_EXTERNAL_SOURCE_NAME = "externalSourceName";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_SOURCE_NAME)
  private String externalSourceName;

  public static final String SERIALIZED_NAME_FACT_FINDER_ID = "factFinderId";
  @SerializedName(SERIALIZED_NAME_FACT_FINDER_ID)
  private Integer factFinderId;

  public static final String SERIALIZED_NAME_FREQUENCY = "frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private Integer frequency;

  public static final String SERIALIZED_NAME_INTEREST_RATE = "interestRate";
  @SerializedName(SERIALIZED_NAME_INTEREST_RATE)
  private Double interestRate;

  public static final String SERIALIZED_NAME_LAST_UPDATED = "lastUpdated";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATED)
  private OffsetDateTime lastUpdated;

  public static final String SERIALIZED_NAME_LIABILITY_TYPE = "liabilityType";
  @SerializedName(SERIALIZED_NAME_LIABILITY_TYPE)
  private Integer liabilityType;

  public static final String SERIALIZED_NAME_LOAN_DATE = "loanDate";
  @SerializedName(SERIALIZED_NAME_LOAN_DATE)
  private OffsetDateTime loanDate;

  public static final String SERIALIZED_NAME_ORIGINAL_PRINCIPAL = "originalPrincipal";
  @SerializedName(SERIALIZED_NAME_ORIGINAL_PRINCIPAL)
  private Double originalPrincipal;

  /**
   * Gets or Sets owner
   */
  @JsonAdapter(OwnerEnum.Adapter.class)
  public enum OwnerEnum {
    CLIENT("Client"),
    
    CO_CLIENT("CoClient"),
    
    JOINT("Joint");

    private String value;

    OwnerEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static OwnerEnum fromValue(String value) {
      for (OwnerEnum b : OwnerEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<OwnerEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final OwnerEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public OwnerEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return OwnerEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      OwnerEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_OWNER = "owner";
  @SerializedName(SERIALIZED_NAME_OWNER)
  private OwnerEnum owner;

  public static final String SERIALIZED_NAME_PAYMENT = "payment";
  @SerializedName(SERIALIZED_NAME_PAYMENT)
  private Double payment;

  /**
   * Gets or Sets paymentType
   */
  @JsonAdapter(PaymentTypeEnum.Adapter.class)
  public enum PaymentTypeEnum {
    INTEREST_ONLY("InterestOnly"),
    
    PRINCIPAL_AND_INTEREST("PrincipalAndInterest"),
    
    SET_PRINCIPAL("SetPrincipal"),
    
    LAST_PERIOD("LastPeriod");

    private String value;

    PaymentTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PaymentTypeEnum fromValue(String value) {
      for (PaymentTypeEnum b : PaymentTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PaymentTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PaymentTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PaymentTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PaymentTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PaymentTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PAYMENT_TYPE = "paymentType";
  @SerializedName(SERIALIZED_NAME_PAYMENT_TYPE)
  private PaymentTypeEnum paymentType;

  public LiabilityModel() {
  }

  public LiabilityModel balance(Double balance) {
    this.balance = balance;
    return this;
  }

  /**
   * Get balance
   * @return balance
   */
  @javax.annotation.Nullable
  public Double getBalance() {
    return balance;
  }

  public void setBalance(Double balance) {
    this.balance = balance;
  }


  public LiabilityModel balanceAsOfDate(OffsetDateTime balanceAsOfDate) {
    this.balanceAsOfDate = balanceAsOfDate;
    return this;
  }

  /**
   * Get balanceAsOfDate
   * @return balanceAsOfDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getBalanceAsOfDate() {
    return balanceAsOfDate;
  }

  public void setBalanceAsOfDate(OffsetDateTime balanceAsOfDate) {
    this.balanceAsOfDate = balanceAsOfDate;
  }


  public LiabilityModel description(String description) {
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


  public LiabilityModel externalDestinationId(String externalDestinationId) {
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


  public LiabilityModel externalSourceId(String externalSourceId) {
    this.externalSourceId = externalSourceId;
    return this;
  }

  /**
   * Get externalSourceId
   * @return externalSourceId
   */
  @javax.annotation.Nullable
  public String getExternalSourceId() {
    return externalSourceId;
  }

  public void setExternalSourceId(String externalSourceId) {
    this.externalSourceId = externalSourceId;
  }


  public LiabilityModel externalSourceName(String externalSourceName) {
    this.externalSourceName = externalSourceName;
    return this;
  }

  /**
   * Get externalSourceName
   * @return externalSourceName
   */
  @javax.annotation.Nullable
  public String getExternalSourceName() {
    return externalSourceName;
  }

  public void setExternalSourceName(String externalSourceName) {
    this.externalSourceName = externalSourceName;
  }


  public LiabilityModel factFinderId(Integer factFinderId) {
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


  public LiabilityModel frequency(Integer frequency) {
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


  public LiabilityModel interestRate(Double interestRate) {
    this.interestRate = interestRate;
    return this;
  }

  /**
   * Get interestRate
   * minimum: 0
   * maximum: 5E+1
   * @return interestRate
   */
  @javax.annotation.Nullable
  public Double getInterestRate() {
    return interestRate;
  }

  public void setInterestRate(Double interestRate) {
    this.interestRate = interestRate;
  }


  public LiabilityModel lastUpdated(OffsetDateTime lastUpdated) {
    this.lastUpdated = lastUpdated;
    return this;
  }

  /**
   * Get lastUpdated
   * @return lastUpdated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLastUpdated() {
    return lastUpdated;
  }

  public void setLastUpdated(OffsetDateTime lastUpdated) {
    this.lastUpdated = lastUpdated;
  }


  public LiabilityModel liabilityType(Integer liabilityType) {
    this.liabilityType = liabilityType;
    return this;
  }

  /**
   * Get liabilityType
   * @return liabilityType
   */
  @javax.annotation.Nullable
  public Integer getLiabilityType() {
    return liabilityType;
  }

  public void setLiabilityType(Integer liabilityType) {
    this.liabilityType = liabilityType;
  }


  public LiabilityModel loanDate(OffsetDateTime loanDate) {
    this.loanDate = loanDate;
    return this;
  }

  /**
   * Get loanDate
   * @return loanDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getLoanDate() {
    return loanDate;
  }

  public void setLoanDate(OffsetDateTime loanDate) {
    this.loanDate = loanDate;
  }


  public LiabilityModel originalPrincipal(Double originalPrincipal) {
    this.originalPrincipal = originalPrincipal;
    return this;
  }

  /**
   * Get originalPrincipal
   * @return originalPrincipal
   */
  @javax.annotation.Nullable
  public Double getOriginalPrincipal() {
    return originalPrincipal;
  }

  public void setOriginalPrincipal(Double originalPrincipal) {
    this.originalPrincipal = originalPrincipal;
  }


  public LiabilityModel owner(OwnerEnum owner) {
    this.owner = owner;
    return this;
  }

  /**
   * Get owner
   * @return owner
   */
  @javax.annotation.Nullable
  public OwnerEnum getOwner() {
    return owner;
  }

  public void setOwner(OwnerEnum owner) {
    this.owner = owner;
  }


  public LiabilityModel payment(Double payment) {
    this.payment = payment;
    return this;
  }

  /**
   * Get payment
   * @return payment
   */
  @javax.annotation.Nullable
  public Double getPayment() {
    return payment;
  }

  public void setPayment(Double payment) {
    this.payment = payment;
  }


  public LiabilityModel paymentType(PaymentTypeEnum paymentType) {
    this.paymentType = paymentType;
    return this;
  }

  /**
   * Get paymentType
   * @return paymentType
   */
  @javax.annotation.Nullable
  public PaymentTypeEnum getPaymentType() {
    return paymentType;
  }

  public void setPaymentType(PaymentTypeEnum paymentType) {
    this.paymentType = paymentType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LiabilityModel liabilityModel = (LiabilityModel) o;
    return Objects.equals(this.balance, liabilityModel.balance) &&
        Objects.equals(this.balanceAsOfDate, liabilityModel.balanceAsOfDate) &&
        Objects.equals(this.description, liabilityModel.description) &&
        Objects.equals(this.externalDestinationId, liabilityModel.externalDestinationId) &&
        Objects.equals(this.externalSourceId, liabilityModel.externalSourceId) &&
        Objects.equals(this.externalSourceName, liabilityModel.externalSourceName) &&
        Objects.equals(this.factFinderId, liabilityModel.factFinderId) &&
        Objects.equals(this.frequency, liabilityModel.frequency) &&
        Objects.equals(this.interestRate, liabilityModel.interestRate) &&
        Objects.equals(this.lastUpdated, liabilityModel.lastUpdated) &&
        Objects.equals(this.liabilityType, liabilityModel.liabilityType) &&
        Objects.equals(this.loanDate, liabilityModel.loanDate) &&
        Objects.equals(this.originalPrincipal, liabilityModel.originalPrincipal) &&
        Objects.equals(this.owner, liabilityModel.owner) &&
        Objects.equals(this.payment, liabilityModel.payment) &&
        Objects.equals(this.paymentType, liabilityModel.paymentType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(balance, balanceAsOfDate, description, externalDestinationId, externalSourceId, externalSourceName, factFinderId, frequency, interestRate, lastUpdated, liabilityType, loanDate, originalPrincipal, owner, payment, paymentType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LiabilityModel {\n");
    sb.append("    balance: ").append(toIndentedString(balance)).append("\n");
    sb.append("    balanceAsOfDate: ").append(toIndentedString(balanceAsOfDate)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    externalDestinationId: ").append(toIndentedString(externalDestinationId)).append("\n");
    sb.append("    externalSourceId: ").append(toIndentedString(externalSourceId)).append("\n");
    sb.append("    externalSourceName: ").append(toIndentedString(externalSourceName)).append("\n");
    sb.append("    factFinderId: ").append(toIndentedString(factFinderId)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    interestRate: ").append(toIndentedString(interestRate)).append("\n");
    sb.append("    lastUpdated: ").append(toIndentedString(lastUpdated)).append("\n");
    sb.append("    liabilityType: ").append(toIndentedString(liabilityType)).append("\n");
    sb.append("    loanDate: ").append(toIndentedString(loanDate)).append("\n");
    sb.append("    originalPrincipal: ").append(toIndentedString(originalPrincipal)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    payment: ").append(toIndentedString(payment)).append("\n");
    sb.append("    paymentType: ").append(toIndentedString(paymentType)).append("\n");
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
    openapiFields.add("balance");
    openapiFields.add("balanceAsOfDate");
    openapiFields.add("description");
    openapiFields.add("externalDestinationId");
    openapiFields.add("externalSourceId");
    openapiFields.add("externalSourceName");
    openapiFields.add("factFinderId");
    openapiFields.add("frequency");
    openapiFields.add("interestRate");
    openapiFields.add("lastUpdated");
    openapiFields.add("liabilityType");
    openapiFields.add("loanDate");
    openapiFields.add("originalPrincipal");
    openapiFields.add("owner");
    openapiFields.add("payment");
    openapiFields.add("paymentType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("factFinderId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LiabilityModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LiabilityModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LiabilityModel is not found in the empty JSON string", LiabilityModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LiabilityModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LiabilityModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : LiabilityModel.openapiRequiredFields) {
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
      if ((jsonObj.get("externalSourceId") != null && !jsonObj.get("externalSourceId").isJsonNull()) && !jsonObj.get("externalSourceId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalSourceId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalSourceId").toString()));
      }
      if ((jsonObj.get("externalSourceName") != null && !jsonObj.get("externalSourceName").isJsonNull()) && !jsonObj.get("externalSourceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `externalSourceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("externalSourceName").toString()));
      }
      if ((jsonObj.get("owner") != null && !jsonObj.get("owner").isJsonNull()) && !jsonObj.get("owner").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner").toString()));
      }
      // validate the optional field `owner`
      if (jsonObj.get("owner") != null && !jsonObj.get("owner").isJsonNull()) {
        OwnerEnum.validateJsonElement(jsonObj.get("owner"));
      }
      if ((jsonObj.get("paymentType") != null && !jsonObj.get("paymentType").isJsonNull()) && !jsonObj.get("paymentType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentType").toString()));
      }
      // validate the optional field `paymentType`
      if (jsonObj.get("paymentType") != null && !jsonObj.get("paymentType").isJsonNull()) {
        PaymentTypeEnum.validateJsonElement(jsonObj.get("paymentType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LiabilityModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LiabilityModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LiabilityModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LiabilityModel.class));

       return (TypeAdapter<T>) new TypeAdapter<LiabilityModel>() {
           @Override
           public void write(JsonWriter out, LiabilityModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LiabilityModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LiabilityModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LiabilityModel
   * @throws IOException if the JSON string is invalid with respect to LiabilityModel
   */
  public static LiabilityModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LiabilityModel.class);
  }

  /**
   * Convert an instance of LiabilityModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

