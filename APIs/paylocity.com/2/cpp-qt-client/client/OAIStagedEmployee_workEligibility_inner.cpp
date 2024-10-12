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

#include "OAIStagedEmployee_workEligibility_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStagedEmployee_workEligibility_inner::OAIStagedEmployee_workEligibility_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStagedEmployee_workEligibility_inner::OAIStagedEmployee_workEligibility_inner() {
    this->initializeModel();
}

OAIStagedEmployee_workEligibility_inner::~OAIStagedEmployee_workEligibility_inner() {}

void OAIStagedEmployee_workEligibility_inner::initializeModel() {

    m_alien_or_admission_document_number_isSet = false;
    m_alien_or_admission_document_number_isValid = false;

    m_attested_date_isSet = false;
    m_attested_date_isValid = false;

    m_country_of_issuance_isSet = false;
    m_country_of_issuance_isValid = false;

    m_foreign_passport_number_isSet = false;
    m_foreign_passport_number_isValid = false;

    m_i94_admission_number_isSet = false;
    m_i94_admission_number_isValid = false;

    m_i9_date_verified_isSet = false;
    m_i9_date_verified_isValid = false;

    m_i9_notes_isSet = false;
    m_i9_notes_isValid = false;

    m_is_i9_verified_isSet = false;
    m_is_i9_verified_isValid = false;

    m_is_ssn_verified_isSet = false;
    m_is_ssn_verified_isValid = false;

    m_ssn_date_verified_isSet = false;
    m_ssn_date_verified_isValid = false;

    m_ssn_notes_isSet = false;
    m_ssn_notes_isValid = false;

    m_visa_type_isSet = false;
    m_visa_type_isValid = false;

    m_work_authorization_isSet = false;
    m_work_authorization_isValid = false;

    m_work_until_isSet = false;
    m_work_until_isValid = false;
}

