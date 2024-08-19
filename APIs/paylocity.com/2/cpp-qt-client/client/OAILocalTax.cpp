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

#include "OAILocalTax.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILocalTax::OAILocalTax(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILocalTax::OAILocalTax() {
    this->initializeModel();
}

OAILocalTax::~OAILocalTax() {}

void OAILocalTax::initializeModel() {

    m_exemptions_isSet = false;
    m_exemptions_isValid = false;

    m_exemptions2_isSet = false;
    m_exemptions2_isValid = false;

    m_filing_status_isSet = false;
    m_filing_status_isValid = false;

    m_resident_psd_isSet = false;
    m_resident_psd_isValid = false;

    m_tax_code_isSet = false;
    m_tax_code_isValid = false;

    m_work_psd_isSet = false;
    m_work_psd_isValid = false;
}

void OAILocalTax::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILocalTax::fromJsonObject(QJsonObject json) {

    m_exemptions_isValid = ::OpenAPI::fromJsonValue(m_exemptions, json[QString("exemptions")]);
    m_exemptions_isSet = !json[QString("exemptions")].isNull() && m_exemptions_isValid;

    m_exemptions2_isValid = ::OpenAPI::fromJsonValue(m_exemptions2, json[QString("exemptions2")]);
    m_exemptions2_isSet = !json[QString("exemptions2")].isNull() && m_exemptions2_isValid;

    m_filing_status_isValid = ::OpenAPI::fromJsonValue(m_filing_status, json[QString("filingStatus")]);
    m_filing_status_isSet = !json[QString("filingStatus")].isNull() && m_filing_status_isValid;

    m_resident_psd_isValid = ::OpenAPI::fromJsonValue(m_resident_psd, json[QString("residentPSD")]);
    m_resident_psd_isSet = !json[QString("residentPSD")].isNull() && m_resident_psd_isValid;

    m_tax_code_isValid = ::OpenAPI::fromJsonValue(m_tax_code, json[QString("taxCode")]);
    m_tax_code_isSet = !json[QString("taxCode")].isNull() && m_tax_code_isValid;

    m_work_psd_isValid = ::OpenAPI::fromJsonValue(m_work_psd, json[QString("workPSD")]);
    m_work_psd_isSet = !json[QString("workPSD")].isNull() && m_work_psd_isValid;
}

QString OAILocalTax::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILocalTax::asJsonObject() const {
    QJsonObject obj;
    if (m_exemptions_isSet) {
        obj.insert(QString("exemptions"), ::OpenAPI::toJsonValue(m_exemptions));
    }
    if (m_exemptions2_isSet) {
        obj.insert(QString("exemptions2"), ::OpenAPI::toJsonValue(m_exemptions2));
    }
    if (m_filing_status_isSet) {
        obj.insert(QString("filingStatus"), ::OpenAPI::toJsonValue(m_filing_status));
    }
    if (m_resident_psd_isSet) {
        obj.insert(QString("residentPSD"), ::OpenAPI::toJsonValue(m_resident_psd));
    }
    if (m_tax_code_isSet) {
        obj.insert(QString("taxCode"), ::OpenAPI::toJsonValue(m_tax_code));
    }
    if (m_work_psd_isSet) {
        obj.insert(QString("workPSD"), ::OpenAPI::toJsonValue(m_work_psd));
    }
    return obj;
}

double OAILocalTax::getExemptions() const {
    return m_exemptions;
}
void OAILocalTax::setExemptions(const double &exemptions) {
    m_exemptions = exemptions;
    m_exemptions_isSet = true;
}

bool OAILocalTax::is_exemptions_Set() const{
    return m_exemptions_isSet;
}

bool OAILocalTax::is_exemptions_Valid() const{
    return m_exemptions_isValid;
}

double OAILocalTax::getExemptions2() const {
    return m_exemptions2;
}
void OAILocalTax::setExemptions2(const double &exemptions2) {
    m_exemptions2 = exemptions2;
    m_exemptions2_isSet = true;
}

bool OAILocalTax::is_exemptions2_Set() const{
    return m_exemptions2_isSet;
}

bool OAILocalTax::is_exemptions2_Valid() const{
    return m_exemptions2_isValid;
}

QString OAILocalTax::getFilingStatus() const {
    return m_filing_status;
}
void OAILocalTax::setFilingStatus(const QString &filing_status) {
    m_filing_status = filing_status;
    m_filing_status_isSet = true;
}

bool OAILocalTax::is_filing_status_Set() const{
    return m_filing_status_isSet;
}

bool OAILocalTax::is_filing_status_Valid() const{
    return m_filing_status_isValid;
}

QString OAILocalTax::getResidentPsd() const {
    return m_resident_psd;
}
void OAILocalTax::setResidentPsd(const QString &resident_psd) {
    m_resident_psd = resident_psd;
    m_resident_psd_isSet = true;
}

bool OAILocalTax::is_resident_psd_Set() const{
    return m_resident_psd_isSet;
}

bool OAILocalTax::is_resident_psd_Valid() const{
    return m_resident_psd_isValid;
}

QString OAILocalTax::getTaxCode() const {
    return m_tax_code;
}
void OAILocalTax::setTaxCode(const QString &tax_code) {
    m_tax_code = tax_code;
    m_tax_code_isSet = true;
}

bool OAILocalTax::is_tax_code_Set() const{
    return m_tax_code_isSet;
}

bool OAILocalTax::is_tax_code_Valid() const{
    return m_tax_code_isValid;
}

QString OAILocalTax::getWorkPsd() const {
    return m_work_psd;
}
void OAILocalTax::setWorkPsd(const QString &work_psd) {
    m_work_psd = work_psd;
    m_work_psd_isSet = true;
}

bool OAILocalTax::is_work_psd_Set() const{
    return m_work_psd_isSet;
}

bool OAILocalTax::is_work_psd_Valid() const{
    return m_work_psd_isValid;
}

bool OAILocalTax::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_exemptions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exemptions2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filing_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resident_psd_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_psd_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILocalTax::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
