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

#include "OAIEmployee_emergencyContacts_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmployee_emergencyContacts_inner::OAIEmployee_emergencyContacts_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmployee_emergencyContacts_inner::OAIEmployee_emergencyContacts_inner() {
    this->initializeModel();
}

OAIEmployee_emergencyContacts_inner::~OAIEmployee_emergencyContacts_inner() {}

void OAIEmployee_emergencyContacts_inner::initializeModel() {

    m_address1_isSet = false;
    m_address1_isValid = false;

    m_address2_isSet = false;
    m_address2_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_county_isSet = false;
    m_county_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_home_phone_isSet = false;
    m_home_phone_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_mobile_phone_isSet = false;
    m_mobile_phone_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_pager_isSet = false;
    m_pager_isValid = false;

    m_primary_phone_isSet = false;
    m_primary_phone_isValid = false;

    m_priority_isSet = false;
    m_priority_isValid = false;

    m_relationship_isSet = false;
    m_relationship_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_sync_employee_info_isSet = false;
    m_sync_employee_info_isValid = false;

    m_work_extension_isSet = false;
    m_work_extension_isValid = false;

    m_work_phone_isSet = false;
    m_work_phone_isValid = false;

    m_zip_isSet = false;
    m_zip_isValid = false;
}

void OAIEmployee_emergencyContacts_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmployee_emergencyContacts_inner::fromJsonObject(QJsonObject json) {

    m_address1_isValid = ::OpenAPI::fromJsonValue(m_address1, json[QString("address1")]);
    m_address1_isSet = !json[QString("address1")].isNull() && m_address1_isValid;

    m_address2_isValid = ::OpenAPI::fromJsonValue(m_address2, json[QString("address2")]);
    m_address2_isSet = !json[QString("address2")].isNull() && m_address2_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_county_isValid = ::OpenAPI::fromJsonValue(m_county, json[QString("county")]);
    m_county_isSet = !json[QString("county")].isNull() && m_county_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_home_phone_isValid = ::OpenAPI::fromJsonValue(m_home_phone, json[QString("homePhone")]);
    m_home_phone_isSet = !json[QString("homePhone")].isNull() && m_home_phone_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_mobile_phone_isValid = ::OpenAPI::fromJsonValue(m_mobile_phone, json[QString("mobilePhone")]);
    m_mobile_phone_isSet = !json[QString("mobilePhone")].isNull() && m_mobile_phone_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_pager_isValid = ::OpenAPI::fromJsonValue(m_pager, json[QString("pager")]);
    m_pager_isSet = !json[QString("pager")].isNull() && m_pager_isValid;

    m_primary_phone_isValid = ::OpenAPI::fromJsonValue(m_primary_phone, json[QString("primaryPhone")]);
    m_primary_phone_isSet = !json[QString("primaryPhone")].isNull() && m_primary_phone_isValid;

    m_priority_isValid = ::OpenAPI::fromJsonValue(m_priority, json[QString("priority")]);
    m_priority_isSet = !json[QString("priority")].isNull() && m_priority_isValid;

    m_relationship_isValid = ::OpenAPI::fromJsonValue(m_relationship, json[QString("relationship")]);
    m_relationship_isSet = !json[QString("relationship")].isNull() && m_relationship_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_sync_employee_info_isValid = ::OpenAPI::fromJsonValue(m_sync_employee_info, json[QString("syncEmployeeInfo")]);
    m_sync_employee_info_isSet = !json[QString("syncEmployeeInfo")].isNull() && m_sync_employee_info_isValid;

    m_work_extension_isValid = ::OpenAPI::fromJsonValue(m_work_extension, json[QString("workExtension")]);
    m_work_extension_isSet = !json[QString("workExtension")].isNull() && m_work_extension_isValid;

    m_work_phone_isValid = ::OpenAPI::fromJsonValue(m_work_phone, json[QString("workPhone")]);
    m_work_phone_isSet = !json[QString("workPhone")].isNull() && m_work_phone_isValid;

    m_zip_isValid = ::OpenAPI::fromJsonValue(m_zip, json[QString("zip")]);
    m_zip_isSet = !json[QString("zip")].isNull() && m_zip_isValid;
}

QString OAIEmployee_emergencyContacts_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmployee_emergencyContacts_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_address1_isSet) {
        obj.insert(QString("address1"), ::OpenAPI::toJsonValue(m_address1));
    }
    if (m_address2_isSet) {
        obj.insert(QString("address2"), ::OpenAPI::toJsonValue(m_address2));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_county_isSet) {
        obj.insert(QString("county"), ::OpenAPI::toJsonValue(m_county));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_home_phone_isSet) {
        obj.insert(QString("homePhone"), ::OpenAPI::toJsonValue(m_home_phone));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_mobile_phone_isSet) {
        obj.insert(QString("mobilePhone"), ::OpenAPI::toJsonValue(m_mobile_phone));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_pager_isSet) {
        obj.insert(QString("pager"), ::OpenAPI::toJsonValue(m_pager));
    }
    if (m_primary_phone_isSet) {
        obj.insert(QString("primaryPhone"), ::OpenAPI::toJsonValue(m_primary_phone));
    }
    if (m_priority_isSet) {
        obj.insert(QString("priority"), ::OpenAPI::toJsonValue(m_priority));
    }
    if (m_relationship_isSet) {
        obj.insert(QString("relationship"), ::OpenAPI::toJsonValue(m_relationship));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_sync_employee_info_isSet) {
        obj.insert(QString("syncEmployeeInfo"), ::OpenAPI::toJsonValue(m_sync_employee_info));
    }
    if (m_work_extension_isSet) {
        obj.insert(QString("workExtension"), ::OpenAPI::toJsonValue(m_work_extension));
    }
    if (m_work_phone_isSet) {
        obj.insert(QString("workPhone"), ::OpenAPI::toJsonValue(m_work_phone));
    }
    if (m_zip_isSet) {
        obj.insert(QString("zip"), ::OpenAPI::toJsonValue(m_zip));
    }
    return obj;
}

