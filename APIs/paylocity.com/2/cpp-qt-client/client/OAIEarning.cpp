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

#include "OAIEarning.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEarning::OAIEarning(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEarning::OAIEarning() {
    this->initializeModel();
}

OAIEarning::~OAIEarning() {}

void OAIEarning::initializeModel() {

    m_agency_isSet = false;
    m_agency_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_annual_maximum_isSet = false;
    m_annual_maximum_isValid = false;

    m_calculation_code_isSet = false;
    m_calculation_code_isValid = false;

    m_cost_center1_isSet = false;
    m_cost_center1_isValid = false;

    m_cost_center2_isSet = false;
    m_cost_center2_isValid = false;

    m_cost_center3_isSet = false;
    m_cost_center3_isValid = false;

    m_earning_code_isSet = false;
    m_earning_code_isValid = false;

    m_effective_date_isSet = false;
    m_effective_date_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_frequency_isSet = false;
    m_frequency_isValid = false;

    m_goal_isSet = false;
    m_goal_isValid = false;

    m_hours_or_units_isSet = false;
    m_hours_or_units_isValid = false;

    m_is_self_insured_isSet = false;
    m_is_self_insured_isValid = false;

    m_job_code_isSet = false;
    m_job_code_isValid = false;

    m_miscellaneous_info_isSet = false;
    m_miscellaneous_info_isValid = false;

    m_paid_towards_goal_isSet = false;
    m_paid_towards_goal_isValid = false;

    m_pay_period_maximum_isSet = false;
    m_pay_period_maximum_isValid = false;

    m_pay_period_minimum_isSet = false;
    m_pay_period_minimum_isValid = false;

    m_rate_isSet = false;
    m_rate_isValid = false;

    m_rate_code_isSet = false;
    m_rate_code_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;
}

void OAIEarning::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEarning::fromJsonObject(QJsonObject json) {

    m_agency_isValid = ::OpenAPI::fromJsonValue(m_agency, json[QString("agency")]);
    m_agency_isSet = !json[QString("agency")].isNull() && m_agency_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_annual_maximum_isValid = ::OpenAPI::fromJsonValue(m_annual_maximum, json[QString("annualMaximum")]);
    m_annual_maximum_isSet = !json[QString("annualMaximum")].isNull() && m_annual_maximum_isValid;

    m_calculation_code_isValid = ::OpenAPI::fromJsonValue(m_calculation_code, json[QString("calculationCode")]);
    m_calculation_code_isSet = !json[QString("calculationCode")].isNull() && m_calculation_code_isValid;

    m_cost_center1_isValid = ::OpenAPI::fromJsonValue(m_cost_center1, json[QString("costCenter1")]);
    m_cost_center1_isSet = !json[QString("costCenter1")].isNull() && m_cost_center1_isValid;

    m_cost_center2_isValid = ::OpenAPI::fromJsonValue(m_cost_center2, json[QString("costCenter2")]);
    m_cost_center2_isSet = !json[QString("costCenter2")].isNull() && m_cost_center2_isValid;

    m_cost_center3_isValid = ::OpenAPI::fromJsonValue(m_cost_center3, json[QString("costCenter3")]);
    m_cost_center3_isSet = !json[QString("costCenter3")].isNull() && m_cost_center3_isValid;

    m_earning_code_isValid = ::OpenAPI::fromJsonValue(m_earning_code, json[QString("earningCode")]);
    m_earning_code_isSet = !json[QString("earningCode")].isNull() && m_earning_code_isValid;

    m_effective_date_isValid = ::OpenAPI::fromJsonValue(m_effective_date, json[QString("effectiveDate")]);
    m_effective_date_isSet = !json[QString("effectiveDate")].isNull() && m_effective_date_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("endDate")]);
    m_end_date_isSet = !json[QString("endDate")].isNull() && m_end_date_isValid;

    m_frequency_isValid = ::OpenAPI::fromJsonValue(m_frequency, json[QString("frequency")]);
    m_frequency_isSet = !json[QString("frequency")].isNull() && m_frequency_isValid;

    m_goal_isValid = ::OpenAPI::fromJsonValue(m_goal, json[QString("goal")]);
    m_goal_isSet = !json[QString("goal")].isNull() && m_goal_isValid;

    m_hours_or_units_isValid = ::OpenAPI::fromJsonValue(m_hours_or_units, json[QString("hoursOrUnits")]);
    m_hours_or_units_isSet = !json[QString("hoursOrUnits")].isNull() && m_hours_or_units_isValid;

    m_is_self_insured_isValid = ::OpenAPI::fromJsonValue(m_is_self_insured, json[QString("isSelfInsured")]);
    m_is_self_insured_isSet = !json[QString("isSelfInsured")].isNull() && m_is_self_insured_isValid;

    m_job_code_isValid = ::OpenAPI::fromJsonValue(m_job_code, json[QString("jobCode")]);
    m_job_code_isSet = !json[QString("jobCode")].isNull() && m_job_code_isValid;

    m_miscellaneous_info_isValid = ::OpenAPI::fromJsonValue(m_miscellaneous_info, json[QString("miscellaneousInfo")]);
    m_miscellaneous_info_isSet = !json[QString("miscellaneousInfo")].isNull() && m_miscellaneous_info_isValid;

    m_paid_towards_goal_isValid = ::OpenAPI::fromJsonValue(m_paid_towards_goal, json[QString("paidTowardsGoal")]);
    m_paid_towards_goal_isSet = !json[QString("paidTowardsGoal")].isNull() && m_paid_towards_goal_isValid;

    m_pay_period_maximum_isValid = ::OpenAPI::fromJsonValue(m_pay_period_maximum, json[QString("payPeriodMaximum")]);
    m_pay_period_maximum_isSet = !json[QString("payPeriodMaximum")].isNull() && m_pay_period_maximum_isValid;

    m_pay_period_minimum_isValid = ::OpenAPI::fromJsonValue(m_pay_period_minimum, json[QString("payPeriodMinimum")]);
    m_pay_period_minimum_isSet = !json[QString("payPeriodMinimum")].isNull() && m_pay_period_minimum_isValid;

    m_rate_isValid = ::OpenAPI::fromJsonValue(m_rate, json[QString("rate")]);
    m_rate_isSet = !json[QString("rate")].isNull() && m_rate_isValid;

    m_rate_code_isValid = ::OpenAPI::fromJsonValue(m_rate_code, json[QString("rateCode")]);
    m_rate_code_isSet = !json[QString("rateCode")].isNull() && m_rate_code_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("startDate")]);
    m_start_date_isSet = !json[QString("startDate")].isNull() && m_start_date_isValid;
}

