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

#include "OAIEmployee_primaryStateTax.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmployee_primaryStateTax::OAIEmployee_primaryStateTax(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmployee_primaryStateTax::OAIEmployee_primaryStateTax() {
    this->initializeModel();
}

OAIEmployee_primaryStateTax::~OAIEmployee_primaryStateTax() {}

void OAIEmployee_primaryStateTax::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_deductions_amount_isSet = false;
    m_deductions_amount_isValid = false;

    m_dependents_amount_isSet = false;
    m_dependents_amount_isValid = false;

    m_exemptions_isSet = false;
    m_exemptions_isValid = false;

    m_exemptions2_isSet = false;
    m_exemptions2_isValid = false;

    m_filing_status_isSet = false;
    m_filing_status_isValid = false;

    m_higher_rate_isSet = false;
    m_higher_rate_isValid = false;

    m_other_income_amount_isSet = false;
    m_other_income_amount_isValid = false;

    m_percentage_isSet = false;
    m_percentage_isValid = false;

    m_special_check_calc_isSet = false;
    m_special_check_calc_isValid = false;

    m_tax_calculation_code_isSet = false;
    m_tax_calculation_code_isValid = false;

    m_tax_code_isSet = false;
    m_tax_code_isValid = false;

    m_w4_form_year_isSet = false;
    m_w4_form_year_isValid = false;
}

void OAIEmployee_primaryStateTax::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmployee_primaryStateTax::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_deductions_amount_isValid = ::OpenAPI::fromJsonValue(m_deductions_amount, json[QString("deductionsAmount")]);
    m_deductions_amount_isSet = !json[QString("deductionsAmount")].isNull() && m_deductions_amount_isValid;

    m_dependents_amount_isValid = ::OpenAPI::fromJsonValue(m_dependents_amount, json[QString("dependentsAmount")]);
    m_dependents_amount_isSet = !json[QString("dependentsAmount")].isNull() && m_dependents_amount_isValid;

    m_exemptions_isValid = ::OpenAPI::fromJsonValue(m_exemptions, json[QString("exemptions")]);
    m_exemptions_isSet = !json[QString("exemptions")].isNull() && m_exemptions_isValid;

    m_exemptions2_isValid = ::OpenAPI::fromJsonValue(m_exemptions2, json[QString("exemptions2")]);
    m_exemptions2_isSet = !json[QString("exemptions2")].isNull() && m_exemptions2_isValid;

    m_filing_status_isValid = ::OpenAPI::fromJsonValue(m_filing_status, json[QString("filingStatus")]);
    m_filing_status_isSet = !json[QString("filingStatus")].isNull() && m_filing_status_isValid;

    m_higher_rate_isValid = ::OpenAPI::fromJsonValue(m_higher_rate, json[QString("higherRate")]);
    m_higher_rate_isSet = !json[QString("higherRate")].isNull() && m_higher_rate_isValid;

    m_other_income_amount_isValid = ::OpenAPI::fromJsonValue(m_other_income_amount, json[QString("otherIncomeAmount")]);
    m_other_income_amount_isSet = !json[QString("otherIncomeAmount")].isNull() && m_other_income_amount_isValid;

    m_percentage_isValid = ::OpenAPI::fromJsonValue(m_percentage, json[QString("percentage")]);
    m_percentage_isSet = !json[QString("percentage")].isNull() && m_percentage_isValid;

    m_special_check_calc_isValid = ::OpenAPI::fromJsonValue(m_special_check_calc, json[QString("specialCheckCalc")]);
    m_special_check_calc_isSet = !json[QString("specialCheckCalc")].isNull() && m_special_check_calc_isValid;

    m_tax_calculation_code_isValid = ::OpenAPI::fromJsonValue(m_tax_calculation_code, json[QString("taxCalculationCode")]);
    m_tax_calculation_code_isSet = !json[QString("taxCalculationCode")].isNull() && m_tax_calculation_code_isValid;

    m_tax_code_isValid = ::OpenAPI::fromJsonValue(m_tax_code, json[QString("taxCode")]);
    m_tax_code_isSet = !json[QString("taxCode")].isNull() && m_tax_code_isValid;

    m_w4_form_year_isValid = ::OpenAPI::fromJsonValue(m_w4_form_year, json[QString("w4FormYear")]);
    m_w4_form_year_isSet = !json[QString("w4FormYear")].isNull() && m_w4_form_year_isValid;
}

