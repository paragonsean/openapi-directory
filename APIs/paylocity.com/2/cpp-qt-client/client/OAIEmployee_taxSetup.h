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
 * OAIEmployee_taxSetup.h
 *
 * Add tax form, 1099 exempt reasons and notes, and 943 agricultural employee information. Once the employee receives wages, this information cannot be updated. Add or update SUI tax state, retirement plan, and statutory information.
 */

#ifndef OAIEmployee_taxSetup_H
#define OAIEmployee_taxSetup_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEmployee_taxSetup : public OAIObject {
public:
    OAIEmployee_taxSetup();
    OAIEmployee_taxSetup(QString json);
    ~OAIEmployee_taxSetup() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFitwExemptNotes() const;
    void setFitwExemptNotes(const QString &fitw_exempt_notes);
    bool is_fitw_exempt_notes_Set() const;
    bool is_fitw_exempt_notes_Valid() const;

    QString getFitwExemptReason() const;
    void setFitwExemptReason(const QString &fitw_exempt_reason);
    bool is_fitw_exempt_reason_Set() const;
    bool is_fitw_exempt_reason_Valid() const;

    QString getFutaExemptNotes() const;
    void setFutaExemptNotes(const QString &futa_exempt_notes);
    bool is_futa_exempt_notes_Set() const;
    bool is_futa_exempt_notes_Valid() const;

    QString getFutaExemptReason() const;
    void setFutaExemptReason(const QString &futa_exempt_reason);
    bool is_futa_exempt_reason_Set() const;
    bool is_futa_exempt_reason_Valid() const;

    bool isIsEmployee943() const;
    void setIsEmployee943(const bool &is_employee943);
    bool is_is_employee943_Set() const;
    bool is_is_employee943_Valid() const;

    bool isIsPension() const;
    void setIsPension(const bool &is_pension);
    bool is_is_pension_Set() const;
    bool is_is_pension_Valid() const;

    bool isIsStatutory() const;
    void setIsStatutory(const bool &is_statutory);
    bool is_is_statutory_Set() const;
    bool is_is_statutory_Valid() const;

    QString getMedExemptNotes() const;
    void setMedExemptNotes(const QString &med_exempt_notes);
    bool is_med_exempt_notes_Set() const;
    bool is_med_exempt_notes_Valid() const;

    QString getMedExemptReason() const;
    void setMedExemptReason(const QString &med_exempt_reason);
    bool is_med_exempt_reason_Set() const;
    bool is_med_exempt_reason_Valid() const;

    QString getSitwExemptNotes() const;
    void setSitwExemptNotes(const QString &sitw_exempt_notes);
    bool is_sitw_exempt_notes_Set() const;
    bool is_sitw_exempt_notes_Valid() const;

    QString getSitwExemptReason() const;
    void setSitwExemptReason(const QString &sitw_exempt_reason);
    bool is_sitw_exempt_reason_Set() const;
    bool is_sitw_exempt_reason_Valid() const;

    QString getSsExemptNotes() const;
    void setSsExemptNotes(const QString &ss_exempt_notes);
    bool is_ss_exempt_notes_Set() const;
    bool is_ss_exempt_notes_Valid() const;

    QString getSsExemptReason() const;
    void setSsExemptReason(const QString &ss_exempt_reason);
    bool is_ss_exempt_reason_Set() const;
    bool is_ss_exempt_reason_Valid() const;

    QString getSuiExemptNotes() const;
    void setSuiExemptNotes(const QString &sui_exempt_notes);
    bool is_sui_exempt_notes_Set() const;
    bool is_sui_exempt_notes_Valid() const;

    QString getSuiExemptReason() const;
    void setSuiExemptReason(const QString &sui_exempt_reason);
    bool is_sui_exempt_reason_Set() const;
    bool is_sui_exempt_reason_Valid() const;

    QString getSuiState() const;
    void setSuiState(const QString &sui_state);
    bool is_sui_state_Set() const;
    bool is_sui_state_Valid() const;

    QString getTaxDistributionCode1099R() const;
    void setTaxDistributionCode1099R(const QString &tax_distribution_code1099_r);
    bool is_tax_distribution_code1099_r_Set() const;
    bool is_tax_distribution_code1099_r_Valid() const;

    QString getTaxForm() const;
    void setTaxForm(const QString &tax_form);
    bool is_tax_form_Set() const;
    bool is_tax_form_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_fitw_exempt_notes;
    bool m_fitw_exempt_notes_isSet;
    bool m_fitw_exempt_notes_isValid;

    QString m_fitw_exempt_reason;
    bool m_fitw_exempt_reason_isSet;
    bool m_fitw_exempt_reason_isValid;

    QString m_futa_exempt_notes;
    bool m_futa_exempt_notes_isSet;
    bool m_futa_exempt_notes_isValid;

    QString m_futa_exempt_reason;
    bool m_futa_exempt_reason_isSet;
    bool m_futa_exempt_reason_isValid;

    bool m_is_employee943;
    bool m_is_employee943_isSet;
    bool m_is_employee943_isValid;

    bool m_is_pension;
    bool m_is_pension_isSet;
    bool m_is_pension_isValid;

    bool m_is_statutory;
    bool m_is_statutory_isSet;
    bool m_is_statutory_isValid;

    QString m_med_exempt_notes;
    bool m_med_exempt_notes_isSet;
    bool m_med_exempt_notes_isValid;

    QString m_med_exempt_reason;
    bool m_med_exempt_reason_isSet;
    bool m_med_exempt_reason_isValid;

    QString m_sitw_exempt_notes;
    bool m_sitw_exempt_notes_isSet;
    bool m_sitw_exempt_notes_isValid;

    QString m_sitw_exempt_reason;
    bool m_sitw_exempt_reason_isSet;
    bool m_sitw_exempt_reason_isValid;

    QString m_ss_exempt_notes;
    bool m_ss_exempt_notes_isSet;
    bool m_ss_exempt_notes_isValid;

    QString m_ss_exempt_reason;
    bool m_ss_exempt_reason_isSet;
    bool m_ss_exempt_reason_isValid;

    QString m_sui_exempt_notes;
    bool m_sui_exempt_notes_isSet;
    bool m_sui_exempt_notes_isValid;

    QString m_sui_exempt_reason;
    bool m_sui_exempt_reason_isSet;
    bool m_sui_exempt_reason_isValid;

    QString m_sui_state;
    bool m_sui_state_isSet;
    bool m_sui_state_isValid;

    QString m_tax_distribution_code1099_r;
    bool m_tax_distribution_code1099_r_isSet;
    bool m_tax_distribution_code1099_r_isValid;

    QString m_tax_form;
    bool m_tax_form_isSet;
    bool m_tax_form_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEmployee_taxSetup)

#endif // OAIEmployee_taxSetup_H
