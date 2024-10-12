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
 */

#include "OAIStagedEmployee.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStagedEmployee::OAIStagedEmployee(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStagedEmployee::OAIStagedEmployee() {
    this->initializeModel();
}

OAIStagedEmployee::~OAIStagedEmployee() {}

void OAIStagedEmployee::initializeModel() {

    m_additional_direct_deposit_isSet = false;
    m_additional_direct_deposit_isValid = false;

    m_benefit_setup_isSet = false;
    m_benefit_setup_isValid = false;

    m_birth_date_isSet = false;
    m_birth_date_isValid = false;

    m_custom_boolean_fields_isSet = false;
    m_custom_boolean_fields_isValid = false;

    m_custom_date_fields_isSet = false;
    m_custom_date_fields_isValid = false;

    m_custom_drop_down_fields_isSet = false;
    m_custom_drop_down_fields_isValid = false;

    m_custom_number_fields_isSet = false;
    m_custom_number_fields_isValid = false;

    m_custom_text_fields_isSet = false;
    m_custom_text_fields_isValid = false;

    m_department_position_isSet = false;
    m_department_position_isValid = false;

    m_disability_description_isSet = false;
    m_disability_description_isValid = false;

    m_employee_id_isSet = false;
    m_employee_id_isValid = false;

    m_ethnicity_isSet = false;
    m_ethnicity_isValid = false;

    m_federal_tax_isSet = false;
    m_federal_tax_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_fitw_exempt_reason_isSet = false;
    m_fitw_exempt_reason_isValid = false;

    m_futa_exempt_reason_isSet = false;
    m_futa_exempt_reason_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_home_address_isSet = false;
    m_home_address_isValid = false;

    m_is_employee943_isSet = false;
    m_is_employee943_isValid = false;

    m_is_smoker_isSet = false;
    m_is_smoker_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_local_tax_isSet = false;
    m_local_tax_isValid = false;

    m_main_direct_deposit_isSet = false;
    m_main_direct_deposit_isValid = false;

    m_marital_status_isSet = false;
    m_marital_status_isValid = false;

    m_med_exempt_reason_isSet = false;
    m_med_exempt_reason_isValid = false;

    m_middle_name_isSet = false;
    m_middle_name_isValid = false;

    m_non_primary_state_tax_isSet = false;
    m_non_primary_state_tax_isValid = false;

    m_preferred_name_isSet = false;
    m_preferred_name_isValid = false;

    m_primary_pay_rate_isSet = false;
    m_primary_pay_rate_isValid = false;

    m_primary_state_tax_isSet = false;
    m_primary_state_tax_isValid = false;

    m_prior_last_name_isSet = false;
    m_prior_last_name_isValid = false;

    m_salutation_isSet = false;
    m_salutation_isValid = false;

    m_sitw_exempt_reason_isSet = false;
    m_sitw_exempt_reason_isValid = false;

    m_ss_exempt_reason_isSet = false;
    m_ss_exempt_reason_isValid = false;

    m_ssn_isSet = false;
    m_ssn_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_suffix_isSet = false;
    m_suffix_isValid = false;

    m_sui_exempt_reason_isSet = false;
    m_sui_exempt_reason_isValid = false;

    m_sui_state_isSet = false;
    m_sui_state_isValid = false;

    m_tax_distribution_code1099_r_isSet = false;
    m_tax_distribution_code1099_r_isValid = false;

    m_tax_form_isSet = false;
    m_tax_form_isValid = false;

    m_veteran_description_isSet = false;
    m_veteran_description_isValid = false;

    m_web_time_isSet = false;
    m_web_time_isValid = false;

    m_work_address_isSet = false;
    m_work_address_isValid = false;

    m_work_eligibility_isSet = false;
    m_work_eligibility_isValid = false;
}

