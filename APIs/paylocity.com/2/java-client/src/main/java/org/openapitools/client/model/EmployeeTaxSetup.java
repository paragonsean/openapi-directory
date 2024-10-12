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
 * Add tax form, 1099 exempt reasons and notes, and 943 agricultural employee information. Once the employee receives wages, this information cannot be updated. Add or update SUI tax state, retirement plan, and statutory information.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EmployeeTaxSetup {
  public static final String SERIALIZED_NAME_FITW_EXEMPT_NOTES = "fitwExemptNotes";
  @SerializedName(SERIALIZED_NAME_FITW_EXEMPT_NOTES)
  private String fitwExemptNotes;

  public static final String SERIALIZED_NAME_FITW_EXEMPT_REASON = "fitwExemptReason";
  @SerializedName(SERIALIZED_NAME_FITW_EXEMPT_REASON)
  private String fitwExemptReason;

  public static final String SERIALIZED_NAME_FUTA_EXEMPT_NOTES = "futaExemptNotes";
  @SerializedName(SERIALIZED_NAME_FUTA_EXEMPT_NOTES)
  private String futaExemptNotes;

  public static final String SERIALIZED_NAME_FUTA_EXEMPT_REASON = "futaExemptReason";
  @SerializedName(SERIALIZED_NAME_FUTA_EXEMPT_REASON)
  private String futaExemptReason;

  public static final String SERIALIZED_NAME_IS_EMPLOYEE943 = "isEmployee943";
  @SerializedName(SERIALIZED_NAME_IS_EMPLOYEE943)
  private Boolean isEmployee943;

  public static final String SERIALIZED_NAME_IS_PENSION = "isPension";
  @SerializedName(SERIALIZED_NAME_IS_PENSION)
  private Boolean isPension;

  public static final String SERIALIZED_NAME_IS_STATUTORY = "isStatutory";
  @SerializedName(SERIALIZED_NAME_IS_STATUTORY)
  private Boolean isStatutory;

  public static final String SERIALIZED_NAME_MED_EXEMPT_NOTES = "medExemptNotes";
  @SerializedName(SERIALIZED_NAME_MED_EXEMPT_NOTES)
  private String medExemptNotes;

  public static final String SERIALIZED_NAME_MED_EXEMPT_REASON = "medExemptReason";
  @SerializedName(SERIALIZED_NAME_MED_EXEMPT_REASON)
  private String medExemptReason;

  public static final String SERIALIZED_NAME_SITW_EXEMPT_NOTES = "sitwExemptNotes";
  @SerializedName(SERIALIZED_NAME_SITW_EXEMPT_NOTES)
  private String sitwExemptNotes;

  public static final String SERIALIZED_NAME_SITW_EXEMPT_REASON = "sitwExemptReason";
  @SerializedName(SERIALIZED_NAME_SITW_EXEMPT_REASON)
  private String sitwExemptReason;

  public static final String SERIALIZED_NAME_SS_EXEMPT_NOTES = "ssExemptNotes";
  @SerializedName(SERIALIZED_NAME_SS_EXEMPT_NOTES)
  private String ssExemptNotes;

  public static final String SERIALIZED_NAME_SS_EXEMPT_REASON = "ssExemptReason";
  @SerializedName(SERIALIZED_NAME_SS_EXEMPT_REASON)
  private String ssExemptReason;

  public static final String SERIALIZED_NAME_SUI_EXEMPT_NOTES = "suiExemptNotes";
  @SerializedName(SERIALIZED_NAME_SUI_EXEMPT_NOTES)
  private String suiExemptNotes;

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

  public EmployeeTaxSetup() {
  }

  public EmployeeTaxSetup fitwExemptNotes(String fitwExemptNotes) {
    this.fitwExemptNotes = fitwExemptNotes;
    return this;
  }

  /**
   * Notes for FITW exemption.&lt;br  /&gt; Max length: 250
   * @return fitwExemptNotes
   */
  @javax.annotation.Nullable
  public String getFitwExemptNotes() {
    return fitwExemptNotes;
  }

  public void setFitwExemptNotes(String fitwExemptNotes) {
    this.fitwExemptNotes = fitwExemptNotes;
  }


  public EmployeeTaxSetup fitwExemptReason(String fitwExemptReason) {
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


  public EmployeeTaxSetup futaExemptNotes(String futaExemptNotes) {
    this.futaExemptNotes = futaExemptNotes;
    return this;
  }

  /**
   * Notes for FUTA exemption.&lt;br  /&gt; Max length: 250
   * @return futaExemptNotes
   */
  @javax.annotation.Nullable
  public String getFutaExemptNotes() {
    return futaExemptNotes;
  }

  public void setFutaExemptNotes(String futaExemptNotes) {
    this.futaExemptNotes = futaExemptNotes;
  }


  public EmployeeTaxSetup futaExemptReason(String futaExemptReason) {
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


  public EmployeeTaxSetup isEmployee943(Boolean isEmployee943) {
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


  public EmployeeTaxSetup isPension(Boolean isPension) {
    this.isPension = isPension;
    return this;
  }

  /**
   * Indicates if employee is eligible for pension.
   * @return isPension
   */
  @javax.annotation.Nullable
  public Boolean getIsPension() {
    return isPension;
  }

  public void setIsPension(Boolean isPension) {
    this.isPension = isPension;
  }


  public EmployeeTaxSetup isStatutory(Boolean isStatutory) {
    this.isStatutory = isStatutory;
    return this;
  }

  /**
   * Indicates if employee is statutory.
   * @return isStatutory
   */
  @javax.annotation.Nullable
  public Boolean getIsStatutory() {
    return isStatutory;
  }

  public void setIsStatutory(Boolean isStatutory) {
    this.isStatutory = isStatutory;
  }


  public EmployeeTaxSetup medExemptNotes(String medExemptNotes) {
    this.medExemptNotes = medExemptNotes;
    return this;
  }

  /**
   * Notes for Medicare exemption.&lt;br  /&gt; Max length: 250
   * @return medExemptNotes
   */
  @javax.annotation.Nullable
  public String getMedExemptNotes() {
    return medExemptNotes;
  }

  public void setMedExemptNotes(String medExemptNotes) {
    this.medExemptNotes = medExemptNotes;
  }


  public EmployeeTaxSetup medExemptReason(String medExemptReason) {
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


  public EmployeeTaxSetup sitwExemptNotes(String sitwExemptNotes) {
    this.sitwExemptNotes = sitwExemptNotes;
    return this;
  }

  /**
   * Notes for SITW exemption.&lt;br  /&gt; Max length: 250
   * @return sitwExemptNotes
   */
  @javax.annotation.Nullable
  public String getSitwExemptNotes() {
    return sitwExemptNotes;
  }

  public void setSitwExemptNotes(String sitwExemptNotes) {
    this.sitwExemptNotes = sitwExemptNotes;
  }


  public EmployeeTaxSetup sitwExemptReason(String sitwExemptReason) {
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


  public EmployeeTaxSetup ssExemptNotes(String ssExemptNotes) {
    this.ssExemptNotes = ssExemptNotes;
    return this;
  }

  /**
   * Notes for Social Security exemption.&lt;br  /&gt; Max length: 250
   * @return ssExemptNotes
   */
  @javax.annotation.Nullable
  public String getSsExemptNotes() {
    return ssExemptNotes;
  }

  public void setSsExemptNotes(String ssExemptNotes) {
    this.ssExemptNotes = ssExemptNotes;
  }


  public EmployeeTaxSetup ssExemptReason(String ssExemptReason) {
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


  public EmployeeTaxSetup suiExemptNotes(String suiExemptNotes) {
    this.suiExemptNotes = suiExemptNotes;
    return this;
  }

  /**
   * Notes for SUI exemption.&lt;br  /&gt; Max length: 250
   * @return suiExemptNotes
   */
  @javax.annotation.Nullable
  public String getSuiExemptNotes() {
    return suiExemptNotes;
  }

  public void setSuiExemptNotes(String suiExemptNotes) {
    this.suiExemptNotes = suiExemptNotes;
  }


  public EmployeeTaxSetup suiExemptReason(String suiExemptReason) {
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


  public EmployeeTaxSetup suiState(String suiState) {
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


  public EmployeeTaxSetup taxDistributionCode1099R(String taxDistributionCode1099R) {
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


  public EmployeeTaxSetup taxForm(String taxForm) {
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



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EmployeeTaxSetup employeeTaxSetup = (EmployeeTaxSetup) o;
    return Objects.equals(this.fitwExemptNotes, employeeTaxSetup.fitwExemptNotes) &&
        Objects.equals(this.fitwExemptReason, employeeTaxSetup.fitwExemptReason) &&
        Objects.equals(this.futaExemptNotes, employeeTaxSetup.futaExemptNotes) &&
        Objects.equals(this.futaExemptReason, employeeTaxSetup.futaExemptReason) &&
        Objects.equals(this.isEmployee943, employeeTaxSetup.isEmployee943) &&
        Objects.equals(this.isPension, employeeTaxSetup.isPension) &&
        Objects.equals(this.isStatutory, employeeTaxSetup.isStatutory) &&
        Objects.equals(this.medExemptNotes, employeeTaxSetup.medExemptNotes) &&
        Objects.equals(this.medExemptReason, employeeTaxSetup.medExemptReason) &&
        Objects.equals(this.sitwExemptNotes, employeeTaxSetup.sitwExemptNotes) &&
        Objects.equals(this.sitwExemptReason, employeeTaxSetup.sitwExemptReason) &&
        Objects.equals(this.ssExemptNotes, employeeTaxSetup.ssExemptNotes) &&
        Objects.equals(this.ssExemptReason, employeeTaxSetup.ssExemptReason) &&
        Objects.equals(this.suiExemptNotes, employeeTaxSetup.suiExemptNotes) &&
        Objects.equals(this.suiExemptReason, employeeTaxSetup.suiExemptReason) &&
        Objects.equals(this.suiState, employeeTaxSetup.suiState) &&
        Objects.equals(this.taxDistributionCode1099R, employeeTaxSetup.taxDistributionCode1099R) &&
        Objects.equals(this.taxForm, employeeTaxSetup.taxForm);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(fitwExemptNotes, fitwExemptReason, futaExemptNotes, futaExemptReason, isEmployee943, isPension, isStatutory, medExemptNotes, medExemptReason, sitwExemptNotes, sitwExemptReason, ssExemptNotes, ssExemptReason, suiExemptNotes, suiExemptReason, suiState, taxDistributionCode1099R, taxForm);
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
    sb.append("class EmployeeTaxSetup {\n");
    sb.append("    fitwExemptNotes: ").append(toIndentedString(fitwExemptNotes)).append("\n");
    sb.append("    fitwExemptReason: ").append(toIndentedString(fitwExemptReason)).append("\n");
    sb.append("    futaExemptNotes: ").append(toIndentedString(futaExemptNotes)).append("\n");
    sb.append("    futaExemptReason: ").append(toIndentedString(futaExemptReason)).append("\n");
    sb.append("    isEmployee943: ").append(toIndentedString(isEmployee943)).append("\n");
    sb.append("    isPension: ").append(toIndentedString(isPension)).append("\n");
    sb.append("    isStatutory: ").append(toIndentedString(isStatutory)).append("\n");
    sb.append("    medExemptNotes: ").append(toIndentedString(medExemptNotes)).append("\n");
    sb.append("    medExemptReason: ").append(toIndentedString(medExemptReason)).append("\n");
    sb.append("    sitwExemptNotes: ").append(toIndentedString(sitwExemptNotes)).append("\n");
    sb.append("    sitwExemptReason: ").append(toIndentedString(sitwExemptReason)).append("\n");
    sb.append("    ssExemptNotes: ").append(toIndentedString(ssExemptNotes)).append("\n");
    sb.append("    ssExemptReason: ").append(toIndentedString(ssExemptReason)).append("\n");
    sb.append("    suiExemptNotes: ").append(toIndentedString(suiExemptNotes)).append("\n");
    sb.append("    suiExemptReason: ").append(toIndentedString(suiExemptReason)).append("\n");
    sb.append("    suiState: ").append(toIndentedString(suiState)).append("\n");
    sb.append("    taxDistributionCode1099R: ").append(toIndentedString(taxDistributionCode1099R)).append("\n");
    sb.append("    taxForm: ").append(toIndentedString(taxForm)).append("\n");
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
    openapiFields.add("fitwExemptNotes");
    openapiFields.add("fitwExemptReason");
    openapiFields.add("futaExemptNotes");
    openapiFields.add("futaExemptReason");
    openapiFields.add("isEmployee943");
    openapiFields.add("isPension");
    openapiFields.add("isStatutory");
    openapiFields.add("medExemptNotes");
    openapiFields.add("medExemptReason");
    openapiFields.add("sitwExemptNotes");
    openapiFields.add("sitwExemptReason");
    openapiFields.add("ssExemptNotes");
    openapiFields.add("ssExemptReason");
    openapiFields.add("suiExemptNotes");
    openapiFields.add("suiExemptReason");
    openapiFields.add("suiState");
    openapiFields.add("taxDistributionCode1099R");
    openapiFields.add("taxForm");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EmployeeTaxSetup
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EmployeeTaxSetup.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EmployeeTaxSetup is not found in the empty JSON string", EmployeeTaxSetup.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EmployeeTaxSetup.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EmployeeTaxSetup` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("fitwExemptNotes") != null && !jsonObj.get("fitwExemptNotes").isJsonNull()) && !jsonObj.get("fitwExemptNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fitwExemptNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fitwExemptNotes").toString()));
      }
      if ((jsonObj.get("fitwExemptReason") != null && !jsonObj.get("fitwExemptReason").isJsonNull()) && !jsonObj.get("fitwExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fitwExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fitwExemptReason").toString()));
      }
      if ((jsonObj.get("futaExemptNotes") != null && !jsonObj.get("futaExemptNotes").isJsonNull()) && !jsonObj.get("futaExemptNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `futaExemptNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("futaExemptNotes").toString()));
      }
      if ((jsonObj.get("futaExemptReason") != null && !jsonObj.get("futaExemptReason").isJsonNull()) && !jsonObj.get("futaExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `futaExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("futaExemptReason").toString()));
      }
      if ((jsonObj.get("medExemptNotes") != null && !jsonObj.get("medExemptNotes").isJsonNull()) && !jsonObj.get("medExemptNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `medExemptNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("medExemptNotes").toString()));
      }
      if ((jsonObj.get("medExemptReason") != null && !jsonObj.get("medExemptReason").isJsonNull()) && !jsonObj.get("medExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `medExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("medExemptReason").toString()));
      }
      if ((jsonObj.get("sitwExemptNotes") != null && !jsonObj.get("sitwExemptNotes").isJsonNull()) && !jsonObj.get("sitwExemptNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sitwExemptNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sitwExemptNotes").toString()));
      }
      if ((jsonObj.get("sitwExemptReason") != null && !jsonObj.get("sitwExemptReason").isJsonNull()) && !jsonObj.get("sitwExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sitwExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sitwExemptReason").toString()));
      }
      if ((jsonObj.get("ssExemptNotes") != null && !jsonObj.get("ssExemptNotes").isJsonNull()) && !jsonObj.get("ssExemptNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssExemptNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssExemptNotes").toString()));
      }
      if ((jsonObj.get("ssExemptReason") != null && !jsonObj.get("ssExemptReason").isJsonNull()) && !jsonObj.get("ssExemptReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssExemptReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssExemptReason").toString()));
      }
      if ((jsonObj.get("suiExemptNotes") != null && !jsonObj.get("suiExemptNotes").isJsonNull()) && !jsonObj.get("suiExemptNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suiExemptNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suiExemptNotes").toString()));
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
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EmployeeTaxSetup.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EmployeeTaxSetup' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EmployeeTaxSetup> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EmployeeTaxSetup.class));

       return (TypeAdapter<T>) new TypeAdapter<EmployeeTaxSetup>() {
           @Override
           public void write(JsonWriter out, EmployeeTaxSetup value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EmployeeTaxSetup read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EmployeeTaxSetup given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EmployeeTaxSetup
   * @throws IOException if the JSON string is invalid with respect to EmployeeTaxSetup
   */
  public static EmployeeTaxSetup fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EmployeeTaxSetup.class);
  }

  /**
   * Convert an instance of EmployeeTaxSetup to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

