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
 * OAIStagedEmployee.h
 *
 * The staged employee model
 */

#ifndef OAIStagedEmployee_H
#define OAIStagedEmployee_H

#include <QJsonObject>

#include "OAIEmployee_customBooleanFields_inner.h"
#include "OAIEmployee_customDateFields_inner.h"
#include "OAIEmployee_customDropDownFields_inner.h"
#include "OAIEmployee_customNumberFields_inner.h"
#include "OAIEmployee_customTextFields_inner.h"
#include "OAIEmployee_localTax_inner.h"
#include "OAIStagedEmployee_additionalDirectDeposit_inner.h"
#include "OAIStagedEmployee_benefitSetup_inner.h"
#include "OAIStagedEmployee_departmentPosition_inner.h"
#include "OAIStagedEmployee_federalTax_inner.h"
#include "OAIStagedEmployee_homeAddress_inner.h"
#include "OAIStagedEmployee_mainDirectDeposit_inner.h"
#include "OAIStagedEmployee_nonPrimaryStateTax_inner.h"
#include "OAIStagedEmployee_primaryPayRate_inner.h"
#include "OAIStagedEmployee_primaryStateTax_inner.h"
#include "OAIStagedEmployee_status_inner.h"
#include "OAIStagedEmployee_webTime.h"
#include "OAIStagedEmployee_workAddress_inner.h"
#include "OAIStagedEmployee_workEligibility_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIStagedEmployee_additionalDirectDeposit_inner;
class OAIStagedEmployee_benefitSetup_inner;
class OAIEmployee_customBooleanFields_inner;
class OAIEmployee_customDateFields_inner;
class OAIEmployee_customDropDownFields_inner;
class OAIEmployee_customNumberFields_inner;
class OAIEmployee_customTextFields_inner;
class OAIStagedEmployee_departmentPosition_inner;
class OAIStagedEmployee_federalTax_inner;
class OAIStagedEmployee_homeAddress_inner;
class OAIEmployee_localTax_inner;
class OAIStagedEmployee_mainDirectDeposit_inner;
class OAIStagedEmployee_nonPrimaryStateTax_inner;
class OAIStagedEmployee_primaryPayRate_inner;
class OAIStagedEmployee_primaryStateTax_inner;
class OAIStagedEmployee_status_inner;
class OAIStagedEmployee_webTime;
class OAIStagedEmployee_workAddress_inner;
class OAIStagedEmployee_workEligibility_inner;

class OAIStagedEmployee : public OAIObject {
public:
    OAIStagedEmployee();
    OAIStagedEmployee(QString json);
    ~OAIStagedEmployee() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIStagedEmployee_additionalDirectDeposit_inner> getAdditionalDirectDeposit() const;
    void setAdditionalDirectDeposit(const QList<OAIStagedEmployee_additionalDirectDeposit_inner> &additional_direct_deposit);
    bool is_additional_direct_deposit_Set() const;
    bool is_additional_direct_deposit_Valid() const;

    QList<OAIStagedEmployee_benefitSetup_inner> getBenefitSetup() const;
    void setBenefitSetup(const QList<OAIStagedEmployee_benefitSetup_inner> &benefit_setup);
    bool is_benefit_setup_Set() const;
    bool is_benefit_setup_Valid() const;

    QString getBirthDate() const;
    void setBirthDate(const QString &birth_date);
    bool is_birth_date_Set() const;
    bool is_birth_date_Valid() const;

    QList<OAIEmployee_customBooleanFields_inner> getCustomBooleanFields() const;
    void setCustomBooleanFields(const QList<OAIEmployee_customBooleanFields_inner> &custom_boolean_fields);
    bool is_custom_boolean_fields_Set() const;
    bool is_custom_boolean_fields_Valid() const;

    QList<OAIEmployee_customDateFields_inner> getCustomDateFields() const;
    void setCustomDateFields(const QList<OAIEmployee_customDateFields_inner> &custom_date_fields);
    bool is_custom_date_fields_Set() const;
    bool is_custom_date_fields_Valid() const;

    QList<OAIEmployee_customDropDownFields_inner> getCustomDropDownFields() const;
    void setCustomDropDownFields(const QList<OAIEmployee_customDropDownFields_inner> &custom_drop_down_fields);
    bool is_custom_drop_down_fields_Set() const;
    bool is_custom_drop_down_fields_Valid() const;

