/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserDetailsUpdateRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserDetailsUpdateRequest::OAIUserDetailsUpdateRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserDetailsUpdateRequest::OAIUserDetailsUpdateRequest() {
    this->initializeModel();
}

OAIUserDetailsUpdateRequest::~OAIUserDetailsUpdateRequest() {}

void OAIUserDetailsUpdateRequest::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_mfa_type_isSet = false;
    m_mfa_type_isValid = false;

    m_primary_contact_number_isSet = false;
    m_primary_contact_number_isValid = false;

    m_secondary_contact_number_isSet = false;
    m_secondary_contact_number_isValid = false;

    m_sms_number_isSet = false;
    m_sms_number_isValid = false;

    m_verification_code_isSet = false;
    m_verification_code_isValid = false;
}

void OAIUserDetailsUpdateRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserDetailsUpdateRequest::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_mfa_type_isValid = ::OpenAPI::fromJsonValue(m_mfa_type, json[QString("mfaType")]);
    m_mfa_type_isSet = !json[QString("mfaType")].isNull() && m_mfa_type_isValid;

    m_primary_contact_number_isValid = ::OpenAPI::fromJsonValue(m_primary_contact_number, json[QString("primaryContactNumber")]);
    m_primary_contact_number_isSet = !json[QString("primaryContactNumber")].isNull() && m_primary_contact_number_isValid;

    m_secondary_contact_number_isValid = ::OpenAPI::fromJsonValue(m_secondary_contact_number, json[QString("secondaryContactNumber")]);
    m_secondary_contact_number_isSet = !json[QString("secondaryContactNumber")].isNull() && m_secondary_contact_number_isValid;

    m_sms_number_isValid = ::OpenAPI::fromJsonValue(m_sms_number, json[QString("smsNumber")]);
    m_sms_number_isSet = !json[QString("smsNumber")].isNull() && m_sms_number_isValid;

    m_verification_code_isValid = ::OpenAPI::fromJsonValue(m_verification_code, json[QString("verificationCode")]);
    m_verification_code_isSet = !json[QString("verificationCode")].isNull() && m_verification_code_isValid;
}

QString OAIUserDetailsUpdateRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserDetailsUpdateRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_mfa_type.isSet()) {
        obj.insert(QString("mfaType"), ::OpenAPI::toJsonValue(m_mfa_type));
    }
    if (m_primary_contact_number_isSet) {
        obj.insert(QString("primaryContactNumber"), ::OpenAPI::toJsonValue(m_primary_contact_number));
    }
    if (m_secondary_contact_number_isSet) {
        obj.insert(QString("secondaryContactNumber"), ::OpenAPI::toJsonValue(m_secondary_contact_number));
    }
    if (m_sms_number_isSet) {
        obj.insert(QString("smsNumber"), ::OpenAPI::toJsonValue(m_sms_number));
    }
    if (m_verification_code_isSet) {
        obj.insert(QString("verificationCode"), ::OpenAPI::toJsonValue(m_verification_code));
    }
    return obj;
}

QString OAIUserDetailsUpdateRequest::getEmail() const {
    return m_email;
}
void OAIUserDetailsUpdateRequest::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUserDetailsUpdateRequest::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIUserDetailsUpdateRequest::getFirstName() const {
    return m_first_name;
}
void OAIUserDetailsUpdateRequest::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIUserDetailsUpdateRequest::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIUserDetailsUpdateRequest::getLastName() const {
    return m_last_name;
}
void OAIUserDetailsUpdateRequest::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIUserDetailsUpdateRequest::is_last_name_Valid() const{
    return m_last_name_isValid;
}

OAIMFAType OAIUserDetailsUpdateRequest::getMfaType() const {
    return m_mfa_type;
}
void OAIUserDetailsUpdateRequest::setMfaType(const OAIMFAType &mfa_type) {
    m_mfa_type = mfa_type;
    m_mfa_type_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_mfa_type_Set() const{
    return m_mfa_type_isSet;
}

bool OAIUserDetailsUpdateRequest::is_mfa_type_Valid() const{
    return m_mfa_type_isValid;
}

QString OAIUserDetailsUpdateRequest::getPrimaryContactNumber() const {
    return m_primary_contact_number;
}
void OAIUserDetailsUpdateRequest::setPrimaryContactNumber(const QString &primary_contact_number) {
    m_primary_contact_number = primary_contact_number;
    m_primary_contact_number_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_primary_contact_number_Set() const{
    return m_primary_contact_number_isSet;
}

bool OAIUserDetailsUpdateRequest::is_primary_contact_number_Valid() const{
    return m_primary_contact_number_isValid;
}

QString OAIUserDetailsUpdateRequest::getSecondaryContactNumber() const {
    return m_secondary_contact_number;
}
void OAIUserDetailsUpdateRequest::setSecondaryContactNumber(const QString &secondary_contact_number) {
    m_secondary_contact_number = secondary_contact_number;
    m_secondary_contact_number_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_secondary_contact_number_Set() const{
    return m_secondary_contact_number_isSet;
}

bool OAIUserDetailsUpdateRequest::is_secondary_contact_number_Valid() const{
    return m_secondary_contact_number_isValid;
}

QString OAIUserDetailsUpdateRequest::getSmsNumber() const {
    return m_sms_number;
}
void OAIUserDetailsUpdateRequest::setSmsNumber(const QString &sms_number) {
    m_sms_number = sms_number;
    m_sms_number_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_sms_number_Set() const{
    return m_sms_number_isSet;
}

bool OAIUserDetailsUpdateRequest::is_sms_number_Valid() const{
    return m_sms_number_isValid;
}

QString OAIUserDetailsUpdateRequest::getVerificationCode() const {
    return m_verification_code;
}
void OAIUserDetailsUpdateRequest::setVerificationCode(const QString &verification_code) {
    m_verification_code = verification_code;
    m_verification_code_isSet = true;
}

bool OAIUserDetailsUpdateRequest::is_verification_code_Set() const{
    return m_verification_code_isSet;
}

bool OAIUserDetailsUpdateRequest::is_verification_code_Valid() const{
    return m_verification_code_isValid;
}

bool OAIUserDetailsUpdateRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mfa_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_contact_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_contact_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sms_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_verification_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserDetailsUpdateRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
