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

#include "OAIPayStatementSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayStatementSummary::OAIPayStatementSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayStatementSummary::OAIPayStatementSummary() {
    this->initializeModel();
}

OAIPayStatementSummary::~OAIPayStatementSummary() {}

void OAIPayStatementSummary::initializeModel() {

    m_auto_pay_isSet = false;
    m_auto_pay_isValid = false;

    m_begin_date_isSet = false;
    m_begin_date_isValid = false;

    m_check_date_isSet = false;
    m_check_date_isValid = false;

    m_check_number_isSet = false;
    m_check_number_isValid = false;

    m_direct_deposit_amount_isSet = false;
    m_direct_deposit_amount_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_gross_pay_isSet = false;
    m_gross_pay_isValid = false;

    m_hours_isSet = false;
    m_hours_isValid = false;

    m_net_check_isSet = false;
    m_net_check_isValid = false;

    m_net_pay_isSet = false;
    m_net_pay_isValid = false;

    m_overtime_dollars_isSet = false;
    m_overtime_dollars_isValid = false;

    m_overtime_hours_isSet = false;
    m_overtime_hours_isValid = false;

    m_process_isSet = false;
    m_process_isValid = false;

    m_regular_dollars_isSet = false;
    m_regular_dollars_isValid = false;

    m_regular_hours_isSet = false;
    m_regular_hours_isValid = false;

    m_transaction_number_isSet = false;
    m_transaction_number_isValid = false;

    m_voucher_number_isSet = false;
    m_voucher_number_isValid = false;

    m_workers_comp_code_isSet = false;
    m_workers_comp_code_isValid = false;

    m_year_isSet = false;
    m_year_isValid = false;
}

void OAIPayStatementSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayStatementSummary::fromJsonObject(QJsonObject json) {

    m_auto_pay_isValid = ::OpenAPI::fromJsonValue(m_auto_pay, json[QString("autoPay")]);
    m_auto_pay_isSet = !json[QString("autoPay")].isNull() && m_auto_pay_isValid;

    m_begin_date_isValid = ::OpenAPI::fromJsonValue(m_begin_date, json[QString("beginDate")]);
    m_begin_date_isSet = !json[QString("beginDate")].isNull() && m_begin_date_isValid;

    m_check_date_isValid = ::OpenAPI::fromJsonValue(m_check_date, json[QString("checkDate")]);
    m_check_date_isSet = !json[QString("checkDate")].isNull() && m_check_date_isValid;

    m_check_number_isValid = ::OpenAPI::fromJsonValue(m_check_number, json[QString("checkNumber")]);
    m_check_number_isSet = !json[QString("checkNumber")].isNull() && m_check_number_isValid;

    m_direct_deposit_amount_isValid = ::OpenAPI::fromJsonValue(m_direct_deposit_amount, json[QString("directDepositAmount")]);
    m_direct_deposit_amount_isSet = !json[QString("directDepositAmount")].isNull() && m_direct_deposit_amount_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("endDate")]);
    m_end_date_isSet = !json[QString("endDate")].isNull() && m_end_date_isValid;

    m_gross_pay_isValid = ::OpenAPI::fromJsonValue(m_gross_pay, json[QString("grossPay")]);
    m_gross_pay_isSet = !json[QString("grossPay")].isNull() && m_gross_pay_isValid;

    m_hours_isValid = ::OpenAPI::fromJsonValue(m_hours, json[QString("hours")]);
    m_hours_isSet = !json[QString("hours")].isNull() && m_hours_isValid;

    m_net_check_isValid = ::OpenAPI::fromJsonValue(m_net_check, json[QString("netCheck")]);
    m_net_check_isSet = !json[QString("netCheck")].isNull() && m_net_check_isValid;

    m_net_pay_isValid = ::OpenAPI::fromJsonValue(m_net_pay, json[QString("netPay")]);
    m_net_pay_isSet = !json[QString("netPay")].isNull() && m_net_pay_isValid;

    m_overtime_dollars_isValid = ::OpenAPI::fromJsonValue(m_overtime_dollars, json[QString("overtimeDollars")]);
    m_overtime_dollars_isSet = !json[QString("overtimeDollars")].isNull() && m_overtime_dollars_isValid;

    m_overtime_hours_isValid = ::OpenAPI::fromJsonValue(m_overtime_hours, json[QString("overtimeHours")]);
    m_overtime_hours_isSet = !json[QString("overtimeHours")].isNull() && m_overtime_hours_isValid;

    m_process_isValid = ::OpenAPI::fromJsonValue(m_process, json[QString("process")]);
    m_process_isSet = !json[QString("process")].isNull() && m_process_isValid;

    m_regular_dollars_isValid = ::OpenAPI::fromJsonValue(m_regular_dollars, json[QString("regularDollars")]);
    m_regular_dollars_isSet = !json[QString("regularDollars")].isNull() && m_regular_dollars_isValid;

    m_regular_hours_isValid = ::OpenAPI::fromJsonValue(m_regular_hours, json[QString("regularHours")]);
    m_regular_hours_isSet = !json[QString("regularHours")].isNull() && m_regular_hours_isValid;

    m_transaction_number_isValid = ::OpenAPI::fromJsonValue(m_transaction_number, json[QString("transactionNumber")]);
    m_transaction_number_isSet = !json[QString("transactionNumber")].isNull() && m_transaction_number_isValid;

    m_voucher_number_isValid = ::OpenAPI::fromJsonValue(m_voucher_number, json[QString("voucherNumber")]);
    m_voucher_number_isSet = !json[QString("voucherNumber")].isNull() && m_voucher_number_isValid;

    m_workers_comp_code_isValid = ::OpenAPI::fromJsonValue(m_workers_comp_code, json[QString("workersCompCode")]);
    m_workers_comp_code_isSet = !json[QString("workersCompCode")].isNull() && m_workers_comp_code_isValid;

    m_year_isValid = ::OpenAPI::fromJsonValue(m_year, json[QString("year")]);
    m_year_isSet = !json[QString("year")].isNull() && m_year_isValid;
}