    QList<OAIEmployee_customNumberFields_inner> getCustomNumberFields() const;
    void setCustomNumberFields(const QList<OAIEmployee_customNumberFields_inner> &custom_number_fields);
    bool is_custom_number_fields_Set() const;
    bool is_custom_number_fields_Valid() const;

    QList<OAIEmployee_customTextFields_inner> getCustomTextFields() const;
    void setCustomTextFields(const QList<OAIEmployee_customTextFields_inner> &custom_text_fields);
    bool is_custom_text_fields_Set() const;
    bool is_custom_text_fields_Valid() const;

    QList<OAIStagedEmployee_departmentPosition_inner> getDepartmentPosition() const;
    void setDepartmentPosition(const QList<OAIStagedEmployee_departmentPosition_inner> &department_position);
    bool is_department_position_Set() const;
    bool is_department_position_Valid() const;

    QString getDisabilityDescription() const;
    void setDisabilityDescription(const QString &disability_description);
    bool is_disability_description_Set() const;
    bool is_disability_description_Valid() const;

    QString getEmployeeId() const;
    void setEmployeeId(const QString &employee_id);
    bool is_employee_id_Set() const;
    bool is_employee_id_Valid() const;

    QString getEthnicity() const;
    void setEthnicity(const QString &ethnicity);
    bool is_ethnicity_Set() const;
    bool is_ethnicity_Valid() const;

    QList<OAIStagedEmployee_federalTax_inner> getFederalTax() const;
    void setFederalTax(const QList<OAIStagedEmployee_federalTax_inner> &federal_tax);
    bool is_federal_tax_Set() const;
    bool is_federal_tax_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QString getFitwExemptReason() const;
    void setFitwExemptReason(const QString &fitw_exempt_reason);
    bool is_fitw_exempt_reason_Set() const;
    bool is_fitw_exempt_reason_Valid() const;

    QString getFutaExemptReason() const;
    void setFutaExemptReason(const QString &futa_exempt_reason);
    bool is_futa_exempt_reason_Set() const;
    bool is_futa_exempt_reason_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QList<OAIStagedEmployee_homeAddress_inner> getHomeAddress() const;
    void setHomeAddress(const QList<OAIStagedEmployee_homeAddress_inner> &home_address);
    bool is_home_address_Set() const;
    bool is_home_address_Valid() const;

    bool isIsEmployee943() const;
    void setIsEmployee943(const bool &is_employee943);
    bool is_is_employee943_Set() const;
    bool is_is_employee943_Valid() const;

    bool isIsSmoker() const;
    void setIsSmoker(const bool &is_smoker);
    bool is_is_smoker_Set() const;
    bool is_is_smoker_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QList<OAIEmployee_localTax_inner> getLocalTax() const;
    void setLocalTax(const QList<OAIEmployee_localTax_inner> &local_tax);
    bool is_local_tax_Set() const;
    bool is_local_tax_Valid() const;

    QList<OAIStagedEmployee_mainDirectDeposit_inner> getMainDirectDeposit() const;
    void setMainDirectDeposit(const QList<OAIStagedEmployee_mainDirectDeposit_inner> &main_direct_deposit);
    bool is_main_direct_deposit_Set() const;
    bool is_main_direct_deposit_Valid() const;

    QString getMaritalStatus() const;
    void setMaritalStatus(const QString &marital_status);
    bool is_marital_status_Set() const;
    bool is_marital_status_Valid() const;

    QString getMedExemptReason() const;
    void setMedExemptReason(const QString &med_exempt_reason);
    bool is_med_exempt_reason_Set() const;
    bool is_med_exempt_reason_Valid() const;

    QString getMiddleName() const;
    void setMiddleName(const QString &middle_name);
    bool is_middle_name_Set() const;
    bool is_middle_name_Valid() const;

    QList<OAIStagedEmployee_nonPrimaryStateTax_inner> getNonPrimaryStateTax() const;
    void setNonPrimaryStateTax(const QList<OAIStagedEmployee_nonPrimaryStateTax_inner> &non_primary_state_tax);
    bool is_non_primary_state_tax_Set() const;
    bool is_non_primary_state_tax_Valid() const;

