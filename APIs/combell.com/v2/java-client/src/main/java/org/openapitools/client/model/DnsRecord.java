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
import java.util.Arrays;

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
 * DnsRecord
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:18.229870-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DnsRecord {
  public static final String SERIALIZED_NAME_CONTENT = "content";
  @SerializedName(SERIALIZED_NAME_CONTENT)
  private String content;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_PORT = "port";
  @SerializedName(SERIALIZED_NAME_PORT)
  private Integer port;

  public static final String SERIALIZED_NAME_PRIORITY = "priority";
  @SerializedName(SERIALIZED_NAME_PRIORITY)
  private Integer priority = 10;

  public static final String SERIALIZED_NAME_PROTOCOL = "protocol";
  @SerializedName(SERIALIZED_NAME_PROTOCOL)
  private String protocol = "TCP";

  public static final String SERIALIZED_NAME_RECORD_NAME = "record_name";
  @SerializedName(SERIALIZED_NAME_RECORD_NAME)
  private String recordName;

  public static final String SERIALIZED_NAME_SERVICE = "service";
  @SerializedName(SERIALIZED_NAME_SERVICE)
  private String service;

  public static final String SERIALIZED_NAME_TARGET = "target";
  @SerializedName(SERIALIZED_NAME_TARGET)
  private String target;

  public static final String SERIALIZED_NAME_TTL = "ttl";
  @SerializedName(SERIALIZED_NAME_TTL)
  private Integer ttl = 3600;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public static final String SERIALIZED_NAME_WEIGHT = "weight";
  @SerializedName(SERIALIZED_NAME_WEIGHT)
  private Integer weight = 0;

  public DnsRecord() {
  }

  public DnsRecord content(String content) {
    this.content = content;
    return this;
  }

  /**
   * Variable data depending on the record type.  &lt;ul&gt;&lt;li&gt;A: the IPv4 address.&lt;/li&gt;&lt;li&gt;CNAME: canonical name of an alias.&lt;/li&gt;&lt;li&gt;MX: fully qualified domain name of a mail host.&lt;/li&gt;&lt;li&gt;SRV: does not apply. Data for the SRV records can be found in specific properties.&lt;/li&gt;&lt;li&gt;TXT: free form text data.&lt;/li&gt;&lt;li&gt;CAA: format should match specific values for flag, tag and ca: \&quot;{flag} {tag} {ca}\&quot;.          &lt;ul&gt;&lt;li&gt;The flag. The values 128 (critical) or 0 (non-critical) are expected, with 0 as the default.&lt;/li&gt;&lt;li&gt;The tag. A tag specifies which actions an authorized CA can take in terms of issuing SSL/TLS certificates.&lt;br /&gt;&lt;ul&gt;&lt;li&gt;The value \&quot;issue\&quot;: explicitly authorizes a single certificate authority to issue a certificate (any type) for the hostname.&lt;/li&gt;&lt;li&gt;The value \&quot;issuewild\&quot;: explicitly authorizes a single certificate authority to issue a wildcard certificate (and only wildcard) for the hostname.&lt;/li&gt;&lt;li&gt;The value \&quot;iodef\&quot;: specifies a URL to which a certificate authority may report policy violations.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;The ca. This is the domain of the CA (Certification Authority) that has the authority to issue certificates for the domain in question. If the value is a semicolon (;), it means that no CA has the authority to issue a certificate for that domain.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;ALIAS: canonical name of an alias.&lt;/li&gt;&lt;li&gt;TLSA: format should match specific values for usage, selector, matching type and data: \&quot;{usage} {selector} {matching_type} {data}\&quot;          &lt;ul&gt;&lt;li&gt;The usage. The first field after the TLSA text in the DNS RR, specifies how to verify the certificate.&lt;br /&gt;&lt;ul&gt;&lt;li&gt;A value of 0 is for what is commonly called CA constraint (and PKIX-TA). The certificate provided when establishing TLS must be issued by the listed root-CA or one of its intermediate CAs, with a valid certification path to a root-CA already trusted by the application doing the verification.&lt;/li&gt;&lt;li&gt;A value of 1 is for what is commonly called Service certificate constraint (and PKIX-EE). The certificate used must match the TLSA record exactly, and it must also pass PKIX certification path validation to a trusted root-CA.&lt;/li&gt;&lt;li&gt;A value of 2 is for what is commonly called Trust Anchor Assertion (and DANE-TA). The certificate used has a valid certification path pointing back to the certificate mention in this record, but there is no need for it to pass the PKIX certification path validation to a trusted root-CA.&lt;/li&gt;&lt;li&gt;A value of 3 is for what is commonly called Domain issued certificate (and DANE-EE). The services uses a self-signed certificate. It is not signed by anyone else, and is exactly this record.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;The selector. When connecting to the service and a certificate is received, the selector field specifies which parts of it should be checked.&lt;br /&gt;&lt;ul&gt;&lt;li&gt;A value of 0 means to select the entire certificate for matching.&lt;/li&gt;&lt;li&gt;A value of 1 means to select just the public key for certificate matching. Matching the public key is often sufficient, as this is likely to be unique.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;The matching type.&lt;br /&gt;&lt;ul&gt;&lt;li&gt;A type of 0 means the entire information selected is present in the certificate association data.&lt;/li&gt;&lt;li&gt;A type of 1 means to do a SHA-256 hash of the selected data.&lt;/li&gt;&lt;li&gt;A type of 2 means to do a SHA-512 hash of the selected data.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;li&gt;The actual data to be matched given the settings of the other fields. This is a long text string of hexadecimal data.&lt;/li&gt;&lt;/ul&gt;&lt;/li&gt;&lt;/ul&gt;
   * @return content
   */
  @javax.annotation.Nullable
  public String getContent() {
    return content;
  }

  public void setContent(String content) {
    this.content = content;
  }


  public DnsRecord id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The id of the record  This value is ignored for creation of new records.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public DnsRecord port(Integer port) {
    this.port = port;
    return this;
  }

  /**
   * The port for SRV records.&lt;br /&gt;  The value MUST be a positive integer.&lt;br /&gt;  Editing the value is not possible. You should add a new SRV record and delete the existing record.
   * @return port
   */
  @javax.annotation.Nullable
  public Integer getPort() {
    return port;
  }

  public void setPort(Integer port) {
    this.port = port;
  }


  public DnsRecord priority(Integer priority) {
    this.priority = priority;
    return this;
  }

  /**
   * The priority for MX or SRV records.&lt;br /&gt;  A lower value means more preferred.&lt;br /&gt;  The value MUST be a positive integer less or equal to 9999.
   * @return priority
   */
  @javax.annotation.Nullable
  public Integer getPriority() {
    return priority;
  }

  public void setPriority(Integer priority) {
    this.priority = priority;
  }


  public DnsRecord protocol(String protocol) {
    this.protocol = protocol;
    return this;
  }

  /**
   * Used for the creation of SRV records. Possible options: TCP, UDP, ...&lt;br /&gt;  Editing the value is not possible. You should add a new SRV record and delete the existing record.
   * @return protocol
   */
  @javax.annotation.Nullable
  public String getProtocol() {
    return protocol;
  }

  public void setProtocol(String protocol) {
    this.protocol = protocol;
  }


  public DnsRecord recordName(String recordName) {
    this.recordName = recordName;
    return this;
  }

  /**
   * The name of the record.&lt;br /&gt;  This is the host name, alias defined by the record.&lt;br /&gt;  An empty record or &#39;@&#39; is equal to the domain name.&lt;br /&gt;  Applies to A, MX, CNAME, TXT, CAA, ALIAS and TLSA records.&lt;br /&gt;  When type is TLSA the recommended value format is port number, protocol and host: _25._tcp.&lt;br /&gt;  Does not apply for SRV records.
   * @return recordName
   */
  @javax.annotation.Nullable
  public String getRecordName() {
    return recordName;
  }

  public void setRecordName(String recordName) {
    this.recordName = recordName;
  }


  public DnsRecord service(String service) {
    this.service = service;
    return this;
  }

  /**
   * The symbolic name of the desired service for SRV records.&lt;br /&gt;  Editing the value is not possible. You should add a new SRV record and can delete the existing record.
   * @return service
   */
  @javax.annotation.Nullable
  public String getService() {
    return service;
  }

  public void setService(String service) {
    this.service = service;
  }


  public DnsRecord target(String target) {
    this.target = target;
    return this;
  }

  /**
   * The canonical hostname of the machine providing the service for SRV records.&lt;br /&gt;  Editing the value is not possible. You should add a new SRV record and delete the existing record.
   * @return target
   */
  @javax.annotation.Nullable
  public String getTarget() {
    return target;
  }

  public void setTarget(String target) {
    this.target = target;
  }


  public DnsRecord ttl(Integer ttl) {
    this.ttl = ttl;
    return this;
  }

  /**
   * Time to live of the record in seconds.&lt;br /&gt;  It defines the time frame that clients can cache the information.&lt;br /&gt;  The value MUST be between 60 and 86400. The default value is 3600 (&#x3D; 1 hour).
   * @return ttl
   */
  @javax.annotation.Nullable
  public Integer getTtl() {
    return ttl;
  }

  public void setTtl(Integer ttl) {
    this.ttl = ttl;
  }


  public DnsRecord type(String type) {
    this.type = type;
    return this;
  }

  /**
   * The type of the record (A, MX, CNAME, SRV, TXT, CAA, ALIAS and TLSA).
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }


  public DnsRecord weight(Integer weight) {
    this.weight = weight;
    return this;
  }

  /**
   * The weight for SRV records with the same priority.&lt;br /&gt;  A higher value means more preferred.
   * @return weight
   */
  @javax.annotation.Nullable
  public Integer getWeight() {
    return weight;
  }

  public void setWeight(Integer weight) {
    this.weight = weight;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DnsRecord dnsRecord = (DnsRecord) o;
    return Objects.equals(this.content, dnsRecord.content) &&
        Objects.equals(this.id, dnsRecord.id) &&
        Objects.equals(this.port, dnsRecord.port) &&
        Objects.equals(this.priority, dnsRecord.priority) &&
        Objects.equals(this.protocol, dnsRecord.protocol) &&
        Objects.equals(this.recordName, dnsRecord.recordName) &&
        Objects.equals(this.service, dnsRecord.service) &&
        Objects.equals(this.target, dnsRecord.target) &&
        Objects.equals(this.ttl, dnsRecord.ttl) &&
        Objects.equals(this.type, dnsRecord.type) &&
        Objects.equals(this.weight, dnsRecord.weight);
  }

  @Override
  public int hashCode() {
    return Objects.hash(content, id, port, priority, protocol, recordName, service, target, ttl, type, weight);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DnsRecord {\n");
    sb.append("    content: ").append(toIndentedString(content)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    port: ").append(toIndentedString(port)).append("\n");
    sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
    sb.append("    recordName: ").append(toIndentedString(recordName)).append("\n");
    sb.append("    service: ").append(toIndentedString(service)).append("\n");
    sb.append("    target: ").append(toIndentedString(target)).append("\n");
    sb.append("    ttl: ").append(toIndentedString(ttl)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    weight: ").append(toIndentedString(weight)).append("\n");
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
    openapiFields.add("content");
    openapiFields.add("id");
    openapiFields.add("port");
    openapiFields.add("priority");
    openapiFields.add("protocol");
    openapiFields.add("record_name");
    openapiFields.add("service");
    openapiFields.add("target");
    openapiFields.add("ttl");
    openapiFields.add("type");
    openapiFields.add("weight");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DnsRecord
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DnsRecord.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DnsRecord is not found in the empty JSON string", DnsRecord.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DnsRecord.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DnsRecord` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("content") != null && !jsonObj.get("content").isJsonNull()) && !jsonObj.get("content").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("protocol") != null && !jsonObj.get("protocol").isJsonNull()) && !jsonObj.get("protocol").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `protocol` to be a primitive type in the JSON string but got `%s`", jsonObj.get("protocol").toString()));
      }
      if ((jsonObj.get("record_name") != null && !jsonObj.get("record_name").isJsonNull()) && !jsonObj.get("record_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `record_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("record_name").toString()));
      }
      if ((jsonObj.get("service") != null && !jsonObj.get("service").isJsonNull()) && !jsonObj.get("service").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service").toString()));
      }
      if ((jsonObj.get("target") != null && !jsonObj.get("target").isJsonNull()) && !jsonObj.get("target").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `target` to be a primitive type in the JSON string but got `%s`", jsonObj.get("target").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DnsRecord.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DnsRecord' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DnsRecord> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DnsRecord.class));

       return (TypeAdapter<T>) new TypeAdapter<DnsRecord>() {
           @Override
           public void write(JsonWriter out, DnsRecord value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DnsRecord read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DnsRecord given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DnsRecord
   * @throws IOException if the JSON string is invalid with respect to DnsRecord
   */
  public static DnsRecord fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DnsRecord.class);
  }

  /**
   * Convert an instance of DnsRecord to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