void OAIStagedEmployee::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStagedEmployee::fromJsonObject(QJsonObject json) {

    m_additional_direct_deposit_isValid = ::OpenAPI::fromJsonValue(m_additional_direct_deposit, json[QString("additionalDirectDeposit")]);
    m_additional_direct_deposit_isSet = !json[QString("additionalDirectDeposit")].isNull() && m_additional_direct_deposit_isValid;

    m_benefit_setup_isValid = ::OpenAPI::fromJsonValue(m_benefit_setup, json[QString("benefitSetup")]);
    m_benefit_setup_isSet = !json[QString("benefitSetup")].isNull() && m_benefit_setup_isValid;

    m_birth_date_isValid = ::OpenAPI::fromJsonValue(m_birth_date, json[QString("birthDate")]);
    m_birth_date_isSet = !json[QString("birthDate")].isNull() && m_birth_date_isValid;

    m_custom_boolean_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_boolean_fields, json[QString("customBooleanFields")]);
    m_custom_boolean_fields_isSet = !json[QString("customBooleanFields")].isNull() && m_custom_boolean_fields_isValid;

    m_custom_date_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_date_fields, json[QString("customDateFields")]);
    m_custom_date_fields_isSet = !json[QString("customDateFields")].isNull() && m_custom_date_fields_isValid;

    m_custom_drop_down_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_drop_down_fields, json[QString("customDropDownFields")]);
    m_custom_drop_down_fields_isSet = !json[QString("customDropDownFields")].isNull() && m_custom_drop_down_fields_isValid;

    m_custom_number_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_number_fields, json[QString("customNumberFields")]);
    m_custom_number_fields_isSet = !json[QString("customNumberFields")].isNull() && m_custom_number_fields_isValid;

    m_custom_text_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_text_fields, json[QString("customTextFields")]);
    m_custom_text_fields_isSet = !json[QString("customTextFields")].isNull() && m_custom_text_fields_isValid;

    m_department_position_isValid = ::OpenAPI::fromJsonValue(m_department_position, json[QString("departmentPosition")]);
    m_department_position_isSet = !json[QString("departmentPosition")].isNull() && m_department_position_isValid;

    m_disability_description_isValid = ::OpenAPI::fromJsonValue(m_disability_description, json[QString("disabilityDescription")]);
    m_disability_description_isSet = !json[QString("disabilityDescription")].isNull() && m_disability_description_isValid;

    m_employee_id_isValid = ::OpenAPI::fromJsonValue(m_employee_id, json[QString("employeeId")]);
    m_employee_id_isSet = !json[QString("employeeId")].isNull() && m_employee_id_isValid;

    m_ethnicity_isValid = ::OpenAPI::fromJsonValue(m_ethnicity, json[QString("ethnicity")]);
    m_ethnicity_isSet = !json[QString("ethnicity")].isNull() && m_ethnicity_isValid;

    m_federal_tax_isValid = ::OpenAPI::fromJsonValue(m_federal_tax, json[QString("federalTax")]);
    m_federal_tax_isSet = !json[QString("federalTax")].isNull() && m_federal_tax_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_fitw_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_fitw_exempt_reason, json[QString("fitwExemptReason")]);
    m_fitw_exempt_reason_isSet = !json[QString("fitwExemptReason")].isNull() && m_fitw_exempt_reason_isValid;

    m_futa_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_futa_exempt_reason, json[QString("futaExemptReason")]);
    m_futa_exempt_reason_isSet = !json[QString("futaExemptReason")].isNull() && m_futa_exempt_reason_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_home_address_isValid = ::OpenAPI::fromJsonValue(m_home_address, json[QString("homeAddress")]);
    m_home_address_isSet = !json[QString("homeAddress")].isNull() && m_home_address_isValid;

    m_is_employee943_isValid = ::OpenAPI::fromJsonValue(m_is_employee943, json[QString("isEmployee943")]);
    m_is_employee943_isSet = !json[QString("isEmployee943")].isNull() && m_is_employee943_isValid;

    m_is_smoker_isValid = ::OpenAPI::fromJsonValue(m_is_smoker, json[QString("isSmoker")]);
    m_is_smoker_isSet = !json[QString("isSmoker")].isNull() && m_is_smoker_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_local_tax_isValid = ::OpenAPI::fromJsonValue(m_local_tax, json[QString("localTax")]);
    m_local_tax_isSet = !json[QString("localTax")].isNull() && m_local_tax_isValid;

    m_main_direct_deposit_isValid = ::OpenAPI::fromJsonValue(m_main_direct_deposit, json[QString("mainDirectDeposit")]);
    m_main_direct_deposit_isSet = !json[QString("mainDirectDeposit")].isNull() && m_main_direct_deposit_isValid;

    m_marital_status_isValid = ::OpenAPI::fromJsonValue(m_marital_status, json[QString("maritalStatus")]);
    m_marital_status_isSet = !json[QString("maritalStatus")].isNull() && m_marital_status_isValid;

    m_med_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_med_exempt_reason, json[QString("medExemptReason")]);
    m_med_exempt_reason_isSet = !json[QString("medExemptReason")].isNull() && m_med_exempt_reason_isValid;

    m_middle_name_isValid = ::OpenAPI::fromJsonValue(m_middle_name, json[QString("middleName")]);
    m_middle_name_isSet = !json[QString("middleName")].isNull() && m_middle_name_isValid;

    m_non_primary_state_tax_isValid = ::OpenAPI::fromJsonValue(m_non_primary_state_tax, json[QString("nonPrimaryStateTax")]);
    m_non_primary_state_tax_isSet = !json[QString("nonPrimaryStateTax")].isNull() && m_non_primary_state_tax_isValid;

    m_preferred_name_isValid = ::OpenAPI::fromJsonValue(m_preferred_name, json[QString("preferredName")]);
    m_preferred_name_isSet = !json[QString("preferredName")].isNull() && m_preferred_name_isValid;

    m_primary_pay_rate_isValid = ::OpenAPI::fromJsonValue(m_primary_pay_rate, json[QString("primaryPayRate")]);
    m_primary_pay_rate_isSet = !json[QString("primaryPayRate")].isNull() && m_primary_pay_rate_isValid;

    m_primary_state_tax_isValid = ::OpenAPI::fromJsonValue(m_primary_state_tax, json[QString("primaryStateTax")]);
    m_primary_state_tax_isSet = !json[QString("primaryStateTax")].isNull() && m_primary_state_tax_isValid;

    m_prior_last_name_isValid = ::OpenAPI::fromJsonValue(m_prior_last_name, json[QString("priorLastName")]);
    m_prior_last_name_isSet = !json[QString("priorLastName")].isNull() && m_prior_last_name_isValid;

    m_salutation_isValid = ::OpenAPI::fromJsonValue(m_salutation, json[QString("salutation")]);
    m_salutation_isSet = !json[QString("salutation")].isNull() && m_salutation_isValid;

    m_sitw_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_sitw_exempt_reason, json[QString("sitwExemptReason")]);
    m_sitw_exempt_reason_isSet = !json[QString("sitwExemptReason")].isNull() && m_sitw_exempt_reason_isValid;

    m_ss_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_ss_exempt_reason, json[QString("ssExemptReason")]);
    m_ss_exempt_reason_isSet = !json[QString("ssExemptReason")].isNull() && m_ss_exempt_reason_isValid;

    m_ssn_isValid = ::OpenAPI::fromJsonValue(m_ssn, json[QString("ssn")]);
    m_ssn_isSet = !json[QString("ssn")].isNull() && m_ssn_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_suffix_isValid = ::OpenAPI::fromJsonValue(m_suffix, json[QString("suffix")]);
    m_suffix_isSet = !json[QString("suffix")].isNull() && m_suffix_isValid;

    m_sui_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_sui_exempt_reason, json[QString("suiExemptReason")]);
    m_sui_exempt_reason_isSet = !json[QString("suiExemptReason")].isNull() && m_sui_exempt_reason_isValid;

    m_sui_state_isValid = ::OpenAPI::fromJsonValue(m_sui_state, json[QString("suiState")]);
    m_sui_state_isSet = !json[QString("suiState")].isNull() && m_sui_state_isValid;

    m_tax_distribution_code1099_r_isValid = ::OpenAPI::fromJsonValue(m_tax_distribution_code1099_r, json[QString("taxDistributionCode1099R")]);
    m_tax_distribution_code1099_r_isSet = !json[QString("taxDistributionCode1099R")].isNull() && m_tax_distribution_code1099_r_isValid;

    m_tax_form_isValid = ::OpenAPI::fromJsonValue(m_tax_form, json[QString("taxForm")]);
    m_tax_form_isSet = !json[QString("taxForm")].isNull() && m_tax_form_isValid;

    m_veteran_description_isValid = ::OpenAPI::fromJsonValue(m_veteran_description, json[QString("veteranDescription")]);
    m_veteran_description_isSet = !json[QString("veteranDescription")].isNull() && m_veteran_description_isValid;

    m_web_time_isValid = ::OpenAPI::fromJsonValue(m_web_time, json[QString("webTime")]);
    m_web_time_isSet = !json[QString("webTime")].isNull() && m_web_time_isValid;

    m_work_address_isValid = ::OpenAPI::fromJsonValue(m_work_address, json[QString("workAddress")]);
    m_work_address_isSet = !json[QString("workAddress")].isNull() && m_work_address_isValid;

    m_work_eligibility_isValid = ::OpenAPI::fromJsonValue(m_work_eligibility, json[QString("workEligibility")]);
    m_work_eligibility_isSet = !json[QString("workEligibility")].isNull() && m_work_eligibility_isValid;
}