QString OAIEarning::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEarning::asJsonObject() const {
    QJsonObject obj;
    if (m_agency_isSet) {
        obj.insert(QString("agency"), ::OpenAPI::toJsonValue(m_agency));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_annual_maximum_isSet) {
        obj.insert(QString("annualMaximum"), ::OpenAPI::toJsonValue(m_annual_maximum));
    }
    if (m_calculation_code_isSet) {
        obj.insert(QString("calculationCode"), ::OpenAPI::toJsonValue(m_calculation_code));
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
    if (m_earning_code_isSet) {
        obj.insert(QString("earningCode"), ::OpenAPI::toJsonValue(m_earning_code));
    }
    if (m_effective_date_isSet) {
        obj.insert(QString("effectiveDate"), ::OpenAPI::toJsonValue(m_effective_date));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("endDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_frequency_isSet) {
        obj.insert(QString("frequency"), ::OpenAPI::toJsonValue(m_frequency));
    }
    if (m_goal_isSet) {
        obj.insert(QString("goal"), ::OpenAPI::toJsonValue(m_goal));
    }
    if (m_hours_or_units_isSet) {
        obj.insert(QString("hoursOrUnits"), ::OpenAPI::toJsonValue(m_hours_or_units));
    }
    if (m_is_self_insured_isSet) {
        obj.insert(QString("isSelfInsured"), ::OpenAPI::toJsonValue(m_is_self_insured));
    }
    if (m_job_code_isSet) {
        obj.insert(QString("jobCode"), ::OpenAPI::toJsonValue(m_job_code));
    }
    if (m_miscellaneous_info_isSet) {
        obj.insert(QString("miscellaneousInfo"), ::OpenAPI::toJsonValue(m_miscellaneous_info));
    }
    if (m_paid_towards_goal_isSet) {
        obj.insert(QString("paidTowardsGoal"), ::OpenAPI::toJsonValue(m_paid_towards_goal));
    }
    if (m_pay_period_maximum_isSet) {
        obj.insert(QString("payPeriodMaximum"), ::OpenAPI::toJsonValue(m_pay_period_maximum));
    }
    if (m_pay_period_minimum_isSet) {
        obj.insert(QString("payPeriodMinimum"), ::OpenAPI::toJsonValue(m_pay_period_minimum));
    }
    if (m_rate_isSet) {
        obj.insert(QString("rate"), ::OpenAPI::toJsonValue(m_rate));
    }
    if (m_rate_code_isSet) {
        obj.insert(QString("rateCode"), ::OpenAPI::toJsonValue(m_rate_code));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("startDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    return obj;
}

QString OAIEarning::getAgency() const {
    return m_agency;
}
void OAIEarning::setAgency(const QString &agency) {
    m_agency = agency;
    m_agency_isSet = true;
}

bool OAIEarning::is_agency_Set() const{
    return m_agency_isSet;
}

bool OAIEarning::is_agency_Valid() const{
    return m_agency_isValid;
}

double OAIEarning::getAmount() const {
    return m_amount;
}
void OAIEarning::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIEarning::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIEarning::is_amount_Valid() const{
    return m_amount_isValid;
}

double OAIEarning::getAnnualMaximum() const {
    return m_annual_maximum;
}
void OAIEarning::setAnnualMaximum(const double &annual_maximum) {
    m_annual_maximum = annual_maximum;
    m_annual_maximum_isSet = true;
}

bool OAIEarning::is_annual_maximum_Set() const{
    return m_annual_maximum_isSet;
}

bool OAIEarning::is_annual_maximum_Valid() const{
    return m_annual_maximum_isValid;
}

QString OAIEarning::getCalculationCode() const {
    return m_calculation_code;
}
void OAIEarning::setCalculationCode(const QString &calculation_code) {
    m_calculation_code = calculation_code;
    m_calculation_code_isSet = true;
}

bool OAIEarning::is_calculation_code_Set() const{
    return m_calculation_code_isSet;
}

bool OAIEarning::is_calculation_code_Valid() const{
    return m_calculation_code_isValid;
}

QString OAIEarning::getCostCenter1() const {
    return m_cost_center1;
}
void OAIEarning::setCostCenter1(const QString &cost_center1) {
    m_cost_center1 = cost_center1;
    m_cost_center1_isSet = true;
}

bool OAIEarning::is_cost_center1_Set() const{
    return m_cost_center1_isSet;
}

bool OAIEarning::is_cost_center1_Valid() const{
    return m_cost_center1_isValid;
}

QString OAIEarning::getCostCenter2() const {
    return m_cost_center2;
}
void OAIEarning::setCostCenter2(const QString &cost_center2) {
    m_cost_center2 = cost_center2;
    m_cost_center2_isSet = true;
}

bool OAIEarning::is_cost_center2_Set() const{
    return m_cost_center2_isSet;
}

bool OAIEarning::is_cost_center2_Valid() const{
    return m_cost_center2_isValid;
}

QString OAIEarning::getCostCenter3() const {
    return m_cost_center3;
}
void OAIEarning::setCostCenter3(const QString &cost_center3) {
    m_cost_center3 = cost_center3;
    m_cost_center3_isSet = true;
}

bool OAIEarning::is_cost_center3_Set() const{
    return m_cost_center3_isSet;
}

bool OAIEarning::is_cost_center3_Valid() const{
    return m_cost_center3_isValid;
}

QString OAIEarning::getEarningCode() const {
    return m_earning_code;
}
void OAIEarning::setEarningCode(const QString &earning_code) {
    m_earning_code = earning_code;
    m_earning_code_isSet = true;
}

bool OAIEarning::is_earning_code_Set() const{
    return m_earning_code_isSet;
}

bool OAIEarning::is_earning_code_Valid() const{
    return m_earning_code_isValid;
}

QString OAIEarning::getEffectiveDate() const {
    return m_effective_date;
}
void OAIEarning::setEffectiveDate(const QString &effective_date) {
    m_effective_date = effective_date;
    m_effective_date_isSet = true;
}

bool OAIEarning::is_effective_date_Set() const{
    return m_effective_date_isSet;
}

bool OAIEarning::is_effective_date_Valid() const{
    return m_effective_date_isValid;
}

QString OAIEarning::getEndDate() const {
    return m_end_date;
}
void OAIEarning::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIEarning::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIEarning::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAIEarning::getFrequency() const {
    return m_frequency;
}
void OAIEarning::setFrequency(const QString &frequency) {
    m_frequency = frequency;
    m_frequency_isSet = true;
}

bool OAIEarning::is_frequency_Set() const{
    return m_frequency_isSet;
}

bool OAIEarning::is_frequency_Valid() const{
    return m_frequency_isValid;
}

double OAIEarning::getGoal() const {
    return m_goal;
}
void OAIEarning::setGoal(const double &goal) {
    m_goal = goal;
    m_goal_isSet = true;
}

bool OAIEarning::is_goal_Set() const{
    return m_goal_isSet;
}

bool OAIEarning::is_goal_Valid() const{
    return m_goal_isValid;
}

double OAIEarning::getHoursOrUnits() const {
    return m_hours_or_units;
}
void OAIEarning::setHoursOrUnits(const double &hours_or_units) {
    m_hours_or_units = hours_or_units;
    m_hours_or_units_isSet = true;
}

bool OAIEarning::is_hours_or_units_Set() const{
    return m_hours_or_units_isSet;
}

bool OAIEarning::is_hours_or_units_Valid() const{
    return m_hours_or_units_isValid;
}

bool OAIEarning::isIsSelfInsured() const {
    return m_is_self_insured;
}
void OAIEarning::setIsSelfInsured(const bool &is_self_insured) {
    m_is_self_insured = is_self_insured;
    m_is_self_insured_isSet = true;
}

bool OAIEarning::is_is_self_insured_Set() const{
    return m_is_self_insured_isSet;
}

bool OAIEarning::is_is_self_insured_Valid() const{
    return m_is_self_insured_isValid;
}

QString OAIEarning::getJobCode() const {
    return m_job_code;
}
void OAIEarning::setJobCode(const QString &job_code) {
    m_job_code = job_code;
    m_job_code_isSet = true;
}

bool OAIEarning::is_job_code_Set() const{
    return m_job_code_isSet;
}

bool OAIEarning::is_job_code_Valid() const{
    return m_job_code_isValid;
}

QString OAIEarning::getMiscellaneousInfo() const {
    return m_miscellaneous_info;
}
void OAIEarning::setMiscellaneousInfo(const QString &miscellaneous_info) {
    m_miscellaneous_info = miscellaneous_info;
    m_miscellaneous_info_isSet = true;
}

bool OAIEarning::is_miscellaneous_info_Set() const{
    return m_miscellaneous_info_isSet;
}

bool OAIEarning::is_miscellaneous_info_Valid() const{
    return m_miscellaneous_info_isValid;
}

double OAIEarning::getPaidTowardsGoal() const {
    return m_paid_towards_goal;
}
void OAIEarning::setPaidTowardsGoal(const double &paid_towards_goal) {
    m_paid_towards_goal = paid_towards_goal;
    m_paid_towards_goal_isSet = true;
}

bool OAIEarning::is_paid_towards_goal_Set() const{
    return m_paid_towards_goal_isSet;
}

bool OAIEarning::is_paid_towards_goal_Valid() const{
    return m_paid_towards_goal_isValid;
}

double OAIEarning::getPayPeriodMaximum() const {
    return m_pay_period_maximum;
}
void OAIEarning::setPayPeriodMaximum(const double &pay_period_maximum) {
    m_pay_period_maximum = pay_period_maximum;
    m_pay_period_maximum_isSet = true;
}

bool OAIEarning::is_pay_period_maximum_Set() const{
    return m_pay_period_maximum_isSet;
}

bool OAIEarning::is_pay_period_maximum_Valid() const{
    return m_pay_period_maximum_isValid;
}

double OAIEarning::getPayPeriodMinimum() const {
    return m_pay_period_minimum;
}
void OAIEarning::setPayPeriodMinimum(const double &pay_period_minimum) {
    m_pay_period_minimum = pay_period_minimum;
    m_pay_period_minimum_isSet = true;
}

bool OAIEarning::is_pay_period_minimum_Set() const{
    return m_pay_period_minimum_isSet;
}

bool OAIEarning::is_pay_period_minimum_Valid() const{
    return m_pay_period_minimum_isValid;
}

double OAIEarning::getRate() const {
    return m_rate;
}
void OAIEarning::setRate(const double &rate) {
    m_rate = rate;
    m_rate_isSet = true;
}

bool OAIEarning::is_rate_Set() const{
    return m_rate_isSet;
}

bool OAIEarning::is_rate_Valid() const{
    return m_rate_isValid;
}

QString OAIEarning::getRateCode() const {
    return m_rate_code;
}
void OAIEarning::setRateCode(const QString &rate_code) {
    m_rate_code = rate_code;
    m_rate_code_isSet = true;
}

bool OAIEarning::is_rate_code_Set() const{
    return m_rate_code_isSet;
}

bool OAIEarning::is_rate_code_Valid() const{
    return m_rate_code_isValid;
}

QString OAIEarning::getStartDate() const {
    return m_start_date;
}
void OAIEarning::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIEarning::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIEarning::is_start_date_Valid() const{
    return m_start_date_isValid;
}

bool OAIEarning::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_agency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_annual_maximum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_calculation_code_isSet) {
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

        if (m_earning_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_effective_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_frequency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_goal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hours_or_units_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_self_insured_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_miscellaneous_info_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_paid_towards_goal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pay_period_maximum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pay_period_minimum_isSet) {
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

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEarning::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_earning_code_isValid && m_start_date_isValid && true;
}

} // namespace OpenAPI