QString OAIEmployee_emergencyContacts_inner::getAddress1() const {
    return m_address1;
}
void OAIEmployee_emergencyContacts_inner::setAddress1(const QString &address1) {
    m_address1 = address1;
    m_address1_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_address1_Set() const{
    return m_address1_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_address1_Valid() const{
    return m_address1_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getAddress2() const {
    return m_address2;
}
void OAIEmployee_emergencyContacts_inner::setAddress2(const QString &address2) {
    m_address2 = address2;
    m_address2_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_address2_Set() const{
    return m_address2_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_address2_Valid() const{
    return m_address2_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getCity() const {
    return m_city;
}
void OAIEmployee_emergencyContacts_inner::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_city_Set() const{
    return m_city_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getCountry() const {
    return m_country;
}
void OAIEmployee_emergencyContacts_inner::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_country_Set() const{
    return m_country_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getCounty() const {
    return m_county;
}
void OAIEmployee_emergencyContacts_inner::setCounty(const QString &county) {
    m_county = county;
    m_county_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_county_Set() const{
    return m_county_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_county_Valid() const{
    return m_county_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getEmail() const {
    return m_email;
}
void OAIEmployee_emergencyContacts_inner::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_email_Set() const{
    return m_email_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getFirstName() const {
    return m_first_name;
}
void OAIEmployee_emergencyContacts_inner::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getHomePhone() const {
    return m_home_phone;
}
void OAIEmployee_emergencyContacts_inner::setHomePhone(const QString &home_phone) {
    m_home_phone = home_phone;
    m_home_phone_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_home_phone_Set() const{
    return m_home_phone_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_home_phone_Valid() const{
    return m_home_phone_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getLastName() const {
    return m_last_name;
}
void OAIEmployee_emergencyContacts_inner::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getMobilePhone() const {
    return m_mobile_phone;
}
void OAIEmployee_emergencyContacts_inner::setMobilePhone(const QString &mobile_phone) {
    m_mobile_phone = mobile_phone;
    m_mobile_phone_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_mobile_phone_Set() const{
    return m_mobile_phone_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_mobile_phone_Valid() const{
    return m_mobile_phone_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getNotes() const {
    return m_notes;
}
void OAIEmployee_emergencyContacts_inner::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getPager() const {
    return m_pager;
}
void OAIEmployee_emergencyContacts_inner::setPager(const QString &pager) {
    m_pager = pager;
    m_pager_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_pager_Set() const{
    return m_pager_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_pager_Valid() const{
    return m_pager_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getPrimaryPhone() const {
    return m_primary_phone;
}
void OAIEmployee_emergencyContacts_inner::setPrimaryPhone(const QString &primary_phone) {
    m_primary_phone = primary_phone;
    m_primary_phone_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_primary_phone_Set() const{
    return m_primary_phone_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_primary_phone_Valid() const{
    return m_primary_phone_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getPriority() const {
    return m_priority;
}
void OAIEmployee_emergencyContacts_inner::setPriority(const QString &priority) {
    m_priority = priority;
    m_priority_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_priority_Set() const{
    return m_priority_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_priority_Valid() const{
    return m_priority_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getRelationship() const {
    return m_relationship;
}
void OAIEmployee_emergencyContacts_inner::setRelationship(const QString &relationship) {
    m_relationship = relationship;
    m_relationship_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_relationship_Set() const{
    return m_relationship_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_relationship_Valid() const{
    return m_relationship_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getState() const {
    return m_state;
}
void OAIEmployee_emergencyContacts_inner::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_state_Set() const{
    return m_state_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIEmployee_emergencyContacts_inner::isSyncEmployeeInfo() const {
    return m_sync_employee_info;
}
void OAIEmployee_emergencyContacts_inner::setSyncEmployeeInfo(const bool &sync_employee_info) {
    m_sync_employee_info = sync_employee_info;
    m_sync_employee_info_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_sync_employee_info_Set() const{
    return m_sync_employee_info_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_sync_employee_info_Valid() const{
    return m_sync_employee_info_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getWorkExtension() const {
    return m_work_extension;
}
void OAIEmployee_emergencyContacts_inner::setWorkExtension(const QString &work_extension) {
    m_work_extension = work_extension;
    m_work_extension_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_work_extension_Set() const{
    return m_work_extension_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_work_extension_Valid() const{
    return m_work_extension_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getWorkPhone() const {
    return m_work_phone;
}
void OAIEmployee_emergencyContacts_inner::setWorkPhone(const QString &work_phone) {
    m_work_phone = work_phone;
    m_work_phone_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_work_phone_Set() const{
    return m_work_phone_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_work_phone_Valid() const{
    return m_work_phone_isValid;
}

QString OAIEmployee_emergencyContacts_inner::getZip() const {
    return m_zip;
}
void OAIEmployee_emergencyContacts_inner::setZip(const QString &zip) {
    m_zip = zip;
    m_zip_isSet = true;
}

bool OAIEmployee_emergencyContacts_inner::is_zip_Set() const{
    return m_zip_isSet;
}

bool OAIEmployee_emergencyContacts_inner::is_zip_Valid() const{
    return m_zip_isValid;
}

bool OAIEmployee_emergencyContacts_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_address2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_county_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mobile_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pager_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relationship_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sync_employee_info_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_extension_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_work_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_zip_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEmployee_emergencyContacts_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_first_name_isValid && m_last_name_isValid && true;
}

} // namespace OpenAPI
