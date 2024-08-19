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
 * Add or update federal tax amount type (taxCalculationCode), amount or percentage, filing status, and exemptions.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EmployeeFederalTax {
  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_DEDUCTIONS_AMOUNT = "deductionsAmount";
  @SerializedName(SERIALIZED_NAME_DEDUCTIONS_AMOUNT)
  private BigDecimal deductionsAmount;

  public static final String SERIALIZED_NAME_DEPENDENTS_AMOUNT = "dependentsAmount";
  @SerializedName(SERIALIZED_NAME_DEPENDENTS_AMOUNT)
  private BigDecimal dependentsAmount;

  public static final String SERIALIZED_NAME_EXEMPTIONS = "exemptions";
  @SerializedName(SERIALIZED_NAME_EXEMPTIONS)
  private BigDecimal exemptions;

  public static final String SERIALIZED_NAME_FILING_STATUS = "filingStatus";
  @SerializedName(SERIALIZED_NAME_FILING_STATUS)
  private String filingStatus;

  public static final String SERIALIZED_NAME_HIGHER_RATE = "higherRate";
  @SerializedName(SERIALIZED_NAME_HIGHER_RATE)
  private Boolean higherRate;

  public static final String SERIALIZED_NAME_OTHER_INCOME_AMOUNT = "otherIncomeAmount";
  @SerializedName(SERIALIZED_NAME_OTHER_INCOME_AMOUNT)
  private BigDecimal otherIncomeAmount;

  public static final String SERIALIZED_NAME_PERCENTAGE = "percentage";
  @SerializedName(SERIALIZED_NAME_PERCENTAGE)
  private BigDecimal percentage;

  public static final String SERIALIZED_NAME_TAX_CALCULATION_CODE = "taxCalculationCode";
  @SerializedName(SERIALIZED_NAME_TAX_CALCULATION_CODE)
  private String taxCalculationCode;

  public static final String SERIALIZED_NAME_W4_FORM_YEAR = "w4FormYear";
  @SerializedName(SERIALIZED_NAME_W4_FORM_YEAR)
  private Integer w4FormYear;

  public EmployeeFederalTax() {
  }

  public EmployeeFederalTax amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Tax amount. &lt;br  /&gt;Decimal (12,2)
   * @return amount
   */
  @javax.annotation.Nullable
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public EmployeeFederalTax deductionsAmount(BigDecimal deductionsAmount) {
    this.deductionsAmount = deductionsAmount;
    return this;
  }

  /**
   * Box 4(b) on form W4 (year 2020 or later): Deductions amount. &lt;br  /&gt;Decimal (12,2)
   * @return deductionsAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getDeductionsAmount() {
    return deductionsAmount;
  }

  public void setDeductionsAmount(BigDecimal deductionsAmount) {
    this.deductionsAmount = deductionsAmount;
  }


  public EmployeeFederalTax dependentsAmount(BigDecimal dependentsAmount) {
    this.dependentsAmount = dependentsAmount;
    return this;
  }

  /**
   * Box 3 on form W4 (year 2020 or later): Total dependents amount. &lt;br  /&gt;Decimal (12,2)
   * @return dependentsAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getDependentsAmount() {
    return dependentsAmount;
  }

  public void setDependentsAmount(BigDecimal dependentsAmount) {
    this.dependentsAmount = dependentsAmount;
  }


  public EmployeeFederalTax exemptions(BigDecimal exemptions) {
    this.exemptions = exemptions;
    return this;
  }

  /**
   * Federal tax exemptions value. &lt;br  /&gt;Decimal (12,2)
   * @return exemptions
   */
  @javax.annotation.Nullable
  public BigDecimal getExemptions() {
    return exemptions;
  }

  public void setExemptions(BigDecimal exemptions) {
    this.exemptions = exemptions;
  }


  public EmployeeFederalTax filingStatus(String filingStatus) {
    this.filingStatus = filingStatus;
    return this;
  }

  /**
   * Employee federal filing status. Common values are *S* (Single), *M* (Married).&lt;br  /&gt;Max length: 50
   * @return filingStatus
   */
  @javax.annotation.Nullable
  public String getFilingStatus() {
    return filingStatus;
  }

  public void setFilingStatus(String filingStatus) {
    this.filingStatus = filingStatus;
  }


  public EmployeeFederalTax higherRate(Boolean higherRate) {
    this.higherRate = higherRate;
    return this;
  }

  /**
   * Box 2(c) on form W4 (year 2020 or later): Multiple Jobs or Spouse Works. &lt;br  /&gt;Boolean
   * @return higherRate
   */
  @javax.annotation.Nullable
  public Boolean getHigherRate() {
    return higherRate;
  }

  public void setHigherRate(Boolean higherRate) {
    this.higherRate = higherRate;
  }


  public EmployeeFederalTax otherIncomeAmount(BigDecimal otherIncomeAmount) {
    this.otherIncomeAmount = otherIncomeAmount;
    return this;
  }

  /**
   * Box 4(a) on form W4 (year 2020 or later): Other income amount. &lt;br  /&gt;Decimal (12,2)
   * @return otherIncomeAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getOtherIncomeAmount() {
    return otherIncomeAmount;
  }

  public void setOtherIncomeAmount(BigDecimal otherIncomeAmount) {
    this.otherIncomeAmount = otherIncomeAmount;
  }


  public EmployeeFederalTax percentage(BigDecimal percentage) {
    this.percentage = percentage;
    return this;
  }

  /**
   * Tax percentage. &lt;br  /&gt;Decimal (12,2)
   * @return percentage
   */
  @javax.annotation.Nullable
  public BigDecimal getPercentage() {
    return percentage;
  }

  public void setPercentage(BigDecimal percentage) {
    this.percentage = percentage;
  }


  public EmployeeFederalTax taxCalculationCode(String taxCalculationCode) {
    this.taxCalculationCode = taxCalculationCode;
    return this;
  }

  /**
   * Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). &lt;br  /&gt;Max length: 10
   * @return taxCalculationCode
   */
  @javax.annotation.Nullable
  public String getTaxCalculationCode() {
    return taxCalculationCode;
  }

  public void setTaxCalculationCode(String taxCalculationCode) {
    this.taxCalculationCode = taxCalculationCode;
  }


  public EmployeeFederalTax w4FormYear(Integer w4FormYear) {
    this.w4FormYear = w4FormYear;
    return this;
  }

  /**
   * The federal W4 form year &lt;br  /&gt;Integer
   * @return w4FormYear
   */
  @javax.annotation.Nullable
  public Integer getW4FormYear() {
    return w4FormYear;
  }

  public void setW4FormYear(Integer w4FormYear) {
    this.w4FormYear = w4FormYear;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EmployeeFederalTax employeeFederalTax = (EmployeeFederalTax) o;
    return Objects.equals(this.amount, employeeFederalTax.amount) &&
        Objects.equals(this.deductionsAmount, employeeFederalTax.deductionsAmount) &&
        Objects.equals(this.dependentsAmount, employeeFederalTax.dependentsAmount) &&
        Objects.equals(this.exemptions, employeeFederalTax.exemptions) &&
        Objects.equals(this.filingStatus, employeeFederalTax.filingStatus) &&
        Objects.equals(this.higherRate, employeeFederalTax.higherRate) &&
        Objects.equals(this.otherIncomeAmount, employeeFederalTax.otherIncomeAmount) &&
        Objects.equals(this.percentage, employeeFederalTax.percentage) &&
        Objects.equals(this.taxCalculationCode, employeeFederalTax.taxCalculationCode) &&
        Objects.equals(this.w4FormYear, employeeFederalTax.w4FormYear);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount, deductionsAmount, dependentsAmount, exemptions, filingStatus, higherRate, otherIncomeAmount, percentage, taxCalculationCode, w4FormYear);
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
    sb.append("class EmployeeFederalTax {\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    deductionsAmount: ").append(toIndentedString(deductionsAmount)).append("\n");
    sb.append("    dependentsAmount: ").append(toIndentedString(dependentsAmount)).append("\n");
    sb.append("    exemptions: ").append(toIndentedString(exemptions)).append("\n");
    sb.append("    filingStatus: ").append(toIndentedString(filingStatus)).append("\n");
    sb.append("    higherRate: ").append(toIndentedString(higherRate)).append("\n");
    sb.append("    otherIncomeAmount: ").append(toIndentedString(otherIncomeAmount)).append("\n");
    sb.append("    percentage: ").append(toIndentedString(percentage)).append("\n");
    sb.append("    taxCalculationCode: ").append(toIndentedString(taxCalculationCode)).append("\n");
    sb.append("    w4FormYear: ").append(toIndentedString(w4FormYear)).append("\n");
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
    openapiFields.add("amount");
    openapiFields.add("deductionsAmount");
    openapiFields.add("dependentsAmount");
    openapiFields.add("exemptions");
    openapiFields.add("filingStatus");
    openapiFields.add("higherRate");
    openapiFields.add("otherIncomeAmount");
    openapiFields.add("percentage");
    openapiFields.add("taxCalculationCode");
    openapiFields.add("w4FormYear");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EmployeeFederalTax
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EmployeeFederalTax.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EmployeeFederalTax is not found in the empty JSON string", EmployeeFederalTax.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EmployeeFederalTax.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EmployeeFederalTax` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("filingStatus") != null && !jsonObj.get("filingStatus").isJsonNull()) && !jsonObj.get("filingStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `filingStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("filingStatus").toString()));
      }
      if ((jsonObj.get("taxCalculationCode") != null && !jsonObj.get("taxCalculationCode").isJsonNull()) && !jsonObj.get("taxCalculationCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `taxCalculationCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("taxCalculationCode").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EmployeeFederalTax.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EmployeeFederalTax' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EmployeeFederalTax> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EmployeeFederalTax.class));

       return (TypeAdapter<T>) new TypeAdapter<EmployeeFederalTax>() {
           @Override
           public void write(JsonWriter out, EmployeeFederalTax value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EmployeeFederalTax read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EmployeeFederalTax given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EmployeeFederalTax
   * @throws IOException if the JSON string is invalid with respect to EmployeeFederalTax
   */
  public static EmployeeFederalTax fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EmployeeFederalTax.class);
  }

  /**
   * Convert an instance of EmployeeFederalTax to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

