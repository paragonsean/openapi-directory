/*
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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
 * BankAccountQueryDto
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:05.666566-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BankAccountQueryDto {
  public static final String SERIALIZED_NAME_AC_CODE = "acCode";
  @SerializedName(SERIALIZED_NAME_AC_CODE)
  private String acCode;

  public static final String SERIALIZED_NAME_ACCOUNT_NAME = "accountName";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NAME)
  private String accountName;

  public static final String SERIALIZED_NAME_ACCOUNT_NUMBER = "accountNumber";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NUMBER)
  private String accountNumber;

  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private List<String> address = new ArrayList<>();

  public static final String SERIALIZED_NAME_BANK_FEED_SOURCE = "bankFeedSource";
  @SerializedName(SERIALIZED_NAME_BANK_FEED_SOURCE)
  private Integer bankFeedSource;

  public static final String SERIALIZED_NAME_BUSINESS_IDENTIFIER_CODES = "businessIdentifierCodes";
  @SerializedName(SERIALIZED_NAME_BUSINESS_IDENTIFIER_CODES)
  private String businessIdentifierCodes;

  public static final String SERIALIZED_NAME_CATEGORY_ID = "categoryId";
  @SerializedName(SERIALIZED_NAME_CATEGORY_ID)
  private Long categoryId;

  public static final String SERIALIZED_NAME_CREDITOR_SCHEME = "creditorScheme";
  @SerializedName(SERIALIZED_NAME_CREDITOR_SCHEME)
  private String creditorScheme;

  public static final String SERIALIZED_NAME_DETAILS = "details";
  @SerializedName(SERIALIZED_NAME_DETAILS)
  private String details;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_INTERNATIONAL_BANK_ACCOUNT_NUMBER = "internationalBankAccountNumber";
  @SerializedName(SERIALIZED_NAME_INTERNATIONAL_BANK_ACCOUNT_NUMBER)
  private String internationalBankAccountNumber;

  public static final String SERIALIZED_NAME_IS_DEFAULT_BANK = "isDefaultBank";
  @SerializedName(SERIALIZED_NAME_IS_DEFAULT_BANK)
  private Boolean isDefaultBank;

  public static final String SERIALIZED_NAME_LAST_CHQ = "lastChq";
  @SerializedName(SERIALIZED_NAME_LAST_CHQ)
  private String lastChq;

  public static final String SERIALIZED_NAME_NOMINAL_AC_CODE = "nominalAcCode";
  @SerializedName(SERIALIZED_NAME_NOMINAL_AC_CODE)
  private String nominalAcCode;

  public static final String SERIALIZED_NAME_SORT_CODE = "sortCode";
  @SerializedName(SERIALIZED_NAME_SORT_CODE)
  private String sortCode;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private byte[] timestamp;

  public BankAccountQueryDto() {
  }

  public BankAccountQueryDto acCode(String acCode) {
    this.acCode = acCode;
    return this;
  }

  /**
   * Get acCode
   * @return acCode
   */
  @javax.annotation.Nullable
  public String getAcCode() {
    return acCode;
  }

  public void setAcCode(String acCode) {
    this.acCode = acCode;
  }


  public BankAccountQueryDto accountName(String accountName) {
    this.accountName = accountName;
    return this;
  }

  /**
   * Get accountName
   * @return accountName
   */
  @javax.annotation.Nullable
  public String getAccountName() {
    return accountName;
  }

  public void setAccountName(String accountName) {
    this.accountName = accountName;
  }


  public BankAccountQueryDto accountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
    return this;
  }

  /**
   * Get accountNumber
   * @return accountNumber
   */
  @javax.annotation.Nullable
  public String getAccountNumber() {
    return accountNumber;
  }

  public void setAccountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
  }


  public BankAccountQueryDto address(List<String> address) {
    this.address = address;
    return this;
  }

  public BankAccountQueryDto addAddressItem(String addressItem) {
    if (this.address == null) {
      this.address = new ArrayList<>();
    }
    this.address.add(addressItem);
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public List<String> getAddress() {
    return address;
  }

  public void setAddress(List<String> address) {
    this.address = address;
  }


  public BankAccountQueryDto bankFeedSource(Integer bankFeedSource) {
    this.bankFeedSource = bankFeedSource;
    return this;
  }

  /**
   * Get bankFeedSource
   * @return bankFeedSource
   */
  @javax.annotation.Nullable
  public Integer getBankFeedSource() {
    return bankFeedSource;
  }

  public void setBankFeedSource(Integer bankFeedSource) {
    this.bankFeedSource = bankFeedSource;
  }


  public BankAccountQueryDto businessIdentifierCodes(String businessIdentifierCodes) {
    this.businessIdentifierCodes = businessIdentifierCodes;
    return this;
  }

  /**
   * Get businessIdentifierCodes
   * @return businessIdentifierCodes
   */
  @javax.annotation.Nullable
  public String getBusinessIdentifierCodes() {
    return businessIdentifierCodes;
  }

  public void setBusinessIdentifierCodes(String businessIdentifierCodes) {
    this.businessIdentifierCodes = businessIdentifierCodes;
  }


  public BankAccountQueryDto categoryId(Long categoryId) {
    this.categoryId = categoryId;
    return this;
  }

  /**
   * Get categoryId
   * @return categoryId
   */
  @javax.annotation.Nullable
  public Long getCategoryId() {
    return categoryId;
  }

  public void setCategoryId(Long categoryId) {
    this.categoryId = categoryId;
  }


  public BankAccountQueryDto creditorScheme(String creditorScheme) {
    this.creditorScheme = creditorScheme;
    return this;
  }

  /**
   * Get creditorScheme
   * @return creditorScheme
   */
  @javax.annotation.Nullable
  public String getCreditorScheme() {
    return creditorScheme;
  }

  public void setCreditorScheme(String creditorScheme) {
    this.creditorScheme = creditorScheme;
  }


  public BankAccountQueryDto details(String details) {
    this.details = details;
    return this;
  }

  /**
   * Get details
   * @return details
   */
  @javax.annotation.Nullable
  public String getDetails() {
    return details;
  }

  public void setDetails(String details) {
    this.details = details;
  }


  public BankAccountQueryDto id(Long id) {
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


  public BankAccountQueryDto internationalBankAccountNumber(String internationalBankAccountNumber) {
    this.internationalBankAccountNumber = internationalBankAccountNumber;
    return this;
  }

  /**
   * Get internationalBankAccountNumber
   * @return internationalBankAccountNumber
   */
  @javax.annotation.Nullable
  public String getInternationalBankAccountNumber() {
    return internationalBankAccountNumber;
  }

  public void setInternationalBankAccountNumber(String internationalBankAccountNumber) {
    this.internationalBankAccountNumber = internationalBankAccountNumber;
  }


  public BankAccountQueryDto isDefaultBank(Boolean isDefaultBank) {
    this.isDefaultBank = isDefaultBank;
    return this;
  }

  /**
   * Get isDefaultBank
   * @return isDefaultBank
   */
  @javax.annotation.Nullable
  public Boolean getIsDefaultBank() {
    return isDefaultBank;
  }

  public void setIsDefaultBank(Boolean isDefaultBank) {
    this.isDefaultBank = isDefaultBank;
  }


  public BankAccountQueryDto lastChq(String lastChq) {
    this.lastChq = lastChq;
    return this;
  }

  /**
   * Get lastChq
   * @return lastChq
   */
  @javax.annotation.Nullable
  public String getLastChq() {
    return lastChq;
  }

  public void setLastChq(String lastChq) {
    this.lastChq = lastChq;
  }


  public BankAccountQueryDto nominalAcCode(String nominalAcCode) {
    this.nominalAcCode = nominalAcCode;
    return this;
  }

  /**
   * Get nominalAcCode
   * @return nominalAcCode
   */
  @javax.annotation.Nullable
  public String getNominalAcCode() {
    return nominalAcCode;
  }

  public void setNominalAcCode(String nominalAcCode) {
    this.nominalAcCode = nominalAcCode;
  }


  public BankAccountQueryDto sortCode(String sortCode) {
    this.sortCode = sortCode;
    return this;
  }

  /**
   * Get sortCode
   * @return sortCode
   */
  @javax.annotation.Nullable
  public String getSortCode() {
    return sortCode;
  }

  public void setSortCode(String sortCode) {
    this.sortCode = sortCode;
  }


  public BankAccountQueryDto timestamp(byte[] timestamp) {
    this.timestamp = timestamp;
    return this;
  }

  /**
   * Get timestamp
   * @return timestamp
   */
  @javax.annotation.Nullable
  public byte[] getTimestamp() {
    return timestamp;
  }

  public void setTimestamp(byte[] timestamp) {
    this.timestamp = timestamp;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BankAccountQueryDto bankAccountQueryDto = (BankAccountQueryDto) o;
    return Objects.equals(this.acCode, bankAccountQueryDto.acCode) &&
        Objects.equals(this.accountName, bankAccountQueryDto.accountName) &&
        Objects.equals(this.accountNumber, bankAccountQueryDto.accountNumber) &&
        Objects.equals(this.address, bankAccountQueryDto.address) &&
        Objects.equals(this.bankFeedSource, bankAccountQueryDto.bankFeedSource) &&
        Objects.equals(this.businessIdentifierCodes, bankAccountQueryDto.businessIdentifierCodes) &&
        Objects.equals(this.categoryId, bankAccountQueryDto.categoryId) &&
        Objects.equals(this.creditorScheme, bankAccountQueryDto.creditorScheme) &&
        Objects.equals(this.details, bankAccountQueryDto.details) &&
        Objects.equals(this.id, bankAccountQueryDto.id) &&
        Objects.equals(this.internationalBankAccountNumber, bankAccountQueryDto.internationalBankAccountNumber) &&
        Objects.equals(this.isDefaultBank, bankAccountQueryDto.isDefaultBank) &&
        Objects.equals(this.lastChq, bankAccountQueryDto.lastChq) &&
        Objects.equals(this.nominalAcCode, bankAccountQueryDto.nominalAcCode) &&
        Objects.equals(this.sortCode, bankAccountQueryDto.sortCode) &&
        Arrays.equals(this.timestamp, bankAccountQueryDto.timestamp);
  }

  @Override
  public int hashCode() {
    return Objects.hash(acCode, accountName, accountNumber, address, bankFeedSource, businessIdentifierCodes, categoryId, creditorScheme, details, id, internationalBankAccountNumber, isDefaultBank, lastChq, nominalAcCode, sortCode, Arrays.hashCode(timestamp));
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BankAccountQueryDto {\n");
    sb.append("    acCode: ").append(toIndentedString(acCode)).append("\n");
    sb.append("    accountName: ").append(toIndentedString(accountName)).append("\n");
    sb.append("    accountNumber: ").append(toIndentedString(accountNumber)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    bankFeedSource: ").append(toIndentedString(bankFeedSource)).append("\n");
    sb.append("    businessIdentifierCodes: ").append(toIndentedString(businessIdentifierCodes)).append("\n");
    sb.append("    categoryId: ").append(toIndentedString(categoryId)).append("\n");
    sb.append("    creditorScheme: ").append(toIndentedString(creditorScheme)).append("\n");
    sb.append("    details: ").append(toIndentedString(details)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    internationalBankAccountNumber: ").append(toIndentedString(internationalBankAccountNumber)).append("\n");
    sb.append("    isDefaultBank: ").append(toIndentedString(isDefaultBank)).append("\n");
    sb.append("    lastChq: ").append(toIndentedString(lastChq)).append("\n");
    sb.append("    nominalAcCode: ").append(toIndentedString(nominalAcCode)).append("\n");
    sb.append("    sortCode: ").append(toIndentedString(sortCode)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
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
    openapiFields.add("acCode");
    openapiFields.add("accountName");
    openapiFields.add("accountNumber");
    openapiFields.add("address");
    openapiFields.add("bankFeedSource");
    openapiFields.add("businessIdentifierCodes");
    openapiFields.add("categoryId");
    openapiFields.add("creditorScheme");
    openapiFields.add("details");
    openapiFields.add("id");
    openapiFields.add("internationalBankAccountNumber");
    openapiFields.add("isDefaultBank");
    openapiFields.add("lastChq");
    openapiFields.add("nominalAcCode");
    openapiFields.add("sortCode");
    openapiFields.add("timestamp");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BankAccountQueryDto
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BankAccountQueryDto.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BankAccountQueryDto is not found in the empty JSON string", BankAccountQueryDto.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BankAccountQueryDto.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BankAccountQueryDto` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("acCode") != null && !jsonObj.get("acCode").isJsonNull()) && !jsonObj.get("acCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `acCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("acCode").toString()));
      }
      if ((jsonObj.get("accountName") != null && !jsonObj.get("accountName").isJsonNull()) && !jsonObj.get("accountName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountName").toString()));
      }
      if ((jsonObj.get("accountNumber") != null && !jsonObj.get("accountNumber").isJsonNull()) && !jsonObj.get("accountNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountNumber").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull() && !jsonObj.get("address").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be an array in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("businessIdentifierCodes") != null && !jsonObj.get("businessIdentifierCodes").isJsonNull()) && !jsonObj.get("businessIdentifierCodes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `businessIdentifierCodes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("businessIdentifierCodes").toString()));
      }
      if ((jsonObj.get("creditorScheme") != null && !jsonObj.get("creditorScheme").isJsonNull()) && !jsonObj.get("creditorScheme").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creditorScheme` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creditorScheme").toString()));
      }
      if ((jsonObj.get("details") != null && !jsonObj.get("details").isJsonNull()) && !jsonObj.get("details").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `details` to be a primitive type in the JSON string but got `%s`", jsonObj.get("details").toString()));
      }
      if ((jsonObj.get("internationalBankAccountNumber") != null && !jsonObj.get("internationalBankAccountNumber").isJsonNull()) && !jsonObj.get("internationalBankAccountNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `internationalBankAccountNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("internationalBankAccountNumber").toString()));
      }
      if ((jsonObj.get("lastChq") != null && !jsonObj.get("lastChq").isJsonNull()) && !jsonObj.get("lastChq").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastChq` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastChq").toString()));
      }
      if ((jsonObj.get("nominalAcCode") != null && !jsonObj.get("nominalAcCode").isJsonNull()) && !jsonObj.get("nominalAcCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nominalAcCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nominalAcCode").toString()));
      }
      if ((jsonObj.get("sortCode") != null && !jsonObj.get("sortCode").isJsonNull()) && !jsonObj.get("sortCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sortCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sortCode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BankAccountQueryDto.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BankAccountQueryDto' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BankAccountQueryDto> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BankAccountQueryDto.class));

       return (TypeAdapter<T>) new TypeAdapter<BankAccountQueryDto>() {
           @Override
           public void write(JsonWriter out, BankAccountQueryDto value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BankAccountQueryDto read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BankAccountQueryDto given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BankAccountQueryDto
   * @throws IOException if the JSON string is invalid with respect to BankAccountQueryDto
   */
  public static BankAccountQueryDto fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BankAccountQueryDto.class);
  }

  /**
   * Convert an instance of BankAccountQueryDto to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

