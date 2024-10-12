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
 * OAIStagedEmployee_nonPrimaryStateTax_inner.h
 *
 * The Non-Primary State Tax model
 */

#ifndef OAIStagedEmployee_nonPrimaryStateTax_inner_H
#define OAIStagedEmployee_nonPrimaryStateTax_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIStagedEmployee_nonPrimaryStateTax_inner : public OAIObject {
public:
    OAIStagedEmployee_nonPrimaryStateTax_inner();
    OAIStagedEmployee_nonPrimaryStateTax_inner(QString json);
    ~OAIStagedEmployee_nonPrimaryStateTax_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAmount() const;
    void setAmount(const double &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    double getDeductionsAmount() const;
    void setDeductionsAmount(const double &deductions_amount);
    bool is_deductions_amount_Set() const;
    bool is_deductions_amount_Valid() const;

    double getDependentsAmount() const;
    void setDependentsAmount(const double &dependents_amount);
    bool is_dependents_amount_Set() const;
    bool is_dependents_amount_Valid() const;

    double getExemptions() const;
    void setExemptions(const double &exemptions);
    bool is_exemptions_Set() const;
    bool is_exemptions_Valid() const;

    double getExemptions2() const;
    void setExemptions2(const double &exemptions2);
    bool is_exemptions2_Set() const;
    bool is_exemptions2_Valid() const;

    QString getFilingStatus() const;
    void setFilingStatus(const QString &filing_status);
    bool is_filing_status_Set() const;
    bool is_filing_status_Valid() const;

    bool isHigherRate() const;
    void setHigherRate(const bool &higher_rate);
    bool is_higher_rate_Set() const;
    bool is_higher_rate_Valid() const;

    double getOtherIncomeAmount() const;
    void setOtherIncomeAmount(const double &other_income_amount);
    bool is_other_income_amount_Set() const;
    bool is_other_income_amount_Valid() const;

    double getPercentage() const;
    void setPercentage(const double &percentage);
    bool is_percentage_Set() const;
    bool is_percentage_Valid() const;

    QString getReciprocityCode() const;
    void setReciprocityCode(const QString &reciprocity_code);
    bool is_reciprocity_code_Set() const;
    bool is_reciprocity_code_Valid() const;

    QString getSpecialCheckCalc() const;
    void setSpecialCheckCalc(const QString &special_check_calc);
    bool is_special_check_calc_Set() const;
    bool is_special_check_calc_Valid() const;

    QString getTaxCalculationCode() const;
    void setTaxCalculationCode(const QString &tax_calculation_code);
    bool is_tax_calculation_code_Set() const;
    bool is_tax_calculation_code_Valid() const;

    QString getTaxCode() const;
    void setTaxCode(const QString &tax_code);
    bool is_tax_code_Set() const;
    bool is_tax_code_Valid() const;

    qint32 getW4FormYear() const;
    void setW4FormYear(const qint32 &w4_form_year);
    bool is_w4_form_year_Set() const;
    bool is_w4_form_year_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    double m_deductions_amount;
    bool m_deductions_amount_isSet;
    bool m_deductions_amount_isValid;

    double m_dependents_amount;
    bool m_dependents_amount_isSet;
    bool m_dependents_amount_isValid;

    double m_exemptions;
    bool m_exemptions_isSet;
    bool m_exemptions_isValid;

    double m_exemptions2;
    bool m_exemptions2_isSet;
    bool m_exemptions2_isValid;

    QString m_filing_status;
    bool m_filing_status_isSet;
    bool m_filing_status_isValid;

    bool m_higher_rate;
    bool m_higher_rate_isSet;
    bool m_higher_rate_isValid;

    double m_other_income_amount;
    bool m_other_income_amount_isSet;
    bool m_other_income_amount_isValid;

    double m_percentage;
    bool m_percentage_isSet;
    bool m_percentage_isValid;

    QString m_reciprocity_code;
    bool m_reciprocity_code_isSet;
    bool m_reciprocity_code_isValid;

    QString m_special_check_calc;
    bool m_special_check_calc_isSet;
    bool m_special_check_calc_isValid;

    QString m_tax_calculation_code;
    bool m_tax_calculation_code_isSet;
    bool m_tax_calculation_code_isValid;

    QString m_tax_code;
    bool m_tax_code_isSet;
    bool m_tax_code_isValid;

    qint32 m_w4_form_year;
    bool m_w4_form_year_isSet;
    bool m_w4_form_year_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStagedEmployee_nonPrimaryStateTax_inner)

#endif // OAIStagedEmployee_nonPrimaryStateTax_inner_H
