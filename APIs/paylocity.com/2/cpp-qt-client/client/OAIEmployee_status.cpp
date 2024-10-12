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

#include "OAIEmployee_status.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmployee_status::OAIEmployee_status(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmployee_status::OAIEmployee_status() {
    this->initializeModel();
}

OAIEmployee_status::~OAIEmployee_status() {}

void OAIEmployee_status::initializeModel() {

    m_adjusted_seniority_date_isSet = false;
    m_adjusted_seniority_date_isValid = false;

    m_change_reason_isSet = false;
    m_change_reason_isValid = false;

    m_effective_date_isSet = false;
    m_effective_date_isValid = false;

    m_employee_status_isSet = false;
    m_employee_status_isValid = false;

    m_hire_date_isSet = false;
    m_hire_date_isValid = false;

    m_is_eligible_for_rehire_isSet = false;
    m_is_eligible_for_rehire_isValid = false;

    m_re_hire_date_isSet = false;
    m_re_hire_date_isValid = false;

    m_status_type_isSet = false;
    m_status_type_isValid = false;

    m_termination_date_isSet = false;
    m_termination_date_isValid = false;
}

void OAIEmployee_status::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmployee_status::fromJsonObject(QJsonObject json) {

    m_adjusted_seniority_date_isValid = ::OpenAPI::fromJsonValue(m_adjusted_seniority_date, json[QString("adjustedSeniorityDate")]);
    m_adjusted_seniority_date_isSet = !json[QString("adjustedSeniorityDate")].isNull() && m_adjusted_seniority_date_isValid;

    m_change_reason_isValid = ::OpenAPI::fromJsonValue(m_change_reason, json[QString("changeReason")]);
    m_change_reason_isSet = !json[QString("changeReason")].isNull() && m_change_reason_isValid;

    m_effective_date_isValid = ::OpenAPI::fromJsonValue(m_effective_date, json[QString("effectiveDate")]);
    m_effective_date_isSet = !json[QString("effectiveDate")].isNull() && m_effective_date_isValid;

    m_employee_status_isValid = ::OpenAPI::fromJsonValue(m_employee_status, json[QString("employeeStatus")]);
    m_employee_status_isSet = !json[QString("employeeStatus")].isNull() && m_employee_status_isValid;

    m_hire_date_isValid = ::OpenAPI::fromJsonValue(m_hire_date, json[QString("hireDate")]);
    m_hire_date_isSet = !json[QString("hireDate")].isNull() && m_hire_date_isValid;

    m_is_eligible_for_rehire_isValid = ::OpenAPI::fromJsonValue(m_is_eligible_for_rehire, json[QString("isEligibleForRehire")]);
    m_is_eligible_for_rehire_isSet = !json[QString("isEligibleForRehire")].isNull() && m_is_eligible_for_rehire_isValid;

    m_re_hire_date_isValid = ::OpenAPI::fromJsonValue(m_re_hire_date, json[QString("reHireDate")]);
    m_re_hire_date_isSet = !json[QString("reHireDate")].isNull() && m_re_hire_date_isValid;

    m_status_type_isValid = ::OpenAPI::fromJsonValue(m_status_type, json[QString("statusType")]);
    m_status_type_isSet = !json[QString("statusType")].isNull() && m_status_type_isValid;

    m_termination_date_isValid = ::OpenAPI::fromJsonValue(m_termination_date, json[QString("terminationDate")]);
    m_termination_date_isSet = !json[QString("terminationDate")].isNull() && m_termination_date_isValid;
}

QString OAIEmployee_status::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmployee_status::asJsonObject() const {
    QJsonObject obj;
    if (m_adjusted_seniority_date_isSet) {
        obj.insert(QString("adjustedSeniorityDate"), ::OpenAPI::toJsonValue(m_adjusted_seniority_date));
    }
    if (m_change_reason_isSet) {
        obj.insert(QString("changeReason"), ::OpenAPI::toJsonValue(m_change_reason));
    }
    if (m_effective_date_isSet) {
        obj.insert(QString("effectiveDate"), ::OpenAPI::toJsonValue(m_effective_date));
    }
    if (m_employee_status_isSet) {
        obj.insert(QString("employeeStatus"), ::OpenAPI::toJsonValue(m_employee_status));
    }
    if (m_hire_date_isSet) {
        obj.insert(QString("hireDate"), ::OpenAPI::toJsonValue(m_hire_date));
    }
    if (m_is_eligible_for_rehire_isSet) {
        obj.insert(QString("isEligibleForRehire"), ::OpenAPI::toJsonValue(m_is_eligible_for_rehire));
    }
    if (m_re_hire_date_isSet) {
        obj.insert(QString("reHireDate"), ::OpenAPI::toJsonValue(m_re_hire_date));
    }
    if (m_status_type_isSet) {
        obj.insert(QString("statusType"), ::OpenAPI::toJsonValue(m_status_type));
    }
    if (m_termination_date_isSet) {
        obj.insert(QString("terminationDate"), ::OpenAPI::toJsonValue(m_termination_date));
    }
    return obj;
}

