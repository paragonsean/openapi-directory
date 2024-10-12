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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AdditionalValidationAttribute;
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
 * CreateSslCertificateRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:18.229870-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateSslCertificateRequest {
  public static final String SERIALIZED_NAME_ADDITIONAL_VALIDATION_ATTRIBUTES = "additional_validation_attributes";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_VALIDATION_ATTRIBUTES)
  private List<AdditionalValidationAttribute> additionalValidationAttributes = new ArrayList<>();

  public static final String SERIALIZED_NAME_CERTIFICATE_TYPE = "certificate_type";
  @SerializedName(SERIALIZED_NAME_CERTIFICATE_TYPE)
  private SslCertificateType certificateType;

  public static final String SERIALIZED_NAME_CSR = "csr";
  @SerializedName(SERIALIZED_NAME_CSR)
  private String csr;

  public static final String SERIALIZED_NAME_VALIDATION_LEVEL = "validation_level";
  @SerializedName(SERIALIZED_NAME_VALIDATION_LEVEL)
  private SslCertificateValidationLevel validationLevel;

  public CreateSslCertificateRequest() {
  }

  public CreateSslCertificateRequest additionalValidationAttributes(List<AdditionalValidationAttribute> additionalValidationAttributes) {
    this.additionalValidationAttributes = additionalValidationAttributes;
    return this;
  }

  public CreateSslCertificateRequest addAdditionalValidationAttributesItem(AdditionalValidationAttribute additionalValidationAttributesItem) {
    if (this.additionalValidationAttributes == null) {
      this.additionalValidationAttributes = new ArrayList<>();
    }
    this.additionalValidationAttributes.add(additionalValidationAttributesItem);
    return this;
  }

  /**
   * List of additional validation attributes for the certificate when choosing organization or extended validation.  &lt;table&gt;&lt;tr&gt;&lt;th&gt;Name&lt;/th&gt;&lt;th&gt;Info&lt;/th&gt;&lt;th&gt;Required&lt;/th&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Firstname&lt;/td&gt;&lt;td&gt;Firstname of the technical contact&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Lastname&lt;/td&gt;&lt;td&gt;Lastname of the technical contact&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Phone&lt;/td&gt;&lt;td&gt;Phone of the technical contact&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;EmailAddress&lt;/td&gt;&lt;td&gt;Email address of the technical contact&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Street&lt;/td&gt;&lt;td&gt;Address street of the organization&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Number&lt;/td&gt;&lt;td&gt;Address house number of the organization&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;PostalCode&lt;/td&gt;&lt;td&gt;Address postal code of the organization&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;VatCountryCode&lt;/td&gt;&lt;td&gt;VAT country code of the organization, ISO 3166-1 alpha-2 country code&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;OrganizationNumber&lt;/td&gt;&lt;td&gt;Business number of the organization&lt;/td&gt;&lt;td&gt;No&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;
   * @return additionalValidationAttributes
   */
  @javax.annotation.Nullable
  public List<AdditionalValidationAttribute> getAdditionalValidationAttributes() {
    return additionalValidationAttributes;
  }

  public void setAdditionalValidationAttributes(List<AdditionalValidationAttribute> additionalValidationAttributes) {
    this.additionalValidationAttributes = additionalValidationAttributes;
  }


  public CreateSslCertificateRequest certificateType(SslCertificateType certificateType) {
    this.certificateType = certificateType;
    return this;
  }

  /**
   * Get certificateType
   * @return certificateType
   */
  @javax.annotation.Nullable
  public SslCertificateType getCertificateType() {
    return certificateType;
  }

  public void setCertificateType(SslCertificateType certificateType) {
    this.certificateType = certificateType;
  }


  public CreateSslCertificateRequest csr(String csr) {
    this.csr = csr;
    return this;
  }

  /**
   * The certificate signing request data.&lt;br /&gt;  The certificate signing request subject should contain following attributes:&lt;br /&gt;&lt;table&gt;&lt;tr&gt;&lt;th&gt;Name&lt;/th&gt;&lt;th&gt;Code&lt;/th&gt;&lt;th&gt;Format&lt;/th&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;CommonName&lt;/td&gt;&lt;td&gt;CN&lt;/td&gt;&lt;td&gt;Valid domain name, for example site.be, alias.site.be or *.site.be&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Country&lt;/td&gt;&lt;td&gt;C&lt;/td&gt;&lt;td&gt;ISO 3166-1 alpha-2 country code&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;State&lt;/td&gt;&lt;td&gt;ST&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Locality&lt;/td&gt;&lt;td&gt;L&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Organization&lt;/td&gt;&lt;td&gt;O&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;EmailAddress&lt;/td&gt;&lt;td&gt;E&lt;/td&gt;&lt;td&gt;Valid email address&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;  The certificate signing request should also contain all the additional aliases and domains (SAN&#39;s) for the certificate.
   * @return csr
   */
  @javax.annotation.Nullable
  public String getCsr() {
    return csr;
  }

  public void setCsr(String csr) {
    this.csr = csr;
  }


  public CreateSslCertificateRequest validationLevel(SslCertificateValidationLevel validationLevel) {
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
    CreateSslCertificateRequest createSslCertificateRequest = (CreateSslCertificateRequest) o;
    return Objects.equals(this.additionalValidationAttributes, createSslCertificateRequest.additionalValidationAttributes) &&
        Objects.equals(this.certificateType, createSslCertificateRequest.certificateType) &&
        Objects.equals(this.csr, createSslCertificateRequest.csr) &&
        Objects.equals(this.validationLevel, createSslCertificateRequest.validationLevel);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalValidationAttributes, certificateType, csr, validationLevel);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateSslCertificateRequest {\n");
    sb.append("    additionalValidationAttributes: ").append(toIndentedString(additionalValidationAttributes)).append("\n");
    sb.append("    certificateType: ").append(toIndentedString(certificateType)).append("\n");
    sb.append("    csr: ").append(toIndentedString(csr)).append("\n");
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
    openapiFields.add("additional_validation_attributes");
    openapiFields.add("certificate_type");
    openapiFields.add("csr");
    openapiFields.add("validation_level");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateSslCertificateRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateSslCertificateRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateSslCertificateRequest is not found in the empty JSON string", CreateSslCertificateRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateSslCertificateRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateSslCertificateRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("additional_validation_attributes") != null && !jsonObj.get("additional_validation_attributes").isJsonNull()) {
        JsonArray jsonArrayadditionalValidationAttributes = jsonObj.getAsJsonArray("additional_validation_attributes");
        if (jsonArrayadditionalValidationAttributes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("additional_validation_attributes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `additional_validation_attributes` to be an array in the JSON string but got `%s`", jsonObj.get("additional_validation_attributes").toString()));
          }

          // validate the optional field `additional_validation_attributes` (array)
          for (int i = 0; i < jsonArrayadditionalValidationAttributes.size(); i++) {
            AdditionalValidationAttribute.validateJsonElement(jsonArrayadditionalValidationAttributes.get(i));
          };
        }
      }
      // validate the optional field `certificate_type`
      if (jsonObj.get("certificate_type") != null && !jsonObj.get("certificate_type").isJsonNull()) {
        SslCertificateType.validateJsonElement(jsonObj.get("certificate_type"));
      }
      if ((jsonObj.get("csr") != null && !jsonObj.get("csr").isJsonNull()) && !jsonObj.get("csr").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `csr` to be a primitive type in the JSON string but got `%s`", jsonObj.get("csr").toString()));
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
       if (!CreateSslCertificateRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateSslCertificateRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateSslCertificateRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateSslCertificateRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateSslCertificateRequest>() {
           @Override
           public void write(JsonWriter out, CreateSslCertificateRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateSslCertificateRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateSslCertificateRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateSslCertificateRequest
   * @throws IOException if the JSON string is invalid with respect to CreateSslCertificateRequest
   */
  public static CreateSslCertificateRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateSslCertificateRequest.class);
  }

  /**
   * Convert an instance of CreateSslCertificateRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

