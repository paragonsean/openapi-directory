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
import org.openapitools.client.model.LinuxIpType;
import org.openapitools.client.model.LinuxSite;

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
 * LinuxHostingDetail
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:18.229870-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LinuxHostingDetail {
  public static final String SERIALIZED_NAME_ACTUAL_SIZE = "actual_size";
  @SerializedName(SERIALIZED_NAME_ACTUAL_SIZE)
  private Integer actualSize;

  public static final String SERIALIZED_NAME_DOMAIN_NAME = "domain_name";
  @SerializedName(SERIALIZED_NAME_DOMAIN_NAME)
  private String domainName;

  public static final String SERIALIZED_NAME_FTP_ENABLED = "ftp_enabled";
  @SerializedName(SERIALIZED_NAME_FTP_ENABLED)
  private Boolean ftpEnabled;

  public static final String SERIALIZED_NAME_FTP_USERNAME = "ftp_username";
  @SerializedName(SERIALIZED_NAME_FTP_USERNAME)
  private String ftpUsername;

  public static final String SERIALIZED_NAME_IP = "ip";
  @SerializedName(SERIALIZED_NAME_IP)
  private String ip;

  public static final String SERIALIZED_NAME_IP_TYPE = "ip_type";
  @SerializedName(SERIALIZED_NAME_IP_TYPE)
  private LinuxIpType ipType;

  public static final String SERIALIZED_NAME_MAX_SIZE = "max_size";
  @SerializedName(SERIALIZED_NAME_MAX_SIZE)
  private Integer maxSize;

  public static final String SERIALIZED_NAME_MAX_WEBSPACE_SIZE = "max_webspace_size";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_MAX_WEBSPACE_SIZE)
  private Integer maxWebspaceSize;

  public static final String SERIALIZED_NAME_MYSQL_DATABASE_NAMES = "mysql_database_names";
  @SerializedName(SERIALIZED_NAME_MYSQL_DATABASE_NAMES)
  private List<String> mysqlDatabaseNames = new ArrayList<>();

  public static final String SERIALIZED_NAME_PHP_VERSION = "php_version";
  @SerializedName(SERIALIZED_NAME_PHP_VERSION)
  private String phpVersion;

  public static final String SERIALIZED_NAME_SERVICEPACK_ID = "servicepack_id";
  @SerializedName(SERIALIZED_NAME_SERVICEPACK_ID)
  private Integer servicepackId;

  public static final String SERIALIZED_NAME_SITES = "sites";
  @SerializedName(SERIALIZED_NAME_SITES)
  private List<LinuxSite> sites = new ArrayList<>();

  public static final String SERIALIZED_NAME_SSH_HOST = "ssh_host";
  @SerializedName(SERIALIZED_NAME_SSH_HOST)
  private String sshHost;

  public static final String SERIALIZED_NAME_SSH_USERNAME = "ssh_username";
  @SerializedName(SERIALIZED_NAME_SSH_USERNAME)
  private String sshUsername;

  public static final String SERIALIZED_NAME_WEBSPACE_USAGE = "webspace_usage";
  @Deprecated
  @SerializedName(SERIALIZED_NAME_WEBSPACE_USAGE)
  private Integer webspaceUsage;

  public LinuxHostingDetail() {
  }

  public LinuxHostingDetail actualSize(Integer actualSize) {
    this.actualSize = actualSize;
    return this;
  }

  /**
   * Used webspace size in MB
   * @return actualSize
   */
  @javax.annotation.Nullable
  public Integer getActualSize() {
    return actualSize;
  }

  public void setActualSize(Integer actualSize) {
    this.actualSize = actualSize;
  }


  public LinuxHostingDetail domainName(String domainName) {
    this.domainName = domainName;
    return this;
  }

  /**
   * Domain name for the Linux hosting account.
   * @return domainName
   */
  @javax.annotation.Nullable
  public String getDomainName() {
    return domainName;
  }

  public void setDomainName(String domainName) {
    this.domainName = domainName;
  }


  public LinuxHostingDetail ftpEnabled(Boolean ftpEnabled) {
    this.ftpEnabled = ftpEnabled;
    return this;
  }

  /**
   * Indicates whether ftp is enabled for the hosting account.
   * @return ftpEnabled
   */
  @javax.annotation.Nullable
  public Boolean getFtpEnabled() {
    return ftpEnabled;
  }

  public void setFtpEnabled(Boolean ftpEnabled) {
    this.ftpEnabled = ftpEnabled;
  }


  public LinuxHostingDetail ftpUsername(String ftpUsername) {
    this.ftpUsername = ftpUsername;
    return this;
  }

  /**
   * Ftp username
   * @return ftpUsername
   */
  @javax.annotation.Nullable
  public String getFtpUsername() {
    return ftpUsername;
  }

  public void setFtpUsername(String ftpUsername) {
    this.ftpUsername = ftpUsername;
  }


  public LinuxHostingDetail ip(String ip) {
    this.ip = ip;
    return this;
  }

  /**
   * Linux hosting IP address
   * @return ip
   */
  @javax.annotation.Nullable
  public String getIp() {
    return ip;
  }

  public void setIp(String ip) {
    this.ip = ip;
  }


  public LinuxHostingDetail ipType(LinuxIpType ipType) {
    this.ipType = ipType;
    return this;
  }

  /**
   * Get ipType
   * @return ipType
   */
  @javax.annotation.Nullable
  public LinuxIpType getIpType() {
    return ipType;
  }

  public void setIpType(LinuxIpType ipType) {
    this.ipType = ipType;
  }


  public LinuxHostingDetail maxSize(Integer maxSize) {
    this.maxSize = maxSize;
    return this;
  }

  /**
   * Maximum webspace size in MB
   * @return maxSize
   */
  @javax.annotation.Nullable
  public Integer getMaxSize() {
    return maxSize;
  }

  public void setMaxSize(Integer maxSize) {
    this.maxSize = maxSize;
  }


  @Deprecated
  public LinuxHostingDetail maxWebspaceSize(Integer maxWebspaceSize) {
    this.maxWebspaceSize = maxWebspaceSize;
    return this;
  }

  /**
   * Maximum webspace size in MB&lt;br /&gt;  Use max_size instead.
   * @return maxWebspaceSize
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Integer getMaxWebspaceSize() {
    return maxWebspaceSize;
  }

  @Deprecated
  public void setMaxWebspaceSize(Integer maxWebspaceSize) {
    this.maxWebspaceSize = maxWebspaceSize;
  }


  public LinuxHostingDetail mysqlDatabaseNames(List<String> mysqlDatabaseNames) {
    this.mysqlDatabaseNames = mysqlDatabaseNames;
    return this;
  }

  public LinuxHostingDetail addMysqlDatabaseNamesItem(String mysqlDatabaseNamesItem) {
    if (this.mysqlDatabaseNames == null) {
      this.mysqlDatabaseNames = new ArrayList<>();
    }
    this.mysqlDatabaseNames.add(mysqlDatabaseNamesItem);
    return this;
  }

  /**
   * A list of mysql databases linked to the hosting account.&lt;br /&gt;  Details of the database can be read using the mysql database detail.
   * @return mysqlDatabaseNames
   */
  @javax.annotation.Nullable
  public List<String> getMysqlDatabaseNames() {
    return mysqlDatabaseNames;
  }

  public void setMysqlDatabaseNames(List<String> mysqlDatabaseNames) {
    this.mysqlDatabaseNames = mysqlDatabaseNames;
  }


  public LinuxHostingDetail phpVersion(String phpVersion) {
    this.phpVersion = phpVersion;
    return this;
  }

  /**
   * The active php version for the hosting account.
   * @return phpVersion
   */
  @javax.annotation.Nullable
  public String getPhpVersion() {
    return phpVersion;
  }

  public void setPhpVersion(String phpVersion) {
    this.phpVersion = phpVersion;
  }


  public LinuxHostingDetail servicepackId(Integer servicepackId) {
    this.servicepackId = servicepackId;
    return this;
  }

  /**
   * Id of Linux hosting service package.
   * @return servicepackId
   */
  @javax.annotation.Nullable
  public Integer getServicepackId() {
    return servicepackId;
  }

  public void setServicepackId(Integer servicepackId) {
    this.servicepackId = servicepackId;
  }


  public LinuxHostingDetail sites(List<LinuxSite> sites) {
    this.sites = sites;
    return this;
  }

  public LinuxHostingDetail addSitesItem(LinuxSite sitesItem) {
    if (this.sites == null) {
      this.sites = new ArrayList<>();
    }
    this.sites.add(sitesItem);
    return this;
  }

  /**
   * A list of websites on the hosting account.
   * @return sites
   */
  @javax.annotation.Nullable
  public List<LinuxSite> getSites() {
    return sites;
  }

  public void setSites(List<LinuxSite> sites) {
    this.sites = sites;
  }


  public LinuxHostingDetail sshHost(String sshHost) {
    this.sshHost = sshHost;
    return this;
  }

  /**
   * Ssh host of the linux hosting account
   * @return sshHost
   */
  @javax.annotation.Nullable
  public String getSshHost() {
    return sshHost;
  }

  public void setSshHost(String sshHost) {
    this.sshHost = sshHost;
  }


  public LinuxHostingDetail sshUsername(String sshUsername) {
    this.sshUsername = sshUsername;
    return this;
  }

  /**
   * Ssh username
   * @return sshUsername
   */
  @javax.annotation.Nullable
  public String getSshUsername() {
    return sshUsername;
  }

  public void setSshUsername(String sshUsername) {
    this.sshUsername = sshUsername;
  }


  @Deprecated
  public LinuxHostingDetail webspaceUsage(Integer webspaceUsage) {
    this.webspaceUsage = webspaceUsage;
    return this;
  }

  /**
   * Used webspace size in MB&lt;br /&gt;  Use actual_size instead.
   * @return webspaceUsage
   * @deprecated
   */
  @Deprecated
  @javax.annotation.Nullable
  public Integer getWebspaceUsage() {
    return webspaceUsage;
  }

  @Deprecated
  public void setWebspaceUsage(Integer webspaceUsage) {
    this.webspaceUsage = webspaceUsage;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LinuxHostingDetail linuxHostingDetail = (LinuxHostingDetail) o;
    return Objects.equals(this.actualSize, linuxHostingDetail.actualSize) &&
        Objects.equals(this.domainName, linuxHostingDetail.domainName) &&
        Objects.equals(this.ftpEnabled, linuxHostingDetail.ftpEnabled) &&
        Objects.equals(this.ftpUsername, linuxHostingDetail.ftpUsername) &&
        Objects.equals(this.ip, linuxHostingDetail.ip) &&
        Objects.equals(this.ipType, linuxHostingDetail.ipType) &&
        Objects.equals(this.maxSize, linuxHostingDetail.maxSize) &&
        Objects.equals(this.maxWebspaceSize, linuxHostingDetail.maxWebspaceSize) &&
        Objects.equals(this.mysqlDatabaseNames, linuxHostingDetail.mysqlDatabaseNames) &&
        Objects.equals(this.phpVersion, linuxHostingDetail.phpVersion) &&
        Objects.equals(this.servicepackId, linuxHostingDetail.servicepackId) &&
        Objects.equals(this.sites, linuxHostingDetail.sites) &&
        Objects.equals(this.sshHost, linuxHostingDetail.sshHost) &&
        Objects.equals(this.sshUsername, linuxHostingDetail.sshUsername) &&
        Objects.equals(this.webspaceUsage, linuxHostingDetail.webspaceUsage);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actualSize, domainName, ftpEnabled, ftpUsername, ip, ipType, maxSize, maxWebspaceSize, mysqlDatabaseNames, phpVersion, servicepackId, sites, sshHost, sshUsername, webspaceUsage);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LinuxHostingDetail {\n");
    sb.append("    actualSize: ").append(toIndentedString(actualSize)).append("\n");
    sb.append("    domainName: ").append(toIndentedString(domainName)).append("\n");
    sb.append("    ftpEnabled: ").append(toIndentedString(ftpEnabled)).append("\n");
    sb.append("    ftpUsername: ").append(toIndentedString(ftpUsername)).append("\n");
    sb.append("    ip: ").append(toIndentedString(ip)).append("\n");
    sb.append("    ipType: ").append(toIndentedString(ipType)).append("\n");
    sb.append("    maxSize: ").append(toIndentedString(maxSize)).append("\n");
    sb.append("    maxWebspaceSize: ").append(toIndentedString(maxWebspaceSize)).append("\n");
    sb.append("    mysqlDatabaseNames: ").append(toIndentedString(mysqlDatabaseNames)).append("\n");
    sb.append("    phpVersion: ").append(toIndentedString(phpVersion)).append("\n");
    sb.append("    servicepackId: ").append(toIndentedString(servicepackId)).append("\n");
    sb.append("    sites: ").append(toIndentedString(sites)).append("\n");
    sb.append("    sshHost: ").append(toIndentedString(sshHost)).append("\n");
    sb.append("    sshUsername: ").append(toIndentedString(sshUsername)).append("\n");
    sb.append("    webspaceUsage: ").append(toIndentedString(webspaceUsage)).append("\n");
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
    openapiFields.add("actual_size");
    openapiFields.add("domain_name");
    openapiFields.add("ftp_enabled");
    openapiFields.add("ftp_username");
    openapiFields.add("ip");
    openapiFields.add("ip_type");
    openapiFields.add("max_size");
    openapiFields.add("max_webspace_size");
    openapiFields.add("mysql_database_names");
    openapiFields.add("php_version");
    openapiFields.add("servicepack_id");
    openapiFields.add("sites");
    openapiFields.add("ssh_host");
    openapiFields.add("ssh_username");
    openapiFields.add("webspace_usage");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LinuxHostingDetail
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LinuxHostingDetail.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LinuxHostingDetail is not found in the empty JSON string", LinuxHostingDetail.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LinuxHostingDetail.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LinuxHostingDetail` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("domain_name") != null && !jsonObj.get("domain_name").isJsonNull()) && !jsonObj.get("domain_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `domain_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("domain_name").toString()));
      }
      if ((jsonObj.get("ftp_username") != null && !jsonObj.get("ftp_username").isJsonNull()) && !jsonObj.get("ftp_username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ftp_username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ftp_username").toString()));
      }
      if ((jsonObj.get("ip") != null && !jsonObj.get("ip").isJsonNull()) && !jsonObj.get("ip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ip").toString()));
      }
      // validate the optional field `ip_type`
      if (jsonObj.get("ip_type") != null && !jsonObj.get("ip_type").isJsonNull()) {
        LinuxIpType.validateJsonElement(jsonObj.get("ip_type"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("mysql_database_names") != null && !jsonObj.get("mysql_database_names").isJsonNull() && !jsonObj.get("mysql_database_names").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `mysql_database_names` to be an array in the JSON string but got `%s`", jsonObj.get("mysql_database_names").toString()));
      }
      if ((jsonObj.get("php_version") != null && !jsonObj.get("php_version").isJsonNull()) && !jsonObj.get("php_version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `php_version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("php_version").toString()));
      }
      if (jsonObj.get("sites") != null && !jsonObj.get("sites").isJsonNull()) {
        JsonArray jsonArraysites = jsonObj.getAsJsonArray("sites");
        if (jsonArraysites != null) {
          // ensure the json data is an array
          if (!jsonObj.get("sites").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `sites` to be an array in the JSON string but got `%s`", jsonObj.get("sites").toString()));
          }

          // validate the optional field `sites` (array)
          for (int i = 0; i < jsonArraysites.size(); i++) {
            LinuxSite.validateJsonElement(jsonArraysites.get(i));
          };
        }
      }
      if ((jsonObj.get("ssh_host") != null && !jsonObj.get("ssh_host").isJsonNull()) && !jsonObj.get("ssh_host").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssh_host` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssh_host").toString()));
      }
      if ((jsonObj.get("ssh_username") != null && !jsonObj.get("ssh_username").isJsonNull()) && !jsonObj.get("ssh_username").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ssh_username` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ssh_username").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LinuxHostingDetail.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LinuxHostingDetail' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LinuxHostingDetail> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LinuxHostingDetail.class));

       return (TypeAdapter<T>) new TypeAdapter<LinuxHostingDetail>() {
           @Override
           public void write(JsonWriter out, LinuxHostingDetail value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LinuxHostingDetail read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LinuxHostingDetail given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LinuxHostingDetail
   * @throws IOException if the JSON string is invalid with respect to LinuxHostingDetail
   */
  public static LinuxHostingDetail fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LinuxHostingDetail.class);
  }

  /**
   * Convert an instance of LinuxHostingDetail to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

