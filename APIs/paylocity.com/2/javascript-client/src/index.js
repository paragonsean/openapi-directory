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


import ApiClient from './ApiClient';
import AddClientSecret from './model/AddClientSecret';
import AdditionalRate from './model/AdditionalRate';
import BenefitSetup from './model/BenefitSetup';
import ClientCredentialsResponse from './model/ClientCredentialsResponse';
import CompanyCodes from './model/CompanyCodes';
import CustomFieldDefinition from './model/CustomFieldDefinition';
import CustomFieldDefinitionValuesInner from './model/CustomFieldDefinitionValuesInner';
import DirectDeposit from './model/DirectDeposit';
import DirectDepositAdditionalDirectDepositInner from './model/DirectDepositAdditionalDirectDepositInner';
import DirectDepositMainDirectDeposit from './model/DirectDepositMainDirectDeposit';
import Earning from './model/Earning';
import EmergencyContact from './model/EmergencyContact';
import Employee from './model/Employee';
import EmployeeAdditionalRateInner from './model/EmployeeAdditionalRateInner';
import EmployeeBenefitSetup from './model/EmployeeBenefitSetup';
import EmployeeCustomBooleanFieldsInner from './model/EmployeeCustomBooleanFieldsInner';
import EmployeeCustomDateFieldsInner from './model/EmployeeCustomDateFieldsInner';
import EmployeeCustomDropDownFieldsInner from './model/EmployeeCustomDropDownFieldsInner';
import EmployeeCustomNumberFieldsInner from './model/EmployeeCustomNumberFieldsInner';
import EmployeeCustomTextFieldsInner from './model/EmployeeCustomTextFieldsInner';
import EmployeeDepartmentPosition from './model/EmployeeDepartmentPosition';
import EmployeeEmergencyContactsInner from './model/EmployeeEmergencyContactsInner';
import EmployeeFederalTax from './model/EmployeeFederalTax';
import EmployeeHomeAddress from './model/EmployeeHomeAddress';
import EmployeeIdResponse from './model/EmployeeIdResponse';
import EmployeeInfo from './model/EmployeeInfo';
import EmployeeLocalTaxInner from './model/EmployeeLocalTaxInner';
import EmployeeMainDirectDeposit from './model/EmployeeMainDirectDeposit';
import EmployeeNonPrimaryStateTax from './model/EmployeeNonPrimaryStateTax';
import EmployeePrimaryPayRate from './model/EmployeePrimaryPayRate';
import EmployeePrimaryStateTax from './model/EmployeePrimaryStateTax';
import EmployeeStatus from './model/EmployeeStatus';
import EmployeeTaxSetup from './model/EmployeeTaxSetup';
import EmployeeWebTime from './model/EmployeeWebTime';
import EmployeeWorkAddress from './model/EmployeeWorkAddress';
import EmployeeWorkEligibility from './model/EmployeeWorkEligibility';
import Error from './model/Error';
import ErrorOptionsInner from './model/ErrorOptionsInner';
import LocalTax from './model/LocalTax';
import NonPrimaryStateTax from './model/NonPrimaryStateTax';
import PayStatementDetails from './model/PayStatementDetails';
import PayStatementSummary from './model/PayStatementSummary';
import SensitiveData from './model/SensitiveData';
import SensitiveDataDisability from './model/SensitiveDataDisability';
import SensitiveDataDisabilityDisabilityClassificationsInner from './model/SensitiveDataDisabilityDisabilityClassificationsInner';
import SensitiveDataEthnicity from './model/SensitiveDataEthnicity';
import SensitiveDataEthnicityEthnicRacialIdentitiesInner from './model/SensitiveDataEthnicityEthnicRacialIdentitiesInner';
import SensitiveDataGender from './model/SensitiveDataGender';
import SensitiveDataVeteran from './model/SensitiveDataVeteran';
import StagedEmployee from './model/StagedEmployee';
import StagedEmployeeAdditionalDirectDepositInner from './model/StagedEmployeeAdditionalDirectDepositInner';
import StagedEmployeeBenefitSetupInner from './model/StagedEmployeeBenefitSetupInner';
import StagedEmployeeDepartmentPositionInner from './model/StagedEmployeeDepartmentPositionInner';
import StagedEmployeeFederalTaxInner from './model/StagedEmployeeFederalTaxInner';
import StagedEmployeeHomeAddressInner from './model/StagedEmployeeHomeAddressInner';
import StagedEmployeeMainDirectDepositInner from './model/StagedEmployeeMainDirectDepositInner';
import StagedEmployeeNonPrimaryStateTaxInner from './model/StagedEmployeeNonPrimaryStateTaxInner';
import StagedEmployeePrimaryPayRateInner from './model/StagedEmployeePrimaryPayRateInner';
import StagedEmployeePrimaryStateTaxInner from './model/StagedEmployeePrimaryStateTaxInner';
import StagedEmployeeStatusInner from './model/StagedEmployeeStatusInner';
import StagedEmployeeWebTime from './model/StagedEmployeeWebTime';
import StagedEmployeeWorkAddressInner from './model/StagedEmployeeWorkAddressInner';
import StagedEmployeeWorkEligibilityInner from './model/StagedEmployeeWorkEligibilityInner';
import StateTax from './model/StateTax';
import TrackingNumberResponse from './model/TrackingNumberResponse';
import AdditionalRatesApi from './api/AdditionalRatesApi';
import ClientCredentialsApi from './api/ClientCredentialsApi';
import CompanyCodesApi from './api/CompanyCodesApi';
import CompanySpecificSchemaApi from './api/CompanySpecificSchemaApi';
import CustomFieldsApi from './api/CustomFieldsApi';
import DirectDepositApi from './api/DirectDepositApi';
import EarningsApi from './api/EarningsApi';
import EmergencyContactsApi from './api/EmergencyContactsApi';
import EmployeeApi from './api/EmployeeApi';
import EmployeeBenefitSetupApi from './api/EmployeeBenefitSetupApi';
import EmployeeStagingApi from './api/EmployeeStagingApi';
import LocalTaxesApi from './api/LocalTaxesApi';
import NonPrimaryStateTaxApi from './api/NonPrimaryStateTaxApi';
import PayStatementsApi from './api/PayStatementsApi';
import PrimaryStateTaxApi from './api/PrimaryStateTaxApi';
import SensitiveDataApi from './api/SensitiveDataApi';


