/*
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
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
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AccountReference16CH;
import org.openapitools.client.model.Address;
import org.openapitools.client.model.Amount;
import org.openapitools.client.model.CreditorAgent7CH;
import org.openapitools.client.model.PurposeCode;
import org.openapitools.client.model.RemittanceInformationStructured;
import org.openapitools.client.model.TransactionStatus;

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
 * Generic JSON response body consistion of the corresponding payment initation JSON body together with an optional transaction status field. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:56.314640-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PaymentInitiationWithStatusResponse {
  public static final String SERIALIZED_NAME_CREDITOR_ACCOUNT = "creditorAccount";
  @SerializedName(SERIALIZED_NAME_CREDITOR_ACCOUNT)
  private AccountReference16CH creditorAccount;

  public static final String SERIALIZED_NAME_CREDITOR_ADDRESS = "creditorAddress";
  @SerializedName(SERIALIZED_NAME_CREDITOR_ADDRESS)
  private Address creditorAddress;

  public static final String SERIALIZED_NAME_CREDITOR_AGENT = "creditorAgent";
  @SerializedName(SERIALIZED_NAME_CREDITOR_AGENT)
  private CreditorAgent7CH creditorAgent;

  public static final String SERIALIZED_NAME_CREDITOR_NAME = "creditorName";
  @SerializedName(SERIALIZED_NAME_CREDITOR_NAME)
  private String creditorName;

  public static final String SERIALIZED_NAME_DEBTOR_ACCOUNT = "debtorAccount";
  @SerializedName(SERIALIZED_NAME_DEBTOR_ACCOUNT)
  private AccountReference16CH debtorAccount;

  public static final String SERIALIZED_NAME_END_TO_END_IDENTIFICATION = "endToEndIdentification";
  @SerializedName(SERIALIZED_NAME_END_TO_END_IDENTIFICATION)
  private String endToEndIdentification;

  public static final String SERIALIZED_NAME_INSTRUCTED_AMOUNT = "instructedAmount";
  @SerializedName(SERIALIZED_NAME_INSTRUCTED_AMOUNT)
  private Amount instructedAmount;

  public static final String SERIALIZED_NAME_PURPOSE_CODE = "purposeCode";
  @SerializedName(SERIALIZED_NAME_PURPOSE_CODE)
  private PurposeCode purposeCode;

  public static final String SERIALIZED_NAME_REMITTANCE_INFORMATION_STRUCTURED = "remittanceInformationStructured";
  @SerializedName(SERIALIZED_NAME_REMITTANCE_INFORMATION_STRUCTURED)
  private RemittanceInformationStructured remittanceInformationStructured;

  public static final String SERIALIZED_NAME_REMITTANCE_INFORMATION_UNSTRUCTURED = "remittanceInformationUnstructured";
  @SerializedName(SERIALIZED_NAME_REMITTANCE_INFORMATION_UNSTRUCTURED)
  private String remittanceInformationUnstructured;

  public static final String SERIALIZED_NAME_REMITTANCE_INFORMATION_UNSTRUCTURED_ARRAY = "remittanceInformationUnstructuredArray";
  @SerializedName(SERIALIZED_NAME_REMITTANCE_INFORMATION_UNSTRUCTURED_ARRAY)
  private List<String> remittanceInformationUnstructuredArray = new ArrayList<>();

  public static final String SERIALIZED_NAME_REQUESTED_EXECUTION_DATE = "requestedExecutionDate";
  @SerializedName(SERIALIZED_NAME_REQUESTED_EXECUTION_DATE)
  private LocalDate requestedExecutionDate;

  public static final String SERIALIZED_NAME_REQUESTED_EXECUTION_TIME = "requestedExecutionTime";
  @SerializedName(SERIALIZED_NAME_REQUESTED_EXECUTION_TIME)
  private OffsetDateTime requestedExecutionTime;

  public static final String SERIALIZED_NAME_TRANSACTION_STATUS = "transactionStatus";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_STATUS)
  private TransactionStatus transactionStatus;

  public static final String SERIALIZED_NAME_ULTIMATE_CREDITOR = "ultimateCreditor";
  @SerializedName(SERIALIZED_NAME_ULTIMATE_CREDITOR)
  private String ultimateCreditor;

  public static final String SERIALIZED_NAME_ULTIMATE_DEBTOR = "ultimateDebtor";
  @SerializedName(SERIALIZED_NAME_ULTIMATE_DEBTOR)
  private String ultimateDebtor;

  public PaymentInitiationWithStatusResponse() {
  }

  public PaymentInitiationWithStatusResponse creditorAccount(AccountReference16CH creditorAccount) {
    this.creditorAccount = creditorAccount;
    return this;
  }

  /**
   * Get creditorAccount
   * @return creditorAccount
   */
  @javax.annotation.Nonnull
  public AccountReference16CH getCreditorAccount() {
    return creditorAccount;
  }

  public void setCreditorAccount(AccountReference16CH creditorAccount) {
    this.creditorAccount = creditorAccount;
  }


  public PaymentInitiationWithStatusResponse creditorAddress(Address creditorAddress) {
    this.creditorAddress = creditorAddress;
    return this;
  }

  /**
   * Get creditorAddress
   * @return creditorAddress
   */
  @javax.annotation.Nullable
  public Address getCreditorAddress() {
    return creditorAddress;
  }

  public void setCreditorAddress(Address creditorAddress) {
    this.creditorAddress = creditorAddress;
  }


  public PaymentInitiationWithStatusResponse creditorAgent(CreditorAgent7CH creditorAgent) {
    this.creditorAgent = creditorAgent;
    return this;
  }

  /**
   * Get creditorAgent
   * @return creditorAgent
   */
  @javax.annotation.Nullable
  public CreditorAgent7CH getCreditorAgent() {
    return creditorAgent;
  }

  public void setCreditorAgent(CreditorAgent7CH creditorAgent) {
    this.creditorAgent = creditorAgent;
  }


  public PaymentInitiationWithStatusResponse creditorName(String creditorName) {
    this.creditorName = creditorName;
    return this;
  }

  /**
   * Creditor name.
   * @return creditorName
   */
  @javax.annotation.Nonnull
  public String getCreditorName() {
    return creditorName;
  }

  public void setCreditorName(String creditorName) {
    this.creditorName = creditorName;
  }


  public PaymentInitiationWithStatusResponse debtorAccount(AccountReference16CH debtorAccount) {
    this.debtorAccount = debtorAccount;
    return this;
  }

  /**
   * Get debtorAccount
   * @return debtorAccount
   */
  @javax.annotation.Nonnull
  public AccountReference16CH getDebtorAccount() {
    return debtorAccount;
  }

  public void setDebtorAccount(AccountReference16CH debtorAccount) {
    this.debtorAccount = debtorAccount;
  }


  public PaymentInitiationWithStatusResponse endToEndIdentification(String endToEndIdentification) {
    this.endToEndIdentification = endToEndIdentification;
    return this;
  }

  /**
   * Get endToEndIdentification
   * @return endToEndIdentification
   */
  @javax.annotation.Nullable
  public String getEndToEndIdentification() {
    return endToEndIdentification;
  }

  public void setEndToEndIdentification(String endToEndIdentification) {
    this.endToEndIdentification = endToEndIdentification;
  }


  public PaymentInitiationWithStatusResponse instructedAmount(Amount instructedAmount) {
    this.instructedAmount = instructedAmount;
    return this;
  }

  /**
   * Get instructedAmount
   * @return instructedAmount
   */
  @javax.annotation.Nonnull
  public Amount getInstructedAmount() {
    return instructedAmount;
  }

  public void setInstructedAmount(Amount instructedAmount) {
    this.instructedAmount = instructedAmount;
  }


  public PaymentInitiationWithStatusResponse purposeCode(PurposeCode purposeCode) {
    this.purposeCode = purposeCode;
    return this;
  }

  /**
   * Get purposeCode
   * @return purposeCode
   */
  @javax.annotation.Nullable
  public PurposeCode getPurposeCode() {
    return purposeCode;
  }

  public void setPurposeCode(PurposeCode purposeCode) {
    this.purposeCode = purposeCode;
  }


  public PaymentInitiationWithStatusResponse remittanceInformationStructured(RemittanceInformationStructured remittanceInformationStructured) {
    this.remittanceInformationStructured = remittanceInformationStructured;
    return this;
  }

  /**
   * Get remittanceInformationStructured
   * @return remittanceInformationStructured
   */
  @javax.annotation.Nullable
  public RemittanceInformationStructured getRemittanceInformationStructured() {
    return remittanceInformationStructured;
  }

  public void setRemittanceInformationStructured(RemittanceInformationStructured remittanceInformationStructured) {
    this.remittanceInformationStructured = remittanceInformationStructured;
  }


  public PaymentInitiationWithStatusResponse remittanceInformationUnstructured(String remittanceInformationUnstructured) {
    this.remittanceInformationUnstructured = remittanceInformationUnstructured;
    return this;
  }

  /**
   * Unstructured remittance information. 
   * @return remittanceInformationUnstructured
   */
  @javax.annotation.Nullable
  public String getRemittanceInformationUnstructured() {
    return remittanceInformationUnstructured;
  }

  public void setRemittanceInformationUnstructured(String remittanceInformationUnstructured) {
    this.remittanceInformationUnstructured = remittanceInformationUnstructured;
  }


  public PaymentInitiationWithStatusResponse remittanceInformationUnstructuredArray(List<String> remittanceInformationUnstructuredArray) {
    this.remittanceInformationUnstructuredArray = remittanceInformationUnstructuredArray;
    return this;
  }

  public PaymentInitiationWithStatusResponse addRemittanceInformationUnstructuredArrayItem(String remittanceInformationUnstructuredArrayItem) {
    if (this.remittanceInformationUnstructuredArray == null) {
      this.remittanceInformationUnstructuredArray = new ArrayList<>();
    }
    this.remittanceInformationUnstructuredArray.add(remittanceInformationUnstructuredArrayItem);
    return this;
  }

  /**
   * Array of unstructured remittance information. 
   * @return remittanceInformationUnstructuredArray
   */
  @javax.annotation.Nullable
  public List<String> getRemittanceInformationUnstructuredArray() {
    return remittanceInformationUnstructuredArray;
  }

  public void setRemittanceInformationUnstructuredArray(List<String> remittanceInformationUnstructuredArray) {
    this.remittanceInformationUnstructuredArray = remittanceInformationUnstructuredArray;
  }


  public PaymentInitiationWithStatusResponse requestedExecutionDate(LocalDate requestedExecutionDate) {
    this.requestedExecutionDate = requestedExecutionDate;
    return this;
  }

  /**
   * Get requestedExecutionDate
   * @return requestedExecutionDate
   */
  @javax.annotation.Nullable
  public LocalDate getRequestedExecutionDate() {
    return requestedExecutionDate;
  }

  public void setRequestedExecutionDate(LocalDate requestedExecutionDate) {
    this.requestedExecutionDate = requestedExecutionDate;
  }


  public PaymentInitiationWithStatusResponse requestedExecutionTime(OffsetDateTime requestedExecutionTime) {
    this.requestedExecutionTime = requestedExecutionTime;
    return this;
  }

  /**
   * Get requestedExecutionTime
   * @return requestedExecutionTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getRequestedExecutionTime() {
    return requestedExecutionTime;
  }

  public void setRequestedExecutionTime(OffsetDateTime requestedExecutionTime) {
    this.requestedExecutionTime = requestedExecutionTime;
  }


  public PaymentInitiationWithStatusResponse transactionStatus(TransactionStatus transactionStatus) {
    this.transactionStatus = transactionStatus;
    return this;
  }

  /**
   * Get transactionStatus
   * @return transactionStatus
   */
  @javax.annotation.Nullable
  public TransactionStatus getTransactionStatus() {
    return transactionStatus;
  }

  public void setTransactionStatus(TransactionStatus transactionStatus) {
    this.transactionStatus = transactionStatus;
  }


  public PaymentInitiationWithStatusResponse ultimateCreditor(String ultimateCreditor) {
    this.ultimateCreditor = ultimateCreditor;
    return this;
  }

  /**
   * Ultimate creditor.
   * @return ultimateCreditor
   */
  @javax.annotation.Nullable
  public String getUltimateCreditor() {
    return ultimateCreditor;
  }

  public void setUltimateCreditor(String ultimateCreditor) {
    this.ultimateCreditor = ultimateCreditor;
  }


  public PaymentInitiationWithStatusResponse ultimateDebtor(String ultimateDebtor) {
    this.ultimateDebtor = ultimateDebtor;
    return this;
  }

  /**
   * Ultimate debtor.
   * @return ultimateDebtor
   */
  @javax.annotation.Nullable
  public String getUltimateDebtor() {
    return ultimateDebtor;
  }

  public void setUltimateDebtor(String ultimateDebtor) {
    this.ultimateDebtor = ultimateDebtor;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PaymentInitiationWithStatusResponse paymentInitiationWithStatusResponse = (PaymentInitiationWithStatusResponse) o;
    return Objects.equals(this.creditorAccount, paymentInitiationWithStatusResponse.creditorAccount) &&
        Objects.equals(this.creditorAddress, paymentInitiationWithStatusResponse.creditorAddress) &&
        Objects.equals(this.creditorAgent, paymentInitiationWithStatusResponse.creditorAgent) &&
        Objects.equals(this.creditorName, paymentInitiationWithStatusResponse.creditorName) &&
        Objects.equals(this.debtorAccount, paymentInitiationWithStatusResponse.debtorAccount) &&
        Objects.equals(this.endToEndIdentification, paymentInitiationWithStatusResponse.endToEndIdentification) &&
        Objects.equals(this.instructedAmount, paymentInitiationWithStatusResponse.instructedAmount) &&
        Objects.equals(this.purposeCode, paymentInitiationWithStatusResponse.purposeCode) &&
        Objects.equals(this.remittanceInformationStructured, paymentInitiationWithStatusResponse.remittanceInformationStructured) &&
        Objects.equals(this.remittanceInformationUnstructured, paymentInitiationWithStatusResponse.remittanceInformationUnstructured) &&
        Objects.equals(this.remittanceInformationUnstructuredArray, paymentInitiationWithStatusResponse.remittanceInformationUnstructuredArray) &&
        Objects.equals(this.requestedExecutionDate, paymentInitiationWithStatusResponse.requestedExecutionDate) &&
        Objects.equals(this.requestedExecutionTime, paymentInitiationWithStatusResponse.requestedExecutionTime) &&
        Objects.equals(this.transactionStatus, paymentInitiationWithStatusResponse.transactionStatus) &&
        Objects.equals(this.ultimateCreditor, paymentInitiationWithStatusResponse.ultimateCreditor) &&
        Objects.equals(this.ultimateDebtor, paymentInitiationWithStatusResponse.ultimateDebtor);
  }

  @Override
  public int hashCode() {
    return Objects.hash(creditorAccount, creditorAddress, creditorAgent, creditorName, debtorAccount, endToEndIdentification, instructedAmount, purposeCode, remittanceInformationStructured, remittanceInformationUnstructured, remittanceInformationUnstructuredArray, requestedExecutionDate, requestedExecutionTime, transactionStatus, ultimateCreditor, ultimateDebtor);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PaymentInitiationWithStatusResponse {\n");
    sb.append("    creditorAccount: ").append(toIndentedString(creditorAccount)).append("\n");
    sb.append("    creditorAddress: ").append(toIndentedString(creditorAddress)).append("\n");
    sb.append("    creditorAgent: ").append(toIndentedString(creditorAgent)).append("\n");
    sb.append("    creditorName: ").append(toIndentedString(creditorName)).append("\n");
    sb.append("    debtorAccount: ").append(toIndentedString(debtorAccount)).append("\n");
    sb.append("    endToEndIdentification: ").append(toIndentedString(endToEndIdentification)).append("\n");
    sb.append("    instructedAmount: ").append(toIndentedString(instructedAmount)).append("\n");
    sb.append("    purposeCode: ").append(toIndentedString(purposeCode)).append("\n");
    sb.append("    remittanceInformationStructured: ").append(toIndentedString(remittanceInformationStructured)).append("\n");
    sb.append("    remittanceInformationUnstructured: ").append(toIndentedString(remittanceInformationUnstructured)).append("\n");
    sb.append("    remittanceInformationUnstructuredArray: ").append(toIndentedString(remittanceInformationUnstructuredArray)).append("\n");
    sb.append("    requestedExecutionDate: ").append(toIndentedString(requestedExecutionDate)).append("\n");
    sb.append("    requestedExecutionTime: ").append(toIndentedString(requestedExecutionTime)).append("\n");
    sb.append("    transactionStatus: ").append(toIndentedString(transactionStatus)).append("\n");
    sb.append("    ultimateCreditor: ").append(toIndentedString(ultimateCreditor)).append("\n");
    sb.append("    ultimateDebtor: ").append(toIndentedString(ultimateDebtor)).append("\n");
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
    openapiFields.add("creditorAccount");
    openapiFields.add("creditorAddress");
    openapiFields.add("creditorAgent");
    openapiFields.add("creditorName");
    openapiFields.add("debtorAccount");
    openapiFields.add("endToEndIdentification");
    openapiFields.add("instructedAmount");
    openapiFields.add("purposeCode");
    openapiFields.add("remittanceInformationStructured");
    openapiFields.add("remittanceInformationUnstructured");
    openapiFields.add("remittanceInformationUnstructuredArray");
    openapiFields.add("requestedExecutionDate");
    openapiFields.add("requestedExecutionTime");
    openapiFields.add("transactionStatus");
    openapiFields.add("ultimateCreditor");
    openapiFields.add("ultimateDebtor");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("creditorAccount");
    openapiRequiredFields.add("creditorName");
    openapiRequiredFields.add("debtorAccount");
    openapiRequiredFields.add("instructedAmount");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PaymentInitiationWithStatusResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PaymentInitiationWithStatusResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PaymentInitiationWithStatusResponse is not found in the empty JSON string", PaymentInitiationWithStatusResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PaymentInitiationWithStatusResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PaymentInitiationWithStatusResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PaymentInitiationWithStatusResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `creditorAccount`
      AccountReference16CH.validateJsonElement(jsonObj.get("creditorAccount"));
      // validate the optional field `creditorAddress`
      if (jsonObj.get("creditorAddress") != null && !jsonObj.get("creditorAddress").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("creditorAddress"));
      }
      // validate the optional field `creditorAgent`
      if (jsonObj.get("creditorAgent") != null && !jsonObj.get("creditorAgent").isJsonNull()) {
        CreditorAgent7CH.validateJsonElement(jsonObj.get("creditorAgent"));
      }
      if (!jsonObj.get("creditorName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creditorName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creditorName").toString()));
      }
      // validate the required field `debtorAccount`
      AccountReference16CH.validateJsonElement(jsonObj.get("debtorAccount"));
      if ((jsonObj.get("endToEndIdentification") != null && !jsonObj.get("endToEndIdentification").isJsonNull()) && !jsonObj.get("endToEndIdentification").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endToEndIdentification` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endToEndIdentification").toString()));
      }
      // validate the required field `instructedAmount`
      Amount.validateJsonElement(jsonObj.get("instructedAmount"));
      // validate the optional field `purposeCode`
      if (jsonObj.get("purposeCode") != null && !jsonObj.get("purposeCode").isJsonNull()) {
        PurposeCode.validateJsonElement(jsonObj.get("purposeCode"));
      }
      // validate the optional field `remittanceInformationStructured`
      if (jsonObj.get("remittanceInformationStructured") != null && !jsonObj.get("remittanceInformationStructured").isJsonNull()) {
        RemittanceInformationStructured.validateJsonElement(jsonObj.get("remittanceInformationStructured"));
      }
      if ((jsonObj.get("remittanceInformationUnstructured") != null && !jsonObj.get("remittanceInformationUnstructured").isJsonNull()) && !jsonObj.get("remittanceInformationUnstructured").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `remittanceInformationUnstructured` to be a primitive type in the JSON string but got `%s`", jsonObj.get("remittanceInformationUnstructured").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("remittanceInformationUnstructuredArray") != null && !jsonObj.get("remittanceInformationUnstructuredArray").isJsonNull() && !jsonObj.get("remittanceInformationUnstructuredArray").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `remittanceInformationUnstructuredArray` to be an array in the JSON string but got `%s`", jsonObj.get("remittanceInformationUnstructuredArray").toString()));
      }
      // validate the optional field `transactionStatus`
      if (jsonObj.get("transactionStatus") != null && !jsonObj.get("transactionStatus").isJsonNull()) {
        TransactionStatus.validateJsonElement(jsonObj.get("transactionStatus"));
      }
      if ((jsonObj.get("ultimateCreditor") != null && !jsonObj.get("ultimateCreditor").isJsonNull()) && !jsonObj.get("ultimateCreditor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ultimateCreditor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ultimateCreditor").toString()));
      }
      if ((jsonObj.get("ultimateDebtor") != null && !jsonObj.get("ultimateDebtor").isJsonNull()) && !jsonObj.get("ultimateDebtor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ultimateDebtor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ultimateDebtor").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PaymentInitiationWithStatusResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PaymentInitiationWithStatusResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PaymentInitiationWithStatusResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PaymentInitiationWithStatusResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<PaymentInitiationWithStatusResponse>() {
           @Override
           public void write(JsonWriter out, PaymentInitiationWithStatusResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PaymentInitiationWithStatusResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PaymentInitiationWithStatusResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PaymentInitiationWithStatusResponse
   * @throws IOException if the JSON string is invalid with respect to PaymentInitiationWithStatusResponse
   */
  public static PaymentInitiationWithStatusResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PaymentInitiationWithStatusResponse.class);
  }

  /**
   * Convert an instance of PaymentInitiationWithStatusResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

