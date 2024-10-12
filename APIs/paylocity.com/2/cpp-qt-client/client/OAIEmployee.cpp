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

#include "OAIEmployee.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmployee::OAIEmployee(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmployee::OAIEmployee() {
    this->initializeModel();
}

OAIEmployee::~OAIEmployee() {}

void OAIEmployee::initializeModel() {

    m_additional_direct_deposit_isSet = false;
    m_additional_direct_deposit_isValid = false;

    m_additional_rate_isSet = false;
    m_additional_rate_isValid = false;

    m_benefit_setup_isSet = false;
    m_benefit_setup_isValid = false;

    m_birth_date_isSet = false;
    m_birth_date_isValid = false;

    m_co_emp_code_isSet = false;
    m_co_emp_code_isValid = false;

    m_company_fein_isSet = false;
    m_company_fein_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

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

    m_emergency_contacts_isSet = false;
    m_emergency_contacts_isValid = false;

    m_employee_id_isSet = false;
    m_employee_id_isValid = false;

    m_ethnicity_isSet = false;
    m_ethnicity_isValid = false;

    m_federal_tax_isSet = false;
    m_federal_tax_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_home_address_isSet = false;
    m_home_address_isValid = false;

    m_is_highly_compensated_isSet = false;
    m_is_highly_compensated_isValid = false;

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

    m_middle_name_isSet = false;
    m_middle_name_isValid = false;

    m_non_primary_state_tax_isSet = false;
    m_non_primary_state_tax_isValid = false;

    m_owner_percent_isSet = false;
    m_owner_percent_isValid = false;

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

    m_ssn_isSet = false;
    m_ssn_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_suffix_isSet = false;
    m_suffix_isValid = false;

    m_tax_setup_isSet = false;
    m_tax_setup_isValid = false;

    m_veteran_description_isSet = false;
    m_veteran_description_isValid = false;

    m_web_time_isSet = false;
    m_web_time_isValid = false;

    m_work_address_isSet = false;
    m_work_address_isValid = false;

    m_work_eligibility_isSet = false;
    m_work_eligibility_isValid = false;
}

