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
import org.openapitools.client.model.EFTBankDto;

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
 * SupplierQueryDto
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:05.666566-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SupplierQueryDto {
  public static final String SERIALIZED_NAME_ACCOUNT_NAME = "accountName";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NAME)
  private String accountName;

  public static final String SERIALIZED_NAME_ACCOUNT_NUMBER = "accountNumber";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NUMBER)
  private String accountNumber;

  public static final String SERIALIZED_NAME_ADDITIONAL_EMAILS = "additionalEmails";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_EMAILS)
  private List<String> additionalEmails = new ArrayList<>();

  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private List<String> address = new ArrayList<>();

  public static final String SERIALIZED_NAME_AUTH_CODE = "authCode";
  @SerializedName(SERIALIZED_NAME_AUTH_CODE)
  private String authCode;

  public static final String SERIALIZED_NAME_BANK = "bank";
  @SerializedName(SERIALIZED_NAME_BANK)
  private EFTBankDto bank;

  public static final String SERIALIZED_NAME_BUSINESS_IDENTIFIER_CODE = "businessIdentifierCode";
  @SerializedName(SERIALIZED_NAME_BUSINESS_IDENTIFIER_CODE)
  private String businessIdentifierCode;

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_CONTACT = "contact";
  @SerializedName(SERIALIZED_NAME_CONTACT)
  private String contact;

  public static final String SERIALIZED_NAME_E_F_T_REFERENCE = "eFTReference";
  @SerializedName(SERIALIZED_NAME_E_F_T_REFERENCE)
  private String eFTReference;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_FAX = "fax";
  @SerializedName(SERIALIZED_NAME_FAX)
  private String fax;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_INTERNATIONAL_BANK_ACCOUNT_NUMBER = "internationalBankAccountNumber";
  @SerializedName(SERIALIZED_NAME_INTERNATIONAL_BANK_ACCOUNT_NUMBER)
  private String internationalBankAccountNumber;

  public static final String SERIALIZED_NAME_MOBILE = "mobile";
  @SerializedName(SERIALIZED_NAME_MOBILE)
  private String mobile;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OUR_CODE = "ourCode";
  @SerializedName(SERIALIZED_NAME_OUR_CODE)
  private String ourCode;

  public static final String SERIALIZED_NAME_OWNER_TYPE_ID = "ownerTypeId";
  @SerializedName(SERIALIZED_NAME_OWNER_TYPE_ID)
  private Long ownerTypeId;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_POSTPONED_ACCOUNTING = "postponedAccounting";
  @SerializedName(SERIALIZED_NAME_POSTPONED_ACCOUNTING)
  private Boolean postponedAccounting;

  public static final String SERIALIZED_NAME_TIMESTAMP = "timestamp";
  @SerializedName(SERIALIZED_NAME_TIMESTAMP)
  private byte[] timestamp;

  public static final String SERIALIZED_NAME_VAT_ANALYSIS_TYPE_ID = "vatAnalysisTypeId";
  @SerializedName(SERIALIZED_NAME_VAT_ANALYSIS_TYPE_ID)
  private Long vatAnalysisTypeId;

  public static final String SERIALIZED_NAME_VAT_REG = "vatReg";
  @SerializedName(SERIALIZED_NAME_VAT_REG)
  private String vatReg;

  public static final String SERIALIZED_NAME_VAT_TYPE = "vatType";
  @SerializedName(SERIALIZED_NAME_VAT_TYPE)
  private Long vatType;

  public SupplierQueryDto() {
  }

  public SupplierQueryDto accountName(String accountName) {
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


  public SupplierQueryDto accountNumber(String accountNumber) {
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


  public SupplierQueryDto additionalEmails(List<String> additionalEmails) {
    this.additionalEmails = additionalEmails;
    return this;
  }

  public SupplierQueryDto addAdditionalEmailsItem(String additionalEmailsItem) {
    if (this.additionalEmails == null) {
      this.additionalEmails = new ArrayList<>();
    }
    this.additionalEmails.add(additionalEmailsItem);
    return this;
  }

  /**
   * Get additionalEmails
   * @return additionalEmails
   */
  @javax.annotation.Nullable
  public List<String> getAdditionalEmails() {
    return additionalEmails;
  }

  public void setAdditionalEmails(List<String> additionalEmails) {
    this.additionalEmails = additionalEmails;
  }


  public SupplierQueryDto address(List<String> address) {
    this.address = address;
    return this;
  }

  public SupplierQueryDto addAddressItem(String addressItem) {
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


  public SupplierQueryDto authCode(String authCode) {
    this.authCode = authCode;
    return this;
  }

  /**
   * Get authCode
   * @return authCode
   */
  @javax.annotation.Nullable
  public String getAuthCode() {
    return authCode;
  }

  public void setAuthCode(String authCode) {
    this.authCode = authCode;
  }


  public SupplierQueryDto bank(EFTBankDto bank) {
    this.bank = bank;
    return this;
  }

  /**
   * Get bank
   * @return bank
   */
  @javax.annotation.Nullable
  public EFTBankDto getBank() {
    return bank;
  }

  public void setBank(EFTBankDto bank) {
    this.bank = bank;
  }


  public SupplierQueryDto businessIdentifierCode(String businessIdentifierCode) {
    this.businessIdentifierCode = businessIdentifierCode;
    return this;
  }

  /**
   * Get businessIdentifierCode
   * @return businessIdentifierCode
   */
  @javax.annotation.Nullable
  public String getBusinessIdentifierCode() {
    return businessIdentifierCode;
  }

  public void setBusinessIdentifierCode(String businessIdentifierCode) {
    this.businessIdentifierCode = businessIdentifierCode;
  }


  public SupplierQueryDto code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Get code
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public SupplierQueryDto contact(String contact) {
    this.contact = contact;
    return this;
  }

  /**
   * Get contact
   * @return contact
   */
  @javax.annotation.Nullable
  public String getContact() {
    return contact;
  }

  public void setContact(String contact) {
    this.contact = contact;
  }


  public SupplierQueryDto eFTReference(String eFTReference) {
    this.eFTReference = eFTReference;
    return this;
  }

  /**
   * Get eFTReference
   * @return eFTReference
   */
  @javax.annotation.Nullable
  public String geteFTReference() {
    return eFTReference;
  }

  public void seteFTReference(String eFTReference) {
    this.eFTReference = eFTReference;
  }


  public SupplierQueryDto email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Get email
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public SupplierQueryDto fax(String fax) {
    this.fax = fax;
    return this;
  }

  /**
   * Get fax
   * @return fax
   */
  @javax.annotation.Nullable
  public String getFax() {
    return fax;
  }

  public void setFax(String fax) {
    this.fax = fax;
  }


  public SupplierQueryDto id(Long id) {
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


  public SupplierQueryDto internationalBankAccountNumber(String internationalBankAccountNumber) {
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


  public SupplierQueryDto mobile(String mobile) {
    this.mobile = mobile;
    return this;
  }

  /**
   * Get mobile
   * @return mobile
   */
  @javax.annotation.Nullable
  public String getMobile() {
    return mobile;
  }

  public void setMobile(String mobile) {
    this.mobile = mobile;
  }


  public SupplierQueryDto name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public SupplierQueryDto ourCode(String ourCode) {
    this.ourCode = ourCode;
    return this;
  }

  /**
   * Get ourCode
   * @return ourCode
   */
  @javax.annotation.Nullable
  public String getOurCode() {
    return ourCode;
  }

  public void setOurCode(String ourCode) {
    this.ourCode = ourCode;
  }


  public SupplierQueryDto ownerTypeId(Long ownerTypeId) {
    this.ownerTypeId = ownerTypeId;
    return this;
  }

  /**
   * Get ownerTypeId
   * @return ownerTypeId
   */
  @javax.annotation.Nullable
  public Long getOwnerTypeId() {
    return ownerTypeId;
  }

  public void setOwnerTypeId(Long ownerTypeId) {
    this.ownerTypeId = ownerTypeId;
  }


  public SupplierQueryDto phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Get phone
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public SupplierQueryDto postponedAccounting(Boolean postponedAccounting) {
    this.postponedAccounting = postponedAccounting;
    return this;
  }

  /**
   * Get postponedAccounting
   * @return postponedAccounting
   */
  @javax.annotation.Nullable
  public Boolean getPostponedAccounting() {
    return postponedAccounting;
  }

  public void setPostponedAccounting(Boolean postponedAccounting) {
    this.postponedAccounting = postponedAccounting;
  }


  public SupplierQueryDto timestamp(byte[] timestamp) {
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


  public SupplierQueryDto vatAnalysisTypeId(Long vatAnalysisTypeId) {
    this.vatAnalysisTypeId = vatAnalysisTypeId;
    return this;
  }

  /**
   * Get vatAnalysisTypeId
   * @return vatAnalysisTypeId
   */
  @javax.annotation.Nullable
  public Long getVatAnalysisTypeId() {
    return vatAnalysisTypeId;
  }

  public void setVatAnalysisTypeId(Long vatAnalysisTypeId) {
    this.vatAnalysisTypeId = vatAnalysisTypeId;
  }


  public SupplierQueryDto vatReg(String vatReg) {
    this.vatReg = vatReg;
    return this;
  }

  /**
   * Get vatReg
   * @return vatReg
   */
  @javax.annotation.Nullable
  public String getVatReg() {
    return vatReg;
  }

  public void setVatReg(String vatReg) {
    this.vatReg = vatReg;
  }


  public SupplierQueryDto vatType(Long vatType) {
    this.vatType = vatType;
    return this;
  }

  /**
   * Get vatType
   * @return vatType
   */
  @javax.annotation.Nullable
  public Long getVatType() {
    return vatType;
  }

  public void setVatType(Long vatType) {
    this.vatType = vatType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SupplierQueryDto supplierQueryDto = (SupplierQueryDto) o;
    return Objects.equals(this.accountName, supplierQueryDto.accountName) &&
        Objects.equals(this.accountNumber, supplierQueryDto.accountNumber) &&
        Objects.equals(this.additionalEmails, supplierQueryDto.additionalEmails) &&
        Objects.equals(this.address, supplierQueryDto.address) &&
        Objects.equals(this.authCode, supplierQueryDto.authCode) &&
        Objects.equals(this.bank, supplierQueryDto.bank) &&
        Objects.equals(this.businessIdentifierCode, supplierQueryDto.businessIdentifierCode) &&
        Objects.equals(this.code, supplierQueryDto.code) &&
        Objects.equals(this.contact, supplierQueryDto.contact) &&
        Objects.equals(this.eFTReference, supplierQueryDto.eFTReference) &&
        Objects.equals(this.email, supplierQueryDto.email) &&
        Objects.equals(this.fax, supplierQueryDto.fax) &&
        Objects.equals(this.id, supplierQueryDto.id) &&
        Objects.equals(this.internationalBankAccountNumber, supplierQueryDto.internationalBankAccountNumber) &&
        Objects.equals(this.mobile, supplierQueryDto.mobile) &&
        Objects.equals(this.name, supplierQueryDto.name) &&
        Objects.equals(this.ourCode, supplierQueryDto.ourCode) &&
        Objects.equals(this.ownerTypeId, supplierQueryDto.ownerTypeId) &&
        Objects.equals(this.phone, supplierQueryDto.phone) &&
        Objects.equals(this.postponedAccounting, supplierQueryDto.postponedAccounting) &&
        Arrays.equals(this.timestamp, supplierQueryDto.timestamp) &&
        Objects.equals(this.vatAnalysisTypeId, supplierQueryDto.vatAnalysisTypeId) &&
        Objects.equals(this.vatReg, supplierQueryDto.vatReg) &&
        Objects.equals(this.vatType, supplierQueryDto.vatType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountName, accountNumber, additionalEmails, address, authCode, bank, businessIdentifierCode, code, contact, eFTReference, email, fax, id, internationalBankAccountNumber, mobile, name, ourCode, ownerTypeId, phone, postponedAccounting, Arrays.hashCode(timestamp), vatAnalysisTypeId, vatReg, vatType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SupplierQueryDto {\n");
    sb.append("    accountName: ").append(toIndentedString(accountName)).append("\n");
    sb.append("    accountNumber: ").append(toIndentedString(accountNumber)).append("\n");
    sb.append("    additionalEmails: ").append(toIndentedString(additionalEmails)).append("\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    authCode: ").append(toIndentedString(authCode)).append("\n");
    sb.append("    bank: ").append(toIndentedString(bank)).append("\n");
    sb.append("    businessIdentifierCode: ").append(toIndentedString(businessIdentifierCode)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    contact: ").append(toIndentedString(contact)).append("\n");
    sb.append("    eFTReference: ").append(toIndentedString(eFTReference)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    fax: ").append(toIndentedString(fax)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    internationalBankAccountNumber: ").append(toIndentedString(internationalBankAccountNumber)).append("\n");
    sb.append("    mobile: ").append(toIndentedString(mobile)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    ourCode: ").append(toIndentedString(ourCode)).append("\n");
    sb.append("    ownerTypeId: ").append(toIndentedString(ownerTypeId)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    postponedAccounting: ").append(toIndentedString(postponedAccounting)).append("\n");
    sb.append("    timestamp: ").append(toIndentedString(timestamp)).append("\n");
    sb.append("    vatAnalysisTypeId: ").append(toIndentedString(vatAnalysisTypeId)).append("\n");
    sb.append("    vatReg: ").append(toIndentedString(vatReg)).append("\n");
    sb.append("    vatType: ").append(toIndentedString(vatType)).append("\n");
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
    openapiFields.add("accountName");
    openapiFields.add("accountNumber");
    openapiFields.add("additionalEmails");
    openapiFields.add("address");
    openapiFields.add("authCode");
    openapiFields.add("bank");
    openapiFields.add("businessIdentifierCode");
    openapiFields.add("code");
    openapiFields.add("contact");
    openapiFields.add("eFTReference");
    openapiFields.add("email");
    openapiFields.add("fax");
    openapiFields.add("id");
    openapiFields.add("internationalBankAccountNumber");
    openapiFields.add("mobile");
    openapiFields.add("name");
    openapiFields.add("ourCode");
    openapiFields.add("ownerTypeId");
    openapiFields.add("phone");
    openapiFields.add("postponedAccounting");
    openapiFields.add("timestamp");
    openapiFields.add("vatAnalysisTypeId");
    openapiFields.add("vatReg");
    openapiFields.add("vatType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SupplierQueryDto
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SupplierQueryDto.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SupplierQueryDto is not found in the empty JSON string", SupplierQueryDto.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SupplierQueryDto.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SupplierQueryDto` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("accountName") != null && !jsonObj.get("accountName").isJsonNull()) && !jsonObj.get("accountName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountName").toString()));
      }
      if ((jsonObj.get("accountNumber") != null && !jsonObj.get("accountNumber").isJsonNull()) && !jsonObj.get("accountNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountNumber").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("additionalEmails") != null && !jsonObj.get("additionalEmails").isJsonNull() && !jsonObj.get("additionalEmails").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `additionalEmails` to be an array in the JSON string but got `%s`", jsonObj.get("additionalEmails").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull() && !jsonObj.get("address").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be an array in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("authCode") != null && !jsonObj.get("authCode").isJsonNull()) && !jsonObj.get("authCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authCode").toString()));
      }
      // validate the optional field `bank`
      if (jsonObj.get("bank") != null && !jsonObj.get("bank").isJsonNull()) {
        EFTBankDto.validateJsonElement(jsonObj.get("bank"));
      }
      if ((jsonObj.get("businessIdentifierCode") != null && !jsonObj.get("businessIdentifierCode").isJsonNull()) && !jsonObj.get("businessIdentifierCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `businessIdentifierCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("businessIdentifierCode").toString()));
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("contact") != null && !jsonObj.get("contact").isJsonNull()) && !jsonObj.get("contact").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact").toString()));
      }
      if ((jsonObj.get("eFTReference") != null && !jsonObj.get("eFTReference").isJsonNull()) && !jsonObj.get("eFTReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eFTReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eFTReference").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("fax") != null && !jsonObj.get("fax").isJsonNull()) && !jsonObj.get("fax").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fax` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fax").toString()));
      }
      if ((jsonObj.get("internationalBankAccountNumber") != null && !jsonObj.get("internationalBankAccountNumber").isJsonNull()) && !jsonObj.get("internationalBankAccountNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `internationalBankAccountNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("internationalBankAccountNumber").toString()));
      }
      if ((jsonObj.get("mobile") != null && !jsonObj.get("mobile").isJsonNull()) && !jsonObj.get("mobile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mobile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mobile").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("ourCode") != null && !jsonObj.get("ourCode").isJsonNull()) && !jsonObj.get("ourCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ourCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ourCode").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      if ((jsonObj.get("vatReg") != null && !jsonObj.get("vatReg").isJsonNull()) && !jsonObj.get("vatReg").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vatReg` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vatReg").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SupplierQueryDto.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SupplierQueryDto' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SupplierQueryDto> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SupplierQueryDto.class));

       return (TypeAdapter<T>) new TypeAdapter<SupplierQueryDto>() {
           @Override
           public void write(JsonWriter out, SupplierQueryDto value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SupplierQueryDto read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SupplierQueryDto given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SupplierQueryDto
   * @throws IOException if the JSON string is invalid with respect to SupplierQueryDto
   */
  public static SupplierQueryDto fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SupplierQueryDto.class);
  }

  /**
   * Convert an instance of SupplierQueryDto to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

