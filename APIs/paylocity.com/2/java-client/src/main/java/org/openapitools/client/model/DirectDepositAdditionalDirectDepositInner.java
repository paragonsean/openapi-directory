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
 * The additional direct deposit model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DirectDepositAdditionalDirectDepositInner {
  public static final String SERIALIZED_NAME_ACCOUNT_NUMBER = "accountNumber";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_NUMBER)
  private String accountNumber;

  public static final String SERIALIZED_NAME_ACCOUNT_TYPE = "accountType";
  @SerializedName(SERIALIZED_NAME_ACCOUNT_TYPE)
  private String accountType;

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_AMOUNT_TYPE = "amountType";
  @SerializedName(SERIALIZED_NAME_AMOUNT_TYPE)
  private String amountType;

  public static final String SERIALIZED_NAME_BLOCK_SPECIAL = "blockSpecial";
  @SerializedName(SERIALIZED_NAME_BLOCK_SPECIAL)
  private Boolean blockSpecial;

  public static final String SERIALIZED_NAME_IS_SKIP_PRE_NOTE = "isSkipPreNote";
  @SerializedName(SERIALIZED_NAME_IS_SKIP_PRE_NOTE)
  private Boolean isSkipPreNote;

  public static final String SERIALIZED_NAME_NAME_ON_ACCOUNT = "nameOnAccount";
  @SerializedName(SERIALIZED_NAME_NAME_ON_ACCOUNT)
  private String nameOnAccount;

  public static final String SERIALIZED_NAME_PRE_NOTE_DATE = "preNoteDate";
  @SerializedName(SERIALIZED_NAME_PRE_NOTE_DATE)
  private String preNoteDate;

  public static final String SERIALIZED_NAME_ROUTING_NUMBER = "routingNumber";
  @SerializedName(SERIALIZED_NAME_ROUTING_NUMBER)
  private String routingNumber;

  public DirectDepositAdditionalDirectDepositInner() {
  }

  public DirectDepositAdditionalDirectDepositInner accountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
    return this;
  }

  /**
   * Account number, entered without special characters and spaces. &lt;br  /&gt;Max length: 17&lt;br /&gt;
   * @return accountNumber
   */
  @javax.annotation.Nullable
  public String getAccountNumber() {
    return accountNumber;
  }

  public void setAccountNumber(String accountNumber) {
    this.accountNumber = accountNumber;
  }


  public DirectDepositAdditionalDirectDepositInner accountType(String accountType) {
    this.accountType = accountType;
    return this;
  }

  /**
   * Account type. Valid values are *C* (Checking), *S* (Saving), *P* (Pay Card). &lt;br   /&gt;Max length: 1&lt;br /&gt;
   * @return accountType
   */
  @javax.annotation.Nullable
  public String getAccountType() {
    return accountType;
  }

  public void setAccountType(String accountType) {
    this.accountType = accountType;
  }


  public DirectDepositAdditionalDirectDepositInner amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Amount value to be deposited to the account.&lt;br  /&gt;Decimal (12,2)&lt;br /&gt;
   * @return amount
   */
  @javax.annotation.Nullable
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public DirectDepositAdditionalDirectDepositInner amountType(String amountType) {
    this.amountType = amountType;
    return this;
  }

  /**
   * Amount type to indicate the context of the amount. Common values are *F* (FLAT), *F-* (Net Minus), *P* (Percent). &lt;br  /&gt; Max length: 5&lt;br /&gt;
   * @return amountType
   */
  @javax.annotation.Nullable
  public String getAmountType() {
    return amountType;
  }

  public void setAmountType(String amountType) {
    this.amountType = amountType;
  }


  public DirectDepositAdditionalDirectDepositInner blockSpecial(Boolean blockSpecial) {
    this.blockSpecial = blockSpecial;
    return this;
  }

  /**
   * Indicates if direct deposit should be blocked when special check types such as Bonus are processed.&lt;br /&gt;
   * @return blockSpecial
   */
  @javax.annotation.Nullable
  public Boolean getBlockSpecial() {
    return blockSpecial;
  }

  public void setBlockSpecial(Boolean blockSpecial) {
    this.blockSpecial = blockSpecial;
  }


  public DirectDepositAdditionalDirectDepositInner isSkipPreNote(Boolean isSkipPreNote) {
    this.isSkipPreNote = isSkipPreNote;
    return this;
  }

  /**
   * Indicates if account will not pre-note.&lt;br /&gt;
   * @return isSkipPreNote
   */
  @javax.annotation.Nullable
  public Boolean getIsSkipPreNote() {
    return isSkipPreNote;
  }

  public void setIsSkipPreNote(Boolean isSkipPreNote) {
    this.isSkipPreNote = isSkipPreNote;
  }


  public DirectDepositAdditionalDirectDepositInner nameOnAccount(String nameOnAccount) {
    this.nameOnAccount = nameOnAccount;
    return this;
  }

  /**
   * Name on the bank account. Defaults to employee&#39;s name. &lt;br  /&gt;Max length: 30&lt;br /&gt;
   * @return nameOnAccount
   */
  @javax.annotation.Nullable
  public String getNameOnAccount() {
    return nameOnAccount;
  }

  public void setNameOnAccount(String nameOnAccount) {
    this.nameOnAccount = nameOnAccount;
  }


  public DirectDepositAdditionalDirectDepositInner preNoteDate(String preNoteDate) {
    this.preNoteDate = preNoteDate;
    return this;
  }

  /**
   * Date to end the pre-note of the account. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.&lt;br /&gt;
   * @return preNoteDate
   */
  @javax.annotation.Nullable
  public String getPreNoteDate() {
    return preNoteDate;
  }

  public void setPreNoteDate(String preNoteDate) {
    this.preNoteDate = preNoteDate;
  }


  public DirectDepositAdditionalDirectDepositInner routingNumber(String routingNumber) {
    this.routingNumber = routingNumber;
    return this;
  }

  /**
   * ABA Transit Routing Number, entered without dashes or spaces. &lt;br  /&gt;Max length: 9&lt;br /&gt;
   * @return routingNumber
   */
  @javax.annotation.Nullable
  public String getRoutingNumber() {
    return routingNumber;
  }

  public void setRoutingNumber(String routingNumber) {
    this.routingNumber = routingNumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DirectDepositAdditionalDirectDepositInner directDepositAdditionalDirectDepositInner = (DirectDepositAdditionalDirectDepositInner) o;
    return Objects.equals(this.accountNumber, directDepositAdditionalDirectDepositInner.accountNumber) &&
        Objects.equals(this.accountType, directDepositAdditionalDirectDepositInner.accountType) &&
        Objects.equals(this.amount, directDepositAdditionalDirectDepositInner.amount) &&
        Objects.equals(this.amountType, directDepositAdditionalDirectDepositInner.amountType) &&
        Objects.equals(this.blockSpecial, directDepositAdditionalDirectDepositInner.blockSpecial) &&
        Objects.equals(this.isSkipPreNote, directDepositAdditionalDirectDepositInner.isSkipPreNote) &&
        Objects.equals(this.nameOnAccount, directDepositAdditionalDirectDepositInner.nameOnAccount) &&
        Objects.equals(this.preNoteDate, directDepositAdditionalDirectDepositInner.preNoteDate) &&
        Objects.equals(this.routingNumber, directDepositAdditionalDirectDepositInner.routingNumber);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(accountNumber, accountType, amount, amountType, blockSpecial, isSkipPreNote, nameOnAccount, preNoteDate, routingNumber);
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
    sb.append("class DirectDepositAdditionalDirectDepositInner {\n");
    sb.append("    accountNumber: ").append(toIndentedString(accountNumber)).append("\n");
    sb.append("    accountType: ").append(toIndentedString(accountType)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    amountType: ").append(toIndentedString(amountType)).append("\n");
    sb.append("    blockSpecial: ").append(toIndentedString(blockSpecial)).append("\n");
    sb.append("    isSkipPreNote: ").append(toIndentedString(isSkipPreNote)).append("\n");
    sb.append("    nameOnAccount: ").append(toIndentedString(nameOnAccount)).append("\n");
    sb.append("    preNoteDate: ").append(toIndentedString(preNoteDate)).append("\n");
    sb.append("    routingNumber: ").append(toIndentedString(routingNumber)).append("\n");
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
    openapiFields.add("accountNumber");
    openapiFields.add("accountType");
    openapiFields.add("amount");
    openapiFields.add("amountType");
    openapiFields.add("blockSpecial");
    openapiFields.add("isSkipPreNote");
    openapiFields.add("nameOnAccount");
    openapiFields.add("preNoteDate");
    openapiFields.add("routingNumber");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DirectDepositAdditionalDirectDepositInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DirectDepositAdditionalDirectDepositInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DirectDepositAdditionalDirectDepositInner is not found in the empty JSON string", DirectDepositAdditionalDirectDepositInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DirectDepositAdditionalDirectDepositInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DirectDepositAdditionalDirectDepositInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("accountNumber") != null && !jsonObj.get("accountNumber").isJsonNull()) && !jsonObj.get("accountNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountNumber").toString()));
      }
      if ((jsonObj.get("accountType") != null && !jsonObj.get("accountType").isJsonNull()) && !jsonObj.get("accountType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `accountType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("accountType").toString()));
      }
      if ((jsonObj.get("amountType") != null && !jsonObj.get("amountType").isJsonNull()) && !jsonObj.get("amountType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `amountType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("amountType").toString()));
      }
      if ((jsonObj.get("nameOnAccount") != null && !jsonObj.get("nameOnAccount").isJsonNull()) && !jsonObj.get("nameOnAccount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nameOnAccount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nameOnAccount").toString()));
      }
      if ((jsonObj.get("preNoteDate") != null && !jsonObj.get("preNoteDate").isJsonNull()) && !jsonObj.get("preNoteDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preNoteDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preNoteDate").toString()));
      }
      if ((jsonObj.get("routingNumber") != null && !jsonObj.get("routingNumber").isJsonNull()) && !jsonObj.get("routingNumber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `routingNumber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("routingNumber").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DirectDepositAdditionalDirectDepositInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DirectDepositAdditionalDirectDepositInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DirectDepositAdditionalDirectDepositInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DirectDepositAdditionalDirectDepositInner.class));

       return (TypeAdapter<T>) new TypeAdapter<DirectDepositAdditionalDirectDepositInner>() {
           @Override
           public void write(JsonWriter out, DirectDepositAdditionalDirectDepositInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DirectDepositAdditionalDirectDepositInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DirectDepositAdditionalDirectDepositInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DirectDepositAdditionalDirectDepositInner
   * @throws IOException if the JSON string is invalid with respect to DirectDepositAdditionalDirectDepositInner
   */
  public static DirectDepositAdditionalDirectDepositInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DirectDepositAdditionalDirectDepositInner.class);
  }

  /**
   * Convert an instance of DirectDepositAdditionalDirectDepositInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