    QString getPreferredName() const;
    void setPreferredName(const QString &preferred_name);
    bool is_preferred_name_Set() const;
    bool is_preferred_name_Valid() const;

    QList<OAIStagedEmployee_primaryPayRate_inner> getPrimaryPayRate() const;
    void setPrimaryPayRate(const QList<OAIStagedEmployee_primaryPayRate_inner> &primary_pay_rate);
    bool is_primary_pay_rate_Set() const;
    bool is_primary_pay_rate_Valid() const;

    QList<OAIStagedEmployee_primaryStateTax_inner> getPrimaryStateTax() const;
    void setPrimaryStateTax(const QList<OAIStagedEmployee_primaryStateTax_inner> &primary_state_tax);
    bool is_primary_state_tax_Set() const;
    bool is_primary_state_tax_Valid() const;

    QString getPriorLastName() const;
    void setPriorLastName(const QString &prior_last_name);
    bool is_prior_last_name_Set() const;
    bool is_prior_last_name_Valid() const;

    QString getSalutation() const;
    void setSalutation(const QString &salutation);
    bool is_salutation_Set() const;
    bool is_salutation_Valid() const;

    QString getSitwExemptReason() const;
    void setSitwExemptReason(const QString &sitw_exempt_reason);
    bool is_sitw_exempt_reason_Set() const;
    bool is_sitw_exempt_reason_Valid() const;

    QString getSsExemptReason() const;
    void setSsExemptReason(const QString &ss_exempt_reason);
    bool is_ss_exempt_reason_Set() const;
    bool is_ss_exempt_reason_Valid() const;

    QString getSsn() const;
    void setSsn(const QString &ssn);
    bool is_ssn_Set() const;
    bool is_ssn_Valid() const;

