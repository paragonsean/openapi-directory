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

#include "OAIStagedEmployee_departmentPosition_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStagedEmployee_departmentPosition_inner::OAIStagedEmployee_departmentPosition_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStagedEmployee_departmentPosition_inner::OAIStagedEmployee_departmentPosition_inner() {
    this->initializeModel();
}

OAIStagedEmployee_departmentPosition_inner::~OAIStagedEmployee_departmentPosition_inner() {}

void OAIStagedEmployee_departmentPosition_inner::initializeModel() {

    m_change_reason_isSet = false;
    m_change_reason_isValid = false;

    m_clock_badge_number_isSet = false;
    m_clock_badge_number_isValid = false;

    m_cost_center1_isSet = false;
    m_cost_center1_isValid = false;

    m_cost_center2_isSet = false;
    m_cost_center2_isValid = false;

    m_cost_center3_isSet = false;
    m_cost_center3_isValid = false;

    m_effective_date_isSet = false;
    m_effective_date_isValid = false;

    m_employee_type_isSet = false;
    m_employee_type_isValid = false;

    m_equal_employment_opportunity_class_isSet = false;
    m_equal_employment_opportunity_class_isValid = false;

    m_is_minimum_wage_exempt_isSet = false;
    m_is_minimum_wage_exempt_isValid = false;

    m_is_overtime_exempt_isSet = false;
    m_is_overtime_exempt_isValid = false;

    m_is_supervisor_reviewer_isSet = false;
    m_is_supervisor_reviewer_isValid = false;

    m_is_union_dues_collected_isSet = false;
    m_is_union_dues_collected_isValid = false;

    m_is_union_initiation_collected_isSet = false;
    m_is_union_initiation_collected_isValid = false;

    m_job_title_isSet = false;
    m_job_title_isValid = false;

    m_pay_group_isSet = false;
    m_pay_group_isValid = false;

    m_position_code_isSet = false;
    m_position_code_isValid = false;

    m_shift_isSet = false;
    m_shift_isValid = false;

    m_supervisor_company_number_isSet = false;
    m_supervisor_company_number_isValid = false;

    m_supervisor_employee_id_isSet = false;
    m_supervisor_employee_id_isValid = false;

    m_tipped_isSet = false;
    m_tipped_isValid = false;

    m_union_affiliation_date_isSet = false;
    m_union_affiliation_date_isValid = false;

    m_union_code_isSet = false;
    m_union_code_isValid = false;

    m_union_position_isSet = false;
    m_union_position_isValid = false;

    m_workers_compensation_isSet = false;
    m_workers_compensation_isValid = false;
}

