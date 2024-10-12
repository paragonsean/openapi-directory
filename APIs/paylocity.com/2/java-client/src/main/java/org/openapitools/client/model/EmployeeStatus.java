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
 * Add or update employee status, change reason, effective date, and adjusted seniority date. Note that companies that are still in Implementation cannot hire future employees.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EmployeeStatus {
  public static final String SERIALIZED_NAME_ADJUSTED_SENIORITY_DATE = "adjustedSeniorityDate";
  @SerializedName(SERIALIZED_NAME_ADJUSTED_SENIORITY_DATE)
  private String adjustedSeniorityDate;

  public static final String SERIALIZED_NAME_CHANGE_REASON = "changeReason";
  @SerializedName(SERIALIZED_NAME_CHANGE_REASON)
  private String changeReason;

  public static final String SERIALIZED_NAME_EFFECTIVE_DATE = "effectiveDate";
  @SerializedName(SERIALIZED_NAME_EFFECTIVE_DATE)
  private String effectiveDate;

  public static final String SERIALIZED_NAME_EMPLOYEE_STATUS = "employeeStatus";
  @SerializedName(SERIALIZED_NAME_EMPLOYEE_STATUS)
  private String employeeStatus;

  public static final String SERIALIZED_NAME_HIRE_DATE = "hireDate";
  @SerializedName(SERIALIZED_NAME_HIRE_DATE)
  private String hireDate;

  public static final String SERIALIZED_NAME_IS_ELIGIBLE_FOR_REHIRE = "isEligibleForRehire";
  @SerializedName(SERIALIZED_NAME_IS_ELIGIBLE_FOR_REHIRE)
  private Boolean isEligibleForRehire;

  public static final String SERIALIZED_NAME_RE_HIRE_DATE = "reHireDate";
  @SerializedName(SERIALIZED_NAME_RE_HIRE_DATE)
  private String reHireDate;

  public static final String SERIALIZED_NAME_STATUS_TYPE = "statusType";
  @SerializedName(SERIALIZED_NAME_STATUS_TYPE)
  private String statusType;

  public static final String SERIALIZED_NAME_TERMINATION_DATE = "terminationDate";
  @SerializedName(SERIALIZED_NAME_TERMINATION_DATE)
  private String terminationDate;

  public EmployeeStatus() {
  }

  public EmployeeStatus adjustedSeniorityDate(String adjustedSeniorityDate) {
    this.adjustedSeniorityDate = adjustedSeniorityDate;
    return this;
  }

  /**
   * Adjusted seniority date. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return adjustedSeniorityDate
   */
  @javax.annotation.Nullable
  public String getAdjustedSeniorityDate() {
    return adjustedSeniorityDate;
  }

  public void setAdjustedSeniorityDate(String adjustedSeniorityDate) {
    this.adjustedSeniorityDate = adjustedSeniorityDate;
  }


  public EmployeeStatus changeReason(String changeReason) {
    this.changeReason = changeReason;
    return this;
  }

  /**
   * Employee status change reason. Must match Company setup.&lt;br  /&gt; Max length: 15
   * @return changeReason
   */
  @javax.annotation.Nullable
  public String getChangeReason() {
    return changeReason;
  }

  public void setChangeReason(String changeReason) {
    this.changeReason = changeReason;
  }


  public EmployeeStatus effectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
    return this;
  }

  /**
   * Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return effectiveDate
   */
  @javax.annotation.Nullable
  public String getEffectiveDate() {
    return effectiveDate;
  }

  public void setEffectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
  }


  public EmployeeStatus employeeStatus(String employeeStatus) {
    this.employeeStatus = employeeStatus;
    return this;
  }

  /**
   * Employee current work status. Common values are *A* (Active), *L* (Leave of Absence), *T* (Terminated). &lt;br  /&gt;Max length: 20
   * @return employeeStatus
   */
  @javax.annotation.Nullable
  public String getEmployeeStatus() {
    return employeeStatus;
  }

  public void setEmployeeStatus(String employeeStatus) {
    this.employeeStatus = employeeStatus;
  }


  public EmployeeStatus hireDate(String hireDate) {
    this.hireDate = hireDate;
    return this;
  }

  /**
   * Employee hired date. Updates to hire date are not allowed and will be ignored. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return hireDate
   */
  @javax.annotation.Nullable
  public String getHireDate() {
    return hireDate;
  }

  public void setHireDate(String hireDate) {
    this.hireDate = hireDate;
  }


  public EmployeeStatus isEligibleForRehire(Boolean isEligibleForRehire) {
    this.isEligibleForRehire = isEligibleForRehire;
    return this;
  }

  /**
   * Indicates if employee eligible for rehire.
   * @return isEligibleForRehire
   */
  @javax.annotation.Nullable
  public Boolean getIsEligibleForRehire() {
    return isEligibleForRehire;
  }

  public void setIsEligibleForRehire(Boolean isEligibleForRehire) {
    this.isEligibleForRehire = isEligibleForRehire;
  }


  public EmployeeStatus reHireDate(String reHireDate) {
    this.reHireDate = reHireDate;
    return this;
  }

  /**
   * Rehire date if employee is rehired.  Updates to re-hire date are not allowed and will be ignored. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
   * @return reHireDate
   */
  @javax.annotation.Nullable
  public String getReHireDate() {
    return reHireDate;
  }

  public void setReHireDate(String reHireDate) {
    this.reHireDate = reHireDate;
  }


  public EmployeeStatus statusType(String statusType) {
    this.statusType = statusType;
    return this;
  }

  /**
   * The Status Type associated with the Employee Status code. Each Employee Status  code for a company is assigned to one of the Status Type values of  A (Active), L (Leave of Absence), T (Terminated).
   * @return statusType
   */
  @javax.annotation.Nullable
  public String getStatusType() {
    return statusType;
  }

  public void setStatusType(String statusType) {
    this.statusType = statusType;
  }


  public EmployeeStatus terminationDate(String terminationDate) {
    this.terminationDate = terminationDate;
    return this;
  }

  /**
   * Employee termination date. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
   * @return terminationDate
   */
  @javax.annotation.Nullable
  public String getTerminationDate() {
    return terminationDate;
  }

  public void setTerminationDate(String terminationDate) {
    this.terminationDate = terminationDate;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EmployeeStatus employeeStatus = (EmployeeStatus) o;
    return Objects.equals(this.adjustedSeniorityDate, employeeStatus.adjustedSeniorityDate) &&
        Objects.equals(this.changeReason, employeeStatus.changeReason) &&
        Objects.equals(this.effectiveDate, employeeStatus.effectiveDate) &&
        Objects.equals(this.employeeStatus, employeeStatus.employeeStatus) &&
        Objects.equals(this.hireDate, employeeStatus.hireDate) &&
        Objects.equals(this.isEligibleForRehire, employeeStatus.isEligibleForRehire) &&
        Objects.equals(this.reHireDate, employeeStatus.reHireDate) &&
        Objects.equals(this.statusType, employeeStatus.statusType) &&
        Objects.equals(this.terminationDate, employeeStatus.terminationDate);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(adjustedSeniorityDate, changeReason, effectiveDate, employeeStatus, hireDate, isEligibleForRehire, reHireDate, statusType, terminationDate);
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
    sb.append("class EmployeeStatus {\n");
    sb.append("    adjustedSeniorityDate: ").append(toIndentedString(adjustedSeniorityDate)).append("\n");
    sb.append("    changeReason: ").append(toIndentedString(changeReason)).append("\n");
    sb.append("    effectiveDate: ").append(toIndentedString(effectiveDate)).append("\n");
    sb.append("    employeeStatus: ").append(toIndentedString(employeeStatus)).append("\n");
    sb.append("    hireDate: ").append(toIndentedString(hireDate)).append("\n");
    sb.append("    isEligibleForRehire: ").append(toIndentedString(isEligibleForRehire)).append("\n");
    sb.append("    reHireDate: ").append(toIndentedString(reHireDate)).append("\n");
    sb.append("    statusType: ").append(toIndentedString(statusType)).append("\n");
    sb.append("    terminationDate: ").append(toIndentedString(terminationDate)).append("\n");
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
    openapiFields.add("adjustedSeniorityDate");
    openapiFields.add("changeReason");
    openapiFields.add("effectiveDate");
    openapiFields.add("employeeStatus");
    openapiFields.add("hireDate");
    openapiFields.add("isEligibleForRehire");
    openapiFields.add("reHireDate");
    openapiFields.add("statusType");
    openapiFields.add("terminationDate");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EmployeeStatus
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EmployeeStatus.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EmployeeStatus is not found in the empty JSON string", EmployeeStatus.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EmployeeStatus.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EmployeeStatus` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("adjustedSeniorityDate") != null && !jsonObj.get("adjustedSeniorityDate").isJsonNull()) && !jsonObj.get("adjustedSeniorityDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `adjustedSeniorityDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("adjustedSeniorityDate").toString()));
      }
      if ((jsonObj.get("changeReason") != null && !jsonObj.get("changeReason").isJsonNull()) && !jsonObj.get("changeReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `changeReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("changeReason").toString()));
      }
      if ((jsonObj.get("effectiveDate") != null && !jsonObj.get("effectiveDate").isJsonNull()) && !jsonObj.get("effectiveDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `effectiveDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("effectiveDate").toString()));
      }
      if ((jsonObj.get("employeeStatus") != null && !jsonObj.get("employeeStatus").isJsonNull()) && !jsonObj.get("employeeStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employeeStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employeeStatus").toString()));
      }
      if ((jsonObj.get("hireDate") != null && !jsonObj.get("hireDate").isJsonNull()) && !jsonObj.get("hireDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `hireDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("hireDate").toString()));
      }
      if ((jsonObj.get("reHireDate") != null && !jsonObj.get("reHireDate").isJsonNull()) && !jsonObj.get("reHireDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reHireDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reHireDate").toString()));
      }
      if ((jsonObj.get("statusType") != null && !jsonObj.get("statusType").isJsonNull()) && !jsonObj.get("statusType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `statusType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("statusType").toString()));
      }
      if ((jsonObj.get("terminationDate") != null && !jsonObj.get("terminationDate").isJsonNull()) && !jsonObj.get("terminationDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `terminationDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("terminationDate").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EmployeeStatus.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EmployeeStatus' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EmployeeStatus> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EmployeeStatus.class));

       return (TypeAdapter<T>) new TypeAdapter<EmployeeStatus>() {
           @Override
           public void write(JsonWriter out, EmployeeStatus value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EmployeeStatus read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EmployeeStatus given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EmployeeStatus
   * @throws IOException if the JSON string is invalid with respect to EmployeeStatus
   */
  public static EmployeeStatus fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EmployeeStatus.class);
  }

  /**
   * Convert an instance of EmployeeStatus to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

