/*
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
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
import java.util.UUID;
import org.openapitools.client.model.PayorAddressV2;
import org.openapitools.client.model.TransmissionTypes2;

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
 * PayorV2
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:55.204956-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PayorV2 {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private PayorAddressV2 address;

  public static final String SERIALIZED_NAME_ALLOWS_LANGUAGE_CHOICE = "allowsLanguageChoice";
  @SerializedName(SERIALIZED_NAME_ALLOWS_LANGUAGE_CHOICE)
  private Boolean allowsLanguageChoice;

  public static final String SERIALIZED_NAME_COLLECTIVE_ALIAS = "collectiveAlias";
  @SerializedName(SERIALIZED_NAME_COLLECTIVE_ALIAS)
  private String collectiveAlias;

  public static final String SERIALIZED_NAME_DBA_NAME = "dbaName";
  @SerializedName(SERIALIZED_NAME_DBA_NAME)
  private String dbaName;

  public static final String SERIALIZED_NAME_INCLUDES_REPORTS = "includesReports";
  @SerializedName(SERIALIZED_NAME_INCLUDES_REPORTS)
  private Boolean includesReports;

  public static final String SERIALIZED_NAME_KYC_STATE = "kycState";
  @SerializedName(SERIALIZED_NAME_KYC_STATE)
  private String kycState;

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private String language;

  public static final String SERIALIZED_NAME_MANAGING_PAYEES = "managingPayees";
  @SerializedName(SERIALIZED_NAME_MANAGING_PAYEES)
  private Boolean managingPayees;

  public static final String SERIALIZED_NAME_MANUAL_LOCKOUT = "manualLockout";
  @SerializedName(SERIALIZED_NAME_MANUAL_LOCKOUT)
  private Boolean manualLockout;

  public static final String SERIALIZED_NAME_MAX_MASTER_PAYOR_ADMINS = "maxMasterPayorAdmins";
  @SerializedName(SERIALIZED_NAME_MAX_MASTER_PAYOR_ADMINS)
  private Integer maxMasterPayorAdmins;

  public static final String SERIALIZED_NAME_OPEN_BANKING_ENABLED = "openBankingEnabled";
  @SerializedName(SERIALIZED_NAME_OPEN_BANKING_ENABLED)
  private Boolean openBankingEnabled;

  public static final String SERIALIZED_NAME_PAYEE_GRACE_PERIOD_DAYS = "payeeGracePeriodDays";
  @SerializedName(SERIALIZED_NAME_PAYEE_GRACE_PERIOD_DAYS)
  private Integer payeeGracePeriodDays;

  public static final String SERIALIZED_NAME_PAYEE_GRACE_PERIOD_PROCESSING_ENABLED = "payeeGracePeriodProcessingEnabled";
  @SerializedName(SERIALIZED_NAME_PAYEE_GRACE_PERIOD_PROCESSING_ENABLED)
  private Boolean payeeGracePeriodProcessingEnabled;

  public static final String SERIALIZED_NAME_PAYMENT_RAILS = "paymentRails";
  @SerializedName(SERIALIZED_NAME_PAYMENT_RAILS)
  private String paymentRails;

  public static final String SERIALIZED_NAME_PAYOR_ID = "payorId";
  @SerializedName(SERIALIZED_NAME_PAYOR_ID)
  private UUID payorId;

  public static final String SERIALIZED_NAME_PAYOR_NAME = "payorName";
  @SerializedName(SERIALIZED_NAME_PAYOR_NAME)
  private String payorName;

  public static final String SERIALIZED_NAME_PAYOR_XID = "payorXid";
  @SerializedName(SERIALIZED_NAME_PAYOR_XID)
  private String payorXid;

  public static final String SERIALIZED_NAME_PRIMARY_CONTACT_EMAIL = "primaryContactEmail";
  @SerializedName(SERIALIZED_NAME_PRIMARY_CONTACT_EMAIL)
  private String primaryContactEmail;

  public static final String SERIALIZED_NAME_PRIMARY_CONTACT_NAME = "primaryContactName";
  @SerializedName(SERIALIZED_NAME_PRIMARY_CONTACT_NAME)
  private String primaryContactName;

  public static final String SERIALIZED_NAME_PRIMARY_CONTACT_PHONE = "primaryContactPhone";
  @SerializedName(SERIALIZED_NAME_PRIMARY_CONTACT_PHONE)
  private String primaryContactPhone;

  public static final String SERIALIZED_NAME_PROVIDER = "provider";
  @SerializedName(SERIALIZED_NAME_PROVIDER)
  private String provider;

  public static final String SERIALIZED_NAME_REMINDER_EMAILS_OPT_OUT = "reminderEmailsOptOut";
  @SerializedName(SERIALIZED_NAME_REMINDER_EMAILS_OPT_OUT)
  private Boolean reminderEmailsOptOut;

  public static final String SERIALIZED_NAME_REMOTE_SYSTEM_IDS = "remoteSystemIds";
  @SerializedName(SERIALIZED_NAME_REMOTE_SYSTEM_IDS)
  private List<String> remoteSystemIds = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUPPORT_CONTACT = "supportContact";
  @SerializedName(SERIALIZED_NAME_SUPPORT_CONTACT)
  private String supportContact;

  public static final String SERIALIZED_NAME_TRANSMISSION_TYPES = "transmissionTypes";
  @SerializedName(SERIALIZED_NAME_TRANSMISSION_TYPES)
  private TransmissionTypes2 transmissionTypes;

  public static final String SERIALIZED_NAME_USD_TXN_VALUE_REPORTING_THRESHOLD = "usdTxnValueReportingThreshold";
  @SerializedName(SERIALIZED_NAME_USD_TXN_VALUE_REPORTING_THRESHOLD)
  private Integer usdTxnValueReportingThreshold;

  public static final String SERIALIZED_NAME_WU_CUSTOMER_ID = "wuCustomerId";
  @SerializedName(SERIALIZED_NAME_WU_CUSTOMER_ID)
  private String wuCustomerId;

  public PayorV2() {
  }

  public PayorV2(
     String kycState, 
     Integer payeeGracePeriodDays, 
     Boolean payeeGracePeriodProcessingEnabled, 
     UUID payorId, 
     Boolean reminderEmailsOptOut
  ) {
    this();
    this.kycState = kycState;
    this.payeeGracePeriodDays = payeeGracePeriodDays;
    this.payeeGracePeriodProcessingEnabled = payeeGracePeriodProcessingEnabled;
    this.payorId = payorId;
    this.reminderEmailsOptOut = reminderEmailsOptOut;
  }

  public PayorV2 address(PayorAddressV2 address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public PayorAddressV2 getAddress() {
    return address;
  }

  public void setAddress(PayorAddressV2 address) {
    this.address = address;
  }


  public PayorV2 allowsLanguageChoice(Boolean allowsLanguageChoice) {
    this.allowsLanguageChoice = allowsLanguageChoice;
    return this;
  }

  /**
   * Whether or not the payor allows language choice in the UI.
   * @return allowsLanguageChoice
   */
  @javax.annotation.Nullable
  public Boolean getAllowsLanguageChoice() {
    return allowsLanguageChoice;
  }

  public void setAllowsLanguageChoice(Boolean allowsLanguageChoice) {
    this.allowsLanguageChoice = allowsLanguageChoice;
  }


  public PayorV2 collectiveAlias(String collectiveAlias) {
    this.collectiveAlias = collectiveAlias;
    return this;
  }

  /**
   * How the payor has chosen to refer to payees.
   * @return collectiveAlias
   */
  @javax.annotation.Nullable
  public String getCollectiveAlias() {
    return collectiveAlias;
  }

  public void setCollectiveAlias(String collectiveAlias) {
    this.collectiveAlias = collectiveAlias;
  }


  public PayorV2 dbaName(String dbaName) {
    this.dbaName = dbaName;
    return this;
  }

  /**
   * The payor’s &#39;Doing Business As&#39; name.
   * @return dbaName
   */
  @javax.annotation.Nullable
  public String getDbaName() {
    return dbaName;
  }

  public void setDbaName(String dbaName) {
    this.dbaName = dbaName;
  }


  public PayorV2 includesReports(Boolean includesReports) {
    this.includesReports = includesReports;
    return this;
  }

  /**
   * Get includesReports
   * @return includesReports
   */
  @javax.annotation.Nullable
  public Boolean getIncludesReports() {
    return includesReports;
  }

  public void setIncludesReports(Boolean includesReports) {
    this.includesReports = includesReports;
  }


  /**
   * The kyc state of the payor. One of the following values: FAILED_KYC, PASSED_KYC, REQUIRES_KYC
   * @return kycState
   */
  @javax.annotation.Nullable
  public String getKycState() {
    return kycState;
  }



  public PayorV2 language(String language) {
    this.language = language;
    return this;
  }

  /**
   * The payor’s language preference. Must be one of [EN, FR]
   * @return language
   */
  @javax.annotation.Nullable
  public String getLanguage() {
    return language;
  }

  public void setLanguage(String language) {
    this.language = language;
  }


  public PayorV2 managingPayees(Boolean managingPayees) {
    this.managingPayees = managingPayees;
    return this;
  }

  /**
   * Get managingPayees
   * @return managingPayees
   */
  @javax.annotation.Nullable
  public Boolean getManagingPayees() {
    return managingPayees;
  }

  public void setManagingPayees(Boolean managingPayees) {
    this.managingPayees = managingPayees;
  }


  public PayorV2 manualLockout(Boolean manualLockout) {
    this.manualLockout = manualLockout;
    return this;
  }

  /**
   * Whether or not the payor has been manually locked by the backoffice.
   * @return manualLockout
   */
  @javax.annotation.Nullable
  public Boolean getManualLockout() {
    return manualLockout;
  }

  public void setManualLockout(Boolean manualLockout) {
    this.manualLockout = manualLockout;
  }


  public PayorV2 maxMasterPayorAdmins(Integer maxMasterPayorAdmins) {
    this.maxMasterPayorAdmins = maxMasterPayorAdmins;
    return this;
  }

  /**
   * Get maxMasterPayorAdmins
   * @return maxMasterPayorAdmins
   */
  @javax.annotation.Nullable
  public Integer getMaxMasterPayorAdmins() {
    return maxMasterPayorAdmins;
  }

  public void setMaxMasterPayorAdmins(Integer maxMasterPayorAdmins) {
    this.maxMasterPayorAdmins = maxMasterPayorAdmins;
  }


  public PayorV2 openBankingEnabled(Boolean openBankingEnabled) {
    this.openBankingEnabled = openBankingEnabled;
    return this;
  }

  /**
   * Is Open Banking supported for this payor
   * @return openBankingEnabled
   */
  @javax.annotation.Nullable
  public Boolean getOpenBankingEnabled() {
    return openBankingEnabled;
  }

  public void setOpenBankingEnabled(Boolean openBankingEnabled) {
    this.openBankingEnabled = openBankingEnabled;
  }


  /**
   * The grace period for paying payees in days.
   * @return payeeGracePeriodDays
   */
  @javax.annotation.Nullable
  public Integer getPayeeGracePeriodDays() {
    return payeeGracePeriodDays;
  }



  /**
   * Whether grace period processing is enabled.
   * @return payeeGracePeriodProcessingEnabled
   */
  @javax.annotation.Nullable
  public Boolean getPayeeGracePeriodProcessingEnabled() {
    return payeeGracePeriodProcessingEnabled;
  }



  public PayorV2 paymentRails(String paymentRails) {
    this.paymentRails = paymentRails;
    return this;
  }

  /**
   * The id of the payment rails
   * @return paymentRails
   */
  @javax.annotation.Nullable
  public String getPaymentRails() {
    return paymentRails;
  }

  public void setPaymentRails(String paymentRails) {
    this.paymentRails = paymentRails;
  }


  /**
   * Get payorId
   * @return payorId
   */
  @javax.annotation.Nonnull
  public UUID getPayorId() {
    return payorId;
  }



  public PayorV2 payorName(String payorName) {
    this.payorName = payorName;
    return this;
  }

  /**
   * The name of the payor.
   * @return payorName
   */
  @javax.annotation.Nonnull
  public String getPayorName() {
    return payorName;
  }

  public void setPayorName(String payorName) {
    this.payorName = payorName;
  }


  public PayorV2 payorXid(String payorXid) {
    this.payorXid = payorXid;
    return this;
  }

  /**
   * A unique identifier that an external system uses to reference the payor in their system
   * @return payorXid
   */
  @javax.annotation.Nullable
  public String getPayorXid() {
    return payorXid;
  }

  public void setPayorXid(String payorXid) {
    this.payorXid = payorXid;
  }


  public PayorV2 primaryContactEmail(String primaryContactEmail) {
    this.primaryContactEmail = primaryContactEmail;
    return this;
  }

  /**
   * Primary contact email for the payor.
   * @return primaryContactEmail
   */
  @javax.annotation.Nullable
  public String getPrimaryContactEmail() {
    return primaryContactEmail;
  }

  public void setPrimaryContactEmail(String primaryContactEmail) {
    this.primaryContactEmail = primaryContactEmail;
  }


  public PayorV2 primaryContactName(String primaryContactName) {
    this.primaryContactName = primaryContactName;
    return this;
  }

  /**
   * Name of primary contact for the payor.
   * @return primaryContactName
   */
  @javax.annotation.Nullable
  public String getPrimaryContactName() {
    return primaryContactName;
  }

  public void setPrimaryContactName(String primaryContactName) {
    this.primaryContactName = primaryContactName;
  }


  public PayorV2 primaryContactPhone(String primaryContactPhone) {
    this.primaryContactPhone = primaryContactPhone;
    return this;
  }

  /**
   * Primary contact phone number for the payor.
   * @return primaryContactPhone
   */
  @javax.annotation.Nullable
  public String getPrimaryContactPhone() {
    return primaryContactPhone;
  }

  public void setPrimaryContactPhone(String primaryContactPhone) {
    this.primaryContactPhone = primaryContactPhone;
  }


  public PayorV2 provider(String provider) {
    this.provider = provider;
    return this;
  }

  /**
   * The source of the payorXid, default is null which means Velo
   * @return provider
   */
  @javax.annotation.Nullable
  public String getProvider() {
    return provider;
  }

  public void setProvider(String provider) {
    this.provider = provider;
  }


  /**
   * Whether or not the payor has opted-out of reminder emails being sent.
   * @return reminderEmailsOptOut
   */
  @javax.annotation.Nullable
  public Boolean getReminderEmailsOptOut() {
    return reminderEmailsOptOut;
  }



  public PayorV2 remoteSystemIds(List<String> remoteSystemIds) {
    this.remoteSystemIds = remoteSystemIds;
    return this;
  }

  public PayorV2 addRemoteSystemIdsItem(String remoteSystemIdsItem) {
    if (this.remoteSystemIds == null) {
      this.remoteSystemIds = new ArrayList<>();
    }
    this.remoteSystemIds.add(remoteSystemIdsItem);
    return this;
  }

  /**
   * The payor’s supported remote systems by id
   * @return remoteSystemIds
   */
  @javax.annotation.Nullable
  public List<String> getRemoteSystemIds() {
    return remoteSystemIds;
  }

  public void setRemoteSystemIds(List<String> remoteSystemIds) {
    this.remoteSystemIds = remoteSystemIds;
  }


  public PayorV2 supportContact(String supportContact) {
    this.supportContact = supportContact;
    return this;
  }

  /**
   * The payor’s support contact email address.
   * @return supportContact
   */
  @javax.annotation.Nullable
  public String getSupportContact() {
    return supportContact;
  }

  public void setSupportContact(String supportContact) {
    this.supportContact = supportContact;
  }


  public PayorV2 transmissionTypes(TransmissionTypes2 transmissionTypes) {
    this.transmissionTypes = transmissionTypes;
    return this;
  }

  /**
   * Get transmissionTypes
   * @return transmissionTypes
   */
  @javax.annotation.Nullable
  public TransmissionTypes2 getTransmissionTypes() {
    return transmissionTypes;
  }

  public void setTransmissionTypes(TransmissionTypes2 transmissionTypes) {
    this.transmissionTypes = transmissionTypes;
  }


  public PayorV2 usdTxnValueReportingThreshold(Integer usdTxnValueReportingThreshold) {
    this.usdTxnValueReportingThreshold = usdTxnValueReportingThreshold;
    return this;
  }

  /**
   * USD in minor units
   * @return usdTxnValueReportingThreshold
   */
  @javax.annotation.Nullable
  public Integer getUsdTxnValueReportingThreshold() {
    return usdTxnValueReportingThreshold;
  }

  public void setUsdTxnValueReportingThreshold(Integer usdTxnValueReportingThreshold) {
    this.usdTxnValueReportingThreshold = usdTxnValueReportingThreshold;
  }


  public PayorV2 wuCustomerId(String wuCustomerId) {
    this.wuCustomerId = wuCustomerId;
    return this;
  }

  /**
   * Get wuCustomerId
   * @return wuCustomerId
   */
  @javax.annotation.Nullable
  public String getWuCustomerId() {
    return wuCustomerId;
  }

  public void setWuCustomerId(String wuCustomerId) {
    this.wuCustomerId = wuCustomerId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PayorV2 payorV2 = (PayorV2) o;
    return Objects.equals(this.address, payorV2.address) &&
        Objects.equals(this.allowsLanguageChoice, payorV2.allowsLanguageChoice) &&
        Objects.equals(this.collectiveAlias, payorV2.collectiveAlias) &&
        Objects.equals(this.dbaName, payorV2.dbaName) &&
        Objects.equals(this.includesReports, payorV2.includesReports) &&
        Objects.equals(this.kycState, payorV2.kycState) &&
        Objects.equals(this.language, payorV2.language) &&
        Objects.equals(this.managingPayees, payorV2.managingPayees) &&
        Objects.equals(this.manualLockout, payorV2.manualLockout) &&
        Objects.equals(this.maxMasterPayorAdmins, payorV2.maxMasterPayorAdmins) &&
        Objects.equals(this.openBankingEnabled, payorV2.openBankingEnabled) &&
        Objects.equals(this.payeeGracePeriodDays, payorV2.payeeGracePeriodDays) &&
        Objects.equals(this.payeeGracePeriodProcessingEnabled, payorV2.payeeGracePeriodProcessingEnabled) &&
        Objects.equals(this.paymentRails, payorV2.paymentRails) &&
        Objects.equals(this.payorId, payorV2.payorId) &&
        Objects.equals(this.payorName, payorV2.payorName) &&
        Objects.equals(this.payorXid, payorV2.payorXid) &&
        Objects.equals(this.primaryContactEmail, payorV2.primaryContactEmail) &&
        Objects.equals(this.primaryContactName, payorV2.primaryContactName) &&
        Objects.equals(this.primaryContactPhone, payorV2.primaryContactPhone) &&
        Objects.equals(this.provider, payorV2.provider) &&
        Objects.equals(this.reminderEmailsOptOut, payorV2.reminderEmailsOptOut) &&
        Objects.equals(this.remoteSystemIds, payorV2.remoteSystemIds) &&
        Objects.equals(this.supportContact, payorV2.supportContact) &&
        Objects.equals(this.transmissionTypes, payorV2.transmissionTypes) &&
        Objects.equals(this.usdTxnValueReportingThreshold, payorV2.usdTxnValueReportingThreshold) &&
        Objects.equals(this.wuCustomerId, payorV2.wuCustomerId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, allowsLanguageChoice, collectiveAlias, dbaName, includesReports, kycState, language, managingPayees, manualLockout, maxMasterPayorAdmins, openBankingEnabled, payeeGracePeriodDays, payeeGracePeriodProcessingEnabled, paymentRails, payorId, payorName, payorXid, primaryContactEmail, primaryContactName, primaryContactPhone, provider, reminderEmailsOptOut, remoteSystemIds, supportContact, transmissionTypes, usdTxnValueReportingThreshold, wuCustomerId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PayorV2 {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    allowsLanguageChoice: ").append(toIndentedString(allowsLanguageChoice)).append("\n");
    sb.append("    collectiveAlias: ").append(toIndentedString(collectiveAlias)).append("\n");
    sb.append("    dbaName: ").append(toIndentedString(dbaName)).append("\n");
    sb.append("    includesReports: ").append(toIndentedString(includesReports)).append("\n");
    sb.append("    kycState: ").append(toIndentedString(kycState)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    managingPayees: ").append(toIndentedString(managingPayees)).append("\n");
    sb.append("    manualLockout: ").append(toIndentedString(manualLockout)).append("\n");
    sb.append("    maxMasterPayorAdmins: ").append(toIndentedString(maxMasterPayorAdmins)).append("\n");
    sb.append("    openBankingEnabled: ").append(toIndentedString(openBankingEnabled)).append("\n");
    sb.append("    payeeGracePeriodDays: ").append(toIndentedString(payeeGracePeriodDays)).append("\n");
    sb.append("    payeeGracePeriodProcessingEnabled: ").append(toIndentedString(payeeGracePeriodProcessingEnabled)).append("\n");
    sb.append("    paymentRails: ").append(toIndentedString(paymentRails)).append("\n");
    sb.append("    payorId: ").append(toIndentedString(payorId)).append("\n");
    sb.append("    payorName: ").append(toIndentedString(payorName)).append("\n");
    sb.append("    payorXid: ").append(toIndentedString(payorXid)).append("\n");
    sb.append("    primaryContactEmail: ").append(toIndentedString(primaryContactEmail)).append("\n");
    sb.append("    primaryContactName: ").append(toIndentedString(primaryContactName)).append("\n");
    sb.append("    primaryContactPhone: ").append(toIndentedString(primaryContactPhone)).append("\n");
    sb.append("    provider: ").append(toIndentedString(provider)).append("\n");
    sb.append("    reminderEmailsOptOut: ").append(toIndentedString(reminderEmailsOptOut)).append("\n");
    sb.append("    remoteSystemIds: ").append(toIndentedString(remoteSystemIds)).append("\n");
    sb.append("    supportContact: ").append(toIndentedString(supportContact)).append("\n");
    sb.append("    transmissionTypes: ").append(toIndentedString(transmissionTypes)).append("\n");
    sb.append("    usdTxnValueReportingThreshold: ").append(toIndentedString(usdTxnValueReportingThreshold)).append("\n");
    sb.append("    wuCustomerId: ").append(toIndentedString(wuCustomerId)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("allowsLanguageChoice");
    openapiFields.add("collectiveAlias");
    openapiFields.add("dbaName");
    openapiFields.add("includesReports");
    openapiFields.add("kycState");
    openapiFields.add("language");
    openapiFields.add("managingPayees");
    openapiFields.add("manualLockout");
    openapiFields.add("maxMasterPayorAdmins");
    openapiFields.add("openBankingEnabled");
    openapiFields.add("payeeGracePeriodDays");
    openapiFields.add("payeeGracePeriodProcessingEnabled");
    openapiFields.add("paymentRails");
    openapiFields.add("payorId");
    openapiFields.add("payorName");
    openapiFields.add("payorXid");
    openapiFields.add("primaryContactEmail");
    openapiFields.add("primaryContactName");
    openapiFields.add("primaryContactPhone");
    openapiFields.add("provider");
    openapiFields.add("reminderEmailsOptOut");
    openapiFields.add("remoteSystemIds");
    openapiFields.add("supportContact");
    openapiFields.add("transmissionTypes");
    openapiFields.add("usdTxnValueReportingThreshold");
    openapiFields.add("wuCustomerId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("payorId");
    openapiRequiredFields.add("payorName");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PayorV2
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PayorV2.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PayorV2 is not found in the empty JSON string", PayorV2.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PayorV2.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PayorV2` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PayorV2.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `address`
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) {
        PayorAddressV2.validateJsonElement(jsonObj.get("address"));
      }
      if ((jsonObj.get("collectiveAlias") != null && !jsonObj.get("collectiveAlias").isJsonNull()) && !jsonObj.get("collectiveAlias").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `collectiveAlias` to be a primitive type in the JSON string but got `%s`", jsonObj.get("collectiveAlias").toString()));
      }
      if ((jsonObj.get("dbaName") != null && !jsonObj.get("dbaName").isJsonNull()) && !jsonObj.get("dbaName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `dbaName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("dbaName").toString()));
      }
      if ((jsonObj.get("kycState") != null && !jsonObj.get("kycState").isJsonNull()) && !jsonObj.get("kycState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `kycState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("kycState").toString()));
      }
      if ((jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) && !jsonObj.get("language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("language").toString()));
      }
      if ((jsonObj.get("paymentRails") != null && !jsonObj.get("paymentRails").isJsonNull()) && !jsonObj.get("paymentRails").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `paymentRails` to be a primitive type in the JSON string but got `%s`", jsonObj.get("paymentRails").toString()));
      }
      if (!jsonObj.get("payorId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payorId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payorId").toString()));
      }
      if (!jsonObj.get("payorName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payorName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payorName").toString()));
      }
      if ((jsonObj.get("payorXid") != null && !jsonObj.get("payorXid").isJsonNull()) && !jsonObj.get("payorXid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payorXid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payorXid").toString()));
      }
      if ((jsonObj.get("primaryContactEmail") != null && !jsonObj.get("primaryContactEmail").isJsonNull()) && !jsonObj.get("primaryContactEmail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primaryContactEmail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primaryContactEmail").toString()));
      }
      if ((jsonObj.get("primaryContactName") != null && !jsonObj.get("primaryContactName").isJsonNull()) && !jsonObj.get("primaryContactName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primaryContactName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primaryContactName").toString()));
      }
      if ((jsonObj.get("primaryContactPhone") != null && !jsonObj.get("primaryContactPhone").isJsonNull()) && !jsonObj.get("primaryContactPhone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primaryContactPhone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primaryContactPhone").toString()));
      }
      if ((jsonObj.get("provider") != null && !jsonObj.get("provider").isJsonNull()) && !jsonObj.get("provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provider").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("remoteSystemIds") != null && !jsonObj.get("remoteSystemIds").isJsonNull() && !jsonObj.get("remoteSystemIds").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `remoteSystemIds` to be an array in the JSON string but got `%s`", jsonObj.get("remoteSystemIds").toString()));
      }
      if ((jsonObj.get("supportContact") != null && !jsonObj.get("supportContact").isJsonNull()) && !jsonObj.get("supportContact").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supportContact` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supportContact").toString()));
      }
      // validate the optional field `transmissionTypes`
      if (jsonObj.get("transmissionTypes") != null && !jsonObj.get("transmissionTypes").isJsonNull()) {
        TransmissionTypes2.validateJsonElement(jsonObj.get("transmissionTypes"));
      }
      if ((jsonObj.get("wuCustomerId") != null && !jsonObj.get("wuCustomerId").isJsonNull()) && !jsonObj.get("wuCustomerId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `wuCustomerId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("wuCustomerId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PayorV2.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PayorV2' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PayorV2> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PayorV2.class));

       return (TypeAdapter<T>) new TypeAdapter<PayorV2>() {
           @Override
           public void write(JsonWriter out, PayorV2 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PayorV2 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PayorV2 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PayorV2
   * @throws IOException if the JSON string is invalid with respect to PayorV2
   */
  public static PayorV2 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PayorV2.class);
  }

  /**
   * Convert an instance of PayorV2 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