QString OAIStagedEmployee::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStagedEmployee::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_direct_deposit.size() > 0) {
        obj.insert(QString("additionalDirectDeposit"), ::OpenAPI::toJsonValue(m_additional_direct_deposit));
    }
    if (m_benefit_setup.size() > 0) {
        obj.insert(QString("benefitSetup"), ::OpenAPI::toJsonValue(m_benefit_setup));
    }
    if (m_birth_date_isSet) {
        obj.insert(QString("birthDate"), ::OpenAPI::toJsonValue(m_birth_date));
    }
    if (m_custom_boolean_fields.size() > 0) {
        obj.insert(QString("customBooleanFields"), ::OpenAPI::toJsonValue(m_custom_boolean_fields));
    }
    if (m_custom_date_fields.size() > 0) {
        obj.insert(QString("customDateFields"), ::OpenAPI::toJsonValue(m_custom_date_fields));
    }
    if (m_custom_drop_down_fields.size() > 0) {
        obj.insert(QString("customDropDownFields"), ::OpenAPI::toJsonValue(m_custom_drop_down_fields));
    }
    if (m_custom_number_fields.size() > 0) {
        obj.insert(QString("customNumberFields"), ::OpenAPI::toJsonValue(m_custom_number_fields));
    }
    if (m_custom_text_fields.size() > 0) {
        obj.insert(QString("customTextFields"), ::OpenAPI::toJsonValue(m_custom_text_fields));
    }
    if (m_department_position.size() > 0) {
        obj.insert(QString("departmentPosition"), ::OpenAPI::toJsonValue(m_department_position));
    }
    if (m_disability_description_isSet) {
        obj.insert(QString("disabilityDescription"), ::OpenAPI::toJsonValue(m_disability_description));
    }
    if (m_employee_id_isSet) {
        obj.insert(QString("employeeId"), ::OpenAPI::toJsonValue(m_employee_id));
    }
    if (m_ethnicity_isSet) {
        obj.insert(QString("ethnicity"), ::OpenAPI::toJsonValue(m_ethnicity));
    }
    if (m_federal_tax.size() > 0) {
        obj.insert(QString("federalTax"), ::OpenAPI::toJsonValue(m_federal_tax));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_fitw_exempt_reason_isSet) {
        obj.insert(QString("fitwExemptReason"), ::OpenAPI::toJsonValue(m_fitw_exempt_reason));
    }
    if (m_futa_exempt_reason_isSet) {
        obj.insert(QString("futaExemptReason"), ::OpenAPI::toJsonValue(m_futa_exempt_reason));
    }
    if (m_gender_isSet) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_home_address.size() > 0) {
        obj.insert(QString("homeAddress"), ::OpenAPI::toJsonValue(m_home_address));
    }
    if (m_is_employee943_isSet) {
        obj.insert(QString("isEmployee943"), ::OpenAPI::toJsonValue(m_is_employee943));
    }
    if (m_is_smoker_isSet) {
        obj.insert(QString("isSmoker"), ::OpenAPI::toJsonValue(m_is_smoker));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_local_tax.size() > 0) {
        obj.insert(QString("localTax"), ::OpenAPI::toJsonValue(m_local_tax));
    }
    if (m_main_direct_deposit.size() > 0) {
        obj.insert(QString("mainDirectDeposit"), ::OpenAPI::toJsonValue(m_main_direct_deposit));
    }
    if (m_marital_status_isSet) {
        obj.insert(QString("maritalStatus"), ::OpenAPI::toJsonValue(m_marital_status));
    }
    if (m_med_exempt_reason_isSet) {
        obj.insert(QString("medExemptReason"), ::OpenAPI::toJsonValue(m_med_exempt_reason));
    }
    if (m_middle_name_isSet) {
        obj.insert(QString("middleName"), ::OpenAPI::toJsonValue(m_middle_name));
    }
    if (m_non_primary_state_tax.size() > 0) {
        obj.insert(QString("nonPrimaryStateTax"), ::OpenAPI::toJsonValue(m_non_primary_state_tax));
    }
    if (m_preferred_name_isSet) {
        obj.insert(QString("preferredName"), ::OpenAPI::toJsonValue(m_preferred_name));
    }
    if (m_primary_pay_rate.size() > 0) {
        obj.insert(QString("primaryPayRate"), ::OpenAPI::toJsonValue(m_primary_pay_rate));
    }
    if (m_primary_state_tax.size() > 0) {
        obj.insert(QString("primaryStateTax"), ::OpenAPI::toJsonValue(m_primary_state_tax));
    }
    if (m_prior_last_name_isSet) {
        obj.insert(QString("priorLastName"), ::OpenAPI::toJsonValue(m_prior_last_name));
    }
    if (m_salutation_isSet) {
        obj.insert(QString("salutation"), ::OpenAPI::toJsonValue(m_salutation));
    }
    if (m_sitw_exempt_reason_isSet) {
        obj.insert(QString("sitwExemptReason"), ::OpenAPI::toJsonValue(m_sitw_exempt_reason));
    }
    if (m_ss_exempt_reason_isSet) {
        obj.insert(QString("ssExemptReason"), ::OpenAPI::toJsonValue(m_ss_exempt_reason));
    }
    if (m_ssn_isSet) {
        obj.insert(QString("ssn"), ::OpenAPI::toJsonValue(m_ssn));
    }
    if (m_status.size() > 0) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_suffix_isSet) {
        obj.insert(QString("suffix"), ::OpenAPI::toJsonValue(m_suffix));
    }
    if (m_sui_exempt_reason_isSet) {
        obj.insert(QString("suiExemptReason"), ::OpenAPI::toJsonValue(m_sui_exempt_reason));
    }
    if (m_sui_state_isSet) {
        obj.insert(QString("suiState"), ::OpenAPI::toJsonValue(m_sui_state));
    }
    if (m_tax_distribution_code1099_r_isSet) {
        obj.insert(QString("taxDistributionCode1099R"), ::OpenAPI::toJsonValue(m_tax_distribution_code1099_r));
    }
    if (m_tax_form_isSet) {
        obj.insert(QString("taxForm"), ::OpenAPI::toJsonValue(m_tax_form));
    }
    if (m_veteran_description_isSet) {
        obj.insert(QString("veteranDescription"), ::OpenAPI::toJsonValue(m_veteran_description));
    }
    if (m_web_time.isSet()) {
        obj.insert(QString("webTime"), ::OpenAPI::toJsonValue(m_web_time));
    }
    if (m_work_address.size() > 0) {
        obj.insert(QString("workAddress"), ::OpenAPI::toJsonValue(m_work_address));
    }
    if (m_work_eligibility.size() > 0) {
        obj.insert(QString("workEligibility"), ::OpenAPI::toJsonValue(m_work_eligibility));
    }
    return obj;
}

