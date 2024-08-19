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

#include "OAIAdditionalRate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAdditionalRate::OAIAdditionalRate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAdditionalRate::OAIAdditionalRate() {
    this->initializeModel();
}

OAIAdditionalRate::~OAIAdditionalRate() {}

void OAIAdditionalRate::initializeModel() {

    m_change_reason_isSet = false;
    m_change_reason_isValid = false;

    m_cost_center1_isSet = false;
    m_cost_center1_isValid = false;

    m_cost_center2_isSet = false;
    m_cost_center2_isValid = false;

    m_cost_center3_isSet = false;
    m_cost_center3_isValid = false;

    m_effective_date_isSet = false;
    m_effective_date_isValid = false;

    m_end_check_date_isSet = false;
    m_end_check_date_isValid = false;

    m_job_isSet = false;
    m_job_isValid = false;

    m_rate_isSet = false;
    m_rate_isValid = false;

    m_rate_code_isSet = false;
    m_rate_code_isValid = false;

    m_rate_notes_isSet = false;
    m_rate_notes_isValid = false;

    m_rate_per_isSet = false;
    m_rate_per_isValid = false;

    m_shift_isSet = false;
    m_shift_isValid = false;
}

void OAIAdditionalRate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAdditionalRate::fromJsonObject(QJsonObject json) {

    m_change_reason_isValid = ::OpenAPI::fromJsonValue(m_change_reason, json[QString("changeReason")]);
    m_change_reason_isSet = !json[QString("changeReason")].isNull() && m_change_reason_isValid;

    m_cost_center1_isValid = ::OpenAPI::fromJsonValue(m_cost_center1, json[QString("costCenter1")]);
    m_cost_center1_isSet = !json[QString("costCenter1")].isNull() && m_cost_center1_isValid;

    m_cost_center2_isValid = ::OpenAPI::fromJsonValue(m_cost_center2, json[QString("costCenter2")]);
    m_cost_center2_isSet = !json[QString("costCenter2")].isNull() && m_cost_center2_isValid;

    m_cost_center3_isValid = ::OpenAPI::fromJsonValue(m_cost_center3, json[QString("costCenter3")]);
    m_cost_center3_isSet = !json[QString("costCenter3")].isNull() && m_cost_center3_isValid;

    m_effective_date_isValid = ::OpenAPI::fromJsonValue(m_effective_date, json[QString("effectiveDate")]);
    m_effective_date_isSet = !json[QString("effectiveDate")].isNull() && m_effective_date_isValid;

    m_end_check_date_isValid = ::OpenAPI::fromJsonValue(m_end_check_date, json[QString("endCheckDate")]);
    m_end_check_date_isSet = !json[QString("endCheckDate")].isNull() && m_end_check_date_isValid;

    m_job_isValid = ::OpenAPI::fromJsonValue(m_job, json[QString("job")]);
    m_job_isSet = !json[QString("job")].isNull() && m_job_isValid;

    m_rate_isValid = ::OpenAPI::fromJsonValue(m_rate, json[QString("rate")]);
    m_rate_isSet = !json[QString("rate")].isNull() && m_rate_isValid;

    m_rate_code_isValid = ::OpenAPI::fromJsonValue(m_rate_code, json[QString("rateCode")]);
    m_rate_code_isSet = !json[QString("rateCode")].isNull() && m_rate_code_isValid;

    m_rate_notes_isValid = ::OpenAPI::fromJsonValue(m_rate_notes, json[QString("rateNotes")]);
    m_rate_notes_isSet = !json[QString("rateNotes")].isNull() && m_rate_notes_isValid;

    m_rate_per_isValid = ::OpenAPI::fromJsonValue(m_rate_per, json[QString("ratePer")]);
    m_rate_per_isSet = !json[QString("ratePer")].isNull() && m_rate_per_isValid;

    m_shift_isValid = ::OpenAPI::fromJsonValue(m_shift, json[QString("shift")]);
    m_shift_isSet = !json[QString("shift")].isNull() && m_shift_isValid;
}