void OAIStagedEmployee_departmentPosition_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStagedEmployee_departmentPosition_inner::fromJsonObject(QJsonObject json) {

    m_change_reason_isValid = ::OpenAPI::fromJsonValue(m_change_reason, json[QString("changeReason")]);
    m_change_reason_isSet = !json[QString("changeReason")].isNull() && m_change_reason_isValid;

    m_clock_badge_number_isValid = ::OpenAPI::fromJsonValue(m_clock_badge_number, json[QString("clockBadgeNumber")]);
    m_clock_badge_number_isSet = !json[QString("clockBadgeNumber")].isNull() && m_clock_badge_number_isValid;

    m_cost_center1_isValid = ::OpenAPI::fromJsonValue(m_cost_center1, json[QString("costCenter1")]);
    m_cost_center1_isSet = !json[QString("costCenter1")].isNull() && m_cost_center1_isValid;

    m_cost_center2_isValid = ::OpenAPI::fromJsonValue(m_cost_center2, json[QString("costCenter2")]);
    m_cost_center2_isSet = !json[QString("costCenter2")].isNull() && m_cost_center2_isValid;

    m_cost_center3_isValid = ::OpenAPI::fromJsonValue(m_cost_center3, json[QString("costCenter3")]);
    m_cost_center3_isSet = !json[QString("costCenter3")].isNull() && m_cost_center3_isValid;

    m_effective_date_isValid = ::OpenAPI::fromJsonValue(m_effective_date, json[QString("effectiveDate")]);
    m_effective_date_isSet = !json[QString("effectiveDate")].isNull() && m_effective_date_isValid;

    m_employee_type_isValid = ::OpenAPI::fromJsonValue(m_employee_type, json[QString("employeeType")]);
    m_employee_type_isSet = !json[QString("employeeType")].isNull() && m_employee_type_isValid;

    m_equal_employment_opportunity_class_isValid = ::OpenAPI::fromJsonValue(m_equal_employment_opportunity_class, json[QString("equalEmploymentOpportunityClass")]);
    m_equal_employment_opportunity_class_isSet = !json[QString("equalEmploymentOpportunityClass")].isNull() && m_equal_employment_opportunity_class_isValid;

    m_is_minimum_wage_exempt_isValid = ::OpenAPI::fromJsonValue(m_is_minimum_wage_exempt, json[QString("isMinimumWageExempt")]);
    m_is_minimum_wage_exempt_isSet = !json[QString("isMinimumWageExempt")].isNull() && m_is_minimum_wage_exempt_isValid;

    m_is_overtime_exempt_isValid = ::OpenAPI::fromJsonValue(m_is_overtime_exempt, json[QString("isOvertimeExempt")]);
    m_is_overtime_exempt_isSet = !json[QString("isOvertimeExempt")].isNull() && m_is_overtime_exempt_isValid;

    m_is_supervisor_reviewer_isValid = ::OpenAPI::fromJsonValue(m_is_supervisor_reviewer, json[QString("isSupervisorReviewer")]);
    m_is_supervisor_reviewer_isSet = !json[QString("isSupervisorReviewer")].isNull() && m_is_supervisor_reviewer_isValid;

    m_is_union_dues_collected_isValid = ::OpenAPI::fromJsonValue(m_is_union_dues_collected, json[QString("isUnionDuesCollected")]);
    m_is_union_dues_collected_isSet = !json[QString("isUnionDuesCollected")].isNull() && m_is_union_dues_collected_isValid;

    m_is_union_initiation_collected_isValid = ::OpenAPI::fromJsonValue(m_is_union_initiation_collected, json[QString("isUnionInitiationCollected")]);
    m_is_union_initiation_collected_isSet = !json[QString("isUnionInitiationCollected")].isNull() && m_is_union_initiation_collected_isValid;

    m_job_title_isValid = ::OpenAPI::fromJsonValue(m_job_title, json[QString("jobTitle")]);
    m_job_title_isSet = !json[QString("jobTitle")].isNull() && m_job_title_isValid;

    m_pay_group_isValid = ::OpenAPI::fromJsonValue(m_pay_group, json[QString("payGroup")]);
    m_pay_group_isSet = !json[QString("payGroup")].isNull() && m_pay_group_isValid;

    m_position_code_isValid = ::OpenAPI::fromJsonValue(m_position_code, json[QString("positionCode")]);
    m_position_code_isSet = !json[QString("positionCode")].isNull() && m_position_code_isValid;

    m_shift_isValid = ::OpenAPI::fromJsonValue(m_shift, json[QString("shift")]);
    m_shift_isSet = !json[QString("shift")].isNull() && m_shift_isValid;

    m_supervisor_company_number_isValid = ::OpenAPI::fromJsonValue(m_supervisor_company_number, json[QString("supervisorCompanyNumber")]);
    m_supervisor_company_number_isSet = !json[QString("supervisorCompanyNumber")].isNull() && m_supervisor_company_number_isValid;

    m_supervisor_employee_id_isValid = ::OpenAPI::fromJsonValue(m_supervisor_employee_id, json[QString("supervisorEmployeeId")]);
    m_supervisor_employee_id_isSet = !json[QString("supervisorEmployeeId")].isNull() && m_supervisor_employee_id_isValid;

    m_tipped_isValid = ::OpenAPI::fromJsonValue(m_tipped, json[QString("tipped")]);
    m_tipped_isSet = !json[QString("tipped")].isNull() && m_tipped_isValid;

    m_union_affiliation_date_isValid = ::OpenAPI::fromJsonValue(m_union_affiliation_date, json[QString("unionAffiliationDate")]);
    m_union_affiliation_date_isSet = !json[QString("unionAffiliationDate")].isNull() && m_union_affiliation_date_isValid;

    m_union_code_isValid = ::OpenAPI::fromJsonValue(m_union_code, json[QString("unionCode")]);
    m_union_code_isSet = !json[QString("unionCode")].isNull() && m_union_code_isValid;

    m_union_position_isValid = ::OpenAPI::fromJsonValue(m_union_position, json[QString("unionPosition")]);
    m_union_position_isSet = !json[QString("unionPosition")].isNull() && m_union_position_isValid;

    m_workers_compensation_isValid = ::OpenAPI::fromJsonValue(m_workers_compensation, json[QString("workersCompensation")]);
    m_workers_compensation_isSet = !json[QString("workersCompensation")].isNull() && m_workers_compensation_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStagedEmployee_departmentPosition_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_change_reason_isSet) {
        obj.insert(QString("changeReason"), ::OpenAPI::toJsonValue(m_change_reason));
    }
    if (m_clock_badge_number_isSet) {
        obj.insert(QString("clockBadgeNumber"), ::OpenAPI::toJsonValue(m_clock_badge_number));
    }
    if (m_cost_center1_isSet) {
        obj.insert(QString("costCenter1"), ::OpenAPI::toJsonValue(m_cost_center1));
    }
    if (m_cost_center2_isSet) {
        obj.insert(QString("costCenter2"), ::OpenAPI::toJsonValue(m_cost_center2));
    }
    if (m_cost_center3_isSet) {
        obj.insert(QString("costCenter3"), ::OpenAPI::toJsonValue(m_cost_center3));
    }
    if (m_effective_date_isSet) {
        obj.insert(QString("effectiveDate"), ::OpenAPI::toJsonValue(m_effective_date));
    }
    if (m_employee_type_isSet) {
        obj.insert(QString("employeeType"), ::OpenAPI::toJsonValue(m_employee_type));
    }
    if (m_equal_employment_opportunity_class_isSet) {
        obj.insert(QString("equalEmploymentOpportunityClass"), ::OpenAPI::toJsonValue(m_equal_employment_opportunity_class));
    }
    if (m_is_minimum_wage_exempt_isSet) {
        obj.insert(QString("isMinimumWageExempt"), ::OpenAPI::toJsonValue(m_is_minimum_wage_exempt));
    }
    if (m_is_overtime_exempt_isSet) {
        obj.insert(QString("isOvertimeExempt"), ::OpenAPI::toJsonValue(m_is_overtime_exempt));
    }
    if (m_is_supervisor_reviewer_isSet) {
        obj.insert(QString("isSupervisorReviewer"), ::OpenAPI::toJsonValue(m_is_supervisor_reviewer));
    }
    if (m_is_union_dues_collected_isSet) {
        obj.insert(QString("isUnionDuesCollected"), ::OpenAPI::toJsonValue(m_is_union_dues_collected));
    }
    if (m_is_union_initiation_collected_isSet) {
        obj.insert(QString("isUnionInitiationCollected"), ::OpenAPI::toJsonValue(m_is_union_initiation_collected));
    }
    if (m_job_title_isSet) {
        obj.insert(QString("jobTitle"), ::OpenAPI::toJsonValue(m_job_title));
    }
    if (m_pay_group_isSet) {
        obj.insert(QString("payGroup"), ::OpenAPI::toJsonValue(m_pay_group));
    }
    if (m_position_code_isSet) {
        obj.insert(QString("positionCode"), ::OpenAPI::toJsonValue(m_position_code));
    }
    if (m_shift_isSet) {
        obj.insert(QString("shift"), ::OpenAPI::toJsonValue(m_shift));
    }
    if (m_supervisor_company_number_isSet) {
        obj.insert(QString("supervisorCompanyNumber"), ::OpenAPI::toJsonValue(m_supervisor_company_number));
    }
    if (m_supervisor_employee_id_isSet) {
        obj.insert(QString("supervisorEmployeeId"), ::OpenAPI::toJsonValue(m_supervisor_employee_id));
    }
    if (m_tipped_isSet) {
        obj.insert(QString("tipped"), ::OpenAPI::toJsonValue(m_tipped));
    }
    if (m_union_affiliation_date_isSet) {
        obj.insert(QString("unionAffiliationDate"), ::OpenAPI::toJsonValue(m_union_affiliation_date));
    }
    if (m_union_code_isSet) {
        obj.insert(QString("unionCode"), ::OpenAPI::toJsonValue(m_union_code));
    }
    if (m_union_position_isSet) {
        obj.insert(QString("unionPosition"), ::OpenAPI::toJsonValue(m_union_position));
    }
    if (m_workers_compensation_isSet) {
        obj.insert(QString("workersCompensation"), ::OpenAPI::toJsonValue(m_workers_compensation));
    }
    return obj;
}

