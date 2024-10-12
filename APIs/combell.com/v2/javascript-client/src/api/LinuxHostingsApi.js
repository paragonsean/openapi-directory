/**
 * Public Api
 * # Introduction  This API allows resellers to manage their resources in a simple, programmatic way using HTTP requests.  # Conventions  ## Requests  The API supports different methods depending on the required action.  | Method | Description | ---  | --- | GET  | Retrieve resources in a collection or get a single resource.<br/>Getters will never have any effect on the queried resources. | POST  | Create a new resource in a collection. | PUT  | Update an existing resource with its new representation. | DELETE | Delete an existing resource.  ## HTTP status codes  The API will reply with different HTTP statuscodes:  | StatusCode    | Description | ---      | --- | 200 OK     | The requests was processed and you receive data as a result. | 201 CREATED    | The resource has been created. Either the Location header contains a link to the created resource, or links are being returned in the response body. The applied method will be indicated in the documentation. | 202 ACCEPTED    | The request has been validated and accepted. Because we need to do some background processing prior to returning the result, we cannot send back a useful representation. | 204 NOCONTENT    | The request has been processed, but no details can be returned. | 400 BADREQUEST   | Your request is malformed. | 401 UNAUTHORIZED   | You are not authorized. Follow the instructions in the Authorization documentation. | 403 FORBIDDEN    | Access to the resource or operation is not allowed. | 404 NOTFOUND    | The resource cannot be found. | 410 GONE                  | The resource is permanently no longer available. | 429 TOOMANYREQUESTS  | The ratelimit has been exceeded. Please refer to the documentation on rate limiting for more details. | 500 INTERNALSERVERERROR | An error occurred during the processing of the request. The error is unexpected and most likely due to a bug in the api.  In the event of a problem, the body of the response will usually contain an errorcode and errormessage. In rare cases additional details about the error are reported.  Errorcodes 400-499 are considered to be client errors and indicate that there was an issue with the request. We will not take any action besides monitoring.   Errorcodes 500-599 are considered to be server errors. The errors are monitored AND action will be taken to resolve the error.  ## Formatting  Snake casing is applied on resources and query parameters. The API is strictly returning JSON. No other formats are supported.  Datetimes are returned in ISO-8601 format.  ## Pagination  Pagination is on by default on collections and is controlled by specifying *skip* and *take* parameters.   **Skip** indicates the number of results to skip and where to start the new take.   **Take** indicates the number of records to return. The returned number of items can be smaller than the requested take.  Paged results will have headers with useful information regarding the paging.  | Header    | Description | ---     | --- | X-Paging-Skipped  | The number of results that have been skipped. | X-Paging-Take   | The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. | X-Paging-TotalResults | The total number of results regardless of paging.  ## Rate limiting  The number of requests per interval is limited. Detailed information on the rate limiting can be found in specific headers which will be sent on each request.  | Header    | Description | ---     | --- | X-RateLimit-Limit  | The number of requests that can be made in a specific time interval. | X-RateLimit-Usage  | The number of requests already made in the current time interval. | X-RateLimit-Remaining | The number of requests remaining until the reset. | X-RateLimit-Reset  | The number of seconds until the reset.<br />After the reset you are allowed to make as many requests as specified by the X-RateLimit-Limit header. | Retry-After   | The number of seconds you have to wait until you can make new requests.<br />This header is only present when the rate limit has been reached. It is identical to X-RateLimit-Reset.  When the ratelimit has been reached, all requests will return with a HTTP statuscode 429 and ReasonPhrase '*Too many requests, retry later.*'.  # Authentication  The Api uses HMAC authentication.   Hash-based message authentication code (HMAC) is a mechanism for calculating a message authentication code involving a hash function in combination with a secret key.   Both the integrity and the authenticity of the message are verified this way.  ## Steps to generate the HMAC  1. Get your api key and secret from your controlpanel.   It is absolutely vital that the secret is never exposed. Once the secret is out, anyone would be able to generate hmacs to impersonate you.   In case your secret is compromised, you can generate a new api key and secret on your controlpanel. 2. Construct the input value for generating the hmac.   Concatenate:apikey, request method, path and querystring information, unix timestamp, nonce and content.  |          | Description | ---         | --- | apikey        | The key that is linked to your user. | request method      | lowercased (eg: get, post, delete,...) | path and querystring information  | urlencoding of the lowercased relative path and querystring.<br />The path **MUST start with the api version (/v2)**.<br />The hexadecimal codes (percent encoding) MUST be uppercased. | unix timestamp      | the unix timestamp in **seconds**. | nonce         | a unique string for each request. It should be a random string, not related to the request. The nonce (in combination with the unix timestamp) protects you from replay attacks in case anyone was able to intercept a request. | content        | When the request body is not empty, this should be the Base64 encoded Md5 hash of the request body.<br />An empty body should not be encoded.  3. Hash the concatenated string using your api secret and the SHA-256 algorithm. 4. Base64 encode the result of the hash function. This is the hmac signature you will need to send an authorized request.  ## Sending an authorized request  An authorized request can be made by sending the generated HMAC in the authorization header.   A correct authorizationheader uses the hmac authorization scheme and a correctly formatted authorization parameter.  Create the authorization parameter by concatenating:   * apikey   * colon ':'   * generated HMAC signature (see above)   * colon ':'   * nonce (the one used to generate the signature)   * colon ':'   * unix timestamp (the one used to generate the signature)  A sample (illustrated):  * The first line is the string you create to feed to the hashing algorithm. * The second line is the authorization header that should be sent in the request.  ![hmac authorization header illustrated](/v2/images/authentication_illustration.jpg \"authorization header illustrated\")  ## IP whitelisting  Access is by default restricted for all IP addresses. You need to explicitly whitelist an IP or an IP range in your controlpanel.  # Versioning  Because of breaking contract changes compared to v1, we released v2 of the API.   V1 will still be available, but you are strongly encouraged to migrate to the latest version.   New features will only be available on v2.  # Policy  ### Fair use policy  Please respect the rate limits and do not use the api for any purposes of abuse.   All requests are being monitored and logged.   Intentional abuse might result in api key revocation.  # Errors  The API attempts to return appropriate HTTP status codes for every request.   When the status code indicates failure, the API will also provide an error message in most cases.  An error message contains a machine-parseable error code accompanied by a descriptive error text.   The text for an error message might change over time, but codes will stay the same.  [An overview of error codes can be found here](/v2/documentation/errorcodes).  # Change log  [An overview of new changes can be found here](/v2/documentation/changelog).  # Provisioning information  ## Terminology  | Term   | Definition                | | ---   | ---                  | | Servicepack | Defines a set of assets that belong together. An example is a hosting package which offers Linux hosting, a domain name, a couple of mailboxes and databases.<br/>It also limits the size of individual assets within the same account. | | Account  | Represents an instance of the servicepack. It contains one or more assets. The number and size of assets is defined by the servicepack. | | Asset   | A manageable service. For example: a mysql database, a linux hosting, a mailbox,...<br/>Some assets are created at the moment when the account is created. Other assets can be created afterwards.   ## Common provisioning scenario  **Provisioning of an account with Linux hosting with one MySql database**  *Without a pre-existing account:*  1. Create a new account.<br/>Perform a POST on the accounts route and provide the desired servicepack id and identifier (domain name). 2. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 3. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 4. The created resource will point to an account. You now know the account's Id and can continue with the provisioning of a MySql database on this account. 5. Perform a POST on the mysqldatabases route and provide the account id along with other requested information. 6. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 7. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 8. The created resource will point to a MySql database resource.  ## SSL certificate requests  **Requesting an SSL certificate causes the purchase of a paying product.**  1. A certificate is created by adding an ssl certificate request. 2. Upon statuscode 201 you should query for certificate completion on the resource provided in the location response header. 3. The resource request can respond with different statuscodes: <ul>     <li>200: the certificate request is ongoing.<br/> Check the validations collection for validation values that are not auto_validated. Those should be set by you system.<br/> Call verify domain validations once all validation values are in place. It might take some time for verification to take place. It is not necessary to call this method more than once.</li>     <li>303: the certificate request is complete; there is no more certificate request resource available. Check the location header value to retrieve the representation of the resulting ssl certificate.</li>     <li>410: the certificate request does not exist anymore, there is no certificate created as a result of the request.</li> </ul>
 *
 * The version of the OpenAPI document: v2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AddHostHeaderRequest from '../model/AddHostHeaderRequest';
import AddSshKeyRequest from '../model/AddSshKeyRequest';
import AddSubsiteRequest from '../model/AddSubsiteRequest';
import AutoRedirectConfig from '../model/AutoRedirectConfig';
import FtpConfiguration from '../model/FtpConfiguration';
import GzipConfig from '../model/GzipConfig';
import Http2Configuration from '../model/Http2Configuration';
import LetsEncryptConfig from '../model/LetsEncryptConfig';
import LinuxHosting from '../model/LinuxHosting';
import LinuxHostingDetail from '../model/LinuxHostingDetail';
import PhpVersion from '../model/PhpVersion';
import ScheduledTask from '../model/ScheduledTask';
import SshConfiguration from '../model/SshConfiguration';
import SshKey from '../model/SshKey';
import UpdatePhpAPcuRequest from '../model/UpdatePhpAPcuRequest';
import UpdatePhpMemoryLimitRequest from '../model/UpdatePhpMemoryLimitRequest';

/**
* LinuxHostings service.
* @module api/LinuxHostingsApi
* @version v2
*/
export default class LinuxHostingsApi {