QString OAIEmployee_primaryStateTax::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmployee_primaryStateTax::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_deductions_amount_isSet) {
        obj.insert(QString("deductionsAmount"), ::OpenAPI::toJsonValue(m_deductions_amount));
    }
    if (m_dependents_amount_isSet) {
        obj.insert(QString("dependentsAmount"), ::OpenAPI::toJsonValue(m_dependents_amount));
    }
    if (m_exemptions_isSet) {
        obj.insert(QString("exemptions"), ::OpenAPI::toJsonValue(m_exemptions));
    }
    if (m_exemptions2_isSet) {
        obj.insert(QString("exemptions2"), ::OpenAPI::toJsonValue(m_exemptions2));
    }
    if (m_filing_status_isSet) {
        obj.insert(QString("filingStatus"), ::OpenAPI::toJsonValue(m_filing_status));
    }
    if (m_higher_rate_isSet) {
        obj.insert(QString("higherRate"), ::OpenAPI::toJsonValue(m_higher_rate));
    }
    if (m_other_income_amount_isSet) {
        obj.insert(QString("otherIncomeAmount"), ::OpenAPI::toJsonValue(m_other_income_amount));
    }
    if (m_percentage_isSet) {
        obj.insert(QString("percentage"), ::OpenAPI::toJsonValue(m_percentage));
    }
    if (m_special_check_calc_isSet) {
        obj.insert(QString("specialCheckCalc"), ::OpenAPI::toJsonValue(m_special_check_calc));
    }
    if (m_tax_calculation_code_isSet) {
        obj.insert(QString("taxCalculationCode"), ::OpenAPI::toJsonValue(m_tax_calculation_code));
    }
    if (m_tax_code_isSet) {
        obj.insert(QString("taxCode"), ::OpenAPI::toJsonValue(m_tax_code));
    }
    if (m_w4_form_year_isSet) {
        obj.insert(QString("w4FormYear"), ::OpenAPI::toJsonValue(m_w4_form_year));
    }
    return obj;
}

double OAIEmployee_primaryStateTax::getAmount() const {
    return m_amount;
}
void OAIEmployee_primaryStateTax::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIEmployee_primaryStateTax::is_amount_Valid() const{
    return m_amount_isValid;
}