QString OAIEmployee_status::getAdjustedSeniorityDate() const {
    return m_adjusted_seniority_date;
}
void OAIEmployee_status::setAdjustedSeniorityDate(const QString &adjusted_seniority_date) {
    m_adjusted_seniority_date = adjusted_seniority_date;
    m_adjusted_seniority_date_isSet = true;
}

bool OAIEmployee_status::is_adjusted_seniority_date_Set() const{
    return m_adjusted_seniority_date_isSet;
}

bool OAIEmployee_status::is_adjusted_seniority_date_Valid() const{
    return m_adjusted_seniority_date_isValid;
}

QString OAIEmployee_status::getChangeReason() const {
    return m_change_reason;
}
void OAIEmployee_status::setChangeReason(const QString &change_reason) {
    m_change_reason = change_reason;
    m_change_reason_isSet = true;
}

bool OAIEmployee_status::is_change_reason_Set() const{
    return m_change_reason_isSet;
}

bool OAIEmployee_status::is_change_reason_Valid() const{
    return m_change_reason_isValid;
}

QString OAIEmployee_status::getEffectiveDate() const {
    return m_effective_date;
}
void OAIEmployee_status::setEffectiveDate(const QString &effective_date) {
    m_effective_date = effective_date;
    m_effective_date_isSet = true;
}

bool OAIEmployee_status::is_effective_date_Set() const{
    return m_effective_date_isSet;
}

bool OAIEmployee_status::is_effective_date_Valid() const{
    return m_effective_date_isValid;
}

QString OAIEmployee_status::getEmployeeStatus() const {
    return m_employee_status;
}
void OAIEmployee_status::setEmployeeStatus(const QString &employee_status) {
    m_employee_status = employee_status;
    m_employee_status_isSet = true;
}

bool OAIEmployee_status::is_employee_status_Set() const{
    return m_employee_status_isSet;
}

bool OAIEmployee_status::is_employee_status_Valid() const{
    return m_employee_status_isValid;
}

QString OAIEmployee_status::getHireDate() const {
    return m_hire_date;
}
void OAIEmployee_status::setHireDate(const QString &hire_date) {
    m_hire_date = hire_date;
    m_hire_date_isSet = true;
}

bool OAIEmployee_status::is_hire_date_Set() const{
    return m_hire_date_isSet;
}

bool OAIEmployee_status::is_hire_date_Valid() const{
    return m_hire_date_isValid;
}

bool OAIEmployee_status::isIsEligibleForRehire() const {
    return m_is_eligible_for_rehire;
}
void OAIEmployee_status::setIsEligibleForRehire(const bool &is_eligible_for_rehire) {
    m_is_eligible_for_rehire = is_eligible_for_rehire;
    m_is_eligible_for_rehire_isSet = true;
}

bool OAIEmployee_status::is_is_eligible_for_rehire_Set() const{
    return m_is_eligible_for_rehire_isSet;
}

bool OAIEmployee_status::is_is_eligible_for_rehire_Valid() const{
    return m_is_eligible_for_rehire_isValid;
}

QString OAIEmployee_status::getReHireDate() const {
    return m_re_hire_date;
}
void OAIEmployee_status::setReHireDate(const QString &re_hire_date) {
    m_re_hire_date = re_hire_date;
    m_re_hire_date_isSet = true;
}

bool OAIEmployee_status::is_re_hire_date_Set() const{
    return m_re_hire_date_isSet;
}

bool OAIEmployee_status::is_re_hire_date_Valid() const{
    return m_re_hire_date_isValid;
}

QString OAIEmployee_status::getStatusType() const {
    return m_status_type;
}
void OAIEmployee_status::setStatusType(const QString &status_type) {
    m_status_type = status_type;
    m_status_type_isSet = true;
}

bool OAIEmployee_status::is_status_type_Set() const{
    return m_status_type_isSet;
}

bool OAIEmployee_status::is_status_type_Valid() const{
    return m_status_type_isValid;
}

QString OAIEmployee_status::getTerminationDate() const {
    return m_termination_date;
}
void OAIEmployee_status::setTerminationDate(const QString &termination_date) {
    m_termination_date = termination_date;
    m_termination_date_isSet = true;
}

bool OAIEmployee_status::is_termination_date_Set() const{
    return m_termination_date_isSet;
}

bool OAIEmployee_status::is_termination_date_Valid() const{
    return m_termination_date_isValid;
}

bool OAIEmployee_status::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_adjusted_seniority_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_change_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_effective_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employee_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hire_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_eligible_for_rehire_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_re_hire_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_termination_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEmployee_status::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