QList<OAIStagedEmployee_additionalDirectDeposit_inner> OAIStagedEmployee::getAdditionalDirectDeposit() const {
    return m_additional_direct_deposit;
}
void OAIStagedEmployee::setAdditionalDirectDeposit(const QList<OAIStagedEmployee_additionalDirectDeposit_inner> &additional_direct_deposit) {
    m_additional_direct_deposit = additional_direct_deposit;
    m_additional_direct_deposit_isSet = true;
}

bool OAIStagedEmployee::is_additional_direct_deposit_Set() const{
    return m_additional_direct_deposit_isSet;
}

bool OAIStagedEmployee::is_additional_direct_deposit_Valid() const{
    return m_additional_direct_deposit_isValid;
}

QList<OAIStagedEmployee_benefitSetup_inner> OAIStagedEmployee::getBenefitSetup() const {
    return m_benefit_setup;
}
void OAIStagedEmployee::setBenefitSetup(const QList<OAIStagedEmployee_benefitSetup_inner> &benefit_setup) {
    m_benefit_setup = benefit_setup;
    m_benefit_setup_isSet = true;
}

bool OAIStagedEmployee::is_benefit_setup_Set() const{
    return m_benefit_setup_isSet;
}

bool OAIStagedEmployee::is_benefit_setup_Valid() const{
    return m_benefit_setup_isValid;
}

QString OAIStagedEmployee::getBirthDate() const {
    return m_birth_date;
}
void OAIStagedEmployee::setBirthDate(const QString &birth_date) {
    m_birth_date = birth_date;
    m_birth_date_isSet = true;
}

bool OAIStagedEmployee::is_birth_date_Set() const{
    return m_birth_date_isSet;
}

bool OAIStagedEmployee::is_birth_date_Valid() const{
    return m_birth_date_isValid;
}