/**
* For general questions and support of the API, contact: webservices@paylocity.com  # Overview    Paylocity Web Services API is an externally facing RESTful Internet protocol. The Paylocity API uses HTTP verbs and a RESTful endpoint structure. OAuth 2.0 is used as the API Authorization framework. Request and response payloads are formatted as JSON.  Paylocity supports v1 and v2 versions of its API endpoints. v1, while supported, won&#39;t be enhanced with additional functionality. For direct link to v1 documentation, please click [here](https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm). For additional resources regarding v1/v2 differences and conversion path, please contact webservices@paylocity.com.    ##### Setup    Paylocity will provide the secure client credentials and set up the scope (type of requests and allowed company numbers). You will receive the unique client id, secret, and Paylocity public key for the data encryption. The secret will expire in 365 days.   * Paylocity will send you an e-mail 10 days prior to the expiration date for the current secret. If not renewed, the second e-mail notification will be sent 5 days prior to secret&#39;s expiration. Each email will contain the code necessary to renew the client secret.   * You can obtain the new secret by calling API endpoint using your current not yet expired credentials and the code that was sent with the notification email. For details on API endpoint, please see Client Credentials section.   * Both the current secret value and the new secret value will be recognized during the transition period. After the current secret expires, you must use the new secret.   * If you were unable to renew the secret via API endpoint, you can still contact Service and they will email you new secret via secure email.      When validating the request, Paylocity API will honor the defaults and required fields set up for the company default New Hire Template as defined in Web Pay.      # Authorization    Paylocity Web Services API uses OAuth2.0 Authentication with JSON Message Format.      All requests of the Paylocity Web Services API require a bearer token which can be obtained by authenticating the client with the Paylocity Web Services API via OAuth 2.0.      The client must request a bearer token from the authorization endpoint:      auth-server for production: https://api.paylocity.com/IdentityServer/connect/token      auth-server for testing: https://apisandbox.paylocity.com/IdentityServer/connect/token    Paylocity reserves the right to impose rate limits on the number of calls made to our APIs. Changes to API features/functionality may be made at anytime with or without prior notice.    ##### Authorization Header    The request is expected to be in the form of a basic authentication request, with the \&quot;Authorization\&quot; header containing the client-id and client-secret. This means the standard base-64 encoded user:password, prefixed with \&quot;Basic\&quot; as the value for the Authorization header, where user is the client-id and password is the client-secret.    ##### Content-Type Header    The \&quot;Content-Type\&quot; header is required to be \&quot;application/x-www-form-urlencoded\&quot;.    ##### Additional Values    The request must post the following form encoded values within the request body:        grant_type &#x3D; client_credentials      scope &#x3D; WebLinkAPI    ##### Responses    Success will return HTTP 200 OK with JSON content:        {        \&quot;access_token\&quot;: \&quot;xxx\&quot;,        \&quot;expires_in\&quot;: 3600,        \&quot;token_type\&quot;: \&quot;Bearer\&quot;      }    # Encryption    Paylocity uses a combination of RSA and AES cryptography. As part of the setup, each client is issued a public RSA key.    Paylocity recommends the encryption of the incoming requests as additional protection of the sensitive data. Clients can opt-out of the encryption during the initial setup process. Opt-out will allow Paylocity to process unencrypted requests.    The Paylocity Public Key has the following properties:    * 2048 bit key size    * PKCS1 key format    * PEM encoding    ##### Properties    * key (base 64 encoded): The AES symmetric key encrypted with the Paylocity Public Key. It is the key used to encrypt the content. Paylocity will decrypt the AES key using RSA decryption and use it to decrypt the content.    * iv (base 64 encoded): The AES IV (Initialization Vector) used when encrypting the content.    * content (base 64 encoded): The AES encrypted request. The key and iv provided in the secureContent request are used by Paylocity for decryption of the content.    We suggest using the following for the AES:    * CBC cipher mode    * PKCS7 padding    * 128 bit block size    * 256 bit key size    ##### Encryption Flow    * Generate the unencrypted JSON payload to POST/PUT  * Encrypt this JSON payload using your _own key and IV_ (NOT with the Paylocity public key)  * RSA encrypt the _key_ you used in step 2 with the Paylocity Public Key, then, base64 encode the result  * Base64 encode the IV used to encrypt the JSON payload in step 2  * Put together a \&quot;securecontent\&quot; JSON object:     {    &#39;secureContent&#39; : {      &#39;key&#39; : -- RSA-encrypted &amp; base64 encoded key from step 3,      &#39;iv&#39; : -- base64 encoded iv from step 4      &#39;content&#39; -- content encrypted with your own key from step 2, base64 encoded    }  }    ##### Sample Example        {        \&quot;secureContent\&quot;: {          \&quot;key\&quot;: \&quot;eS3aw6H/qzHMJ00gSi6gQ3xa08DPMazk8BFY96Pd99ODA&#x3D;&#x3D;\&quot;,          \&quot;iv\&quot;: \&quot;NLyXMGq9svw0XO5aI9BzWw&#x3D;&#x3D;\&quot;,          \&quot;content\&quot;: \&quot;gAEOiQltO1w+LzGUoIK8FiYbU42hug94EasSl7N+Q1w&#x3D;\&quot;        }      }    ##### Sample C# Code        using Newtonsoft.Json;      using System;      using System.IO;      using System.Security.Cryptography;      using System.Text;        public class SecuredContent      {        [JsonProperty(\&quot;key\&quot;)]        public string Key { get; set; }          [JsonProperty(\&quot;iv\&quot;)]        public string Iv { get; set; }          [JsonProperty(\&quot;content\&quot;)]        public string Content { get; set; }        }        public class EndUserSecureRequestExample      {        public string CreateSecuredRequest(FileInfo paylocityPublicKey, string unsecuredJsonRequest)        {          string publicKeyXml &#x3D; File.ReadAllText(paylocityPublicKey.FullName, Encoding.UTF8);            SecuredContent secureContent &#x3D; this.CreateSecuredContent(publicKeyXml, unsecuredJsonRequest);            string secureRequest &#x3D; JsonConvert.SerializeObject(new { secureContent });            return secureRequest;        }          private SecuredContent CreateSecuredContent(string publicKeyXml, string request)        {          using (AesCryptoServiceProvider aesCsp &#x3D; new AesCryptoServiceProvider())          {            aesCsp.Mode &#x3D; CipherMode.CBC;            aesCsp.Padding &#x3D; PaddingMode.PKCS7;            aesCsp.BlockSize &#x3D; 128;            aesCsp.KeySize &#x3D; 256;              using (ICryptoTransform crt &#x3D; aesCsp.CreateEncryptor(aesCsp.Key, aesCsp.IV))            {              using (MemoryStream outputStream &#x3D; new MemoryStream())              {                using (CryptoStream encryptStream &#x3D; new CryptoStream(outputStream, crt, CryptoStreamMode.Write))                {                  byte[] encodedRequest &#x3D; Encoding.UTF8.GetBytes(request);                  encryptStream.Write(encodedRequest, 0, encodedRequest.Length);                  encryptStream.FlushFinalBlock();                  byte[] encryptedRequest &#x3D; outputStream.ToArray();                    using (RSACryptoServiceProvider crp &#x3D; new RSACryptoServiceProvider())                  {                    crp.FromXmlstring(publicKeyXml);                    byte[] encryptedKey &#x3D; crp.Encrypt(aesCsp.Key, false);                      return new SecuredContent()                    {                      Key &#x3D; Convert.ToBase64string(encryptedKey),                      Iv &#x3D; Convert.ToBase64string(aesCsp.IV),                      Content &#x3D; Convert.ToBase64string(encryptedRequest)                    };                  }                }              }            }          }        }      }    ## Support    Questions about using the Paylocity API? Please contact webservices@paylocity.com.    # Deductions (v1)    Deductions API provides endpoints to retrieve, add, update and delete deductions for a company&#39;s employees. For schema details, click &lt;a href&#x3D;\&quot;https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;.    # OnBoarding (v1)    Onboarding API sends employee data into Paylocity Onboarding to help ensure an easy and accurate hiring process for subsequent completion into Web Pay. For schema details, click &lt;a href&#x3D;\&quot;https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\&quot; target&#x3D;\&quot;_blank\&quot;&gt;here&lt;/a&gt;..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var PaylocityApi = require('index'); // See note below*.
* var xxxSvc = new PaylocityApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new PaylocityApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new PaylocityApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new PaylocityApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AddClientSecret model constructor.
     * @property {module:model/AddClientSecret}
     */
    AddClientSecret,

    /**
     * The AdditionalRate model constructor.
     * @property {module:model/AdditionalRate}
     */
    AdditionalRate,

    /**
     * The BenefitSetup model constructor.
     * @property {module:model/BenefitSetup}
     */
    BenefitSetup,

    /**
     * The ClientCredentialsResponse model constructor.
     * @property {module:model/ClientCredentialsResponse}
     */
    ClientCredentialsResponse,

    /**
     * The CompanyCodes model constructor.
     * @property {module:model/CompanyCodes}
     */
    CompanyCodes,

    /**
     * The CustomFieldDefinition model constructor.
     * @property {module:model/CustomFieldDefinition}
     */
    CustomFieldDefinition,

    /**
     * The CustomFieldDefinitionValuesInner model constructor.
     * @property {module:model/CustomFieldDefinitionValuesInner}
     */
    CustomFieldDefinitionValuesInner,

    /**
     * The DirectDeposit model constructor.
     * @property {module:model/DirectDeposit}
     */
    DirectDeposit,

    /**
     * The DirectDepositAdditionalDirectDepositInner model constructor.
     * @property {module:model/DirectDepositAdditionalDirectDepositInner}
     */
    DirectDepositAdditionalDirectDepositInner,

    /**
     * The DirectDepositMainDirectDeposit model constructor.
     * @property {module:model/DirectDepositMainDirectDeposit}
     */
    DirectDepositMainDirectDeposit,

    /**
     * The Earning model constructor.
     * @property {module:model/Earning}
     */
    Earning,

    /**
     * The EmergencyContact model constructor.
     * @property {module:model/EmergencyContact}
     */
    EmergencyContact,

    /**
     * The Employee model constructor.
     * @property {module:model/Employee}
     */
    Employee,

    /**
     * The EmployeeAdditionalRateInner model constructor.
     * @property {module:model/EmployeeAdditionalRateInner}
     */
    EmployeeAdditionalRateInner,

    /**
     * The EmployeeBenefitSetup model constructor.
     * @property {module:model/EmployeeBenefitSetup}
     */
    EmployeeBenefitSetup,

    /**
     * The EmployeeCustomBooleanFieldsInner model constructor.
     * @property {module:model/EmployeeCustomBooleanFieldsInner}
     */
    EmployeeCustomBooleanFieldsInner,

    /**
     * The EmployeeCustomDateFieldsInner model constructor.
     * @property {module:model/EmployeeCustomDateFieldsInner}
     */
    EmployeeCustomDateFieldsInner,

    /**
     * The EmployeeCustomDropDownFieldsInner model constructor.
     * @property {module:model/EmployeeCustomDropDownFieldsInner}
     */
    EmployeeCustomDropDownFieldsInner,

    /**
     * The EmployeeCustomNumberFieldsInner model constructor.
     * @property {module:model/EmployeeCustomNumberFieldsInner}
     */
    EmployeeCustomNumberFieldsInner,

    /**
     * The EmployeeCustomTextFieldsInner model constructor.
     * @property {module:model/EmployeeCustomTextFieldsInner}
     */
    EmployeeCustomTextFieldsInner,

    /**
     * The EmployeeDepartmentPosition model constructor.
     * @property {module:model/EmployeeDepartmentPosition}
     */
    EmployeeDepartmentPosition,

    /**
     * The EmployeeEmergencyContactsInner model constructor.
     * @property {module:model/EmployeeEmergencyContactsInner}
     */
    EmployeeEmergencyContactsInner,

    /**
     * The EmployeeFederalTax model constructor.
     * @property {module:model/EmployeeFederalTax}
     */
    EmployeeFederalTax,

    /**
     * The EmployeeHomeAddress model constructor.
     * @property {module:model/EmployeeHomeAddress}
     */
    EmployeeHomeAddress,

    /**
     * The EmployeeIdResponse model constructor.
     * @property {module:model/EmployeeIdResponse}
     */
    EmployeeIdResponse,

    /**
     * The EmployeeInfo model constructor.
     * @property {module:model/EmployeeInfo}
     */
    EmployeeInfo,

    /**
     * The EmployeeLocalTaxInner model constructor.
     * @property {module:model/EmployeeLocalTaxInner}
     */
    EmployeeLocalTaxInner,

    /**
     * The EmployeeMainDirectDeposit model constructor.
     * @property {module:model/EmployeeMainDirectDeposit}
     */
    EmployeeMainDirectDeposit,

    /**
     * The EmployeeNonPrimaryStateTax model constructor.
     * @property {module:model/EmployeeNonPrimaryStateTax}
     */
    EmployeeNonPrimaryStateTax,

    /**
     * The EmployeePrimaryPayRate model constructor.
     * @property {module:model/EmployeePrimaryPayRate}
     */
    EmployeePrimaryPayRate,

    /**
     * The EmployeePrimaryStateTax model constructor.
     * @property {module:model/EmployeePrimaryStateTax}
     */
    EmployeePrimaryStateTax,

    /**
     * The EmployeeStatus model constructor.
     * @property {module:model/EmployeeStatus}
     */
    EmployeeStatus,

    /**
     * The EmployeeTaxSetup model constructor.
     * @property {module:model/EmployeeTaxSetup}
     */
    EmployeeTaxSetup,

    /**
     * The EmployeeWebTime model constructor.
     * @property {module:model/EmployeeWebTime}
     */
    EmployeeWebTime,

    /**
     * The EmployeeWorkAddress model constructor.
     * @property {module:model/EmployeeWorkAddress}
     */
    EmployeeWorkAddress,

    /**
     * The EmployeeWorkEligibility model constructor.
     * @property {module:model/EmployeeWorkEligibility}
     */
    EmployeeWorkEligibility,

    /**
     * The Error model constructor.
     * @property {module:model/Error}
     */
    Error,

    /**
     * The ErrorOptionsInner model constructor.
     * @property {module:model/ErrorOptionsInner}
     */
    ErrorOptionsInner,

    /**
     * The LocalTax model constructor.
     * @property {module:model/LocalTax}
     */
    LocalTax,

    /**
     * The NonPrimaryStateTax model constructor.
     * @property {module:model/NonPrimaryStateTax}
     */
    NonPrimaryStateTax,

    /**
     * The PayStatementDetails model constructor.
     * @property {module:model/PayStatementDetails}
     */
    PayStatementDetails,

    /**
     * The PayStatementSummary model constructor.
     * @property {module:model/PayStatementSummary}
     */
    PayStatementSummary,

    /**
     * The SensitiveData model constructor.
     * @property {module:model/SensitiveData}
     */
    SensitiveData,

    /**
     * The SensitiveDataDisability model constructor.
     * @property {module:model/SensitiveDataDisability}
     */
    SensitiveDataDisability,

    /**
     * The SensitiveDataDisabilityDisabilityClassificationsInner model constructor.
     * @property {module:model/SensitiveDataDisabilityDisabilityClassificationsInner}
     */
    SensitiveDataDisabilityDisabilityClassificationsInner,

    /**
     * The SensitiveDataEthnicity model constructor.
     * @property {module:model/SensitiveDataEthnicity}
     */
    SensitiveDataEthnicity,

    /**
     * The SensitiveDataEthnicityEthnicRacialIdentitiesInner model constructor.
     * @property {module:model/SensitiveDataEthnicityEthnicRacialIdentitiesInner}
     */
    SensitiveDataEthnicityEthnicRacialIdentitiesInner,

    /**
     * The SensitiveDataGender model constructor.
     * @property {module:model/SensitiveDataGender}
     */
    SensitiveDataGender,

    /**
     * The SensitiveDataVeteran model constructor.
     * @property {module:model/SensitiveDataVeteran}
     */
    SensitiveDataVeteran,

    /**
     * The StagedEmployee model constructor.
     * @property {module:model/StagedEmployee}
     */
    StagedEmployee,

    /**
     * The StagedEmployeeAdditionalDirectDepositInner model constructor.
     * @property {module:model/StagedEmployeeAdditionalDirectDepositInner}
     */
    StagedEmployeeAdditionalDirectDepositInner,

    /**
     * The StagedEmployeeBenefitSetupInner model constructor.
     * @property {module:model/StagedEmployeeBenefitSetupInner}
     */
    StagedEmployeeBenefitSetupInner,

    /**
     * The StagedEmployeeDepartmentPositionInner model constructor.
     * @property {module:model/StagedEmployeeDepartmentPositionInner}
     */
    StagedEmployeeDepartmentPositionInner,

    /**
     * The StagedEmployeeFederalTaxInner model constructor.
     * @property {module:model/StagedEmployeeFederalTaxInner}
     */
    StagedEmployeeFederalTaxInner,

    /**
     * The StagedEmployeeHomeAddressInner model constructor.
     * @property {module:model/StagedEmployeeHomeAddressInner}
     */
    StagedEmployeeHomeAddressInner,

    /**
     * The StagedEmployeeMainDirectDepositInner model constructor.
     * @property {module:model/StagedEmployeeMainDirectDepositInner}
     */
    StagedEmployeeMainDirectDepositInner,

    /**
     * The StagedEmployeeNonPrimaryStateTaxInner model constructor.
     * @property {module:model/StagedEmployeeNonPrimaryStateTaxInner}
     */
    StagedEmployeeNonPrimaryStateTaxInner,

    /**
     * The StagedEmployeePrimaryPayRateInner model constructor.
     * @property {module:model/StagedEmployeePrimaryPayRateInner}
     */
    StagedEmployeePrimaryPayRateInner,

    /**
     * The StagedEmployeePrimaryStateTaxInner model constructor.
     * @property {module:model/StagedEmployeePrimaryStateTaxInner}
     */
    StagedEmployeePrimaryStateTaxInner,

    /**
     * The StagedEmployeeStatusInner model constructor.
     * @property {module:model/StagedEmployeeStatusInner}
     */
    StagedEmployeeStatusInner,

    /**
     * The StagedEmployeeWebTime model constructor.
     * @property {module:model/StagedEmployeeWebTime}
     */
    StagedEmployeeWebTime,

    /**
     * The StagedEmployeeWorkAddressInner model constructor.
     * @property {module:model/StagedEmployeeWorkAddressInner}
     */
    StagedEmployeeWorkAddressInner,

    /**
     * The StagedEmployeeWorkEligibilityInner model constructor.
     * @property {module:model/StagedEmployeeWorkEligibilityInner}
     */
    StagedEmployeeWorkEligibilityInner,

    /**
     * The StateTax model constructor.
     * @property {module:model/StateTax}
     */
    StateTax,

    /**
     * The TrackingNumberResponse model constructor.
     * @property {module:model/TrackingNumberResponse}
     */
    TrackingNumberResponse,

    /**
    * The AdditionalRatesApi service constructor.
    * @property {module:api/AdditionalRatesApi}
    */
    AdditionalRatesApi,

    /**
    * The ClientCredentialsApi service constructor.
    * @property {module:api/ClientCredentialsApi}
    */
    ClientCredentialsApi,

    /**
    * The CompanyCodesApi service constructor.
    * @property {module:api/CompanyCodesApi}
    */
    CompanyCodesApi,

    /**
    * The CompanySpecificSchemaApi service constructor.
    * @property {module:api/CompanySpecificSchemaApi}
    */
    CompanySpecificSchemaApi,

    /**
    * The CustomFieldsApi service constructor.
    * @property {module:api/CustomFieldsApi}
    */
    CustomFieldsApi,

    /**
    * The DirectDepositApi service constructor.
    * @property {module:api/DirectDepositApi}
    */
    DirectDepositApi,

    /**
    * The EarningsApi service constructor.
    * @property {module:api/EarningsApi}
    */
    EarningsApi,

    /**
    * The EmergencyContactsApi service constructor.
    * @property {module:api/EmergencyContactsApi}
    */
    EmergencyContactsApi,

    /**
    * The EmployeeApi service constructor.
    * @property {module:api/EmployeeApi}
    */
    EmployeeApi,

    /**
    * The EmployeeBenefitSetupApi service constructor.
    * @property {module:api/EmployeeBenefitSetupApi}
    */
    EmployeeBenefitSetupApi,

    /**
    * The EmployeeStagingApi service constructor.
    * @property {module:api/EmployeeStagingApi}
    */
    EmployeeStagingApi,

    /**
    * The LocalTaxesApi service constructor.
    * @property {module:api/LocalTaxesApi}
    */
    LocalTaxesApi,

    /**
    * The NonPrimaryStateTaxApi service constructor.
    * @property {module:api/NonPrimaryStateTaxApi}
    */
    NonPrimaryStateTaxApi,

    /**
    * The PayStatementsApi service constructor.
    * @property {module:api/PayStatementsApi}
    */
    PayStatementsApi,

    /**
    * The PrimaryStateTaxApi service constructor.
    * @property {module:api/PrimaryStateTaxApi}
    */
    PrimaryStateTaxApi,

    /**
    * The SensitiveDataApi service constructor.
    * @property {module:api/SensitiveDataApi}
    */
    SensitiveDataApi
};