void OAIStagedEmployee_workEligibility_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStagedEmployee_workEligibility_inner::fromJsonObject(QJsonObject json) {

    m_alien_or_admission_document_number_isValid = ::OpenAPI::fromJsonValue(m_alien_or_admission_document_number, json[QString("alienOrAdmissionDocumentNumber")]);
    m_alien_or_admission_document_number_isSet = !json[QString("alienOrAdmissionDocumentNumber")].isNull() && m_alien_or_admission_document_number_isValid;

    m_attested_date_isValid = ::OpenAPI::fromJsonValue(m_attested_date, json[QString("attestedDate")]);
    m_attested_date_isSet = !json[QString("attestedDate")].isNull() && m_attested_date_isValid;

    m_country_of_issuance_isValid = ::OpenAPI::fromJsonValue(m_country_of_issuance, json[QString("countryOfIssuance")]);
    m_country_of_issuance_isSet = !json[QString("countryOfIssuance")].isNull() && m_country_of_issuance_isValid;

    m_foreign_passport_number_isValid = ::OpenAPI::fromJsonValue(m_foreign_passport_number, json[QString("foreignPassportNumber")]);
    m_foreign_passport_number_isSet = !json[QString("foreignPassportNumber")].isNull() && m_foreign_passport_number_isValid;

    m_i94_admission_number_isValid = ::OpenAPI::fromJsonValue(m_i94_admission_number, json[QString("i94AdmissionNumber")]);
    m_i94_admission_number_isSet = !json[QString("i94AdmissionNumber")].isNull() && m_i94_admission_number_isValid;

    m_i9_date_verified_isValid = ::OpenAPI::fromJsonValue(m_i9_date_verified, json[QString("i9DateVerified")]);
    m_i9_date_verified_isSet = !json[QString("i9DateVerified")].isNull() && m_i9_date_verified_isValid;

    m_i9_notes_isValid = ::OpenAPI::fromJsonValue(m_i9_notes, json[QString("i9Notes")]);
    m_i9_notes_isSet = !json[QString("i9Notes")].isNull() && m_i9_notes_isValid;

    m_is_i9_verified_isValid = ::OpenAPI::fromJsonValue(m_is_i9_verified, json[QString("isI9Verified")]);
    m_is_i9_verified_isSet = !json[QString("isI9Verified")].isNull() && m_is_i9_verified_isValid;

    m_is_ssn_verified_isValid = ::OpenAPI::fromJsonValue(m_is_ssn_verified, json[QString("isSsnVerified")]);
    m_is_ssn_verified_isSet = !json[QString("isSsnVerified")].isNull() && m_is_ssn_verified_isValid;

    m_ssn_date_verified_isValid = ::OpenAPI::fromJsonValue(m_ssn_date_verified, json[QString("ssnDateVerified")]);
    m_ssn_date_verified_isSet = !json[QString("ssnDateVerified")].isNull() && m_ssn_date_verified_isValid;

    m_ssn_notes_isValid = ::OpenAPI::fromJsonValue(m_ssn_notes, json[QString("ssnNotes")]);
    m_ssn_notes_isSet = !json[QString("ssnNotes")].isNull() && m_ssn_notes_isValid;

    m_visa_type_isValid = ::OpenAPI::fromJsonValue(m_visa_type, json[QString("visaType")]);
    m_visa_type_isSet = !json[QString("visaType")].isNull() && m_visa_type_isValid;

    m_work_authorization_isValid = ::OpenAPI::fromJsonValue(m_work_authorization, json[QString("workAuthorization")]);
    m_work_authorization_isSet = !json[QString("workAuthorization")].isNull() && m_work_authorization_isValid;

    m_work_until_isValid = ::OpenAPI::fromJsonValue(m_work_until, json[QString("workUntil")]);
    m_work_until_isSet = !json[QString("workUntil")].isNull() && m_work_until_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStagedEmployee_workEligibility_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_alien_or_admission_document_number_isSet) {
        obj.insert(QString("alienOrAdmissionDocumentNumber"), ::OpenAPI::toJsonValue(m_alien_or_admission_document_number));
    }
    if (m_attested_date_isSet) {
        obj.insert(QString("attestedDate"), ::OpenAPI::toJsonValue(m_attested_date));
    }
    if (m_country_of_issuance_isSet) {
        obj.insert(QString("countryOfIssuance"), ::OpenAPI::toJsonValue(m_country_of_issuance));
    }
    if (m_foreign_passport_number_isSet) {
        obj.insert(QString("foreignPassportNumber"), ::OpenAPI::toJsonValue(m_foreign_passport_number));
    }
    if (m_i94_admission_number_isSet) {
        obj.insert(QString("i94AdmissionNumber"), ::OpenAPI::toJsonValue(m_i94_admission_number));
    }
    if (m_i9_date_verified_isSet) {
        obj.insert(QString("i9DateVerified"), ::OpenAPI::toJsonValue(m_i9_date_verified));
    }
    if (m_i9_notes_isSet) {
        obj.insert(QString("i9Notes"), ::OpenAPI::toJsonValue(m_i9_notes));
    }
    if (m_is_i9_verified_isSet) {
        obj.insert(QString("isI9Verified"), ::OpenAPI::toJsonValue(m_is_i9_verified));
    }
    if (m_is_ssn_verified_isSet) {
        obj.insert(QString("isSsnVerified"), ::OpenAPI::toJsonValue(m_is_ssn_verified));
    }
    if (m_ssn_date_verified_isSet) {
        obj.insert(QString("ssnDateVerified"), ::OpenAPI::toJsonValue(m_ssn_date_verified));
    }
    if (m_ssn_notes_isSet) {
        obj.insert(QString("ssnNotes"), ::OpenAPI::toJsonValue(m_ssn_notes));
    }
    if (m_visa_type_isSet) {
        obj.insert(QString("visaType"), ::OpenAPI::toJsonValue(m_visa_type));
    }
    if (m_work_authorization_isSet) {
        obj.insert(QString("workAuthorization"), ::OpenAPI::toJsonValue(m_work_authorization));
    }
    if (m_work_until_isSet) {
        obj.insert(QString("workUntil"), ::OpenAPI::toJsonValue(m_work_until));
    }
    return obj;
}