QList<OAIEmployee_customBooleanFields_inner> OAIStagedEmployee::getCustomBooleanFields() const {
    return m_custom_boolean_fields;
}
void OAIStagedEmployee::setCustomBooleanFields(const QList<OAIEmployee_customBooleanFields_inner> &custom_boolean_fields) {
    m_custom_boolean_fields = custom_boolean_fields;
    m_custom_boolean_fields_isSet = true;
}

bool OAIStagedEmployee::is_custom_boolean_fields_Set() const{
    return m_custom_boolean_fields_isSet;
}

bool OAIStagedEmployee::is_custom_boolean_fields_Valid() const{
    return m_custom_boolean_fields_isValid;
}

QList<OAIEmployee_customDateFields_inner> OAIStagedEmployee::getCustomDateFields() const {
    return m_custom_date_fields;
}
void OAIStagedEmployee::setCustomDateFields(const QList<OAIEmployee_customDateFields_inner> &custom_date_fields) {
    m_custom_date_fields = custom_date_fields;
    m_custom_date_fields_isSet = true;
}

bool OAIStagedEmployee::is_custom_date_fields_Set() const{
    return m_custom_date_fields_isSet;
}

bool OAIStagedEmployee::is_custom_date_fields_Valid() const{
    return m_custom_date_fields_isValid;
}

QList<OAIEmployee_customDropDownFields_inner> OAIStagedEmployee::getCustomDropDownFields() const {
    return m_custom_drop_down_fields;
}
void OAIStagedEmployee::setCustomDropDownFields(const QList<OAIEmployee_customDropDownFields_inner> &custom_drop_down_fields) {
    m_custom_drop_down_fields = custom_drop_down_fields;
    m_custom_drop_down_fields_isSet = true;
}

bool OAIStagedEmployee::is_custom_drop_down_fields_Set() const{
    return m_custom_drop_down_fields_isSet;
}

bool OAIStagedEmployee::is_custom_drop_down_fields_Valid() const{
    return m_custom_drop_down_fields_isValid;
}

QList<OAIEmployee_customNumberFields_inner> OAIStagedEmployee::getCustomNumberFields() const {
    return m_custom_number_fields;
}
void OAIStagedEmployee::setCustomNumberFields(const QList<OAIEmployee_customNumberFields_inner> &custom_number_fields) {
    m_custom_number_fields = custom_number_fields;
    m_custom_number_fields_isSet = true;
}

bool OAIStagedEmployee::is_custom_number_fields_Set() const{
    return m_custom_number_fields_isSet;
}

bool OAIStagedEmployee::is_custom_number_fields_Valid() const{
    return m_custom_number_fields_isValid;
}

QList<OAIEmployee_customTextFields_inner> OAIStagedEmployee::getCustomTextFields() const {
    return m_custom_text_fields;
}
void OAIStagedEmployee::setCustomTextFields(const QList<OAIEmployee_customTextFields_inner> &custom_text_fields) {
    m_custom_text_fields = custom_text_fields;
    m_custom_text_fields_isSet = true;
}

bool OAIStagedEmployee::is_custom_text_fields_Set() const{
    return m_custom_text_fields_isSet;
}

bool OAIStagedEmployee::is_custom_text_fields_Valid() const{
    return m_custom_text_fields_isValid;
}

QList<OAIStagedEmployee_departmentPosition_inner> OAIStagedEmployee::getDepartmentPosition() const {
    return m_department_position;
}
void OAIStagedEmployee::setDepartmentPosition(const QList<OAIStagedEmployee_departmentPosition_inner> &department_position) {
    m_department_position = department_position;
    m_department_position_isSet = true;
}

bool OAIStagedEmployee::is_department_position_Set() const{
    return m_department_position_isSet;
}

bool OAIStagedEmployee::is_department_position_Valid() const{
    return m_department_position_isValid;
}

QString OAIStagedEmployee::getDisabilityDescription() const {
    return m_disability_description;
}
void OAIStagedEmployee::setDisabilityDescription(const QString &disability_description) {
    m_disability_description = disability_description;
    m_disability_description_isSet = true;
}

bool OAIStagedEmployee::is_disability_description_Set() const{
    return m_disability_description_isSet;
}

bool OAIStagedEmployee::is_disability_description_Valid() const{
    return m_disability_description_isValid;
}

QString OAIStagedEmployee::getEmployeeId() const {
    return m_employee_id;
}
void OAIStagedEmployee::setEmployeeId(const QString &employee_id) {
    m_employee_id = employee_id;
    m_employee_id_isSet = true;
}

bool OAIStagedEmployee::is_employee_id_Set() const{
    return m_employee_id_isSet;
}

bool OAIStagedEmployee::is_employee_id_Valid() const{
    return m_employee_id_isValid;
}

QString OAIStagedEmployee::getEthnicity() const {
    return m_ethnicity;
}
void OAIStagedEmployee::setEthnicity(const QString &ethnicity) {
    m_ethnicity = ethnicity;
    m_ethnicity_isSet = true;
}

bool OAIStagedEmployee::is_ethnicity_Set() const{
    return m_ethnicity_isSet;
}

bool OAIStagedEmployee::is_ethnicity_Valid() const{
    return m_ethnicity_isValid;
}

QList<OAIStagedEmployee_federalTax_inner> OAIStagedEmployee::getFederalTax() const {
    return m_federal_tax;
}
void OAIStagedEmployee::setFederalTax(const QList<OAIStagedEmployee_federalTax_inner> &federal_tax) {
    m_federal_tax = federal_tax;
    m_federal_tax_isSet = true;
}

