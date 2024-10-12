/*
 * Paylocity API
 * For general questions and support of the API, contact: webservices@paylocity.com  # Overview    Paylocity Web Services API is an externally facing RESTful Internet protocol. The Paylocity API uses HTTP verbs and a RESTful endpoint structure. OAuth 2.0 is used as the API Authorization framework. Request and response payloads are formatted as JSON.  Paylocity supports v1 and v2 versions of its API endpoints. v1, while supported, won't be enhanced with additional functionality. For direct link to v1 documentation, please click [here](https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm). For additional resources regarding v1/v2 differences and conversion path, please contact webservices@paylocity.com.    ##### Setup    Paylocity will provide the secure client credentials and set up the scope (type of requests and allowed company numbers). You will receive the unique client id, secret, and Paylocity public key for the data encryption. The secret will expire in 365 days.   * Paylocity will send you an e-mail 10 days prior to the expiration date for the current secret. If not renewed, the second e-mail notification will be sent 5 days prior to secret's expiration. Each email will contain the code necessary to renew the client secret.   * You can obtain the new secret by calling API endpoint using your current not yet expired credentials and the code that was sent with the notification email. For details on API endpoint, please see Client Credentials section.   * Both the current secret value and the new secret value will be recognized during the transition period. After the current secret expires, you must use the new secret.   * If you were unable to renew the secret via API endpoint, you can still contact Service and they will email you new secret via secure email.      When validating the request, Paylocity API will honor the defaults and required fields set up for the company default New Hire Template as defined in Web Pay.      # Authorization    Paylocity Web Services API uses OAuth2.0 Authentication with JSON Message Format.      All requests of the Paylocity Web Services API require a bearer token which can be obtained by authenticating the client with the Paylocity Web Services API via OAuth 2.0.      The client must request a bearer token from the authorization endpoint:      auth-server for production: https://api.paylocity.com/IdentityServer/connect/token      auth-server for testing: https://apisandbox.paylocity.com/IdentityServer/connect/token    Paylocity reserves the right to impose rate limits on the number of calls made to our APIs. Changes to API features/functionality may be made at anytime with or without prior notice.    ##### Authorization Header    The request is expected to be in the form of a basic authentication request, with the \"Authorization\" header containing the client-id and client-secret. This means the standard base-64 encoded user:password, prefixed with \"Basic\" as the value for the Authorization header, where user is the client-id and password is the client-secret.    ##### Content-Type Header    The \"Content-Type\" header is required to be \"application/x-www-form-urlencoded\".    ##### Additional Values    The request must post the following form encoded values within the request body:        grant_type = client_credentials      scope = WebLinkAPI    ##### Responses    Success will return HTTP 200 OK with JSON content:        {        \"access_token\": \"xxx\",        \"expires_in\": 3600,        \"token_type\": \"Bearer\"      }    # Encryption    Paylocity uses a combination of RSA and AES cryptography. As part of the setup, each client is issued a public RSA key.    Paylocity recommends the encryption of the incoming requests as additional protection of the sensitive data. Clients can opt-out of the encryption during the initial setup process. Opt-out will allow Paylocity to process unencrypted requests.    The Paylocity Public Key has the following properties:    * 2048 bit key size    * PKCS1 key format    * PEM encoding    ##### Properties    * key (base 64 encoded): The AES symmetric key encrypted with the Paylocity Public Key. It is the key used to encrypt the content. Paylocity will decrypt the AES key using RSA decryption and use it to decrypt the content.    * iv (base 64 encoded): The AES IV (Initialization Vector) used when encrypting the content.    * content (base 64 encoded): The AES encrypted request. The key and iv provided in the secureContent request are used by Paylocity for decryption of the content.    We suggest using the following for the AES:    * CBC cipher mode    * PKCS7 padding    * 128 bit block size    * 256 bit key size    ##### Encryption Flow    * Generate the unencrypted JSON payload to POST/PUT  * Encrypt this JSON payload using your _own key and IV_ (NOT with the Paylocity public key)  * RSA encrypt the _key_ you used in step 2 with the Paylocity Public Key, then, base64 encode the result  * Base64 encode the IV used to encrypt the JSON payload in step 2  * Put together a \"securecontent\" JSON object:     {    'secureContent' : {      'key' : -- RSA-encrypted & base64 encoded key from step 3,      'iv' : -- base64 encoded iv from step 4      'content' -- content encrypted with your own key from step 2, base64 encoded    }  }    ##### Sample Example        {        \"secureContent\": {          \"key\": \"eS3aw6H/qzHMJ00gSi6gQ3xa08DPMazk8BFY96Pd99ODA==\",          \"iv\": \"NLyXMGq9svw0XO5aI9BzWw==\",          \"content\": \"gAEOiQltO1w+LzGUoIK8FiYbU42hug94EasSl7N+Q1w=\"        }      }    ##### Sample C# Code        using Newtonsoft.Json;      using System;      using System.IO;      using System.Security.Cryptography;      using System.Text;        public class SecuredContent      {        [JsonProperty(\"key\")]        public string Key { get; set; }          [JsonProperty(\"iv\")]        public string Iv { get; set; }          [JsonProperty(\"content\")]        public string Content { get; set; }        }        public class EndUserSecureRequestExample      {        public string CreateSecuredRequest(FileInfo paylocityPublicKey, string unsecuredJsonRequest)        {          string publicKeyXml = File.ReadAllText(paylocityPublicKey.FullName, Encoding.UTF8);            SecuredContent secureContent = this.CreateSecuredContent(publicKeyXml, unsecuredJsonRequest);            string secureRequest = JsonConvert.SerializeObject(new { secureContent });            return secureRequest;        }          private SecuredContent CreateSecuredContent(string publicKeyXml, string request)        {          using (AesCryptoServiceProvider aesCsp = new AesCryptoServiceProvider())          {            aesCsp.Mode = CipherMode.CBC;            aesCsp.Padding = PaddingMode.PKCS7;            aesCsp.BlockSize = 128;            aesCsp.KeySize = 256;              using (ICryptoTransform crt = aesCsp.CreateEncryptor(aesCsp.Key, aesCsp.IV))            {              using (MemoryStream outputStream = new MemoryStream())              {                using (CryptoStream encryptStream = new CryptoStream(outputStream, crt, CryptoStreamMode.Write))                {                  byte[] encodedRequest = Encoding.UTF8.GetBytes(request);                  encryptStream.Write(encodedRequest, 0, encodedRequest.Length);                  encryptStream.FlushFinalBlock();                  byte[] encryptedRequest = outputStream.ToArray();                    using (RSACryptoServiceProvider crp = new RSACryptoServiceProvider())                  {                    crp.FromXmlstring(publicKeyXml);                    byte[] encryptedKey = crp.Encrypt(aesCsp.Key, false);                      return new SecuredContent()                    {                      Key = Convert.ToBase64string(encryptedKey),                      Iv = Convert.ToBase64string(aesCsp.IV),                      Content = Convert.ToBase64string(encryptedRequest)                    };                  }                }              }            }          }        }      }    ## Support    Questions about using the Paylocity API? Please contact webservices@paylocity.com.    # Deductions (v1)    Deductions API provides endpoints to retrieve, add, update and delete deductions for a company's employees. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.    # OnBoarding (v1)    Onboarding API sends employee data into Paylocity Onboarding to help ensure an easy and accurate hiring process for subsequent completion into Web Pay. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.
 *
 * The version of the OpenAPI document: 2
 * Contact: webservices@paylocity.com
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
import org.openapitools.client.model.EmployeeCustomBooleanFieldsInner;
import org.openapitools.client.model.EmployeeCustomDateFieldsInner;
import org.openapitools.client.model.EmployeeCustomDropDownFieldsInner;
import org.openapitools.client.model.EmployeeCustomNumberFieldsInner;
import org.openapitools.client.model.EmployeeCustomTextFieldsInner;
import org.openapitools.client.model.EmployeeLocalTaxInner;
import org.openapitools.client.model.StagedEmployeeAdditionalDirectDepositInner;
import org.openapitools.client.model.StagedEmployeeBenefitSetupInner;
import org.openapitools.client.model.StagedEmployeeDepartmentPositionInner;
import org.openapitools.client.model.StagedEmployeeFederalTaxInner;
import org.openapitools.client.model.StagedEmployeeHomeAddressInner;
import org.openapitools.client.model.StagedEmployeeMainDirectDepositInner;
import org.openapitools.client.model.StagedEmployeeNonPrimaryStateTaxInner;
import org.openapitools.client.model.StagedEmployeePrimaryPayRateInner;
import org.openapitools.client.model.StagedEmployeePrimaryStateTaxInner;
import org.openapitools.client.model.StagedEmployeeStatusInner;
import org.openapitools.client.model.StagedEmployeeWebTime;
import org.openapitools.client.model.StagedEmployeeWorkAddressInner;
import org.openapitools.client.model.StagedEmployeeWorkEligibilityInner;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * The staged employee model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StagedEmployee {
  public static final String SERIALIZED_NAME_ADDITIONAL_DIRECT_DEPOSIT = "additionalDirectDeposit";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_DIRECT_DEPOSIT)
  private List<StagedEmployeeAdditionalDirectDepositInner> additionalDirectDeposit = new ArrayList<>();

  public static final String SERIALIZED_NAME_BENEFIT_SETUP = "benefitSetup";
  @SerializedName(SERIALIZED_NAME_BENEFIT_SETUP)
  private List<StagedEmployeeBenefitSetupInner> benefitSetup = new ArrayList<>();

  public static final String SERIALIZED_NAME_BIRTH_DATE = "birthDate";
  @SerializedName(SERIALIZED_NAME_BIRTH_DATE)
  private String birthDate;

  public static final String SERIALIZED_NAME_CUSTOM_BOOLEAN_FIELDS = "customBooleanFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_BOOLEAN_FIELDS)
  private List<EmployeeCustomBooleanFieldsInner> customBooleanFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_DATE_FIELDS = "customDateFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_DATE_FIELDS)
  private List<EmployeeCustomDateFieldsInner> customDateFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_DROP_DOWN_FIELDS = "customDropDownFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_DROP_DOWN_FIELDS)
  private List<EmployeeCustomDropDownFieldsInner> customDropDownFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_NUMBER_FIELDS = "customNumberFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_NUMBER_FIELDS)
  private List<EmployeeCustomNumberFieldsInner> customNumberFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_TEXT_FIELDS = "customTextFields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_TEXT_FIELDS)
  private List<EmployeeCustomTextFieldsInner> customTextFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_DEPARTMENT_POSITION = "departmentPosition";
  @SerializedName(SERIALIZED_NAME_DEPARTMENT_POSITION)
  private List<StagedEmployeeDepartmentPositionInner> departmentPosition = new ArrayList<>();

  public static final String SERIALIZED_NAME_DISABILITY_DESCRIPTION = "disabilityDescription";
  @SerializedName(SERIALIZED_NAME_DISABILITY_DESCRIPTION)
  private String disabilityDescription;

  public static final String SERIALIZED_NAME_EMPLOYEE_ID = "employeeId";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE_ID)
  private String employeeId;

  public static final String SERIALIZED_NAME_ETHNICITY = "ethnicity";
  @SerializedName(SERIALIZED_NAME_ETHNICITY)
  private String ethnicity;

  public static final String SERIALIZED_NAME_FEDERAL_TAX = "federalTax";
  @SerializedName(SERIALIZED_NAME_FEDERAL_TAX)
  private List<StagedEmployeeFederalTaxInner> federalTax = new ArrayList<>();

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_FITW_EXEMPT_REASON = "fitwExemptReason";
  @SerializedName(SERIALIZED_NAME_FITW_EXEMPT_REASON)
  private String fitwExemptReason;

  public static final String SERIALIZED_NAME_FUTA_EXEMPT_REASON = "futaExemptReason";
  @SerializedName(SERIALIZED_NAME_FUTA_EXEMPT_REASON)
  private String futaExemptReason;

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_HOME_ADDRESS = "homeAddress";
  @SerializedName(SERIALIZED_NAME_HOME_ADDRESS)
  private List<StagedEmployeeHomeAddressInner> homeAddress = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_EMPLOYEE943 = "isEmployee943";
  @SerializedName(SERIALIZED_NAME_IS_EMPLOYEE943)
  private Boolean isEmployee943;

  public static final String SERIALIZED_NAME_IS_SMOKER = "isSmoker";
  @SerializedName(SERIALIZED_NAME_IS_SMOKER)
  private Boolean isSmoker;

  public static final String SERIALIZED_NAME_LAST_NAME = "lastName";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_LOCAL_TAX = "localTax";
  @SerializedName(SERIALIZED_NAME_LOCAL_TAX)
  private List<EmployeeLocalTaxInner> localTax = new ArrayList<>();

  public static final String SERIALIZED_NAME_MAIN_DIRECT_DEPOSIT = "mainDirectDeposit";
  @SerializedName(SERIALIZED_NAME_MAIN_DIRECT_DEPOSIT)
  private List<StagedEmployeeMainDirectDepositInner> mainDirectDeposit = new ArrayList<>();

  public static final String SERIALIZED_NAME_MARITAL_STATUS = "maritalStatus";
  @SerializedName(SERIALIZED_NAME_MARITAL_STATUS)
  private String maritalStatus;

  public static final String SERIALIZED_NAME_MED_EXEMPT_REASON = "medExemptReason";
  @SerializedName(SERIALIZED_NAME_MED_EXEMPT_REASON)
  private String medExemptReason;

  public static final String SERIALIZED_NAME_MIDDLE_NAME = "middleName";
  @SerializedName(SERIALIZED_NAME_MIDDLE_NAME)
  private String middleName;

  public static final String SERIALIZED_NAME_NON_PRIMARY_STATE_TAX = "nonPrimaryStateTax";
  @SerializedName(SERIALIZED_NAME_NON_PRIMARY_STATE_TAX)
  private List<StagedEmployeeNonPrimaryStateTaxInner> nonPrimaryStateTax = new ArrayList<>();

  public static final String SERIALIZED_NAME_PREFERRED_NAME = "preferredName";
  @SerializedName(SERIALIZED_NAME_PREFERRED_NAME)
  private String preferredName;

  public static final String SERIALIZED_NAME_PRIMARY_PAY_RATE = "primaryPayRate";
  @SerializedName(SERIALIZED_NAME_PRIMARY_PAY_RATE)
  private List<StagedEmployeePrimaryPayRateInner> primaryPayRate = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRIMARY_STATE_TAX = "primaryStateTax";
  @SerializedName(SERIALIZED_NAME_PRIMARY_STATE_TAX)
  private List<StagedEmployeePrimaryStateTaxInner> primaryStateTax = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRIOR_LAST_NAME = "priorLastName";
  @SerializedName(SERIALIZED_NAME_PRIOR_LAST_NAME)
  private String priorLastName;

  public static final String SERIALIZED_NAME_SALUTATION = "salutation";
  @SerializedName(SERIALIZED_NAME_SALUTATION)
  private String salutation;

  public static final String SERIALIZED_NAME_SITW_EXEMPT_REASON = "sitwExemptReason";
  @SerializedName(SERIALIZED_NAME_SITW_EXEMPT_REASON)
  private String sitwExemptReason;

  public static final String SERIALIZED_NAME_SS_EXEMPT_REASON = "ssExemptReason";
  @SerializedName(SERIALIZED_NAME_SS_EXEMPT_REASON)
  private String ssExemptReason;

  public static final String SERIALIZED_NAME_SSN = "ssn";
  @SerializedName(SERIALIZED_NAME_SSN)
  private String ssn;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private List<StagedEmployeeStatusInner> status = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUFFIX = "suffix";
  @SerializedName(SERIALIZED_NAME_SUFFIX)
  private String suffix;

  public static final String SERIALIZED_NAME_SUI_EXEMPT_REASON = "suiExemptReason";
  @SerializedName(SERIALIZED_NAME_SUI_EXEMPT_REASON)
  private String suiExemptReason;

  public static final String SERIALIZED_NAME_SUI_STATE = "suiState";
  @SerializedName(SERIALIZED_NAME_SUI_STATE)
  private String suiState;

  public static final String SERIALIZED_NAME_TAX_DISTRIBUTION_CODE1099_R = "taxDistributionCode1099R";
  @SerializedName(SERIALIZED_NAME_TAX_DISTRIBUTION_CODE1099_R)
  private String taxDistributionCode1099R;

  public static final String SERIALIZED_NAME_TAX_FORM = "taxForm";
  @SerializedName(SERIALIZED_NAME_TAX_FORM)
  private String taxForm;

  public static final String SERIALIZED_NAME_VETERAN_DESCRIPTION = "veteranDescription";
  @SerializedName(SERIALIZED_NAME_VETERAN_DESCRIPTION)
  private String veteranDescription;

  public static final String SERIALIZED_NAME_WEB_TIME = "webTime";
  @SerializedName(SERIALIZED_NAME_WEB_TIME)
  private StagedEmployeeWebTime webTime;

  public static final String SERIALIZED_NAME_WORK_ADDRESS = "workAddress";
  @SerializedName(SERIALIZED_NAME_WORK_ADDRESS)
  private List<StagedEmployeeWorkAddressInner> workAddress = new ArrayList<>();

  public static final String SERIALIZED_NAME_WORK_ELIGIBILITY = "workEligibility";
  @SerializedName(SERIALIZED_NAME_WORK_ELIGIBILITY)
  private List<StagedEmployeeWorkEligibilityInner> workEligibility = new ArrayList<>();

  public StagedEmployee() {
  }

  public StagedEmployee additionalDirectDeposit(List<StagedEmployeeAdditionalDirectDepositInner> additionalDirectDeposit) {
    this.additionalDirectDeposit = additionalDirectDeposit;
    return this;
  }

  public StagedEmployee addAdditionalDirectDepositItem(StagedEmployeeAdditionalDirectDepositInner additionalDirectDepositItem) {
    if (this.additionalDirectDeposit == null) {
      this.additionalDirectDeposit = new ArrayList<>();
    }
    this.additionalDirectDeposit.add(additionalDirectDepositItem);
    return this;
  }

  /**
   * Add up to 19 direct deposit accounts in addition to the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with information provided on the request. GET API will not return direct deposit data.
   * @return additionalDirectDeposit
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeAdditionalDirectDepositInner> getAdditionalDirectDeposit() {
    return additionalDirectDeposit;
  }

  public void setAdditionalDirectDeposit(List<StagedEmployeeAdditionalDirectDepositInner> additionalDirectDeposit) {
    this.additionalDirectDeposit = additionalDirectDeposit;
  }


  public StagedEmployee benefitSetup(List<StagedEmployeeBenefitSetupInner> benefitSetup) {
    this.benefitSetup = benefitSetup;
    return this;
  }

  public StagedEmployee addBenefitSetupItem(StagedEmployeeBenefitSetupInner benefitSetupItem) {
    if (this.benefitSetup == null) {
      this.benefitSetup = new ArrayList<>();
    }
    this.benefitSetup.add(benefitSetupItem);
    return this;
  }

  /**
   * Add setup values used for employee benefits integration, insurance plan settings, and ACA reporting.
   * @return benefitSetup
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeBenefitSetupInner> getBenefitSetup() {
    return benefitSetup;
  }

  public void setBenefitSetup(List<StagedEmployeeBenefitSetupInner> benefitSetup) {
    this.benefitSetup = benefitSetup;
  }


  public StagedEmployee birthDate(String birthDate) {
    this.birthDate = birthDate;
    return this;
  }

  /**
   * Employee birthdate. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return birthDate
   */
  @javax.annotation.Nullable
  public String getBirthDate() {
    return birthDate;
  }

  public void setBirthDate(String birthDate) {
    this.birthDate = birthDate;
  }


  public StagedEmployee customBooleanFields(List<EmployeeCustomBooleanFieldsInner> customBooleanFields) {
    this.customBooleanFields = customBooleanFields;
    return this;
  }

  public StagedEmployee addCustomBooleanFieldsItem(EmployeeCustomBooleanFieldsInner customBooleanFieldsItem) {
    if (this.customBooleanFields == null) {
      this.customBooleanFields = new ArrayList<>();
    }
    this.customBooleanFields.add(customBooleanFieldsItem);
    return this;
  }

  /**
   * Up to 8 custom fields of boolean (checkbox) type value.
   * @return customBooleanFields
   */
  @javax.annotation.Nullable
  public List<EmployeeCustomBooleanFieldsInner> getCustomBooleanFields() {
    return customBooleanFields;
  }

  public void setCustomBooleanFields(List<EmployeeCustomBooleanFieldsInner> customBooleanFields) {
    this.customBooleanFields = customBooleanFields;
  }


  public StagedEmployee customDateFields(List<EmployeeCustomDateFieldsInner> customDateFields) {
    this.customDateFields = customDateFields;
    return this;
  }

  public StagedEmployee addCustomDateFieldsItem(EmployeeCustomDateFieldsInner customDateFieldsItem) {
    if (this.customDateFields == null) {
      this.customDateFields = new ArrayList<>();
    }
    this.customDateFields.add(customDateFieldsItem);
    return this;
  }

  /**
   * Up to 8 custom fields of the date type value.
   * @return customDateFields
   */
  @javax.annotation.Nullable
  public List<EmployeeCustomDateFieldsInner> getCustomDateFields() {
    return customDateFields;
  }

  public void setCustomDateFields(List<EmployeeCustomDateFieldsInner> customDateFields) {
    this.customDateFields = customDateFields;
  }


  public StagedEmployee customDropDownFields(List<EmployeeCustomDropDownFieldsInner> customDropDownFields) {
    this.customDropDownFields = customDropDownFields;
    return this;
  }

  public StagedEmployee addCustomDropDownFieldsItem(EmployeeCustomDropDownFieldsInner customDropDownFieldsItem) {
    if (this.customDropDownFields == null) {
      this.customDropDownFields = new ArrayList<>();
    }
    this.customDropDownFields.add(customDropDownFieldsItem);
    return this;
  }

  /**
   * Up to 8 custom fields of the dropdown type value.
   * @return customDropDownFields
   */
  @javax.annotation.Nullable
  public List<EmployeeCustomDropDownFieldsInner> getCustomDropDownFields() {
    return customDropDownFields;
  }

  public void setCustomDropDownFields(List<EmployeeCustomDropDownFieldsInner> customDropDownFields) {
    this.customDropDownFields = customDropDownFields;
  }


  public StagedEmployee customNumberFields(List<EmployeeCustomNumberFieldsInner> customNumberFields) {
    this.customNumberFields = customNumberFields;
    return this;
  }

  public StagedEmployee addCustomNumberFieldsItem(EmployeeCustomNumberFieldsInner customNumberFieldsItem) {
    if (this.customNumberFields == null) {
      this.customNumberFields = new ArrayList<>();
    }
    this.customNumberFields.add(customNumberFieldsItem);
    return this;
  }

  /**
   * Up to 8 custom fields of numeric type value.
   * @return customNumberFields
   */
  @javax.annotation.Nullable
  public List<EmployeeCustomNumberFieldsInner> getCustomNumberFields() {
    return customNumberFields;
  }

  public void setCustomNumberFields(List<EmployeeCustomNumberFieldsInner> customNumberFields) {
    this.customNumberFields = customNumberFields;
  }


  public StagedEmployee customTextFields(List<EmployeeCustomTextFieldsInner> customTextFields) {
    this.customTextFields = customTextFields;
    return this;
  }

  public StagedEmployee addCustomTextFieldsItem(EmployeeCustomTextFieldsInner customTextFieldsItem) {
    if (this.customTextFields == null) {
      this.customTextFields = new ArrayList<>();
    }
    this.customTextFields.add(customTextFieldsItem);
    return this;
  }

  /**
   * Up to 8 custom fields of text type value.
   * @return customTextFields
   */
  @javax.annotation.Nullable
  public List<EmployeeCustomTextFieldsInner> getCustomTextFields() {
    return customTextFields;
  }

  public void setCustomTextFields(List<EmployeeCustomTextFieldsInner> customTextFields) {
    this.customTextFields = customTextFields;
  }


  public StagedEmployee departmentPosition(List<StagedEmployeeDepartmentPositionInner> departmentPosition) {
    this.departmentPosition = departmentPosition;
    return this;
  }

  public StagedEmployee addDepartmentPositionItem(StagedEmployeeDepartmentPositionInner departmentPositionItem) {
    if (this.departmentPosition == null) {
      this.departmentPosition = new ArrayList<>();
    }
    this.departmentPosition.add(departmentPositionItem);
    return this;
  }

  /**
   * Add home department cost center, position, supervisor, reviewer, employment type, EEO class, pay settings, and union information.
   * @return departmentPosition
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeDepartmentPositionInner> getDepartmentPosition() {
    return departmentPosition;
  }

  public void setDepartmentPosition(List<StagedEmployeeDepartmentPositionInner> departmentPosition) {
    this.departmentPosition = departmentPosition;
  }


  public StagedEmployee disabilityDescription(String disabilityDescription) {
    this.disabilityDescription = disabilityDescription;
    return this;
  }

  /**
   * Indicates if employee has disability status.
   * @return disabilityDescription
   */
  @javax.annotation.Nullable
  public String getDisabilityDescription() {
    return disabilityDescription;
  }

  public void setDisabilityDescription(String disabilityDescription) {
    this.disabilityDescription = disabilityDescription;
  }


  public StagedEmployee employeeId(String employeeId) {
    this.employeeId = employeeId;
    return this;
  }

  /**
   * Leave blank to have Web Pay automatically assign the next available employee ID.&lt;br  /&gt; Max length: 10
   * @return employeeId
   */
  @javax.annotation.Nullable
  public String getEmployeeId() {
    return employeeId;
  }

  public void setEmployeeId(String employeeId) {
    this.employeeId = employeeId;
  }


  public StagedEmployee ethnicity(String ethnicity) {
    this.ethnicity = ethnicity;
    return this;
  }

  /**
   * Employee ethnicity.&lt;br  /&gt; Max length: 10
   * @return ethnicity
   */
  @javax.annotation.Nullable
  public String getEthnicity() {
    return ethnicity;
  }

  public void setEthnicity(String ethnicity) {
    this.ethnicity = ethnicity;
  }


  public StagedEmployee federalTax(List<StagedEmployeeFederalTaxInner> federalTax) {
    this.federalTax = federalTax;
    return this;
  }

  public StagedEmployee addFederalTaxItem(StagedEmployeeFederalTaxInner federalTaxItem) {
    if (this.federalTax == null) {
      this.federalTax = new ArrayList<>();
    }
    this.federalTax.add(federalTaxItem);
    return this;
  }

  /**
   * Add federal tax amount type (taxCalculationCode), amount or percentage, filing status, and exemptions.
   * @return federalTax
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeFederalTaxInner> getFederalTax() {
    return federalTax;
  }

  public void setFederalTax(List<StagedEmployeeFederalTaxInner> federalTax) {
    this.federalTax = federalTax;
  }


  public StagedEmployee firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * Employee first name. &lt;br  /&gt;Max length: 40
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public StagedEmployee fitwExemptReason(String fitwExemptReason) {
    this.fitwExemptReason = fitwExemptReason;
    return this;
  }

  /**
   * Reason code for FITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30
   * @return fitwExemptReason
   */
  @javax.annotation.Nullable
  public String getFitwExemptReason() {
    return fitwExemptReason;
  }

  public void setFitwExemptReason(String fitwExemptReason) {
    this.fitwExemptReason = fitwExemptReason;
  }


  public StagedEmployee futaExemptReason(String futaExemptReason) {
    this.futaExemptReason = futaExemptReason;
    return this;
  }

  /**
   * Reason code for FUTA exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).&lt;br  /&gt; Max length: 30
   * @return futaExemptReason
   */
  @javax.annotation.Nullable
  public String getFutaExemptReason() {
    return futaExemptReason;
  }

  public void setFutaExemptReason(String futaExemptReason) {
    this.futaExemptReason = futaExemptReason;
  }


  public StagedEmployee gender(String gender) {
    this.gender = gender;
    return this;
  }

  /**
   * Employee gender. Common values *M* (Male), *F* (Female). &lt;br  /&gt;Max length: 1
   * @return gender
   */
  @javax.annotation.Nullable
  public String getGender() {
    return gender;
  }

  public void setGender(String gender) {
    this.gender = gender;
  }


  public StagedEmployee homeAddress(List<StagedEmployeeHomeAddressInner> homeAddress) {
    this.homeAddress = homeAddress;
    return this;
  }

  public StagedEmployee addHomeAddressItem(StagedEmployeeHomeAddressInner homeAddressItem) {
    if (this.homeAddress == null) {
      this.homeAddress = new ArrayList<>();
    }
    this.homeAddress.add(homeAddressItem);
    return this;
  }

  /**
   * Add employee&#39;s home address, personal phone numbers, and personal email.
   * @return homeAddress
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeHomeAddressInner> getHomeAddress() {
    return homeAddress;
  }

  public void setHomeAddress(List<StagedEmployeeHomeAddressInner> homeAddress) {
    this.homeAddress = homeAddress;
  }


  public StagedEmployee isEmployee943(Boolean isEmployee943) {
    this.isEmployee943 = isEmployee943;
    return this;
  }

  /**
   * Indicates if employee in agriculture or farming.
   * @return isEmployee943
   */
  @javax.annotation.Nullable
  public Boolean getIsEmployee943() {
    return isEmployee943;
  }

  public void setIsEmployee943(Boolean isEmployee943) {
    this.isEmployee943 = isEmployee943;
  }


  public StagedEmployee isSmoker(Boolean isSmoker) {
    this.isSmoker = isSmoker;
    return this;
  }

  /**
   * Indicates if employee is a smoker.
   * @return isSmoker
   */
  @javax.annotation.Nullable
  public Boolean getIsSmoker() {
    return isSmoker;
  }

  public void setIsSmoker(Boolean isSmoker) {
    this.isSmoker = isSmoker;
  }


  public StagedEmployee lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * Employee last name. &lt;br  /&gt;Max length: 40
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public StagedEmployee localTax(List<EmployeeLocalTaxInner> localTax) {
    this.localTax = localTax;
    return this;
  }

  public StagedEmployee addLocalTaxItem(EmployeeLocalTaxInner localTaxItem) {
    if (this.localTax == null) {
      this.localTax = new ArrayList<>();
    }
    this.localTax.add(localTaxItem);
    return this;
  }

  /**
   * Add local tax code, filing status, and exemptions including PA-PSD taxes.
   * @return localTax
   */
  @javax.annotation.Nullable
  public List<EmployeeLocalTaxInner> getLocalTax() {
    return localTax;
  }

  public void setLocalTax(List<EmployeeLocalTaxInner> localTax) {
    this.localTax = localTax;
  }


  public StagedEmployee mainDirectDeposit(List<StagedEmployeeMainDirectDepositInner> mainDirectDeposit) {
    this.mainDirectDeposit = mainDirectDeposit;
    return this;
  }

  public StagedEmployee addMainDirectDepositItem(StagedEmployeeMainDirectDepositInner mainDirectDepositItem) {
    if (this.mainDirectDeposit == null) {
      this.mainDirectDeposit = new ArrayList<>();
    }
    this.mainDirectDeposit.add(mainDirectDepositItem);
    return this;
  }

  /**
   * Add the main direct deposit account. After deposits are made to any additional direct deposit accounts, the remaining net check is deposited in the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with what is provided on the request. GET API will not return direct deposit data.
   * @return mainDirectDeposit
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeMainDirectDepositInner> getMainDirectDeposit() {
    return mainDirectDeposit;
  }

  public void setMainDirectDeposit(List<StagedEmployeeMainDirectDepositInner> mainDirectDeposit) {
    this.mainDirectDeposit = mainDirectDeposit;
  }


  public StagedEmployee maritalStatus(String maritalStatus) {
    this.maritalStatus = maritalStatus;
    return this;
  }

  /**
   * Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. &lt;br  /&gt;Max length: 10
   * @return maritalStatus
   */
  @javax.annotation.Nullable
  public String getMaritalStatus() {
    return maritalStatus;
  }

  public void setMaritalStatus(String maritalStatus) {
    this.maritalStatus = maritalStatus;
  }


  public StagedEmployee medExemptReason(String medExemptReason) {
    this.medExemptReason = medExemptReason;
    return this;
  }

  /**
   * Reason code for Medicare exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).&lt;br  /&gt; Max length: 30
   * @return medExemptReason
   */
  @javax.annotation.Nullable
  public String getMedExemptReason() {
    return medExemptReason;
  }

  public void setMedExemptReason(String medExemptReason) {
    this.medExemptReason = medExemptReason;
  }


  public StagedEmployee middleName(String middleName) {
    this.middleName = middleName;
    return this;
  }

  /**
   * Employee middle name.&lt;br  /&gt; Max length: 20
   * @return middleName
   */
  @javax.annotation.Nullable
  public String getMiddleName() {
    return middleName;
  }

  public void setMiddleName(String middleName) {
    this.middleName = middleName;
  }


  public StagedEmployee nonPrimaryStateTax(List<StagedEmployeeNonPrimaryStateTaxInner> nonPrimaryStateTax) {
    this.nonPrimaryStateTax = nonPrimaryStateTax;
    return this;
  }

  public StagedEmployee addNonPrimaryStateTaxItem(StagedEmployeeNonPrimaryStateTaxInner nonPrimaryStateTaxItem) {
    if (this.nonPrimaryStateTax == null) {
      this.nonPrimaryStateTax = new ArrayList<>();
    }
    this.nonPrimaryStateTax.add(nonPrimaryStateTaxItem);
    return this;
  }

  /**
   * Add non-primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, supplemental check (specialCheckCalc), and reciprocity code information.
   * @return nonPrimaryStateTax
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeNonPrimaryStateTaxInner> getNonPrimaryStateTax() {
    return nonPrimaryStateTax;
  }

  public void setNonPrimaryStateTax(List<StagedEmployeeNonPrimaryStateTaxInner> nonPrimaryStateTax) {
    this.nonPrimaryStateTax = nonPrimaryStateTax;
  }


  public StagedEmployee preferredName(String preferredName) {
    this.preferredName = preferredName;
    return this;
  }

  /**
   * Employee preferred display name.&lt;br  /&gt; Max length: 20
   * @return preferredName
   */
  @javax.annotation.Nullable
  public String getPreferredName() {
    return preferredName;
  }

  public void setPreferredName(String preferredName) {
    this.preferredName = preferredName;
  }


  public StagedEmployee primaryPayRate(List<StagedEmployeePrimaryPayRateInner> primaryPayRate) {
    this.primaryPayRate = primaryPayRate;
    return this;
  }

  public StagedEmployee addPrimaryPayRateItem(StagedEmployeePrimaryPayRateInner primaryPayRateItem) {
    if (this.primaryPayRate == null) {
      this.primaryPayRate = new ArrayList<>();
    }
    this.primaryPayRate.add(primaryPayRateItem);
    return this;
  }

  /**
   * Add hourly or salary pay rate, effective date, and pay frequency.
   * @return primaryPayRate
   */
  @javax.annotation.Nullable
  public List<StagedEmployeePrimaryPayRateInner> getPrimaryPayRate() {
    return primaryPayRate;
  }

  public void setPrimaryPayRate(List<StagedEmployeePrimaryPayRateInner> primaryPayRate) {
    this.primaryPayRate = primaryPayRate;
  }


  public StagedEmployee primaryStateTax(List<StagedEmployeePrimaryStateTaxInner> primaryStateTax) {
    this.primaryStateTax = primaryStateTax;
    return this;
  }

  public StagedEmployee addPrimaryStateTaxItem(StagedEmployeePrimaryStateTaxInner primaryStateTaxItem) {
    if (this.primaryStateTax == null) {
      this.primaryStateTax = new ArrayList<>();
    }
    this.primaryStateTax.add(primaryStateTaxItem);
    return this;
  }

  /**
   * Add primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, and supplemental check (specialCheckCalc) information. Only one primary state is allowed.
   * @return primaryStateTax
   */
  @javax.annotation.Nullable
  public List<StagedEmployeePrimaryStateTaxInner> getPrimaryStateTax() {
    return primaryStateTax;
  }

  public void setPrimaryStateTax(List<StagedEmployeePrimaryStateTaxInner> primaryStateTax) {
    this.primaryStateTax = primaryStateTax;
  }


  public StagedEmployee priorLastName(String priorLastName) {
    this.priorLastName = priorLastName;
    return this;
  }

  /**
   * Prior last name if applicable.&lt;br  /&gt;Max length: 40
   * @return priorLastName
   */
  @javax.annotation.Nullable
  public String getPriorLastName() {
    return priorLastName;
  }

  public void setPriorLastName(String priorLastName) {
    this.priorLastName = priorLastName;
  }


  public StagedEmployee salutation(String salutation) {
    this.salutation = salutation;
    return this;
  }

  /**
   * Employee preferred salutation. &lt;br  /&gt;Max length: 10
   * @return salutation
   */
  @javax.annotation.Nullable
  public String getSalutation() {
    return salutation;
  }

  public void setSalutation(String salutation) {
    this.salutation = salutation;
  }


  public StagedEmployee sitwExemptReason(String sitwExemptReason) {
    this.sitwExemptReason = sitwExemptReason;
    return this;
  }

  /**
   * Reason code for SITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30
   * @return sitwExemptReason
   */
  @javax.annotation.Nullable
  public String getSitwExemptReason() {
    return sitwExemptReason;
  }

  public void setSitwExemptReason(String sitwExemptReason) {
    this.sitwExemptReason = sitwExemptReason;
  }


  public StagedEmployee ssExemptReason(String ssExemptReason) {
    this.ssExemptReason = ssExemptReason;
    return this;
  }

  /**
   * Reason code for Social Security exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30
   * @return ssExemptReason
   */
  @javax.annotation.Nullable
  public String getSsExemptReason() {
    return ssExemptReason;
  }

  public void setSsExemptReason(String ssExemptReason) {
    this.ssExemptReason = ssExemptReason;
  }


  public StagedEmployee ssn(String ssn) {
    this.ssn = ssn;
    return this;
  }

  /**
   * Employee social security number. Leave it blank if valid social security number not available. &lt;br  /&gt;Max length: 11
   * @return ssn
   */
  @javax.annotation.Nullable
  public String getSsn() {
    return ssn;
  }

  public void setSsn(String ssn) {
    this.ssn = ssn;
  }


  public StagedEmployee status(List<StagedEmployeeStatusInner> status) {
    this.status = status;
    return this;
  }

  public StagedEmployee addStatusItem(StagedEmployeeStatusInner statusItem) {
    if (this.status == null) {
      this.status = new ArrayList<>();
    }
    this.status.add(statusItem);
    return this;
  }

  /**
   * Add employee status, change reason, effective date, and adjusted seniority date. Note that companies that are still in Implementation cannot hire future employees.
   * @return status
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeStatusInner> getStatus() {
    return status;
  }

  public void setStatus(List<StagedEmployeeStatusInner> status) {
    this.status = status;
  }


  public StagedEmployee suffix(String suffix) {
    this.suffix = suffix;
    return this;
  }

  /**
   * Employee name suffix. Common values are *Jr, Sr, II*.&lt;br  /&gt;Max length: 30
   * @return suffix
   */
  @javax.annotation.Nullable
  public String getSuffix() {
    return suffix;
  }

  public void setSuffix(String suffix) {
    this.suffix = suffix;
  }


  public StagedEmployee suiExemptReason(String suiExemptReason) {
    this.suiExemptReason = suiExemptReason;
    return this;
  }

  /**
   * Reason code for SUI exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30
   * @return suiExemptReason
   */
  @javax.annotation.Nullable
  public String getSuiExemptReason() {
    return suiExemptReason;
  }

  public void setSuiExemptReason(String suiExemptReason) {
    this.suiExemptReason = suiExemptReason;
  }


  public StagedEmployee suiState(String suiState) {
    this.suiState = suiState;
    return this;
  }

  /**
   * Employee SUI (State Unemployment Insurance) state. &lt;br  /&gt;Max length: 2
   * @return suiState
   */
  @javax.annotation.Nullable
  public String getSuiState() {
    return suiState;
  }

  public void setSuiState(String suiState) {
    this.suiState = suiState;
  }


  public StagedEmployee taxDistributionCode1099R(String taxDistributionCode1099R) {
    this.taxDistributionCode1099R = taxDistributionCode1099R;
    return this;
  }

  /**
   * Employee 1099R distribution code. Common values are *7* (Normal Distribution), *F* (Charitable Gift Annuity). &lt;br  /&gt;Max length: 1
   * @return taxDistributionCode1099R
   */
  @javax.annotation.Nullable
  public String getTaxDistributionCode1099R() {
    return taxDistributionCode1099R;
  }

  public void setTaxDistributionCode1099R(String taxDistributionCode1099R) {
    this.taxDistributionCode1099R = taxDistributionCode1099R;
  }


  public StagedEmployee taxForm(String taxForm) {
    this.taxForm = taxForm;
    return this;
  }

  /**
   * Employee tax form for reporting income. Valid values are *W2, 1099M, 1099R*. Default is W2. &lt;br  /&gt;Max length: 15
   * @return taxForm
   */
  @javax.annotation.Nullable
  public String getTaxForm() {
    return taxForm;
  }

  public void setTaxForm(String taxForm) {
    this.taxForm = taxForm;
  }


  public StagedEmployee veteranDescription(String veteranDescription) {
    this.veteranDescription = veteranDescription;
    return this;
  }

  /**
   * Indicates if employee is a veteran.
   * @return veteranDescription
   */
  @javax.annotation.Nullable
  public String getVeteranDescription() {
    return veteranDescription;
  }

  public void setVeteranDescription(String veteranDescription) {
    this.veteranDescription = veteranDescription;
  }


  public StagedEmployee webTime(StagedEmployeeWebTime webTime) {
    this.webTime = webTime;
    return this;
  }

  /**
   * Get webTime
   * @return webTime
   */
  @javax.annotation.Nullable
  public StagedEmployeeWebTime getWebTime() {
    return webTime;
  }

  public void setWebTime(StagedEmployeeWebTime webTime) {
    this.webTime = webTime;
  }


  public StagedEmployee workAddress(List<StagedEmployeeWorkAddressInner> workAddress) {
    this.workAddress = workAddress;
    return this;
  }

  public StagedEmployee addWorkAddressItem(StagedEmployeeWorkAddressInner workAddressItem) {
    if (this.workAddress == null) {
      this.workAddress = new ArrayList<>();
    }
    this.workAddress.add(workAddressItem);
    return this;
  }

  /**
   * Add employee&#39;s work address, phone numbers, and email. Work Location drop down field is not included.
   * @return workAddress
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeWorkAddressInner> getWorkAddress() {
    return workAddress;
  }

  public void setWorkAddress(List<StagedEmployeeWorkAddressInner> workAddress) {
    this.workAddress = workAddress;
  }


  public StagedEmployee workEligibility(List<StagedEmployeeWorkEligibilityInner> workEligibility) {
    this.workEligibility = workEligibility;
    return this;
  }

  public StagedEmployee addWorkEligibilityItem(StagedEmployeeWorkEligibilityInner workEligibilityItem) {
    if (this.workEligibility == null) {
      this.workEligibility = new ArrayList<>();
    }
    this.workEligibility.add(workEligibilityItem);
    return this;
  }

  /**
   * Add I-9 work authorization information.
   * @return workEligibility
   */
  @javax.annotation.Nullable
  public List<StagedEmployeeWorkEligibilityInner> getWorkEligibility() {
    return workEligibility;
  }

  public void setWorkEligibility(List<StagedEmployeeWorkEligibilityInner> workEligibility) {
    this.workEligibility = workEligibility;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StagedEmployee stagedEmployee = (StagedEmployee) o;
    return Objects.equals(this.additionalDirectDeposit, stagedEmployee.additionalDirectDeposit) &&
        Objects.equals(this.benefitSetup, stagedEmployee.benefitSetup) &&
        Objects.equals(this.birthDate, stagedEmployee.birthDate) &&
        Objects.equals(this.customBooleanFields, stagedEmployee.customBooleanFields) &&
        Objects.equals(this.customDateFields, stagedEmployee.customDateFields) &&
        Objects.equals(this.customDropDownFields, stagedEmployee.customDropDownFields) &&
        Objects.equals(this.customNumberFields, stagedEmployee.customNumberFields) &&
        Objects.equals(this.customTextFields, stagedEmployee.customTextFields) &&
        Objects.equals(this.departmentPosition, stagedEmployee.departmentPosition) &&
        Objects.equals(this.disabilityDescription, stagedEmployee.disabilityDescription) &&
        Objects.equals(this.employeeId, stagedEmployee.employeeId) &&
        Objects.equals(this.ethnicity, stagedEmployee.ethnicity) &&
        Objects.equals(this.federalTax, stagedEmployee.federalTax) &&
        Objects.equals(this.firstName, stagedEmployee.firstName) &&
        Objects.equals(this.fitwExemptReason, stagedEmployee.fitwExemptReason) &&
        Objects.equals(this.futaExemptReason, stagedEmployee.futaExemptReason) &&
        Objects.equals(this.gender, stagedEmployee.gender) &&
        Objects.equals(this.homeAddress, stagedEmployee.homeAddress) &&
        Objects.equals(this.isEmployee943, stagedEmployee.isEmployee943) &&
        Objects.equals(this.isSmoker, stagedEmployee.isSmoker) &&
        Objects.equals(this.lastName, stagedEmployee.lastName) &&
        Objects.equals(this.localTax, stagedEmployee.localTax) &&
        Objects.equals(this.mainDirectDeposit, stagedEmployee.mainDirectDeposit) &&
        Objects.equals(this.maritalStatus, stagedEmployee.maritalStatus) &&
        Objects.equals(this.medExemptReason, stagedEmployee.medExemptReason) &&
        Objects.equals(this.middleName, stagedEmployee.middleName) &&
        Objects.equals(this.nonPrimaryStateTax, stagedEmployee.nonPrimaryStateTax) &&
        Objects.equals(this.preferredName, stagedEmployee.preferredName) &&
        Objects.equals(this.primaryPayRate, stagedEmployee.primaryPayRate) &&
        Objects.equals(this.primaryStateTax, stagedEmployee.primaryStateTax) &&
        Objects.equals(this.priorLastName, stagedEmployee.priorLastName) &&
        Objects.equals(this.salutation, stagedEmployee.salutation) &&
        Objects.equals(this.sitwExemptReason, stagedEmployee.sitwExemptReason) &&
        Objects.equals(this.ssExemptReason, stagedEmployee.ssExemptReason) &&
        Objects.equals(this.ssn, stagedEmployee.ssn) &&
        Objects.equals(this.status, stagedEmployee.status) &&
        Objects.equals(this.suffix, stagedEmployee.suffix) &&
        Objects.equals(this.suiExemptReason, stagedEmployee.suiExemptReason) &&
        Objects.equals(this.suiState, stagedEmployee.suiState) &&
        Objects.equals(this.taxDistributionCode1099R, stagedEmployee.taxDistributionCode1099R) &&
        Objects.equals(this.taxForm, stagedEmployee.taxForm) &&
        Objects.equals(this.veteranDescription, stagedEmployee.veteranDescription) &&
        Objects.equals(this.webTime, stagedEmployee.webTime) &&
        Objects.equals(this.workAddress, stagedEmployee.workAddress) &&
        Objects.equals(this.workEligibility, stagedEmployee.workEligibility);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalDirectDeposit, benefitSetup, birthDate, customBooleanFields, customDateFields, customDropDownFields, customNumberFields, customTextFields, departmentPosition, disabilityDescription, employeeId, ethnicity, federalTax, firstName, fitwExemptReason, futaExemptReason, gender, homeAddress, isEmployee943, isSmoker, lastName, localTax, mainDirectDeposit, maritalStatus, medExemptReason, middleName, nonPrimaryStateTax, preferredName, primaryPayRate, primaryStateTax, priorLastName, salutation, sitwExemptReason, ssExemptReason, ssn, status, suffix, suiExemptReason, suiState, taxDistributionCode1099R, taxForm, veteranDescription, webTime, workAddress, workEligibility);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StagedEmployee {\n");
    sb.append("    additionalDirectDeposit: ").append(toIndentedString(additionalDirectDeposit)).append("\n");
    sb.append("    benefitSetup: ").append(toIndentedString(benefitSetup)).append("\n");
    sb.append("    birthDate: ").append(toIndentedString(birthDate)).append("\n");
    sb.append("    customBooleanFields: ").append(toIndentedString(customBooleanFields)).append("\n");
    sb.append("    customDateFields: ").append(toIndentedString(customDateFields)).append("\n");
    sb.append("    customDropDownFields: ").append(toIndentedString(customDropDownFields)).append("\n");
    sb.append("    customNumberFields: ").append(toIndentedString(customNumberFields)).append("\n");
    sb.append("    customTextFields: ").append(toIndentedString(customTextFields)).append("\n");
    sb.append("    departmentPosition: ").append(toIndentedString(departmentPosition)).append("\n");
    sb.append("    disabilityDescription: ").append(toIndentedString(disabilityDescription)).append("\n");
    sb.append("    employeeId: ").append(toIndentedString(employeeId)).append("\n");
    sb.append("    ethnicity: ").append(toIndentedString(ethnicity)).append("\n");
    sb.append("    federalTax: ").append(toIndentedString(federalTax)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    fitwExemptReason: ").append(toIndentedString(fitwExemptReason)).append("\n");
    sb.append("    futaExemptReason: ").append(toIndentedString(futaExemptReason)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    homeAddress: ").append(toIndentedString(homeAddress)).append("\n");
    sb.append("    isEmployee943: ").append(toIndentedString(isEmployee943)).append("\n");
    sb.append("    isSmoker: ").append(toIndentedString(isSmoker)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    localTax: ").append(toIndentedString(localTax)).append("\n");
    sb.append("    mainDirectDeposit: ").append(toIndentedString(mainDirectDeposit)).append("\n");
    sb.append("    maritalStatus: ").append(toIndentedString(maritalStatus)).append("\n");
    sb.append("    medExemptReason: ").append(toIndentedString(medExemptReason)).append("\n");
    sb.append("    middleName: ").append(toIndentedString(middleName)).append("\n");
    sb.append("    nonPrimaryStateTax: ").append(toIndentedString(nonPrimaryStateTax)).append("\n");
    sb.append("    preferredName: ").append(toIndentedString(preferredName)).append("\n");
    sb.append("    primaryPayRate: ").append(toIndentedString(primaryPayRate)).append("\n");
    sb.append("    primaryStateTax: ").append(toIndentedString(primaryStateTax)).append("\n");
    sb.append("    priorLastName: ").append(toIndentedString(priorLastName)).append("\n");
    sb.append("    salutation: ").append(toIndentedString(salutation)).append("\n");
    sb.append("    sitwExemptReason: ").append(toIndentedString(sitwExemptReason)).append("\n");
    sb.append("    ssExemptReason: ").append(toIndentedString(ssExemptReason)).append("\n");
    sb.append("    ssn: ").append(toIndentedString(ssn)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    suffix: ").append(toIndentedString(suffix)).append("\n");
    sb.append("    suiExemptReason: ").append(toIndentedString(suiExemptReason)).append("\n");
    sb.append("    suiState: ").append(toIndentedString(suiState)).append("\n");
    sb.append("    taxDistributionCode1099R: ").append(toIndentedString(taxDistributionCode1099R)).append("\n");
    sb.append("    taxForm: ").append(toIndentedString(taxForm)).append("\n");
    sb.append("    veteranDescription: ").append(toIndentedString(veteranDescription)).append("\n");
    sb.append("    webTime: ").append(toIndentedString(webTime)).append("\n");
    sb.append("    workAddress: ").append(toIndentedString(workAddress)).append("\n");
    sb.append("    workEligibility: ").append(toIndentedString(workEligibility)).append("\n");
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
    openapiFields.add("additionalDirectDeposit");
    openapiFields.add("benefitSetup");
    openapiFields.add("birthDate");
    openapiFields.add("customBooleanFields");
    openapiFields.add("customDateFields");
    openapiFields.add("customDropDownFields");
    openapiFields.add("customNumberFields");
    openapiFields.add("customTextFields");
    openapiFields.add("departmentPosition");
    openapiFields.add("disabilityDescription");
    openapiFields.add("employeeId");
    openapiFields.add("ethnicity");
    openapiFields.add("federalTax");
    openapiFields.add("firstName");
    openapiFields.add("fitwExemptReason");
    openapiFields.add("futaExemptReason");
    openapiFields.add("gender");
    openapiFields.add("homeAddress");
    openapiFields.add("isEmployee943");
    openapiFields.add("isSmoker");
    openapiFields.add("lastName");
    openapiFields.add("localTax");
    openapiFields.add("mainDirectDeposit");
    openapiFields.add("maritalStatus");
    openapiFields.add("medExemptReason");
    openapiFields.add("middleName");
    openapiFields.add("nonPrimaryStateTax");
    openapiFields.add("preferredName");
    openapiFields.add("primaryPayRate");
    openapiFields.add("primaryStateTax");
    openapiFields.add("priorLastName");
    openapiFields.add("salutation");
    openapiFields.add("sitwExemptReason");
    openapiFields.add("ssExemptReason");
    openapiFields.add("ssn");
    openapiFields.add("status");
    openapiFields.add("suffix");
    openapiFields.add("suiExemptReason");
    openapiFields.add("suiState");
    openapiFields.add("taxDistributionCode1099R");
    openapiFields.add("taxForm");
    openapiFields.add("veteranDescription");
    openapiFields.add("webTime");
    openapiFields.add("workAddress");
    openapiFields.add("workEligibility");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StagedEmployee
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StagedEmployee.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StagedEmployee is not found in the empty JSON string", StagedEmployee.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StagedEmployee.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StagedEmployee` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("additionalDirectDeposit") != null && !jsonObj.get("additionalDirectDeposit").isJsonNull()) {
        JsonArray jsonArrayadditionalDirectDeposit = jsonObj.getAsJsonArray("additionalDirectDeposit");
        if (jsonArrayadditionalDirectDeposit != null) {
          // ensure the json data is an array
          if (!jsonObj.get("additionalDirectDeposit").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `additionalDirectDeposit` to be an array in the JSON string but got `%s`", jsonObj.get("additionalDirectDeposit").toString()));
          }

          // validate the optional field `additionalDirectDeposit` (array)
          for (int i = 0; i < jsonArrayadditionalDirectDeposit.size(); i++) {
            StagedEmployeeAdditionalDirectDepositInner.validateJsonElement(jsonArrayadditionalDirectDeposit.get(i));
          };
        }
      }
      if (jsonObj.get("benefitSetup") != null && !jsonObj.get("benefitSetup").isJsonNull()) {
        JsonArray jsonArraybenefitSetup = jsonObj.getAsJsonArray("benefitSetup");
        if (jsonArraybenefitSetup != null) {
          // ensure the json data is an array
          if (!jsonObj.get("benefitSetup").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `benefitSetup` to be an array in the JSON string but got `%s`", jsonObj.get("benefitSetup").toString()));
          }

          // validate the optional field `benefitSetup` (array)
          for (int i = 0; i < jsonArraybenefitSetup.size(); i++) {
            StagedEmployeeBenefitSetupInner.validateJsonElement(jsonArraybenefitSetup.get(i));
          };
        }
      }
      if ((jsonObj.get("birthDate") != null && !jsonObj.get("birthDate").isJsonNull()) && !jsonObj.get("birthDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `birthDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("birthDate").toString()));
      }
      if (jsonObj.get("customBooleanFields") != null && !jsonObj.get("customBooleanFields").isJsonNull()) {
        JsonArray jsonArraycustomBooleanFields = jsonObj.getAsJsonArray("customBooleanFields");
        if (jsonArraycustomBooleanFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customBooleanFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customBooleanFields` to be an array in the JSON string but got `%s`", jsonObj.get("customBooleanFields").toString()));
          }

          // validate the optional field `customBooleanFields` (array)
          for (int i = 0; i < jsonArraycustomBooleanFields.size(); i++) {
            EmployeeCustomBooleanFieldsInner.validateJsonElement(jsonArraycustomBooleanFields.get(i));
          };
        }
      }
      if (jsonObj.get("customDateFields") != null && !jsonObj.get("customDateFields").isJsonNull()) {
        JsonArray jsonArraycustomDateFields = jsonObj.getAsJsonArray("customDateFields");
        if (jsonArraycustomDateFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customDateFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customDateFields` to be an array in the JSON string but got `%s`", jsonObj.get("customDateFields").toString()));
          }

          // validate the optional field `customDateFields` (array)
          for (int i = 0; i < jsonArraycustomDateFields.size(); i++) {
            EmployeeCustomDateFieldsInner.validateJsonElement(jsonArraycustomDateFields.get(i));
          };
        }
      }
      if (jsonObj.get("customDropDownFields") != null && !jsonObj.get("customDropDownFields").isJsonNull()) {
        JsonArray jsonArraycustomDropDownFields = jsonObj.getAsJsonArray("customDropDownFields");
        if (jsonArraycustomDropDownFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customDropDownFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customDropDownFields` to be an array in the JSON string but got `%s`", jsonObj.get("customDropDownFields").toString()));
          }

          // validate the optional field `customDropDownFields` (array)
          for (int i = 0; i < jsonArraycustomDropDownFields.size(); i++) {
            EmployeeCustomDropDownFieldsInner.validateJsonElement(jsonArraycustomDropDownFields.get(i));
          };
        }
      }
      if (jsonObj.get("customNumberFields") != null && !jsonObj.get("customNumberFields").isJsonNull()) {
        JsonArray jsonArraycustomNumberFields = jsonObj.getAsJsonArray("customNumberFields");
        if (jsonArraycustomNumberFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customNumberFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customNumberFields` to be an array in the JSON string but got `%s`", jsonObj.get("customNumberFields").toString()));
          }

          // validate the optional field `customNumberFields` (array)
          for (int i = 0; i < jsonArraycustomNumberFields.size(); i++) {
            EmployeeCustomNumberFieldsInner.validateJsonElement(jsonArraycustomNumberFields.get(i));
          };
        }
      }
      if (jsonObj.get("customTextFields") != null && !jsonObj.get("customTextFields").isJsonNull()) {
        JsonArray jsonArraycustomTextFields = jsonObj.getAsJsonArray("customTextFields");
        if (jsonArraycustomTextFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customTextFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customTextFields` to be an array in the JSON string but got `%s`", jsonObj.get("customTextFields").toString()));
          }

          // validate the optional field `customTextFields` (array)
          for (int i = 0; i < jsonArraycustomTextFields.size(); i++) {
            EmployeeCustomTextFieldsInner.validateJsonElement(jsonArraycustomTextFields.get(i));
          };
        }
      }
      if (jsonObj.get("departmentPosition") != null && !jsonObj.get("departmentPosition").isJsonNull()) {
        JsonArray jsonArraydepartmentPosition = jsonObj.getAsJsonArray("departmentPosition");
        if (jsonArraydepartmentPosition != null) {
          // ensure the json data is an array
          if (!jsonObj.get("departmentPosition").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `departmentPosition` to be an array in the JSON string but got `%s`", jsonObj.get("departmentPosition").toString()));
          }

          // validate the optional field `departmentPosition` (array)
          for (int i = 0; i < jsonArraydepartmentPosition.size(); i++) {
            StagedEmployeeDepartmentPositionInner.validateJsonElement(jsonArraydepartmentPosition.get(i));
          };
        }
      }
      if ((jsonObj.get("disabilityDescription") != null && !jsonObj.get("disabilityDescription").isJsonNull()) && !jsonObj.get("disabilityDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `disabilityDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("disabilityDescription").toString()));
      }
      if ((jsonObj.get("employeeId") != null && !jsonObj.get("employeeId").isJsonNull()) && !jsonObj.get("employeeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employeeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employeeId").toString()));
      }
      if ((jsonObj.get("ethnicity") != null && !jsonObj.get("ethnicity").isJsonNull()) && !jsonObj.get("ethnicity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ethnicity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ethnicity").toString()));
      }
      if (jsonObj.get("federalTax") != null && !jsonObj.get("federalTax").isJsonNull()) {
        JsonArray jsonArrayfederalTax = jsonObj.getAsJsonArray("federalTax");
        if (jsonArrayfederalTax != null) {
          // ensure the json data is an array
          if (!jsonObj.get("federalTax").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `federalTax` to be an array in the JSON string but got `%s`", jsonObj.get("federalTax").toString()));
          }

          // validate the optional field `federalTax` (array)
          for (int i = 0; i < jsonArrayfederalTax.size(); i++) {
            StagedEmployeeFederalTaxInner.validateJsonElement(jsonArrayfederalTax.get(i));
          };
        }
      }
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("fitwExemptReason") != null && !jsonObj.get("fitwExemptReason").isJsonNull()) && !jsonObj.get("fitwExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fitwExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fitwExemptReason").toString()));
      }
      if ((jsonObj.get("futaExemptReason") != null && !jsonObj.get("futaExemptReason").isJsonNull()) && !jsonObj.get("futaExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `futaExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("futaExemptReason").toString()));
      }
      if ((jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) && !jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      if (jsonObj.get("homeAddress") != null && !jsonObj.get("homeAddress").isJsonNull()) {
        JsonArray jsonArrayhomeAddress = jsonObj.getAsJsonArray("homeAddress");
        if (jsonArrayhomeAddress != null) {
          // ensure the json data is an array
          if (!jsonObj.get("homeAddress").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `homeAddress` to be an array in the JSON string but got `%s`", jsonObj.get("homeAddress").toString()));
          }

          // validate the optional field `homeAddress` (array)
          for (int i = 0; i < jsonArrayhomeAddress.size(); i++) {
            StagedEmployeeHomeAddressInner.validateJsonElement(jsonArrayhomeAddress.get(i));
          };
        }
      }
      if ((jsonObj.get("lastName") != null && !jsonObj.get("lastName").isJsonNull()) && !jsonObj.get("lastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastName").toString()));
      }
      if (jsonObj.get("localTax") != null && !jsonObj.get("localTax").isJsonNull()) {
        JsonArray jsonArraylocalTax = jsonObj.getAsJsonArray("localTax");
        if (jsonArraylocalTax != null) {
          // ensure the json data is an array
          if (!jsonObj.get("localTax").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `localTax` to be an array in the JSON string but got `%s`", jsonObj.get("localTax").toString()));
          }

          // validate the optional field `localTax` (array)
          for (int i = 0; i < jsonArraylocalTax.size(); i++) {
            EmployeeLocalTaxInner.validateJsonElement(jsonArraylocalTax.get(i));
          };
        }
      }
      if (jsonObj.get("mainDirectDeposit") != null && !jsonObj.get("mainDirectDeposit").isJsonNull()) {
        JsonArray jsonArraymainDirectDeposit = jsonObj.getAsJsonArray("mainDirectDeposit");
        if (jsonArraymainDirectDeposit != null) {
          // ensure the json data is an array
          if (!jsonObj.get("mainDirectDeposit").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `mainDirectDeposit` to be an array in the JSON string but got `%s`", jsonObj.get("mainDirectDeposit").toString()));
          }

          // validate the optional field `mainDirectDeposit` (array)
          for (int i = 0; i < jsonArraymainDirectDeposit.size(); i++) {
            StagedEmployeeMainDirectDepositInner.validateJsonElement(jsonArraymainDirectDeposit.get(i));
          };
        }
      }
      if ((jsonObj.get("maritalStatus") != null && !jsonObj.get("maritalStatus").isJsonNull()) && !jsonObj.get("maritalStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `maritalStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("maritalStatus").toString()));
      }
      if ((jsonObj.get("medExemptReason") != null && !jsonObj.get("medExemptReason").isJsonNull()) && !jsonObj.get("medExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `medExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("medExemptReason").toString()));
      }
      if ((jsonObj.get("middleName") != null && !jsonObj.get("middleName").isJsonNull()) && !jsonObj.get("middleName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `middleName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("middleName").toString()));
      }
      if (jsonObj.get("nonPrimaryStateTax") != null && !jsonObj.get("nonPrimaryStateTax").isJsonNull()) {
        JsonArray jsonArraynonPrimaryStateTax = jsonObj.getAsJsonArray("nonPrimaryStateTax");
        if (jsonArraynonPrimaryStateTax != null) {
          // ensure the json data is an array
          if (!jsonObj.get("nonPrimaryStateTax").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `nonPrimaryStateTax` to be an array in the JSON string but got `%s`", jsonObj.get("nonPrimaryStateTax").toString()));
          }

          // validate the optional field `nonPrimaryStateTax` (array)
          for (int i = 0; i < jsonArraynonPrimaryStateTax.size(); i++) {
            StagedEmployeeNonPrimaryStateTaxInner.validateJsonElement(jsonArraynonPrimaryStateTax.get(i));
          };
        }
      }
      if ((jsonObj.get("preferredName") != null && !jsonObj.get("preferredName").isJsonNull()) && !jsonObj.get("preferredName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preferredName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preferredName").toString()));
      }
      if (jsonObj.get("primaryPayRate") != null && !jsonObj.get("primaryPayRate").isJsonNull()) {
        JsonArray jsonArrayprimaryPayRate = jsonObj.getAsJsonArray("primaryPayRate");
        if (jsonArrayprimaryPayRate != null) {
          // ensure the json data is an array
          if (!jsonObj.get("primaryPayRate").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `primaryPayRate` to be an array in the JSON string but got `%s`", jsonObj.get("primaryPayRate").toString()));
          }

          // validate the optional field `primaryPayRate` (array)
          for (int i = 0; i < jsonArrayprimaryPayRate.size(); i++) {
            StagedEmployeePrimaryPayRateInner.validateJsonElement(jsonArrayprimaryPayRate.get(i));
          };
        }
      }
      if (jsonObj.get("primaryStateTax") != null && !jsonObj.get("primaryStateTax").isJsonNull()) {
        JsonArray jsonArrayprimaryStateTax = jsonObj.getAsJsonArray("primaryStateTax");
        if (jsonArrayprimaryStateTax != null) {
          // ensure the json data is an array
          if (!jsonObj.get("primaryStateTax").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `primaryStateTax` to be an array in the JSON string but got `%s`", jsonObj.get("primaryStateTax").toString()));
          }

          // validate the optional field `primaryStateTax` (array)
          for (int i = 0; i < jsonArrayprimaryStateTax.size(); i++) {
            StagedEmployeePrimaryStateTaxInner.validateJsonElement(jsonArrayprimaryStateTax.get(i));
          };
        }
      }
      if ((jsonObj.get("priorLastName") != null && !jsonObj.get("priorLastName").isJsonNull()) && !jsonObj.get("priorLastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `priorLastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("priorLastName").toString()));
      }
      if ((jsonObj.get("salutation") != null && !jsonObj.get("salutation").isJsonNull()) && !jsonObj.get("salutation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `salutation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("salutation").toString()));
      }
      if ((jsonObj.get("sitwExemptReason") != null && !jsonObj.get("sitwExemptReason").isJsonNull()) && !jsonObj.get("sitwExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sitwExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sitwExemptReason").toString()));
      }
      if ((jsonObj.get("ssExemptReason") != null && !jsonObj.get("ssExemptReason").isJsonNull()) && !jsonObj.get("ssExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssExemptReason").toString()));
      }
      if ((jsonObj.get("ssn") != null && !jsonObj.get("ssn").isJsonNull()) && !jsonObj.get("ssn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssn").toString()));
      }
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        JsonArray jsonArraystatus = jsonObj.getAsJsonArray("status");
        if (jsonArraystatus != null) {
          // ensure the json data is an array
          if (!jsonObj.get("status").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `status` to be an array in the JSON string but got `%s`", jsonObj.get("status").toString()));
          }

          // validate the optional field `status` (array)
          for (int i = 0; i < jsonArraystatus.size(); i++) {
            StagedEmployeeStatusInner.validateJsonElement(jsonArraystatus.get(i));
          };
        }
      }
      if ((jsonObj.get("suffix") != null && !jsonObj.get("suffix").isJsonNull()) && !jsonObj.get("suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suffix").toString()));
      }
      if ((jsonObj.get("suiExemptReason") != null && !jsonObj.get("suiExemptReason").isJsonNull()) && !jsonObj.get("suiExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suiExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suiExemptReason").toString()));
      }
      if ((jsonObj.get("suiState") != null && !jsonObj.get("suiState").isJsonNull()) && !jsonObj.get("suiState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suiState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suiState").toString()));
      }
      if ((jsonObj.get("taxDistributionCode1099R") != null && !jsonObj.get("taxDistributionCode1099R").isJsonNull()) && !jsonObj.get("taxDistributionCode1099R").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `taxDistributionCode1099R` to be a primitive type in the JSON string but got `%s`", jsonObj.get("taxDistributionCode1099R").toString()));
      }
      if ((jsonObj.get("taxForm") != null && !jsonObj.get("taxForm").isJsonNull()) && !jsonObj.get("taxForm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `taxForm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("taxForm").toString()));
      }
      if ((jsonObj.get("veteranDescription") != null && !jsonObj.get("veteranDescription").isJsonNull()) && !jsonObj.get("veteranDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `veteranDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("veteranDescription").toString()));
      }
      // validate the optional field `webTime`
      if (jsonObj.get("webTime") != null && !jsonObj.get("webTime").isJsonNull()) {
        StagedEmployeeWebTime.validateJsonElement(jsonObj.get("webTime"));
      }
      if (jsonObj.get("workAddress") != null && !jsonObj.get("workAddress").isJsonNull()) {
        JsonArray jsonArrayworkAddress = jsonObj.getAsJsonArray("workAddress");
        if (jsonArrayworkAddress != null) {
          // ensure the json data is an array
          if (!jsonObj.get("workAddress").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `workAddress` to be an array in the JSON string but got `%s`", jsonObj.get("workAddress").toString()));
          }

          // validate the optional field `workAddress` (array)
          for (int i = 0; i < jsonArrayworkAddress.size(); i++) {
            StagedEmployeeWorkAddressInner.validateJsonElement(jsonArrayworkAddress.get(i));
          };
        }
      }
      if (jsonObj.get("workEligibility") != null && !jsonObj.get("workEligibility").isJsonNull()) {
        JsonArray jsonArrayworkEligibility = jsonObj.getAsJsonArray("workEligibility");
        if (jsonArrayworkEligibility != null) {
          // ensure the json data is an array
          if (!jsonObj.get("workEligibility").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `workEligibility` to be an array in the JSON string but got `%s`", jsonObj.get("workEligibility").toString()));
          }

          // validate the optional field `workEligibility` (array)
          for (int i = 0; i < jsonArrayworkEligibility.size(); i++) {
            StagedEmployeeWorkEligibilityInner.validateJsonElement(jsonArrayworkEligibility.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StagedEmployee.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StagedEmployee' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StagedEmployee> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StagedEmployee.class));

       return (TypeAdapter<T>) new TypeAdapter<StagedEmployee>() {
           @Override
           public void write(JsonWriter out, StagedEmployee value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StagedEmployee read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StagedEmployee given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StagedEmployee
   * @throws IOException if the JSON string is invalid with respect to StagedEmployee
   */
  public static StagedEmployee fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StagedEmployee.class);
  }

  /**
   * Convert an instance of StagedEmployee to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

