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

/*
 * OAIEmergencyContact.h
 *
 * The emergency contact model
 */

#ifndef OAIEmergencyContact_H
#define OAIEmergencyContact_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEmergencyContact : public OAIObject {
public:
    OAIEmergencyContact();
    OAIEmergencyContact(QString json);
    ~OAIEmergencyContact() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddress1() const;
    void setAddress1(const QString &address1);
    bool is_address1_Set() const;
    bool is_address1_Valid() const;

    QString getAddress2() const;
    void setAddress2(const QString &address2);
    bool is_address2_Set() const;
    bool is_address2_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    QString getCounty() const;
    void setCounty(const QString &county);
    bool is_county_Set() const;
    bool is_county_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getHomePhone() const;
    void setHomePhone(const QString &home_phone);
    bool is_home_phone_Set() const;
    bool is_home_phone_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getMobilePhone() const;
    void setMobilePhone(const QString &mobile_phone);
    bool is_mobile_phone_Set() const;
    bool is_mobile_phone_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    QString getPager() const;
    void setPager(const QString &pager);
    bool is_pager_Set() const;
    bool is_pager_Valid() const;

    QString getPrimaryPhone() const;
    void setPrimaryPhone(const QString &primary_phone);
    bool is_primary_phone_Set() const;
    bool is_primary_phone_Valid() const;

    QString getPriority() const;
    void setPriority(const QString &priority);
    bool is_priority_Set() const;
    bool is_priority_Valid() const;

    QString getRelationship() const;
    void setRelationship(const QString &relationship);
    bool is_relationship_Set() const;
    bool is_relationship_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    bool isSyncEmployeeInfo() const;
    void setSyncEmployeeInfo(const bool &sync_employee_info);
    bool is_sync_employee_info_Set() const;
    bool is_sync_employee_info_Valid() const;

    QString getWorkExtension() const;
    void setWorkExtension(const QString &work_extension);
    bool is_work_extension_Set() const;
    bool is_work_extension_Valid() const;

    QString getWorkPhone() const;
    void setWorkPhone(const QString &work_phone);
    bool is_work_phone_Set() const;
    bool is_work_phone_Valid() const;

    QString getZip() const;
    void setZip(const QString &zip);
    bool is_zip_Set() const;
    bool is_zip_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address1;
    bool m_address1_isSet;
    bool m_address1_isValid;

    QString m_address2;
    bool m_address2_isSet;
    bool m_address2_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    QString m_county;
    bool m_county_isSet;
    bool m_county_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_home_phone;
    bool m_home_phone_isSet;
    bool m_home_phone_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_mobile_phone;
    bool m_mobile_phone_isSet;
    bool m_mobile_phone_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    QString m_pager;
    bool m_pager_isSet;
    bool m_pager_isValid;

    QString m_primary_phone;
    bool m_primary_phone_isSet;
    bool m_primary_phone_isValid;

    QString m_priority;
    bool m_priority_isSet;
    bool m_priority_isValid;

    QString m_relationship;
    bool m_relationship_isSet;
    bool m_relationship_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    bool m_sync_employee_info;
    bool m_sync_employee_info_isSet;
    bool m_sync_employee_info_isValid;

    QString m_work_extension;
    bool m_work_extension_isSet;
    bool m_work_extension_isValid;

    QString m_work_phone;
    bool m_work_phone_isSet;
    bool m_work_phone_isValid;

    QString m_zip;
    bool m_zip_isSet;
    bool m_zip_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEmergencyContact)

#endif // OAIEmergencyContact_H
