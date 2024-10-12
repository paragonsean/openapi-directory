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
import EmployeeCustomBooleanFieldsInner from './EmployeeCustomBooleanFieldsInner';
import EmployeeCustomDateFieldsInner from './EmployeeCustomDateFieldsInner';
import EmployeeCustomDropDownFieldsInner from './EmployeeCustomDropDownFieldsInner';
import EmployeeCustomNumberFieldsInner from './EmployeeCustomNumberFieldsInner';
import EmployeeCustomTextFieldsInner from './EmployeeCustomTextFieldsInner';
import EmployeeLocalTaxInner from './EmployeeLocalTaxInner';
import StagedEmployeeAdditionalDirectDepositInner from './StagedEmployeeAdditionalDirectDepositInner';
import StagedEmployeeBenefitSetupInner from './StagedEmployeeBenefitSetupInner';
import StagedEmployeeDepartmentPositionInner from './StagedEmployeeDepartmentPositionInner';
import StagedEmployeeFederalTaxInner from './StagedEmployeeFederalTaxInner';
import StagedEmployeeHomeAddressInner from './StagedEmployeeHomeAddressInner';
import StagedEmployeeMainDirectDepositInner from './StagedEmployeeMainDirectDepositInner';
import StagedEmployeeNonPrimaryStateTaxInner from './StagedEmployeeNonPrimaryStateTaxInner';
import StagedEmployeePrimaryPayRateInner from './StagedEmployeePrimaryPayRateInner';
import StagedEmployeePrimaryStateTaxInner from './StagedEmployeePrimaryStateTaxInner';
import StagedEmployeeStatusInner from './StagedEmployeeStatusInner';
import StagedEmployeeWebTime from './StagedEmployeeWebTime';
import StagedEmployeeWorkAddressInner from './StagedEmployeeWorkAddressInner';
import StagedEmployeeWorkEligibilityInner from './StagedEmployeeWorkEligibilityInner';

/**
 * The StagedEmployee model module.
 * @module model/StagedEmployee
 * @version 2
 */
class StagedEmployee {
    /**
     * Constructs a new <code>StagedEmployee</code>.
     * The staged employee model
     * @alias module:model/StagedEmployee
     */
    constructor() { 
        
        StagedEmployee.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>StagedEmployee</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StagedEmployee} obj Optional instance to populate.
     * @return {module:model/StagedEmployee} The populated <code>StagedEmployee</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StagedEmployee();

