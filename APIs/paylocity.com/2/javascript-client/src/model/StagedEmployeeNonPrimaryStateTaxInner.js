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
 * The StagedEmployeeNonPrimaryStateTaxInner model module.
 * @module model/StagedEmployeeNonPrimaryStateTaxInner
 * @version 2
 */
class StagedEmployeeNonPrimaryStateTaxInner {
    /**
     * Constructs a new <code>StagedEmployeeNonPrimaryStateTaxInner</code>.
     * The Non-Primary State Tax model
     * @alias module:model/StagedEmployeeNonPrimaryStateTaxInner
     */
    constructor() { 
        
        StagedEmployeeNonPrimaryStateTaxInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>StagedEmployeeNonPrimaryStateTaxInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StagedEmployeeNonPrimaryStateTaxInner} obj Optional instance to populate.
     * @return {module:model/StagedEmployeeNonPrimaryStateTaxInner} The populated <code>StagedEmployeeNonPrimaryStateTaxInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StagedEmployeeNonPrimaryStateTaxInner();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('deductionsAmount')) {
                obj['deductionsAmount'] = ApiClient.convertToType(data['deductionsAmount'], 'Number');
            }
            if (data.hasOwnProperty('dependentsAmount')) {
                obj['dependentsAmount'] = ApiClient.convertToType(data['dependentsAmount'], 'Number');
            }
            if (data.hasOwnProperty('exemptions')) {
                obj['exemptions'] = ApiClient.convertToType(data['exemptions'], 'Number');
            }
            if (data.hasOwnProperty('exemptions2')) {
                obj['exemptions2'] = ApiClient.convertToType(data['exemptions2'], 'Number');
            }
            if (data.hasOwnProperty('filingStatus')) {
                obj['filingStatus'] = ApiClient.convertToType(data['filingStatus'], 'String');
            }
            if (data.hasOwnProperty('higherRate')) {
                obj['higherRate'] = ApiClient.convertToType(data['higherRate'], 'Boolean');
            }
            if (data.hasOwnProperty('otherIncomeAmount')) {
                obj['otherIncomeAmount'] = ApiClient.convertToType(data['otherIncomeAmount'], 'Number');
            }
            if (data.hasOwnProperty('percentage')) {
                obj['percentage'] = ApiClient.convertToType(data['percentage'], 'Number');
            }
            if (data.hasOwnProperty('reciprocityCode')) {
                obj['reciprocityCode'] = ApiClient.convertToType(data['reciprocityCode'], 'String');
            }
            if (data.hasOwnProperty('specialCheckCalc')) {
                obj['specialCheckCalc'] = ApiClient.convertToType(data['specialCheckCalc'], 'String');
            }
            if (data.hasOwnProperty('taxCalculationCode')) {
                obj['taxCalculationCode'] = ApiClient.convertToType(data['taxCalculationCode'], 'String');
            }
            if (data.hasOwnProperty('taxCode')) {
                obj['taxCode'] = ApiClient.convertToType(data['taxCode'], 'String');
            }
            if (data.hasOwnProperty('w4FormYear')) {
                obj['w4FormYear'] = ApiClient.convertToType(data['w4FormYear'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StagedEmployeeNonPrimaryStateTaxInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StagedEmployeeNonPrimaryStateTaxInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['filingStatus'] && !(typeof data['filingStatus'] === 'string' || data['filingStatus'] instanceof String)) {
            throw new Error("Expected the field `filingStatus` to be a primitive type in the JSON string but got " + data['filingStatus']);
        }
        // ensure the json data is a string
        if (data['reciprocityCode'] && !(typeof data['reciprocityCode'] === 'string' || data['reciprocityCode'] instanceof String)) {
            throw new Error("Expected the field `reciprocityCode` to be a primitive type in the JSON string but got " + data['reciprocityCode']);
        }
        // ensure the json data is a string
        if (data['specialCheckCalc'] && !(typeof data['specialCheckCalc'] === 'string' || data['specialCheckCalc'] instanceof String)) {
            throw new Error("Expected the field `specialCheckCalc` to be a primitive type in the JSON string but got " + data['specialCheckCalc']);
        }
        // ensure the json data is a string
        if (data['taxCalculationCode'] && !(typeof data['taxCalculationCode'] === 'string' || data['taxCalculationCode'] instanceof String)) {
            throw new Error("Expected the field `taxCalculationCode` to be a primitive type in the JSON string but got " + data['taxCalculationCode']);
        }
        // ensure the json data is a string
        if (data['taxCode'] && !(typeof data['taxCode'] === 'string' || data['taxCode'] instanceof String)) {
            throw new Error("Expected the field `taxCode` to be a primitive type in the JSON string but got " + data['taxCode']);
        }

        return true;
    }


}



/**
 * State tax code.<br  /> Max length: 50
 * @member {Number} amount
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['amount'] = undefined;

/**
 * Box 4(b) on form W4 (year 2020 or later): Deductions amount. <br  />Decimal (12,2)
 * @member {Number} deductionsAmount
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['deductionsAmount'] = undefined;

/**
 * Box 3 on form W4 (year 2020 or later): Total dependents amount. <br  />Decimal (12,2)
 * @member {Number} dependentsAmount
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['dependentsAmount'] = undefined;

/**
 * State tax exemptions value.<br  />Decimal (12,2)
 * @member {Number} exemptions
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['exemptions'] = undefined;

/**
 * State tax exemptions 2 value.<br  />Decimal (12,2)
 * @member {Number} exemptions2
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['exemptions2'] = undefined;

/**
 * Employee state tax filing status. Common values are *S* (Single), *M* (Married).<br  />Max length: 50
 * @member {String} filingStatus
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['filingStatus'] = undefined;

/**
 * Box 2(c) on form W4 (year 2020 or later): Multiple Jobs or Spouse Works. <br  />Boolean
 * @member {Boolean} higherRate
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['higherRate'] = undefined;

/**
 * Box 4(a) on form W4 (year 2020 or later): Other income amount. <br  />Decimal (12,2)
 * @member {Number} otherIncomeAmount
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['otherIncomeAmount'] = undefined;

/**
 * State Tax percentage. <br  />Decimal (12,2)
 * @member {Number} percentage
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['percentage'] = undefined;

/**
 * Non-primary state tax reciprocity code.<br  /> Max length: 50
 * @member {String} reciprocityCode
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['reciprocityCode'] = undefined;

/**
 * Supplemental check calculation code. Common values are *Blocked* (Taxes blocked on Supplemental checks), *Supp* (Use supplemental Tax Rate-Code). <br  />Max length: 10
 * @member {String} specialCheckCalc
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['specialCheckCalc'] = undefined;

/**
 * Tax calculation code. Common values are *F* (Flat), *P* (Percentage), *FDFP* (Flat Dollar Amount plus Fixed Percentage). <br  />Max length: 10
 * @member {String} taxCalculationCode
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['taxCalculationCode'] = undefined;

/**
 * State tax code.<br  /> Max length: 50
 * @member {String} taxCode
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['taxCode'] = undefined;

/**
 * The state W4 form year <br  />Integer
 * @member {Number} w4FormYear
 */
StagedEmployeeNonPrimaryStateTaxInner.prototype['w4FormYear'] = undefined;






export default StagedEmployeeNonPrimaryStateTaxInner;

