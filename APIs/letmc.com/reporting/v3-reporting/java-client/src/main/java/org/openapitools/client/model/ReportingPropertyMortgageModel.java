/*
 * LetMC Api V3, reporting
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-reporting
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
 * Represents an receivership case.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:11.827585-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ReportingPropertyMortgageModel {
  public static final String SERIALIZED_NAME_AMOUNT = "Amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private Double amount;

  public static final String SERIALIZED_NAME_BORROWERS_ACCOUNT_NAME = "BorrowersAccountName";
  @SerializedName(SERIALIZED_NAME_BORROWERS_ACCOUNT_NAME)
  private String borrowersAccountName;

  public static final String SERIALIZED_NAME_CREATED_AT = "CreatedAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_DISPLAY_TYPE = "DisplayType";
  @SerializedName(SERIALIZED_NAME_DISPLAY_TYPE)
  private String displayType;

  public static final String SERIALIZED_NAME_EXTRA_NOTES = "ExtraNotes";
  @SerializedName(SERIALIZED_NAME_EXTRA_NOTES)
  private String extraNotes;

  public static final String SERIALIZED_NAME_FROM = "From";
  @SerializedName(SERIALIZED_NAME_FROM)
  private OffsetDateTime from;

  public static final String SERIALIZED_NAME_INTREST_RATE = "IntrestRate";
  @SerializedName(SERIALIZED_NAME_INTREST_RATE)
  private Double intrestRate;

  public static final String SERIALIZED_NAME_MARKET_VALUE = "MarketValue";
  @SerializedName(SERIALIZED_NAME_MARKET_VALUE)
  private Double marketValue;

  public static final String SERIALIZED_NAME_MONTHLY_PAYMENT = "MonthlyPayment";
  @SerializedName(SERIALIZED_NAME_MONTHLY_PAYMENT)
  private Double monthlyPayment;

  public static final String SERIALIZED_NAME_MORTGAGE_ACCOUNT_NUMBER = "MortgageAccountNumber";
  @SerializedName(SERIALIZED_NAME_MORTGAGE_ACCOUNT_NUMBER)
  private String mortgageAccountNumber;

  public static final String SERIALIZED_NAME_MORTGAGE_PROVIDER = "MortgageProvider";
  @SerializedName(SERIALIZED_NAME_MORTGAGE_PROVIDER)
  private String mortgageProvider;

  public static final String SERIALIZED_NAME_PROPERTY_OWNABLE_I_D = "PropertyOwnableID";
  @SerializedName(SERIALIZED_NAME_PROPERTY_OWNABLE_I_D)
  private String propertyOwnableID;

  public static final String SERIALIZED_NAME_SALES_INSTRUCTION_I_D = "SalesInstructionID";
  @SerializedName(SERIALIZED_NAME_SALES_INSTRUCTION_I_D)
  private String salesInstructionID;

  /**
   * The mortgages type.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    INTEREST_ONLY_FIXED_RATE("InterestOnlyFixedRate"),
    
    INTEREST_ONLY_SVR("InterestOnlySVR"),
    
    INTEREST_ONLY_DISCOUNT_MORTGAGE("InterestOnlyDiscountMortgage"),
    
    INTEREST_ONLY_TRACKER("InterestOnlyTracker"),
    
    INTEREST_ONLY_CAPPED("InterestOnlyCapped"),
    
    INTEREST_ONLY_OFFSET("InterestOnlyOffset"),
    
    CAPITAL_REPAYMENT_FIXED_RATE("CapitalRepaymentFixedRate"),
    
    CAPITAL_REPAYMENT_SVR("CapitalRepaymentSVR"),
    
    CAPITAL_REPAYMENT_DISCOUNT_MORTGAGE("CapitalRepaymentDiscountMortgage"),
    
    CAPITAL_REPAYMENT_TRACKER("CapitalRepaymentTracker"),
    
    CAPITAL_REPAYMENT_CAPPED("CapitalRepaymentCapped"),
    
    CAPITAL_REPAYMENT_OFFSET("CapitalRepaymentOffset");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "Type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_VALUATION_DATE = "ValuationDate";
  @SerializedName(SERIALIZED_NAME_VALUATION_DATE)
  private OffsetDateTime valuationDate;

  public ReportingPropertyMortgageModel() {
  }

  public ReportingPropertyMortgageModel(
     String displayType
  ) {
    this();
    this.displayType = displayType;
  }

  public ReportingPropertyMortgageModel amount(Double amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Amount.
   * @return amount
   */
  @javax.annotation.Nullable
  public Double getAmount() {
    return amount;
  }

  public void setAmount(Double amount) {
    this.amount = amount;
  }


  public ReportingPropertyMortgageModel borrowersAccountName(String borrowersAccountName) {
    this.borrowersAccountName = borrowersAccountName;
    return this;
  }

  /**
   * Borrowers Account Name
   * @return borrowersAccountName
   */
  @javax.annotation.Nullable
  public String getBorrowersAccountName() {
    return borrowersAccountName;
  }

  public void setBorrowersAccountName(String borrowersAccountName) {
    this.borrowersAccountName = borrowersAccountName;
  }


  public ReportingPropertyMortgageModel createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * The created at date.
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  /**
   * Friendly type name.
   * @return displayType
   */
  @javax.annotation.Nullable
  public String getDisplayType() {
    return displayType;
  }



  public ReportingPropertyMortgageModel extraNotes(String extraNotes) {
    this.extraNotes = extraNotes;
    return this;
  }

  /**
   * Extra notes.
   * @return extraNotes
   */
  @javax.annotation.Nullable
  public String getExtraNotes() {
    return extraNotes;
  }

  public void setExtraNotes(String extraNotes) {
    this.extraNotes = extraNotes;
  }


  public ReportingPropertyMortgageModel from(OffsetDateTime from) {
    this.from = from;
    return this;
  }

  /**
   * The from date.
   * @return from
   */
  @javax.annotation.Nullable
  public OffsetDateTime getFrom() {
    return from;
  }

  public void setFrom(OffsetDateTime from) {
    this.from = from;
  }


  public ReportingPropertyMortgageModel intrestRate(Double intrestRate) {
    this.intrestRate = intrestRate;
    return this;
  }

  /**
   * The mortgages intrest rate.
   * @return intrestRate
   */
  @javax.annotation.Nullable
  public Double getIntrestRate() {
    return intrestRate;
  }

  public void setIntrestRate(Double intrestRate) {
    this.intrestRate = intrestRate;
  }


  public ReportingPropertyMortgageModel marketValue(Double marketValue) {
    this.marketValue = marketValue;
    return this;
  }

  /**
   * The property market value.
   * @return marketValue
   */
  @javax.annotation.Nullable
  public Double getMarketValue() {
    return marketValue;
  }

  public void setMarketValue(Double marketValue) {
    this.marketValue = marketValue;
  }


  public ReportingPropertyMortgageModel monthlyPayment(Double monthlyPayment) {
    this.monthlyPayment = monthlyPayment;
    return this;
  }

  /**
   * The mortgages monthly payment.
   * @return monthlyPayment
   */
  @javax.annotation.Nullable
  public Double getMonthlyPayment() {
    return monthlyPayment;
  }

  public void setMonthlyPayment(Double monthlyPayment) {
    this.monthlyPayment = monthlyPayment;
  }


  public ReportingPropertyMortgageModel mortgageAccountNumber(String mortgageAccountNumber) {
    this.mortgageAccountNumber = mortgageAccountNumber;
    return this;
  }

  /**
   * Mortgage account number.
   * @return mortgageAccountNumber
   */
  @javax.annotation.Nullable
  public String getMortgageAccountNumber() {
    return mortgageAccountNumber;
  }

  public void setMortgageAccountNumber(String mortgageAccountNumber) {
    this.mortgageAccountNumber = mortgageAccountNumber;
  }


  public ReportingPropertyMortgageModel mortgageProvider(String mortgageProvider) {
    this.mortgageProvider = mortgageProvider;
    return this;
  }

  /**
   * Mortgages provider.
   * @return mortgageProvider
   */
  @javax.annotation.Nullable
  public String getMortgageProvider() {
    return mortgageProvider;
  }

  public void setMortgageProvider(String mortgageProvider) {
    this.mortgageProvider = mortgageProvider;
  }


  public ReportingPropertyMortgageModel propertyOwnableID(String propertyOwnableID) {
    this.propertyOwnableID = propertyOwnableID;
    return this;
  }

  /**
   * The unique Property Ownable identifier.
   * @return propertyOwnableID
   */
  @javax.annotation.Nullable
  public String getPropertyOwnableID() {
    return propertyOwnableID;
  }

  public void setPropertyOwnableID(String propertyOwnableID) {
    this.propertyOwnableID = propertyOwnableID;
  }


  public ReportingPropertyMortgageModel salesInstructionID(String salesInstructionID) {
    this.salesInstructionID = salesInstructionID;
    return this;
  }

  /**
   * The unique Sales Instruction identifier.
   * @return salesInstructionID
   */
  @javax.annotation.Nullable
  public String getSalesInstructionID() {
    return salesInstructionID;
  }

  public void setSalesInstructionID(String salesInstructionID) {
    this.salesInstructionID = salesInstructionID;
  }


  public ReportingPropertyMortgageModel type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * The mortgages type.
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  public ReportingPropertyMortgageModel valuationDate(OffsetDateTime valuationDate) {
    this.valuationDate = valuationDate;
    return this;
  }

  /**
   * The mortgages valuation date.
   * @return valuationDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getValuationDate() {
    return valuationDate;
  }

  public void setValuationDate(OffsetDateTime valuationDate) {
    this.valuationDate = valuationDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ReportingPropertyMortgageModel reportingPropertyMortgageModel = (ReportingPropertyMortgageModel) o;
    return Objects.equals(this.amount, reportingPropertyMortgageModel.amount) &&
        Objects.equals(this.borrowersAccountName, reportingPropertyMortgageModel.borrowersAccountName) &&
        Objects.equals(this.createdAt, reportingPropertyMortgageModel.createdAt) &&
        Objects.equals(this.displayType, reportingPropertyMortgageModel.displayType) &&
        Objects.equals(this.extraNotes, reportingPropertyMortgageModel.extraNotes) &&
        Objects.equals(this.from, reportingPropertyMortgageModel.from) &&
        Objects.equals(this.intrestRate, reportingPropertyMortgageModel.intrestRate) &&
        Objects.equals(this.marketValue, reportingPropertyMortgageModel.marketValue) &&
        Objects.equals(this.monthlyPayment, reportingPropertyMortgageModel.monthlyPayment) &&
        Objects.equals(this.mortgageAccountNumber, reportingPropertyMortgageModel.mortgageAccountNumber) &&
        Objects.equals(this.mortgageProvider, reportingPropertyMortgageModel.mortgageProvider) &&
        Objects.equals(this.propertyOwnableID, reportingPropertyMortgageModel.propertyOwnableID) &&
        Objects.equals(this.salesInstructionID, reportingPropertyMortgageModel.salesInstructionID) &&
        Objects.equals(this.type, reportingPropertyMortgageModel.type) &&
        Objects.equals(this.valuationDate, reportingPropertyMortgageModel.valuationDate);
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, borrowersAccountName, createdAt, displayType, extraNotes, from, intrestRate, marketValue, monthlyPayment, mortgageAccountNumber, mortgageProvider, propertyOwnableID, salesInstructionID, type, valuationDate);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ReportingPropertyMortgageModel {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    borrowersAccountName: ").append(toIndentedString(borrowersAccountName)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    displayType: ").append(toIndentedString(displayType)).append("\n");
    sb.append("    extraNotes: ").append(toIndentedString(extraNotes)).append("\n");
    sb.append("    from: ").append(toIndentedString(from)).append("\n");
    sb.append("    intrestRate: ").append(toIndentedString(intrestRate)).append("\n");
    sb.append("    marketValue: ").append(toIndentedString(marketValue)).append("\n");
    sb.append("    monthlyPayment: ").append(toIndentedString(monthlyPayment)).append("\n");
    sb.append("    mortgageAccountNumber: ").append(toIndentedString(mortgageAccountNumber)).append("\n");
    sb.append("    mortgageProvider: ").append(toIndentedString(mortgageProvider)).append("\n");
    sb.append("    propertyOwnableID: ").append(toIndentedString(propertyOwnableID)).append("\n");
    sb.append("    salesInstructionID: ").append(toIndentedString(salesInstructionID)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    valuationDate: ").append(toIndentedString(valuationDate)).append("\n");
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
    openapiFields.add("Amount");
    openapiFields.add("BorrowersAccountName");
    openapiFields.add("CreatedAt");
    openapiFields.add("DisplayType");
    openapiFields.add("ExtraNotes");
    openapiFields.add("From");
    openapiFields.add("IntrestRate");
    openapiFields.add("MarketValue");
    openapiFields.add("MonthlyPayment");
    openapiFields.add("MortgageAccountNumber");
    openapiFields.add("MortgageProvider");
    openapiFields.add("PropertyOwnableID");
    openapiFields.add("SalesInstructionID");
    openapiFields.add("Type");
    openapiFields.add("ValuationDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ReportingPropertyMortgageModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ReportingPropertyMortgageModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ReportingPropertyMortgageModel is not found in the empty JSON string", ReportingPropertyMortgageModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ReportingPropertyMortgageModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ReportingPropertyMortgageModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("BorrowersAccountName") != null && !jsonObj.get("BorrowersAccountName").isJsonNull()) && !jsonObj.get("BorrowersAccountName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `BorrowersAccountName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("BorrowersAccountName").toString()));
      }
      if ((jsonObj.get("DisplayType") != null && !jsonObj.get("DisplayType").isJsonNull()) && !jsonObj.get("DisplayType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `DisplayType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("DisplayType").toString()));
      }
      if ((jsonObj.get("ExtraNotes") != null && !jsonObj.get("ExtraNotes").isJsonNull()) && !jsonObj.get("ExtraNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ExtraNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ExtraNotes").toString()));
      }
      if ((jsonObj.get("MortgageAccountNumber") != null && !jsonObj.get("MortgageAccountNumber").isJsonNull()) && !jsonObj.get("MortgageAccountNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MortgageAccountNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MortgageAccountNumber").toString()));
      }
      if ((jsonObj.get("MortgageProvider") != null && !jsonObj.get("MortgageProvider").isJsonNull()) && !jsonObj.get("MortgageProvider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `MortgageProvider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("MortgageProvider").toString()));
      }
      if ((jsonObj.get("PropertyOwnableID") != null && !jsonObj.get("PropertyOwnableID").isJsonNull()) && !jsonObj.get("PropertyOwnableID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PropertyOwnableID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PropertyOwnableID").toString()));
      }
      if ((jsonObj.get("SalesInstructionID") != null && !jsonObj.get("SalesInstructionID").isJsonNull()) && !jsonObj.get("SalesInstructionID").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SalesInstructionID` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SalesInstructionID").toString()));
      }
      if ((jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) && !jsonObj.get("Type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Type").toString()));
      }
      // validate the optional field `Type`
      if (jsonObj.get("Type") != null && !jsonObj.get("Type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("Type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ReportingPropertyMortgageModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ReportingPropertyMortgageModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ReportingPropertyMortgageModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ReportingPropertyMortgageModel.class));

       return (TypeAdapter<T>) new TypeAdapter<ReportingPropertyMortgageModel>() {
           @Override
           public void write(JsonWriter out, ReportingPropertyMortgageModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ReportingPropertyMortgageModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ReportingPropertyMortgageModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ReportingPropertyMortgageModel
   * @throws IOException if the JSON string is invalid with respect to ReportingPropertyMortgageModel
   */
  public static ReportingPropertyMortgageModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ReportingPropertyMortgageModel.class);
  }

  /**
   * Convert an instance of ReportingPropertyMortgageModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