            if (data.hasOwnProperty('additionalDirectDeposit')) {
                obj['additionalDirectDeposit'] = ApiClient.convertToType(data['additionalDirectDeposit'], [StagedEmployeeAdditionalDirectDepositInner]);
            }
            if (data.hasOwnProperty('benefitSetup')) {
                obj['benefitSetup'] = ApiClient.convertToType(data['benefitSetup'], [StagedEmployeeBenefitSetupInner]);
            }
            if (data.hasOwnProperty('birthDate')) {
                obj['birthDate'] = ApiClient.convertToType(data['birthDate'], 'String');
            }
            if (data.hasOwnProperty('customBooleanFields')) {
                obj['customBooleanFields'] = ApiClient.convertToType(data['customBooleanFields'], [EmployeeCustomBooleanFieldsInner]);
            }
            if (data.hasOwnProperty('customDateFields')) {
                obj['customDateFields'] = ApiClient.convertToType(data['customDateFields'], [EmployeeCustomDateFieldsInner]);
            }
            if (data.hasOwnProperty('customDropDownFields')) {
                obj['customDropDownFields'] = ApiClient.convertToType(data['customDropDownFields'], [EmployeeCustomDropDownFieldsInner]);
            }
            if (data.hasOwnProperty('customNumberFields')) {
                obj['customNumberFields'] = ApiClient.convertToType(data['customNumberFields'], [EmployeeCustomNumberFieldsInner]);
            }
            if (data.hasOwnProperty('customTextFields')) {
                obj['customTextFields'] = ApiClient.convertToType(data['customTextFields'], [EmployeeCustomTextFieldsInner]);
            }
            if (data.hasOwnProperty('departmentPosition')) {
                obj['departmentPosition'] = ApiClient.convertToType(data['departmentPosition'], [StagedEmployeeDepartmentPositionInner]);
            }
            if (data.hasOwnProperty('disabilityDescription')) {
                obj['disabilityDescription'] = ApiClient.convertToType(data['disabilityDescription'], 'String');
            }
            if (data.hasOwnProperty('employeeId')) {
                obj['employeeId'] = ApiClient.convertToType(data['employeeId'], 'String');
            }
            if (data.hasOwnProperty('ethnicity')) {
                obj['ethnicity'] = ApiClient.convertToType(data['ethnicity'], 'String');
            }
            if (data.hasOwnProperty('federalTax')) {
                obj['federalTax'] = ApiClient.convertToType(data['federalTax'], [StagedEmployeeFederalTaxInner]);
            }
            if (data.hasOwnProperty('firstName')) {
                obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
            }
            if (data.hasOwnProperty('fitwExemptReason')) {
                obj['fitwExemptReason'] = ApiClient.convertToType(data['fitwExemptReason'], 'String');
            }
            if (data.hasOwnProperty('futaExemptReason')) {
                obj['futaExemptReason'] = ApiClient.convertToType(data['futaExemptReason'], 'String');
            }
            if (data.hasOwnProperty('gender')) {
                obj['gender'] = ApiClient.convertToType(data['gender'], 'String');
            }
            if (data.hasOwnProperty('homeAddress')) {
                obj['homeAddress'] = ApiClient.convertToType(data['homeAddress'], [StagedEmployeeHomeAddressInner]);
            }
            if (data.hasOwnProperty('isEmployee943')) {
                obj['isEmployee943'] = ApiClient.convertToType(data['isEmployee943'], 'Boolean');
            }
            if (data.hasOwnProperty('isSmoker')) {
                obj['isSmoker'] = ApiClient.convertToType(data['isSmoker'], 'Boolean');
            }
            if (data.hasOwnProperty('lastName')) {
                obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
            }
            if (data.hasOwnProperty('localTax')) {
                obj['localTax'] = ApiClient.convertToType(data['localTax'], [EmployeeLocalTaxInner]);
            }
            if (data.hasOwnProperty('mainDirectDeposit')) {
                obj['mainDirectDeposit'] = ApiClient.convertToType(data['mainDirectDeposit'], [StagedEmployeeMainDirectDepositInner]);
            }
            if (data.hasOwnProperty('maritalStatus')) {
                obj['maritalStatus'] = ApiClient.convertToType(data['maritalStatus'], 'String');
            }
            if (data.hasOwnProperty('medExemptReason')) {
                obj['medExemptReason'] = ApiClient.convertToType(data['medExemptReason'], 'String');
            }
            if (data.hasOwnProperty('middleName')) {
                obj['middleName'] = ApiClient.convertToType(data['middleName'], 'String');
            }
            if (data.hasOwnProperty('nonPrimaryStateTax')) {
                obj['nonPrimaryStateTax'] = ApiClient.convertToType(data['nonPrimaryStateTax'], [StagedEmployeeNonPrimaryStateTaxInner]);
            }
            if (data.hasOwnProperty('preferredName')) {
                obj['preferredName'] = ApiClient.convertToType(data['preferredName'], 'String');
            }
            if (data.hasOwnProperty('primaryPayRate')) {
                obj['primaryPayRate'] = ApiClient.convertToType(data['primaryPayRate'], [StagedEmployeePrimaryPayRateInner]);
            }
            if (data.hasOwnProperty('primaryStateTax')) {
                obj['primaryStateTax'] = ApiClient.convertToType(data['primaryStateTax'], [StagedEmployeePrimaryStateTaxInner]);
            }
            if (data.hasOwnProperty('priorLastName')) {
                obj['priorLastName'] = ApiClient.convertToType(data['priorLastName'], 'String');
            }
            if (data.hasOwnProperty('salutation')) {
                obj['salutation'] = ApiClient.convertToType(data['salutation'], 'String');
            }
            if (data.hasOwnProperty('sitwExemptReason')) {
                obj['sitwExemptReason'] = ApiClient.convertToType(data['sitwExemptReason'], 'String');
            }
            if (data.hasOwnProperty('ssExemptReason')) {
                obj['ssExemptReason'] = ApiClient.convertToType(data['ssExemptReason'], 'String');
            }
            if (data.hasOwnProperty('ssn')) {
                obj['ssn'] = ApiClient.convertToType(data['ssn'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], [StagedEmployeeStatusInner]);
            }
            if (data.hasOwnProperty('suffix')) {
                obj['suffix'] = ApiClient.convertToType(data['suffix'], 'String');
            }
            if (data.hasOwnProperty('suiExemptReason')) {
                obj['suiExemptReason'] = ApiClient.convertToType(data['suiExemptReason'], 'String');
            }
            if (data.hasOwnProperty('suiState')) {
                obj['suiState'] = ApiClient.convertToType(data['suiState'], 'String');
            }
            if (data.hasOwnProperty('taxDistributionCode1099R')) {
                obj['taxDistributionCode1099R'] = ApiClient.convertToType(data['taxDistributionCode1099R'], 'String');
            }
            if (data.hasOwnProperty('taxForm')) {
                obj['taxForm'] = ApiClient.convertToType(data['taxForm'], 'String');
            }
            if (data.hasOwnProperty('veteranDescription')) {
                obj['veteranDescription'] = ApiClient.convertToType(data['veteranDescription'], 'String');
            }
            if (data.hasOwnProperty('webTime')) {
                obj['webTime'] = StagedEmployeeWebTime.constructFromObject(data['webTime']);
            }
            if (data.hasOwnProperty('workAddress')) {
                obj['workAddress'] = ApiClient.convertToType(data['workAddress'], [StagedEmployeeWorkAddressInner]);
            }
            if (data.hasOwnProperty('workEligibility')) {
                obj['workEligibility'] = ApiClient.convertToType(data['workEligibility'], [StagedEmployeeWorkEligibilityInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StagedEmployee</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StagedEmployee</code>.
     */
    static validateJSON(data) {
        if (data['additionalDirectDeposit']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['additionalDirectDeposit'])) {
                throw new Error("Expected the field `additionalDirectDeposit` to be an array in the JSON data but got " + data['additionalDirectDeposit']);
            }
            // validate the optional field `additionalDirectDeposit` (array)
            for (const item of data['additionalDirectDeposit']) {
                StagedEmployeeAdditionalDirectDepositInner.validateJSON(item);
            };
        }
        if (data['benefitSetup']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['benefitSetup'])) {
                throw new Error("Expected the field `benefitSetup` to be an array in the JSON data but got " + data['benefitSetup']);
            }
            // validate the optional field `benefitSetup` (array)
            for (const item of data['benefitSetup']) {
                StagedEmployeeBenefitSetupInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['birthDate'] && !(typeof data['birthDate'] === 'string' || data['birthDate'] instanceof String)) {
            throw new Error("Expected the field `birthDate` to be a primitive type in the JSON string but got " + data['birthDate']);
        }
        if (data['customBooleanFields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customBooleanFields'])) {
                throw new Error("Expected the field `customBooleanFields` to be an array in the JSON data but got " + data['customBooleanFields']);
            }
            // validate the optional field `customBooleanFields` (array)
            for (const item of data['customBooleanFields']) {
                EmployeeCustomBooleanFieldsInner.validateJSON(item);
            };
        }
        if (data['customDateFields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customDateFields'])) {
                throw new Error("Expected the field `customDateFields` to be an array in the JSON data but got " + data['customDateFields']);
            }
            // validate the optional field `customDateFields` (array)
            for (const item of data['customDateFields']) {
                EmployeeCustomDateFieldsInner.validateJSON(item);
            };
        }
        if (data['customDropDownFields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customDropDownFields'])) {
                throw new Error("Expected the field `customDropDownFields` to be an array in the JSON data but got " + data['customDropDownFields']);
            }
            // validate the optional field `customDropDownFields` (array)
            for (const item of data['customDropDownFields']) {
                EmployeeCustomDropDownFieldsInner.validateJSON(item);
            };
        }
        if (data['customNumberFields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customNumberFields'])) {
                throw new Error("Expected the field `customNumberFields` to be an array in the JSON data but got " + data['customNumberFields']);
            }
            // validate the optional field `customNumberFields` (array)
            for (const item of data['customNumberFields']) {
                EmployeeCustomNumberFieldsInner.validateJSON(item);
            };
        }
        if (data['customTextFields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customTextFields'])) {
                throw new Error("Expected the field `customTextFields` to be an array in the JSON data but got " + data['customTextFields']);
            }
            // validate the optional field `customTextFields` (array)
            for (const item of data['customTextFields']) {
                EmployeeCustomTextFieldsInner.validateJSON(item);
            };
        }
        if (data['departmentPosition']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['departmentPosition'])) {
                throw new Error("Expected the field `departmentPosition` to be an array in the JSON data but got " + data['departmentPosition']);
            }
            // validate the optional field `departmentPosition` (array)
            for (const item of data['departmentPosition']) {
                StagedEmployeeDepartmentPositionInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['disabilityDescription'] && !(typeof data['disabilityDescription'] === 'string' || data['disabilityDescription'] instanceof String)) {
            throw new Error("Expected the field `disabilityDescription` to be a primitive type in the JSON string but got " + data['disabilityDescription']);
        }
        // ensure the json data is a string
        if (data['employeeId'] && !(typeof data['employeeId'] === 'string' || data['employeeId'] instanceof String)) {
            throw new Error("Expected the field `employeeId` to be a primitive type in the JSON string but got " + data['employeeId']);
        }
        // ensure the json data is a string
        if (data['ethnicity'] && !(typeof data['ethnicity'] === 'string' || data['ethnicity'] instanceof String)) {
            throw new Error("Expected the field `ethnicity` to be a primitive type in the JSON string but got " + data['ethnicity']);
        }
        if (data['federalTax']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['federalTax'])) {
                throw new Error("Expected the field `federalTax` to be an array in the JSON data but got " + data['federalTax']);
            }
            // validate the optional field `federalTax` (array)
            for (const item of data['federalTax']) {
                StagedEmployeeFederalTaxInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['firstName'] && !(typeof data['firstName'] === 'string' || data['firstName'] instanceof String)) {
            throw new Error("Expected the field `firstName` to be a primitive type in the JSON string but got " + data['firstName']);
        }
        // ensure the json data is a string
        if (data['fitwExemptReason'] && !(typeof data['fitwExemptReason'] === 'string' || data['fitwExemptReason'] instanceof String)) {
            throw new Error("Expected the field `fitwExemptReason` to be a primitive type in the JSON string but got " + data['fitwExemptReason']);
        }
        // ensure the json data is a string
        if (data['futaExemptReason'] && !(typeof data['futaExemptReason'] === 'string' || data['futaExemptReason'] instanceof String)) {
            throw new Error("Expected the field `futaExemptReason` to be a primitive type in the JSON string but got " + data['futaExemptReason']);
        }
        // ensure the json data is a string
        if (data['gender'] && !(typeof data['gender'] === 'string' || data['gender'] instanceof String)) {
            throw new Error("Expected the field `gender` to be a primitive type in the JSON string but got " + data['gender']);
        }
        if (data['homeAddress']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['homeAddress'])) {
                throw new Error("Expected the field `homeAddress` to be an array in the JSON data but got " + data['homeAddress']);
            }
            // validate the optional field `homeAddress` (array)
            for (const item of data['homeAddress']) {
                StagedEmployeeHomeAddressInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['lastName'] && !(typeof data['lastName'] === 'string' || data['lastName'] instanceof String)) {
            throw new Error("Expected the field `lastName` to be a primitive type in the JSON string but got " + data['lastName']);
        }
        if (data['localTax']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['localTax'])) {
                throw new Error("Expected the field `localTax` to be an array in the JSON data but got " + data['localTax']);
            }
            // validate the optional field `localTax` (array)
            for (const item of data['localTax']) {
                EmployeeLocalTaxInner.validateJSON(item);
            };
        }
        if (data['mainDirectDeposit']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['mainDirectDeposit'])) {
                throw new Error("Expected the field `mainDirectDeposit` to be an array in the JSON data but got " + data['mainDirectDeposit']);
            }
            // validate the optional field `mainDirectDeposit` (array)
            for (const item of data['mainDirectDeposit']) {
                StagedEmployeeMainDirectDepositInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['maritalStatus'] && !(typeof data['maritalStatus'] === 'string' || data['maritalStatus'] instanceof String)) {
            throw new Error("Expected the field `maritalStatus` to be a primitive type in the JSON string but got " + data['maritalStatus']);
        }
        // ensure the json data is a string
        if (data['medExemptReason'] && !(typeof data['medExemptReason'] === 'string' || data['medExemptReason'] instanceof String)) {
            throw new Error("Expected the field `medExemptReason` to be a primitive type in the JSON string but got " + data['medExemptReason']);
        }
        // ensure the json data is a string
        if (data['middleName'] && !(typeof data['middleName'] === 'string' || data['middleName'] instanceof String)) {
            throw new Error("Expected the field `middleName` to be a primitive type in the JSON string but got " + data['middleName']);
        }
        if (data['nonPrimaryStateTax']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['nonPrimaryStateTax'])) {
                throw new Error("Expected the field `nonPrimaryStateTax` to be an array in the JSON data but got " + data['nonPrimaryStateTax']);
            }
            // validate the optional field `nonPrimaryStateTax` (array)
            for (const item of data['nonPrimaryStateTax']) {
                StagedEmployeeNonPrimaryStateTaxInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['preferredName'] && !(typeof data['preferredName'] === 'string' || data['preferredName'] instanceof String)) {
            throw new Error("Expected the field `preferredName` to be a primitive type in the JSON string but got " + data['preferredName']);
        }
        if (data['primaryPayRate']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['primaryPayRate'])) {
                throw new Error("Expected the field `primaryPayRate` to be an array in the JSON data but got " + data['primaryPayRate']);
            }
            // validate the optional field `primaryPayRate` (array)
            for (const item of data['primaryPayRate']) {
                StagedEmployeePrimaryPayRateInner.validateJSON(item);
            };
        }
        if (data['primaryStateTax']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['primaryStateTax'])) {
                throw new Error("Expected the field `primaryStateTax` to be an array in the JSON data but got " + data['primaryStateTax']);
            }
            // validate the optional field `primaryStateTax` (array)
            for (const item of data['primaryStateTax']) {
                StagedEmployeePrimaryStateTaxInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['priorLastName'] && !(typeof data['priorLastName'] === 'string' || data['priorLastName'] instanceof String)) {
            throw new Error("Expected the field `priorLastName` to be a primitive type in the JSON string but got " + data['priorLastName']);
        }
        // ensure the json data is a string
        if (data['salutation'] && !(typeof data['salutation'] === 'string' || data['salutation'] instanceof String)) {
            throw new Error("Expected the field `salutation` to be a primitive type in the JSON string but got " + data['salutation']);
        }
        // ensure the json data is a string
        if (data['sitwExemptReason'] && !(typeof data['sitwExemptReason'] === 'string' || data['sitwExemptReason'] instanceof String)) {
            throw new Error("Expected the field `sitwExemptReason` to be a primitive type in the JSON string but got " + data['sitwExemptReason']);
        }
        // ensure the json data is a string
        if (data['ssExemptReason'] && !(typeof data['ssExemptReason'] === 'string' || data['ssExemptReason'] instanceof String)) {
            throw new Error("Expected the field `ssExemptReason` to be a primitive type in the JSON string but got " + data['ssExemptReason']);
        }
        // ensure the json data is a string
        if (data['ssn'] && !(typeof data['ssn'] === 'string' || data['ssn'] instanceof String)) {
            throw new Error("Expected the field `ssn` to be a primitive type in the JSON string but got " + data['ssn']);
        }
        if (data['status']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['status'])) {
                throw new Error("Expected the field `status` to be an array in the JSON data but got " + data['status']);
            }
            // validate the optional field `status` (array)
            for (const item of data['status']) {
                StagedEmployeeStatusInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['suffix'] && !(typeof data['suffix'] === 'string' || data['suffix'] instanceof String)) {
            throw new Error("Expected the field `suffix` to be a primitive type in the JSON string but got " + data['suffix']);
        }
        // ensure the json data is a string
        if (data['suiExemptReason'] && !(typeof data['suiExemptReason'] === 'string' || data['suiExemptReason'] instanceof String)) {
            throw new Error("Expected the field `suiExemptReason` to be a primitive type in the JSON string but got " + data['suiExemptReason']);
        }
        // ensure the json data is a string
        if (data['suiState'] && !(typeof data['suiState'] === 'string' || data['suiState'] instanceof String)) {
            throw new Error("Expected the field `suiState` to be a primitive type in the JSON string but got " + data['suiState']);
        }
        // ensure the json data is a string
        if (data['taxDistributionCode1099R'] && !(typeof data['taxDistributionCode1099R'] === 'string' || data['taxDistributionCode1099R'] instanceof String)) {
            throw new Error("Expected the field `taxDistributionCode1099R` to be a primitive type in the JSON string but got " + data['taxDistributionCode1099R']);
        }
        // ensure the json data is a string
        if (data['taxForm'] && !(typeof data['taxForm'] === 'string' || data['taxForm'] instanceof String)) {
            throw new Error("Expected the field `taxForm` to be a primitive type in the JSON string but got " + data['taxForm']);
        }
        // ensure the json data is a string
        if (data['veteranDescription'] && !(typeof data['veteranDescription'] === 'string' || data['veteranDescription'] instanceof String)) {
            throw new Error("Expected the field `veteranDescription` to be a primitive type in the JSON string but got " + data['veteranDescription']);
        }
        // validate the optional field `webTime`
        if (data['webTime']) { // data not null
          StagedEmployeeWebTime.validateJSON(data['webTime']);
        }
        if (data['workAddress']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['workAddress'])) {
                throw new Error("Expected the field `workAddress` to be an array in the JSON data but got " + data['workAddress']);
            }
            // validate the optional field `workAddress` (array)
            for (const item of data['workAddress']) {
                StagedEmployeeWorkAddressInner.validateJSON(item);
            };
        }
        if (data['workEligibility']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['workEligibility'])) {
                throw new Error("Expected the field `workEligibility` to be an array in the JSON data but got " + data['workEligibility']);
            }
            // validate the optional field `workEligibility` (array)
            for (const item of data['workEligibility']) {
                StagedEmployeeWorkEligibilityInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Add up to 19 direct deposit accounts in addition to the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with information provided on the request. GET API will not return direct deposit data.
 * @member {Array.<module:model/StagedEmployeeAdditionalDirectDepositInner>} additionalDirectDeposit
 */
StagedEmployee.prototype['additionalDirectDeposit'] = undefined;

/**
 * Add setup values used for employee benefits integration, insurance plan settings, and ACA reporting.
 * @member {Array.<module:model/StagedEmployeeBenefitSetupInner>} benefitSetup
 */
StagedEmployee.prototype['benefitSetup'] = undefined;

/**
 * Employee birthdate. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.
 * @member {String} birthDate
 */
StagedEmployee.prototype['birthDate'] = undefined;

/**
 * Up to 8 custom fields of boolean (checkbox) type value.
 * @member {Array.<module:model/EmployeeCustomBooleanFieldsInner>} customBooleanFields
 */
StagedEmployee.prototype['customBooleanFields'] = undefined;

/**
 * Up to 8 custom fields of the date type value.
 * @member {Array.<module:model/EmployeeCustomDateFieldsInner>} customDateFields
 */
StagedEmployee.prototype['customDateFields'] = undefined;

/**
 * Up to 8 custom fields of the dropdown type value.
 * @member {Array.<module:model/EmployeeCustomDropDownFieldsInner>} customDropDownFields
 */
StagedEmployee.prototype['customDropDownFields'] = undefined;

/**
 * Up to 8 custom fields of numeric type value.
 * @member {Array.<module:model/EmployeeCustomNumberFieldsInner>} customNumberFields
 */
StagedEmployee.prototype['customNumberFields'] = undefined;

/**
 * Up to 8 custom fields of text type value.
 * @member {Array.<module:model/EmployeeCustomTextFieldsInner>} customTextFields
 */
StagedEmployee.prototype['customTextFields'] = undefined;

/**
 * Add home department cost center, position, supervisor, reviewer, employment type, EEO class, pay settings, and union information.
 * @member {Array.<module:model/StagedEmployeeDepartmentPositionInner>} departmentPosition
 */
StagedEmployee.prototype['departmentPosition'] = undefined;

/**
 * Indicates if employee has disability status.
 * @member {String} disabilityDescription
 */
StagedEmployee.prototype['disabilityDescription'] = undefined;

/**
 * Leave blank to have Web Pay automatically assign the next available employee ID.<br  /> Max length: 10
 * @member {String} employeeId
 */
StagedEmployee.prototype['employeeId'] = undefined;

/**
 * Employee ethnicity.<br  /> Max length: 10
 * @member {String} ethnicity
 */
StagedEmployee.prototype['ethnicity'] = undefined;

/**
 * Add federal tax amount type (taxCalculationCode), amount or percentage, filing status, and exemptions.
 * @member {Array.<module:model/StagedEmployeeFederalTaxInner>} federalTax
 */
StagedEmployee.prototype['federalTax'] = undefined;

/**
 * Employee first name. <br  />Max length: 40
 * @member {String} firstName
 */
StagedEmployee.prototype['firstName'] = undefined;

/**
 * Reason code for FITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
 * @member {String} fitwExemptReason
 */
StagedEmployee.prototype['fitwExemptReason'] = undefined;

/**
 * Reason code for FUTA exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).<br  /> Max length: 30
 * @member {String} futaExemptReason
 */
StagedEmployee.prototype['futaExemptReason'] = undefined;

/**
 * Employee gender. Common values *M* (Male), *F* (Female). <br  />Max length: 1
 * @member {String} gender
 */
StagedEmployee.prototype['gender'] = undefined;

/**
 * Add employee's home address, personal phone numbers, and personal email.
 * @member {Array.<module:model/StagedEmployeeHomeAddressInner>} homeAddress
 */
StagedEmployee.prototype['homeAddress'] = undefined;

/**
 * Indicates if employee in agriculture or farming.
 * @member {Boolean} isEmployee943
 */
StagedEmployee.prototype['isEmployee943'] = undefined;

/**
 * Indicates if employee is a smoker.
 * @member {Boolean} isSmoker
 */
StagedEmployee.prototype['isSmoker'] = undefined;

/**
 * Employee last name. <br  />Max length: 40
 * @member {String} lastName
 */
StagedEmployee.prototype['lastName'] = undefined;

/**
 * Add local tax code, filing status, and exemptions including PA-PSD taxes.
 * @member {Array.<module:model/EmployeeLocalTaxInner>} localTax
 */
StagedEmployee.prototype['localTax'] = undefined;

/**
 * Add the main direct deposit account. After deposits are made to any additional direct deposit accounts, the remaining net check is deposited in the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with what is provided on the request. GET API will not return direct deposit data.
 * @member {Array.<module:model/StagedEmployeeMainDirectDepositInner>} mainDirectDeposit
 */
StagedEmployee.prototype['mainDirectDeposit'] = undefined;

/**
 * Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. <br  />Max length: 10
 * @member {String} maritalStatus
 */
StagedEmployee.prototype['maritalStatus'] = undefined;

/**
 * Reason code for Medicare exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).<br  /> Max length: 30
 * @member {String} medExemptReason
 */
StagedEmployee.prototype['medExemptReason'] = undefined;

/**
 * Employee middle name.<br  /> Max length: 20
 * @member {String} middleName
 */
StagedEmployee.prototype['middleName'] = undefined;

/**
 * Add non-primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, supplemental check (specialCheckCalc), and reciprocity code information.
 * @member {Array.<module:model/StagedEmployeeNonPrimaryStateTaxInner>} nonPrimaryStateTax
 */
StagedEmployee.prototype['nonPrimaryStateTax'] = undefined;

/**
 * Employee preferred display name.<br  /> Max length: 20
 * @member {String} preferredName
 */
StagedEmployee.prototype['preferredName'] = undefined;

/**
 * Add hourly or salary pay rate, effective date, and pay frequency.
 * @member {Array.<module:model/StagedEmployeePrimaryPayRateInner>} primaryPayRate
 */
StagedEmployee.prototype['primaryPayRate'] = undefined;

/**
 * Add primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, and supplemental check (specialCheckCalc) information. Only one primary state is allowed.
 * @member {Array.<module:model/StagedEmployeePrimaryStateTaxInner>} primaryStateTax
 */
StagedEmployee.prototype['primaryStateTax'] = undefined;

/**
 * Prior last name if applicable.<br  />Max length: 40
 * @member {String} priorLastName
 */
StagedEmployee.prototype['priorLastName'] = undefined;

/**
 * Employee preferred salutation. <br  />Max length: 10
 * @member {String} salutation
 */
StagedEmployee.prototype['salutation'] = undefined;

/**
 * Reason code for SITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
 * @member {String} sitwExemptReason
 */
StagedEmployee.prototype['sitwExemptReason'] = undefined;

/**
 * Reason code for Social Security exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
 * @member {String} ssExemptReason
 */
StagedEmployee.prototype['ssExemptReason'] = undefined;

/**
 * Employee social security number. Leave it blank if valid social security number not available. <br  />Max length: 11
 * @member {String} ssn
 */
StagedEmployee.prototype['ssn'] = undefined;

/**
 * Add employee status, change reason, effective date, and adjusted seniority date. Note that companies that are still in Implementation cannot hire future employees.
 * @member {Array.<module:model/StagedEmployeeStatusInner>} status
 */
StagedEmployee.prototype['status'] = undefined;

/**
 * Employee name suffix. Common values are *Jr, Sr, II*.<br  />Max length: 30
 * @member {String} suffix
 */
StagedEmployee.prototype['suffix'] = undefined;

/**
 * Reason code for SUI exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). <br  /> Max length: 30
 * @member {String} suiExemptReason
 */
StagedEmployee.prototype['suiExemptReason'] = undefined;

/**
 * Employee SUI (State Unemployment Insurance) state. <br  />Max length: 2
 * @member {String} suiState
 */
StagedEmployee.prototype['suiState'] = undefined;

/**
 * Employee 1099R distribution code. Common values are *7* (Normal Distribution), *F* (Charitable Gift Annuity). <br  />Max length: 1
 * @member {String} taxDistributionCode1099R
 */
StagedEmployee.prototype['taxDistributionCode1099R'] = undefined;

/**
 * Employee tax form for reporting income. Valid values are *W2, 1099M, 1099R*. Default is W2. <br  />Max length: 15
 * @member {String} taxForm
 */
StagedEmployee.prototype['taxForm'] = undefined;

/**
 * Indicates if employee is a veteran.
 * @member {String} veteranDescription
 */
StagedEmployee.prototype['veteranDescription'] = undefined;

/**
 * @member {module:model/StagedEmployeeWebTime} webTime
 */
StagedEmployee.prototype['webTime'] = undefined;

/**
 * Add employee's work address, phone numbers, and email. Work Location drop down field is not included.
 * @member {Array.<module:model/StagedEmployeeWorkAddressInner>} workAddress
 */
StagedEmployee.prototype['workAddress'] = undefined;

/**
 * Add I-9 work authorization information.
 * @member {Array.<module:model/StagedEmployeeWorkEligibilityInner>} workEligibility
 */
StagedEmployee.prototype['workEligibility'] = undefined;






export default StagedEmployee;

