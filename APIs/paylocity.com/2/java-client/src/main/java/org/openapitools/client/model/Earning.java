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
 * The employee earning model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Earning {
  public static final String SERIALIZED_NAME_AGENCY = "agency";
  @SerializedName(SERIALIZED_NAME_AGENCY)
  private String agency;

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_ANNUAL_MAXIMUM = "annualMaximum";
  @SerializedName(SERIALIZED_NAME_ANNUAL_MAXIMUM)
  private BigDecimal annualMaximum;

  public static final String SERIALIZED_NAME_CALCULATION_CODE = "calculationCode";
  @SerializedName(SERIALIZED_NAME_CALCULATION_CODE)
  private String calculationCode;

  public static final String SERIALIZED_NAME_COST_CENTER1 = "costCenter1";
  @SerializedName(SERIALIZED_NAME_COST_CENTER1)
  private String costCenter1;

  public static final String SERIALIZED_NAME_COST_CENTER2 = "costCenter2";
  @SerializedName(SERIALIZED_NAME_COST_CENTER2)
  private String costCenter2;

  public static final String SERIALIZED_NAME_COST_CENTER3 = "costCenter3";
  @SerializedName(SERIALIZED_NAME_COST_CENTER3)
  private String costCenter3;

  public static final String SERIALIZED_NAME_EARNING_CODE = "earningCode";
  @SerializedName(SERIALIZED_NAME_EARNING_CODE)
  private String earningCode;

  public static final String SERIALIZED_NAME_EFFECTIVE_DATE = "effectiveDate";
  @SerializedName(SERIALIZED_NAME_EFFECTIVE_DATE)
  private String effectiveDate;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private String endDate;

  public static final String SERIALIZED_NAME_FREQUENCY = "frequency";
  @SerializedName(SERIALIZED_NAME_FREQUENCY)
  private String frequency;

  public static final String SERIALIZED_NAME_GOAL = "goal";
  @SerializedName(SERIALIZED_NAME_GOAL)
  private BigDecimal goal;

  public static final String SERIALIZED_NAME_HOURS_OR_UNITS = "hoursOrUnits";
  @SerializedName(SERIALIZED_NAME_HOURS_OR_UNITS)
  private BigDecimal hoursOrUnits;

  public static final String SERIALIZED_NAME_IS_SELF_INSURED = "isSelfInsured";
  @SerializedName(SERIALIZED_NAME_IS_SELF_INSURED)
  private Boolean isSelfInsured;

  public static final String SERIALIZED_NAME_JOB_CODE = "jobCode";
  @SerializedName(SERIALIZED_NAME_JOB_CODE)
  private String jobCode;

  public static final String SERIALIZED_NAME_MISCELLANEOUS_INFO = "miscellaneousInfo";
  @SerializedName(SERIALIZED_NAME_MISCELLANEOUS_INFO)
  private String miscellaneousInfo;

  public static final String SERIALIZED_NAME_PAID_TOWARDS_GOAL = "paidTowardsGoal";
  @SerializedName(SERIALIZED_NAME_PAID_TOWARDS_GOAL)
  private BigDecimal paidTowardsGoal;

  public static final String SERIALIZED_NAME_PAY_PERIOD_MAXIMUM = "payPeriodMaximum";
  @SerializedName(SERIALIZED_NAME_PAY_PERIOD_MAXIMUM)
  private BigDecimal payPeriodMaximum;

  public static final String SERIALIZED_NAME_PAY_PERIOD_MINIMUM = "payPeriodMinimum";
  @SerializedName(SERIALIZED_NAME_PAY_PERIOD_MINIMUM)
  private BigDecimal payPeriodMinimum;

  public static final String SERIALIZED_NAME_RATE = "rate";
  @SerializedName(SERIALIZED_NAME_RATE)
  private BigDecimal rate;

  public static final String SERIALIZED_NAME_RATE_CODE = "rateCode";
  @SerializedName(SERIALIZED_NAME_RATE_CODE)
  private String rateCode;

  public static final String SERIALIZED_NAME_START_DATE = "startDate";
  @SerializedName(SERIALIZED_NAME_START_DATE)
  private String startDate;

  public Earning() {
  }

  public Earning agency(String agency) {
    this.agency = agency;
    return this;
  }

  /**
   * Third-party agency associated with earning. Must match Company setup.&lt;br  /&gt;Max length: 10
   * @return agency
   */
  @javax.annotation.Nullable
  public String getAgency() {
    return agency;
  }

  public void setAgency(String agency) {
    this.agency = agency;
  }


  public Earning amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Value that matches CalculationCode to add to gross wages. For percentage (%), enter whole number (10 &#x3D; 10%).  &lt;br  /&gt;Decimal(12,2)
   * @return amount
   */
  @javax.annotation.Nullable
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public Earning annualMaximum(BigDecimal annualMaximum) {
    this.annualMaximum = annualMaximum;
    return this;
  }

  /**
   * Year to Date dollar amount not to be exceeded for an earning in the calendar year. Used only with company driven maximums. &lt;br  /&gt;Decimal(12,2)
   * @return annualMaximum
   */
  @javax.annotation.Nullable
  public BigDecimal getAnnualMaximum() {
    return annualMaximum;
  }

  public void setAnnualMaximum(BigDecimal annualMaximum) {
    this.annualMaximum = annualMaximum;
  }


  public Earning calculationCode(String calculationCode) {
    this.calculationCode = calculationCode;
    return this;
  }

  /**
   * Defines how earnings are calculated. Common values are *% (percentage of gross), flat (flat dollar amount)*. Defaulted to the Company setup calcCode for earning. &lt;br  /&gt;Max length: 20
   * @return calculationCode
   */
  @javax.annotation.Nullable
  public String getCalculationCode() {
    return calculationCode;
  }

  public void setCalculationCode(String calculationCode) {
    this.calculationCode = calculationCode;
  }


  public Earning costCenter1(String costCenter1) {
    this.costCenter1 = costCenter1;
    return this;
  }

  /**
   * Cost Center associated with earning. Must match Company setup.&lt;br  /&gt; Max length: 10
   * @return costCenter1
   */
  @javax.annotation.Nullable
  public String getCostCenter1() {
    return costCenter1;
  }

  public void setCostCenter1(String costCenter1) {
    this.costCenter1 = costCenter1;
  }


  public Earning costCenter2(String costCenter2) {
    this.costCenter2 = costCenter2;
    return this;
  }

  /**
   * Cost Center associated with earning. Must match Company setup.&lt;br  /&gt; Max length: 10
   * @return costCenter2
   */
  @javax.annotation.Nullable
  public String getCostCenter2() {
    return costCenter2;
  }

  public void setCostCenter2(String costCenter2) {
    this.costCenter2 = costCenter2;
  }


  public Earning costCenter3(String costCenter3) {
    this.costCenter3 = costCenter3;
    return this;
  }

  /**
   * Cost Center associated with earning. Must match Company setup.&lt;br  /&gt; Max length: 10
   * @return costCenter3
   */
  @javax.annotation.Nullable
  public String getCostCenter3() {
    return costCenter3;
  }

  public void setCostCenter3(String costCenter3) {
    this.costCenter3 = costCenter3;
  }


  public Earning earningCode(String earningCode) {
    this.earningCode = earningCode;
    return this;
  }

  /**
   * Earning code. Must match Company setup. &lt;br  /&gt;Max length: 10
   * @return earningCode
   */
  @javax.annotation.Nullable
  public String getEarningCode() {
    return earningCode;
  }

  public void setEarningCode(String earningCode) {
    this.earningCode = earningCode;
  }


  public Earning effectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
    return this;
  }

  /**
   * Date earning is active. Defaulted to run date or check date based on Company setup. Common formats are MM-DD-CCYY, CCYY-MM-DD.
   * @return effectiveDate
   */
  @javax.annotation.Nullable
  public String getEffectiveDate() {
    return effectiveDate;
  }

  public void setEffectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
  }


  public Earning endDate(String endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * Stop date of an earning. Common formats are MM-DD-CCYY, CCYY-MM-DD.
   * @return endDate
   */
  @javax.annotation.Nullable
  public String getEndDate() {
    return endDate;
  }

  public void setEndDate(String endDate) {
    this.endDate = endDate;
  }


  public Earning frequency(String frequency) {
    this.frequency = frequency;
    return this;
  }

  /**
   * Needed if earning is applied differently from the payroll frequency (one time earning for example).&lt;br  /&gt; Max length: 5
   * @return frequency
   */
  @javax.annotation.Nullable
  public String getFrequency() {
    return frequency;
  }

  public void setFrequency(String frequency) {
    this.frequency = frequency;
  }


  public Earning goal(BigDecimal goal) {
    this.goal = goal;
    return this;
  }

  /**
   * Dollar amount. The employee earning will stop when the goal amount is reached.&lt;br  /&gt; Decimal(12,2)
   * @return goal
   */
  @javax.annotation.Nullable
  public BigDecimal getGoal() {
    return goal;
  }

  public void setGoal(BigDecimal goal) {
    this.goal = goal;
  }


  public Earning hoursOrUnits(BigDecimal hoursOrUnits) {
    this.hoursOrUnits = hoursOrUnits;
    return this;
  }

  /**
   * The value is used in conjunction with the Rate field. When entering Group Term Life Insurance (GTL), it should contain the full amount of the group term life insurance policy. &lt;br  /&gt; Decimal(12,2)
   * @return hoursOrUnits
   */
  @javax.annotation.Nullable
  public BigDecimal getHoursOrUnits() {
    return hoursOrUnits;
  }

  public void setHoursOrUnits(BigDecimal hoursOrUnits) {
    this.hoursOrUnits = hoursOrUnits;
  }


  public Earning isSelfInsured(Boolean isSelfInsured) {
    this.isSelfInsured = isSelfInsured;
    return this;
  }

  /**
   * Used for ACA. If not entered, defaulted to Company earning setup.
   * @return isSelfInsured
   */
  @javax.annotation.Nullable
  public Boolean getIsSelfInsured() {
    return isSelfInsured;
  }

  public void setIsSelfInsured(Boolean isSelfInsured) {
    this.isSelfInsured = isSelfInsured;
  }


  public Earning jobCode(String jobCode) {
    this.jobCode = jobCode;
    return this;
  }

  /**
   * Job code associated with earnings. Must match Company setup.&lt;br  /&gt; Max length: 20
   * @return jobCode
   */
  @javax.annotation.Nullable
  public String getJobCode() {
    return jobCode;
  }

  public void setJobCode(String jobCode) {
    this.jobCode = jobCode;
  }


  public Earning miscellaneousInfo(String miscellaneousInfo) {
    this.miscellaneousInfo = miscellaneousInfo;
    return this;
  }

  /**
   * Information to print on the check stub if agency is set up for this earning. &lt;br  /&gt;Max length: 50
   * @return miscellaneousInfo
   */
  @javax.annotation.Nullable
  public String getMiscellaneousInfo() {
    return miscellaneousInfo;
  }

  public void setMiscellaneousInfo(String miscellaneousInfo) {
    this.miscellaneousInfo = miscellaneousInfo;
  }


  public Earning paidTowardsGoal(BigDecimal paidTowardsGoal) {
    this.paidTowardsGoal = paidTowardsGoal;
    return this;
  }

  /**
   * Amount already paid to employee toward goal. &lt;br  /&gt; Decimal(12,2)
   * @return paidTowardsGoal
   */
  @javax.annotation.Nullable
  public BigDecimal getPaidTowardsGoal() {
    return paidTowardsGoal;
  }

  public void setPaidTowardsGoal(BigDecimal paidTowardsGoal) {
    this.paidTowardsGoal = paidTowardsGoal;
  }


  public Earning payPeriodMaximum(BigDecimal payPeriodMaximum) {
    this.payPeriodMaximum = payPeriodMaximum;
    return this;
  }

  /**
   * Maximum amount of the earning on a single paycheck. &lt;br  /&gt; Decimal(12,2)
   * @return payPeriodMaximum
   */
  @javax.annotation.Nullable
  public BigDecimal getPayPeriodMaximum() {
    return payPeriodMaximum;
  }

  public void setPayPeriodMaximum(BigDecimal payPeriodMaximum) {
    this.payPeriodMaximum = payPeriodMaximum;
  }


  public Earning payPeriodMinimum(BigDecimal payPeriodMinimum) {
    this.payPeriodMinimum = payPeriodMinimum;
    return this;
  }

  /**
   * Minimum amount of the earning on a single paycheck. &lt;br  /&gt; Decimal(12,2)
   * @return payPeriodMinimum
   */
  @javax.annotation.Nullable
  public BigDecimal getPayPeriodMinimum() {
    return payPeriodMinimum;
  }

  public void setPayPeriodMinimum(BigDecimal payPeriodMinimum) {
    this.payPeriodMinimum = payPeriodMinimum;
  }


  public Earning rate(BigDecimal rate) {
    this.rate = rate;
    return this;
  }

  /**
   * Rate is used in conjunction with the hoursOrUnits field. &lt;br  /&gt; Decimal(12,2)
   * @return rate
   */
  @javax.annotation.Nullable
  public BigDecimal getRate() {
    return rate;
  }

  public void setRate(BigDecimal rate) {
    this.rate = rate;
  }


  public Earning rateCode(String rateCode) {
    this.rateCode = rateCode;
    return this;
  }

  /**
   * Rate Code applies to additional pay rates entered for an employee. Must match Company setup. &lt;br  /&gt; Max length: 10
   * @return rateCode
   */
  @javax.annotation.Nullable
  public String getRateCode() {
    return rateCode;
  }

  public void setRateCode(String rateCode) {
    this.rateCode = rateCode;
  }


  public Earning startDate(String startDate) {
    this.startDate = startDate;
    return this;
  }

  /**
   * Start date of an earning based on payroll calendar. Common formats are MM-DD-CCYY, CCYY-MM-DD.
   * @return startDate
   */
  @javax.annotation.Nullable
  public String getStartDate() {
    return startDate;
  }

  public void setStartDate(String startDate) {
    this.startDate = startDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Earning earning = (Earning) o;
    return Objects.equals(this.agency, earning.agency) &&
        Objects.equals(this.amount, earning.amount) &&
        Objects.equals(this.annualMaximum, earning.annualMaximum) &&
        Objects.equals(this.calculationCode, earning.calculationCode) &&
        Objects.equals(this.costCenter1, earning.costCenter1) &&
        Objects.equals(this.costCenter2, earning.costCenter2) &&
        Objects.equals(this.costCenter3, earning.costCenter3) &&
        Objects.equals(this.earningCode, earning.earningCode) &&
        Objects.equals(this.effectiveDate, earning.effectiveDate) &&
        Objects.equals(this.endDate, earning.endDate) &&
        Objects.equals(this.frequency, earning.frequency) &&
        Objects.equals(this.goal, earning.goal) &&
        Objects.equals(this.hoursOrUnits, earning.hoursOrUnits) &&
        Objects.equals(this.isSelfInsured, earning.isSelfInsured) &&
        Objects.equals(this.jobCode, earning.jobCode) &&
        Objects.equals(this.miscellaneousInfo, earning.miscellaneousInfo) &&
        Objects.equals(this.paidTowardsGoal, earning.paidTowardsGoal) &&
        Objects.equals(this.payPeriodMaximum, earning.payPeriodMaximum) &&
        Objects.equals(this.payPeriodMinimum, earning.payPeriodMinimum) &&
        Objects.equals(this.rate, earning.rate) &&
        Objects.equals(this.rateCode, earning.rateCode) &&
        Objects.equals(this.startDate, earning.startDate);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(agency, amount, annualMaximum, calculationCode, costCenter1, costCenter2, costCenter3, earningCode, effectiveDate, endDate, frequency, goal, hoursOrUnits, isSelfInsured, jobCode, miscellaneousInfo, paidTowardsGoal, payPeriodMaximum, payPeriodMinimum, rate, rateCode, startDate);
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
    sb.append("class Earning {\n");
    sb.append("    agency: ").append(toIndentedString(agency)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    annualMaximum: ").append(toIndentedString(annualMaximum)).append("\n");
    sb.append("    calculationCode: ").append(toIndentedString(calculationCode)).append("\n");
    sb.append("    costCenter1: ").append(toIndentedString(costCenter1)).append("\n");
    sb.append("    costCenter2: ").append(toIndentedString(costCenter2)).append("\n");
    sb.append("    costCenter3: ").append(toIndentedString(costCenter3)).append("\n");
    sb.append("    earningCode: ").append(toIndentedString(earningCode)).append("\n");
    sb.append("    effectiveDate: ").append(toIndentedString(effectiveDate)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    frequency: ").append(toIndentedString(frequency)).append("\n");
    sb.append("    goal: ").append(toIndentedString(goal)).append("\n");
    sb.append("    hoursOrUnits: ").append(toIndentedString(hoursOrUnits)).append("\n");
    sb.append("    isSelfInsured: ").append(toIndentedString(isSelfInsured)).append("\n");
    sb.append("    jobCode: ").append(toIndentedString(jobCode)).append("\n");
    sb.append("    miscellaneousInfo: ").append(toIndentedString(miscellaneousInfo)).append("\n");
    sb.append("    paidTowardsGoal: ").append(toIndentedString(paidTowardsGoal)).append("\n");
    sb.append("    payPeriodMaximum: ").append(toIndentedString(payPeriodMaximum)).append("\n");
    sb.append("    payPeriodMinimum: ").append(toIndentedString(payPeriodMinimum)).append("\n");
    sb.append("    rate: ").append(toIndentedString(rate)).append("\n");
    sb.append("    rateCode: ").append(toIndentedString(rateCode)).append("\n");
    sb.append("    startDate: ").append(toIndentedString(startDate)).append("\n");
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
    openapiFields.add("agency");
    openapiFields.add("amount");
    openapiFields.add("annualMaximum");
    openapiFields.add("calculationCode");
    openapiFields.add("costCenter1");
    openapiFields.add("costCenter2");
    openapiFields.add("costCenter3");
    openapiFields.add("earningCode");
    openapiFields.add("effectiveDate");
    openapiFields.add("endDate");
    openapiFields.add("frequency");
    openapiFields.add("goal");
    openapiFields.add("hoursOrUnits");
    openapiFields.add("isSelfInsured");
    openapiFields.add("jobCode");
    openapiFields.add("miscellaneousInfo");
    openapiFields.add("paidTowardsGoal");
    openapiFields.add("payPeriodMaximum");
    openapiFields.add("payPeriodMinimum");
    openapiFields.add("rate");
    openapiFields.add("rateCode");
    openapiFields.add("startDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("earningCode");
    openapiRequiredFields.add("startDate");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Earning
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Earning.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Earning is not found in the empty JSON string", Earning.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Earning.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Earning` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Earning.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("agency") != null && !jsonObj.get("agency").isJsonNull()) && !jsonObj.get("agency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `agency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("agency").toString()));
      }
      if ((jsonObj.get("calculationCode") != null && !jsonObj.get("calculationCode").isJsonNull()) && !jsonObj.get("calculationCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `calculationCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("calculationCode").toString()));
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
      if ((jsonObj.get("earningCode") != null && !jsonObj.get("earningCode").isJsonNull()) && !jsonObj.get("earningCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `earningCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("earningCode").toString()));
      }
      if ((jsonObj.get("effectiveDate") != null && !jsonObj.get("effectiveDate").isJsonNull()) && !jsonObj.get("effectiveDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `effectiveDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("effectiveDate").toString()));
      }
      if ((jsonObj.get("endDate") != null && !jsonObj.get("endDate").isJsonNull()) && !jsonObj.get("endDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endDate").toString()));
      }
      if ((jsonObj.get("frequency") != null && !jsonObj.get("frequency").isJsonNull()) && !jsonObj.get("frequency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `frequency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("frequency").toString()));
      }
      if ((jsonObj.get("jobCode") != null && !jsonObj.get("jobCode").isJsonNull()) && !jsonObj.get("jobCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `jobCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("jobCode").toString()));
      }
      if ((jsonObj.get("miscellaneousInfo") != null && !jsonObj.get("miscellaneousInfo").isJsonNull()) && !jsonObj.get("miscellaneousInfo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `miscellaneousInfo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("miscellaneousInfo").toString()));
      }
      if ((jsonObj.get("rateCode") != null && !jsonObj.get("rateCode").isJsonNull()) && !jsonObj.get("rateCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rateCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rateCode").toString()));
      }
      if ((jsonObj.get("startDate") != null && !jsonObj.get("startDate").isJsonNull()) && !jsonObj.get("startDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `startDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("startDate").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Earning.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Earning' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Earning> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Earning.class));

       return (TypeAdapter<T>) new TypeAdapter<Earning>() {
           @Override
           public void write(JsonWriter out, Earning value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Earning read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Earning given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Earning
   * @throws IOException if the JSON string is invalid with respect to Earning
   */
  public static Earning fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Earning.class);
  }

  /**
   * Convert an instance of Earning to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

