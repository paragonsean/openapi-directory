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

import ApiClient from '../ApiClient';
import Alias from './Alias';
import AntiSpam from './AntiSpam';
import CatchAll from './CatchAll';
import MailZoneAccount from './MailZoneAccount';
import SmtpDomain from './SmtpDomain';

/**
 * The MailZone model module.
 * @module model/MailZone
 * @version v2
 */
class MailZone {
    /**
     * Constructs a new <code>MailZone</code>.
     * @alias module:model/MailZone
     */
    constructor() { 
        
        MailZone.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MailZone</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MailZone} obj Optional instance to populate.
     * @return {module:model/MailZone} The populated <code>MailZone</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MailZone();

            if (data.hasOwnProperty('aliases')) {
                obj['aliases'] = ApiClient.convertToType(data['aliases'], [Alias]);
            }
            if (data.hasOwnProperty('anti_spam')) {
                obj['anti_spam'] = AntiSpam.constructFromObject(data['anti_spam']);
            }
            if (data.hasOwnProperty('available_accounts')) {
                obj['available_accounts'] = ApiClient.convertToType(data['available_accounts'], [MailZoneAccount]);
            }
            if (data.hasOwnProperty('catch_all')) {
                obj['catch_all'] = CatchAll.constructFromObject(data['catch_all']);
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('smtp_domains')) {
                obj['smtp_domains'] = ApiClient.convertToType(data['smtp_domains'], [SmtpDomain]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MailZone</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MailZone</code>.
     */
    static validateJSON(data) {
        if (data['aliases']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['aliases'])) {
                throw new Error("Expected the field `aliases` to be an array in the JSON data but got " + data['aliases']);
            }
            // validate the optional field `aliases` (array)
            for (const item of data['aliases']) {
                Alias.validateJSON(item);
            };
        }
        // validate the optional field `anti_spam`
        if (data['anti_spam']) { // data not null
          AntiSpam.validateJSON(data['anti_spam']);
        }
        if (data['available_accounts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['available_accounts'])) {
                throw new Error("Expected the field `available_accounts` to be an array in the JSON data but got " + data['available_accounts']);
            }
            // validate the optional field `available_accounts` (array)
            for (const item of data['available_accounts']) {
                MailZoneAccount.validateJSON(item);
            };
        }
        // validate the optional field `catch_all`
        if (data['catch_all']) { // data not null
          CatchAll.validateJSON(data['catch_all']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['smtp_domains']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['smtp_domains'])) {
                throw new Error("Expected the field `smtp_domains` to be an array in the JSON data but got " + data['smtp_domains']);
            }
            // validate the optional field `smtp_domains` (array)
            for (const item of data['smtp_domains']) {
                SmtpDomain.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * List of aliases on the mail zone<br />  An alias is an e-mail address (alias) that automatically forwards received e-mails to another e-mail address (destination).
 * @member {Array.<module:model/Alias>} aliases
 */
MailZone.prototype['aliases'] = undefined;

/**
 * @member {module:model/AntiSpam} anti_spam
 */
MailZone.prototype['anti_spam'] = undefined;

/**
 * List of mail zone accounts with their mailbox size.
 * @member {Array.<module:model/MailZoneAccount>} available_accounts
 */
MailZone.prototype['available_accounts'] = undefined;

/**
 * @member {module:model/CatchAll} catch_all
 */
MailZone.prototype['catch_all'] = undefined;

/**
 * Indicates whether the mail zone is enabled.
 * @member {Boolean} enabled
 */
MailZone.prototype['enabled'] = undefined;

/**
 * @member {String} name
 */
MailZone.prototype['name'] = undefined;

/**
 * List of extra smtp domains on the mail zone<br />  SMTP domain names allow you to link multiple domain names to a single e-mail address.<br />  E-mails sent to an SMTP domain will be caught by the respective e-mail address on the main domain name.
 * @member {Array.<module:model/SmtpDomain>} smtp_domains
 */
MailZone.prototype['smtp_domains'] = undefined;






export default MailZone;

