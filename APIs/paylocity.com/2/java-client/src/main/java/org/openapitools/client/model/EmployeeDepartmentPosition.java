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
import java.util.Arrays;
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
 * Add or update home department cost center, position, supervisor, reviewer, employment type, EEO class, pay settings, and union information.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EmployeeDepartmentPosition {
  public static final String SERIALIZED_NAME_CHANGE_REASON = "changeReason";
  @SerializedName(SERIALIZED_NAME_CHANGE_REASON)
  private String changeReason;

  public static final String SERIALIZED_NAME_CLOCK_BADGE_NUMBER = "clockBadgeNumber";
  @SerializedName(SERIALIZED_NAME_CLOCK_BADGE_NUMBER)
  private String clockBadgeNumber;

  public static final String SERIALIZED_NAME_COST_CENTER1 = "costCenter1";
  @SerializedName(SERIALIZED_NAME_COST_CENTER1)
  private String costCenter1;

  public static final String SERIALIZED_NAME_COST_CENTER2 = "costCenter2";
  @SerializedName(SERIALIZED_NAME_COST_CENTER2)
  private String costCenter2;

  public static final String SERIALIZED_NAME_COST_CENTER3 = "costCenter3";
  @SerializedName(SERIALIZED_NAME_COST_CENTER3)
  private String costCenter3;

  public static final String SERIALIZED_NAME_EFFECTIVE_DATE = "effectiveDate";
  @SerializedName(SERIALIZED_NAME_EFFECTIVE_DATE)
  private String effectiveDate;

  public static final String SERIALIZED_NAME_EMPLOYEE_TYPE = "employeeType";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE_TYPE)
  private String employeeType;

  public static final String SERIALIZED_NAME_EQUAL_EMPLOYMENT_OPPORTUNITY_CLASS = "equalEmploymentOpportunityClass";
  @SerializedName(SERIALIZED_NAME_EQUAL_EMPLOYMENT_OPPORTUNITY_CLASS)
  private String equalEmploymentOpportunityClass;

  public static final String SERIALIZED_NAME_IS_MINIMUM_WAGE_EXEMPT = "isMinimumWageExempt";
  @SerializedName(SERIALIZED_NAME_IS_MINIMUM_WAGE_EXEMPT)
  private Boolean isMinimumWageExempt;

  public static final String SERIALIZED_NAME_IS_OVERTIME_EXEMPT = "isOvertimeExempt";
  @SerializedName(SERIALIZED_NAME_IS_OVERTIME_EXEMPT)
  private Boolean isOvertimeExempt;

  public static final String SERIALIZED_NAME_IS_SUPERVISOR_REVIEWER = "isSupervisorReviewer";
  @SerializedName(SERIALIZED_NAME_IS_SUPERVISOR_REVIEWER)
  private Boolean isSupervisorReviewer;

  public static final String SERIALIZED_NAME_IS_UNION_DUES_COLLECTED = "isUnionDuesCollected";
  @SerializedName(SERIALIZED_NAME_IS_UNION_DUES_COLLECTED)
  private Boolean isUnionDuesCollected;

  public static final String SERIALIZED_NAME_IS_UNION_INITIATION_COLLECTED = "isUnionInitiationCollected";
  @SerializedName(SERIALIZED_NAME_IS_UNION_INITIATION_COLLECTED)
  private Boolean isUnionInitiationCollected;

  public static final String SERIALIZED_NAME_JOB_TITLE = "jobTitle";
  @SerializedName(SERIALIZED_NAME_JOB_TITLE)
  private String jobTitle;

  public static final String SERIALIZED_NAME_PAY_GROUP = "payGroup";
  @SerializedName(SERIALIZED_NAME_PAY_GROUP)
  private String payGroup;

  public static final String SERIALIZED_NAME_POSITION_CODE = "positionCode";
  @SerializedName(SERIALIZED_NAME_POSITION_CODE)
  private String positionCode;

  public static final String SERIALIZED_NAME_REVIEWER_COMPANY_NUMBER = "reviewerCompanyNumber";
  @SerializedName(SERIALIZED_NAME_REVIEWER_COMPANY_NUMBER)
  private String reviewerCompanyNumber;

  public static final String SERIALIZED_NAME_REVIEWER_EMPLOYEE_ID = "reviewerEmployeeId";
  @SerializedName(SERIALIZED_NAME_REVIEWER_EMPLOYEE_ID)
  private String reviewerEmployeeId;

  public static final String SERIALIZED_NAME_SHIFT = "shift";
  @SerializedName(SERIALIZED_NAME_SHIFT)
  private String shift;

  public static final String SERIALIZED_NAME_SUPERVISOR_COMPANY_NUMBER = "supervisorCompanyNumber";
  @SerializedName(SERIALIZED_NAME_SUPERVISOR_COMPANY_NUMBER)
  private String supervisorCompanyNumber;

  public static final String SERIALIZED_NAME_SUPERVISOR_EMPLOYEE_ID = "supervisorEmployeeId";
  @SerializedName(SERIALIZED_NAME_SUPERVISOR_EMPLOYEE_ID)
  private String supervisorEmployeeId;

  public static final String SERIALIZED_NAME_TIPPED = "tipped";
  @SerializedName(SERIALIZED_NAME_TIPPED)
  private String tipped;

  public static final String SERIALIZED_NAME_UNION_AFFILIATION_DATE = "unionAffiliationDate";
  @SerializedName(SERIALIZED_NAME_UNION_AFFILIATION_DATE)
  private String unionAffiliationDate;

  public static final String SERIALIZED_NAME_UNION_CODE = "unionCode";
  @SerializedName(SERIALIZED_NAME_UNION_CODE)
  private String unionCode;

  public static final String SERIALIZED_NAME_UNION_POSITION = "unionPosition";
  @SerializedName(SERIALIZED_NAME_UNION_POSITION)
  private String unionPosition;

  public static final String SERIALIZED_NAME_WORKERS_COMPENSATION = "workersCompensation";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMPENSATION)
  private String workersCompensation;

  public EmployeeDepartmentPosition() {
  }

  public EmployeeDepartmentPosition changeReason(String changeReason) {
    this.changeReason = changeReason;
    return this;
  }

  /**
   * Employee department/position change reason. Must match Company setup. &lt;br  /&gt;Max length: 15
   * @return changeReason
   */
  @javax.annotation.Nullable
  public String getChangeReason() {
    return changeReason;
  }

  public void setChangeReason(String changeReason) {
    this.changeReason = changeReason;
  }


  public EmployeeDepartmentPosition clockBadgeNumber(String clockBadgeNumber) {
    this.clockBadgeNumber = clockBadgeNumber;
    return this;
  }

  /**
   * Employee clock badge number. Defaults to employeeId. &lt;br  /&gt;Max length: 10
   * @return clockBadgeNumber
   */
  @javax.annotation.Nullable
  public String getClockBadgeNumber() {
    return clockBadgeNumber;
  }

  public void setClockBadgeNumber(String clockBadgeNumber) {
    this.clockBadgeNumber = clockBadgeNumber;
  }


  public EmployeeDepartmentPosition costCenter1(String costCenter1) {
    this.costCenter1 = costCenter1;
    return this;
  }

  /**
   * Employer defined location, like *branch, division, department*, etc. Must match Company setup. &lt;br  /&gt;Max length: 10
   * @return costCenter1
   */
  @javax.annotation.Nullable
  public String getCostCenter1() {
    return costCenter1;
  }

  public void setCostCenter1(String costCenter1) {
    this.costCenter1 = costCenter1;
  }


  public EmployeeDepartmentPosition costCenter2(String costCenter2) {
    this.costCenter2 = costCenter2;
    return this;
  }

  /**
   * Employer defined location, like *branch, division, department*, etc. Must match Company setup. &lt;br  /&gt;Max length: 10
   * @return costCenter2
   */
  @javax.annotation.Nullable
  public String getCostCenter2() {
    return costCenter2;
  }

  public void setCostCenter2(String costCenter2) {
    this.costCenter2 = costCenter2;
  }


  public EmployeeDepartmentPosition costCenter3(String costCenter3) {
    this.costCenter3 = costCenter3;
    return this;
  }

  /**
   * Employer defined location, like *branch, division, department*, etc. Must match Company setup. &lt;br  /&gt;Max length: 10
   * @return costCenter3
   */
  @javax.annotation.Nullable
  public String getCostCenter3() {
    return costCenter3;
  }

  public void setCostCenter3(String costCenter3) {
    this.costCenter3 = costCenter3;
  }


  public EmployeeDepartmentPosition effectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
    return this;
  }

  /**
   * The date the position takes effect. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return effectiveDate
   */
  @javax.annotation.Nullable
  public String getEffectiveDate() {
    return effectiveDate;
  }

  public void setEffectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
  }


  public EmployeeDepartmentPosition employeeType(String employeeType) {
    this.employeeType = employeeType;
    return this;
  }

  /**
   * Employee current employment type. Common values *RFT (Regular Full Time), RPT (Regular Part Time), SNL (Seasonal), TFT (Temporary Full Time), TPT (Temporary Part Time)*. &lt;br  /&gt;Max length: 10
   * @return employeeType
   */
  @javax.annotation.Nullable
  public String getEmployeeType() {
    return employeeType;
  }

  public void setEmployeeType(String employeeType) {
    this.employeeType = employeeType;
  }


  public EmployeeDepartmentPosition equalEmploymentOpportunityClass(String equalEmploymentOpportunityClass) {
    this.equalEmploymentOpportunityClass = equalEmploymentOpportunityClass;
    return this;
  }

  /**
   * Values are configured in Company &gt; Setup &gt; HR &gt; EEO Classes.&lt;br  /&gt; Max length: 10
   * @return equalEmploymentOpportunityClass
   */
  @javax.annotation.Nullable
  public String getEqualEmploymentOpportunityClass() {
    return equalEmploymentOpportunityClass;
  }

  public void setEqualEmploymentOpportunityClass(String equalEmploymentOpportunityClass) {
    this.equalEmploymentOpportunityClass = equalEmploymentOpportunityClass;
  }


  public EmployeeDepartmentPosition isMinimumWageExempt(Boolean isMinimumWageExempt) {
    this.isMinimumWageExempt = isMinimumWageExempt;
    return this;
  }

  /**
   * Indicates if employee is exempt from minimum wage.
   * @return isMinimumWageExempt
   */
  @javax.annotation.Nullable
  public Boolean getIsMinimumWageExempt() {
    return isMinimumWageExempt;
  }

  public void setIsMinimumWageExempt(Boolean isMinimumWageExempt) {
    this.isMinimumWageExempt = isMinimumWageExempt;
  }


  public EmployeeDepartmentPosition isOvertimeExempt(Boolean isOvertimeExempt) {
    this.isOvertimeExempt = isOvertimeExempt;
    return this;
  }

  /**
   * Indicates if employee is exempt from overtime.
   * @return isOvertimeExempt
   */
  @javax.annotation.Nullable
  public Boolean getIsOvertimeExempt() {
    return isOvertimeExempt;
  }

  public void setIsOvertimeExempt(Boolean isOvertimeExempt) {
    this.isOvertimeExempt = isOvertimeExempt;
  }


  public EmployeeDepartmentPosition isSupervisorReviewer(Boolean isSupervisorReviewer) {
    this.isSupervisorReviewer = isSupervisorReviewer;
    return this;
  }

  /**
   * Indicates if employee is a supervisor or reviewer.
   * @return isSupervisorReviewer
   */
  @javax.annotation.Nullable
  public Boolean getIsSupervisorReviewer() {
    return isSupervisorReviewer;
  }

  public void setIsSupervisorReviewer(Boolean isSupervisorReviewer) {
    this.isSupervisorReviewer = isSupervisorReviewer;
  }


  public EmployeeDepartmentPosition isUnionDuesCollected(Boolean isUnionDuesCollected) {
    this.isUnionDuesCollected = isUnionDuesCollected;
    return this;
  }

  /**
   * Indicates if union dues are collected.
   * @return isUnionDuesCollected
   */
  @javax.annotation.Nullable
  public Boolean getIsUnionDuesCollected() {
    return isUnionDuesCollected;
  }

  public void setIsUnionDuesCollected(Boolean isUnionDuesCollected) {
    this.isUnionDuesCollected = isUnionDuesCollected;
  }


  public EmployeeDepartmentPosition isUnionInitiationCollected(Boolean isUnionInitiationCollected) {
    this.isUnionInitiationCollected = isUnionInitiationCollected;
    return this;
  }

  /**
   * Indicates if initiations fees are collected.
   * @return isUnionInitiationCollected
   */
  @javax.annotation.Nullable
  public Boolean getIsUnionInitiationCollected() {
    return isUnionInitiationCollected;
  }

  public void setIsUnionInitiationCollected(Boolean isUnionInitiationCollected) {
    this.isUnionInitiationCollected = isUnionInitiationCollected;
  }


  public EmployeeDepartmentPosition jobTitle(String jobTitle) {
    this.jobTitle = jobTitle;
    return this;
  }

  /**
   * Employee current job title. &lt;br  /&gt;Max length: 50
   * @return jobTitle
   */
  @javax.annotation.Nullable
  public String getJobTitle() {
    return jobTitle;
  }

  public void setJobTitle(String jobTitle) {
    this.jobTitle = jobTitle;
  }


  public EmployeeDepartmentPosition payGroup(String payGroup) {
    this.payGroup = payGroup;
    return this;
  }

  /**
   * Employee pay group. Must match Company setup. &lt;br  /&gt; Max length: 20
   * @return payGroup
   */
  @javax.annotation.Nullable
  public String getPayGroup() {
    return payGroup;
  }

  public void setPayGroup(String payGroup) {
    this.payGroup = payGroup;
  }


  public EmployeeDepartmentPosition positionCode(String positionCode) {
    this.positionCode = positionCode;
    return this;
  }

  /**
   * Employee position code. Must match Company setup.&lt;br  /&gt;Max length: 20
   * @return positionCode
   */
  @javax.annotation.Nullable
  public String getPositionCode() {
    return positionCode;
  }

  public void setPositionCode(String positionCode) {
    this.positionCode = positionCode;
  }


  public EmployeeDepartmentPosition reviewerCompanyNumber(String reviewerCompanyNumber) {
    this.reviewerCompanyNumber = reviewerCompanyNumber;
    return this;
  }

  /**
   * Company number of reviewer.&lt;br /&gt;Max length: 9
   * @return reviewerCompanyNumber
   */
  @javax.annotation.Nullable
  public String getReviewerCompanyNumber() {
    return reviewerCompanyNumber;
  }

  public void setReviewerCompanyNumber(String reviewerCompanyNumber) {
    this.reviewerCompanyNumber = reviewerCompanyNumber;
  }


  public EmployeeDepartmentPosition reviewerEmployeeId(String reviewerEmployeeId) {
    this.reviewerEmployeeId = reviewerEmployeeId;
    return this;
  }

  /**
   * Employee id of the reviewer.&lt;br /&gt;Max length: 10
   * @return reviewerEmployeeId
   */
  @javax.annotation.Nullable
  public String getReviewerEmployeeId() {
    return reviewerEmployeeId;
  }

  public void setReviewerEmployeeId(String reviewerEmployeeId) {
    this.reviewerEmployeeId = reviewerEmployeeId;
  }


  public EmployeeDepartmentPosition shift(String shift) {
    this.shift = shift;
    return this;
  }

  /**
   * Employee work shift.&lt;br  /&gt;Max length: 255
   * @return shift
   */
  @javax.annotation.Nullable
  public String getShift() {
    return shift;
  }

  public void setShift(String shift) {
    this.shift = shift;
  }


  public EmployeeDepartmentPosition supervisorCompanyNumber(String supervisorCompanyNumber) {
    this.supervisorCompanyNumber = supervisorCompanyNumber;
    return this;
  }

  /**
   * Supervisor&#39;s company number. Defaults to employee company number.&lt;br  /&gt;Max length: 9
   * @return supervisorCompanyNumber
   */
  @javax.annotation.Nullable
  public String getSupervisorCompanyNumber() {
    return supervisorCompanyNumber;
  }

  public void setSupervisorCompanyNumber(String supervisorCompanyNumber) {
    this.supervisorCompanyNumber = supervisorCompanyNumber;
  }


  public EmployeeDepartmentPosition supervisorEmployeeId(String supervisorEmployeeId) {
    this.supervisorEmployeeId = supervisorEmployeeId;
    return this;
  }

  /**
   * EmployeeId of the supervisor. &lt;br  /&gt;Max length: 10
   * @return supervisorEmployeeId
   */
  @javax.annotation.Nullable
  public String getSupervisorEmployeeId() {
    return supervisorEmployeeId;
  }

  public void setSupervisorEmployeeId(String supervisorEmployeeId) {
    this.supervisorEmployeeId = supervisorEmployeeId;
  }


  public EmployeeDepartmentPosition tipped(String tipped) {
    this.tipped = tipped;
    return this;
  }

  /**
   * Indicates if employee receives tips.
   * @return tipped
   */
  @javax.annotation.Nullable
  public String getTipped() {
    return tipped;
  }

  public void setTipped(String tipped) {
    this.tipped = tipped;
  }


  public EmployeeDepartmentPosition unionAffiliationDate(String unionAffiliationDate) {
    this.unionAffiliationDate = unionAffiliationDate;
    return this;
  }

  /**
   * Employee union affiliation effective date. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return unionAffiliationDate
   */
  @javax.annotation.Nullable
  public String getUnionAffiliationDate() {
    return unionAffiliationDate;
  }

  public void setUnionAffiliationDate(String unionAffiliationDate) {
    this.unionAffiliationDate = unionAffiliationDate;
  }


  public EmployeeDepartmentPosition unionCode(String unionCode) {
    this.unionCode = unionCode;
    return this;
  }

  /**
   * Employee union code. Must match Company setup. &lt;br  /&gt;Max length: 10
   * @return unionCode
   */
  @javax.annotation.Nullable
  public String getUnionCode() {
    return unionCode;
  }

  public void setUnionCode(String unionCode) {
    this.unionCode = unionCode;
  }


  public EmployeeDepartmentPosition unionPosition(String unionPosition) {
    this.unionPosition = unionPosition;
    return this;
  }

  /**
   * Employee union position. Must match Company setup. &lt;br  /&gt;Max length: 30
   * @return unionPosition
   */
  @javax.annotation.Nullable
  public String getUnionPosition() {
    return unionPosition;
  }

  public void setUnionPosition(String unionPosition) {
    this.unionPosition = unionPosition;
  }


  public EmployeeDepartmentPosition workersCompensation(String workersCompensation) {
    this.workersCompensation = workersCompensation;
    return this;
  }

  /**
   * Employee worker compensation code. Must match Company setup.&lt;br  /&gt; Max length: 10
   * @return workersCompensation
   */
  @javax.annotation.Nullable
  public String getWorkersCompensation() {
    return workersCompensation;
  }

  public void setWorkersCompensation(String workersCompensation) {
    this.workersCompensation = workersCompensation;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EmployeeDepartmentPosition employeeDepartmentPosition = (EmployeeDepartmentPosition) o;
    return Objects.equals(this.changeReason, employeeDepartmentPosition.changeReason) &&
        Objects.equals(this.clockBadgeNumber, employeeDepartmentPosition.clockBadgeNumber) &&
        Objects.equals(this.costCenter1, employeeDepartmentPosition.costCenter1) &&
        Objects.equals(this.costCenter2, employeeDepartmentPosition.costCenter2) &&
        Objects.equals(this.costCenter3, employeeDepartmentPosition.costCenter3) &&
        Objects.equals(this.effectiveDate, employeeDepartmentPosition.effectiveDate) &&
        Objects.equals(this.employeeType, employeeDepartmentPosition.employeeType) &&
        Objects.equals(this.equalEmploymentOpportunityClass, employeeDepartmentPosition.equalEmploymentOpportunityClass) &&
        Objects.equals(this.isMinimumWageExempt, employeeDepartmentPosition.isMinimumWageExempt) &&
        Objects.equals(this.isOvertimeExempt, employeeDepartmentPosition.isOvertimeExempt) &&
        Objects.equals(this.isSupervisorReviewer, employeeDepartmentPosition.isSupervisorReviewer) &&
        Objects.equals(this.isUnionDuesCollected, employeeDepartmentPosition.isUnionDuesCollected) &&
        Objects.equals(this.isUnionInitiationCollected, employeeDepartmentPosition.isUnionInitiationCollected) &&
        Objects.equals(this.jobTitle, employeeDepartmentPosition.jobTitle) &&
        Objects.equals(this.payGroup, employeeDepartmentPosition.payGroup) &&
        Objects.equals(this.positionCode, employeeDepartmentPosition.positionCode) &&
        Objects.equals(this.reviewerCompanyNumber, employeeDepartmentPosition.reviewerCompanyNumber) &&
        Objects.equals(this.reviewerEmployeeId, employeeDepartmentPosition.reviewerEmployeeId) &&
        Objects.equals(this.shift, employeeDepartmentPosition.shift) &&
        Objects.equals(this.supervisorCompanyNumber, employeeDepartmentPosition.supervisorCompanyNumber) &&
        Objects.equals(this.supervisorEmployeeId, employeeDepartmentPosition.supervisorEmployeeId) &&
        Objects.equals(this.tipped, employeeDepartmentPosition.tipped) &&
        Objects.equals(this.unionAffiliationDate, employeeDepartmentPosition.unionAffiliationDate) &&
        Objects.equals(this.unionCode, employeeDepartmentPosition.unionCode) &&
        Objects.equals(this.unionPosition, employeeDepartmentPosition.unionPosition) &&
        Objects.equals(this.workersCompensation, employeeDepartmentPosition.workersCompensation);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(changeReason, clockBadgeNumber, costCenter1, costCenter2, costCenter3, effectiveDate, employeeType, equalEmploymentOpportunityClass, isMinimumWageExempt, isOvertimeExempt, isSupervisorReviewer, isUnionDuesCollected, isUnionInitiationCollected, jobTitle, payGroup, positionCode, reviewerCompanyNumber, reviewerEmployeeId, shift, supervisorCompanyNumber, supervisorEmployeeId, tipped, unionAffiliationDate, unionCode, unionPosition, workersCompensation);
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
    sb.append("class EmployeeDepartmentPosition {\n");
    sb.append("    changeReason: ").append(toIndentedString(changeReason)).append("\n");
    sb.append("    clockBadgeNumber: ").append(toIndentedString(clockBadgeNumber)).append("\n");
    sb.append("    costCenter1: ").append(toIndentedString(costCenter1)).append("\n");
    sb.append("    costCenter2: ").append(toIndentedString(costCenter2)).append("\n");
    sb.append("    costCenter3: ").append(toIndentedString(costCenter3)).append("\n");
    sb.append("    effectiveDate: ").append(toIndentedString(effectiveDate)).append("\n");
    sb.append("    employeeType: ").append(toIndentedString(employeeType)).append("\n");
    sb.append("    equalEmploymentOpportunityClass: ").append(toIndentedString(equalEmploymentOpportunityClass)).append("\n");
    sb.append("    isMinimumWageExempt: ").append(toIndentedString(isMinimumWageExempt)).append("\n");
    sb.append("    isOvertimeExempt: ").append(toIndentedString(isOvertimeExempt)).append("\n");
    sb.append("    isSupervisorReviewer: ").append(toIndentedString(isSupervisorReviewer)).append("\n");
    sb.append("    isUnionDuesCollected: ").append(toIndentedString(isUnionDuesCollected)).append("\n");
    sb.append("    isUnionInitiationCollected: ").append(toIndentedString(isUnionInitiationCollected)).append("\n");
    sb.append("    jobTitle: ").append(toIndentedString(jobTitle)).append("\n");
    sb.append("    payGroup: ").append(toIndentedString(payGroup)).append("\n");
    sb.append("    positionCode: ").append(toIndentedString(positionCode)).append("\n");
    sb.append("    reviewerCompanyNumber: ").append(toIndentedString(reviewerCompanyNumber)).append("\n");
    sb.append("    reviewerEmployeeId: ").append(toIndentedString(reviewerEmployeeId)).append("\n");
    sb.append("    shift: ").append(toIndentedString(shift)).append("\n");
    sb.append("    supervisorCompanyNumber: ").append(toIndentedString(supervisorCompanyNumber)).append("\n");
    sb.append("    supervisorEmployeeId: ").append(toIndentedString(supervisorEmployeeId)).append("\n");
    sb.append("    tipped: ").append(toIndentedString(tipped)).append("\n");
    sb.append("    unionAffiliationDate: ").append(toIndentedString(unionAffiliationDate)).append("\n");
    sb.append("    unionCode: ").append(toIndentedString(unionCode)).append("\n");
    sb.append("    unionPosition: ").append(toIndentedString(unionPosition)).append("\n");
    sb.append("    workersCompensation: ").append(toIndentedString(workersCompensation)).append("\n");
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
    openapiFields.add("changeReason");
    openapiFields.add("clockBadgeNumber");
    openapiFields.add("costCenter1");
    openapiFields.add("costCenter2");
    openapiFields.add("costCenter3");
    openapiFields.add("effectiveDate");
    openapiFields.add("employeeType");
    openapiFields.add("equalEmploymentOpportunityClass");
    openapiFields.add("isMinimumWageExempt");
    openapiFields.add("isOvertimeExempt");
    openapiFields.add("isSupervisorReviewer");
    openapiFields.add("isUnionDuesCollected");
    openapiFields.add("isUnionInitiationCollected");
    openapiFields.add("jobTitle");
    openapiFields.add("payGroup");
    openapiFields.add("positionCode");
    openapiFields.add("reviewerCompanyNumber");
    openapiFields.add("reviewerEmployeeId");
    openapiFields.add("shift");
    openapiFields.add("supervisorCompanyNumber");
    openapiFields.add("supervisorEmployeeId");
    openapiFields.add("tipped");
    openapiFields.add("unionAffiliationDate");
    openapiFields.add("unionCode");
    openapiFields.add("unionPosition");
    openapiFields.add("workersCompensation");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EmployeeDepartmentPosition
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EmployeeDepartmentPosition.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EmployeeDepartmentPosition is not found in the empty JSON string", EmployeeDepartmentPosition.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EmployeeDepartmentPosition.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EmployeeDepartmentPosition` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("changeReason") != null && !jsonObj.get("changeReason").isJsonNull()) && !jsonObj.get("changeReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `changeReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("changeReason").toString()));
      }
      if ((jsonObj.get("clockBadgeNumber") != null && !jsonObj.get("clockBadgeNumber").isJsonNull()) && !jsonObj.get("clockBadgeNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clockBadgeNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clockBadgeNumber").toString()));
      }
      if ((jsonObj.get("costCenter1") != null && !jsonObj.get("costCenter1").isJsonNull()) && !jsonObj.get("costCenter1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `costCenter1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("costCenter1").toString()));
      }
      if ((jsonObj.get("costCenter2") != null && !jsonObj.get("costCenter2").isJsonNull()) && !jsonObj.get("costCenter2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `costCenter2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("costCenter2").toString()));
      }
      if ((jsonObj.get("costCenter3") != null && !jsonObj.get("costCenter3").isJsonNull()) && !jsonObj.get("costCenter3").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `costCenter3` to be a primitive type in the JSON string but got `%s`", jsonObj.get("costCenter3").toString()));
      }
      if ((jsonObj.get("effectiveDate") != null && !jsonObj.get("effectiveDate").isJsonNull()) && !jsonObj.get("effectiveDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `effectiveDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("effectiveDate").toString()));
      }
      if ((jsonObj.get("employeeType") != null && !jsonObj.get("employeeType").isJsonNull()) && !jsonObj.get("employeeType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employeeType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employeeType").toString()));
      }
      if ((jsonObj.get("equalEmploymentOpportunityClass") != null && !jsonObj.get("equalEmploymentOpportunityClass").isJsonNull()) && !jsonObj.get("equalEmploymentOpportunityClass").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `equalEmploymentOpportunityClass` to be a primitive type in the JSON string but got `%s`", jsonObj.get("equalEmploymentOpportunityClass").toString()));
      }
      if ((jsonObj.get("jobTitle") != null && !jsonObj.get("jobTitle").isJsonNull()) && !jsonObj.get("jobTitle").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `jobTitle` to be a primitive type in the JSON string but got `%s`", jsonObj.get("jobTitle").toString()));
      }
      if ((jsonObj.get("payGroup") != null && !jsonObj.get("payGroup").isJsonNull()) && !jsonObj.get("payGroup").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payGroup` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payGroup").toString()));
      }
      if ((jsonObj.get("positionCode") != null && !jsonObj.get("positionCode").isJsonNull()) && !jsonObj.get("positionCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `positionCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("positionCode").toString()));
      }
      if ((jsonObj.get("reviewerCompanyNumber") != null && !jsonObj.get("reviewerCompanyNumber").isJsonNull()) && !jsonObj.get("reviewerCompanyNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reviewerCompanyNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reviewerCompanyNumber").toString()));
      }
      if ((jsonObj.get("reviewerEmployeeId") != null && !jsonObj.get("reviewerEmployeeId").isJsonNull()) && !jsonObj.get("reviewerEmployeeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reviewerEmployeeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reviewerEmployeeId").toString()));
      }
      if ((jsonObj.get("shift") != null && !jsonObj.get("shift").isJsonNull()) && !jsonObj.get("shift").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shift` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shift").toString()));
      }
      if ((jsonObj.get("supervisorCompanyNumber") != null && !jsonObj.get("supervisorCompanyNumber").isJsonNull()) && !jsonObj.get("supervisorCompanyNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supervisorCompanyNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supervisorCompanyNumber").toString()));
      }
      if ((jsonObj.get("supervisorEmployeeId") != null && !jsonObj.get("supervisorEmployeeId").isJsonNull()) && !jsonObj.get("supervisorEmployeeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supervisorEmployeeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supervisorEmployeeId").toString()));
      }
      if ((jsonObj.get("tipped") != null && !jsonObj.get("tipped").isJsonNull()) && !jsonObj.get("tipped").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tipped` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tipped").toString()));
      }
      if ((jsonObj.get("unionAffiliationDate") != null && !jsonObj.get("unionAffiliationDate").isJsonNull()) && !jsonObj.get("unionAffiliationDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unionAffiliationDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unionAffiliationDate").toString()));
      }
      if ((jsonObj.get("unionCode") != null && !jsonObj.get("unionCode").isJsonNull()) && !jsonObj.get("unionCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unionCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unionCode").toString()));
      }
      if ((jsonObj.get("unionPosition") != null && !jsonObj.get("unionPosition").isJsonNull()) && !jsonObj.get("unionPosition").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unionPosition` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unionPosition").toString()));
      }
      if ((jsonObj.get("workersCompensation") != null && !jsonObj.get("workersCompensation").isJsonNull()) && !jsonObj.get("workersCompensation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workersCompensation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workersCompensation").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EmployeeDepartmentPosition.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EmployeeDepartmentPosition' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EmployeeDepartmentPosition> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EmployeeDepartmentPosition.class));

       return (TypeAdapter<T>) new TypeAdapter<EmployeeDepartmentPosition>() {
           @Override
           public void write(JsonWriter out, EmployeeDepartmentPosition value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EmployeeDepartmentPosition read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EmployeeDepartmentPosition given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EmployeeDepartmentPosition
   * @throws IOException if the JSON string is invalid with respect to EmployeeDepartmentPosition
   */
  public static EmployeeDepartmentPosition fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EmployeeDepartmentPosition.class);
  }

  /**
   * Convert an instance of EmployeeDepartmentPosition to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