bool OAIStagedEmployee::is_federal_tax_Set() const{
    return m_federal_tax_isSet;
}

bool OAIStagedEmployee::is_federal_tax_Valid() const{
    return m_federal_tax_isValid;
}

QString OAIStagedEmployee::getFirstName() const {
    return m_first_name;
}
void OAIStagedEmployee::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIStagedEmployee::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIStagedEmployee::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIStagedEmployee::getFitwExemptReason() const {
    return m_fitw_exempt_reason;
}
void OAIStagedEmployee::setFitwExemptReason(const QString &fitw_exempt_reason) {
    m_fitw_exempt_reason = fitw_exempt_reason;
    m_fitw_exempt_reason_isSet = true;
}

bool OAIStagedEmployee::is_fitw_exempt_reason_Set() const{
    return m_fitw_exempt_reason_isSet;
}

bool OAIStagedEmployee::is_fitw_exempt_reason_Valid() const{
    return m_fitw_exempt_reason_isValid;
}

QString OAIStagedEmployee::getFutaExemptReason() const {
    return m_futa_exempt_reason;
}
void OAIStagedEmployee::setFutaExemptReason(const QString &futa_exempt_reason) {
    m_futa_exempt_reason = futa_exempt_reason;
    m_futa_exempt_reason_isSet = true;
}

bool OAIStagedEmployee::is_futa_exempt_reason_Set() const{
    return m_futa_exempt_reason_isSet;
}

bool OAIStagedEmployee::is_futa_exempt_reason_Valid() const{
    return m_futa_exempt_reason_isValid;
}

QString OAIStagedEmployee::getGender() const {
    return m_gender;
}
void OAIStagedEmployee::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIStagedEmployee::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIStagedEmployee::is_gender_Valid() const{
    return m_gender_isValid;
}

QList<OAIStagedEmployee_homeAddress_inner> OAIStagedEmployee::getHomeAddress() const {
    return m_home_address;
}
void OAIStagedEmployee::setHomeAddress(const QList<OAIStagedEmployee_homeAddress_inner> &home_address) {
    m_home_address = home_address;
    m_home_address_isSet = true;
}

bool OAIStagedEmployee::is_home_address_Set() const{
    return m_home_address_isSet;
}

bool OAIStagedEmployee::is_home_address_Valid() const{
    return m_home_address_isValid;
}

bool OAIStagedEmployee::isIsEmployee943() const {
    return m_is_employee943;
}
void OAIStagedEmployee::setIsEmployee943(const bool &is_employee943) {
    m_is_employee943 = is_employee943;
    m_is_employee943_isSet = true;
}

bool OAIStagedEmployee::is_is_employee943_Set() const{
    return m_is_employee943_isSet;
}

bool OAIStagedEmployee::is_is_employee943_Valid() const{
    return m_is_employee943_isValid;
}

bool OAIStagedEmployee::isIsSmoker() const {
    return m_is_smoker;
}
void OAIStagedEmployee::setIsSmoker(const bool &is_smoker) {
    m_is_smoker = is_smoker;
    m_is_smoker_isSet = true;
}

bool OAIStagedEmployee::is_is_smoker_Set() const{
    return m_is_smoker_isSet;
}

bool OAIStagedEmployee::is_is_smoker_Valid() const{
    return m_is_smoker_isValid;
}

QString OAIStagedEmployee::getLastName() const {
    return m_last_name;
}
void OAIStagedEmployee::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIStagedEmployee::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIStagedEmployee::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QList<OAIEmployee_localTax_inner> OAIStagedEmployee::getLocalTax() const {
    return m_local_tax;
}
void OAIStagedEmployee::setLocalTax(const QList<OAIEmployee_localTax_inner> &local_tax) {
    m_local_tax = local_tax;
    m_local_tax_isSet = true;
}

bool OAIStagedEmployee::is_local_tax_Set() const{
    return m_local_tax_isSet;
}

bool OAIStagedEmployee::is_local_tax_Valid() const{
    return m_local_tax_isValid;
}

QList<OAIStagedEmployee_mainDirectDeposit_inner> OAIStagedEmployee::getMainDirectDeposit() const {
    return m_main_direct_deposit;
}
void OAIStagedEmployee::setMainDirectDeposit(const QList<OAIStagedEmployee_mainDirectDeposit_inner> &main_direct_deposit) {
    m_main_direct_deposit = main_direct_deposit;
    m_main_direct_deposit_isSet = true;
}

bool OAIStagedEmployee::is_main_direct_deposit_Set() const{
    return m_main_direct_deposit_isSet;
}

bool OAIStagedEmployee::is_main_direct_deposit_Valid() const{
    return m_main_direct_deposit_isValid;
}

QString OAIStagedEmployee::getMaritalStatus() const {
    return m_marital_status;
}
void OAIStagedEmployee::setMaritalStatus(const QString &marital_status) {
    m_marital_status = marital_status;
    m_marital_status_isSet = true;
}

bool OAIStagedEmployee::is_marital_status_Set() const{
    return m_marital_status_isSet;
}

bool OAIStagedEmployee::is_marital_status_Valid() const{
    return m_marital_status_isValid;
}

QString OAIStagedEmployee::getMedExemptReason() const {
    return m_med_exempt_reason;
}
void OAIStagedEmployee::setMedExemptReason(const QString &med_exempt_reason) {
    m_med_exempt_reason = med_exempt_reason;
    m_med_exempt_reason_isSet = true;
}

bool OAIStagedEmployee::is_med_exempt_reason_Set() const{
    return m_med_exempt_reason_isSet;
}

