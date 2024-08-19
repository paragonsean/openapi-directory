/**
 * Paylocity API
 * For general questions and support of the API, contact: webservices@paylocity.com  # Overview    Paylocity Web Services API is an externally facing RESTful Internet protocol. The Paylocity API uses HTTP verbs and a RESTful endpoint structure. OAuth 2.0 is used as the API Authorization framework. Request and response payloads are formatted as JSON.  Paylocity supports v1 and v2 versions of its API endpoints. v1, while supported, won't be enhanced with additional functionality. For direct link to v1 documentation, please click [here](https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm). For additional resources regarding v1/v2 differences and conversion path, please contact webservices@paylocity.com.    ##### Setup    Paylocity will provide the secure client credentials and set up the scope (type of requests and allowed company numbers). You will receive the unique client id, secret, and Paylocity public key for the data encryption. The secret will expire in 365 days.   * Paylocity will send you an e-mail 10 days prior to the expiration date for the current secret. If not renewed, the second e-mail notification will be sent 5 days prior to secret's expiration. Each email will contain the code necessary to renew the client secret.   * You can obtain the new secret by calling API endpoint using your current not yet expired credentials and the code that was sent with the notification email. For details on API endpoint, please see Client Credentials section.   * Both the current secret value and the new secret value will be recognized during the transition period. After the current secret expires, you must use the new secret.   * If you were unable to renew the secret via API endpoint, you can still contact Service and they will email you new secret via secure email.      When validating the request, Paylocity API will honor the defaults and required fields set up for the company default New Hire Template as defined in Web Pay.      # Authorization    Paylocity Web Services API uses OAuth2.0 Authentication with JSON Message Format.      All requests of the Paylocity Web Services API require a bearer token which can be obtained by authenticating the client with the Paylocity Web Services API via OAuth 2.0.      The client must request a bearer token from the authorization endpoint:      auth-server for production: https://api.paylocity.com/IdentityServer/connect/token      auth-server for testing: https://apisandbox.paylocity.com/IdentityServer/connect/token    Paylocity reserves the right to impose rate limits on the number of calls made to our APIs. Changes to API features/functionality may be made at anytime with or without prior notice.    ##### Authorization Header    The request is expected to be in the form of a basic authentication request, with the \"Authorization\" header containing the client-id and client-secret. This means the standard base-64 encoded user:password, prefixed with \"Basic\" as the value for the Authorization header, where user is the client-id and password is the client-secret.    ##### Content-Type Header    The \"Content-Type\" header is required to be \"application/x-www-form-urlencoded\".    ##### Additional Values    The request must post the following form encoded values within the request body:        grant_type = client_credentials      scope = WebLinkAPI    ##### Responses    Success will return HTTP 200 OK with JSON content:        {        \"access_token\": \"xxx\",        \"expires_in\": 3600,        \"token_type\": \"Bearer\"      }    # Encryption    Paylocity uses a combination of RSA and AES cryptography. As part of the setup, each client is issued a public RSA key.    Paylocity recommends the encryption of the incoming requests as additional protection of the sensitive data. Clients can opt-out of the encryption during the initial setup process. Opt-out will allow Paylocity to process unencrypted requests.    The Paylocity Public Key has the following properties:    * 2048 bit key size    * PKCS1 key format    * PEM encoding    ##### Properties    * key (base 64 encoded): The AES symmetric key encrypted with the Paylocity Public Key. It is the key used to encrypt the content. Paylocity will decrypt the AES key using RSA decryption and use it to decrypt the content.    * iv (base 64 encoded): The AES IV (Initialization Vector) used when encrypting the content.    * content (base 64 encoded): The AES encrypted request. The key and iv provided in the secureContent request are used by Paylocity for decryption of the content.    We suggest using the following for the AES:    * CBC cipher mode    * PKCS7 padding    * 128 bit block size    * 256 bit key size    ##### Encryption Flow    * Generate the unencrypted JSON payload to POST/PUT  * Encrypt this JSON payload using your _own key and IV_ (NOT with the Paylocity public key)  * RSA encrypt the _key_ you used in step 2 with the Paylocity Public Key, then, base64 encode the result  * Base64 encode the IV used to encrypt the JSON payload in step 2  * Put together a \"securecontent\" JSON object:     {    'secureContent' : {      'key' : -- RSA-encrypted & base64 encoded key from step 3,      'iv' : -- base64 encoded iv from step 4      'content' -- content encrypted with your own key from step 2, base64 encoded    }  }    ##### Sample Example        {        \"secureContent\": {          \"key\": \"eS3aw6H/qzHMJ00gSi6gQ3xa08DPMazk8BFY96Pd99ODA==\",          \"iv\": \"NLyXMGq9svw0XO5aI9BzWw==\",          \"content\": \"gAEOiQltO1w+LzGUoIK8FiYbU42hug94EasSl7N+Q1w=\"        }      }    ##### Sample C# Code        using Newtonsoft.Json;      using System;      using System.IO;      using System.Security.Cryptography;      using System.Text;        public class SecuredContent      {        [JsonProperty(\"key\")]        public string Key { get; set; }          [JsonProperty(\"iv\")]        public string Iv { get; set; }          [JsonProperty(\"content\")]        public string Content { get; set; }        }        public class EndUserSecureRequestExample      {        public string CreateSecuredRequest(FileInfo paylocityPublicKey, string unsecuredJsonRequest)        {          string publicKeyXml = File.ReadAllText(paylocityPublicKey.FullName, Encoding.UTF8);            SecuredContent secureContent = this.CreateSecuredContent(publicKeyXml, unsecuredJsonRequest);            string secureRequest = JsonConvert.SerializeObject(new { secureContent });            return secureRequest;        }          private SecuredContent CreateSecuredContent(string publicKeyXml, string request)        {          using (AesCryptoServiceProvider aesCsp = new AesCryptoServiceProvider())          {            aesCsp.Mode = CipherMode.CBC;            aesCsp.Padding = PaddingMode.PKCS7;            aesCsp.BlockSize = 128;            aesCsp.KeySize = 256;              using (ICryptoTransform crt = aesCsp.CreateEncryptor(aesCsp.Key, aesCsp.IV))            {              using (MemoryStream outputStream = new MemoryStream())              {                using (CryptoStream encryptStream = new CryptoStream(outputStream, crt, CryptoStreamMode.Write))                {                  byte[] encodedRequest = Encoding.UTF8.GetBytes(request);                  encryptStream.Write(encodedRequest, 0, encodedRequest.Length);                  encryptStream.FlushFinalBlock();                  byte[] encryptedRequest = outputStream.ToArray();                    using (RSACryptoServiceProvider crp = new RSACryptoServiceProvider())                  {                    crp.FromXmlstring(publicKeyXml);                    byte[] encryptedKey = crp.Encrypt(aesCsp.Key, false);                      return new SecuredContent()                    {                      Key = Convert.ToBase64string(encryptedKey),                      Iv = Convert.ToBase64string(aesCsp.IV),                      Content = Convert.ToBase64string(encryptedRequest)                    };                  }                }              }            }          }        }      }    ## Support    Questions about using the Paylocity API? Please contact webservices@paylocity.com.    # Deductions (v1)    Deductions API provides endpoints to retrieve, add, update and delete deductions for a company's employees. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.    # OnBoarding (v1)    Onboarding API sends employee data into Paylocity Onboarding to help ensure an easy and accurate hiring process for subsequent completion into Web Pay. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.
 *
 * The version of the OpenAPI document: 2
 * Contact: webservices@paylocity.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The StagedEmployeeWorkEligibilityInner model module.
 * @module model/StagedEmployeeWorkEligibilityInner
 * @version 2
 */