QString OAIPayStatementSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayStatementSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_auto_pay_isSet) {
        obj.insert(QString("autoPay"), ::OpenAPI::toJsonValue(m_auto_pay));
    }
    if (m_begin_date_isSet) {
        obj.insert(QString("beginDate"), ::OpenAPI::toJsonValue(m_begin_date));
    }
    if (m_check_date_isSet) {
        obj.insert(QString("checkDate"), ::OpenAPI::toJsonValue(m_check_date));
    }
    if (m_check_number_isSet) {
        obj.insert(QString("checkNumber"), ::OpenAPI::toJsonValue(m_check_number));
    }
    if (m_direct_deposit_amount_isSet) {
        obj.insert(QString("directDepositAmount"), ::OpenAPI::toJsonValue(m_direct_deposit_amount));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("endDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_gross_pay_isSet) {
        obj.insert(QString("grossPay"), ::OpenAPI::toJsonValue(m_gross_pay));
    }
    if (m_hours_isSet) {
        obj.insert(QString("hours"), ::OpenAPI::toJsonValue(m_hours));
    }
    if (m_net_check_isSet) {
        obj.insert(QString("netCheck"), ::OpenAPI::toJsonValue(m_net_check));
    }
    if (m_net_pay_isSet) {
        obj.insert(QString("netPay"), ::OpenAPI::toJsonValue(m_net_pay));
    }
    if (m_overtime_dollars_isSet) {
        obj.insert(QString("overtimeDollars"), ::OpenAPI::toJsonValue(m_overtime_dollars));
    }
    if (m_overtime_hours_isSet) {
        obj.insert(QString("overtimeHours"), ::OpenAPI::toJsonValue(m_overtime_hours));
    }
    if (m_process_isSet) {
        obj.insert(QString("process"), ::OpenAPI::toJsonValue(m_process));
    }
    if (m_regular_dollars_isSet) {
        obj.insert(QString("regularDollars"), ::OpenAPI::toJsonValue(m_regular_dollars));
    }
    if (m_regular_hours_isSet) {
        obj.insert(QString("regularHours"), ::OpenAPI::toJsonValue(m_regular_hours));
    }
    if (m_transaction_number_isSet) {
        obj.insert(QString("transactionNumber"), ::OpenAPI::toJsonValue(m_transaction_number));
    }
    if (m_voucher_number_isSet) {
        obj.insert(QString("voucherNumber"), ::OpenAPI::toJsonValue(m_voucher_number));
    }
    if (m_workers_comp_code_isSet) {
        obj.insert(QString("workersCompCode"), ::OpenAPI::toJsonValue(m_workers_comp_code));
    }
    if (m_year_isSet) {
        obj.insert(QString("year"), ::OpenAPI::toJsonValue(m_year));
    }
    return obj;
}

bool OAIPayStatementSummary::isAutoPay() const {
    return m_auto_pay;
}
void OAIPayStatementSummary::setAutoPay(const bool &auto_pay) {
    m_auto_pay = auto_pay;
    m_auto_pay_isSet = true;
}

