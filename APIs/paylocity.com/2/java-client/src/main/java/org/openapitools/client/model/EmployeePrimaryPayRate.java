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
 * Add or update hourly or salary pay rate, effective date, and pay frequency.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EmployeePrimaryPayRate {
  public static final String SERIALIZED_NAME_ANNUAL_SALARY = "annualSalary";
  @SerializedName(SERIALIZED_NAME_ANNUAL_SALARY)
  private BigDecimal annualSalary;

  public static final String SERIALIZED_NAME_BASE_RATE = "baseRate";
  @SerializedName(SERIALIZED_NAME_BASE_RATE)
  private BigDecimal baseRate;

  public static final String SERIALIZED_NAME_BEGIN_CHECK_DATE = "beginCheckDate";
  @SerializedName(SERIALIZED_NAME_BEGIN_CHECK_DATE)
  private String beginCheckDate;

  public static final String SERIALIZED_NAME_CHANGE_REASON = "changeReason";
  @SerializedName(SERIALIZED_NAME_CHANGE_REASON)
  private String changeReason;

  public static final String SERIALIZED_NAME_DEFAULT_HOURS = "defaultHours";
  @SerializedName(SERIALIZED_NAME_DEFAULT_HOURS)
  private BigDecimal defaultHours;

  public static final String SERIALIZED_NAME_EFFECTIVE_DATE = "effectiveDate";
  @SerializedName(SERIALIZED_NAME_EFFECTIVE_DATE)
  private String effectiveDate;

  public static final String SERIALIZED_NAME_IS_AUTO_PAY = "isAutoPay";
  @SerializedName(SERIALIZED_NAME_IS_AUTO_PAY)
  private Boolean isAutoPay;

  public static final String SERIALIZED_NAME_PAY_FREQUENCY = "payFrequency";
  @SerializedName(SERIALIZED_NAME_PAY_FREQUENCY)
  private String payFrequency;

  public static final String SERIALIZED_NAME_PAY_GRADE = "payGrade";
  @SerializedName(SERIALIZED_NAME_PAY_GRADE)
  private String payGrade;

  public static final String SERIALIZED_NAME_PAY_RATE_NOTE = "payRateNote";
  @SerializedName(SERIALIZED_NAME_PAY_RATE_NOTE)
  private String payRateNote;

  public static final String SERIALIZED_NAME_PAY_TYPE = "payType";
  @SerializedName(SERIALIZED_NAME_PAY_TYPE)
  private String payType;

  public static final String SERIALIZED_NAME_RATE_PER = "ratePer";
  @SerializedName(SERIALIZED_NAME_RATE_PER)
  private String ratePer;

  public static final String SERIALIZED_NAME_SALARY = "salary";
  @SerializedName(SERIALIZED_NAME_SALARY)
  private BigDecimal salary;

  public EmployeePrimaryPayRate() {
  }

  public EmployeePrimaryPayRate annualSalary(BigDecimal annualSalary) {
    this.annualSalary = annualSalary;
    return this;
  }

  /**
   * Employee annual salary.&lt;br /&gt;Decimal (12,6)
   * @return annualSalary
   */
  @javax.annotation.Nullable
  public BigDecimal getAnnualSalary() {
    return annualSalary;
  }

  public void setAnnualSalary(BigDecimal annualSalary) {
    this.annualSalary = annualSalary;
  }


  public EmployeePrimaryPayRate baseRate(BigDecimal baseRate) {
    this.baseRate = baseRate;
    return this;
  }

  /**
   * Employee base rate, used for Hourly employees. &lt;br  /&gt;Decimal (12,6)
   * @return baseRate
   */
  @javax.annotation.Nullable
  public BigDecimal getBaseRate() {
    return baseRate;
  }

  public void setBaseRate(BigDecimal baseRate) {
    this.baseRate = baseRate;
  }


  public EmployeePrimaryPayRate beginCheckDate(String beginCheckDate) {
    this.beginCheckDate = beginCheckDate;
    return this;
  }

  /**
   * The date of the first check on which the new pay rate will appear. This value is only applicable when updating an existing employee. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return beginCheckDate
   */
  @javax.annotation.Nullable
  public String getBeginCheckDate() {
    return beginCheckDate;
  }

  public void setBeginCheckDate(String beginCheckDate) {
    this.beginCheckDate = beginCheckDate;
  }


  public EmployeePrimaryPayRate changeReason(String changeReason) {
    this.changeReason = changeReason;
    return this;
  }

  /**
   * Pay rate change reason.&lt;br  /&gt; Max length: 30
   * @return changeReason
   */
  @javax.annotation.Nullable
  public String getChangeReason() {
    return changeReason;
  }

  public void setChangeReason(String changeReason) {
    this.changeReason = changeReason;
  }


  public EmployeePrimaryPayRate defaultHours(BigDecimal defaultHours) {
    this.defaultHours = defaultHours;
    return this;
  }

  /**
   * Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. &lt;br  /&gt;Decimal (12,2)
   * @return defaultHours
   */
  @javax.annotation.Nullable
  public BigDecimal getDefaultHours() {
    return defaultHours;
  }

  public void setDefaultHours(BigDecimal defaultHours) {
    this.defaultHours = defaultHours;
  }


  public EmployeePrimaryPayRate effectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
    return this;
  }

  /**
   * The date the employee&#39;s pay rate takes effect. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return effectiveDate
   */
  @javax.annotation.Nullable
  public String getEffectiveDate() {
    return effectiveDate;
  }

  public void setEffectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
  }


  public EmployeePrimaryPayRate isAutoPay(Boolean isAutoPay) {
    this.isAutoPay = isAutoPay;
    return this;
  }

  /**
   * If set to *True*, employee will be paid automatically using deafultHours.
   * @return isAutoPay
   */
  @javax.annotation.Nullable
  public Boolean getIsAutoPay() {
    return isAutoPay;
  }

  public void setIsAutoPay(Boolean isAutoPay) {
    this.isAutoPay = isAutoPay;
  }


  public EmployeePrimaryPayRate payFrequency(String payFrequency) {
    this.payFrequency = payFrequency;
    return this;
  }

  /**
   * Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. &lt;br  /&gt;Max length: 5
   * @return payFrequency
   */
  @javax.annotation.Nullable
  public String getPayFrequency() {
    return payFrequency;
  }

  public void setPayFrequency(String payFrequency) {
    this.payFrequency = payFrequency;
  }


  public EmployeePrimaryPayRate payGrade(String payGrade) {
    this.payGrade = payGrade;
    return this;
  }

  /**
   * Employee pay grade. Must match Company setup. &lt;br  /&gt; Max length: 10
   * @return payGrade
   */
  @javax.annotation.Nullable
  public String getPayGrade() {
    return payGrade;
  }

  public void setPayGrade(String payGrade) {
    this.payGrade = payGrade;
  }


  public EmployeePrimaryPayRate payRateNote(String payRateNote) {
    this.payRateNote = payRateNote;
    return this;
  }

  /**
   * Pay rate notes regarding employee.&lt;br  /&gt; Max length: 250
   * @return payRateNote
   */
  @javax.annotation.Nullable
  public String getPayRateNote() {
    return payRateNote;
  }

  public void setPayRateNote(String payRateNote) {
    this.payRateNote = payRateNote;
  }


  public EmployeePrimaryPayRate payType(String payType) {
    this.payType = payType;
    return this;
  }

  /**
   * Employee pay type (rate code). Valid values are *Hourly* or *Salary*. &lt;br  /&gt;Max length: 10
   * @return payType
   */
  @javax.annotation.Nullable
  public String getPayType() {
    return payType;
  }

  public void setPayType(String payType) {
    this.payType = payType;
  }


  public EmployeePrimaryPayRate ratePer(String ratePer) {
    this.ratePer = ratePer;
    return this;
  }

  /**
   * Employee base rate frequency used with payType Hourly. Common values are *Hour, Week*. Default is Hour. &lt;br  /&gt;Max length: 10
   * @return ratePer
   */
  @javax.annotation.Nullable
  public String getRatePer() {
    return ratePer;
  }

  public void setRatePer(String ratePer) {
    this.ratePer = ratePer;
  }


  public EmployeePrimaryPayRate salary(BigDecimal salary) {
    this.salary = salary;
    return this;
  }

  /**
   * Employee gross salary per pay period used with payType Salary.&lt;br  /&gt;Decimal (12,6)
   * @return salary
   */
  @javax.annotation.Nullable
  public BigDecimal getSalary() {
    return salary;
  }

  public void setSalary(BigDecimal salary) {
    this.salary = salary;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EmployeePrimaryPayRate employeePrimaryPayRate = (EmployeePrimaryPayRate) o;
    return Objects.equals(this.annualSalary, employeePrimaryPayRate.annualSalary) &&
        Objects.equals(this.baseRate, employeePrimaryPayRate.baseRate) &&
        Objects.equals(this.beginCheckDate, employeePrimaryPayRate.beginCheckDate) &&
        Objects.equals(this.changeReason, employeePrimaryPayRate.changeReason) &&
        Objects.equals(this.defaultHours, employeePrimaryPayRate.defaultHours) &&
        Objects.equals(this.effectiveDate, employeePrimaryPayRate.effectiveDate) &&
        Objects.equals(this.isAutoPay, employeePrimaryPayRate.isAutoPay) &&
        Objects.equals(this.payFrequency, employeePrimaryPayRate.payFrequency) &&
        Objects.equals(this.payGrade, employeePrimaryPayRate.payGrade) &&
        Objects.equals(this.payRateNote, employeePrimaryPayRate.payRateNote) &&
        Objects.equals(this.payType, employeePrimaryPayRate.payType) &&
        Objects.equals(this.ratePer, employeePrimaryPayRate.ratePer) &&
        Objects.equals(this.salary, employeePrimaryPayRate.salary);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(annualSalary, baseRate, beginCheckDate, changeReason, defaultHours, effectiveDate, isAutoPay, payFrequency, payGrade, payRateNote, payType, ratePer, salary);
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
    sb.append("class EmployeePrimaryPayRate {\n");
    sb.append("    annualSalary: ").append(toIndentedString(annualSalary)).append("\n");
    sb.append("    baseRate: ").append(toIndentedString(baseRate)).append("\n");
    sb.append("    beginCheckDate: ").append(toIndentedString(beginCheckDate)).append("\n");
    sb.append("    changeReason: ").append(toIndentedString(changeReason)).append("\n");
    sb.append("    defaultHours: ").append(toIndentedString(defaultHours)).append("\n");
    sb.append("    effectiveDate: ").append(toIndentedString(effectiveDate)).append("\n");
    sb.append("    isAutoPay: ").append(toIndentedString(isAutoPay)).append("\n");
    sb.append("    payFrequency: ").append(toIndentedString(payFrequency)).append("\n");
    sb.append("    payGrade: ").append(toIndentedString(payGrade)).append("\n");
    sb.append("    payRateNote: ").append(toIndentedString(payRateNote)).append("\n");
    sb.append("    payType: ").append(toIndentedString(payType)).append("\n");
    sb.append("    ratePer: ").append(toIndentedString(ratePer)).append("\n");
    sb.append("    salary: ").append(toIndentedString(salary)).append("\n");
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
    openapiFields.add("annualSalary");
    openapiFields.add("baseRate");
    openapiFields.add("beginCheckDate");
    openapiFields.add("changeReason");
    openapiFields.add("defaultHours");
    openapiFields.add("effectiveDate");
    openapiFields.add("isAutoPay");
    openapiFields.add("payFrequency");
    openapiFields.add("payGrade");
    openapiFields.add("payRateNote");
    openapiFields.add("payType");
    openapiFields.add("ratePer");
    openapiFields.add("salary");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EmployeePrimaryPayRate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EmployeePrimaryPayRate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EmployeePrimaryPayRate is not found in the empty JSON string", EmployeePrimaryPayRate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EmployeePrimaryPayRate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EmployeePrimaryPayRate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("beginCheckDate") != null && !jsonObj.get("beginCheckDate").isJsonNull()) && !jsonObj.get("beginCheckDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `beginCheckDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("beginCheckDate").toString()));
      }
      if ((jsonObj.get("changeReason") != null && !jsonObj.get("changeReason").isJsonNull()) && !jsonObj.get("changeReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `changeReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("changeReason").toString()));
      }
      if ((jsonObj.get("effectiveDate") != null && !jsonObj.get("effectiveDate").isJsonNull()) && !jsonObj.get("effectiveDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `effectiveDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("effectiveDate").toString()));
      }
      if ((jsonObj.get("payFrequency") != null && !jsonObj.get("payFrequency").isJsonNull()) && !jsonObj.get("payFrequency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payFrequency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payFrequency").toString()));
      }
      if ((jsonObj.get("payGrade") != null && !jsonObj.get("payGrade").isJsonNull()) && !jsonObj.get("payGrade").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payGrade` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payGrade").toString()));
      }
      if ((jsonObj.get("payRateNote") != null && !jsonObj.get("payRateNote").isJsonNull()) && !jsonObj.get("payRateNote").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payRateNote` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payRateNote").toString()));
      }
      if ((jsonObj.get("payType") != null && !jsonObj.get("payType").isJsonNull()) && !jsonObj.get("payType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payType").toString()));
      }
      if ((jsonObj.get("ratePer") != null && !jsonObj.get("ratePer").isJsonNull()) && !jsonObj.get("ratePer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ratePer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ratePer").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EmployeePrimaryPayRate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EmployeePrimaryPayRate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EmployeePrimaryPayRate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EmployeePrimaryPayRate.class));

       return (TypeAdapter<T>) new TypeAdapter<EmployeePrimaryPayRate>() {
           @Override
           public void write(JsonWriter out, EmployeePrimaryPayRate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EmployeePrimaryPayRate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EmployeePrimaryPayRate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EmployeePrimaryPayRate
   * @throws IOException if the JSON string is invalid with respect to EmployeePrimaryPayRate
   */
  public static EmployeePrimaryPayRate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EmployeePrimaryPayRate.class);
  }

  /**
   * Convert an instance of EmployeePrimaryPayRate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

