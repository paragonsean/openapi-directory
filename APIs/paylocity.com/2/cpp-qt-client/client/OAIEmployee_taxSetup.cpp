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

#include "OAIEmployee_taxSetup.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmployee_taxSetup::OAIEmployee_taxSetup(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmployee_taxSetup::OAIEmployee_taxSetup() {
    this->initializeModel();
}

OAIEmployee_taxSetup::~OAIEmployee_taxSetup() {}

void OAIEmployee_taxSetup::initializeModel() {

    m_fitw_exempt_notes_isSet = false;
    m_fitw_exempt_notes_isValid = false;

    m_fitw_exempt_reason_isSet = false;
    m_fitw_exempt_reason_isValid = false;

    m_futa_exempt_notes_isSet = false;
    m_futa_exempt_notes_isValid = false;

    m_futa_exempt_reason_isSet = false;
    m_futa_exempt_reason_isValid = false;

    m_is_employee943_isSet = false;
    m_is_employee943_isValid = false;

    m_is_pension_isSet = false;
    m_is_pension_isValid = false;

    m_is_statutory_isSet = false;
    m_is_statutory_isValid = false;

    m_med_exempt_notes_isSet = false;
    m_med_exempt_notes_isValid = false;

    m_med_exempt_reason_isSet = false;
    m_med_exempt_reason_isValid = false;

    m_sitw_exempt_notes_isSet = false;
    m_sitw_exempt_notes_isValid = false;

    m_sitw_exempt_reason_isSet = false;
    m_sitw_exempt_reason_isValid = false;

    m_ss_exempt_notes_isSet = false;
    m_ss_exempt_notes_isValid = false;

    m_ss_exempt_reason_isSet = false;
    m_ss_exempt_reason_isValid = false;

    m_sui_exempt_notes_isSet = false;
    m_sui_exempt_notes_isValid = false;

    m_sui_exempt_reason_isSet = false;
    m_sui_exempt_reason_isValid = false;

    m_sui_state_isSet = false;
    m_sui_state_isValid = false;

    m_tax_distribution_code1099_r_isSet = false;
    m_tax_distribution_code1099_r_isValid = false;

    m_tax_form_isSet = false;
    m_tax_form_isValid = false;
}

