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
 * The pay statement summary model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PayStatementSummary {
  public static final String SERIALIZED_NAME_AUTO_PAY = "autoPay";
  @SerializedName(SERIALIZED_NAME_AUTO_PAY)
  private Boolean autoPay;

  public static final String SERIALIZED_NAME_BEGIN_DATE = "beginDate";
  @SerializedName(SERIALIZED_NAME_BEGIN_DATE)
  private String beginDate;

  public static final String SERIALIZED_NAME_CHECK_DATE = "checkDate";
  @SerializedName(SERIALIZED_NAME_CHECK_DATE)
  private String checkDate;

  public static final String SERIALIZED_NAME_CHECK_NUMBER = "checkNumber";
  @SerializedName(SERIALIZED_NAME_CHECK_NUMBER)
  private Integer checkNumber;

  public static final String SERIALIZED_NAME_DIRECT_DEPOSIT_AMOUNT = "directDepositAmount";
  @SerializedName(SERIALIZED_NAME_DIRECT_DEPOSIT_AMOUNT)
  private BigDecimal directDepositAmount;

  public static final String SERIALIZED_NAME_END_DATE = "endDate";
  @SerializedName(SERIALIZED_NAME_END_DATE)
  private String endDate;

  public static final String SERIALIZED_NAME_GROSS_PAY = "grossPay";
  @SerializedName(SERIALIZED_NAME_GROSS_PAY)
  private BigDecimal grossPay;

  public static final String SERIALIZED_NAME_HOURS = "hours";
  @SerializedName(SERIALIZED_NAME_HOURS)
  private BigDecimal hours;

  public static final String SERIALIZED_NAME_NET_CHECK = "netCheck";
  @SerializedName(SERIALIZED_NAME_NET_CHECK)
  private BigDecimal netCheck;

  public static final String SERIALIZED_NAME_NET_PAY = "netPay";
  @SerializedName(SERIALIZED_NAME_NET_PAY)
  private BigDecimal netPay;

  public static final String SERIALIZED_NAME_OVERTIME_DOLLARS = "overtimeDollars";
  @SerializedName(SERIALIZED_NAME_OVERTIME_DOLLARS)
  private BigDecimal overtimeDollars;

  public static final String SERIALIZED_NAME_OVERTIME_HOURS = "overtimeHours";
  @SerializedName(SERIALIZED_NAME_OVERTIME_HOURS)
  private BigDecimal overtimeHours;

  public static final String SERIALIZED_NAME_PROCESS = "process";
  @SerializedName(SERIALIZED_NAME_PROCESS)
  private Integer process;

  public static final String SERIALIZED_NAME_REGULAR_DOLLARS = "regularDollars";
  @SerializedName(SERIALIZED_NAME_REGULAR_DOLLARS)
  private BigDecimal regularDollars;

  public static final String SERIALIZED_NAME_REGULAR_HOURS = "regularHours";
  @SerializedName(SERIALIZED_NAME_REGULAR_HOURS)
  private BigDecimal regularHours;

  public static final String SERIALIZED_NAME_TRANSACTION_NUMBER = "transactionNumber";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_NUMBER)
  private Integer transactionNumber;

  public static final String SERIALIZED_NAME_VOUCHER_NUMBER = "voucherNumber";
  @SerializedName(SERIALIZED_NAME_VOUCHER_NUMBER)
  private Integer voucherNumber;

  public static final String SERIALIZED_NAME_WORKERS_COMP_CODE = "workersCompCode";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_CODE)
  private String workersCompCode;

  public static final String SERIALIZED_NAME_YEAR = "year";
  @SerializedName(SERIALIZED_NAME_YEAR)
  private Integer year;

  public PayStatementSummary() {
  }

  public PayStatementSummary autoPay(Boolean autoPay) {
    this.autoPay = autoPay;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return autoPay
   */
  @javax.annotation.Nullable
  public Boolean getAutoPay() {
    return autoPay;
  }

  public void setAutoPay(Boolean autoPay) {
    this.autoPay = autoPay;
  }


  public PayStatementSummary beginDate(String beginDate) {
    this.beginDate = beginDate;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return beginDate
   */
  @javax.annotation.Nullable
  public String getBeginDate() {
    return beginDate;
  }

  public void setBeginDate(String beginDate) {
    this.beginDate = beginDate;
  }


  public PayStatementSummary checkDate(String checkDate) {
    this.checkDate = checkDate;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return checkDate
   */
  @javax.annotation.Nullable
  public String getCheckDate() {
    return checkDate;
  }

  public void setCheckDate(String checkDate) {
    this.checkDate = checkDate;
  }


  public PayStatementSummary checkNumber(Integer checkNumber) {
    this.checkNumber = checkNumber;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return checkNumber
   */
  @javax.annotation.Nullable
  public Integer getCheckNumber() {
    return checkNumber;
  }

  public void setCheckNumber(Integer checkNumber) {
    this.checkNumber = checkNumber;
  }


  public PayStatementSummary directDepositAmount(BigDecimal directDepositAmount) {
    this.directDepositAmount = directDepositAmount;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return directDepositAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getDirectDepositAmount() {
    return directDepositAmount;
  }

  public void setDirectDepositAmount(BigDecimal directDepositAmount) {
    this.directDepositAmount = directDepositAmount;
  }


  public PayStatementSummary endDate(String endDate) {
    this.endDate = endDate;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return endDate
   */
  @javax.annotation.Nullable
  public String getEndDate() {
    return endDate;
  }

  public void setEndDate(String endDate) {
    this.endDate = endDate;
  }


  public PayStatementSummary grossPay(BigDecimal grossPay) {
    this.grossPay = grossPay;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return grossPay
   */
  @javax.annotation.Nullable
  public BigDecimal getGrossPay() {
    return grossPay;
  }

  public void setGrossPay(BigDecimal grossPay) {
    this.grossPay = grossPay;
  }


  public PayStatementSummary hours(BigDecimal hours) {
    this.hours = hours;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return hours
   */
  @javax.annotation.Nullable
  public BigDecimal getHours() {
    return hours;
  }

  public void setHours(BigDecimal hours) {
    this.hours = hours;
  }


  public PayStatementSummary netCheck(BigDecimal netCheck) {
    this.netCheck = netCheck;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return netCheck
   */
  @javax.annotation.Nullable
  public BigDecimal getNetCheck() {
    return netCheck;
  }

  public void setNetCheck(BigDecimal netCheck) {
    this.netCheck = netCheck;
  }


  public PayStatementSummary netPay(BigDecimal netPay) {
    this.netPay = netPay;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return netPay
   */
  @javax.annotation.Nullable
  public BigDecimal getNetPay() {
    return netPay;
  }

  public void setNetPay(BigDecimal netPay) {
    this.netPay = netPay;
  }


  public PayStatementSummary overtimeDollars(BigDecimal overtimeDollars) {
    this.overtimeDollars = overtimeDollars;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return overtimeDollars
   */
  @javax.annotation.Nullable
  public BigDecimal getOvertimeDollars() {
    return overtimeDollars;
  }

  public void setOvertimeDollars(BigDecimal overtimeDollars) {
    this.overtimeDollars = overtimeDollars;
  }


  public PayStatementSummary overtimeHours(BigDecimal overtimeHours) {
    this.overtimeHours = overtimeHours;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return overtimeHours
   */
  @javax.annotation.Nullable
  public BigDecimal getOvertimeHours() {
    return overtimeHours;
  }

  public void setOvertimeHours(BigDecimal overtimeHours) {
    this.overtimeHours = overtimeHours;
  }


  public PayStatementSummary process(Integer process) {
    this.process = process;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return process
   */
  @javax.annotation.Nullable
  public Integer getProcess() {
    return process;
  }

  public void setProcess(Integer process) {
    this.process = process;
  }


  public PayStatementSummary regularDollars(BigDecimal regularDollars) {
    this.regularDollars = regularDollars;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return regularDollars
   */
  @javax.annotation.Nullable
  public BigDecimal getRegularDollars() {
    return regularDollars;
  }

  public void setRegularDollars(BigDecimal regularDollars) {
    this.regularDollars = regularDollars;
  }


  public PayStatementSummary regularHours(BigDecimal regularHours) {
    this.regularHours = regularHours;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return regularHours
   */
  @javax.annotation.Nullable
  public BigDecimal getRegularHours() {
    return regularHours;
  }

  public void setRegularHours(BigDecimal regularHours) {
    this.regularHours = regularHours;
  }


  public PayStatementSummary transactionNumber(Integer transactionNumber) {
    this.transactionNumber = transactionNumber;
    return this;
  }

  /**
   * &lt;br /&gt;
   * @return transactionNumber
   */
  @javax.annotation.Nullable
  public Integer getTransactionNumber() {
    return transactionNumber;
  }

  public void setTransactionNumber(Integer transactionNumber) {
    this.transactionNumber = transactionNumber;
  }


  public PayStatementSummary voucherNumber(Integer voucherNumber) {
    this.voucherNumber = voucherNumber;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return voucherNumber
   */
  @javax.annotation.Nullable
  public Integer getVoucherNumber() {
    return voucherNumber;
  }

  public void setVoucherNumber(Integer voucherNumber) {
    this.voucherNumber = voucherNumber;
  }


  public PayStatementSummary workersCompCode(String workersCompCode) {
    this.workersCompCode = workersCompCode;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return workersCompCode
   */
  @javax.annotation.Nullable
  public String getWorkersCompCode() {
    return workersCompCode;
  }

  public void setWorkersCompCode(String workersCompCode) {
    this.workersCompCode = workersCompCode;
  }


  public PayStatementSummary year(Integer year) {
    this.year = year;
    return this;
  }

  /**
   * .&lt;br /&gt;
   * @return year
   */
  @javax.annotation.Nullable
  public Integer getYear() {
    return year;
  }

  public void setYear(Integer year) {
    this.year = year;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PayStatementSummary payStatementSummary = (PayStatementSummary) o;
    return Objects.equals(this.autoPay, payStatementSummary.autoPay) &&
        Objects.equals(this.beginDate, payStatementSummary.beginDate) &&
        Objects.equals(this.checkDate, payStatementSummary.checkDate) &&
        Objects.equals(this.checkNumber, payStatementSummary.checkNumber) &&
        Objects.equals(this.directDepositAmount, payStatementSummary.directDepositAmount) &&
        Objects.equals(this.endDate, payStatementSummary.endDate) &&
        Objects.equals(this.grossPay, payStatementSummary.grossPay) &&
        Objects.equals(this.hours, payStatementSummary.hours) &&
        Objects.equals(this.netCheck, payStatementSummary.netCheck) &&
        Objects.equals(this.netPay, payStatementSummary.netPay) &&
        Objects.equals(this.overtimeDollars, payStatementSummary.overtimeDollars) &&
        Objects.equals(this.overtimeHours, payStatementSummary.overtimeHours) &&
        Objects.equals(this.process, payStatementSummary.process) &&
        Objects.equals(this.regularDollars, payStatementSummary.regularDollars) &&
        Objects.equals(this.regularHours, payStatementSummary.regularHours) &&
        Objects.equals(this.transactionNumber, payStatementSummary.transactionNumber) &&
        Objects.equals(this.voucherNumber, payStatementSummary.voucherNumber) &&
        Objects.equals(this.workersCompCode, payStatementSummary.workersCompCode) &&
        Objects.equals(this.year, payStatementSummary.year);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoPay, beginDate, checkDate, checkNumber, directDepositAmount, endDate, grossPay, hours, netCheck, netPay, overtimeDollars, overtimeHours, process, regularDollars, regularHours, transactionNumber, voucherNumber, workersCompCode, year);
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
    sb.append("class PayStatementSummary {\n");
    sb.append("    autoPay: ").append(toIndentedString(autoPay)).append("\n");
    sb.append("    beginDate: ").append(toIndentedString(beginDate)).append("\n");
    sb.append("    checkDate: ").append(toIndentedString(checkDate)).append("\n");
    sb.append("    checkNumber: ").append(toIndentedString(checkNumber)).append("\n");
    sb.append("    directDepositAmount: ").append(toIndentedString(directDepositAmount)).append("\n");
    sb.append("    endDate: ").append(toIndentedString(endDate)).append("\n");
    sb.append("    grossPay: ").append(toIndentedString(grossPay)).append("\n");
    sb.append("    hours: ").append(toIndentedString(hours)).append("\n");
    sb.append("    netCheck: ").append(toIndentedString(netCheck)).append("\n");
    sb.append("    netPay: ").append(toIndentedString(netPay)).append("\n");
    sb.append("    overtimeDollars: ").append(toIndentedString(overtimeDollars)).append("\n");
    sb.append("    overtimeHours: ").append(toIndentedString(overtimeHours)).append("\n");
    sb.append("    process: ").append(toIndentedString(process)).append("\n");
    sb.append("    regularDollars: ").append(toIndentedString(regularDollars)).append("\n");
    sb.append("    regularHours: ").append(toIndentedString(regularHours)).append("\n");
    sb.append("    transactionNumber: ").append(toIndentedString(transactionNumber)).append("\n");
    sb.append("    voucherNumber: ").append(toIndentedString(voucherNumber)).append("\n");
    sb.append("    workersCompCode: ").append(toIndentedString(workersCompCode)).append("\n");
    sb.append("    year: ").append(toIndentedString(year)).append("\n");
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
    openapiFields.add("autoPay");
    openapiFields.add("beginDate");
    openapiFields.add("checkDate");
    openapiFields.add("checkNumber");
    openapiFields.add("directDepositAmount");
    openapiFields.add("endDate");
    openapiFields.add("grossPay");
    openapiFields.add("hours");
    openapiFields.add("netCheck");
    openapiFields.add("netPay");
    openapiFields.add("overtimeDollars");
    openapiFields.add("overtimeHours");
    openapiFields.add("process");
    openapiFields.add("regularDollars");
    openapiFields.add("regularHours");
    openapiFields.add("transactionNumber");
    openapiFields.add("voucherNumber");
    openapiFields.add("workersCompCode");
    openapiFields.add("year");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PayStatementSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PayStatementSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PayStatementSummary is not found in the empty JSON string", PayStatementSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PayStatementSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PayStatementSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("beginDate") != null && !jsonObj.get("beginDate").isJsonNull()) && !jsonObj.get("beginDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `beginDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("beginDate").toString()));
      }
      if ((jsonObj.get("checkDate") != null && !jsonObj.get("checkDate").isJsonNull()) && !jsonObj.get("checkDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checkDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checkDate").toString()));
      }
      if ((jsonObj.get("endDate") != null && !jsonObj.get("endDate").isJsonNull()) && !jsonObj.get("endDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endDate").toString()));
      }
      if ((jsonObj.get("workersCompCode") != null && !jsonObj.get("workersCompCode").isJsonNull()) && !jsonObj.get("workersCompCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workersCompCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workersCompCode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PayStatementSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PayStatementSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PayStatementSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PayStatementSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<PayStatementSummary>() {
           @Override
           public void write(JsonWriter out, PayStatementSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PayStatementSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PayStatementSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PayStatementSummary
   * @throws IOException if the JSON string is invalid with respect to PayStatementSummary
   */
  public static PayStatementSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PayStatementSummary.class);
  }

  /**
   * Convert an instance of PayStatementSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