class StagedEmployeeWorkEligibilityInner {
    /**
     * Constructs a new <code>StagedEmployeeWorkEligibilityInner</code>.
     * The Work Eligibility model
     * @alias module:model/StagedEmployeeWorkEligibilityInner
     */
    constructor() { 
        
        StagedEmployeeWorkEligibilityInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>StagedEmployeeWorkEligibilityInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StagedEmployeeWorkEligibilityInner} obj Optional instance to populate.
     * @return {module:model/StagedEmployeeWorkEligibilityInner} The populated <code>StagedEmployeeWorkEligibilityInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StagedEmployeeWorkEligibilityInner();

            if (data.hasOwnProperty('alienOrAdmissionDocumentNumber')) {
                obj['alienOrAdmissionDocumentNumber'] = ApiClient.convertToType(data['alienOrAdmissionDocumentNumber'], 'String');
            }
            if (data.hasOwnProperty('attestedDate')) {
                obj['attestedDate'] = ApiClient.convertToType(data['attestedDate'], 'String');
            }
            if (data.hasOwnProperty('countryOfIssuance')) {
                obj['countryOfIssuance'] = ApiClient.convertToType(data['countryOfIssuance'], 'String');
            }
            if (data.hasOwnProperty('foreignPassportNumber')) {
                obj['foreignPassportNumber'] = ApiClient.convertToType(data['foreignPassportNumber'], 'String');
            }
            if (data.hasOwnProperty('i94AdmissionNumber')) {
                obj['i94AdmissionNumber'] = ApiClient.convertToType(data['i94AdmissionNumber'], 'String');
            }
            if (data.hasOwnProperty('i9DateVerified')) {
                obj['i9DateVerified'] = ApiClient.convertToType(data['i9DateVerified'], 'String');
            }
            if (data.hasOwnProperty('i9Notes')) {
                obj['i9Notes'] = ApiClient.convertToType(data['i9Notes'], 'String');
            }
            if (data.hasOwnProperty('isI9Verified')) {
                obj['isI9Verified'] = ApiClient.convertToType(data['isI9Verified'], 'Boolean');
            }
            if (data.hasOwnProperty('isSsnVerified')) {
                obj['isSsnVerified'] = ApiClient.convertToType(data['isSsnVerified'], 'Boolean');
            }
            if (data.hasOwnProperty('ssnDateVerified')) {
                obj['ssnDateVerified'] = ApiClient.convertToType(data['ssnDateVerified'], 'String');
            }
            if (data.hasOwnProperty('ssnNotes')) {
                obj['ssnNotes'] = ApiClient.convertToType(data['ssnNotes'], 'String');
            }
            if (data.hasOwnProperty('visaType')) {
                obj['visaType'] = ApiClient.convertToType(data['visaType'], 'String');
            }
            if (data.hasOwnProperty('workAuthorization')) {
                obj['workAuthorization'] = ApiClient.convertToType(data['workAuthorization'], 'String');
            }
            if (data.hasOwnProperty('workUntil')) {
                obj['workUntil'] = ApiClient.convertToType(data['workUntil'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StagedEmployeeWorkEligibilityInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StagedEmployeeWorkEligibilityInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['alienOrAdmissionDocumentNumber'] && !(typeof data['alienOrAdmissionDocumentNumber'] === 'string' || data['alienOrAdmissionDocumentNumber'] instanceof String)) {
            throw new Error("Expected the field `alienOrAdmissionDocumentNumber` to be a primitive type in the JSON string but got " + data['alienOrAdmissionDocumentNumber']);
        }
        // ensure the json data is a string
        if (data['attestedDate'] && !(typeof data['attestedDate'] === 'string' || data['attestedDate'] instanceof String)) {
            throw new Error("Expected the field `attestedDate` to be a primitive type in the JSON string but got " + data['attestedDate']);
        }
        // ensure the json data is a string
        if (data['countryOfIssuance'] && !(typeof data['countryOfIssuance'] === 'string' || data['countryOfIssuance'] instanceof String)) {
            throw new Error("Expected the field `countryOfIssuance` to be a primitive type in the JSON string but got " + data['countryOfIssuance']);
        }
        // ensure the json data is a string
        if (data['foreignPassportNumber'] && !(typeof data['foreignPassportNumber'] === 'string' || data['foreignPassportNumber'] instanceof String)) {
            throw new Error("Expected the field `foreignPassportNumber` to be a primitive type in the JSON string but got " + data['foreignPassportNumber']);
        }
        // ensure the json data is a string
        if (data['i94AdmissionNumber'] && !(typeof data['i94AdmissionNumber'] === 'string' || data['i94AdmissionNumber'] instanceof String)) {
            throw new Error("Expected the field `i94AdmissionNumber` to be a primitive type in the JSON string but got " + data['i94AdmissionNumber']);
        }
        // ensure the json data is a string
        if (data['i9DateVerified'] && !(typeof data['i9DateVerified'] === 'string' || data['i9DateVerified'] instanceof String)) {
            throw new Error("Expected the field `i9DateVerified` to be a primitive type in the JSON string but got " + data['i9DateVerified']);
        }
        // ensure the json data is a string
        if (data['i9Notes'] && !(typeof data['i9Notes'] === 'string' || data['i9Notes'] instanceof String)) {
            throw new Error("Expected the field `i9Notes` to be a primitive type in the JSON string but got " + data['i9Notes']);
        }
        // ensure the json data is a string
        if (data['ssnDateVerified'] && !(typeof data['ssnDateVerified'] === 'string' || data['ssnDateVerified'] instanceof String)) {
            throw new Error("Expected the field `ssnDateVerified` to be a primitive type in the JSON string but got " + data['ssnDateVerified']);
        }
        // ensure the json data is a string
        if (data['ssnNotes'] && !(typeof data['ssnNotes'] === 'string' || data['ssnNotes'] instanceof String)) {
            throw new Error("Expected the field `ssnNotes` to be a primitive type in the JSON string but got " + data['ssnNotes']);
        }
        // ensure the json data is a string
        if (data['visaType'] && !(typeof data['visaType'] === 'string' || data['visaType'] instanceof String)) {
            throw new Error("Expected the field `visaType` to be a primitive type in the JSON string but got " + data['visaType']);
        }
        // ensure the json data is a string
        if (data['workAuthorization'] && !(typeof data['workAuthorization'] === 'string' || data['workAuthorization'] instanceof String)) {
            throw new Error("Expected the field `workAuthorization` to be a primitive type in the JSON string but got " + data['workAuthorization']);
        }
        // ensure the json data is a string
        if (data['workUntil'] && !(typeof data['workUntil'] === 'string' || data['workUntil'] instanceof String)) {
            throw new Error("Expected the field `workUntil` to be a primitive type in the JSON string but got " + data['workUntil']);
        }

        return true;
    }


}



/**
 * Employee USCIS or Admission Number. <br  /> Must be 7-10 characters and may begin with an 'A'
 * @member {String} alienOrAdmissionDocumentNumber
 */
StagedEmployeeWorkEligibilityInner.prototype['alienOrAdmissionDocumentNumber'] = undefined;

/**
 * The date the I-9 Verification form was attested by Employer or Authorized representative. Common formats are *MM-DD-CCYY, CCYY-MM-DD*.
 * @member {String} attestedDate
 */
StagedEmployeeWorkEligibilityInner.prototype['attestedDate'] = undefined;

/**
 * If Foreign Passport number is provided, provide its country of issuance. Must match Paylocity setup.<br  /> Max length: 30
 * @member {String} countryOfIssuance
 */
StagedEmployeeWorkEligibilityInner.prototype['countryOfIssuance'] = undefined;

/**
 * Foreign Passport Number.<br  /> Max length: 50
 * @member {String} foreignPassportNumber
 */
StagedEmployeeWorkEligibilityInner.prototype['foreignPassportNumber'] = undefined;

/**
 * Form I-94 admission number.<br  /> Must be 11 numeric characters
 * @member {String} i94AdmissionNumber
 */
StagedEmployeeWorkEligibilityInner.prototype['i94AdmissionNumber'] = undefined;

/**
 * Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
 * @member {String} i9DateVerified
 */
StagedEmployeeWorkEligibilityInner.prototype['i9DateVerified'] = undefined;

/**
 * Notes regarding employee's i9.<br  /> Max length: 4000
 * @member {String} i9Notes
 */
StagedEmployeeWorkEligibilityInner.prototype['i9Notes'] = undefined;

/**
 * Indicates if employee I9 is verified.
 * @member {Boolean} isI9Verified
 */
StagedEmployeeWorkEligibilityInner.prototype['isI9Verified'] = undefined;

/**
 * Indicates if employee SSN is verified.
 * @member {Boolean} isSsnVerified
 */
StagedEmployeeWorkEligibilityInner.prototype['isSsnVerified'] = undefined;

/**
 * The date of employer verification of employee SSN. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
 * @member {String} ssnDateVerified
 */
StagedEmployeeWorkEligibilityInner.prototype['ssnDateVerified'] = undefined;

/**
 * Notes regarding employee's SSN.<br  /> Max length: 4000
 * @member {String} ssnNotes
 */
StagedEmployeeWorkEligibilityInner.prototype['ssnNotes'] = undefined;

/**
 * Employee Visa type. Must match one of the system coded values.<br  /> Max length: 100
 * @member {String} visaType
 */
StagedEmployeeWorkEligibilityInner.prototype['visaType'] = undefined;

/**
 * Employee work authorization. Must match one of the system coded values.<br  /> Max length: 100
 * @member {String} workAuthorization
 */
StagedEmployeeWorkEligibilityInner.prototype['workAuthorization'] = undefined;

/**
 * End date of employee work eligibility.  Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
 * @member {String} workUntil
 */
StagedEmployeeWorkEligibilityInner.prototype['workUntil'] = undefined;






export default StagedEmployeeWorkEligibilityInner;