void OAIEmployee_taxSetup::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmployee_taxSetup::fromJsonObject(QJsonObject json) {

    m_fitw_exempt_notes_isValid = ::OpenAPI::fromJsonValue(m_fitw_exempt_notes, json[QString("fitwExemptNotes")]);
    m_fitw_exempt_notes_isSet = !json[QString("fitwExemptNotes")].isNull() && m_fitw_exempt_notes_isValid;

    m_fitw_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_fitw_exempt_reason, json[QString("fitwExemptReason")]);
    m_fitw_exempt_reason_isSet = !json[QString("fitwExemptReason")].isNull() && m_fitw_exempt_reason_isValid;

    m_futa_exempt_notes_isValid = ::OpenAPI::fromJsonValue(m_futa_exempt_notes, json[QString("futaExemptNotes")]);
    m_futa_exempt_notes_isSet = !json[QString("futaExemptNotes")].isNull() && m_futa_exempt_notes_isValid;

    m_futa_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_futa_exempt_reason, json[QString("futaExemptReason")]);
    m_futa_exempt_reason_isSet = !json[QString("futaExemptReason")].isNull() && m_futa_exempt_reason_isValid;

    m_is_employee943_isValid = ::OpenAPI::fromJsonValue(m_is_employee943, json[QString("isEmployee943")]);
    m_is_employee943_isSet = !json[QString("isEmployee943")].isNull() && m_is_employee943_isValid;

    m_is_pension_isValid = ::OpenAPI::fromJsonValue(m_is_pension, json[QString("isPension")]);
    m_is_pension_isSet = !json[QString("isPension")].isNull() && m_is_pension_isValid;

    m_is_statutory_isValid = ::OpenAPI::fromJsonValue(m_is_statutory, json[QString("isStatutory")]);
    m_is_statutory_isSet = !json[QString("isStatutory")].isNull() && m_is_statutory_isValid;

    m_med_exempt_notes_isValid = ::OpenAPI::fromJsonValue(m_med_exempt_notes, json[QString("medExemptNotes")]);
    m_med_exempt_notes_isSet = !json[QString("medExemptNotes")].isNull() && m_med_exempt_notes_isValid;

    m_med_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_med_exempt_reason, json[QString("medExemptReason")]);
    m_med_exempt_reason_isSet = !json[QString("medExemptReason")].isNull() && m_med_exempt_reason_isValid;

    m_sitw_exempt_notes_isValid = ::OpenAPI::fromJsonValue(m_sitw_exempt_notes, json[QString("sitwExemptNotes")]);
    m_sitw_exempt_notes_isSet = !json[QString("sitwExemptNotes")].isNull() && m_sitw_exempt_notes_isValid;

    m_sitw_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_sitw_exempt_reason, json[QString("sitwExemptReason")]);
    m_sitw_exempt_reason_isSet = !json[QString("sitwExemptReason")].isNull() && m_sitw_exempt_reason_isValid;

    m_ss_exempt_notes_isValid = ::OpenAPI::fromJsonValue(m_ss_exempt_notes, json[QString("ssExemptNotes")]);
    m_ss_exempt_notes_isSet = !json[QString("ssExemptNotes")].isNull() && m_ss_exempt_notes_isValid;

    m_ss_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_ss_exempt_reason, json[QString("ssExemptReason")]);
    m_ss_exempt_reason_isSet = !json[QString("ssExemptReason")].isNull() && m_ss_exempt_reason_isValid;

    m_sui_exempt_notes_isValid = ::OpenAPI::fromJsonValue(m_sui_exempt_notes, json[QString("suiExemptNotes")]);
    m_sui_exempt_notes_isSet = !json[QString("suiExemptNotes")].isNull() && m_sui_exempt_notes_isValid;

    m_sui_exempt_reason_isValid = ::OpenAPI::fromJsonValue(m_sui_exempt_reason, json[QString("suiExemptReason")]);
    m_sui_exempt_reason_isSet = !json[QString("suiExemptReason")].isNull() && m_sui_exempt_reason_isValid;

    m_sui_state_isValid = ::OpenAPI::fromJsonValue(m_sui_state, json[QString("suiState")]);
    m_sui_state_isSet = !json[QString("suiState")].isNull() && m_sui_state_isValid;

    m_tax_distribution_code1099_r_isValid = ::OpenAPI::fromJsonValue(m_tax_distribution_code1099_r, json[QString("taxDistributionCode1099R")]);
    m_tax_distribution_code1099_r_isSet = !json[QString("taxDistributionCode1099R")].isNull() && m_tax_distribution_code1099_r_isValid;

    m_tax_form_isValid = ::OpenAPI::fromJsonValue(m_tax_form, json[QString("taxForm")]);
    m_tax_form_isSet = !json[QString("taxForm")].isNull() && m_tax_form_isValid;
}