QString OAIStagedEmployee_departmentPosition_inner::getChangeReason() const {
    return m_change_reason;
}
void OAIStagedEmployee_departmentPosition_inner::setChangeReason(const QString &change_reason) {
    m_change_reason = change_reason;
    m_change_reason_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_change_reason_Set() const{
    return m_change_reason_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_change_reason_Valid() const{
    return m_change_reason_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getClockBadgeNumber() const {
    return m_clock_badge_number;
}
void OAIStagedEmployee_departmentPosition_inner::setClockBadgeNumber(const QString &clock_badge_number) {
    m_clock_badge_number = clock_badge_number;
    m_clock_badge_number_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_clock_badge_number_Set() const{
    return m_clock_badge_number_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_clock_badge_number_Valid() const{
    return m_clock_badge_number_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getCostCenter1() const {
    return m_cost_center1;
}
void OAIStagedEmployee_departmentPosition_inner::setCostCenter1(const QString &cost_center1) {
    m_cost_center1 = cost_center1;
    m_cost_center1_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_cost_center1_Set() const{
    return m_cost_center1_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_cost_center1_Valid() const{
    return m_cost_center1_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getCostCenter2() const {
    return m_cost_center2;
}
void OAIStagedEmployee_departmentPosition_inner::setCostCenter2(const QString &cost_center2) {
    m_cost_center2 = cost_center2;
    m_cost_center2_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_cost_center2_Set() const{
    return m_cost_center2_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_cost_center2_Valid() const{
    return m_cost_center2_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getCostCenter3() const {
    return m_cost_center3;
}
void OAIStagedEmployee_departmentPosition_inner::setCostCenter3(const QString &cost_center3) {
    m_cost_center3 = cost_center3;
    m_cost_center3_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_cost_center3_Set() const{
    return m_cost_center3_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_cost_center3_Valid() const{
    return m_cost_center3_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getEffectiveDate() const {
    return m_effective_date;
}
void OAIStagedEmployee_departmentPosition_inner::setEffectiveDate(const QString &effective_date) {
    m_effective_date = effective_date;
    m_effective_date_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_effective_date_Set() const{
    return m_effective_date_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_effective_date_Valid() const{
    return m_effective_date_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getEmployeeType() const {
    return m_employee_type;
}
void OAIStagedEmployee_departmentPosition_inner::setEmployeeType(const QString &employee_type) {
    m_employee_type = employee_type;
    m_employee_type_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_employee_type_Set() const{
    return m_employee_type_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_employee_type_Valid() const{
    return m_employee_type_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getEqualEmploymentOpportunityClass() const {
    return m_equal_employment_opportunity_class;
}
void OAIStagedEmployee_departmentPosition_inner::setEqualEmploymentOpportunityClass(const QString &equal_employment_opportunity_class) {
    m_equal_employment_opportunity_class = equal_employment_opportunity_class;
    m_equal_employment_opportunity_class_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_equal_employment_opportunity_class_Set() const{
    return m_equal_employment_opportunity_class_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_equal_employment_opportunity_class_Valid() const{
    return m_equal_employment_opportunity_class_isValid;
}

bool OAIStagedEmployee_departmentPosition_inner::isIsMinimumWageExempt() const {
    return m_is_minimum_wage_exempt;
}
void OAIStagedEmployee_departmentPosition_inner::setIsMinimumWageExempt(const bool &is_minimum_wage_exempt) {
    m_is_minimum_wage_exempt = is_minimum_wage_exempt;
    m_is_minimum_wage_exempt_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_minimum_wage_exempt_Set() const{
    return m_is_minimum_wage_exempt_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_minimum_wage_exempt_Valid() const{
    return m_is_minimum_wage_exempt_isValid;
}

bool OAIStagedEmployee_departmentPosition_inner::isIsOvertimeExempt() const {
    return m_is_overtime_exempt;
}
void OAIStagedEmployee_departmentPosition_inner::setIsOvertimeExempt(const bool &is_overtime_exempt) {
    m_is_overtime_exempt = is_overtime_exempt;
    m_is_overtime_exempt_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_overtime_exempt_Set() const{
    return m_is_overtime_exempt_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_overtime_exempt_Valid() const{
    return m_is_overtime_exempt_isValid;
}

bool OAIStagedEmployee_departmentPosition_inner::isIsSupervisorReviewer() const {
    return m_is_supervisor_reviewer;
}
void OAIStagedEmployee_departmentPosition_inner::setIsSupervisorReviewer(const bool &is_supervisor_reviewer) {
    m_is_supervisor_reviewer = is_supervisor_reviewer;
    m_is_supervisor_reviewer_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_supervisor_reviewer_Set() const{
    return m_is_supervisor_reviewer_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_supervisor_reviewer_Valid() const{
    return m_is_supervisor_reviewer_isValid;
}

bool OAIStagedEmployee_departmentPosition_inner::isIsUnionDuesCollected() const {
    return m_is_union_dues_collected;
}
void OAIStagedEmployee_departmentPosition_inner::setIsUnionDuesCollected(const bool &is_union_dues_collected) {
    m_is_union_dues_collected = is_union_dues_collected;
    m_is_union_dues_collected_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_union_dues_collected_Set() const{
    return m_is_union_dues_collected_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_union_dues_collected_Valid() const{
    return m_is_union_dues_collected_isValid;
}

bool OAIStagedEmployee_departmentPosition_inner::isIsUnionInitiationCollected() const {
    return m_is_union_initiation_collected;
}
void OAIStagedEmployee_departmentPosition_inner::setIsUnionInitiationCollected(const bool &is_union_initiation_collected) {
    m_is_union_initiation_collected = is_union_initiation_collected;
    m_is_union_initiation_collected_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_union_initiation_collected_Set() const{
    return m_is_union_initiation_collected_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_is_union_initiation_collected_Valid() const{
    return m_is_union_initiation_collected_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getJobTitle() const {
    return m_job_title;
}
void OAIStagedEmployee_departmentPosition_inner::setJobTitle(const QString &job_title) {
    m_job_title = job_title;
    m_job_title_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_job_title_Set() const{
    return m_job_title_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_job_title_Valid() const{
    return m_job_title_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getPayGroup() const {
    return m_pay_group;
}
void OAIStagedEmployee_departmentPosition_inner::setPayGroup(const QString &pay_group) {
    m_pay_group = pay_group;
    m_pay_group_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_pay_group_Set() const{
    return m_pay_group_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_pay_group_Valid() const{
    return m_pay_group_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getPositionCode() const {
    return m_position_code;
}
void OAIStagedEmployee_departmentPosition_inner::setPositionCode(const QString &position_code) {
    m_position_code = position_code;
    m_position_code_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_position_code_Set() const{
    return m_position_code_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_position_code_Valid() const{
    return m_position_code_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getShift() const {
    return m_shift;
}
void OAIStagedEmployee_departmentPosition_inner::setShift(const QString &shift) {
    m_shift = shift;
    m_shift_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_shift_Set() const{
    return m_shift_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_shift_Valid() const{
    return m_shift_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getSupervisorCompanyNumber() const {
    return m_supervisor_company_number;
}
void OAIStagedEmployee_departmentPosition_inner::setSupervisorCompanyNumber(const QString &supervisor_company_number) {
    m_supervisor_company_number = supervisor_company_number;
    m_supervisor_company_number_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_supervisor_company_number_Set() const{
    return m_supervisor_company_number_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_supervisor_company_number_Valid() const{
    return m_supervisor_company_number_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getSupervisorEmployeeId() const {
    return m_supervisor_employee_id;
}
void OAIStagedEmployee_departmentPosition_inner::setSupervisorEmployeeId(const QString &supervisor_employee_id) {
    m_supervisor_employee_id = supervisor_employee_id;
    m_supervisor_employee_id_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_supervisor_employee_id_Set() const{
    return m_supervisor_employee_id_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_supervisor_employee_id_Valid() const{
    return m_supervisor_employee_id_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getTipped() const {
    return m_tipped;
}
void OAIStagedEmployee_departmentPosition_inner::setTipped(const QString &tipped) {
    m_tipped = tipped;
    m_tipped_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_tipped_Set() const{
    return m_tipped_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_tipped_Valid() const{
    return m_tipped_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getUnionAffiliationDate() const {
    return m_union_affiliation_date;
}
void OAIStagedEmployee_departmentPosition_inner::setUnionAffiliationDate(const QString &union_affiliation_date) {
    m_union_affiliation_date = union_affiliation_date;
    m_union_affiliation_date_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_union_affiliation_date_Set() const{
    return m_union_affiliation_date_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_union_affiliation_date_Valid() const{
    return m_union_affiliation_date_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getUnionCode() const {
    return m_union_code;
}
void OAIStagedEmployee_departmentPosition_inner::setUnionCode(const QString &union_code) {
    m_union_code = union_code;
    m_union_code_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_union_code_Set() const{
    return m_union_code_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_union_code_Valid() const{
    return m_union_code_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getUnionPosition() const {
    return m_union_position;
}
void OAIStagedEmployee_departmentPosition_inner::setUnionPosition(const QString &union_position) {
    m_union_position = union_position;
    m_union_position_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_union_position_Set() const{
    return m_union_position_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_union_position_Valid() const{
    return m_union_position_isValid;
}

QString OAIStagedEmployee_departmentPosition_inner::getWorkersCompensation() const {
    return m_workers_compensation;
}
void OAIStagedEmployee_departmentPosition_inner::setWorkersCompensation(const QString &workers_compensation) {
    m_workers_compensation = workers_compensation;
    m_workers_compensation_isSet = true;
}

bool OAIStagedEmployee_departmentPosition_inner::is_workers_compensation_Set() const{
    return m_workers_compensation_isSet;
}

bool OAIStagedEmployee_departmentPosition_inner::is_workers_compensation_Valid() const{
    return m_workers_compensation_isValid;
}

bool OAIStagedEmployee_departmentPosition_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_change_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_clock_badge_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_center1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_center2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_center3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_effective_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employee_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_equal_employment_opportunity_class_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_minimum_wage_exempt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_overtime_exempt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_supervisor_reviewer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_union_dues_collected_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_union_initiation_collected_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pay_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shift_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supervisor_company_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supervisor_employee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tipped_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_union_affiliation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_union_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_union_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_workers_compensation_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStagedEmployee_departmentPosition_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