QString OAIStagedEmployee_workEligibility_inner::getAlienOrAdmissionDocumentNumber() const {
    return m_alien_or_admission_document_number;
}
void OAIStagedEmployee_workEligibility_inner::setAlienOrAdmissionDocumentNumber(const QString &alien_or_admission_document_number) {
    m_alien_or_admission_document_number = alien_or_admission_document_number;
    m_alien_or_admission_document_number_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_alien_or_admission_document_number_Set() const{
    return m_alien_or_admission_document_number_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_alien_or_admission_document_number_Valid() const{
    return m_alien_or_admission_document_number_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getAttestedDate() const {
    return m_attested_date;
}
void OAIStagedEmployee_workEligibility_inner::setAttestedDate(const QString &attested_date) {
    m_attested_date = attested_date;
    m_attested_date_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_attested_date_Set() const{
    return m_attested_date_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_attested_date_Valid() const{
    return m_attested_date_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getCountryOfIssuance() const {
    return m_country_of_issuance;
}
void OAIStagedEmployee_workEligibility_inner::setCountryOfIssuance(const QString &country_of_issuance) {
    m_country_of_issuance = country_of_issuance;
    m_country_of_issuance_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_country_of_issuance_Set() const{
    return m_country_of_issuance_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_country_of_issuance_Valid() const{
    return m_country_of_issuance_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getForeignPassportNumber() const {
    return m_foreign_passport_number;
}
void OAIStagedEmployee_workEligibility_inner::setForeignPassportNumber(const QString &foreign_passport_number) {
    m_foreign_passport_number = foreign_passport_number;
    m_foreign_passport_number_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_foreign_passport_number_Set() const{
    return m_foreign_passport_number_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_foreign_passport_number_Valid() const{
    return m_foreign_passport_number_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getI94AdmissionNumber() const {
    return m_i94_admission_number;
}
void OAIStagedEmployee_workEligibility_inner::setI94AdmissionNumber(const QString &i94_admission_number) {
    m_i94_admission_number = i94_admission_number;
    m_i94_admission_number_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_i94_admission_number_Set() const{
    return m_i94_admission_number_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_i94_admission_number_Valid() const{
    return m_i94_admission_number_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getI9DateVerified() const {
    return m_i9_date_verified;
}
void OAIStagedEmployee_workEligibility_inner::setI9DateVerified(const QString &i9_date_verified) {
    m_i9_date_verified = i9_date_verified;
    m_i9_date_verified_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_i9_date_verified_Set() const{
    return m_i9_date_verified_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_i9_date_verified_Valid() const{
    return m_i9_date_verified_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getI9Notes() const {
    return m_i9_notes;
}
void OAIStagedEmployee_workEligibility_inner::setI9Notes(const QString &i9_notes) {
    m_i9_notes = i9_notes;
    m_i9_notes_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_i9_notes_Set() const{
    return m_i9_notes_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_i9_notes_Valid() const{
    return m_i9_notes_isValid;
}

bool OAIStagedEmployee_workEligibility_inner::isIsI9Verified() const {
    return m_is_i9_verified;
}
void OAIStagedEmployee_workEligibility_inner::setIsI9Verified(const bool &is_i9_verified) {
    m_is_i9_verified = is_i9_verified;
    m_is_i9_verified_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_is_i9_verified_Set() const{
    return m_is_i9_verified_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_is_i9_verified_Valid() const{
    return m_is_i9_verified_isValid;
}

bool OAIStagedEmployee_workEligibility_inner::isIsSsnVerified() const {
    return m_is_ssn_verified;
}
void OAIStagedEmployee_workEligibility_inner::setIsSsnVerified(const bool &is_ssn_verified) {
    m_is_ssn_verified = is_ssn_verified;
    m_is_ssn_verified_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_is_ssn_verified_Set() const{
    return m_is_ssn_verified_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_is_ssn_verified_Valid() const{
    return m_is_ssn_verified_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getSsnDateVerified() const {
    return m_ssn_date_verified;
}
void OAIStagedEmployee_workEligibility_inner::setSsnDateVerified(const QString &ssn_date_verified) {
    m_ssn_date_verified = ssn_date_verified;
    m_ssn_date_verified_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_ssn_date_verified_Set() const{
    return m_ssn_date_verified_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_ssn_date_verified_Valid() const{
    return m_ssn_date_verified_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getSsnNotes() const {
    return m_ssn_notes;
}
void OAIStagedEmployee_workEligibility_inner::setSsnNotes(const QString &ssn_notes) {
    m_ssn_notes = ssn_notes;
    m_ssn_notes_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_ssn_notes_Set() const{
    return m_ssn_notes_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_ssn_notes_Valid() const{
    return m_ssn_notes_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getVisaType() const {
    return m_visa_type;
}
void OAIStagedEmployee_workEligibility_inner::setVisaType(const QString &visa_type) {
    m_visa_type = visa_type;
    m_visa_type_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_visa_type_Set() const{
    return m_visa_type_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_visa_type_Valid() const{
    return m_visa_type_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getWorkAuthorization() const {
    return m_work_authorization;
}
void OAIStagedEmployee_workEligibility_inner::setWorkAuthorization(const QString &work_authorization) {
    m_work_authorization = work_authorization;
    m_work_authorization_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_work_authorization_Set() const{
    return m_work_authorization_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_work_authorization_Valid() const{
    return m_work_authorization_isValid;
}

QString OAIStagedEmployee_workEligibility_inner::getWorkUntil() const {
    return m_work_until;
}
void OAIStagedEmployee_workEligibility_inner::setWorkUntil(const QString &work_until) {
    m_work_until = work_until;
    m_work_until_isSet = true;
}

bool OAIStagedEmployee_workEligibility_inner::is_work_until_Set() const{
    return m_work_until_isSet;
}

bool OAIStagedEmployee_workEligibility_inner::is_work_until_Valid() const{
    return m_work_until_isValid;
}

bool OAIStagedEmployee_workEligibility_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alien_or_admission_document_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_attested_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_of_issuance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_foreign_passport_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_i94_admission_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_i9_date_verified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_i9_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_i9_verified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_ssn_verified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssn_date_verified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssn_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_visa_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_authorization_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_until_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStagedEmployee_workEligibility_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
