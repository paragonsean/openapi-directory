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

#include "OAIPayStatementDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayStatementDetails::OAIPayStatementDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayStatementDetails::OAIPayStatementDetails() {
    this->initializeModel();
}

OAIPayStatementDetails::~OAIPayStatementDetails() {}

void OAIPayStatementDetails::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_check_date_isSet = false;
    m_check_date_isValid = false;

    m_det_isSet = false;
    m_det_isValid = false;

    m_det_code_isSet = false;
    m_det_code_isValid = false;

    m_det_type_isSet = false;
    m_det_type_isValid = false;

    m_eligible_compensation_isSet = false;
    m_eligible_compensation_isValid = false;

    m_hours_isSet = false;
    m_hours_isValid = false;

    m_rate_isSet = false;
    m_rate_isValid = false;

    m_transaction_number_isSet = false;
    m_transaction_number_isValid = false;

    m_transaction_type_isSet = false;
    m_transaction_type_isValid = false;

    m_year_isSet = false;
    m_year_isValid = false;
}

void OAIPayStatementDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayStatementDetails::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_check_date_isValid = ::OpenAPI::fromJsonValue(m_check_date, json[QString("checkDate")]);
    m_check_date_isSet = !json[QString("checkDate")].isNull() && m_check_date_isValid;

    m_det_isValid = ::OpenAPI::fromJsonValue(m_det, json[QString("det")]);
    m_det_isSet = !json[QString("det")].isNull() && m_det_isValid;

    m_det_code_isValid = ::OpenAPI::fromJsonValue(m_det_code, json[QString("detCode")]);
    m_det_code_isSet = !json[QString("detCode")].isNull() && m_det_code_isValid;

    m_det_type_isValid = ::OpenAPI::fromJsonValue(m_det_type, json[QString("detType")]);
    m_det_type_isSet = !json[QString("detType")].isNull() && m_det_type_isValid;

    m_eligible_compensation_isValid = ::OpenAPI::fromJsonValue(m_eligible_compensation, json[QString("eligibleCompensation")]);
    m_eligible_compensation_isSet = !json[QString("eligibleCompensation")].isNull() && m_eligible_compensation_isValid;

    m_hours_isValid = ::OpenAPI::fromJsonValue(m_hours, json[QString("hours")]);
    m_hours_isSet = !json[QString("hours")].isNull() && m_hours_isValid;

    m_rate_isValid = ::OpenAPI::fromJsonValue(m_rate, json[QString("rate")]);
    m_rate_isSet = !json[QString("rate")].isNull() && m_rate_isValid;

    m_transaction_number_isValid = ::OpenAPI::fromJsonValue(m_transaction_number, json[QString("transactionNumber")]);
    m_transaction_number_isSet = !json[QString("transactionNumber")].isNull() && m_transaction_number_isValid;

    m_transaction_type_isValid = ::OpenAPI::fromJsonValue(m_transaction_type, json[QString("transactionType")]);
    m_transaction_type_isSet = !json[QString("transactionType")].isNull() && m_transaction_type_isValid;

    m_year_isValid = ::OpenAPI::fromJsonValue(m_year, json[QString("year")]);
    m_year_isSet = !json[QString("year")].isNull() && m_year_isValid;
}

QString OAIPayStatementDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayStatementDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_check_date_isSet) {
        obj.insert(QString("checkDate"), ::OpenAPI::toJsonValue(m_check_date));
    }
    if (m_det_isSet) {
        obj.insert(QString("det"), ::OpenAPI::toJsonValue(m_det));
    }
    if (m_det_code_isSet) {
        obj.insert(QString("detCode"), ::OpenAPI::toJsonValue(m_det_code));
    }
    if (m_det_type_isSet) {
        obj.insert(QString("detType"), ::OpenAPI::toJsonValue(m_det_type));
    }
    if (m_eligible_compensation_isSet) {
        obj.insert(QString("eligibleCompensation"), ::OpenAPI::toJsonValue(m_eligible_compensation));
    }
    if (m_hours_isSet) {
        obj.insert(QString("hours"), ::OpenAPI::toJsonValue(m_hours));
    }
    if (m_rate_isSet) {
        obj.insert(QString("rate"), ::OpenAPI::toJsonValue(m_rate));
    }
    if (m_transaction_number_isSet) {
        obj.insert(QString("transactionNumber"), ::OpenAPI::toJsonValue(m_transaction_number));
    }
    if (m_transaction_type_isSet) {
        obj.insert(QString("transactionType"), ::OpenAPI::toJsonValue(m_transaction_type));
    }
    if (m_year_isSet) {
        obj.insert(QString("year"), ::OpenAPI::toJsonValue(m_year));
    }
    return obj;
}