    /**
    * Constructs a new LinuxHostingsApi. 
    * @alias module:api/LinuxHostingsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the addScheduledTasks operation.
     * @callback module:api/LinuxHostingsApi~addScheduledTasksCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a scheduled task
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/ScheduledTask} [scheduledTask] 
     * @param {module:api/LinuxHostingsApi~addScheduledTasksCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addScheduledTasks(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['scheduledTask'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling addScheduledTasks");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling addScheduledTasks");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/scheduledtasks', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the addSshKey operation.
     * @callback module:api/LinuxHostingsApi~addSshKeyCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add a SSH key
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/AddSshKeyRequest} [addSshKeyRequest] SSH key public key.
     * @param {module:api/LinuxHostingsApi~addSshKeyCallback} callback The callback function, accepting three arguments: error, data, response
     */
    addSshKey(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['addSshKeyRequest'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling addSshKey");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling addSshKey");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/ssh/keys', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changeApcu operation.
     * @callback module:api/LinuxHostingsApi~changeApcuCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure PHP APCu setting
     * @param {String} domainName Linux hosting domain name
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdatePhpAPcuRequest} [updatePhpAPcuRequest] Php APcu config
     * @param {module:api/LinuxHostingsApi~changeApcuCallback} callback The callback function, accepting three arguments: error, data, response
     */
    changeApcu(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['updatePhpAPcuRequest'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling changeApcu");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling changeApcu");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/phpsettings/apcu', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changeAutoRedirect operation.
     * @callback module:api/LinuxHostingsApi~changeAutoRedirectCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure auto redirect
     * @param {String} domainName Linux hosting domain name.
     * @param {String} hostname Specific hostname.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/AutoRedirectConfig} [autoRedirectConfig] Auto redirect config.
     * @param {module:api/LinuxHostingsApi~changeAutoRedirectCallback} callback The callback function, accepting three arguments: error, data, response
     */
    changeAutoRedirect(domainName, hostname, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['autoRedirectConfig'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling changeAutoRedirect");
      }
      // verify the required parameter 'hostname' is set
      if (hostname === undefined || hostname === null) {
        throw new Error("Missing the required parameter 'hostname' when calling changeAutoRedirect");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling changeAutoRedirect");
      }

      let pathParams = {
        'hostname': hostname,
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/sslsettings/{hostname}/autoredirect', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changeGzipCompression operation.
     * @callback module:api/LinuxHostingsApi~changeGzipCompressionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Enable/disable GZIP compression
     * @param {String} domainName Linux hosting domain name
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/GzipConfig} [gzipConfig] Whether GZIP compression is enabled or not.
     * @param {module:api/LinuxHostingsApi~changeGzipCompressionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    changeGzipCompression(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['gzipConfig'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling changeGzipCompression");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling changeGzipCompression");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/settings/gzipcompression', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changeLetsEncrypt operation.
     * @callback module:api/LinuxHostingsApi~changeLetsEncryptCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure let's encrypt
     * @param {String} domainName Linux hosting domain name.
     * @param {String} hostname Specific hostname.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/LetsEncryptConfig} [letsEncryptConfig] Let's encrypt config.
     * @param {module:api/LinuxHostingsApi~changeLetsEncryptCallback} callback The callback function, accepting three arguments: error, data, response
     */
    changeLetsEncrypt(domainName, hostname, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['letsEncryptConfig'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling changeLetsEncrypt");
      }
      // verify the required parameter 'hostname' is set
      if (hostname === undefined || hostname === null) {
        throw new Error("Missing the required parameter 'hostname' when calling changeLetsEncrypt");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling changeLetsEncrypt");
      }

      let pathParams = {
        'hostname': hostname,
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/sslsettings/{hostname}/letsencrypt', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changePhpMemoryLimit operation.
     * @callback module:api/LinuxHostingsApi~changePhpMemoryLimitCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure PHP memory limit
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdatePhpMemoryLimitRequest} [updatePhpMemoryLimitRequest] Memory limit config
     * @param {module:api/LinuxHostingsApi~changePhpMemoryLimitCallback} callback The callback function, accepting three arguments: error, data, response
     */
    changePhpMemoryLimit(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['updatePhpMemoryLimitRequest'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling changePhpMemoryLimit");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling changePhpMemoryLimit");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/phpsettings/memorylimit', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the changePhpVersion operation.
     * @callback module:api/LinuxHostingsApi~changePhpVersionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Change the Linux hosting PHP version.
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/PhpVersion} [phpVersion] The new PHP version.
     * @param {module:api/LinuxHostingsApi~changePhpVersionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    changePhpVersion(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['phpVersion'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling changePhpVersion");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling changePhpVersion");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/phpsettings/version', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configureFtp operation.
     * @callback module:api/LinuxHostingsApi~configureFtpCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure FTP
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/FtpConfiguration} [ftpConfiguration] 
     * @param {module:api/LinuxHostingsApi~configureFtpCallback} callback The callback function, accepting three arguments: error, data, response
     */
    configureFtp(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['ftpConfiguration'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling configureFtp");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling configureFtp");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/ftp/configuration', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configureHttp2 operation.
     * @callback module:api/LinuxHostingsApi~configureHttp2Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure HTTP/2
     * @param {String} domainName Linux hosting domain name.
     * @param {String} siteName Site name where HTTP/2 should be configured.<br />  For HTTP/2 to work correctly, the site must have ssl enabled.
     * @param {String} domainName2 Automatically added
     * @param {String} siteName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/Http2Configuration} [http2Configuration] 
     * @param {module:api/LinuxHostingsApi~configureHttp2Callback} callback The callback function, accepting three arguments: error, data, response
     */
    configureHttp2(domainName, siteName, domainName2, siteName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['http2Configuration'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling configureHttp2");
      }
      // verify the required parameter 'siteName' is set
      if (siteName === undefined || siteName === null) {
        throw new Error("Missing the required parameter 'siteName' when calling configureHttp2");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling configureHttp2");
      }
      // verify the required parameter 'siteName2' is set
      if (siteName2 === undefined || siteName2 === null) {
        throw new Error("Missing the required parameter 'siteName2' when calling configureHttp2");
      }

      let pathParams = {
        'domainName': domainName2,
        'siteName': siteName2
      };
      let queryParams = {
        'domain_name': domainName,
        'site_name': siteName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/sites/{siteName}/http2/configuration', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configureScheduledTask operation.
     * @callback module:api/LinuxHostingsApi~configureScheduledTaskCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure a scheduled task
     * @param {String} domainName Linux hosting domain name.
     * @param {String} scheduledTaskId Id of the scheduled task.
     * @param {String} domainName2 Automatically added
     * @param {String} scheduledTaskId2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/ScheduledTask} [scheduledTask] 
     * @param {module:api/LinuxHostingsApi~configureScheduledTaskCallback} callback The callback function, accepting three arguments: error, data, response
     */
    configureScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, opts, callback) {
      opts = opts || {};
      let postBody = opts['scheduledTask'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling configureScheduledTask");
      }
      // verify the required parameter 'scheduledTaskId' is set
      if (scheduledTaskId === undefined || scheduledTaskId === null) {
        throw new Error("Missing the required parameter 'scheduledTaskId' when calling configureScheduledTask");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling configureScheduledTask");
      }
      // verify the required parameter 'scheduledTaskId2' is set
      if (scheduledTaskId2 === undefined || scheduledTaskId2 === null) {
        throw new Error("Missing the required parameter 'scheduledTaskId2' when calling configureScheduledTask");
      }

      let pathParams = {
        'domainName': domainName2,
        'scheduledTaskId': scheduledTaskId2
      };
      let queryParams = {
        'domain_name': domainName,
        'scheduled_task_id': scheduledTaskId
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the configureSsh operation.
     * @callback module:api/LinuxHostingsApi~configureSshCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Configure SSH
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/SshConfiguration} [sshConfiguration] 
     * @param {module:api/LinuxHostingsApi~configureSshCallback} callback The callback function, accepting three arguments: error, data, response
     */
    configureSsh(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['sshConfiguration'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling configureSsh");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling configureSsh");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/ssh/configuration', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createHostHeader operation.
     * @callback module:api/LinuxHostingsApi~createHostHeaderCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a host header
     * @param {String} domainName Linux hosting domain name.
     * @param {String} siteName Name of the site on the linux hosting.
     * @param {String} domainName2 Automatically added
     * @param {String} siteName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/AddHostHeaderRequest} [addHostHeaderRequest] Add host header request
     * @param {module:api/LinuxHostingsApi~createHostHeaderCallback} callback The callback function, accepting three arguments: error, data, response
     */
    createHostHeader(domainName, siteName, domainName2, siteName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['addHostHeaderRequest'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling createHostHeader");
      }
      // verify the required parameter 'siteName' is set
      if (siteName === undefined || siteName === null) {
        throw new Error("Missing the required parameter 'siteName' when calling createHostHeader");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling createHostHeader");
      }
      // verify the required parameter 'siteName2' is set
      if (siteName2 === undefined || siteName2 === null) {
        throw new Error("Missing the required parameter 'siteName2' when calling createHostHeader");
      }

      let pathParams = {
        'domainName': domainName2,
        'siteName': siteName2
      };
      let queryParams = {
        'domain_name': domainName,
        'site_name': siteName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/sites/{siteName}/hostheaders', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createSubsite operation.
     * @callback module:api/LinuxHostingsApi~createSubsiteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a subsite
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {Object} opts Optional parameters
     * @param {module:model/AddSubsiteRequest} [addSubsiteRequest] Add subsite request
     * @param {module:api/LinuxHostingsApi~createSubsiteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    createSubsite(domainName, domainName2, opts, callback) {
      opts = opts || {};
      let postBody = opts['addSubsiteRequest'];
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling createSubsite");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling createSubsite");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/subsites', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteScheduledTask operation.
     * @callback module:api/LinuxHostingsApi~deleteScheduledTaskCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a scheduled task
     * @param {String} domainName Linux hosting domain name.
     * @param {String} scheduledTaskId Id of the scheduled task.
     * @param {String} domainName2 Automatically added
     * @param {String} scheduledTaskId2 Automatically added
     * @param {module:api/LinuxHostingsApi~deleteScheduledTaskCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling deleteScheduledTask");
      }
      // verify the required parameter 'scheduledTaskId' is set
      if (scheduledTaskId === undefined || scheduledTaskId === null) {
        throw new Error("Missing the required parameter 'scheduledTaskId' when calling deleteScheduledTask");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling deleteScheduledTask");
      }
      // verify the required parameter 'scheduledTaskId2' is set
      if (scheduledTaskId2 === undefined || scheduledTaskId2 === null) {
        throw new Error("Missing the required parameter 'scheduledTaskId2' when calling deleteScheduledTask");
      }

      let pathParams = {
        'domainName': domainName2,
        'scheduledTaskId': scheduledTaskId2
      };
      let queryParams = {
        'domain_name': domainName,
        'scheduled_task_id': scheduledTaskId
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteSshKey operation.
     * @callback module:api/LinuxHostingsApi~deleteSshKeyCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a SSH key
     * @param {String} domainName Linux hosting domain name.
     * @param {String} fingerprint Fingerprint of public key.
     * @param {String} domainName2 Automatically added
     * @param {module:api/LinuxHostingsApi~deleteSshKeyCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteSshKey(domainName, fingerprint, domainName2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling deleteSshKey");
      }
      // verify the required parameter 'fingerprint' is set
      if (fingerprint === undefined || fingerprint === null) {
        throw new Error("Missing the required parameter 'fingerprint' when calling deleteSshKey");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling deleteSshKey");
      }

      let pathParams = {
        'fingerprint': fingerprint,
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/ssh/keys/{fingerprint}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteSubsite operation.
     * @callback module:api/LinuxHostingsApi~deleteSubsiteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a subsite
     * @param {String} domainName Linux hosting domain name.
     * @param {String} siteName Name of the site on the linux hosting.
     * @param {String} domainName2 Automatically added
     * @param {String} siteName2 Automatically added
     * @param {module:api/LinuxHostingsApi~deleteSubsiteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteSubsite(domainName, siteName, domainName2, siteName2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling deleteSubsite");
      }
      // verify the required parameter 'siteName' is set
      if (siteName === undefined || siteName === null) {
        throw new Error("Missing the required parameter 'siteName' when calling deleteSubsite");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling deleteSubsite");
      }
      // verify the required parameter 'siteName2' is set
      if (siteName2 === undefined || siteName2 === null) {
        throw new Error("Missing the required parameter 'siteName2' when calling deleteSubsite");
      }

      let pathParams = {
        'domainName': domainName2,
        'siteName': siteName2
      };
      let queryParams = {
        'domain_name': domainName,
        'site_name': siteName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/subsites/{siteName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getAvailablePhpVersions operation.
     * @callback module:api/LinuxHostingsApi~getAvailablePhpVersionsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/PhpVersion>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the available PHP versions.
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {module:api/LinuxHostingsApi~getAvailablePhpVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/PhpVersion>}
     */
    getAvailablePhpVersions(domainName, domainName2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling getAvailablePhpVersions");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling getAvailablePhpVersions");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [PhpVersion];
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/phpsettings/availableversions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinuxHosting operation.
     * @callback module:api/LinuxHostingsApi~getLinuxHostingCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LinuxHostingDetail} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Linux hosting detail
     * @param {String} domainName The Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {module:api/LinuxHostingsApi~getLinuxHostingCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LinuxHostingDetail}
     */
    getLinuxHosting(domainName, domainName2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling getLinuxHosting");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling getLinuxHosting");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LinuxHostingDetail;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLinuxHostings operation.
     * @callback module:api/LinuxHostingsApi~getLinuxHostingsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/LinuxHosting>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Overview of linux hostings
     * @param {Object} opts Optional parameters
     * @param {Number} [skip] The number of items to skip in the resultset.
     * @param {Number} [take] The number of items to return in the resultset. The returned count can be equal or less than this number.
     * @param {module:api/LinuxHostingsApi~getLinuxHostingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/LinuxHosting>}
     */
    getLinuxHostings(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'skip': opts['skip'],
        'take': opts['take']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [LinuxHosting];
      return this.apiClient.callApi(
        '/linuxhostings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getScheduledTask operation.
     * @callback module:api/LinuxHostingsApi~getScheduledTaskCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScheduledTask} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get scheduled task detail
     * @param {String} domainName Linux hosting domain name.
     * @param {String} scheduledTaskId Id of the scheduled task.
     * @param {String} domainName2 Automatically added
     * @param {String} scheduledTaskId2 Automatically added
     * @param {module:api/LinuxHostingsApi~getScheduledTaskCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScheduledTask}
     */
    getScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling getScheduledTask");
      }
      // verify the required parameter 'scheduledTaskId' is set
      if (scheduledTaskId === undefined || scheduledTaskId === null) {
        throw new Error("Missing the required parameter 'scheduledTaskId' when calling getScheduledTask");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling getScheduledTask");
      }
      // verify the required parameter 'scheduledTaskId2' is set
      if (scheduledTaskId2 === undefined || scheduledTaskId2 === null) {
        throw new Error("Missing the required parameter 'scheduledTaskId2' when calling getScheduledTask");
      }

      let pathParams = {
        'domainName': domainName2,
        'scheduledTaskId': scheduledTaskId2
      };
      let queryParams = {
        'domain_name': domainName,
        'scheduled_task_id': scheduledTaskId
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ScheduledTask;
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getScheduledTasks operation.
     * @callback module:api/LinuxHostingsApi~getScheduledTasksCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ScheduledTask>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Overview of scheduled tasks
     * Manage scheduled tasks which are also manageable via the control panel.
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {module:api/LinuxHostingsApi~getScheduledTasksCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ScheduledTask>}
     */
    getScheduledTasks(domainName, domainName2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling getScheduledTasks");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling getScheduledTasks");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [ScheduledTask];
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/scheduledtasks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSshKeys operation.
     * @callback module:api/LinuxHostingsApi~getSshKeysCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SshKey>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Overview of SSH keys
     * @param {String} domainName Linux hosting domain name.
     * @param {String} domainName2 Automatically added
     * @param {module:api/LinuxHostingsApi~getSshKeysCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SshKey>}
     */
    getSshKeys(domainName, domainName2, callback) {
      let postBody = null;
      // verify the required parameter 'domainName' is set
      if (domainName === undefined || domainName === null) {
        throw new Error("Missing the required parameter 'domainName' when calling getSshKeys");
      }
      // verify the required parameter 'domainName2' is set
      if (domainName2 === undefined || domainName2 === null) {
        throw new Error("Missing the required parameter 'domainName2' when calling getSshKeys");
      }

      let pathParams = {
        'domainName': domainName2
      };
      let queryParams = {
        'domain_name': domainName
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [SshKey];
      return this.apiClient.callApi(
        '/linuxhostings/{domainName}/ssh/keys', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