bool OAIPayStatementSummary::is_auto_pay_Set() const{
    return m_auto_pay_isSet;
}

bool OAIPayStatementSummary::is_auto_pay_Valid() const{
    return m_auto_pay_isValid;
}

QString OAIPayStatementSummary::getBeginDate() const {
    return m_begin_date;
}
void OAIPayStatementSummary::setBeginDate(const QString &begin_date) {
    m_begin_date = begin_date;
    m_begin_date_isSet = true;
}

bool OAIPayStatementSummary::is_begin_date_Set() const{
    return m_begin_date_isSet;
}

bool OAIPayStatementSummary::is_begin_date_Valid() const{
    return m_begin_date_isValid;
}

QString OAIPayStatementSummary::getCheckDate() const {
    return m_check_date;
}
void OAIPayStatementSummary::setCheckDate(const QString &check_date) {
    m_check_date = check_date;
    m_check_date_isSet = true;
}

bool OAIPayStatementSummary::is_check_date_Set() const{
    return m_check_date_isSet;
}

bool OAIPayStatementSummary::is_check_date_Valid() const{
    return m_check_date_isValid;
}

qint32 OAIPayStatementSummary::getCheckNumber() const {
    return m_check_number;
}
void OAIPayStatementSummary::setCheckNumber(const qint32 &check_number) {
    m_check_number = check_number;
    m_check_number_isSet = true;
}

bool OAIPayStatementSummary::is_check_number_Set() const{
    return m_check_number_isSet;
}

bool OAIPayStatementSummary::is_check_number_Valid() const{
    return m_check_number_isValid;
}

double OAIPayStatementSummary::getDirectDepositAmount() const {
    return m_direct_deposit_amount;
}
void OAIPayStatementSummary::setDirectDepositAmount(const double &direct_deposit_amount) {
    m_direct_deposit_amount = direct_deposit_amount;
    m_direct_deposit_amount_isSet = true;
}

bool OAIPayStatementSummary::is_direct_deposit_amount_Set() const{
    return m_direct_deposit_amount_isSet;
}

bool OAIPayStatementSummary::is_direct_deposit_amount_Valid() const{
    return m_direct_deposit_amount_isValid;
}

QString OAIPayStatementSummary::getEndDate() const {
    return m_end_date;
}
void OAIPayStatementSummary::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIPayStatementSummary::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIPayStatementSummary::is_end_date_Valid() const{
    return m_end_date_isValid;
}

double OAIPayStatementSummary::getGrossPay() const {
    return m_gross_pay;
}
void OAIPayStatementSummary::setGrossPay(const double &gross_pay) {
    m_gross_pay = gross_pay;
    m_gross_pay_isSet = true;
}

bool OAIPayStatementSummary::is_gross_pay_Set() const{
    return m_gross_pay_isSet;
}

bool OAIPayStatementSummary::is_gross_pay_Valid() const{
    return m_gross_pay_isValid;
}

double OAIPayStatementSummary::getHours() const {
    return m_hours;
}
void OAIPayStatementSummary::setHours(const double &hours) {
    m_hours = hours;
    m_hours_isSet = true;
}

bool OAIPayStatementSummary::is_hours_Set() const{
    return m_hours_isSet;
}

bool OAIPayStatementSummary::is_hours_Valid() const{
    return m_hours_isValid;
}

double OAIPayStatementSummary::getNetCheck() const {
    return m_net_check;
}
void OAIPayStatementSummary::setNetCheck(const double &net_check) {
    m_net_check = net_check;
    m_net_check_isSet = true;
}

bool OAIPayStatementSummary::is_net_check_Set() const{
    return m_net_check_isSet;
}

bool OAIPayStatementSummary::is_net_check_Valid() const{
    return m_net_check_isValid;
}

double OAIPayStatementSummary::getNetPay() const {
    return m_net_pay;
}
void OAIPayStatementSummary::setNetPay(const double &net_pay) {
    m_net_pay = net_pay;
    m_net_pay_isSet = true;
}

bool OAIPayStatementSummary::is_net_pay_Set() const{
    return m_net_pay_isSet;
}

bool OAIPayStatementSummary::is_net_pay_Valid() const{
    return m_net_pay_isValid;
}

double OAIPayStatementSummary::getOvertimeDollars() const {
    return m_overtime_dollars;
}
void OAIPayStatementSummary::setOvertimeDollars(const double &overtime_dollars) {
    m_overtime_dollars = overtime_dollars;
    m_overtime_dollars_isSet = true;
}