void OAIEmployee::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmployee::fromJsonObject(QJsonObject json) {

    m_additional_direct_deposit_isValid = ::OpenAPI::fromJsonValue(m_additional_direct_deposit, json[QString("additionalDirectDeposit")]);
    m_additional_direct_deposit_isSet = !json[QString("additionalDirectDeposit")].isNull() && m_additional_direct_deposit_isValid;

    m_additional_rate_isValid = ::OpenAPI::fromJsonValue(m_additional_rate, json[QString("additionalRate")]);
    m_additional_rate_isSet = !json[QString("additionalRate")].isNull() && m_additional_rate_isValid;

    m_benefit_setup_isValid = ::OpenAPI::fromJsonValue(m_benefit_setup, json[QString("benefitSetup")]);
    m_benefit_setup_isSet = !json[QString("benefitSetup")].isNull() && m_benefit_setup_isValid;

    m_birth_date_isValid = ::OpenAPI::fromJsonValue(m_birth_date, json[QString("birthDate")]);
    m_birth_date_isSet = !json[QString("birthDate")].isNull() && m_birth_date_isValid;

    m_co_emp_code_isValid = ::OpenAPI::fromJsonValue(m_co_emp_code, json[QString("coEmpCode")]);
    m_co_emp_code_isSet = !json[QString("coEmpCode")].isNull() && m_co_emp_code_isValid;

    m_company_fein_isValid = ::OpenAPI::fromJsonValue(m_company_fein, json[QString("companyFEIN")]);
    m_company_fein_isSet = !json[QString("companyFEIN")].isNull() && m_company_fein_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("companyName")]);
    m_company_name_isSet = !json[QString("companyName")].isNull() && m_company_name_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

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

    m_emergency_contacts_isValid = ::OpenAPI::fromJsonValue(m_emergency_contacts, json[QString("emergencyContacts")]);
    m_emergency_contacts_isSet = !json[QString("emergencyContacts")].isNull() && m_emergency_contacts_isValid;

    m_employee_id_isValid = ::OpenAPI::fromJsonValue(m_employee_id, json[QString("employeeId")]);
    m_employee_id_isSet = !json[QString("employeeId")].isNull() && m_employee_id_isValid;

    m_ethnicity_isValid = ::OpenAPI::fromJsonValue(m_ethnicity, json[QString("ethnicity")]);
    m_ethnicity_isSet = !json[QString("ethnicity")].isNull() && m_ethnicity_isValid;

    m_federal_tax_isValid = ::OpenAPI::fromJsonValue(m_federal_tax, json[QString("federalTax")]);
    m_federal_tax_isSet = !json[QString("federalTax")].isNull() && m_federal_tax_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_home_address_isValid = ::OpenAPI::fromJsonValue(m_home_address, json[QString("homeAddress")]);
    m_home_address_isSet = !json[QString("homeAddress")].isNull() && m_home_address_isValid;

    m_is_highly_compensated_isValid = ::OpenAPI::fromJsonValue(m_is_highly_compensated, json[QString("isHighlyCompensated")]);
    m_is_highly_compensated_isSet = !json[QString("isHighlyCompensated")].isNull() && m_is_highly_compensated_isValid;

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

    m_middle_name_isValid = ::OpenAPI::fromJsonValue(m_middle_name, json[QString("middleName")]);
    m_middle_name_isSet = !json[QString("middleName")].isNull() && m_middle_name_isValid;

    m_non_primary_state_tax_isValid = ::OpenAPI::fromJsonValue(m_non_primary_state_tax, json[QString("nonPrimaryStateTax")]);
    m_non_primary_state_tax_isSet = !json[QString("nonPrimaryStateTax")].isNull() && m_non_primary_state_tax_isValid;

    m_owner_percent_isValid = ::OpenAPI::fromJsonValue(m_owner_percent, json[QString("ownerPercent")]);
    m_owner_percent_isSet = !json[QString("ownerPercent")].isNull() && m_owner_percent_isValid;

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

    m_ssn_isValid = ::OpenAPI::fromJsonValue(m_ssn, json[QString("ssn")]);
    m_ssn_isSet = !json[QString("ssn")].isNull() && m_ssn_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_suffix_isValid = ::OpenAPI::fromJsonValue(m_suffix, json[QString("suffix")]);
    m_suffix_isSet = !json[QString("suffix")].isNull() && m_suffix_isValid;

    m_tax_setup_isValid = ::OpenAPI::fromJsonValue(m_tax_setup, json[QString("taxSetup")]);
    m_tax_setup_isSet = !json[QString("taxSetup")].isNull() && m_tax_setup_isValid;

    m_veteran_description_isValid = ::OpenAPI::fromJsonValue(m_veteran_description, json[QString("veteranDescription")]);
    m_veteran_description_isSet = !json[QString("veteranDescription")].isNull() && m_veteran_description_isValid;

    m_web_time_isValid = ::OpenAPI::fromJsonValue(m_web_time, json[QString("webTime")]);
    m_web_time_isSet = !json[QString("webTime")].isNull() && m_web_time_isValid;

    m_work_address_isValid = ::OpenAPI::fromJsonValue(m_work_address, json[QString("workAddress")]);
    m_work_address_isSet = !json[QString("workAddress")].isNull() && m_work_address_isValid;

    m_work_eligibility_isValid = ::OpenAPI::fromJsonValue(m_work_eligibility, json[QString("workEligibility")]);
    m_work_eligibility_isSet = !json[QString("workEligibility")].isNull() && m_work_eligibility_isValid;
}