bool OAIStagedEmployee::is_med_exempt_reason_Valid() const{
    return m_med_exempt_reason_isValid;
}

QString OAIStagedEmployee::getMiddleName() const {
    return m_middle_name;
}
void OAIStagedEmployee::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAIStagedEmployee::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAIStagedEmployee::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

QList<OAIStagedEmployee_nonPrimaryStateTax_inner> OAIStagedEmployee::getNonPrimaryStateTax() const {
    return m_non_primary_state_tax;
}
void OAIStagedEmployee::setNonPrimaryStateTax(const QList<OAIStagedEmployee_nonPrimaryStateTax_inner> &non_primary_state_tax) {
    m_non_primary_state_tax = non_primary_state_tax;
    m_non_primary_state_tax_isSet = true;
}

bool OAIStagedEmployee::is_non_primary_state_tax_Set() const{
    return m_non_primary_state_tax_isSet;
}

bool OAIStagedEmployee::is_non_primary_state_tax_Valid() const{
    return m_non_primary_state_tax_isValid;
}

QString OAIStagedEmployee::getPreferredName() const {
    return m_preferred_name;
}
void OAIStagedEmployee::setPreferredName(const QString &preferred_name) {
    m_preferred_name = preferred_name;
    m_preferred_name_isSet = true;
}

bool OAIStagedEmployee::is_preferred_name_Set() const{
    return m_preferred_name_isSet;
}

bool OAIStagedEmployee::is_preferred_name_Valid() const{
    return m_preferred_name_isValid;
}

QList<OAIStagedEmployee_primaryPayRate_inner> OAIStagedEmployee::getPrimaryPayRate() const {
    return m_primary_pay_rate;
}
void OAIStagedEmployee::setPrimaryPayRate(const QList<OAIStagedEmployee_primaryPayRate_inner> &primary_pay_rate) {
    m_primary_pay_rate = primary_pay_rate;
    m_primary_pay_rate_isSet = true;
}

bool OAIStagedEmployee::is_primary_pay_rate_Set() const{
    return m_primary_pay_rate_isSet;
}

bool OAIStagedEmployee::is_primary_pay_rate_Valid() const{
    return m_primary_pay_rate_isValid;
}

QList<OAIStagedEmployee_primaryStateTax_inner> OAIStagedEmployee::getPrimaryStateTax() const {
    return m_primary_state_tax;
}
void OAIStagedEmployee::setPrimaryStateTax(const QList<OAIStagedEmployee_primaryStateTax_inner> &primary_state_tax) {
    m_primary_state_tax = primary_state_tax;
    m_primary_state_tax_isSet = true;
}

bool OAIStagedEmployee::is_primary_state_tax_Set() const{
    return m_primary_state_tax_isSet;
}

bool OAIStagedEmployee::is_primary_state_tax_Valid() const{
    return m_primary_state_tax_isValid;
}

QString OAIStagedEmployee::getPriorLastName() const {
    return m_prior_last_name;
}
void OAIStagedEmployee::setPriorLastName(const QString &prior_last_name) {
    m_prior_last_name = prior_last_name;
    m_prior_last_name_isSet = true;
}

bool OAIStagedEmployee::is_prior_last_name_Set() const{
    return m_prior_last_name_isSet;
}

bool OAIStagedEmployee::is_prior_last_name_Valid() const{
    return m_prior_last_name_isValid;
}

QString OAIStagedEmployee::getSalutation() const {
    return m_salutation;
}
void OAIStagedEmployee::setSalutation(const QString &salutation) {
    m_salutation = salutation;
    m_salutation_isSet = true;
}

bool OAIStagedEmployee::is_salutation_Set() const{
    return m_salutation_isSet;
}

bool OAIStagedEmployee::is_salutation_Valid() const{
    return m_salutation_isValid;
}

QString OAIStagedEmployee::getSitwExemptReason() const {
    return m_sitw_exempt_reason;
}
void OAIStagedEmployee::setSitwExemptReason(const QString &sitw_exempt_reason) {
    m_sitw_exempt_reason = sitw_exempt_reason;
    m_sitw_exempt_reason_isSet = true;
}

bool OAIStagedEmployee::is_sitw_exempt_reason_Set() const{
    return m_sitw_exempt_reason_isSet;
}

bool OAIStagedEmployee::is_sitw_exempt_reason_Valid() const{
    return m_sitw_exempt_reason_isValid;
}

QString OAIStagedEmployee::getSsExemptReason() const {
    return m_ss_exempt_reason;
}
void OAIStagedEmployee::setSsExemptReason(const QString &ss_exempt_reason) {
    m_ss_exempt_reason = ss_exempt_reason;
    m_ss_exempt_reason_isSet = true;
}

bool OAIStagedEmployee::is_ss_exempt_reason_Set() const{
    return m_ss_exempt_reason_isSet;
}

bool OAIStagedEmployee::is_ss_exempt_reason_Valid() const{
    return m_ss_exempt_reason_isValid;
}

QString OAIStagedEmployee::getSsn() const {
    return m_ssn;
}
void OAIStagedEmployee::setSsn(const QString &ssn) {
    m_ssn = ssn;
    m_ssn_isSet = true;
}

bool OAIStagedEmployee::is_ssn_Set() const{
    return m_ssn_isSet;
}

bool OAIStagedEmployee::is_ssn_Valid() const{
    return m_ssn_isValid;
}