    QList<OAIStagedEmployee_status_inner> getStatus() const;
    void setStatus(const QList<OAIStagedEmployee_status_inner> &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getSuffix() const;
    void setSuffix(const QString &suffix);
    bool is_suffix_Set() const;
    bool is_suffix_Valid() const;

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

    QString getVeteranDescription() const;
    void setVeteranDescription(const QString &veteran_description);
    bool is_veteran_description_Set() const;
    bool is_veteran_description_Valid() const;

    OAIStagedEmployee_webTime getWebTime() const;
    void setWebTime(const OAIStagedEmployee_webTime &web_time);
    bool is_web_time_Set() const;
    bool is_web_time_Valid() const;

    QList<OAIStagedEmployee_workAddress_inner> getWorkAddress() const;
    void setWorkAddress(const QList<OAIStagedEmployee_workAddress_inner> &work_address);
    bool is_work_address_Set() const;
    bool is_work_address_Valid() const;

    QList<OAIStagedEmployee_workEligibility_inner> getWorkEligibility() const;
    void setWorkEligibility(const QList<OAIStagedEmployee_workEligibility_inner> &work_eligibility);
    bool is_work_eligibility_Set() const;
    bool is_work_eligibility_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIStagedEmployee_additionalDirectDeposit_inner> m_additional_direct_deposit;
    bool m_additional_direct_deposit_isSet;
    bool m_additional_direct_deposit_isValid;

    QList<OAIStagedEmployee_benefitSetup_inner> m_benefit_setup;
    bool m_benefit_setup_isSet;
    bool m_benefit_setup_isValid;

    QString m_birth_date;
    bool m_birth_date_isSet;
    bool m_birth_date_isValid;

    QList<OAIEmployee_customBooleanFields_inner> m_custom_boolean_fields;
    bool m_custom_boolean_fields_isSet;
    bool m_custom_boolean_fields_isValid;

    QList<OAIEmployee_customDateFields_inner> m_custom_date_fields;
    bool m_custom_date_fields_isSet;
    bool m_custom_date_fields_isValid;

    QList<OAIEmployee_customDropDownFields_inner> m_custom_drop_down_fields;
    bool m_custom_drop_down_fields_isSet;
    bool m_custom_drop_down_fields_isValid;

    QList<OAIEmployee_customNumberFields_inner> m_custom_number_fields;
    bool m_custom_number_fields_isSet;
    bool m_custom_number_fields_isValid;

    QList<OAIEmployee_customTextFields_inner> m_custom_text_fields;
    bool m_custom_text_fields_isSet;
    bool m_custom_text_fields_isValid;

    QList<OAIStagedEmployee_departmentPosition_inner> m_department_position;
    bool m_department_position_isSet;
    bool m_department_position_isValid;

    QString m_disability_description;
    bool m_disability_description_isSet;
    bool m_disability_description_isValid;

    QString m_employee_id;
    bool m_employee_id_isSet;
    bool m_employee_id_isValid;

    QString m_ethnicity;
    bool m_ethnicity_isSet;
    bool m_ethnicity_isValid;

    QList<OAIStagedEmployee_federalTax_inner> m_federal_tax;
    bool m_federal_tax_isSet;
    bool m_federal_tax_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QString m_fitw_exempt_reason;
    bool m_fitw_exempt_reason_isSet;
    bool m_fitw_exempt_reason_isValid;

    QString m_futa_exempt_reason;
    bool m_futa_exempt_reason_isSet;
    bool m_futa_exempt_reason_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QList<OAIStagedEmployee_homeAddress_inner> m_home_address;
    bool m_home_address_isSet;
    bool m_home_address_isValid;

    bool m_is_employee943;
    bool m_is_employee943_isSet;
    bool m_is_employee943_isValid;

    bool m_is_smoker;
    bool m_is_smoker_isSet;
    bool m_is_smoker_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QList<OAIEmployee_localTax_inner> m_local_tax;
    bool m_local_tax_isSet;
    bool m_local_tax_isValid;

    QList<OAIStagedEmployee_mainDirectDeposit_inner> m_main_direct_deposit;
    bool m_main_direct_deposit_isSet;
    bool m_main_direct_deposit_isValid;

    QString m_marital_status;
    bool m_marital_status_isSet;
    bool m_marital_status_isValid;

    QString m_med_exempt_reason;
    bool m_med_exempt_reason_isSet;
    bool m_med_exempt_reason_isValid;

    QString m_middle_name;
    bool m_middle_name_isSet;
    bool m_middle_name_isValid;

    QList<OAIStagedEmployee_nonPrimaryStateTax_inner> m_non_primary_state_tax;
    bool m_non_primary_state_tax_isSet;
    bool m_non_primary_state_tax_isValid;

    QString m_preferred_name;
    bool m_preferred_name_isSet;
    bool m_preferred_name_isValid;

    QList<OAIStagedEmployee_primaryPayRate_inner> m_primary_pay_rate;
    bool m_primary_pay_rate_isSet;
    bool m_primary_pay_rate_isValid;

    QList<OAIStagedEmployee_primaryStateTax_inner> m_primary_state_tax;
    bool m_primary_state_tax_isSet;
    bool m_primary_state_tax_isValid;

    QString m_prior_last_name;
    bool m_prior_last_name_isSet;
    bool m_prior_last_name_isValid;

    QString m_salutation;
    bool m_salutation_isSet;
    bool m_salutation_isValid;

    QString m_sitw_exempt_reason;
    bool m_sitw_exempt_reason_isSet;
    bool m_sitw_exempt_reason_isValid;

    QString m_ss_exempt_reason;
    bool m_ss_exempt_reason_isSet;
    bool m_ss_exempt_reason_isValid;

    QString m_ssn;
    bool m_ssn_isSet;
    bool m_ssn_isValid;

    QList<OAIStagedEmployee_status_inner> m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_suffix;
    bool m_suffix_isSet;
    bool m_suffix_isValid;

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

    QString m_veteran_description;
    bool m_veteran_description_isSet;
    bool m_veteran_description_isValid;

    OAIStagedEmployee_webTime m_web_time;
    bool m_web_time_isSet;
    bool m_web_time_isValid;

    QList<OAIStagedEmployee_workAddress_inner> m_work_address;
    bool m_work_address_isSet;
    bool m_work_address_isValid;

    QList<OAIStagedEmployee_workEligibility_inner> m_work_eligibility;
    bool m_work_eligibility_isSet;
    bool m_work_eligibility_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStagedEmployee)

#endif // OAIStagedEmployee_H
