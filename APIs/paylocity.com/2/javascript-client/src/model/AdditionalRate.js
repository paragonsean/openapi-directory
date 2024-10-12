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
 * The AdditionalRate model module.
 * @module model/AdditionalRate
 * @version 2
 */
class AdditionalRate {
    /**
     * Constructs a new <code>AdditionalRate</code>.
     * The additional pay rate model
     * @alias module:model/AdditionalRate
     */
    constructor() { 
        
        AdditionalRate.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AdditionalRate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AdditionalRate} obj Optional instance to populate.
     * @return {module:model/AdditionalRate} The populated <code>AdditionalRate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AdditionalRate();

            if (data.hasOwnProperty('changeReason')) {
                obj['changeReason'] = ApiClient.convertToType(data['changeReason'], 'String');
            }
            if (data.hasOwnProperty('costCenter1')) {
                obj['costCenter1'] = ApiClient.convertToType(data['costCenter1'], 'String');
            }
            if (data.hasOwnProperty('costCenter2')) {
                obj['costCenter2'] = ApiClient.convertToType(data['costCenter2'], 'String');
            }
            if (data.hasOwnProperty('costCenter3')) {
                obj['costCenter3'] = ApiClient.convertToType(data['costCenter3'], 'String');
            }
            if (data.hasOwnProperty('effectiveDate')) {
                obj['effectiveDate'] = ApiClient.convertToType(data['effectiveDate'], 'String');
            }
            if (data.hasOwnProperty('endCheckDate')) {
                obj['endCheckDate'] = ApiClient.convertToType(data['endCheckDate'], 'String');
            }
            if (data.hasOwnProperty('job')) {
                obj['job'] = ApiClient.convertToType(data['job'], 'String');
            }
            if (data.hasOwnProperty('rate')) {
                obj['rate'] = ApiClient.convertToType(data['rate'], 'Number');
            }
            if (data.hasOwnProperty('rateCode')) {
                obj['rateCode'] = ApiClient.convertToType(data['rateCode'], 'String');
            }
            if (data.hasOwnProperty('rateNotes')) {
                obj['rateNotes'] = ApiClient.convertToType(data['rateNotes'], 'String');
            }
            if (data.hasOwnProperty('ratePer')) {
                obj['ratePer'] = ApiClient.convertToType(data['ratePer'], 'String');
            }
            if (data.hasOwnProperty('shift')) {
                obj['shift'] = ApiClient.convertToType(data['shift'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AdditionalRate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AdditionalRate</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['changeReason'] && !(typeof data['changeReason'] === 'string' || data['changeReason'] instanceof String)) {
            throw new Error("Expected the field `changeReason` to be a primitive type in the JSON string but got " + data['changeReason']);
        }
        // ensure the json data is a string
        if (data['costCenter1'] && !(typeof data['costCenter1'] === 'string' || data['costCenter1'] instanceof String)) {
            throw new Error("Expected the field `costCenter1` to be a primitive type in the JSON string but got " + data['costCenter1']);
        }
        // ensure the json data is a string
        if (data['costCenter2'] && !(typeof data['costCenter2'] === 'string' || data['costCenter2'] instanceof String)) {
            throw new Error("Expected the field `costCenter2` to be a primitive type in the JSON string but got " + data['costCenter2']);
        }
        // ensure the json data is a string
        if (data['costCenter3'] && !(typeof data['costCenter3'] === 'string' || data['costCenter3'] instanceof String)) {
            throw new Error("Expected the field `costCenter3` to be a primitive type in the JSON string but got " + data['costCenter3']);
        }
        // ensure the json data is a string
        if (data['effectiveDate'] && !(typeof data['effectiveDate'] === 'string' || data['effectiveDate'] instanceof String)) {
            throw new Error("Expected the field `effectiveDate` to be a primitive type in the JSON string but got " + data['effectiveDate']);
        }
        // ensure the json data is a string
        if (data['endCheckDate'] && !(typeof data['endCheckDate'] === 'string' || data['endCheckDate'] instanceof String)) {
            throw new Error("Expected the field `endCheckDate` to be a primitive type in the JSON string but got " + data['endCheckDate']);
        }
        // ensure the json data is a string
        if (data['job'] && !(typeof data['job'] === 'string' || data['job'] instanceof String)) {
            throw new Error("Expected the field `job` to be a primitive type in the JSON string but got " + data['job']);
        }
        // ensure the json data is a string
        if (data['rateCode'] && !(typeof data['rateCode'] === 'string' || data['rateCode'] instanceof String)) {
            throw new Error("Expected the field `rateCode` to be a primitive type in the JSON string but got " + data['rateCode']);
        }
        // ensure the json data is a string
        if (data['rateNotes'] && !(typeof data['rateNotes'] === 'string' || data['rateNotes'] instanceof String)) {
            throw new Error("Expected the field `rateNotes` to be a primitive type in the JSON string but got " + data['rateNotes']);
        }
        // ensure the json data is a string
        if (data['ratePer'] && !(typeof data['ratePer'] === 'string' || data['ratePer'] instanceof String)) {
            throw new Error("Expected the field `ratePer` to be a primitive type in the JSON string but got " + data['ratePer']);
        }
        // ensure the json data is a string
        if (data['shift'] && !(typeof data['shift'] === 'string' || data['shift'] instanceof String)) {
            throw new Error("Expected the field `shift` to be a primitive type in the JSON string but got " + data['shift']);
        }

        return true;
    }


}



/**
 * Not required. If populated, must match one of the system coded values available in the Additional Rates Change Reason drop down.<br />
 * @member {String} changeReason
 */
AdditionalRate.prototype['changeReason'] = undefined;

/**
 * Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 1 drop down. This cell must be in a text format.<br />
 * @member {String} costCenter1
 */
AdditionalRate.prototype['costCenter1'] = undefined;

/**
 * Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 2 drop down. This cell must be in a text format.<br />
 * @member {String} costCenter2
 */
AdditionalRate.prototype['costCenter2'] = undefined;

/**
 * Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 3 drop down. This cell must be in a text format.<br />
 * @member {String} costCenter3
 */
AdditionalRate.prototype['costCenter3'] = undefined;

/**
 * Required. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.<br />
 * @member {String} effectiveDate
 */
AdditionalRate.prototype['effectiveDate'] = undefined;

/**
 * Not required. Must match one of the system coded check dates available in the Additional Rates End Check Date drop down. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.<br />
 * @member {String} endCheckDate
 */
AdditionalRate.prototype['endCheckDate'] = undefined;

/**
 * Not required. If populated, must match one of the system coded values available in the Additional Rates Job drop down.<br />
 * @member {String} job
 */
AdditionalRate.prototype['job'] = undefined;

/**
 * Required. Enter dollar amount that corresponds to the Per selection.<br />
 * @member {Number} rate
 */
AdditionalRate.prototype['rate'] = undefined;

/**
 * Required. If populated, must match one of the system coded values available in the Additional Rates Rate Code drop down.<br />
 * @member {String} rateCode
 */
AdditionalRate.prototype['rateCode'] = undefined;

/**
 * Not required.<br  />Max length: 4000<br />
 * @member {String} rateNotes
 */
AdditionalRate.prototype['rateNotes'] = undefined;

/**
 * Required. Valid values are HOUR or WEEK.<br />
 * @member {String} ratePer
 */
AdditionalRate.prototype['ratePer'] = undefined;

/**
 * Not required. If populated, must match one of the system coded values available in the Additional Rates Shift drop down.<br />
 * @member {String} shift
 */
AdditionalRate.prototype['shift'] = undefined;






export default AdditionalRate;

