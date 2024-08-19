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
 * The Work Eligibility model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StagedEmployeeWorkEligibilityInner {
  public static final String SERIALIZED_NAME_ALIEN_OR_ADMISSION_DOCUMENT_NUMBER = "alienOrAdmissionDocumentNumber";
  @SerializedName(SERIALIZED_NAME_ALIEN_OR_ADMISSION_DOCUMENT_NUMBER)
  private String alienOrAdmissionDocumentNumber;

  public static final String SERIALIZED_NAME_ATTESTED_DATE = "attestedDate";
  @SerializedName(SERIALIZED_NAME_ATTESTED_DATE)
  private String attestedDate;

  public static final String SERIALIZED_NAME_COUNTRY_OF_ISSUANCE = "countryOfIssuance";
  @SerializedName(SERIALIZED_NAME_COUNTRY_OF_ISSUANCE)
  private String countryOfIssuance;

  public static final String SERIALIZED_NAME_FOREIGN_PASSPORT_NUMBER = "foreignPassportNumber";
  @SerializedName(SERIALIZED_NAME_FOREIGN_PASSPORT_NUMBER)
  private String foreignPassportNumber;

  public static final String SERIALIZED_NAME_I94_ADMISSION_NUMBER = "i94AdmissionNumber";
  @SerializedName(SERIALIZED_NAME_I94_ADMISSION_NUMBER)
  private String i94AdmissionNumber;

  public static final String SERIALIZED_NAME_I9_DATE_VERIFIED = "i9DateVerified";
  @SerializedName(SERIALIZED_NAME_I9_DATE_VERIFIED)
  private String i9DateVerified;

  public static final String SERIALIZED_NAME_I9_NOTES = "i9Notes";
  @SerializedName(SERIALIZED_NAME_I9_NOTES)
  private String i9Notes;

  public static final String SERIALIZED_NAME_IS_I9_VERIFIED = "isI9Verified";
  @SerializedName(SERIALIZED_NAME_IS_I9_VERIFIED)
  private Boolean isI9Verified;

  public static final String SERIALIZED_NAME_IS_SSN_VERIFIED = "isSsnVerified";
  @SerializedName(SERIALIZED_NAME_IS_SSN_VERIFIED)
  private Boolean isSsnVerified;

  public static final String SERIALIZED_NAME_SSN_DATE_VERIFIED = "ssnDateVerified";
  @SerializedName(SERIALIZED_NAME_SSN_DATE_VERIFIED)
  private String ssnDateVerified;

  public static final String SERIALIZED_NAME_SSN_NOTES = "ssnNotes";
  @SerializedName(SERIALIZED_NAME_SSN_NOTES)
  private String ssnNotes;

  public static final String SERIALIZED_NAME_VISA_TYPE = "visaType";
  @SerializedName(SERIALIZED_NAME_VISA_TYPE)
  private String visaType;

  public static final String SERIALIZED_NAME_WORK_AUTHORIZATION = "workAuthorization";
  @SerializedName(SERIALIZED_NAME_WORK_AUTHORIZATION)
  private String workAuthorization;

  public static final String SERIALIZED_NAME_WORK_UNTIL = "workUntil";
  @SerializedName(SERIALIZED_NAME_WORK_UNTIL)
  private String workUntil;

  public StagedEmployeeWorkEligibilityInner() {
  }

  public StagedEmployeeWorkEligibilityInner alienOrAdmissionDocumentNumber(String alienOrAdmissionDocumentNumber) {
    this.alienOrAdmissionDocumentNumber = alienOrAdmissionDocumentNumber;
    return this;
  }

  /**
   * Employee USCIS or Admission Number. &lt;br  /&gt; Must be 7-10 characters and may begin with an &#39;A&#39;
   * @return alienOrAdmissionDocumentNumber
   */
  @javax.annotation.Nullable
  public String getAlienOrAdmissionDocumentNumber() {
    return alienOrAdmissionDocumentNumber;
  }

  public void setAlienOrAdmissionDocumentNumber(String alienOrAdmissionDocumentNumber) {
    this.alienOrAdmissionDocumentNumber = alienOrAdmissionDocumentNumber;
  }


  public StagedEmployeeWorkEligibilityInner attestedDate(String attestedDate) {
    this.attestedDate = attestedDate;
    return this;
  }

  /**
   * The date the I-9 Verification form was attested by Employer or Authorized representative. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
   * @return attestedDate
   */
  @javax.annotation.Nullable
  public String getAttestedDate() {
    return attestedDate;
  }

  public void setAttestedDate(String attestedDate) {
    this.attestedDate = attestedDate;
  }


  public StagedEmployeeWorkEligibilityInner countryOfIssuance(String countryOfIssuance) {
    this.countryOfIssuance = countryOfIssuance;
    return this;
  }

  /**
   * If Foreign Passport number is provided, provide its country of issuance. Must match Paylocity setup.&lt;br  /&gt; Max length: 30
   * @return countryOfIssuance
   */
  @javax.annotation.Nullable
  public String getCountryOfIssuance() {
    return countryOfIssuance;
  }

  public void setCountryOfIssuance(String countryOfIssuance) {
    this.countryOfIssuance = countryOfIssuance;
  }


  public StagedEmployeeWorkEligibilityInner foreignPassportNumber(String foreignPassportNumber) {
    this.foreignPassportNumber = foreignPassportNumber;
    return this;
  }

  /**
   * Foreign Passport Number.&lt;br  /&gt; Max length: 50
   * @return foreignPassportNumber
   */
  @javax.annotation.Nullable
  public String getForeignPassportNumber() {
    return foreignPassportNumber;
  }

  public void setForeignPassportNumber(String foreignPassportNumber) {
    this.foreignPassportNumber = foreignPassportNumber;
  }


  public StagedEmployeeWorkEligibilityInner i94AdmissionNumber(String i94AdmissionNumber) {
    this.i94AdmissionNumber = i94AdmissionNumber;
    return this;
  }

  /**
   * Form I-94 admission number.&lt;br  /&gt; Must be 11 numeric characters
   * @return i94AdmissionNumber
   */
  @javax.annotation.Nullable
  public String getI94AdmissionNumber() {
    return i94AdmissionNumber;
  }

  public void setI94AdmissionNumber(String i94AdmissionNumber) {
    this.i94AdmissionNumber = i94AdmissionNumber;
  }


  public StagedEmployeeWorkEligibilityInner i9DateVerified(String i9DateVerified) {
    this.i9DateVerified = i9DateVerified;
    return this;
  }

  /**
   * Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return i9DateVerified
   */
  @javax.annotation.Nullable
  public String getI9DateVerified() {
    return i9DateVerified;
  }

  public void setI9DateVerified(String i9DateVerified) {
    this.i9DateVerified = i9DateVerified;
  }


  public StagedEmployeeWorkEligibilityInner i9Notes(String i9Notes) {
    this.i9Notes = i9Notes;
    return this;
  }

  /**
   * Notes regarding employee&#39;s i9.&lt;br  /&gt; Max length: 4000
   * @return i9Notes
   */
  @javax.annotation.Nullable
  public String getI9Notes() {
    return i9Notes;
  }

  public void setI9Notes(String i9Notes) {
    this.i9Notes = i9Notes;
  }


  public StagedEmployeeWorkEligibilityInner isI9Verified(Boolean isI9Verified) {
    this.isI9Verified = isI9Verified;
    return this;
  }

  /**
   * Indicates if employee I9 is verified.
   * @return isI9Verified
   */
  @javax.annotation.Nullable
  public Boolean getIsI9Verified() {
    return isI9Verified;
  }

  public void setIsI9Verified(Boolean isI9Verified) {
    this.isI9Verified = isI9Verified;
  }


  public StagedEmployeeWorkEligibilityInner isSsnVerified(Boolean isSsnVerified) {
    this.isSsnVerified = isSsnVerified;
    return this;
  }

  /**
   * Indicates if employee SSN is verified.
   * @return isSsnVerified
   */
  @javax.annotation.Nullable
  public Boolean getIsSsnVerified() {
    return isSsnVerified;
  }

  public void setIsSsnVerified(Boolean isSsnVerified) {
    this.isSsnVerified = isSsnVerified;
  }


  public StagedEmployeeWorkEligibilityInner ssnDateVerified(String ssnDateVerified) {
    this.ssnDateVerified = ssnDateVerified;
    return this;
  }

  /**
   * The date of employer verification of employee SSN. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return ssnDateVerified
   */
  @javax.annotation.Nullable
  public String getSsnDateVerified() {
    return ssnDateVerified;
  }

  public void setSsnDateVerified(String ssnDateVerified) {
    this.ssnDateVerified = ssnDateVerified;
  }


  public StagedEmployeeWorkEligibilityInner ssnNotes(String ssnNotes) {
    this.ssnNotes = ssnNotes;
    return this;
  }

  /**
   * Notes regarding employee&#39;s SSN.&lt;br  /&gt; Max length: 4000
   * @return ssnNotes
   */
  @javax.annotation.Nullable
  public String getSsnNotes() {
    return ssnNotes;
  }

  public void setSsnNotes(String ssnNotes) {
    this.ssnNotes = ssnNotes;
  }


  public StagedEmployeeWorkEligibilityInner visaType(String visaType) {
    this.visaType = visaType;
    return this;
  }

  /**
   * Employee Visa type. Must match one of the system coded values.&lt;br  /&gt; Max length: 100
   * @return visaType
   */
  @javax.annotation.Nullable
  public String getVisaType() {
    return visaType;
  }

  public void setVisaType(String visaType) {
    this.visaType = visaType;
  }


  public StagedEmployeeWorkEligibilityInner workAuthorization(String workAuthorization) {
    this.workAuthorization = workAuthorization;
    return this;
  }

  /**
   * Employee work authorization. Must match one of the system coded values.&lt;br  /&gt; Max length: 100
   * @return workAuthorization
   */
  @javax.annotation.Nullable
  public String getWorkAuthorization() {
    return workAuthorization;
  }

  public void setWorkAuthorization(String workAuthorization) {
    this.workAuthorization = workAuthorization;
  }


  public StagedEmployeeWorkEligibilityInner workUntil(String workUntil) {
    this.workUntil = workUntil;
    return this;
  }

  /**
   * End date of employee work eligibility.  Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return workUntil
   */
  @javax.annotation.Nullable
  public String getWorkUntil() {
    return workUntil;
  }

  public void setWorkUntil(String workUntil) {
    this.workUntil = workUntil;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StagedEmployeeWorkEligibilityInner stagedEmployeeWorkEligibilityInner = (StagedEmployeeWorkEligibilityInner) o;
    return Objects.equals(this.alienOrAdmissionDocumentNumber, stagedEmployeeWorkEligibilityInner.alienOrAdmissionDocumentNumber) &&
        Objects.equals(this.attestedDate, stagedEmployeeWorkEligibilityInner.attestedDate) &&
        Objects.equals(this.countryOfIssuance, stagedEmployeeWorkEligibilityInner.countryOfIssuance) &&
        Objects.equals(this.foreignPassportNumber, stagedEmployeeWorkEligibilityInner.foreignPassportNumber) &&
        Objects.equals(this.i94AdmissionNumber, stagedEmployeeWorkEligibilityInner.i94AdmissionNumber) &&
        Objects.equals(this.i9DateVerified, stagedEmployeeWorkEligibilityInner.i9DateVerified) &&
        Objects.equals(this.i9Notes, stagedEmployeeWorkEligibilityInner.i9Notes) &&
        Objects.equals(this.isI9Verified, stagedEmployeeWorkEligibilityInner.isI9Verified) &&
        Objects.equals(this.isSsnVerified, stagedEmployeeWorkEligibilityInner.isSsnVerified) &&
        Objects.equals(this.ssnDateVerified, stagedEmployeeWorkEligibilityInner.ssnDateVerified) &&
        Objects.equals(this.ssnNotes, stagedEmployeeWorkEligibilityInner.ssnNotes) &&
        Objects.equals(this.visaType, stagedEmployeeWorkEligibilityInner.visaType) &&
        Objects.equals(this.workAuthorization, stagedEmployeeWorkEligibilityInner.workAuthorization) &&
        Objects.equals(this.workUntil, stagedEmployeeWorkEligibilityInner.workUntil);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(alienOrAdmissionDocumentNumber, attestedDate, countryOfIssuance, foreignPassportNumber, i94AdmissionNumber, i9DateVerified, i9Notes, isI9Verified, isSsnVerified, ssnDateVerified, ssnNotes, visaType, workAuthorization, workUntil);
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
    sb.append("class StagedEmployeeWorkEligibilityInner {\n");
    sb.append("    alienOrAdmissionDocumentNumber: ").append(toIndentedString(alienOrAdmissionDocumentNumber)).append("\n");
    sb.append("    attestedDate: ").append(toIndentedString(attestedDate)).append("\n");
    sb.append("    countryOfIssuance: ").append(toIndentedString(countryOfIssuance)).append("\n");
    sb.append("    foreignPassportNumber: ").append(toIndentedString(foreignPassportNumber)).append("\n");
    sb.append("    i94AdmissionNumber: ").append(toIndentedString(i94AdmissionNumber)).append("\n");
    sb.append("    i9DateVerified: ").append(toIndentedString(i9DateVerified)).append("\n");
    sb.append("    i9Notes: ").append(toIndentedString(i9Notes)).append("\n");
    sb.append("    isI9Verified: ").append(toIndentedString(isI9Verified)).append("\n");
    sb.append("    isSsnVerified: ").append(toIndentedString(isSsnVerified)).append("\n");
    sb.append("    ssnDateVerified: ").append(toIndentedString(ssnDateVerified)).append("\n");
    sb.append("    ssnNotes: ").append(toIndentedString(ssnNotes)).append("\n");
    sb.append("    visaType: ").append(toIndentedString(visaType)).append("\n");
    sb.append("    workAuthorization: ").append(toIndentedString(workAuthorization)).append("\n");
    sb.append("    workUntil: ").append(toIndentedString(workUntil)).append("\n");
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
    openapiFields.add("alienOrAdmissionDocumentNumber");
    openapiFields.add("attestedDate");
    openapiFields.add("countryOfIssuance");
    openapiFields.add("foreignPassportNumber");
    openapiFields.add("i94AdmissionNumber");
    openapiFields.add("i9DateVerified");
    openapiFields.add("i9Notes");
    openapiFields.add("isI9Verified");
    openapiFields.add("isSsnVerified");
    openapiFields.add("ssnDateVerified");
    openapiFields.add("ssnNotes");
    openapiFields.add("visaType");
    openapiFields.add("workAuthorization");
    openapiFields.add("workUntil");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StagedEmployeeWorkEligibilityInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StagedEmployeeWorkEligibilityInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StagedEmployeeWorkEligibilityInner is not found in the empty JSON string", StagedEmployeeWorkEligibilityInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StagedEmployeeWorkEligibilityInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StagedEmployeeWorkEligibilityInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("alienOrAdmissionDocumentNumber") != null && !jsonObj.get("alienOrAdmissionDocumentNumber").isJsonNull()) && !jsonObj.get("alienOrAdmissionDocumentNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `alienOrAdmissionDocumentNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("alienOrAdmissionDocumentNumber").toString()));
      }
      if ((jsonObj.get("attestedDate") != null && !jsonObj.get("attestedDate").isJsonNull()) && !jsonObj.get("attestedDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `attestedDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("attestedDate").toString()));
      }
      if ((jsonObj.get("countryOfIssuance") != null && !jsonObj.get("countryOfIssuance").isJsonNull()) && !jsonObj.get("countryOfIssuance").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `countryOfIssuance` to be a primitive type in the JSON string but got `%s`", jsonObj.get("countryOfIssuance").toString()));
      }
      if ((jsonObj.get("foreignPassportNumber") != null && !jsonObj.get("foreignPassportNumber").isJsonNull()) && !jsonObj.get("foreignPassportNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `foreignPassportNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("foreignPassportNumber").toString()));
      }
      if ((jsonObj.get("i94AdmissionNumber") != null && !jsonObj.get("i94AdmissionNumber").isJsonNull()) && !jsonObj.get("i94AdmissionNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `i94AdmissionNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("i94AdmissionNumber").toString()));
      }
      if ((jsonObj.get("i9DateVerified") != null && !jsonObj.get("i9DateVerified").isJsonNull()) && !jsonObj.get("i9DateVerified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `i9DateVerified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("i9DateVerified").toString()));
      }
      if ((jsonObj.get("i9Notes") != null && !jsonObj.get("i9Notes").isJsonNull()) && !jsonObj.get("i9Notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `i9Notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("i9Notes").toString()));
      }
      if ((jsonObj.get("ssnDateVerified") != null && !jsonObj.get("ssnDateVerified").isJsonNull()) && !jsonObj.get("ssnDateVerified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssnDateVerified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssnDateVerified").toString()));
      }
      if ((jsonObj.get("ssnNotes") != null && !jsonObj.get("ssnNotes").isJsonNull()) && !jsonObj.get("ssnNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssnNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssnNotes").toString()));
      }
      if ((jsonObj.get("visaType") != null && !jsonObj.get("visaType").isJsonNull()) && !jsonObj.get("visaType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `visaType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("visaType").toString()));
      }
      if ((jsonObj.get("workAuthorization") != null && !jsonObj.get("workAuthorization").isJsonNull()) && !jsonObj.get("workAuthorization").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workAuthorization` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workAuthorization").toString()));
      }
      if ((jsonObj.get("workUntil") != null && !jsonObj.get("workUntil").isJsonNull()) && !jsonObj.get("workUntil").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workUntil` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workUntil").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StagedEmployeeWorkEligibilityInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StagedEmployeeWorkEligibilityInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StagedEmployeeWorkEligibilityInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StagedEmployeeWorkEligibilityInner.class));

       return (TypeAdapter<T>) new TypeAdapter<StagedEmployeeWorkEligibilityInner>() {
           @Override
           public void write(JsonWriter out, StagedEmployeeWorkEligibilityInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StagedEmployeeWorkEligibilityInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StagedEmployeeWorkEligibilityInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StagedEmployeeWorkEligibilityInner
   * @throws IOException if the JSON string is invalid with respect to StagedEmployeeWorkEligibilityInner
   */
  public static StagedEmployeeWorkEligibilityInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StagedEmployeeWorkEligibilityInner.class);
  }

  /**
   * Convert an instance of StagedEmployeeWorkEligibilityInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