double OAIPayStatementDetails::getAmount() const {
    return m_amount;
}
void OAIPayStatementDetails::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIPayStatementDetails::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIPayStatementDetails::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAIPayStatementDetails::getCheckDate() const {
    return m_check_date;
}
void OAIPayStatementDetails::setCheckDate(const QString &check_date) {
    m_check_date = check_date;
    m_check_date_isSet = true;
}

bool OAIPayStatementDetails::is_check_date_Set() const{
    return m_check_date_isSet;
}

bool OAIPayStatementDetails::is_check_date_Valid() const{
    return m_check_date_isValid;
}

QString OAIPayStatementDetails::getDet() const {
    return m_det;
}
void OAIPayStatementDetails::setDet(const QString &det) {
    m_det = det;
    m_det_isSet = true;
}

bool OAIPayStatementDetails::is_det_Set() const{
    return m_det_isSet;
}

bool OAIPayStatementDetails::is_det_Valid() const{
    return m_det_isValid;
}

QString OAIPayStatementDetails::getDetCode() const {
    return m_det_code;
}
void OAIPayStatementDetails::setDetCode(const QString &det_code) {
    m_det_code = det_code;
    m_det_code_isSet = true;
}

bool OAIPayStatementDetails::is_det_code_Set() const{
    return m_det_code_isSet;
}

bool OAIPayStatementDetails::is_det_code_Valid() const{
    return m_det_code_isValid;
}

QString OAIPayStatementDetails::getDetType() const {
    return m_det_type;
}
void OAIPayStatementDetails::setDetType(const QString &det_type) {
    m_det_type = det_type;
    m_det_type_isSet = true;
}

bool OAIPayStatementDetails::is_det_type_Set() const{
    return m_det_type_isSet;
}

bool OAIPayStatementDetails::is_det_type_Valid() const{
    return m_det_type_isValid;
}

double OAIPayStatementDetails::getEligibleCompensation() const {
    return m_eligible_compensation;
}
void OAIPayStatementDetails::setEligibleCompensation(const double &eligible_compensation) {
    m_eligible_compensation = eligible_compensation;
    m_eligible_compensation_isSet = true;
}

bool OAIPayStatementDetails::is_eligible_compensation_Set() const{
    return m_eligible_compensation_isSet;
}

bool OAIPayStatementDetails::is_eligible_compensation_Valid() const{
    return m_eligible_compensation_isValid;
}

double OAIPayStatementDetails::getHours() const {
    return m_hours;
}
void OAIPayStatementDetails::setHours(const double &hours) {
    m_hours = hours;
    m_hours_isSet = true;
}

bool OAIPayStatementDetails::is_hours_Set() const{
    return m_hours_isSet;
}

bool OAIPayStatementDetails::is_hours_Valid() const{
    return m_hours_isValid;
}

double OAIPayStatementDetails::getRate() const {
    return m_rate;
}
void OAIPayStatementDetails::setRate(const double &rate) {
    m_rate = rate;
    m_rate_isSet = true;
}

bool OAIPayStatementDetails::is_rate_Set() const{
    return m_rate_isSet;
}

bool OAIPayStatementDetails::is_rate_Valid() const{
    return m_rate_isValid;
}

qint32 OAIPayStatementDetails::getTransactionNumber() const {
    return m_transaction_number;
}
void OAIPayStatementDetails::setTransactionNumber(const qint32 &transaction_number) {
    m_transaction_number = transaction_number;
    m_transaction_number_isSet = true;
}

bool OAIPayStatementDetails::is_transaction_number_Set() const{
    return m_transaction_number_isSet;
}

bool OAIPayStatementDetails::is_transaction_number_Valid() const{
    return m_transaction_number_isValid;
}

QString OAIPayStatementDetails::getTransactionType() const {
    return m_transaction_type;
}
void OAIPayStatementDetails::setTransactionType(const QString &transaction_type) {
    m_transaction_type = transaction_type;
    m_transaction_type_isSet = true;
}

bool OAIPayStatementDetails::is_transaction_type_Set() const{
    return m_transaction_type_isSet;
}

bool OAIPayStatementDetails::is_transaction_type_Valid() const{
    return m_transaction_type_isValid;
}

qint32 OAIPayStatementDetails::getYear() const {
    return m_year;
}
void OAIPayStatementDetails::setYear(const qint32 &year) {
    m_year = year;
    m_year_isSet = true;
}

bool OAIPayStatementDetails::is_year_Set() const{
    return m_year_isSet;
}

bool OAIPayStatementDetails::is_year_Valid() const{
    return m_year_isValid;
}

bool OAIPayStatementDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_det_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_det_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_det_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_eligible_compensation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPayStatementDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