double OAIEmployee_primaryStateTax::getDeductionsAmount() const {
    return m_deductions_amount;
}
void OAIEmployee_primaryStateTax::setDeductionsAmount(const double &deductions_amount) {
    m_deductions_amount = deductions_amount;
    m_deductions_amount_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_deductions_amount_Set() const{
    return m_deductions_amount_isSet;
}

bool OAIEmployee_primaryStateTax::is_deductions_amount_Valid() const{
    return m_deductions_amount_isValid;
}

double OAIEmployee_primaryStateTax::getDependentsAmount() const {
    return m_dependents_amount;
}
void OAIEmployee_primaryStateTax::setDependentsAmount(const double &dependents_amount) {
    m_dependents_amount = dependents_amount;
    m_dependents_amount_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_dependents_amount_Set() const{
    return m_dependents_amount_isSet;
}

bool OAIEmployee_primaryStateTax::is_dependents_amount_Valid() const{
    return m_dependents_amount_isValid;
}

double OAIEmployee_primaryStateTax::getExemptions() const {
    return m_exemptions;
}
void OAIEmployee_primaryStateTax::setExemptions(const double &exemptions) {
    m_exemptions = exemptions;
    m_exemptions_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_exemptions_Set() const{
    return m_exemptions_isSet;
}

bool OAIEmployee_primaryStateTax::is_exemptions_Valid() const{
    return m_exemptions_isValid;
}

double OAIEmployee_primaryStateTax::getExemptions2() const {
    return m_exemptions2;
}
void OAIEmployee_primaryStateTax::setExemptions2(const double &exemptions2) {
    m_exemptions2 = exemptions2;
    m_exemptions2_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_exemptions2_Set() const{
    return m_exemptions2_isSet;
}

bool OAIEmployee_primaryStateTax::is_exemptions2_Valid() const{
    return m_exemptions2_isValid;
}

QString OAIEmployee_primaryStateTax::getFilingStatus() const {
    return m_filing_status;
}
void OAIEmployee_primaryStateTax::setFilingStatus(const QString &filing_status) {
    m_filing_status = filing_status;
    m_filing_status_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_filing_status_Set() const{
    return m_filing_status_isSet;
}

bool OAIEmployee_primaryStateTax::is_filing_status_Valid() const{
    return m_filing_status_isValid;
}

bool OAIEmployee_primaryStateTax::isHigherRate() const {
    return m_higher_rate;
}
void OAIEmployee_primaryStateTax::setHigherRate(const bool &higher_rate) {
    m_higher_rate = higher_rate;
    m_higher_rate_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_higher_rate_Set() const{
    return m_higher_rate_isSet;
}

bool OAIEmployee_primaryStateTax::is_higher_rate_Valid() const{
    return m_higher_rate_isValid;
}

double OAIEmployee_primaryStateTax::getOtherIncomeAmount() const {
    return m_other_income_amount;
}
void OAIEmployee_primaryStateTax::setOtherIncomeAmount(const double &other_income_amount) {
    m_other_income_amount = other_income_amount;
    m_other_income_amount_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_other_income_amount_Set() const{
    return m_other_income_amount_isSet;
}

bool OAIEmployee_primaryStateTax::is_other_income_amount_Valid() const{
    return m_other_income_amount_isValid;
}

double OAIEmployee_primaryStateTax::getPercentage() const {
    return m_percentage;
}
void OAIEmployee_primaryStateTax::setPercentage(const double &percentage) {
    m_percentage = percentage;
    m_percentage_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_percentage_Set() const{
    return m_percentage_isSet;
}

bool OAIEmployee_primaryStateTax::is_percentage_Valid() const{
    return m_percentage_isValid;
}

QString OAIEmployee_primaryStateTax::getSpecialCheckCalc() const {
    return m_special_check_calc;
}
void OAIEmployee_primaryStateTax::setSpecialCheckCalc(const QString &special_check_calc) {
    m_special_check_calc = special_check_calc;
    m_special_check_calc_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_special_check_calc_Set() const{
    return m_special_check_calc_isSet;
}

bool OAIEmployee_primaryStateTax::is_special_check_calc_Valid() const{
    return m_special_check_calc_isValid;
}

QString OAIEmployee_primaryStateTax::getTaxCalculationCode() const {
    return m_tax_calculation_code;
}
void OAIEmployee_primaryStateTax::setTaxCalculationCode(const QString &tax_calculation_code) {
    m_tax_calculation_code = tax_calculation_code;
    m_tax_calculation_code_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_tax_calculation_code_Set() const{
    return m_tax_calculation_code_isSet;
}

bool OAIEmployee_primaryStateTax::is_tax_calculation_code_Valid() const{
    return m_tax_calculation_code_isValid;
}

QString OAIEmployee_primaryStateTax::getTaxCode() const {
    return m_tax_code;
}
void OAIEmployee_primaryStateTax::setTaxCode(const QString &tax_code) {
    m_tax_code = tax_code;
    m_tax_code_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_tax_code_Set() const{
    return m_tax_code_isSet;
}

bool OAIEmployee_primaryStateTax::is_tax_code_Valid() const{
    return m_tax_code_isValid;
}

qint32 OAIEmployee_primaryStateTax::getW4FormYear() const {
    return m_w4_form_year;
}
void OAIEmployee_primaryStateTax::setW4FormYear(const qint32 &w4_form_year) {
    m_w4_form_year = w4_form_year;
    m_w4_form_year_isSet = true;
}

bool OAIEmployee_primaryStateTax::is_w4_form_year_Set() const{
    return m_w4_form_year_isSet;
}

bool OAIEmployee_primaryStateTax::is_w4_form_year_Valid() const{
    return m_w4_form_year_isValid;
}

bool OAIEmployee_primaryStateTax::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deductions_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dependents_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

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

        if (m_higher_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_other_income_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_special_check_calc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_calculation_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_w4_form_year_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEmployee_primaryStateTax::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