QString OAIEmployee::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmployee::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_direct_deposit.size() > 0) {
        obj.insert(QString("additionalDirectDeposit"), ::OpenAPI::toJsonValue(m_additional_direct_deposit));
    }
    if (m_additional_rate.size() > 0) {
        obj.insert(QString("additionalRate"), ::OpenAPI::toJsonValue(m_additional_rate));
    }
    if (m_benefit_setup.isSet()) {
        obj.insert(QString("benefitSetup"), ::OpenAPI::toJsonValue(m_benefit_setup));
    }
    if (m_birth_date_isSet) {
        obj.insert(QString("birthDate"), ::OpenAPI::toJsonValue(m_birth_date));
    }
    if (m_co_emp_code_isSet) {
        obj.insert(QString("coEmpCode"), ::OpenAPI::toJsonValue(m_co_emp_code));
    }
    if (m_company_fein_isSet) {
        obj.insert(QString("companyFEIN"), ::OpenAPI::toJsonValue(m_company_fein));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("companyName"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
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
    if (m_department_position.isSet()) {
        obj.insert(QString("departmentPosition"), ::OpenAPI::toJsonValue(m_department_position));
    }
    if (m_disability_description_isSet) {
        obj.insert(QString("disabilityDescription"), ::OpenAPI::toJsonValue(m_disability_description));
    }
    if (m_emergency_contacts.size() > 0) {
        obj.insert(QString("emergencyContacts"), ::OpenAPI::toJsonValue(m_emergency_contacts));
    }
    if (m_employee_id_isSet) {
        obj.insert(QString("employeeId"), ::OpenAPI::toJsonValue(m_employee_id));
    }
    if (m_ethnicity_isSet) {
        obj.insert(QString("ethnicity"), ::OpenAPI::toJsonValue(m_ethnicity));
    }
    if (m_federal_tax.isSet()) {
        obj.insert(QString("federalTax"), ::OpenAPI::toJsonValue(m_federal_tax));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_gender_isSet) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_home_address.isSet()) {
        obj.insert(QString("homeAddress"), ::OpenAPI::toJsonValue(m_home_address));
    }
    if (m_is_highly_compensated_isSet) {
        obj.insert(QString("isHighlyCompensated"), ::OpenAPI::toJsonValue(m_is_highly_compensated));
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
    if (m_main_direct_deposit.isSet()) {
        obj.insert(QString("mainDirectDeposit"), ::OpenAPI::toJsonValue(m_main_direct_deposit));
    }
    if (m_marital_status_isSet) {
        obj.insert(QString("maritalStatus"), ::OpenAPI::toJsonValue(m_marital_status));
    }
    if (m_middle_name_isSet) {
        obj.insert(QString("middleName"), ::OpenAPI::toJsonValue(m_middle_name));
    }
    if (m_non_primary_state_tax.isSet()) {
        obj.insert(QString("nonPrimaryStateTax"), ::OpenAPI::toJsonValue(m_non_primary_state_tax));
    }
    if (m_owner_percent_isSet) {
        obj.insert(QString("ownerPercent"), ::OpenAPI::toJsonValue(m_owner_percent));
    }
    if (m_preferred_name_isSet) {
        obj.insert(QString("preferredName"), ::OpenAPI::toJsonValue(m_preferred_name));
    }
    if (m_primary_pay_rate.isSet()) {
        obj.insert(QString("primaryPayRate"), ::OpenAPI::toJsonValue(m_primary_pay_rate));
    }
    if (m_primary_state_tax.isSet()) {
        obj.insert(QString("primaryStateTax"), ::OpenAPI::toJsonValue(m_primary_state_tax));
    }
    if (m_prior_last_name_isSet) {
        obj.insert(QString("priorLastName"), ::OpenAPI::toJsonValue(m_prior_last_name));
    }
    if (m_salutation_isSet) {
        obj.insert(QString("salutation"), ::OpenAPI::toJsonValue(m_salutation));
    }
    if (m_ssn_isSet) {
        obj.insert(QString("ssn"), ::OpenAPI::toJsonValue(m_ssn));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_suffix_isSet) {
        obj.insert(QString("suffix"), ::OpenAPI::toJsonValue(m_suffix));
    }
    if (m_tax_setup.isSet()) {
        obj.insert(QString("taxSetup"), ::OpenAPI::toJsonValue(m_tax_setup));
    }
    if (m_veteran_description_isSet) {
        obj.insert(QString("veteranDescription"), ::OpenAPI::toJsonValue(m_veteran_description));
    }
    if (m_web_time.isSet()) {
        obj.insert(QString("webTime"), ::OpenAPI::toJsonValue(m_web_time));
    }
    if (m_work_address.isSet()) {
        obj.insert(QString("workAddress"), ::OpenAPI::toJsonValue(m_work_address));
    }
    if (m_work_eligibility.isSet()) {
        obj.insert(QString("workEligibility"), ::OpenAPI::toJsonValue(m_work_eligibility));
    }
    return obj;
}

QList<OAIDirectDeposit_additionalDirectDeposit_inner> OAIEmployee::getAdditionalDirectDeposit() const {
    return m_additional_direct_deposit;
}
void OAIEmployee::setAdditionalDirectDeposit(const QList<OAIDirectDeposit_additionalDirectDeposit_inner> &additional_direct_deposit) {
    m_additional_direct_deposit = additional_direct_deposit;
    m_additional_direct_deposit_isSet = true;
}

bool OAIEmployee::is_additional_direct_deposit_Set() const{
    return m_additional_direct_deposit_isSet;
}

bool OAIEmployee::is_additional_direct_deposit_Valid() const{
    return m_additional_direct_deposit_isValid;
}

QList<OAIEmployee_additionalRate_inner> OAIEmployee::getAdditionalRate() const {
    return m_additional_rate;
}
void OAIEmployee::setAdditionalRate(const QList<OAIEmployee_additionalRate_inner> &additional_rate) {
    m_additional_rate = additional_rate;
    m_additional_rate_isSet = true;
}

bool OAIEmployee::is_additional_rate_Set() const{
    return m_additional_rate_isSet;
}

bool OAIEmployee::is_additional_rate_Valid() const{
    return m_additional_rate_isValid;
}

OAIEmployee_benefitSetup OAIEmployee::getBenefitSetup() const {
    return m_benefit_setup;
}
void OAIEmployee::setBenefitSetup(const OAIEmployee_benefitSetup &benefit_setup) {
    m_benefit_setup = benefit_setup;
    m_benefit_setup_isSet = true;
}

bool OAIEmployee::is_benefit_setup_Set() const{
    return m_benefit_setup_isSet;
}

bool OAIEmployee::is_benefit_setup_Valid() const{
    return m_benefit_setup_isValid;
}

QString OAIEmployee::getBirthDate() const {
    return m_birth_date;
}
void OAIEmployee::setBirthDate(const QString &birth_date) {
    m_birth_date = birth_date;
    m_birth_date_isSet = true;
}

bool OAIEmployee::is_birth_date_Set() const{
    return m_birth_date_isSet;
}

bool OAIEmployee::is_birth_date_Valid() const{
    return m_birth_date_isValid;
}

QString OAIEmployee::getCoEmpCode() const {
    return m_co_emp_code;
}
void OAIEmployee::setCoEmpCode(const QString &co_emp_code) {
    m_co_emp_code = co_emp_code;
    m_co_emp_code_isSet = true;
}

bool OAIEmployee::is_co_emp_code_Set() const{
    return m_co_emp_code_isSet;
}

bool OAIEmployee::is_co_emp_code_Valid() const{
    return m_co_emp_code_isValid;
}

QString OAIEmployee::getCompanyFein() const {
    return m_company_fein;
}
void OAIEmployee::setCompanyFein(const QString &company_fein) {
    m_company_fein = company_fein;
    m_company_fein_isSet = true;
}

bool OAIEmployee::is_company_fein_Set() const{
    return m_company_fein_isSet;
}

bool OAIEmployee::is_company_fein_Valid() const{
    return m_company_fein_isValid;
}

QString OAIEmployee::getCompanyName() const {
    return m_company_name;
}
void OAIEmployee::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAIEmployee::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAIEmployee::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QString OAIEmployee::getCurrency() const {
    return m_currency;
}
void OAIEmployee::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIEmployee::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIEmployee::is_currency_Valid() const{
    return m_currency_isValid;
}

QList<OAIEmployee_customBooleanFields_inner> OAIEmployee::getCustomBooleanFields() const {
    return m_custom_boolean_fields;
}
void OAIEmployee::setCustomBooleanFields(const QList<OAIEmployee_customBooleanFields_inner> &custom_boolean_fields) {
    m_custom_boolean_fields = custom_boolean_fields;
    m_custom_boolean_fields_isSet = true;
}

bool OAIEmployee::is_custom_boolean_fields_Set() const{
    return m_custom_boolean_fields_isSet;
}

bool OAIEmployee::is_custom_boolean_fields_Valid() const{
    return m_custom_boolean_fields_isValid;
}

QList<OAIEmployee_customDateFields_inner> OAIEmployee::getCustomDateFields() const {
    return m_custom_date_fields;
}
void OAIEmployee::setCustomDateFields(const QList<OAIEmployee_customDateFields_inner> &custom_date_fields) {
    m_custom_date_fields = custom_date_fields;
    m_custom_date_fields_isSet = true;
}

bool OAIEmployee::is_custom_date_fields_Set() const{
    return m_custom_date_fields_isSet;
}

bool OAIEmployee::is_custom_date_fields_Valid() const{
    return m_custom_date_fields_isValid;
}

QList<OAIEmployee_customDropDownFields_inner> OAIEmployee::getCustomDropDownFields() const {
    return m_custom_drop_down_fields;
}
void OAIEmployee::setCustomDropDownFields(const QList<OAIEmployee_customDropDownFields_inner> &custom_drop_down_fields) {
    m_custom_drop_down_fields = custom_drop_down_fields;
    m_custom_drop_down_fields_isSet = true;
}

bool OAIEmployee::is_custom_drop_down_fields_Set() const{
    return m_custom_drop_down_fields_isSet;
}

bool OAIEmployee::is_custom_drop_down_fields_Valid() const{
    return m_custom_drop_down_fields_isValid;
}

QList<OAIEmployee_customNumberFields_inner> OAIEmployee::getCustomNumberFields() const {
    return m_custom_number_fields;
}
void OAIEmployee::setCustomNumberFields(const QList<OAIEmployee_customNumberFields_inner> &custom_number_fields) {
    m_custom_number_fields = custom_number_fields;
    m_custom_number_fields_isSet = true;
}

bool OAIEmployee::is_custom_number_fields_Set() const{
    return m_custom_number_fields_isSet;
}

bool OAIEmployee::is_custom_number_fields_Valid() const{
    return m_custom_number_fields_isValid;
}

QList<OAIEmployee_customTextFields_inner> OAIEmployee::getCustomTextFields() const {
    return m_custom_text_fields;
}
void OAIEmployee::setCustomTextFields(const QList<OAIEmployee_customTextFields_inner> &custom_text_fields) {
    m_custom_text_fields = custom_text_fields;
    m_custom_text_fields_isSet = true;
}

bool OAIEmployee::is_custom_text_fields_Set() const{
    return m_custom_text_fields_isSet;
}

bool OAIEmployee::is_custom_text_fields_Valid() const{
    return m_custom_text_fields_isValid;
}

OAIEmployee_departmentPosition OAIEmployee::getDepartmentPosition() const {
    return m_department_position;
}
void OAIEmployee::setDepartmentPosition(const OAIEmployee_departmentPosition &department_position) {
    m_department_position = department_position;
    m_department_position_isSet = true;
}

bool OAIEmployee::is_department_position_Set() const{
    return m_department_position_isSet;
}

bool OAIEmployee::is_department_position_Valid() const{
    return m_department_position_isValid;
}

QString OAIEmployee::getDisabilityDescription() const {
    return m_disability_description;
}
void OAIEmployee::setDisabilityDescription(const QString &disability_description) {
    m_disability_description = disability_description;
    m_disability_description_isSet = true;
}

bool OAIEmployee::is_disability_description_Set() const{
    return m_disability_description_isSet;
}

bool OAIEmployee::is_disability_description_Valid() const{
    return m_disability_description_isValid;
}

QList<OAIEmployee_emergencyContacts_inner> OAIEmployee::getEmergencyContacts() const {
    return m_emergency_contacts;
}
void OAIEmployee::setEmergencyContacts(const QList<OAIEmployee_emergencyContacts_inner> &emergency_contacts) {
    m_emergency_contacts = emergency_contacts;
    m_emergency_contacts_isSet = true;
}

bool OAIEmployee::is_emergency_contacts_Set() const{
    return m_emergency_contacts_isSet;
}

bool OAIEmployee::is_emergency_contacts_Valid() const{
    return m_emergency_contacts_isValid;
}

QString OAIEmployee::getEmployeeId() const {
    return m_employee_id;
}
void OAIEmployee::setEmployeeId(const QString &employee_id) {
    m_employee_id = employee_id;
    m_employee_id_isSet = true;
}

bool OAIEmployee::is_employee_id_Set() const{
    return m_employee_id_isSet;
}

bool OAIEmployee::is_employee_id_Valid() const{
    return m_employee_id_isValid;
}

QString OAIEmployee::getEthnicity() const {
    return m_ethnicity;
}
void OAIEmployee::setEthnicity(const QString &ethnicity) {
    m_ethnicity = ethnicity;
    m_ethnicity_isSet = true;
}

bool OAIEmployee::is_ethnicity_Set() const{
    return m_ethnicity_isSet;
}

bool OAIEmployee::is_ethnicity_Valid() const{
    return m_ethnicity_isValid;
}

OAIEmployee_federalTax OAIEmployee::getFederalTax() const {
    return m_federal_tax;
}
void OAIEmployee::setFederalTax(const OAIEmployee_federalTax &federal_tax) {
    m_federal_tax = federal_tax;
    m_federal_tax_isSet = true;
}

bool OAIEmployee::is_federal_tax_Set() const{
    return m_federal_tax_isSet;
}

bool OAIEmployee::is_federal_tax_Valid() const{
    return m_federal_tax_isValid;
}

QString OAIEmployee::getFirstName() const {
    return m_first_name;
}
void OAIEmployee::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIEmployee::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIEmployee::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIEmployee::getGender() const {
    return m_gender;
}
void OAIEmployee::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIEmployee::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIEmployee::is_gender_Valid() const{
    return m_gender_isValid;
}

OAIEmployee_homeAddress OAIEmployee::getHomeAddress() const {
    return m_home_address;
}
void OAIEmployee::setHomeAddress(const OAIEmployee_homeAddress &home_address) {
    m_home_address = home_address;
    m_home_address_isSet = true;
}

bool OAIEmployee::is_home_address_Set() const{
    return m_home_address_isSet;
}

bool OAIEmployee::is_home_address_Valid() const{
    return m_home_address_isValid;
}

bool OAIEmployee::isIsHighlyCompensated() const {
    return m_is_highly_compensated;
}
void OAIEmployee::setIsHighlyCompensated(const bool &is_highly_compensated) {
    m_is_highly_compensated = is_highly_compensated;
    m_is_highly_compensated_isSet = true;
}

bool OAIEmployee::is_is_highly_compensated_Set() const{
    return m_is_highly_compensated_isSet;
}

bool OAIEmployee::is_is_highly_compensated_Valid() const{
    return m_is_highly_compensated_isValid;
}

bool OAIEmployee::isIsSmoker() const {
    return m_is_smoker;
}
void OAIEmployee::setIsSmoker(const bool &is_smoker) {
    m_is_smoker = is_smoker;
    m_is_smoker_isSet = true;
}

bool OAIEmployee::is_is_smoker_Set() const{
    return m_is_smoker_isSet;
}

bool OAIEmployee::is_is_smoker_Valid() const{
    return m_is_smoker_isValid;
}

QString OAIEmployee::getLastName() const {
    return m_last_name;
}
void OAIEmployee::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIEmployee::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIEmployee::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QList<OAIEmployee_localTax_inner> OAIEmployee::getLocalTax() const {
    return m_local_tax;
}
void OAIEmployee::setLocalTax(const QList<OAIEmployee_localTax_inner> &local_tax) {
    m_local_tax = local_tax;
    m_local_tax_isSet = true;
}

bool OAIEmployee::is_local_tax_Set() const{
    return m_local_tax_isSet;
}

bool OAIEmployee::is_local_tax_Valid() const{
    return m_local_tax_isValid;
}

OAIEmployee_mainDirectDeposit OAIEmployee::getMainDirectDeposit() const {
    return m_main_direct_deposit;
}
void OAIEmployee::setMainDirectDeposit(const OAIEmployee_mainDirectDeposit &main_direct_deposit) {
    m_main_direct_deposit = main_direct_deposit;
    m_main_direct_deposit_isSet = true;
}

bool OAIEmployee::is_main_direct_deposit_Set() const{
    return m_main_direct_deposit_isSet;
}

bool OAIEmployee::is_main_direct_deposit_Valid() const{
    return m_main_direct_deposit_isValid;
}

QString OAIEmployee::getMaritalStatus() const {
    return m_marital_status;
}
void OAIEmployee::setMaritalStatus(const QString &marital_status) {
    m_marital_status = marital_status;
    m_marital_status_isSet = true;
}

bool OAIEmployee::is_marital_status_Set() const{
    return m_marital_status_isSet;
}

bool OAIEmployee::is_marital_status_Valid() const{
    return m_marital_status_isValid;
}

QString OAIEmployee::getMiddleName() const {
    return m_middle_name;
}
void OAIEmployee::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAIEmployee::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAIEmployee::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

OAIEmployee_nonPrimaryStateTax OAIEmployee::getNonPrimaryStateTax() const {
    return m_non_primary_state_tax;
}
void OAIEmployee::setNonPrimaryStateTax(const OAIEmployee_nonPrimaryStateTax &non_primary_state_tax) {
    m_non_primary_state_tax = non_primary_state_tax;
    m_non_primary_state_tax_isSet = true;
}

bool OAIEmployee::is_non_primary_state_tax_Set() const{
    return m_non_primary_state_tax_isSet;
}

bool OAIEmployee::is_non_primary_state_tax_Valid() const{
    return m_non_primary_state_tax_isValid;
}

double OAIEmployee::getOwnerPercent() const {
    return m_owner_percent;
}
void OAIEmployee::setOwnerPercent(const double &owner_percent) {
    m_owner_percent = owner_percent;
    m_owner_percent_isSet = true;
}

bool OAIEmployee::is_owner_percent_Set() const{
    return m_owner_percent_isSet;
}

bool OAIEmployee::is_owner_percent_Valid() const{
    return m_owner_percent_isValid;
}

QString OAIEmployee::getPreferredName() const {
    return m_preferred_name;
}
void OAIEmployee::setPreferredName(const QString &preferred_name) {
    m_preferred_name = preferred_name;
    m_preferred_name_isSet = true;
}

bool OAIEmployee::is_preferred_name_Set() const{
    return m_preferred_name_isSet;
}

bool OAIEmployee::is_preferred_name_Valid() const{
    return m_preferred_name_isValid;
}

OAIEmployee_primaryPayRate OAIEmployee::getPrimaryPayRate() const {
    return m_primary_pay_rate;
}
void OAIEmployee::setPrimaryPayRate(const OAIEmployee_primaryPayRate &primary_pay_rate) {
    m_primary_pay_rate = primary_pay_rate;
    m_primary_pay_rate_isSet = true;
}

bool OAIEmployee::is_primary_pay_rate_Set() const{
    return m_primary_pay_rate_isSet;
}

bool OAIEmployee::is_primary_pay_rate_Valid() const{
    return m_primary_pay_rate_isValid;
}

OAIEmployee_primaryStateTax OAIEmployee::getPrimaryStateTax() const {
    return m_primary_state_tax;
}
void OAIEmployee::setPrimaryStateTax(const OAIEmployee_primaryStateTax &primary_state_tax) {
    m_primary_state_tax = primary_state_tax;
    m_primary_state_tax_isSet = true;
}

bool OAIEmployee::is_primary_state_tax_Set() const{
    return m_primary_state_tax_isSet;
}

bool OAIEmployee::is_primary_state_tax_Valid() const{
    return m_primary_state_tax_isValid;
}

QString OAIEmployee::getPriorLastName() const {
    return m_prior_last_name;
}
void OAIEmployee::setPriorLastName(const QString &prior_last_name) {
    m_prior_last_name = prior_last_name;
    m_prior_last_name_isSet = true;
}

bool OAIEmployee::is_prior_last_name_Set() const{
    return m_prior_last_name_isSet;
}

bool OAIEmployee::is_prior_last_name_Valid() const{
    return m_prior_last_name_isValid;
}

QString OAIEmployee::getSalutation() const {
    return m_salutation;
}
void OAIEmployee::setSalutation(const QString &salutation) {
    m_salutation = salutation;
    m_salutation_isSet = true;
}

bool OAIEmployee::is_salutation_Set() const{
    return m_salutation_isSet;
}

bool OAIEmployee::is_salutation_Valid() const{
    return m_salutation_isValid;
}

QString OAIEmployee::getSsn() const {
    return m_ssn;
}
void OAIEmployee::setSsn(const QString &ssn) {
    m_ssn = ssn;
    m_ssn_isSet = true;
}

bool OAIEmployee::is_ssn_Set() const{
    return m_ssn_isSet;
}

bool OAIEmployee::is_ssn_Valid() const{
    return m_ssn_isValid;
}

OAIEmployee_status OAIEmployee::getStatus() const {
    return m_status;
}
void OAIEmployee::setStatus(const OAIEmployee_status &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIEmployee::is_status_Set() const{
    return m_status_isSet;
}

bool OAIEmployee::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIEmployee::getSuffix() const {
    return m_suffix;
}
void OAIEmployee::setSuffix(const QString &suffix) {
    m_suffix = suffix;
    m_suffix_isSet = true;
}

bool OAIEmployee::is_suffix_Set() const{
    return m_suffix_isSet;
}

bool OAIEmployee::is_suffix_Valid() const{
    return m_suffix_isValid;
}

OAIEmployee_taxSetup OAIEmployee::getTaxSetup() const {
    return m_tax_setup;
}
void OAIEmployee::setTaxSetup(const OAIEmployee_taxSetup &tax_setup) {
    m_tax_setup = tax_setup;
    m_tax_setup_isSet = true;
}

bool OAIEmployee::is_tax_setup_Set() const{
    return m_tax_setup_isSet;
}

bool OAIEmployee::is_tax_setup_Valid() const{
    return m_tax_setup_isValid;
}

QString OAIEmployee::getVeteranDescription() const {
    return m_veteran_description;
}
void OAIEmployee::setVeteranDescription(const QString &veteran_description) {
    m_veteran_description = veteran_description;
    m_veteran_description_isSet = true;
}

bool OAIEmployee::is_veteran_description_Set() const{
    return m_veteran_description_isSet;
}

bool OAIEmployee::is_veteran_description_Valid() const{
    return m_veteran_description_isValid;
}

OAIEmployee_webTime OAIEmployee::getWebTime() const {
    return m_web_time;
}
void OAIEmployee::setWebTime(const OAIEmployee_webTime &web_time) {
    m_web_time = web_time;
    m_web_time_isSet = true;
}

bool OAIEmployee::is_web_time_Set() const{
    return m_web_time_isSet;
}

bool OAIEmployee::is_web_time_Valid() const{
    return m_web_time_isValid;
}

OAIEmployee_workAddress OAIEmployee::getWorkAddress() const {
    return m_work_address;
}
void OAIEmployee::setWorkAddress(const OAIEmployee_workAddress &work_address) {
    m_work_address = work_address;
    m_work_address_isSet = true;
}

bool OAIEmployee::is_work_address_Set() const{
    return m_work_address_isSet;
}

bool OAIEmployee::is_work_address_Valid() const{
    return m_work_address_isValid;
}

OAIEmployee_workEligibility OAIEmployee::getWorkEligibility() const {
    return m_work_eligibility;
}
void OAIEmployee::setWorkEligibility(const OAIEmployee_workEligibility &work_eligibility) {
    m_work_eligibility = work_eligibility;
    m_work_eligibility_isSet = true;
}

bool OAIEmployee::is_work_eligibility_Set() const{
    return m_work_eligibility_isSet;
}

bool OAIEmployee::is_work_eligibility_Valid() const{
    return m_work_eligibility_isValid;
}

bool OAIEmployee::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_direct_deposit.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_additional_rate.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_benefit_setup.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_birth_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_co_emp_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_fein_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
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

        if (m_department_position.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_disability_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emergency_contacts.size() > 0) {
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

        if (m_federal_tax.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_highly_compensated_isSet) {
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

        if (m_main_direct_deposit.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_marital_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_non_primary_state_tax.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preferred_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_pay_rate.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_state_tax.isSet()) {
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

        if (m_ssn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_suffix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_setup.isSet()) {
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

        if (m_work_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_eligibility.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEmployee::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
