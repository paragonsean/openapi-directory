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
 * OAIStagedEmployee_departmentPosition_inner.h
 *
 * The Department Position model
 */

#ifndef OAIStagedEmployee_departmentPosition_inner_H
#define OAIStagedEmployee_departmentPosition_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIStagedEmployee_departmentPosition_inner : public OAIObject {
public:
    OAIStagedEmployee_departmentPosition_inner();
    OAIStagedEmployee_departmentPosition_inner(QString json);
    ~OAIStagedEmployee_departmentPosition_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getChangeReason() const;
    void setChangeReason(const QString &change_reason);
    bool is_change_reason_Set() const;
    bool is_change_reason_Valid() const;

    QString getClockBadgeNumber() const;
    void setClockBadgeNumber(const QString &clock_badge_number);
    bool is_clock_badge_number_Set() const;
    bool is_clock_badge_number_Valid() const;

    QString getCostCenter1() const;
    void setCostCenter1(const QString &cost_center1);
    bool is_cost_center1_Set() const;
    bool is_cost_center1_Valid() const;

    QString getCostCenter2() const;
    void setCostCenter2(const QString &cost_center2);
    bool is_cost_center2_Set() const;
    bool is_cost_center2_Valid() const;

    QString getCostCenter3() const;
    void setCostCenter3(const QString &cost_center3);
    bool is_cost_center3_Set() const;
    bool is_cost_center3_Valid() const;

    QString getEffectiveDate() const;
    void setEffectiveDate(const QString &effective_date);
    bool is_effective_date_Set() const;
    bool is_effective_date_Valid() const;

    QString getEmployeeType() const;
    void setEmployeeType(const QString &employee_type);
    bool is_employee_type_Set() const;
    bool is_employee_type_Valid() const;

    QString getEqualEmploymentOpportunityClass() const;
    void setEqualEmploymentOpportunityClass(const QString &equal_employment_opportunity_class);
    bool is_equal_employment_opportunity_class_Set() const;
    bool is_equal_employment_opportunity_class_Valid() const;

    bool isIsMinimumWageExempt() const;
    void setIsMinimumWageExempt(const bool &is_minimum_wage_exempt);
    bool is_is_minimum_wage_exempt_Set() const;
    bool is_is_minimum_wage_exempt_Valid() const;

    bool isIsOvertimeExempt() const;
    void setIsOvertimeExempt(const bool &is_overtime_exempt);
    bool is_is_overtime_exempt_Set() const;
    bool is_is_overtime_exempt_Valid() const;

    bool isIsSupervisorReviewer() const;
    void setIsSupervisorReviewer(const bool &is_supervisor_reviewer);
    bool is_is_supervisor_reviewer_Set() const;
    bool is_is_supervisor_reviewer_Valid() const;

    bool isIsUnionDuesCollected() const;
    void setIsUnionDuesCollected(const bool &is_union_dues_collected);
    bool is_is_union_dues_collected_Set() const;
    bool is_is_union_dues_collected_Valid() const;

    bool isIsUnionInitiationCollected() const;
    void setIsUnionInitiationCollected(const bool &is_union_initiation_collected);
    bool is_is_union_initiation_collected_Set() const;
    bool is_is_union_initiation_collected_Valid() const;

    QString getJobTitle() const;
    void setJobTitle(const QString &job_title);
    bool is_job_title_Set() const;
    bool is_job_title_Valid() const;

    QString getPayGroup() const;
    void setPayGroup(const QString &pay_group);
    bool is_pay_group_Set() const;
    bool is_pay_group_Valid() const;

    QString getPositionCode() const;
    void setPositionCode(const QString &position_code);
    bool is_position_code_Set() const;
    bool is_position_code_Valid() const;

    QString getShift() const;
    void setShift(const QString &shift);
    bool is_shift_Set() const;
    bool is_shift_Valid() const;

    QString getSupervisorCompanyNumber() const;
    void setSupervisorCompanyNumber(const QString &supervisor_company_number);
    bool is_supervisor_company_number_Set() const;
    bool is_supervisor_company_number_Valid() const;

    QString getSupervisorEmployeeId() const;
    void setSupervisorEmployeeId(const QString &supervisor_employee_id);
    bool is_supervisor_employee_id_Set() const;
    bool is_supervisor_employee_id_Valid() const;

    QString getTipped() const;
    void setTipped(const QString &tipped);
    bool is_tipped_Set() const;
    bool is_tipped_Valid() const;

    QString getUnionAffiliationDate() const;
    void setUnionAffiliationDate(const QString &union_affiliation_date);
    bool is_union_affiliation_date_Set() const;
    bool is_union_affiliation_date_Valid() const;

    QString getUnionCode() const;
    void setUnionCode(const QString &union_code);
    bool is_union_code_Set() const;
    bool is_union_code_Valid() const;

    QString getUnionPosition() const;
    void setUnionPosition(const QString &union_position);
    bool is_union_position_Set() const;
    bool is_union_position_Valid() const;

    QString getWorkersCompensation() const;
    void setWorkersCompensation(const QString &workers_compensation);
    bool is_workers_compensation_Set() const;
    bool is_workers_compensation_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_change_reason;
    bool m_change_reason_isSet;
    bool m_change_reason_isValid;

    QString m_clock_badge_number;
    bool m_clock_badge_number_isSet;
    bool m_clock_badge_number_isValid;

    QString m_cost_center1;
    bool m_cost_center1_isSet;
    bool m_cost_center1_isValid;

    QString m_cost_center2;
    bool m_cost_center2_isSet;
    bool m_cost_center2_isValid;

    QString m_cost_center3;
    bool m_cost_center3_isSet;
    bool m_cost_center3_isValid;

    QString m_effective_date;
    bool m_effective_date_isSet;
    bool m_effective_date_isValid;

    QString m_employee_type;
    bool m_employee_type_isSet;
    bool m_employee_type_isValid;

    QString m_equal_employment_opportunity_class;
    bool m_equal_employment_opportunity_class_isSet;
    bool m_equal_employment_opportunity_class_isValid;

    bool m_is_minimum_wage_exempt;
    bool m_is_minimum_wage_exempt_isSet;
    bool m_is_minimum_wage_exempt_isValid;

    bool m_is_overtime_exempt;
    bool m_is_overtime_exempt_isSet;
    bool m_is_overtime_exempt_isValid;

    bool m_is_supervisor_reviewer;
    bool m_is_supervisor_reviewer_isSet;
    bool m_is_supervisor_reviewer_isValid;

    bool m_is_union_dues_collected;
    bool m_is_union_dues_collected_isSet;
    bool m_is_union_dues_collected_isValid;

    bool m_is_union_initiation_collected;
    bool m_is_union_initiation_collected_isSet;
    bool m_is_union_initiation_collected_isValid;

    QString m_job_title;
    bool m_job_title_isSet;
    bool m_job_title_isValid;

    QString m_pay_group;
    bool m_pay_group_isSet;
    bool m_pay_group_isValid;

    QString m_position_code;
    bool m_position_code_isSet;
    bool m_position_code_isValid;

    QString m_shift;
    bool m_shift_isSet;
    bool m_shift_isValid;

    QString m_supervisor_company_number;
    bool m_supervisor_company_number_isSet;
    bool m_supervisor_company_number_isValid;

    QString m_supervisor_employee_id;
    bool m_supervisor_employee_id_isSet;
    bool m_supervisor_employee_id_isValid;

    QString m_tipped;
    bool m_tipped_isSet;
    bool m_tipped_isValid;

    QString m_union_affiliation_date;
    bool m_union_affiliation_date_isSet;
    bool m_union_affiliation_date_isValid;

    QString m_union_code;
    bool m_union_code_isSet;
    bool m_union_code_isValid;

    QString m_union_position;
    bool m_union_position_isSet;
    bool m_union_position_isValid;

    QString m_workers_compensation;
    bool m_workers_compensation_isSet;
    bool m_workers_compensation_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStagedEmployee_departmentPosition_inner)

#endif // OAIStagedEmployee_departmentPosition_inner_H
