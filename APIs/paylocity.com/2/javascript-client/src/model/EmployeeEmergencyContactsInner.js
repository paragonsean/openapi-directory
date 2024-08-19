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
 * The EmployeeEmergencyContactsInner model module.
 * @module model/EmployeeEmergencyContactsInner
 * @version 2
 */
class EmployeeEmergencyContactsInner {
    /**
     * Constructs a new <code>EmployeeEmergencyContactsInner</code>.
     * The emergency contact model
     * @alias module:model/EmployeeEmergencyContactsInner
     * @param firstName {String} Required. Contact first name. <br  />Max length: 40
     * @param lastName {String} Required. Contact last name. <br  />Max length: 40
     */
    constructor(firstName, lastName) { 
        
        EmployeeEmergencyContactsInner.initialize(this, firstName, lastName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, firstName, lastName) { 
        obj['firstName'] = firstName;
        obj['lastName'] = lastName;
    }

    /**
     * Constructs a <code>EmployeeEmergencyContactsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EmployeeEmergencyContactsInner} obj Optional instance to populate.
     * @return {module:model/EmployeeEmergencyContactsInner} The populated <code>EmployeeEmergencyContactsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EmployeeEmergencyContactsInner();

            if (data.hasOwnProperty('address1')) {
                obj['address1'] = ApiClient.convertToType(data['address1'], 'String');
            }
            if (data.hasOwnProperty('address2')) {
                obj['address2'] = ApiClient.convertToType(data['address2'], 'String');
            }
            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('county')) {
                obj['county'] = ApiClient.convertToType(data['county'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('firstName')) {
                obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
            }
            if (data.hasOwnProperty('homePhone')) {
                obj['homePhone'] = ApiClient.convertToType(data['homePhone'], 'String');
            }
            if (data.hasOwnProperty('lastName')) {
                obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
            }
            if (data.hasOwnProperty('mobilePhone')) {
                obj['mobilePhone'] = ApiClient.convertToType(data['mobilePhone'], 'String');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('pager')) {
                obj['pager'] = ApiClient.convertToType(data['pager'], 'String');
            }
            if (data.hasOwnProperty('primaryPhone')) {
                obj['primaryPhone'] = ApiClient.convertToType(data['primaryPhone'], 'String');
            }
            if (data.hasOwnProperty('priority')) {
                obj['priority'] = ApiClient.convertToType(data['priority'], 'String');
            }
            if (data.hasOwnProperty('relationship')) {
                obj['relationship'] = ApiClient.convertToType(data['relationship'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
            if (data.hasOwnProperty('syncEmployeeInfo')) {
                obj['syncEmployeeInfo'] = ApiClient.convertToType(data['syncEmployeeInfo'], 'Boolean');
            }
            if (data.hasOwnProperty('workExtension')) {
                obj['workExtension'] = ApiClient.convertToType(data['workExtension'], 'String');
            }
            if (data.hasOwnProperty('workPhone')) {
                obj['workPhone'] = ApiClient.convertToType(data['workPhone'], 'String');
            }
            if (data.hasOwnProperty('zip')) {
                obj['zip'] = ApiClient.convertToType(data['zip'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EmployeeEmergencyContactsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EmployeeEmergencyContactsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EmployeeEmergencyContactsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['address1'] && !(typeof data['address1'] === 'string' || data['address1'] instanceof String)) {
            throw new Error("Expected the field `address1` to be a primitive type in the JSON string but got " + data['address1']);
        }
        // ensure the json data is a string
        if (data['address2'] && !(typeof data['address2'] === 'string' || data['address2'] instanceof String)) {
            throw new Error("Expected the field `address2` to be a primitive type in the JSON string but got " + data['address2']);
        }
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['county'] && !(typeof data['county'] === 'string' || data['county'] instanceof String)) {
            throw new Error("Expected the field `county` to be a primitive type in the JSON string but got " + data['county']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['firstName'] && !(typeof data['firstName'] === 'string' || data['firstName'] instanceof String)) {
            throw new Error("Expected the field `firstName` to be a primitive type in the JSON string but got " + data['firstName']);
        }
        // ensure the json data is a string
        if (data['homePhone'] && !(typeof data['homePhone'] === 'string' || data['homePhone'] instanceof String)) {
            throw new Error("Expected the field `homePhone` to be a primitive type in the JSON string but got " + data['homePhone']);
        }
        // ensure the json data is a string
        if (data['lastName'] && !(typeof data['lastName'] === 'string' || data['lastName'] instanceof String)) {
            throw new Error("Expected the field `lastName` to be a primitive type in the JSON string but got " + data['lastName']);
        }
        // ensure the json data is a string
        if (data['mobilePhone'] && !(typeof data['mobilePhone'] === 'string' || data['mobilePhone'] instanceof String)) {
            throw new Error("Expected the field `mobilePhone` to be a primitive type in the JSON string but got " + data['mobilePhone']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['pager'] && !(typeof data['pager'] === 'string' || data['pager'] instanceof String)) {
            throw new Error("Expected the field `pager` to be a primitive type in the JSON string but got " + data['pager']);
        }
        // ensure the json data is a string
        if (data['primaryPhone'] && !(typeof data['primaryPhone'] === 'string' || data['primaryPhone'] instanceof String)) {
            throw new Error("Expected the field `primaryPhone` to be a primitive type in the JSON string but got " + data['primaryPhone']);
        }
        // ensure the json data is a string
        if (data['priority'] && !(typeof data['priority'] === 'string' || data['priority'] instanceof String)) {
            throw new Error("Expected the field `priority` to be a primitive type in the JSON string but got " + data['priority']);
        }
        // ensure the json data is a string
        if (data['relationship'] && !(typeof data['relationship'] === 'string' || data['relationship'] instanceof String)) {
            throw new Error("Expected the field `relationship` to be a primitive type in the JSON string but got " + data['relationship']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }
        // ensure the json data is a string
        if (data['workExtension'] && !(typeof data['workExtension'] === 'string' || data['workExtension'] instanceof String)) {
            throw new Error("Expected the field `workExtension` to be a primitive type in the JSON string but got " + data['workExtension']);
        }
        // ensure the json data is a string
        if (data['workPhone'] && !(typeof data['workPhone'] === 'string' || data['workPhone'] instanceof String)) {
            throw new Error("Expected the field `workPhone` to be a primitive type in the JSON string but got " + data['workPhone']);
        }
        // ensure the json data is a string
        if (data['zip'] && !(typeof data['zip'] === 'string' || data['zip'] instanceof String)) {
            throw new Error("Expected the field `zip` to be a primitive type in the JSON string but got " + data['zip']);
        }

        return true;
    }


}

EmployeeEmergencyContactsInner.RequiredProperties = ["firstName", "lastName"];

/**
 * 1st address line.
 * @member {String} address1
 */
EmployeeEmergencyContactsInner.prototype['address1'] = undefined;

/**
 * 2nd address line.
 * @member {String} address2
 */
EmployeeEmergencyContactsInner.prototype['address2'] = undefined;

/**
 * City.
 * @member {String} city
 */
EmployeeEmergencyContactsInner.prototype['city'] = undefined;

/**
 * County.
 * @member {String} country
 */
EmployeeEmergencyContactsInner.prototype['country'] = undefined;

/**
 * Country.  Must be a valid 3 character country code.  Common values are *USA* (United States), *CAN* (Canada).
 * @member {String} county
 */
EmployeeEmergencyContactsInner.prototype['county'] = undefined;

/**
 * Contact email.  Must be valid email address format.
 * @member {String} email
 */
EmployeeEmergencyContactsInner.prototype['email'] = undefined;

/**
 * Required. Contact first name. <br  />Max length: 40
 * @member {String} firstName
 */
EmployeeEmergencyContactsInner.prototype['firstName'] = undefined;

/**
 * Contact Home Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.
 * @member {String} homePhone
 */
EmployeeEmergencyContactsInner.prototype['homePhone'] = undefined;

/**
 * Required. Contact last name. <br  />Max length: 40
 * @member {String} lastName
 */
EmployeeEmergencyContactsInner.prototype['lastName'] = undefined;

/**
 * Contact Mobile Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.
 * @member {String} mobilePhone
 */
EmployeeEmergencyContactsInner.prototype['mobilePhone'] = undefined;

/**
 * Notes. <br  />Max length: 1000
 * @member {String} notes
 */
EmployeeEmergencyContactsInner.prototype['notes'] = undefined;

/**
 * Contact Pager.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.
 * @member {String} pager
 */
EmployeeEmergencyContactsInner.prototype['pager'] = undefined;

/**
 * Required. Contact primary phone type.  Must match Company setup.  Valid  values are H (Home), M (Mobile), P (Pager), W (Work)
 * @member {String} primaryPhone
 */
EmployeeEmergencyContactsInner.prototype['primaryPhone'] = undefined;

/**
 * Required. Contact priority. Valid values are *P* (Primary) or *S* (Secondary).
 * @member {String} priority
 */
EmployeeEmergencyContactsInner.prototype['priority'] = undefined;

/**
 * Required. Contact relationship.  Must match Company setup.  Common values are Spouse, Mother, Father.
 * @member {String} relationship
 */
EmployeeEmergencyContactsInner.prototype['relationship'] = undefined;

/**
 * State or Province.  If U.S. address, must be valid 2 character state code.  Common values are *IL* (Illinois), *CA* (California).
 * @member {String} state
 */
EmployeeEmergencyContactsInner.prototype['state'] = undefined;

/**
 * Valid values are *true* or *false*.
 * @member {Boolean} syncEmployeeInfo
 */
EmployeeEmergencyContactsInner.prototype['syncEmployeeInfo'] = undefined;

/**
 * Work Extension.
 * @member {String} workExtension
 */
EmployeeEmergencyContactsInner.prototype['workExtension'] = undefined;

/**
 * Contact Work Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed.
 * @member {String} workPhone
 */
EmployeeEmergencyContactsInner.prototype['workPhone'] = undefined;

/**
 * Postal code.  If U.S. address, must be a valid zip code.
 * @member {String} zip
 */
EmployeeEmergencyContactsInner.prototype['zip'] = undefined;






export default EmployeeEmergencyContactsInner;

