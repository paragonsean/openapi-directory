/*
 * Public Api
 * # Introduction  This API allows resellers to manage their resources in a simple, programmatic way using HTTP requests.  # Conventions  ## Requests  The API supports different methods depending on the required action.  | Method | Description | ---  | --- | GET  | Retrieve resources in a collection or get a single resource.<br/>Getters will never have any effect on the queried resources. | POST  | Create a new resource in a collection. | PUT  | Update an existing resource with its new representation. | DELETE | Delete an existing resource.  ## HTTP status codes  The API will reply with different HTTP statuscodes:  | StatusCode    | Description | ---      | --- | 200 OK     | The requests was processed and you receive data as a result. | 201 CREATED    | The resource has been created. Either the Location header contains a link to the created resource, or links are being returned in the response body. The applied method will be indicated in the documentation. | 202 ACCEPTED    | The request has been validated and accepted. Because we need to do some background processing prior to returning the result, we cannot send back a useful representation. | 204 NOCONTENT    | The request has been processed, but no details can be returned. | 400 BADREQUEST   | Your request is malformed. | 401 UNAUTHORIZED   | You are not authorized. Follow the instructions in the Authorization documentation. | 403 FORBIDDEN    | Access to the resource or operation is not allowed. | 404 NOTFOUND    | The resource cannot be found. | 410 GONE                  | The resource is permanently no longer available. | 429 TOOMANYREQUESTS  | The ratelimit has been exceeded. Please refer to the documentation on rate limiting for more details. | 500 INTERNALSERVERERROR | An error occurred during the processing of the request. The error is unexpected and most likely due to a bug in the api.  In the event of a problem, the body of the response will usually contain an errorcode and errormessage. In rare cases additional details about the error are reported.  Errorcodes 400-499 are considered to be client errors and indicate that there was an issue with the request. We will not take any action besides monitoring.   Errorcodes 500-599 are considered to be server errors. The errors are monitored AND action will be taken to resolve the error.  ## Formatting  Snake casing is applied on resources and query parameters. The API is strictly returning JSON. No other formats are supported.  Datetimes are returned in ISO-8601 format.  ## Pagination  Pagination is on by default on collections and is controlled by specifying *skip* and *take* parameters.   **Skip** indicates the number of results to skip and where to start the new take.   **Take** indicates the number of records to return. The returned number of items can be smaller than the requested take.  Paged results will have headers with useful information regarding the paging.  | Header    | Description | ---     | --- | X-Paging-Skipped  | The number of results that have been skipped. | X-Paging-Take   | The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. | X-Paging-TotalResults | The total number of results regardless of paging.  ## Rate limiting  The number of requests per interval is limited. Detailed information on the rate limiting can be found in specific headers which will be sent on each request.  | Header    | Description | ---     | --- | X-RateLimit-Limit  | The number of requests that can be made in a specific time interval. | X-RateLimit-Usage  | The number of requests already made in the current time interval. | X-RateLimit-Remaining | The number of requests remaining until the reset. | X-RateLimit-Reset  | The number of seconds until the reset.<br />After the reset you are allowed to make as many requests as specified by the X-RateLimit-Limit header. | Retry-After   | The number of seconds you have to wait until you can make new requests.<br />This header is only present when the rate limit has been reached. It is identical to X-RateLimit-Reset.  When the ratelimit has been reached, all requests will return with a HTTP statuscode 429 and ReasonPhrase '*Too many requests, retry later.*'.  # Authentication  The Api uses HMAC authentication.   Hash-based message authentication code (HMAC) is a mechanism for calculating a message authentication code involving a hash function in combination with a secret key.   Both the integrity and the authenticity of the message are verified this way.  ## Steps to generate the HMAC  1. Get your api key and secret from your controlpanel.   It is absolutely vital that the secret is never exposed. Once the secret is out, anyone would be able to generate hmacs to impersonate you.   In case your secret is compromised, you can generate a new api key and secret on your controlpanel. 2. Construct the input value for generating the hmac.   Concatenate:apikey, request method, path and querystring information, unix timestamp, nonce and content.  |          | Description | ---         | --- | apikey        | The key that is linked to your user. | request method      | lowercased (eg: get, post, delete,...) | path and querystring information  | urlencoding of the lowercased relative path and querystring.<br />The path **MUST start with the api version (/v2)**.<br />The hexadecimal codes (percent encoding) MUST be uppercased. | unix timestamp      | the unix timestamp in **seconds**. | nonce         | a unique string for each request. It should be a random string, not related to the request. The nonce (in combination with the unix timestamp) protects you from replay attacks in case anyone was able to intercept a request. | content        | When the request body is not empty, this should be the Base64 encoded Md5 hash of the request body.<br />An empty body should not be encoded.  3. Hash the concatenated string using your api secret and the SHA-256 algorithm. 4. Base64 encode the result of the hash function. This is the hmac signature you will need to send an authorized request.  ## Sending an authorized request  An authorized request can be made by sending the generated HMAC in the authorization header.   A correct authorizationheader uses the hmac authorization scheme and a correctly formatted authorization parameter.  Create the authorization parameter by concatenating:   * apikey   * colon ':'   * generated HMAC signature (see above)   * colon ':'   * nonce (the one used to generate the signature)   * colon ':'   * unix timestamp (the one used to generate the signature)  A sample (illustrated):  * The first line is the string you create to feed to the hashing algorithm. * The second line is the authorization header that should be sent in the request.  ![hmac authorization header illustrated](/v2/images/authentication_illustration.jpg \"authorization header illustrated\")  ## IP whitelisting  Access is by default restricted for all IP addresses. You need to explicitly whitelist an IP or an IP range in your controlpanel.  # Versioning  Because of breaking contract changes compared to v1, we released v2 of the API.   V1 will still be available, but you are strongly encouraged to migrate to the latest version.   New features will only be available on v2.  # Policy  ### Fair use policy  Please respect the rate limits and do not use the api for any purposes of abuse.   All requests are being monitored and logged.   Intentional abuse might result in api key revocation.  # Errors  The API attempts to return appropriate HTTP status codes for every request.   When the status code indicates failure, the API will also provide an error message in most cases.  An error message contains a machine-parseable error code accompanied by a descriptive error text.   The text for an error message might change over time, but codes will stay the same.  [An overview of error codes can be found here](/v2/documentation/errorcodes).  # Change log  [An overview of new changes can be found here](/v2/documentation/changelog).  # Provisioning information  ## Terminology  | Term   | Definition                | | ---   | ---                  | | Servicepack | Defines a set of assets that belong together. An example is a hosting package which offers Linux hosting, a domain name, a couple of mailboxes and databases.<br/>It also limits the size of individual assets within the same account. | | Account  | Represents an instance of the servicepack. It contains one or more assets. The number and size of assets is defined by the servicepack. | | Asset   | A manageable service. For example: a mysql database, a linux hosting, a mailbox,...<br/>Some assets are created at the moment when the account is created. Other assets can be created afterwards.   ## Common provisioning scenario  **Provisioning of an account with Linux hosting with one MySql database**  *Without a pre-existing account:*  1. Create a new account.<br/>Perform a POST on the accounts route and provide the desired servicepack id and identifier (domain name). 2. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 3. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 4. The created resource will point to an account. You now know the account's Id and can continue with the provisioning of a MySql database on this account. 5. Perform a POST on the mysqldatabases route and provide the account id along with other requested information. 6. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 7. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 8. The created resource will point to a MySql database resource.  ## SSL certificate requests  **Requesting an SSL certificate causes the purchase of a paying product.**  1. A certificate is created by adding an ssl certificate request. 2. Upon statuscode 201 you should query for certificate completion on the resource provided in the location response header. 3. The resource request can respond with different statuscodes: <ul>     <li>200: the certificate request is ongoing.<br/> Check the validations collection for validation values that are not auto_validated. Those should be set by you system.<br/> Call verify domain validations once all validation values are in place. It might take some time for verification to take place. It is not necessary to call this method more than once.</li>     <li>303: the certificate request is complete; there is no more certificate request resource available. Check the location header value to retrieve the representation of the resulting ssl certificate.</li>     <li>410: the certificate request does not exist anymore, there is no certificate created as a result of the request.</li> </ul>
 *
 * The version of the OpenAPI document: v2
 * 
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.SslCertificateType;
import org.openapitools.client.model.SslCertificateValidationLevel;

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
 * SslCertificate
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:18.229870-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SslCertificate {
  public static final String SERIALIZED_NAME_COMMON_NAME = "common_name";
  @SerializedName(SERIALIZED_NAME_COMMON_NAME)
  private String commonName;

  public static final String SERIALIZED_NAME_EXPIRES_AFTER = "expires_after";
  @SerializedName(SERIALIZED_NAME_EXPIRES_AFTER)
  private OffsetDateTime expiresAfter;

  public static final String SERIALIZED_NAME_SHA1_FINGERPRINT = "sha1_fingerprint";
  @SerializedName(SERIALIZED_NAME_SHA1_FINGERPRINT)
  private String sha1Fingerprint;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private SslCertificateType type;

  public static final String SERIALIZED_NAME_VALIDATION_LEVEL = "validation_level";
  @SerializedName(SERIALIZED_NAME_VALIDATION_LEVEL)
  private SslCertificateValidationLevel validationLevel;

  public SslCertificate() {
  }

  public SslCertificate commonName(String commonName) {
    this.commonName = commonName;
    return this;
  }

  /**
   * The common name (e.g. domain.com) of the certificate.
   * @return commonName
   */
  @javax.annotation.Nullable
  public String getCommonName() {
    return commonName;
  }

  public void setCommonName(String commonName) {
    this.commonName = commonName;
  }


  public SslCertificate expiresAfter(OffsetDateTime expiresAfter) {
    this.expiresAfter = expiresAfter;
    return this;
  }

  /**
   * The exact time the certificate will expire.
   * @return expiresAfter
   */
  @javax.annotation.Nullable
  public OffsetDateTime getExpiresAfter() {
    return expiresAfter;
  }

  public void setExpiresAfter(OffsetDateTime expiresAfter) {
    this.expiresAfter = expiresAfter;
  }


  public SslCertificate sha1Fingerprint(String sha1Fingerprint) {
    this.sha1Fingerprint = sha1Fingerprint;
    return this;
  }

  /**
   * The SHA-1 fingerprint of the certificate.&lt;br /&gt;  The fingerprint is a cryptographic hash which is a short unique identification of the certificate.
   * @return sha1Fingerprint
   */
  @javax.annotation.Nullable
  public String getSha1Fingerprint() {
    return sha1Fingerprint;
  }

  public void setSha1Fingerprint(String sha1Fingerprint) {
    this.sha1Fingerprint = sha1Fingerprint;
  }


  public SslCertificate type(SslCertificateType type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public SslCertificateType getType() {
    return type;
  }

  public void setType(SslCertificateType type) {
    this.type = type;
  }


  public SslCertificate validationLevel(SslCertificateValidationLevel validationLevel) {
    this.validationLevel = validationLevel;
    return this;
  }

  /**
   * Get validationLevel
   * @return validationLevel
   */
  @javax.annotation.Nullable
  public SslCertificateValidationLevel getValidationLevel() {
    return validationLevel;
  }

  public void setValidationLevel(SslCertificateValidationLevel validationLevel) {
    this.validationLevel = validationLevel;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SslCertificate sslCertificate = (SslCertificate) o;
    return Objects.equals(this.commonName, sslCertificate.commonName) &&
        Objects.equals(this.expiresAfter, sslCertificate.expiresAfter) &&
        Objects.equals(this.sha1Fingerprint, sslCertificate.sha1Fingerprint) &&
        Objects.equals(this.type, sslCertificate.type) &&
        Objects.equals(this.validationLevel, sslCertificate.validationLevel);
  }

  @Override
  public int hashCode() {
    return Objects.hash(commonName, expiresAfter, sha1Fingerprint, type, validationLevel);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SslCertificate {\n");
    sb.append("    commonName: ").append(toIndentedString(commonName)).append("\n");
    sb.append("    expiresAfter: ").append(toIndentedString(expiresAfter)).append("\n");
    sb.append("    sha1Fingerprint: ").append(toIndentedString(sha1Fingerprint)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    validationLevel: ").append(toIndentedString(validationLevel)).append("\n");
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
    openapiFields.add("common_name");
    openapiFields.add("expires_after");
    openapiFields.add("sha1_fingerprint");
    openapiFields.add("type");
    openapiFields.add("validation_level");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SslCertificate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SslCertificate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SslCertificate is not found in the empty JSON string", SslCertificate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SslCertificate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SslCertificate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("common_name") != null && !jsonObj.get("common_name").isJsonNull()) && !jsonObj.get("common_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `common_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("common_name").toString()));
      }
      if ((jsonObj.get("sha1_fingerprint") != null && !jsonObj.get("sha1_fingerprint").isJsonNull()) && !jsonObj.get("sha1_fingerprint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sha1_fingerprint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sha1_fingerprint").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        SslCertificateType.validateJsonElement(jsonObj.get("type"));
      }
      // validate the optional field `validation_level`
      if (jsonObj.get("validation_level") != null && !jsonObj.get("validation_level").isJsonNull()) {
        SslCertificateValidationLevel.validateJsonElement(jsonObj.get("validation_level"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SslCertificate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SslCertificate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SslCertificate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SslCertificate.class));

       return (TypeAdapter<T>) new TypeAdapter<SslCertificate>() {
           @Override
           public void write(JsonWriter out, SslCertificate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SslCertificate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SslCertificate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SslCertificate
   * @throws IOException if the JSON string is invalid with respect to SslCertificate
   */
  public static SslCertificate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SslCertificate.class);
  }

  /**
   * Convert an instance of SslCertificate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