QString OAIEmployee_taxSetup::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmployee_taxSetup::asJsonObject() const {
    QJsonObject obj;
    if (m_fitw_exempt_notes_isSet) {
        obj.insert(QString("fitwExemptNotes"), ::OpenAPI::toJsonValue(m_fitw_exempt_notes));
    }
    if (m_fitw_exempt_reason_isSet) {
        obj.insert(QString("fitwExemptReason"), ::OpenAPI::toJsonValue(m_fitw_exempt_reason));
    }
    if (m_futa_exempt_notes_isSet) {
        obj.insert(QString("futaExemptNotes"), ::OpenAPI::toJsonValue(m_futa_exempt_notes));
    }
    if (m_futa_exempt_reason_isSet) {
        obj.insert(QString("futaExemptReason"), ::OpenAPI::toJsonValue(m_futa_exempt_reason));
    }
    if (m_is_employee943_isSet) {
        obj.insert(QString("isEmployee943"), ::OpenAPI::toJsonValue(m_is_employee943));
    }
    if (m_is_pension_isSet) {
        obj.insert(QString("isPension"), ::OpenAPI::toJsonValue(m_is_pension));
    }
    if (m_is_statutory_isSet) {
        obj.insert(QString("isStatutory"), ::OpenAPI::toJsonValue(m_is_statutory));
    }
    if (m_med_exempt_notes_isSet) {
        obj.insert(QString("medExemptNotes"), ::OpenAPI::toJsonValue(m_med_exempt_notes));
    }
    if (m_med_exempt_reason_isSet) {
        obj.insert(QString("medExemptReason"), ::OpenAPI::toJsonValue(m_med_exempt_reason));
    }
    if (m_sitw_exempt_notes_isSet) {
        obj.insert(QString("sitwExemptNotes"), ::OpenAPI::toJsonValue(m_sitw_exempt_notes));
    }
    if (m_sitw_exempt_reason_isSet) {
        obj.insert(QString("sitwExemptReason"), ::OpenAPI::toJsonValue(m_sitw_exempt_reason));
    }
    if (m_ss_exempt_notes_isSet) {
        obj.insert(QString("ssExemptNotes"), ::OpenAPI::toJsonValue(m_ss_exempt_notes));
    }
    if (m_ss_exempt_reason_isSet) {
        obj.insert(QString("ssExemptReason"), ::OpenAPI::toJsonValue(m_ss_exempt_reason));
    }
    if (m_sui_exempt_notes_isSet) {
        obj.insert(QString("suiExemptNotes"), ::OpenAPI::toJsonValue(m_sui_exempt_notes));
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
    return obj;
}

QString OAIEmployee_taxSetup::getFitwExemptNotes() const {
    return m_fitw_exempt_notes;
}
void OAIEmployee_taxSetup::setFitwExemptNotes(const QString &fitw_exempt_notes) {
    m_fitw_exempt_notes = fitw_exempt_notes;
    m_fitw_exempt_notes_isSet = true;
}

bool OAIEmployee_taxSetup::is_fitw_exempt_notes_Set() const{
    return m_fitw_exempt_notes_isSet;
}

bool OAIEmployee_taxSetup::is_fitw_exempt_notes_Valid() const{
    return m_fitw_exempt_notes_isValid;
}

QString OAIEmployee_taxSetup::getFitwExemptReason() const {
    return m_fitw_exempt_reason;
}
void OAIEmployee_taxSetup::setFitwExemptReason(const QString &fitw_exempt_reason) {
    m_fitw_exempt_reason = fitw_exempt_reason;
    m_fitw_exempt_reason_isSet = true;
}

bool OAIEmployee_taxSetup::is_fitw_exempt_reason_Set() const{
    return m_fitw_exempt_reason_isSet;
}

bool OAIEmployee_taxSetup::is_fitw_exempt_reason_Valid() const{
    return m_fitw_exempt_reason_isValid;
}

QString OAIEmployee_taxSetup::getFutaExemptNotes() const {
    return m_futa_exempt_notes;
}
void OAIEmployee_taxSetup::setFutaExemptNotes(const QString &futa_exempt_notes) {
    m_futa_exempt_notes = futa_exempt_notes;
    m_futa_exempt_notes_isSet = true;
}

bool OAIEmployee_taxSetup::is_futa_exempt_notes_Set() const{
    return m_futa_exempt_notes_isSet;
}

bool OAIEmployee_taxSetup::is_futa_exempt_notes_Valid() const{
    return m_futa_exempt_notes_isValid;
}

QString OAIEmployee_taxSetup::getFutaExemptReason() const {
    return m_futa_exempt_reason;
}
void OAIEmployee_taxSetup::setFutaExemptReason(const QString &futa_exempt_reason) {
    m_futa_exempt_reason = futa_exempt_reason;
    m_futa_exempt_reason_isSet = true;
}

bool OAIEmployee_taxSetup::is_futa_exempt_reason_Set() const{
    return m_futa_exempt_reason_isSet;
}

bool OAIEmployee_taxSetup::is_futa_exempt_reason_Valid() const{
    return m_futa_exempt_reason_isValid;
}

bool OAIEmployee_taxSetup::isIsEmployee943() const {
    return m_is_employee943;
}
void OAIEmployee_taxSetup::setIsEmployee943(const bool &is_employee943) {
    m_is_employee943 = is_employee943;
    m_is_employee943_isSet = true;
}

bool OAIEmployee_taxSetup::is_is_employee943_Set() const{
    return m_is_employee943_isSet;
}

bool OAIEmployee_taxSetup::is_is_employee943_Valid() const{
    return m_is_employee943_isValid;
}

bool OAIEmployee_taxSetup::isIsPension() const {
    return m_is_pension;
}
void OAIEmployee_taxSetup::setIsPension(const bool &is_pension) {
    m_is_pension = is_pension;
    m_is_pension_isSet = true;
}

bool OAIEmployee_taxSetup::is_is_pension_Set() const{
    return m_is_pension_isSet;
}

bool OAIEmployee_taxSetup::is_is_pension_Valid() const{
    return m_is_pension_isValid;
}

bool OAIEmployee_taxSetup::isIsStatutory() const {
    return m_is_statutory;
}
void OAIEmployee_taxSetup::setIsStatutory(const bool &is_statutory) {
    m_is_statutory = is_statutory;
    m_is_statutory_isSet = true;
}

bool OAIEmployee_taxSetup::is_is_statutory_Set() const{
    return m_is_statutory_isSet;
}

bool OAIEmployee_taxSetup::is_is_statutory_Valid() const{
    return m_is_statutory_isValid;
}

QString OAIEmployee_taxSetup::getMedExemptNotes() const {
    return m_med_exempt_notes;
}
void OAIEmployee_taxSetup::setMedExemptNotes(const QString &med_exempt_notes) {
    m_med_exempt_notes = med_exempt_notes;
    m_med_exempt_notes_isSet = true;
}

bool OAIEmployee_taxSetup::is_med_exempt_notes_Set() const{
    return m_med_exempt_notes_isSet;
}

bool OAIEmployee_taxSetup::is_med_exempt_notes_Valid() const{
    return m_med_exempt_notes_isValid;
}

QString OAIEmployee_taxSetup::getMedExemptReason() const {
    return m_med_exempt_reason;
}
void OAIEmployee_taxSetup::setMedExemptReason(const QString &med_exempt_reason) {
    m_med_exempt_reason = med_exempt_reason;
    m_med_exempt_reason_isSet = true;
}

bool OAIEmployee_taxSetup::is_med_exempt_reason_Set() const{
    return m_med_exempt_reason_isSet;
}

bool OAIEmployee_taxSetup::is_med_exempt_reason_Valid() const{
    return m_med_exempt_reason_isValid;
}

QString OAIEmployee_taxSetup::getSitwExemptNotes() const {
    return m_sitw_exempt_notes;
}
void OAIEmployee_taxSetup::setSitwExemptNotes(const QString &sitw_exempt_notes) {
    m_sitw_exempt_notes = sitw_exempt_notes;
    m_sitw_exempt_notes_isSet = true;
}

bool OAIEmployee_taxSetup::is_sitw_exempt_notes_Set() const{
    return m_sitw_exempt_notes_isSet;
}

bool OAIEmployee_taxSetup::is_sitw_exempt_notes_Valid() const{
    return m_sitw_exempt_notes_isValid;
}

QString OAIEmployee_taxSetup::getSitwExemptReason() const {
    return m_sitw_exempt_reason;
}
void OAIEmployee_taxSetup::setSitwExemptReason(const QString &sitw_exempt_reason) {
    m_sitw_exempt_reason = sitw_exempt_reason;
    m_sitw_exempt_reason_isSet = true;
}

bool OAIEmployee_taxSetup::is_sitw_exempt_reason_Set() const{
    return m_sitw_exempt_reason_isSet;
}

bool OAIEmployee_taxSetup::is_sitw_exempt_reason_Valid() const{
    return m_sitw_exempt_reason_isValid;
}

QString OAIEmployee_taxSetup::getSsExemptNotes() const {
    return m_ss_exempt_notes;
}
void OAIEmployee_taxSetup::setSsExemptNotes(const QString &ss_exempt_notes) {
    m_ss_exempt_notes = ss_exempt_notes;
    m_ss_exempt_notes_isSet = true;
}

bool OAIEmployee_taxSetup::is_ss_exempt_notes_Set() const{
    return m_ss_exempt_notes_isSet;
}

bool OAIEmployee_taxSetup::is_ss_exempt_notes_Valid() const{
    return m_ss_exempt_notes_isValid;
}

QString OAIEmployee_taxSetup::getSsExemptReason() const {
    return m_ss_exempt_reason;
}
void OAIEmployee_taxSetup::setSsExemptReason(const QString &ss_exempt_reason) {
    m_ss_exempt_reason = ss_exempt_reason;
    m_ss_exempt_reason_isSet = true;
}

bool OAIEmployee_taxSetup::is_ss_exempt_reason_Set() const{
    return m_ss_exempt_reason_isSet;
}

bool OAIEmployee_taxSetup::is_ss_exempt_reason_Valid() const{
    return m_ss_exempt_reason_isValid;
}

QString OAIEmployee_taxSetup::getSuiExemptNotes() const {
    return m_sui_exempt_notes;
}
void OAIEmployee_taxSetup::setSuiExemptNotes(const QString &sui_exempt_notes) {
    m_sui_exempt_notes = sui_exempt_notes;
    m_sui_exempt_notes_isSet = true;
}

bool OAIEmployee_taxSetup::is_sui_exempt_notes_Set() const{
    return m_sui_exempt_notes_isSet;
}

bool OAIEmployee_taxSetup::is_sui_exempt_notes_Valid() const{
    return m_sui_exempt_notes_isValid;
}

QString OAIEmployee_taxSetup::getSuiExemptReason() const {
    return m_sui_exempt_reason;
}
void OAIEmployee_taxSetup::setSuiExemptReason(const QString &sui_exempt_reason) {
    m_sui_exempt_reason = sui_exempt_reason;
    m_sui_exempt_reason_isSet = true;
}

bool OAIEmployee_taxSetup::is_sui_exempt_reason_Set() const{
    return m_sui_exempt_reason_isSet;
}

bool OAIEmployee_taxSetup::is_sui_exempt_reason_Valid() const{
    return m_sui_exempt_reason_isValid;
}

QString OAIEmployee_taxSetup::getSuiState() const {
    return m_sui_state;
}
void OAIEmployee_taxSetup::setSuiState(const QString &sui_state) {
    m_sui_state = sui_state;
    m_sui_state_isSet = true;
}

bool OAIEmployee_taxSetup::is_sui_state_Set() const{
    return m_sui_state_isSet;
}

bool OAIEmployee_taxSetup::is_sui_state_Valid() const{
    return m_sui_state_isValid;
}

QString OAIEmployee_taxSetup::getTaxDistributionCode1099R() const {
    return m_tax_distribution_code1099_r;
}
void OAIEmployee_taxSetup::setTaxDistributionCode1099R(const QString &tax_distribution_code1099_r) {
    m_tax_distribution_code1099_r = tax_distribution_code1099_r;
    m_tax_distribution_code1099_r_isSet = true;
}

bool OAIEmployee_taxSetup::is_tax_distribution_code1099_r_Set() const{
    return m_tax_distribution_code1099_r_isSet;
}

bool OAIEmployee_taxSetup::is_tax_distribution_code1099_r_Valid() const{
    return m_tax_distribution_code1099_r_isValid;
}

QString OAIEmployee_taxSetup::getTaxForm() const {
    return m_tax_form;
}
void OAIEmployee_taxSetup::setTaxForm(const QString &tax_form) {
    m_tax_form = tax_form;
    m_tax_form_isSet = true;
}

bool OAIEmployee_taxSetup::is_tax_form_Set() const{
    return m_tax_form_isSet;
}

bool OAIEmployee_taxSetup::is_tax_form_Valid() const{
    return m_tax_form_isValid;
}

bool OAIEmployee_taxSetup::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fitw_exempt_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fitw_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_futa_exempt_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_futa_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_employee943_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_pension_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_statutory_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_med_exempt_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_med_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sitw_exempt_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sitw_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ss_exempt_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ss_exempt_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sui_exempt_notes_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIEmployee_taxSetup::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
