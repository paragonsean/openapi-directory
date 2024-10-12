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
 * The additional pay rate model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AdditionalRate {
  public static final String SERIALIZED_NAME_CHANGE_REASON = "changeReason";
  @SerializedName(SERIALIZED_NAME_CHANGE_REASON)
  private String changeReason;

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

  public static final String SERIALIZED_NAME_END_CHECK_DATE = "endCheckDate";
  @SerializedName(SERIALIZED_NAME_END_CHECK_DATE)
  private String endCheckDate;

  public static final String SERIALIZED_NAME_JOB = "job";
  @SerializedName(SERIALIZED_NAME_JOB)
  private String job;

  public static final String SERIALIZED_NAME_RATE = "rate";
  @SerializedName(SERIALIZED_NAME_RATE)
  private BigDecimal rate;

  public static final String SERIALIZED_NAME_RATE_CODE = "rateCode";
  @SerializedName(SERIALIZED_NAME_RATE_CODE)
  private String rateCode;

  public static final String SERIALIZED_NAME_RATE_NOTES = "rateNotes";
  @SerializedName(SERIALIZED_NAME_RATE_NOTES)
  private String rateNotes;

  public static final String SERIALIZED_NAME_RATE_PER = "ratePer";
  @SerializedName(SERIALIZED_NAME_RATE_PER)
  private String ratePer;

  public static final String SERIALIZED_NAME_SHIFT = "shift";
  @SerializedName(SERIALIZED_NAME_SHIFT)
  private String shift;

  public AdditionalRate() {
  }

  public AdditionalRate changeReason(String changeReason) {
    this.changeReason = changeReason;
    return this;
  }

  /**
   * Not required. If populated, must match one of the system coded values available in the Additional Rates Change Reason drop down.&lt;br /&gt;
   * @return changeReason
   */
  @javax.annotation.Nullable
  public String getChangeReason() {
    return changeReason;
  }

  public void setChangeReason(String changeReason) {
    this.changeReason = changeReason;
  }


  public AdditionalRate costCenter1(String costCenter1) {
    this.costCenter1 = costCenter1;
    return this;
  }

  /**
   * Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 1 drop down. This cell must be in a text format.&lt;br /&gt;
   * @return costCenter1
   */
  @javax.annotation.Nullable
  public String getCostCenter1() {
    return costCenter1;
  }

  public void setCostCenter1(String costCenter1) {
    this.costCenter1 = costCenter1;
  }


  public AdditionalRate costCenter2(String costCenter2) {
    this.costCenter2 = costCenter2;
    return this;
  }

  /**
   * Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 2 drop down. This cell must be in a text format.&lt;br /&gt;
   * @return costCenter2
   */
  @javax.annotation.Nullable
  public String getCostCenter2() {
    return costCenter2;
  }

  public void setCostCenter2(String costCenter2) {
    this.costCenter2 = costCenter2;
  }


  public AdditionalRate costCenter3(String costCenter3) {
    this.costCenter3 = costCenter3;
    return this;
  }

  /**
   * Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 3 drop down. This cell must be in a text format.&lt;br /&gt;
   * @return costCenter3
   */
  @javax.annotation.Nullable
  public String getCostCenter3() {
    return costCenter3;
  }

  public void setCostCenter3(String costCenter3) {
    this.costCenter3 = costCenter3;
  }


  public AdditionalRate effectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
    return this;
  }

  /**
   * Required. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.&lt;br /&gt;
   * @return effectiveDate
   */
  @javax.annotation.Nullable
  public String getEffectiveDate() {
    return effectiveDate;
  }

  public void setEffectiveDate(String effectiveDate) {
    this.effectiveDate = effectiveDate;
  }


  public AdditionalRate endCheckDate(String endCheckDate) {
    this.endCheckDate = endCheckDate;
    return this;
  }

  /**
   * Not required. Must match one of the system coded check dates available in the Additional Rates End Check Date drop down. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.&lt;br /&gt;
   * @return endCheckDate
   */
  @javax.annotation.Nullable
  public String getEndCheckDate() {
    return endCheckDate;
  }

  public void setEndCheckDate(String endCheckDate) {
    this.endCheckDate = endCheckDate;
  }


  public AdditionalRate job(String job) {
    this.job = job;
    return this;
  }

  /**
   * Not required. If populated, must match one of the system coded values available in the Additional Rates Job drop down.&lt;br /&gt;
   * @return job
   */
  @javax.annotation.Nullable
  public String getJob() {
    return job;
  }

  public void setJob(String job) {
    this.job = job;
  }


  public AdditionalRate rate(BigDecimal rate) {
    this.rate = rate;
    return this;
  }

  /**
   * Required. Enter dollar amount that corresponds to the Per selection.&lt;br /&gt;
   * @return rate
   */
  @javax.annotation.Nullable
  public BigDecimal getRate() {
    return rate;
  }

  public void setRate(BigDecimal rate) {
    this.rate = rate;
  }


  public AdditionalRate rateCode(String rateCode) {
    this.rateCode = rateCode;
    return this;
  }

  /**
   * Required. If populated, must match one of the system coded values available in the Additional Rates Rate Code drop down.&lt;br /&gt;
   * @return rateCode
   */
  @javax.annotation.Nullable
  public String getRateCode() {
    return rateCode;
  }

  public void setRateCode(String rateCode) {
    this.rateCode = rateCode;
  }


  public AdditionalRate rateNotes(String rateNotes) {
    this.rateNotes = rateNotes;
    return this;
  }

  /**
   * Not required.&lt;br  /&gt;Max length: 4000&lt;br /&gt;
   * @return rateNotes
   */
  @javax.annotation.Nullable
  public String getRateNotes() {
    return rateNotes;
  }

  public void setRateNotes(String rateNotes) {
    this.rateNotes = rateNotes;
  }


  public AdditionalRate ratePer(String ratePer) {
    this.ratePer = ratePer;
    return this;
  }

  /**
   * Required. Valid values are HOUR or WEEK.&lt;br /&gt;
   * @return ratePer
   */
  @javax.annotation.Nullable
  public String getRatePer() {
    return ratePer;
  }

  public void setRatePer(String ratePer) {
    this.ratePer = ratePer;
  }


  public AdditionalRate shift(String shift) {
    this.shift = shift;
    return this;
  }

  /**
   * Not required. If populated, must match one of the system coded values available in the Additional Rates Shift drop down.&lt;br /&gt;
   * @return shift
   */
  @javax.annotation.Nullable
  public String getShift() {
    return shift;
  }

  public void setShift(String shift) {
    this.shift = shift;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdditionalRate additionalRate = (AdditionalRate) o;
    return Objects.equals(this.changeReason, additionalRate.changeReason) &&
        Objects.equals(this.costCenter1, additionalRate.costCenter1) &&
        Objects.equals(this.costCenter2, additionalRate.costCenter2) &&
        Objects.equals(this.costCenter3, additionalRate.costCenter3) &&
        Objects.equals(this.effectiveDate, additionalRate.effectiveDate) &&
        Objects.equals(this.endCheckDate, additionalRate.endCheckDate) &&
        Objects.equals(this.job, additionalRate.job) &&
        Objects.equals(this.rate, additionalRate.rate) &&
        Objects.equals(this.rateCode, additionalRate.rateCode) &&
        Objects.equals(this.rateNotes, additionalRate.rateNotes) &&
        Objects.equals(this.ratePer, additionalRate.ratePer) &&
        Objects.equals(this.shift, additionalRate.shift);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(changeReason, costCenter1, costCenter2, costCenter3, effectiveDate, endCheckDate, job, rate, rateCode, rateNotes, ratePer, shift);
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
    sb.append("class AdditionalRate {\n");
    sb.append("    changeReason: ").append(toIndentedString(changeReason)).append("\n");
    sb.append("    costCenter1: ").append(toIndentedString(costCenter1)).append("\n");
    sb.append("    costCenter2: ").append(toIndentedString(costCenter2)).append("\n");
    sb.append("    costCenter3: ").append(toIndentedString(costCenter3)).append("\n");
    sb.append("    effectiveDate: ").append(toIndentedString(effectiveDate)).append("\n");
    sb.append("    endCheckDate: ").append(toIndentedString(endCheckDate)).append("\n");
    sb.append("    job: ").append(toIndentedString(job)).append("\n");
    sb.append("    rate: ").append(toIndentedString(rate)).append("\n");
    sb.append("    rateCode: ").append(toIndentedString(rateCode)).append("\n");
    sb.append("    rateNotes: ").append(toIndentedString(rateNotes)).append("\n");
    sb.append("    ratePer: ").append(toIndentedString(ratePer)).append("\n");
    sb.append("    shift: ").append(toIndentedString(shift)).append("\n");
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
    openapiFields.add("costCenter1");
    openapiFields.add("costCenter2");
    openapiFields.add("costCenter3");
    openapiFields.add("effectiveDate");
    openapiFields.add("endCheckDate");
    openapiFields.add("job");
    openapiFields.add("rate");
    openapiFields.add("rateCode");
    openapiFields.add("rateNotes");
    openapiFields.add("ratePer");
    openapiFields.add("shift");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AdditionalRate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AdditionalRate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AdditionalRate is not found in the empty JSON string", AdditionalRate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AdditionalRate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AdditionalRate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("changeReason") != null && !jsonObj.get("changeReason").isJsonNull()) && !jsonObj.get("changeReason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `changeReason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("changeReason").toString()));
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
      if ((jsonObj.get("endCheckDate") != null && !jsonObj.get("endCheckDate").isJsonNull()) && !jsonObj.get("endCheckDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `endCheckDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("endCheckDate").toString()));
      }
      if ((jsonObj.get("job") != null && !jsonObj.get("job").isJsonNull()) && !jsonObj.get("job").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `job` to be a primitive type in the JSON string but got `%s`", jsonObj.get("job").toString()));
      }
      if ((jsonObj.get("rateCode") != null && !jsonObj.get("rateCode").isJsonNull()) && !jsonObj.get("rateCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rateCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rateCode").toString()));
      }
      if ((jsonObj.get("rateNotes") != null && !jsonObj.get("rateNotes").isJsonNull()) && !jsonObj.get("rateNotes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rateNotes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rateNotes").toString()));
      }
      if ((jsonObj.get("ratePer") != null && !jsonObj.get("ratePer").isJsonNull()) && !jsonObj.get("ratePer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ratePer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ratePer").toString()));
      }
      if ((jsonObj.get("shift") != null && !jsonObj.get("shift").isJsonNull()) && !jsonObj.get("shift").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shift` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shift").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AdditionalRate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AdditionalRate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AdditionalRate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AdditionalRate.class));

       return (TypeAdapter<T>) new TypeAdapter<AdditionalRate>() {
           @Override
           public void write(JsonWriter out, AdditionalRate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AdditionalRate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AdditionalRate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AdditionalRate
   * @throws IOException if the JSON string is invalid with respect to AdditionalRate
   */
  public static AdditionalRate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AdditionalRate.class);
  }

  /**
   * Convert an instance of AdditionalRate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

