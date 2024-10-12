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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.DirectDepositAdditionalDirectDepositInner;
import org.openapitools.client.model.EmployeeAdditionalRateInner;
import org.openapitools.client.model.EmployeeBenefitSetup;
import org.openapitools.client.model.EmployeeCustomBooleanFieldsInner;
import org.openapitools.client.model.EmployeeCustomDateFieldsInner;
import org.openapitools.client.model.EmployeeCustomDropDownFieldsInner;
import org.openapitools.client.model.EmployeeCustomNumberFieldsInner;
import org.openapitools.client.model.EmployeeCustomTextFieldsInner;
import org.openapitools.client.model.EmployeeDepartmentPosition;
import org.openapitools.client.model.EmployeeEmergencyContactsInner;
import org.openapitools.client.model.EmployeeFederalTax;
import org.openapitools.client.model.EmployeeHomeAddress;
import org.openapitools.client.model.EmployeeLocalTaxInner;
import org.openapitools.client.model.EmployeeMainDirectDeposit;
import org.openapitools.client.model.EmployeeNonPrimaryStateTax;
import org.openapitools.client.model.EmployeePrimaryPayRate;
import org.openapitools.client.model.EmployeePrimaryStateTax;
import org.openapitools.client.model.EmployeeStatus;
import org.openapitools.client.model.EmployeeTaxSetup;
import org.openapitools.client.model.EmployeeWebTime;
import org.openapitools.client.model.EmployeeWorkAddress;
import org.openapitools.client.model.EmployeeWorkEligibility;
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
 * The employee model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Employee {
  public static final String SERIALIZED_NAME_ADDITIONAL_DIRECT_DEPOSIT = "additionalDirectDeposit";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_DIRECT_DEPOSIT)
  private List<DirectDepositAdditionalDirectDepositInner> additionalDirectDeposit = new ArrayList<>();

  public static final String SERIALIZED_NAME_ADDITIONAL_RATE = "additionalRate";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_RATE)
  private List<EmployeeAdditionalRateInner> additionalRate = new ArrayList<>();

  public static final String SERIALIZED_NAME_BENEFIT_SETUP = "benefitSetup";
  @SerializedName(SERIALIZED_NAME_BENEFIT_SETUP)
  private EmployeeBenefitSetup benefitSetup;

  public static final String SERIALIZED_NAME_BIRTH_DATE = "birthDate";
  @SerializedName(SERIALIZED_NAME_BIRTH_DATE)
  private String birthDate;

  public static final String SERIALIZED_NAME_CO_EMP_CODE = "coEmpCode";
  @SerializedName(SERIALIZED_NAME_CO_EMP_CODE)
  private String coEmpCode;

  public static final String SERIALIZED_NAME_COMPANY_F_E_I_N = "companyFEIN";
  @SerializedName(SERIALIZED_NAME_COMPANY_F_E_I_N)
  private String companyFEIN;

  public static final String SERIALIZED_NAME_COMPANY_NAME = "companyName";
  @SerializedName(SERIALIZED_NAME_COMPANY_NAME)
  private String companyName;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

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
  private EmployeeDepartmentPosition departmentPosition;

  public static final String SERIALIZED_NAME_DISABILITY_DESCRIPTION = "disabilityDescription";
  @SerializedName(SERIALIZED_NAME_DISABILITY_DESCRIPTION)
  private String disabilityDescription;

  public static final String SERIALIZED_NAME_EMERGENCY_CONTACTS = "emergencyContacts";
  @SerializedName(SERIALIZED_NAME_EMERGENCY_CONTACTS)
  private List<EmployeeEmergencyContactsInner> emergencyContacts = new ArrayList<>();

  public static final String SERIALIZED_NAME_EMPLOYEE_ID = "employeeId";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE_ID)
  private String employeeId;

  public static final String SERIALIZED_NAME_ETHNICITY = "ethnicity";
  @SerializedName(SERIALIZED_NAME_ETHNICITY)
  private String ethnicity;

  public static final String SERIALIZED_NAME_FEDERAL_TAX = "federalTax";
  @SerializedName(SERIALIZED_NAME_FEDERAL_TAX)
  private EmployeeFederalTax federalTax;

  public static final String SERIALIZED_NAME_FIRST_NAME = "firstName";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private String gender;

  public static final String SERIALIZED_NAME_HOME_ADDRESS = "homeAddress";
  @SerializedName(SERIALIZED_NAME_HOME_ADDRESS)
  private EmployeeHomeAddress homeAddress;

  public static final String SERIALIZED_NAME_IS_HIGHLY_COMPENSATED = "isHighlyCompensated";
  @SerializedName(SERIALIZED_NAME_IS_HIGHLY_COMPENSATED)
  private Boolean isHighlyCompensated;

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
  private EmployeeMainDirectDeposit mainDirectDeposit;

  public static final String SERIALIZED_NAME_MARITAL_STATUS = "maritalStatus";
  @SerializedName(SERIALIZED_NAME_MARITAL_STATUS)
  private String maritalStatus;

  public static final String SERIALIZED_NAME_MIDDLE_NAME = "middleName";
  @SerializedName(SERIALIZED_NAME_MIDDLE_NAME)
  private String middleName;

  public static final String SERIALIZED_NAME_NON_PRIMARY_STATE_TAX = "nonPrimaryStateTax";
  @SerializedName(SERIALIZED_NAME_NON_PRIMARY_STATE_TAX)
  private EmployeeNonPrimaryStateTax nonPrimaryStateTax;

  public static final String SERIALIZED_NAME_OWNER_PERCENT = "ownerPercent";
  @SerializedName(SERIALIZED_NAME_OWNER_PERCENT)
  private BigDecimal ownerPercent;

  public static final String SERIALIZED_NAME_PREFERRED_NAME = "preferredName";
  @SerializedName(SERIALIZED_NAME_PREFERRED_NAME)
  private String preferredName;

  public static final String SERIALIZED_NAME_PRIMARY_PAY_RATE = "primaryPayRate";
  @SerializedName(SERIALIZED_NAME_PRIMARY_PAY_RATE)
  private EmployeePrimaryPayRate primaryPayRate;

  public static final String SERIALIZED_NAME_PRIMARY_STATE_TAX = "primaryStateTax";
  @SerializedName(SERIALIZED_NAME_PRIMARY_STATE_TAX)
  private EmployeePrimaryStateTax primaryStateTax;

  public static final String SERIALIZED_NAME_PRIOR_LAST_NAME = "priorLastName";
  @SerializedName(SERIALIZED_NAME_PRIOR_LAST_NAME)
  private String priorLastName;

  public static final String SERIALIZED_NAME_SALUTATION = "salutation";
  @SerializedName(SERIALIZED_NAME_SALUTATION)
  private String salutation;

  public static final String SERIALIZED_NAME_SSN = "ssn";
  @SerializedName(SERIALIZED_NAME_SSN)
  private String ssn;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private EmployeeStatus status;

  public static final String SERIALIZED_NAME_SUFFIX = "suffix";
  @SerializedName(SERIALIZED_NAME_SUFFIX)
  private String suffix;

  public static final String SERIALIZED_NAME_TAX_SETUP = "taxSetup";
  @SerializedName(SERIALIZED_NAME_TAX_SETUP)
  private EmployeeTaxSetup taxSetup;

  public static final String SERIALIZED_NAME_VETERAN_DESCRIPTION = "veteranDescription";
  @SerializedName(SERIALIZED_NAME_VETERAN_DESCRIPTION)
  private String veteranDescription;

  public static final String SERIALIZED_NAME_WEB_TIME = "webTime";
  @SerializedName(SERIALIZED_NAME_WEB_TIME)
  private EmployeeWebTime webTime;

  public static final String SERIALIZED_NAME_WORK_ADDRESS = "workAddress";
  @SerializedName(SERIALIZED_NAME_WORK_ADDRESS)
  private EmployeeWorkAddress workAddress;

  public static final String SERIALIZED_NAME_WORK_ELIGIBILITY = "workEligibility";
  @SerializedName(SERIALIZED_NAME_WORK_ELIGIBILITY)
  private EmployeeWorkEligibility workEligibility;

  public Employee() {
  }

  public Employee additionalDirectDeposit(List<DirectDepositAdditionalDirectDepositInner> additionalDirectDeposit) {
    this.additionalDirectDeposit = additionalDirectDeposit;
    return this;
  }

  public Employee addAdditionalDirectDepositItem(DirectDepositAdditionalDirectDepositInner additionalDirectDepositItem) {
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
  public List<DirectDepositAdditionalDirectDepositInner> getAdditionalDirectDeposit() {
    return additionalDirectDeposit;
  }

  public void setAdditionalDirectDeposit(List<DirectDepositAdditionalDirectDepositInner> additionalDirectDeposit) {
    this.additionalDirectDeposit = additionalDirectDeposit;
  }


  public Employee additionalRate(List<EmployeeAdditionalRateInner> additionalRate) {
    this.additionalRate = additionalRate;
    return this;
  }

  public Employee addAdditionalRateItem(EmployeeAdditionalRateInner additionalRateItem) {
    if (this.additionalRate == null) {
      this.additionalRate = new ArrayList<>();
    }
    this.additionalRate.add(additionalRateItem);
    return this;
  }

  /**
   * Add Additional Rates.
   * @return additionalRate
   */
  @javax.annotation.Nullable
  public List<EmployeeAdditionalRateInner> getAdditionalRate() {
    return additionalRate;
  }

  public void setAdditionalRate(List<EmployeeAdditionalRateInner> additionalRate) {
    this.additionalRate = additionalRate;
  }


  public Employee benefitSetup(EmployeeBenefitSetup benefitSetup) {
    this.benefitSetup = benefitSetup;
    return this;
  }

  /**
   * Get benefitSetup
   * @return benefitSetup
   */
  @javax.annotation.Nullable
  public EmployeeBenefitSetup getBenefitSetup() {
    return benefitSetup;
  }

  public void setBenefitSetup(EmployeeBenefitSetup benefitSetup) {
    this.benefitSetup = benefitSetup;
  }


  public Employee birthDate(String birthDate) {
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


  public Employee coEmpCode(String coEmpCode) {
    this.coEmpCode = coEmpCode;
    return this;
  }

  /**
   * Unique idenifier for SSO.&lt;br  /&gt;Max length: 20
   * @return coEmpCode
   */
  @javax.annotation.Nullable
  public String getCoEmpCode() {
    return coEmpCode;
  }

  public void setCoEmpCode(String coEmpCode) {
    this.coEmpCode = coEmpCode;
  }


  public Employee companyFEIN(String companyFEIN) {
    this.companyFEIN = companyFEIN;
    return this;
  }

  /**
   * Company FEIN as defined in Web Pay, applicable with GET requests only.&lt;br  /&gt; Max length: 20
   * @return companyFEIN
   */
  @javax.annotation.Nullable
  public String getCompanyFEIN() {
    return companyFEIN;
  }

  public void setCompanyFEIN(String companyFEIN) {
    this.companyFEIN = companyFEIN;
  }


  public Employee companyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  /**
   * Company name as defined in Web Pay, applicable with GET requests only.&lt;br  /&gt; Max length: 50
   * @return companyName
   */
  @javax.annotation.Nullable
  public String getCompanyName() {
    return companyName;
  }

  public void setCompanyName(String companyName) {
    this.companyName = companyName;
  }


  public Employee currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Employee is paid in this currency. &lt;br  /&gt;Max length: 30
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public Employee customBooleanFields(List<EmployeeCustomBooleanFieldsInner> customBooleanFields) {
    this.customBooleanFields = customBooleanFields;
    return this;
  }

  public Employee addCustomBooleanFieldsItem(EmployeeCustomBooleanFieldsInner customBooleanFieldsItem) {
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


  public Employee customDateFields(List<EmployeeCustomDateFieldsInner> customDateFields) {
    this.customDateFields = customDateFields;
    return this;
  }

  public Employee addCustomDateFieldsItem(EmployeeCustomDateFieldsInner customDateFieldsItem) {
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


  public Employee customDropDownFields(List<EmployeeCustomDropDownFieldsInner> customDropDownFields) {
    this.customDropDownFields = customDropDownFields;
    return this;
  }

  public Employee addCustomDropDownFieldsItem(EmployeeCustomDropDownFieldsInner customDropDownFieldsItem) {
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


  public Employee customNumberFields(List<EmployeeCustomNumberFieldsInner> customNumberFields) {
    this.customNumberFields = customNumberFields;
    return this;
  }

  public Employee addCustomNumberFieldsItem(EmployeeCustomNumberFieldsInner customNumberFieldsItem) {
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


  public Employee customTextFields(List<EmployeeCustomTextFieldsInner> customTextFields) {
    this.customTextFields = customTextFields;
    return this;
  }

  public Employee addCustomTextFieldsItem(EmployeeCustomTextFieldsInner customTextFieldsItem) {
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


  public Employee departmentPosition(EmployeeDepartmentPosition departmentPosition) {
    this.departmentPosition = departmentPosition;
    return this;
  }

  /**
   * Get departmentPosition
   * @return departmentPosition
   */
  @javax.annotation.Nullable
  public EmployeeDepartmentPosition getDepartmentPosition() {
    return departmentPosition;
  }

  public void setDepartmentPosition(EmployeeDepartmentPosition departmentPosition) {
    this.departmentPosition = departmentPosition;
  }


  public Employee disabilityDescription(String disabilityDescription) {
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


  public Employee emergencyContacts(List<EmployeeEmergencyContactsInner> emergencyContacts) {
    this.emergencyContacts = emergencyContacts;
    return this;
  }

  public Employee addEmergencyContactsItem(EmployeeEmergencyContactsInner emergencyContactsItem) {
    if (this.emergencyContacts == null) {
      this.emergencyContacts = new ArrayList<>();
    }
    this.emergencyContacts.add(emergencyContactsItem);
    return this;
  }

  /**
   * Add or update Emergency Contacts.
   * @return emergencyContacts
   */
  @javax.annotation.Nullable
  public List<EmployeeEmergencyContactsInner> getEmergencyContacts() {
    return emergencyContacts;
  }

  public void setEmergencyContacts(List<EmployeeEmergencyContactsInner> emergencyContacts) {
    this.emergencyContacts = emergencyContacts;
  }


  public Employee employeeId(String employeeId) {
    this.employeeId = employeeId;
    return this;
  }

  /**
   * Leave blank to have Web Pay automatically assign the next available employee ID.&lt;br  /&gt;Max length: 9
   * @return employeeId
   */
  @javax.annotation.Nullable
  public String getEmployeeId() {
    return employeeId;
  }

  public void setEmployeeId(String employeeId) {
    this.employeeId = employeeId;
  }


  public Employee ethnicity(String ethnicity) {
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


  public Employee federalTax(EmployeeFederalTax federalTax) {
    this.federalTax = federalTax;
    return this;
  }

  /**
   * Get federalTax
   * @return federalTax
   */
  @javax.annotation.Nullable
  public EmployeeFederalTax getFederalTax() {
    return federalTax;
  }

  public void setFederalTax(EmployeeFederalTax federalTax) {
    this.federalTax = federalTax;
  }


  public Employee firstName(String firstName) {
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


  public Employee gender(String gender) {
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


  public Employee homeAddress(EmployeeHomeAddress homeAddress) {
    this.homeAddress = homeAddress;
    return this;
  }

  /**
   * Get homeAddress
   * @return homeAddress
   */
  @javax.annotation.Nullable
  public EmployeeHomeAddress getHomeAddress() {
    return homeAddress;
  }

  public void setHomeAddress(EmployeeHomeAddress homeAddress) {
    this.homeAddress = homeAddress;
  }


  public Employee isHighlyCompensated(Boolean isHighlyCompensated) {
    this.isHighlyCompensated = isHighlyCompensated;
    return this;
  }

  /**
   * Indicates if employee meets the highly compensated employee criteria.
   * @return isHighlyCompensated
   */
  @javax.annotation.Nullable
  public Boolean getIsHighlyCompensated() {
    return isHighlyCompensated;
  }

  public void setIsHighlyCompensated(Boolean isHighlyCompensated) {
    this.isHighlyCompensated = isHighlyCompensated;
  }


  public Employee isSmoker(Boolean isSmoker) {
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


  public Employee lastName(String lastName) {
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


  public Employee localTax(List<EmployeeLocalTaxInner> localTax) {
    this.localTax = localTax;
    return this;
  }

  public Employee addLocalTaxItem(EmployeeLocalTaxInner localTaxItem) {
    if (this.localTax == null) {
      this.localTax = new ArrayList<>();
    }
    this.localTax.add(localTaxItem);
    return this;
  }

  /**
   * Add, update, or delete local tax code, filing status, and exemptions including  PA-PSD taxes.
   * @return localTax
   */
  @javax.annotation.Nullable
  public List<EmployeeLocalTaxInner> getLocalTax() {
    return localTax;
  }

  public void setLocalTax(List<EmployeeLocalTaxInner> localTax) {
    this.localTax = localTax;
  }


  public Employee mainDirectDeposit(EmployeeMainDirectDeposit mainDirectDeposit) {
    this.mainDirectDeposit = mainDirectDeposit;
    return this;
  }

  /**
   * Get mainDirectDeposit
   * @return mainDirectDeposit
   */
  @javax.annotation.Nullable
  public EmployeeMainDirectDeposit getMainDirectDeposit() {
    return mainDirectDeposit;
  }

  public void setMainDirectDeposit(EmployeeMainDirectDeposit mainDirectDeposit) {
    this.mainDirectDeposit = mainDirectDeposit;
  }


  public Employee maritalStatus(String maritalStatus) {
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


  public Employee middleName(String middleName) {
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


  public Employee nonPrimaryStateTax(EmployeeNonPrimaryStateTax nonPrimaryStateTax) {
    this.nonPrimaryStateTax = nonPrimaryStateTax;
    return this;
  }

  /**
   * Get nonPrimaryStateTax
   * @return nonPrimaryStateTax
   */
  @javax.annotation.Nullable
  public EmployeeNonPrimaryStateTax getNonPrimaryStateTax() {
    return nonPrimaryStateTax;
  }

  public void setNonPrimaryStateTax(EmployeeNonPrimaryStateTax nonPrimaryStateTax) {
    this.nonPrimaryStateTax = nonPrimaryStateTax;
  }


  public Employee ownerPercent(BigDecimal ownerPercent) {
    this.ownerPercent = ownerPercent;
    return this;
  }

  /**
   * Percentage of employee&#39;s ownership in the company, entered as a whole number. &lt;br  /&gt; Decimal (12,2)
   * @return ownerPercent
   */
  @javax.annotation.Nullable
  public BigDecimal getOwnerPercent() {
    return ownerPercent;
  }

  public void setOwnerPercent(BigDecimal ownerPercent) {
    this.ownerPercent = ownerPercent;
  }


  public Employee preferredName(String preferredName) {
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


  public Employee primaryPayRate(EmployeePrimaryPayRate primaryPayRate) {
    this.primaryPayRate = primaryPayRate;
    return this;
  }

  /**
   * Get primaryPayRate
   * @return primaryPayRate
   */
  @javax.annotation.Nullable
  public EmployeePrimaryPayRate getPrimaryPayRate() {
    return primaryPayRate;
  }

  public void setPrimaryPayRate(EmployeePrimaryPayRate primaryPayRate) {
    this.primaryPayRate = primaryPayRate;
  }


  public Employee primaryStateTax(EmployeePrimaryStateTax primaryStateTax) {
    this.primaryStateTax = primaryStateTax;
    return this;
  }

  /**
   * Get primaryStateTax
   * @return primaryStateTax
   */
  @javax.annotation.Nullable
  public EmployeePrimaryStateTax getPrimaryStateTax() {
    return primaryStateTax;
  }

  public void setPrimaryStateTax(EmployeePrimaryStateTax primaryStateTax) {
    this.primaryStateTax = primaryStateTax;
  }


  public Employee priorLastName(String priorLastName) {
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


  public Employee salutation(String salutation) {
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


  public Employee ssn(String ssn) {
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


  public Employee status(EmployeeStatus status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public EmployeeStatus getStatus() {
    return status;
  }

  public void setStatus(EmployeeStatus status) {
    this.status = status;
  }


  public Employee suffix(String suffix) {
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


  public Employee taxSetup(EmployeeTaxSetup taxSetup) {
    this.taxSetup = taxSetup;
    return this;
  }

  /**
   * Get taxSetup
   * @return taxSetup
   */
  @javax.annotation.Nullable
  public EmployeeTaxSetup getTaxSetup() {
    return taxSetup;
  }

  public void setTaxSetup(EmployeeTaxSetup taxSetup) {
    this.taxSetup = taxSetup;
  }


  public Employee veteranDescription(String veteranDescription) {
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


  public Employee webTime(EmployeeWebTime webTime) {
    this.webTime = webTime;
    return this;
  }

  /**
   * Get webTime
   * @return webTime
   */
  @javax.annotation.Nullable
  public EmployeeWebTime getWebTime() {
    return webTime;
  }

  public void setWebTime(EmployeeWebTime webTime) {
    this.webTime = webTime;
  }


  public Employee workAddress(EmployeeWorkAddress workAddress) {
    this.workAddress = workAddress;
    return this;
  }

  /**
   * Get workAddress
   * @return workAddress
   */
  @javax.annotation.Nullable
  public EmployeeWorkAddress getWorkAddress() {
    return workAddress;
  }

  public void setWorkAddress(EmployeeWorkAddress workAddress) {
    this.workAddress = workAddress;
  }


  public Employee workEligibility(EmployeeWorkEligibility workEligibility) {
    this.workEligibility = workEligibility;
    return this;
  }

  /**
   * Get workEligibility
   * @return workEligibility
   */
  @javax.annotation.Nullable
  public EmployeeWorkEligibility getWorkEligibility() {
    return workEligibility;
  }

  public void setWorkEligibility(EmployeeWorkEligibility workEligibility) {
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
    Employee employee = (Employee) o;
    return Objects.equals(this.additionalDirectDeposit, employee.additionalDirectDeposit) &&
        Objects.equals(this.additionalRate, employee.additionalRate) &&
        Objects.equals(this.benefitSetup, employee.benefitSetup) &&
        Objects.equals(this.birthDate, employee.birthDate) &&
        Objects.equals(this.coEmpCode, employee.coEmpCode) &&
        Objects.equals(this.companyFEIN, employee.companyFEIN) &&
        Objects.equals(this.companyName, employee.companyName) &&
        Objects.equals(this.currency, employee.currency) &&
        Objects.equals(this.customBooleanFields, employee.customBooleanFields) &&
        Objects.equals(this.customDateFields, employee.customDateFields) &&
        Objects.equals(this.customDropDownFields, employee.customDropDownFields) &&
        Objects.equals(this.customNumberFields, employee.customNumberFields) &&
        Objects.equals(this.customTextFields, employee.customTextFields) &&
        Objects.equals(this.departmentPosition, employee.departmentPosition) &&
        Objects.equals(this.disabilityDescription, employee.disabilityDescription) &&
        Objects.equals(this.emergencyContacts, employee.emergencyContacts) &&
        Objects.equals(this.employeeId, employee.employeeId) &&
        Objects.equals(this.ethnicity, employee.ethnicity) &&
        Objects.equals(this.federalTax, employee.federalTax) &&
        Objects.equals(this.firstName, employee.firstName) &&
        Objects.equals(this.gender, employee.gender) &&
        Objects.equals(this.homeAddress, employee.homeAddress) &&
        Objects.equals(this.isHighlyCompensated, employee.isHighlyCompensated) &&
        Objects.equals(this.isSmoker, employee.isSmoker) &&
        Objects.equals(this.lastName, employee.lastName) &&
        Objects.equals(this.localTax, employee.localTax) &&
        Objects.equals(this.mainDirectDeposit, employee.mainDirectDeposit) &&
        Objects.equals(this.maritalStatus, employee.maritalStatus) &&
        Objects.equals(this.middleName, employee.middleName) &&
        Objects.equals(this.nonPrimaryStateTax, employee.nonPrimaryStateTax) &&
        Objects.equals(this.ownerPercent, employee.ownerPercent) &&
        Objects.equals(this.preferredName, employee.preferredName) &&
        Objects.equals(this.primaryPayRate, employee.primaryPayRate) &&
        Objects.equals(this.primaryStateTax, employee.primaryStateTax) &&
        Objects.equals(this.priorLastName, employee.priorLastName) &&
        Objects.equals(this.salutation, employee.salutation) &&
        Objects.equals(this.ssn, employee.ssn) &&
        Objects.equals(this.status, employee.status) &&
        Objects.equals(this.suffix, employee.suffix) &&
        Objects.equals(this.taxSetup, employee.taxSetup) &&
        Objects.equals(this.veteranDescription, employee.veteranDescription) &&
        Objects.equals(this.webTime, employee.webTime) &&
        Objects.equals(this.workAddress, employee.workAddress) &&
        Objects.equals(this.workEligibility, employee.workEligibility);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalDirectDeposit, additionalRate, benefitSetup, birthDate, coEmpCode, companyFEIN, companyName, currency, customBooleanFields, customDateFields, customDropDownFields, customNumberFields, customTextFields, departmentPosition, disabilityDescription, emergencyContacts, employeeId, ethnicity, federalTax, firstName, gender, homeAddress, isHighlyCompensated, isSmoker, lastName, localTax, mainDirectDeposit, maritalStatus, middleName, nonPrimaryStateTax, ownerPercent, preferredName, primaryPayRate, primaryStateTax, priorLastName, salutation, ssn, status, suffix, taxSetup, veteranDescription, webTime, workAddress, workEligibility);
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
    sb.append("class Employee {\n");
    sb.append("    additionalDirectDeposit: ").append(toIndentedString(additionalDirectDeposit)).append("\n");
    sb.append("    additionalRate: ").append(toIndentedString(additionalRate)).append("\n");
    sb.append("    benefitSetup: ").append(toIndentedString(benefitSetup)).append("\n");
    sb.append("    birthDate: ").append(toIndentedString(birthDate)).append("\n");
    sb.append("    coEmpCode: ").append(toIndentedString(coEmpCode)).append("\n");
    sb.append("    companyFEIN: ").append(toIndentedString(companyFEIN)).append("\n");
    sb.append("    companyName: ").append(toIndentedString(companyName)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customBooleanFields: ").append(toIndentedString(customBooleanFields)).append("\n");
    sb.append("    customDateFields: ").append(toIndentedString(customDateFields)).append("\n");
    sb.append("    customDropDownFields: ").append(toIndentedString(customDropDownFields)).append("\n");
    sb.append("    customNumberFields: ").append(toIndentedString(customNumberFields)).append("\n");
    sb.append("    customTextFields: ").append(toIndentedString(customTextFields)).append("\n");
    sb.append("    departmentPosition: ").append(toIndentedString(departmentPosition)).append("\n");
    sb.append("    disabilityDescription: ").append(toIndentedString(disabilityDescription)).append("\n");
    sb.append("    emergencyContacts: ").append(toIndentedString(emergencyContacts)).append("\n");
    sb.append("    employeeId: ").append(toIndentedString(employeeId)).append("\n");
    sb.append("    ethnicity: ").append(toIndentedString(ethnicity)).append("\n");
    sb.append("    federalTax: ").append(toIndentedString(federalTax)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    homeAddress: ").append(toIndentedString(homeAddress)).append("\n");
    sb.append("    isHighlyCompensated: ").append(toIndentedString(isHighlyCompensated)).append("\n");
    sb.append("    isSmoker: ").append(toIndentedString(isSmoker)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    localTax: ").append(toIndentedString(localTax)).append("\n");
    sb.append("    mainDirectDeposit: ").append(toIndentedString(mainDirectDeposit)).append("\n");
    sb.append("    maritalStatus: ").append(toIndentedString(maritalStatus)).append("\n");
    sb.append("    middleName: ").append(toIndentedString(middleName)).append("\n");
    sb.append("    nonPrimaryStateTax: ").append(toIndentedString(nonPrimaryStateTax)).append("\n");
    sb.append("    ownerPercent: ").append(toIndentedString(ownerPercent)).append("\n");
    sb.append("    preferredName: ").append(toIndentedString(preferredName)).append("\n");
    sb.append("    primaryPayRate: ").append(toIndentedString(primaryPayRate)).append("\n");
    sb.append("    primaryStateTax: ").append(toIndentedString(primaryStateTax)).append("\n");
    sb.append("    priorLastName: ").append(toIndentedString(priorLastName)).append("\n");
    sb.append("    salutation: ").append(toIndentedString(salutation)).append("\n");
    sb.append("    ssn: ").append(toIndentedString(ssn)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    suffix: ").append(toIndentedString(suffix)).append("\n");
    sb.append("    taxSetup: ").append(toIndentedString(taxSetup)).append("\n");
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
    openapiFields.add("additionalRate");
    openapiFields.add("benefitSetup");
    openapiFields.add("birthDate");
    openapiFields.add("coEmpCode");
    openapiFields.add("companyFEIN");
    openapiFields.add("companyName");
    openapiFields.add("currency");
    openapiFields.add("customBooleanFields");
    openapiFields.add("customDateFields");
    openapiFields.add("customDropDownFields");
    openapiFields.add("customNumberFields");
    openapiFields.add("customTextFields");
    openapiFields.add("departmentPosition");
    openapiFields.add("disabilityDescription");
    openapiFields.add("emergencyContacts");
    openapiFields.add("employeeId");
    openapiFields.add("ethnicity");
    openapiFields.add("federalTax");
    openapiFields.add("firstName");
    openapiFields.add("gender");
    openapiFields.add("homeAddress");
    openapiFields.add("isHighlyCompensated");
    openapiFields.add("isSmoker");
    openapiFields.add("lastName");
    openapiFields.add("localTax");
    openapiFields.add("mainDirectDeposit");
    openapiFields.add("maritalStatus");
    openapiFields.add("middleName");
    openapiFields.add("nonPrimaryStateTax");
    openapiFields.add("ownerPercent");
    openapiFields.add("preferredName");
    openapiFields.add("primaryPayRate");
    openapiFields.add("primaryStateTax");
    openapiFields.add("priorLastName");
    openapiFields.add("salutation");
    openapiFields.add("ssn");
    openapiFields.add("status");
    openapiFields.add("suffix");
    openapiFields.add("taxSetup");
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
   * @throws IOException if the JSON Element is invalid with respect to Employee
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Employee.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Employee is not found in the empty JSON string", Employee.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Employee.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Employee` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            DirectDepositAdditionalDirectDepositInner.validateJsonElement(jsonArrayadditionalDirectDeposit.get(i));
          };
        }
      }
      if (jsonObj.get("additionalRate") != null && !jsonObj.get("additionalRate").isJsonNull()) {
        JsonArray jsonArrayadditionalRate = jsonObj.getAsJsonArray("additionalRate");
        if (jsonArrayadditionalRate != null) {
          // ensure the json data is an array
          if (!jsonObj.get("additionalRate").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `additionalRate` to be an array in the JSON string but got `%s`", jsonObj.get("additionalRate").toString()));
          }

          // validate the optional field `additionalRate` (array)
          for (int i = 0; i < jsonArrayadditionalRate.size(); i++) {
            EmployeeAdditionalRateInner.validateJsonElement(jsonArrayadditionalRate.get(i));
          };
        }
      }
      // validate the optional field `benefitSetup`
      if (jsonObj.get("benefitSetup") != null && !jsonObj.get("benefitSetup").isJsonNull()) {
        EmployeeBenefitSetup.validateJsonElement(jsonObj.get("benefitSetup"));
      }
      if ((jsonObj.get("birthDate") != null && !jsonObj.get("birthDate").isJsonNull()) && !jsonObj.get("birthDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `birthDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("birthDate").toString()));
      }
      if ((jsonObj.get("coEmpCode") != null && !jsonObj.get("coEmpCode").isJsonNull()) && !jsonObj.get("coEmpCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `coEmpCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("coEmpCode").toString()));
      }
      if ((jsonObj.get("companyFEIN") != null && !jsonObj.get("companyFEIN").isJsonNull()) && !jsonObj.get("companyFEIN").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `companyFEIN` to be a primitive type in the JSON string but got `%s`", jsonObj.get("companyFEIN").toString()));
      }
      if ((jsonObj.get("companyName") != null && !jsonObj.get("companyName").isJsonNull()) && !jsonObj.get("companyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `companyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("companyName").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
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
      // validate the optional field `departmentPosition`
      if (jsonObj.get("departmentPosition") != null && !jsonObj.get("departmentPosition").isJsonNull()) {
        EmployeeDepartmentPosition.validateJsonElement(jsonObj.get("departmentPosition"));
      }
      if ((jsonObj.get("disabilityDescription") != null && !jsonObj.get("disabilityDescription").isJsonNull()) && !jsonObj.get("disabilityDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `disabilityDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("disabilityDescription").toString()));
      }
      if (jsonObj.get("emergencyContacts") != null && !jsonObj.get("emergencyContacts").isJsonNull()) {
        JsonArray jsonArrayemergencyContacts = jsonObj.getAsJsonArray("emergencyContacts");
        if (jsonArrayemergencyContacts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("emergencyContacts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `emergencyContacts` to be an array in the JSON string but got `%s`", jsonObj.get("emergencyContacts").toString()));
          }

          // validate the optional field `emergencyContacts` (array)
          for (int i = 0; i < jsonArrayemergencyContacts.size(); i++) {
            EmployeeEmergencyContactsInner.validateJsonElement(jsonArrayemergencyContacts.get(i));
          };
        }
      }
      if ((jsonObj.get("employeeId") != null && !jsonObj.get("employeeId").isJsonNull()) && !jsonObj.get("employeeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employeeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employeeId").toString()));
      }
      if ((jsonObj.get("ethnicity") != null && !jsonObj.get("ethnicity").isJsonNull()) && !jsonObj.get("ethnicity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ethnicity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ethnicity").toString()));
      }
      // validate the optional field `federalTax`
      if (jsonObj.get("federalTax") != null && !jsonObj.get("federalTax").isJsonNull()) {
        EmployeeFederalTax.validateJsonElement(jsonObj.get("federalTax"));
      }
      if ((jsonObj.get("firstName") != null && !jsonObj.get("firstName").isJsonNull()) && !jsonObj.get("firstName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `firstName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("firstName").toString()));
      }
      if ((jsonObj.get("gender") != null && !jsonObj.get("gender").isJsonNull()) && !jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      // validate the optional field `homeAddress`
      if (jsonObj.get("homeAddress") != null && !jsonObj.get("homeAddress").isJsonNull()) {
        EmployeeHomeAddress.validateJsonElement(jsonObj.get("homeAddress"));
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
      // validate the optional field `mainDirectDeposit`
      if (jsonObj.get("mainDirectDeposit") != null && !jsonObj.get("mainDirectDeposit").isJsonNull()) {
        EmployeeMainDirectDeposit.validateJsonElement(jsonObj.get("mainDirectDeposit"));
      }
      if ((jsonObj.get("maritalStatus") != null && !jsonObj.get("maritalStatus").isJsonNull()) && !jsonObj.get("maritalStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `maritalStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("maritalStatus").toString()));
      }
      if ((jsonObj.get("middleName") != null && !jsonObj.get("middleName").isJsonNull()) && !jsonObj.get("middleName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `middleName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("middleName").toString()));
      }
      // validate the optional field `nonPrimaryStateTax`
      if (jsonObj.get("nonPrimaryStateTax") != null && !jsonObj.get("nonPrimaryStateTax").isJsonNull()) {
        EmployeeNonPrimaryStateTax.validateJsonElement(jsonObj.get("nonPrimaryStateTax"));
      }
      if ((jsonObj.get("preferredName") != null && !jsonObj.get("preferredName").isJsonNull()) && !jsonObj.get("preferredName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preferredName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preferredName").toString()));
      }
      // validate the optional field `primaryPayRate`
      if (jsonObj.get("primaryPayRate") != null && !jsonObj.get("primaryPayRate").isJsonNull()) {
        EmployeePrimaryPayRate.validateJsonElement(jsonObj.get("primaryPayRate"));
      }
      // validate the optional field `primaryStateTax`
      if (jsonObj.get("primaryStateTax") != null && !jsonObj.get("primaryStateTax").isJsonNull()) {
        EmployeePrimaryStateTax.validateJsonElement(jsonObj.get("primaryStateTax"));
      }
      if ((jsonObj.get("priorLastName") != null && !jsonObj.get("priorLastName").isJsonNull()) && !jsonObj.get("priorLastName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `priorLastName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("priorLastName").toString()));
      }
      if ((jsonObj.get("salutation") != null && !jsonObj.get("salutation").isJsonNull()) && !jsonObj.get("salutation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `salutation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("salutation").toString()));
      }
      if ((jsonObj.get("ssn") != null && !jsonObj.get("ssn").isJsonNull()) && !jsonObj.get("ssn").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssn` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssn").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        EmployeeStatus.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("suffix") != null && !jsonObj.get("suffix").isJsonNull()) && !jsonObj.get("suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suffix").toString()));
      }
      // validate the optional field `taxSetup`
      if (jsonObj.get("taxSetup") != null && !jsonObj.get("taxSetup").isJsonNull()) {
        EmployeeTaxSetup.validateJsonElement(jsonObj.get("taxSetup"));
      }
      if ((jsonObj.get("veteranDescription") != null && !jsonObj.get("veteranDescription").isJsonNull()) && !jsonObj.get("veteranDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `veteranDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("veteranDescription").toString()));
      }
      // validate the optional field `webTime`
      if (jsonObj.get("webTime") != null && !jsonObj.get("webTime").isJsonNull()) {
        EmployeeWebTime.validateJsonElement(jsonObj.get("webTime"));
      }
      // validate the optional field `workAddress`
      if (jsonObj.get("workAddress") != null && !jsonObj.get("workAddress").isJsonNull()) {
        EmployeeWorkAddress.validateJsonElement(jsonObj.get("workAddress"));
      }
      // validate the optional field `workEligibility`
      if (jsonObj.get("workEligibility") != null && !jsonObj.get("workEligibility").isJsonNull()) {
        EmployeeWorkEligibility.validateJsonElement(jsonObj.get("workEligibility"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Employee.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Employee' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Employee> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Employee.class));

       return (TypeAdapter<T>) new TypeAdapter<Employee>() {
           @Override
           public void write(JsonWriter out, Employee value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Employee read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Employee given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Employee
   * @throws IOException if the JSON string is invalid with respect to Employee
   */
  public static Employee fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Employee.class);
  }

  /**
   * Convert an instance of Employee to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