QString OAIAdditionalRate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAdditionalRate::asJsonObject() const {
    QJsonObject obj;
    if (m_change_reason_isSet) {
        obj.insert(QString("changeReason"), ::OpenAPI::toJsonValue(m_change_reason));
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
    if (m_end_check_date_isSet) {
        obj.insert(QString("endCheckDate"), ::OpenAPI::toJsonValue(m_end_check_date));
    }
    if (m_job_isSet) {
        obj.insert(QString("job"), ::OpenAPI::toJsonValue(m_job));
    }
    if (m_rate_isSet) {
        obj.insert(QString("rate"), ::OpenAPI::toJsonValue(m_rate));
    }
    if (m_rate_code_isSet) {
        obj.insert(QString("rateCode"), ::OpenAPI::toJsonValue(m_rate_code));
    }
    if (m_rate_notes_isSet) {
        obj.insert(QString("rateNotes"), ::OpenAPI::toJsonValue(m_rate_notes));
    }
    if (m_rate_per_isSet) {
        obj.insert(QString("ratePer"), ::OpenAPI::toJsonValue(m_rate_per));
    }
    if (m_shift_isSet) {
        obj.insert(QString("shift"), ::OpenAPI::toJsonValue(m_shift));
    }
    return obj;
}

QString OAIAdditionalRate::getChangeReason() const {
    return m_change_reason;
}
void OAIAdditionalRate::setChangeReason(const QString &change_reason) {
    m_change_reason = change_reason;
    m_change_reason_isSet = true;
}

bool OAIAdditionalRate::is_change_reason_Set() const{
    return m_change_reason_isSet;
}

bool OAIAdditionalRate::is_change_reason_Valid() const{
    return m_change_reason_isValid;
}

QString OAIAdditionalRate::getCostCenter1() const {
    return m_cost_center1;
}
void OAIAdditionalRate::setCostCenter1(const QString &cost_center1) {
    m_cost_center1 = cost_center1;
    m_cost_center1_isSet = true;
}

bool OAIAdditionalRate::is_cost_center1_Set() const{
    return m_cost_center1_isSet;
}

bool OAIAdditionalRate::is_cost_center1_Valid() const{
    return m_cost_center1_isValid;
}

QString OAIAdditionalRate::getCostCenter2() const {
    return m_cost_center2;
}
void OAIAdditionalRate::setCostCenter2(const QString &cost_center2) {
    m_cost_center2 = cost_center2;
    m_cost_center2_isSet = true;
}

bool OAIAdditionalRate::is_cost_center2_Set() const{
    return m_cost_center2_isSet;
}

bool OAIAdditionalRate::is_cost_center2_Valid() const{
    return m_cost_center2_isValid;
}

QString OAIAdditionalRate::getCostCenter3() const {
    return m_cost_center3;
}
void OAIAdditionalRate::setCostCenter3(const QString &cost_center3) {
    m_cost_center3 = cost_center3;
    m_cost_center3_isSet = true;
}

bool OAIAdditionalRate::is_cost_center3_Set() const{
    return m_cost_center3_isSet;
}

bool OAIAdditionalRate::is_cost_center3_Valid() const{
    return m_cost_center3_isValid;
}

QString OAIAdditionalRate::getEffectiveDate() const {
    return m_effective_date;
}
void OAIAdditionalRate::setEffectiveDate(const QString &effective_date) {
    m_effective_date = effective_date;
    m_effective_date_isSet = true;
}

bool OAIAdditionalRate::is_effective_date_Set() const{
    return m_effective_date_isSet;
}

bool OAIAdditionalRate::is_effective_date_Valid() const{
    return m_effective_date_isValid;
}

QString OAIAdditionalRate::getEndCheckDate() const {
    return m_end_check_date;
}
void OAIAdditionalRate::setEndCheckDate(const QString &end_check_date) {
    m_end_check_date = end_check_date;
    m_end_check_date_isSet = true;
}

bool OAIAdditionalRate::is_end_check_date_Set() const{
    return m_end_check_date_isSet;
}

bool OAIAdditionalRate::is_end_check_date_Valid() const{
    return m_end_check_date_isValid;
}

QString OAIAdditionalRate::getJob() const {
    return m_job;
}
void OAIAdditionalRate::setJob(const QString &job) {
    m_job = job;
    m_job_isSet = true;
}

bool OAIAdditionalRate::is_job_Set() const{
    return m_job_isSet;
}

bool OAIAdditionalRate::is_job_Valid() const{
    return m_job_isValid;
}

double OAIAdditionalRate::getRate() const {
    return m_rate;
}
void OAIAdditionalRate::setRate(const double &rate) {
    m_rate = rate;
    m_rate_isSet = true;
}

bool OAIAdditionalRate::is_rate_Set() const{
    return m_rate_isSet;
}

bool OAIAdditionalRate::is_rate_Valid() const{
    return m_rate_isValid;
}

QString OAIAdditionalRate::getRateCode() const {
    return m_rate_code;
}
void OAIAdditionalRate::setRateCode(const QString &rate_code) {
    m_rate_code = rate_code;
    m_rate_code_isSet = true;
}

bool OAIAdditionalRate::is_rate_code_Set() const{
    return m_rate_code_isSet;
}

bool OAIAdditionalRate::is_rate_code_Valid() const{
    return m_rate_code_isValid;
}

QString OAIAdditionalRate::getRateNotes() const {
    return m_rate_notes;
}
void OAIAdditionalRate::setRateNotes(const QString &rate_notes) {
    m_rate_notes = rate_notes;
    m_rate_notes_isSet = true;
}

bool OAIAdditionalRate::is_rate_notes_Set() const{
    return m_rate_notes_isSet;
}

bool OAIAdditionalRate::is_rate_notes_Valid() const{
    return m_rate_notes_isValid;
}

QString OAIAdditionalRate::getRatePer() const {
    return m_rate_per;
}
void OAIAdditionalRate::setRatePer(const QString &rate_per) {
    m_rate_per = rate_per;
    m_rate_per_isSet = true;
}

bool OAIAdditionalRate::is_rate_per_Set() const{
    return m_rate_per_isSet;
}

bool OAIAdditionalRate::is_rate_per_Valid() const{
    return m_rate_per_isValid;
}

QString OAIAdditionalRate::getShift() const {
    return m_shift;
}
void OAIAdditionalRate::setShift(const QString &shift) {
    m_shift = shift;
    m_shift_isSet = true;
}

bool OAIAdditionalRate::is_shift_Set() const{
    return m_shift_isSet;
}

bool OAIAdditionalRate::is_shift_Valid() const{
    return m_shift_isValid;
}

bool OAIAdditionalRate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_change_reason_isSet) {
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

        if (m_end_check_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rate_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rate_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rate_per_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shift_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAdditionalRate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
