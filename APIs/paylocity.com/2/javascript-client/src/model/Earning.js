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
 * The Earning model module.
 * @module model/Earning
 * @version 2
 */
class Earning {
    /**
     * Constructs a new <code>Earning</code>.
     * The employee earning model
     * @alias module:model/Earning
     * @param earningCode {String} Earning code. Must match Company setup. <br  />Max length: 10
     * @param startDate {String} Start date of an earning based on payroll calendar. Common formats are MM-DD-CCYY, CCYY-MM-DD.
     */
    constructor(earningCode, startDate) { 
        
        Earning.initialize(this, earningCode, startDate);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, earningCode, startDate) { 
        obj['earningCode'] = earningCode;
        obj['startDate'] = startDate;
    }

    /**
     * Constructs a <code>Earning</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Earning} obj Optional instance to populate.
     * @return {module:model/Earning} The populated <code>Earning</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Earning();

            if (data.hasOwnProperty('agency')) {
                obj['agency'] = ApiClient.convertToType(data['agency'], 'String');
            }
            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('annualMaximum')) {
                obj['annualMaximum'] = ApiClient.convertToType(data['annualMaximum'], 'Number');
            }
            if (data.hasOwnProperty('calculationCode')) {
                obj['calculationCode'] = ApiClient.convertToType(data['calculationCode'], 'String');
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
            if (data.hasOwnProperty('earningCode')) {
                obj['earningCode'] = ApiClient.convertToType(data['earningCode'], 'String');
            }
            if (data.hasOwnProperty('effectiveDate')) {
                obj['effectiveDate'] = ApiClient.convertToType(data['effectiveDate'], 'String');
            }
            if (data.hasOwnProperty('endDate')) {
                obj['endDate'] = ApiClient.convertToType(data['endDate'], 'String');
            }
            if (data.hasOwnProperty('frequency')) {
                obj['frequency'] = ApiClient.convertToType(data['frequency'], 'String');
            }
            if (data.hasOwnProperty('goal')) {
                obj['goal'] = ApiClient.convertToType(data['goal'], 'Number');
            }
            if (data.hasOwnProperty('hoursOrUnits')) {
                obj['hoursOrUnits'] = ApiClient.convertToType(data['hoursOrUnits'], 'Number');
            }
            if (data.hasOwnProperty('isSelfInsured')) {
                obj['isSelfInsured'] = ApiClient.convertToType(data['isSelfInsured'], 'Boolean');
            }
            if (data.hasOwnProperty('jobCode')) {
                obj['jobCode'] = ApiClient.convertToType(data['jobCode'], 'String');
            }
            if (data.hasOwnProperty('miscellaneousInfo')) {
                obj['miscellaneousInfo'] = ApiClient.convertToType(data['miscellaneousInfo'], 'String');
            }
            if (data.hasOwnProperty('paidTowardsGoal')) {
                obj['paidTowardsGoal'] = ApiClient.convertToType(data['paidTowardsGoal'], 'Number');
            }
            if (data.hasOwnProperty('payPeriodMaximum')) {
                obj['payPeriodMaximum'] = ApiClient.convertToType(data['payPeriodMaximum'], 'Number');
            }
            if (data.hasOwnProperty('payPeriodMinimum')) {
                obj['payPeriodMinimum'] = ApiClient.convertToType(data['payPeriodMinimum'], 'Number');
            }
            if (data.hasOwnProperty('rate')) {
                obj['rate'] = ApiClient.convertToType(data['rate'], 'Number');
            }
            if (data.hasOwnProperty('rateCode')) {
                obj['rateCode'] = ApiClient.convertToType(data['rateCode'], 'String');
            }
            if (data.hasOwnProperty('startDate')) {
                obj['startDate'] = ApiClient.convertToType(data['startDate'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Earning</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Earning</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Earning.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['agency'] && !(typeof data['agency'] === 'string' || data['agency'] instanceof String)) {
            throw new Error("Expected the field `agency` to be a primitive type in the JSON string but got " + data['agency']);
        }
        // ensure the json data is a string
        if (data['calculationCode'] && !(typeof data['calculationCode'] === 'string' || data['calculationCode'] instanceof String)) {
            throw new Error("Expected the field `calculationCode` to be a primitive type in the JSON string but got " + data['calculationCode']);
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
        if (data['earningCode'] && !(typeof data['earningCode'] === 'string' || data['earningCode'] instanceof String)) {
            throw new Error("Expected the field `earningCode` to be a primitive type in the JSON string but got " + data['earningCode']);
        }
        // ensure the json data is a string
        if (data['effectiveDate'] && !(typeof data['effectiveDate'] === 'string' || data['effectiveDate'] instanceof String)) {
            throw new Error("Expected the field `effectiveDate` to be a primitive type in the JSON string but got " + data['effectiveDate']);
        }
        // ensure the json data is a string
        if (data['endDate'] && !(typeof data['endDate'] === 'string' || data['endDate'] instanceof String)) {
            throw new Error("Expected the field `endDate` to be a primitive type in the JSON string but got " + data['endDate']);
        }
        // ensure the json data is a string
        if (data['frequency'] && !(typeof data['frequency'] === 'string' || data['frequency'] instanceof String)) {
            throw new Error("Expected the field `frequency` to be a primitive type in the JSON string but got " + data['frequency']);
        }
        // ensure the json data is a string
        if (data['jobCode'] && !(typeof data['jobCode'] === 'string' || data['jobCode'] instanceof String)) {
            throw new Error("Expected the field `jobCode` to be a primitive type in the JSON string but got " + data['jobCode']);
        }
        // ensure the json data is a string
        if (data['miscellaneousInfo'] && !(typeof data['miscellaneousInfo'] === 'string' || data['miscellaneousInfo'] instanceof String)) {
            throw new Error("Expected the field `miscellaneousInfo` to be a primitive type in the JSON string but got " + data['miscellaneousInfo']);
        }
        // ensure the json data is a string
        if (data['rateCode'] && !(typeof data['rateCode'] === 'string' || data['rateCode'] instanceof String)) {
            throw new Error("Expected the field `rateCode` to be a primitive type in the JSON string but got " + data['rateCode']);
        }
        // ensure the json data is a string
        if (data['startDate'] && !(typeof data['startDate'] === 'string' || data['startDate'] instanceof String)) {
            throw new Error("Expected the field `startDate` to be a primitive type in the JSON string but got " + data['startDate']);
        }

        return true;
    }


}

Earning.RequiredProperties = ["earningCode", "startDate"];

/**
 * Third-party agency associated with earning. Must match Company setup.<br  />Max length: 10
 * @member {String} agency
 */
Earning.prototype['agency'] = undefined;

/**
 * Value that matches CalculationCode to add to gross wages. For percentage (%), enter whole number (10 = 10%).  <br  />Decimal(12,2)
 * @member {Number} amount
 */
Earning.prototype['amount'] = undefined;

/**
 * Year to Date dollar amount not to be exceeded for an earning in the calendar year. Used only with company driven maximums. <br  />Decimal(12,2)
 * @member {Number} annualMaximum
 */
Earning.prototype['annualMaximum'] = undefined;

/**
 * Defines how earnings are calculated. Common values are *% (percentage of gross), flat (flat dollar amount)*. Defaulted to the Company setup calcCode for earning. <br  />Max length: 20
 * @member {String} calculationCode
 */
Earning.prototype['calculationCode'] = undefined;

/**
 * Cost Center associated with earning. Must match Company setup.<br  /> Max length: 10
 * @member {String} costCenter1
 */
Earning.prototype['costCenter1'] = undefined;

/**
 * Cost Center associated with earning. Must match Company setup.<br  /> Max length: 10
 * @member {String} costCenter2
 */
Earning.prototype['costCenter2'] = undefined;

/**
 * Cost Center associated with earning. Must match Company setup.<br  /> Max length: 10
 * @member {String} costCenter3
 */
Earning.prototype['costCenter3'] = undefined;

/**
 * Earning code. Must match Company setup. <br  />Max length: 10
 * @member {String} earningCode
 */
Earning.prototype['earningCode'] = undefined;

/**
 * Date earning is active. Defaulted to run date or check date based on Company setup. Common formats are MM-DD-CCYY, CCYY-MM-DD.
 * @member {String} effectiveDate
 */
Earning.prototype['effectiveDate'] = undefined;

/**
 * Stop date of an earning. Common formats are MM-DD-CCYY, CCYY-MM-DD.
 * @member {String} endDate
 */
Earning.prototype['endDate'] = undefined;

/**
 * Needed if earning is applied differently from the payroll frequency (one time earning for example).<br  /> Max length: 5
 * @member {String} frequency
 */
Earning.prototype['frequency'] = undefined;

/**
 * Dollar amount. The employee earning will stop when the goal amount is reached.<br  /> Decimal(12,2)
 * @member {Number} goal
 */
Earning.prototype['goal'] = undefined;

/**
 * The value is used in conjunction with the Rate field. When entering Group Term Life Insurance (GTL), it should contain the full amount of the group term life insurance policy. <br  /> Decimal(12,2)
 * @member {Number} hoursOrUnits
 */
Earning.prototype['hoursOrUnits'] = undefined;

/**
 * Used for ACA. If not entered, defaulted to Company earning setup.
 * @member {Boolean} isSelfInsured
 */
Earning.prototype['isSelfInsured'] = undefined;

/**
 * Job code associated with earnings. Must match Company setup.<br  /> Max length: 20
 * @member {String} jobCode
 */
Earning.prototype['jobCode'] = undefined;

/**
 * Information to print on the check stub if agency is set up for this earning. <br  />Max length: 50
 * @member {String} miscellaneousInfo
 */
Earning.prototype['miscellaneousInfo'] = undefined;

/**
 * Amount already paid to employee toward goal. <br  /> Decimal(12,2)
 * @member {Number} paidTowardsGoal
 */
Earning.prototype['paidTowardsGoal'] = undefined;

/**
 * Maximum amount of the earning on a single paycheck. <br  /> Decimal(12,2)
 * @member {Number} payPeriodMaximum
 */
Earning.prototype['payPeriodMaximum'] = undefined;

/**
 * Minimum amount of the earning on a single paycheck. <br  /> Decimal(12,2)
 * @member {Number} payPeriodMinimum
 */
Earning.prototype['payPeriodMinimum'] = undefined;

/**
 * Rate is used in conjunction with the hoursOrUnits field. <br  /> Decimal(12,2)
 * @member {Number} rate
 */
Earning.prototype['rate'] = undefined;

/**
 * Rate Code applies to additional pay rates entered for an employee. Must match Company setup. <br  /> Max length: 10
 * @member {String} rateCode
 */
Earning.prototype['rateCode'] = undefined;

/**
 * Start date of an earning based on payroll calendar. Common formats are MM-DD-CCYY, CCYY-MM-DD.
 * @member {String} startDate
 */
Earning.prototype['startDate'] = undefined;






export default Earning;

