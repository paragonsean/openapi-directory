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
 * The address model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:32:18.209750-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class StagedEmployeeWorkAddressInner {
  public static final String SERIALIZED_NAME_ADDRESS1 = "address1";
  @SerializedName(SERIALIZED_NAME_ADDRESS1)
  private String address1;

  public static final String SERIALIZED_NAME_ADDRESS2 = "address2";
  @SerializedName(SERIALIZED_NAME_ADDRESS2)
  private String address2;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_COUNTY = "county";
  @SerializedName(SERIALIZED_NAME_COUNTY)
  private String county;

  public static final String SERIALIZED_NAME_EMAIL_ADDRESS = "emailAddress";
  @SerializedName(SERIALIZED_NAME_EMAIL_ADDRESS)
  private String emailAddress;

  public static final String SERIALIZED_NAME_MOBILE_PHONE = "mobilePhone";
  @SerializedName(SERIALIZED_NAME_MOBILE_PHONE)
  private String mobilePhone;

  public static final String SERIALIZED_NAME_PAGER = "pager";
  @SerializedName(SERIALIZED_NAME_PAGER)
  private String pager;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_PHONE_EXTENSION = "phoneExtension";
  @SerializedName(SERIALIZED_NAME_PHONE_EXTENSION)
  private String phoneExtension;

  public static final String SERIALIZED_NAME_POSTAL_CODE = "postalCode";
  @SerializedName(SERIALIZED_NAME_POSTAL_CODE)
  private String postalCode;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private String state;

  public StagedEmployeeWorkAddressInner() {
  }

  public StagedEmployeeWorkAddressInner address1(String address1) {
    this.address1 = address1;
    return this;
  }

  /**
   * 1st address line.&lt;br  /&gt; Max length: 40
   * @return address1
   */
  @javax.annotation.Nullable
  public String getAddress1() {
    return address1;
  }

  public void setAddress1(String address1) {
    this.address1 = address1;
  }


  public StagedEmployeeWorkAddressInner address2(String address2) {
    this.address2 = address2;
    return this;
  }

  /**
   * 2nd address line. &lt;br  /&gt; Max length: 40
   * @return address2
   */
  @javax.annotation.Nullable
  public String getAddress2() {
    return address2;
  }

  public void setAddress2(String address2) {
    this.address2 = address2;
  }


  public StagedEmployeeWorkAddressInner city(String city) {
    this.city = city;
    return this;
  }

  /**
   * City.&lt;br  /&gt; Max length: 40
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public StagedEmployeeWorkAddressInner country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Country.&lt;br  /&gt; Max length: 30
   * @return country
   */
  @javax.annotation.Nullable
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public StagedEmployeeWorkAddressInner county(String county) {
    this.county = county;
    return this;
  }

  /**
   * County.&lt;br  /&gt; Max length: 30
   * @return county
   */
  @javax.annotation.Nullable
  public String getCounty() {
    return county;
  }

  public void setCounty(String county) {
    this.county = county;
  }


  public StagedEmployeeWorkAddressInner emailAddress(String emailAddress) {
    this.emailAddress = emailAddress;
    return this;
  }

  /**
   * Email. &lt;br  /&gt;Max length: 50
   * @return emailAddress
   */
  @javax.annotation.Nullable
  public String getEmailAddress() {
    return emailAddress;
  }

  public void setEmailAddress(String emailAddress) {
    this.emailAddress = emailAddress;
  }


  public StagedEmployeeWorkAddressInner mobilePhone(String mobilePhone) {
    this.mobilePhone = mobilePhone;
    return this;
  }

  /**
   * Mobile phone number.&lt;br  /&gt; Max length: 12
   * @return mobilePhone
   */
  @javax.annotation.Nullable
  public String getMobilePhone() {
    return mobilePhone;
  }

  public void setMobilePhone(String mobilePhone) {
    this.mobilePhone = mobilePhone;
  }


  public StagedEmployeeWorkAddressInner pager(String pager) {
    this.pager = pager;
    return this;
  }

  /**
   * Employee pager number.&lt;br  /&gt; Max length: 20
   * @return pager
   */
  @javax.annotation.Nullable
  public String getPager() {
    return pager;
  }

  public void setPager(String pager) {
    this.pager = pager;
  }


  public StagedEmployeeWorkAddressInner phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Phone number.&lt;br  /&gt; Max length: 12
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public StagedEmployeeWorkAddressInner phoneExtension(String phoneExtension) {
    this.phoneExtension = phoneExtension;
    return this;
  }

  /**
   * Phone number extension.&lt;br  /&gt; Max length: 10
   * @return phoneExtension
   */
  @javax.annotation.Nullable
  public String getPhoneExtension() {
    return phoneExtension;
  }

  public void setPhoneExtension(String phoneExtension) {
    this.phoneExtension = phoneExtension;
  }


  public StagedEmployeeWorkAddressInner postalCode(String postalCode) {
    this.postalCode = postalCode;
    return this;
  }

  /**
   * Postal code.&lt;br  /&gt; Max length: 10
   * @return postalCode
   */
  @javax.annotation.Nullable
  public String getPostalCode() {
    return postalCode;
  }

  public void setPostalCode(String postalCode) {
    this.postalCode = postalCode;
  }


  public StagedEmployeeWorkAddressInner state(String state) {
    this.state = state;
    return this;
  }

  /**
   * State or province.&lt;br  /&gt; Max length: 2
   * @return state
   */
  @javax.annotation.Nullable
  public String getState() {
    return state;
  }

  public void setState(String state) {
    this.state = state;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StagedEmployeeWorkAddressInner stagedEmployeeWorkAddressInner = (StagedEmployeeWorkAddressInner) o;
    return Objects.equals(this.address1, stagedEmployeeWorkAddressInner.address1) &&
        Objects.equals(this.address2, stagedEmployeeWorkAddressInner.address2) &&
        Objects.equals(this.city, stagedEmployeeWorkAddressInner.city) &&
        Objects.equals(this.country, stagedEmployeeWorkAddressInner.country) &&
        Objects.equals(this.county, stagedEmployeeWorkAddressInner.county) &&
        Objects.equals(this.emailAddress, stagedEmployeeWorkAddressInner.emailAddress) &&
        Objects.equals(this.mobilePhone, stagedEmployeeWorkAddressInner.mobilePhone) &&
        Objects.equals(this.pager, stagedEmployeeWorkAddressInner.pager) &&
        Objects.equals(this.phone, stagedEmployeeWorkAddressInner.phone) &&
        Objects.equals(this.phoneExtension, stagedEmployeeWorkAddressInner.phoneExtension) &&
        Objects.equals(this.postalCode, stagedEmployeeWorkAddressInner.postalCode) &&
        Objects.equals(this.state, stagedEmployeeWorkAddressInner.state);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(address1, address2, city, country, county, emailAddress, mobilePhone, pager, phone, phoneExtension, postalCode, state);
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
    sb.append("class StagedEmployeeWorkAddressInner {\n");
    sb.append("    address1: ").append(toIndentedString(address1)).append("\n");
    sb.append("    address2: ").append(toIndentedString(address2)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    county: ").append(toIndentedString(county)).append("\n");
    sb.append("    emailAddress: ").append(toIndentedString(emailAddress)).append("\n");
    sb.append("    mobilePhone: ").append(toIndentedString(mobilePhone)).append("\n");
    sb.append("    pager: ").append(toIndentedString(pager)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    phoneExtension: ").append(toIndentedString(phoneExtension)).append("\n");
    sb.append("    postalCode: ").append(toIndentedString(postalCode)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
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
    openapiFields.add("address1");
    openapiFields.add("address2");
    openapiFields.add("city");
    openapiFields.add("country");
    openapiFields.add("county");
    openapiFields.add("emailAddress");
    openapiFields.add("mobilePhone");
    openapiFields.add("pager");
    openapiFields.add("phone");
    openapiFields.add("phoneExtension");
    openapiFields.add("postalCode");
    openapiFields.add("state");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to StagedEmployeeWorkAddressInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!StagedEmployeeWorkAddressInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in StagedEmployeeWorkAddressInner is not found in the empty JSON string", StagedEmployeeWorkAddressInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!StagedEmployeeWorkAddressInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `StagedEmployeeWorkAddressInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address1") != null && !jsonObj.get("address1").isJsonNull()) && !jsonObj.get("address1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address1").toString()));
      }
      if ((jsonObj.get("address2") != null && !jsonObj.get("address2").isJsonNull()) && !jsonObj.get("address2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address2").toString()));
      }
      if ((jsonObj.get("city") != null && !jsonObj.get("city").isJsonNull()) && !jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if ((jsonObj.get("county") != null && !jsonObj.get("county").isJsonNull()) && !jsonObj.get("county").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `county` to be a primitive type in the JSON string but got `%s`", jsonObj.get("county").toString()));
      }
      if ((jsonObj.get("emailAddress") != null && !jsonObj.get("emailAddress").isJsonNull()) && !jsonObj.get("emailAddress").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `emailAddress` to be a primitive type in the JSON string but got `%s`", jsonObj.get("emailAddress").toString()));
      }
      if ((jsonObj.get("mobilePhone") != null && !jsonObj.get("mobilePhone").isJsonNull()) && !jsonObj.get("mobilePhone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mobilePhone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mobilePhone").toString()));
      }
      if ((jsonObj.get("pager") != null && !jsonObj.get("pager").isJsonNull()) && !jsonObj.get("pager").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pager` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pager").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      if ((jsonObj.get("phoneExtension") != null && !jsonObj.get("phoneExtension").isJsonNull()) && !jsonObj.get("phoneExtension").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phoneExtension` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phoneExtension").toString()));
      }
      if ((jsonObj.get("postalCode") != null && !jsonObj.get("postalCode").isJsonNull()) && !jsonObj.get("postalCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `postalCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("postalCode").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!StagedEmployeeWorkAddressInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'StagedEmployeeWorkAddressInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<StagedEmployeeWorkAddressInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(StagedEmployeeWorkAddressInner.class));

       return (TypeAdapter<T>) new TypeAdapter<StagedEmployeeWorkAddressInner>() {
           @Override
           public void write(JsonWriter out, StagedEmployeeWorkAddressInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public StagedEmployeeWorkAddressInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of StagedEmployeeWorkAddressInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of StagedEmployeeWorkAddressInner
   * @throws IOException if the JSON string is invalid with respect to StagedEmployeeWorkAddressInner
   */
  public static StagedEmployeeWorkAddressInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, StagedEmployeeWorkAddressInner.class);
  }

  /**
   * Convert an instance of StagedEmployeeWorkAddressInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