QList<OAIStagedEmployee_status_inner> OAIStagedEmployee::getStatus() const {
    return m_status;
}
void OAIStagedEmployee::setStatus(const QList<OAIStagedEmployee_status_inner> &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIStagedEmployee::is_status_Set() const{
    return m_status_isSet;
}

bool OAIStagedEmployee::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIStagedEmployee::getSuffix() const {
    return m_suffix;
}
void OAIStagedEmployee::setSuffix(const QString &suffix) {
    m_suffix = suffix;
    m_suffix_isSet = true;
}

bool OAIStagedEmployee::is_suffix_Set() const{
    return m_suffix_isSet;
}

bool OAIStagedEmployee::is_suffix_Valid() const{
    return m_suffix_isValid;
}

QString OAIStagedEmployee::getSuiExemptReason() const {
    return m_sui_exempt_reason;
}
void OAIStagedEmployee::setSuiExemptReason(const QString &sui_exempt_reason) {
    m_sui_exempt_reason = sui_exempt_reason;
    m_sui_exempt_reason_isSet = true;
}

bool OAIStagedEmployee::is_sui_exempt_reason_Set() const{
    return m_sui_exempt_reason_isSet;
}

bool OAIStagedEmployee::is_sui_exempt_reason_Valid() const{
    return m_sui_exempt_reason_isValid;
}

QString OAIStagedEmployee::getSuiState() const {
    return m_sui_state;
}
void OAIStagedEmployee::setSuiState(const QString &sui_state) {
    m_sui_state = sui_state;
    m_sui_state_isSet = true;
}

bool OAIStagedEmployee::is_sui_state_Set() const{
    return m_sui_state_isSet;
}

bool OAIStagedEmployee::is_sui_state_Valid() const{
    return m_sui_state_isValid;
}

QString OAIStagedEmployee::getTaxDistributionCode1099R() const {
    return m_tax_distribution_code1099_r;
}
void OAIStagedEmployee::setTaxDistributionCode1099R(const QString &tax_distribution_code1099_r) {
    m_tax_distribution_code1099_r = tax_distribution_code1099_r;
    m_tax_distribution_code1099_r_isSet = true;
}

bool OAIStagedEmployee::is_tax_distribution_code1099_r_Set() const{
    return m_tax_distribution_code1099_r_isSet;
}

bool OAIStagedEmployee::is_tax_distribution_code1099_r_Valid() const{
    return m_tax_distribution_code1099_r_isValid;
}

QString OAIStagedEmployee::getTaxForm() const {
    return m_tax_form;
}
void OAIStagedEmployee::setTaxForm(const QString &tax_form) {
    m_tax_form = tax_form;
    m_tax_form_isSet = true;
}

bool OAIStagedEmployee::is_tax_form_Set() const{
    return m_tax_form_isSet;
}

bool OAIStagedEmployee::is_tax_form_Valid() const{
    return m_tax_form_isValid;
}

QString OAIStagedEmployee::getVeteranDescription() const {
    return m_veteran_description;
}
void OAIStagedEmployee::setVeteranDescription(const QString &veteran_description) {
    m_veteran_description = veteran_description;
    m_veteran_description_isSet = true;
}

bool OAIStagedEmployee::is_veteran_description_Set() const{
    return m_veteran_description_isSet;
}

bool OAIStagedEmployee::is_veteran_description_Valid() const{
    return m_veteran_description_isValid;
}

OAIStagedEmployee_webTime OAIStagedEmployee::getWebTime() const {
    return m_web_time;
}
void OAIStagedEmployee::setWebTime(const OAIStagedEmployee_webTime &web_time) {
    m_web_time = web_time;
    m_web_time_isSet = true;
}

bool OAIStagedEmployee::is_web_time_Set() const{
    return m_web_time_isSet;
}

bool OAIStagedEmployee::is_web_time_Valid() const{
    return m_web_time_isValid;
}

QList<OAIStagedEmployee_workAddress_inner> OAIStagedEmployee::getWorkAddress() const {
    return m_work_address;
}
void OAIStagedEmployee::setWorkAddress(const QList<OAIStagedEmployee_workAddress_inner> &work_address) {
    m_work_address = work_address;
    m_work_address_isSet = true;
}

bool OAIStagedEmployee::is_work_address_Set() const{
    return m_work_address_isSet;
}

bool OAIStagedEmployee::is_work_address_Valid() const{
    return m_work_address_isValid;
}

QList<OAIStagedEmployee_workEligibility_inner> OAIStagedEmployee::getWorkEligibility() const {
    return m_work_eligibility;
}
void OAIStagedEmployee::setWorkEligibility(const QList<OAIStagedEmployee_workEligibility_inner> &work_eligibility) {
    m_work_eligibility = work_eligibility;
    m_work_eligibility_isSet = true;
}

bool OAIStagedEmployee::is_work_eligibility_Set() const{
    return m_work_eligibility_isSet;
}

bool OAIStagedEmployee::is_work_eligibility_Valid() const{
    return m_work_eligibility_isValid;
}

bool OAIStagedEmployee::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_direct_deposit.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_benefit_setup.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_birth_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_boolean_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_date_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_drop_down_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_number_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_text_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_department_position.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_disability_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ethnicity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_federal_tax.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fitw_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_futa_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_address.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_employee943_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_smoker_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_local_tax.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_main_direct_deposit.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_marital_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_med_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_non_primary_state_tax.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_preferred_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_pay_rate.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_state_tax.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_prior_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_salutation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sitw_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ss_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_suffix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sui_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sui_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_distribution_code1099_r_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_form_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_veteran_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_web_time.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_address.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_eligibility.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStagedEmployee::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