bool OAIPayStatementSummary::is_overtime_dollars_Set() const{
    return m_overtime_dollars_isSet;
}

bool OAIPayStatementSummary::is_overtime_dollars_Valid() const{
    return m_overtime_dollars_isValid;
}

double OAIPayStatementSummary::getOvertimeHours() const {
    return m_overtime_hours;
}
void OAIPayStatementSummary::setOvertimeHours(const double &overtime_hours) {
    m_overtime_hours = overtime_hours;
    m_overtime_hours_isSet = true;
}

bool OAIPayStatementSummary::is_overtime_hours_Set() const{
    return m_overtime_hours_isSet;
}

bool OAIPayStatementSummary::is_overtime_hours_Valid() const{
    return m_overtime_hours_isValid;
}

qint32 OAIPayStatementSummary::getProcess() const {
    return m_process;
}
void OAIPayStatementSummary::setProcess(const qint32 &process) {
    m_process = process;
    m_process_isSet = true;
}

bool OAIPayStatementSummary::is_process_Set() const{
    return m_process_isSet;
}

bool OAIPayStatementSummary::is_process_Valid() const{
    return m_process_isValid;
}

double OAIPayStatementSummary::getRegularDollars() const {
    return m_regular_dollars;
}
void OAIPayStatementSummary::setRegularDollars(const double &regular_dollars) {
    m_regular_dollars = regular_dollars;
    m_regular_dollars_isSet = true;
}

bool OAIPayStatementSummary::is_regular_dollars_Set() const{
    return m_regular_dollars_isSet;
}

bool OAIPayStatementSummary::is_regular_dollars_Valid() const{
    return m_regular_dollars_isValid;
}

double OAIPayStatementSummary::getRegularHours() const {
    return m_regular_hours;
}
void OAIPayStatementSummary::setRegularHours(const double &regular_hours) {
    m_regular_hours = regular_hours;
    m_regular_hours_isSet = true;
}

bool OAIPayStatementSummary::is_regular_hours_Set() const{
    return m_regular_hours_isSet;
}

bool OAIPayStatementSummary::is_regular_hours_Valid() const{
    return m_regular_hours_isValid;
}

qint32 OAIPayStatementSummary::getTransactionNumber() const {
    return m_transaction_number;
}
void OAIPayStatementSummary::setTransactionNumber(const qint32 &transaction_number) {
    m_transaction_number = transaction_number;
    m_transaction_number_isSet = true;
}

bool OAIPayStatementSummary::is_transaction_number_Set() const{
    return m_transaction_number_isSet;
}

bool OAIPayStatementSummary::is_transaction_number_Valid() const{
    return m_transaction_number_isValid;
}

qint32 OAIPayStatementSummary::getVoucherNumber() const {
    return m_voucher_number;
}
void OAIPayStatementSummary::setVoucherNumber(const qint32 &voucher_number) {
    m_voucher_number = voucher_number;
    m_voucher_number_isSet = true;
}

bool OAIPayStatementSummary::is_voucher_number_Set() const{
    return m_voucher_number_isSet;
}

bool OAIPayStatementSummary::is_voucher_number_Valid() const{
    return m_voucher_number_isValid;
}

QString OAIPayStatementSummary::getWorkersCompCode() const {
    return m_workers_comp_code;
}
void OAIPayStatementSummary::setWorkersCompCode(const QString &workers_comp_code) {
    m_workers_comp_code = workers_comp_code;
    m_workers_comp_code_isSet = true;
}

bool OAIPayStatementSummary::is_workers_comp_code_Set() const{
    return m_workers_comp_code_isSet;
}

bool OAIPayStatementSummary::is_workers_comp_code_Valid() const{
    return m_workers_comp_code_isValid;
}

qint32 OAIPayStatementSummary::getYear() const {
    return m_year;
}
void OAIPayStatementSummary::setYear(const qint32 &year) {
    m_year = year;
    m_year_isSet = true;
}

bool OAIPayStatementSummary::is_year_Set() const{
    return m_year_isSet;
}

bool OAIPayStatementSummary::is_year_Valid() const{
    return m_year_isValid;
}

bool OAIPayStatementSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auto_pay_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_begin_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_check_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_direct_deposit_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gross_pay_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_check_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_pay_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_overtime_dollars_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_overtime_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_process_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_regular_dollars_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_regular_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_voucher_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_workers_comp_code_isSet) {
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

bool OAIPayStatementSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
