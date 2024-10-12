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

#include "OAIError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError::OAIError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError::OAIError() {
    this->initializeModel();
}

OAIError::~OAIError() {}

void OAIError::initializeModel() {

    m_error_code_isSet = false;
    m_error_code_isValid = false;

    m_error_data_isSet = false;
    m_error_data_isValid = false;

    m_error_message_isSet = false;
    m_error_message_isValid = false;

    m_localisation_details_isSet = false;
    m_localisation_details_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_location_type_isSet = false;
    m_location_type_isValid = false;

    m_reason_code_isSet = false;
    m_reason_code_isValid = false;
}

void OAIError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError::fromJsonObject(QJsonObject json) {

    m_error_code_isValid = ::OpenAPI::fromJsonValue(m_error_code, json[QString("errorCode")]);
    m_error_code_isSet = !json[QString("errorCode")].isNull() && m_error_code_isValid;

    m_error_data_isValid = ::OpenAPI::fromJsonValue(m_error_data, json[QString("errorData")]);
    m_error_data_isSet = !json[QString("errorData")].isNull() && m_error_data_isValid;

    m_error_message_isValid = ::OpenAPI::fromJsonValue(m_error_message, json[QString("errorMessage")]);
    m_error_message_isSet = !json[QString("errorMessage")].isNull() && m_error_message_isValid;

    m_localisation_details_isValid = ::OpenAPI::fromJsonValue(m_localisation_details, json[QString("localisationDetails")]);
    m_localisation_details_isSet = !json[QString("localisationDetails")].isNull() && m_localisation_details_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_location_type_isValid = ::OpenAPI::fromJsonValue(m_location_type, json[QString("locationType")]);
    m_location_type_isSet = !json[QString("locationType")].isNull() && m_location_type_isValid;

    m_reason_code_isValid = ::OpenAPI::fromJsonValue(m_reason_code, json[QString("reasonCode")]);
    m_reason_code_isSet = !json[QString("reasonCode")].isNull() && m_reason_code_isValid;
}

QString OAIError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError::asJsonObject() const {
    QJsonObject obj;
    if (m_error_code_isSet) {
        obj.insert(QString("errorCode"), ::OpenAPI::toJsonValue(m_error_code));
    }
    if (m_error_data.isSet()) {
        obj.insert(QString("errorData"), ::OpenAPI::toJsonValue(m_error_data));
    }
    if (m_error_message_isSet) {
        obj.insert(QString("errorMessage"), ::OpenAPI::toJsonValue(m_error_message));
    }
    if (m_localisation_details.isSet()) {
        obj.insert(QString("localisationDetails"), ::OpenAPI::toJsonValue(m_localisation_details));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_location_type_isSet) {
        obj.insert(QString("locationType"), ::OpenAPI::toJsonValue(m_location_type));
    }
    if (m_reason_code_isSet) {
        obj.insert(QString("reasonCode"), ::OpenAPI::toJsonValue(m_reason_code));
    }
    return obj;
}

QString OAIError::getErrorCode() const {
    return m_error_code;
}
void OAIError::setErrorCode(const QString &error_code) {
    m_error_code = error_code;
    m_error_code_isSet = true;
}

bool OAIError::is_error_code_Set() const{
    return m_error_code_isSet;
}

bool OAIError::is_error_code_Valid() const{
    return m_error_code_isValid;
}

OAIErrorData OAIError::getErrorData() const {
    return m_error_data;
}
void OAIError::setErrorData(const OAIErrorData &error_data) {
    m_error_data = error_data;
    m_error_data_isSet = true;
}

bool OAIError::is_error_data_Set() const{
    return m_error_data_isSet;
}

bool OAIError::is_error_data_Valid() const{
    return m_error_data_isValid;
}

QString OAIError::getErrorMessage() const {
    return m_error_message;
}
void OAIError::setErrorMessage(const QString &error_message) {
    m_error_message = error_message;
    m_error_message_isSet = true;
}

bool OAIError::is_error_message_Set() const{
    return m_error_message_isSet;
}

bool OAIError::is_error_message_Valid() const{
    return m_error_message_isValid;
}

OAILocalisationDetails OAIError::getLocalisationDetails() const {
    return m_localisation_details;
}
void OAIError::setLocalisationDetails(const OAILocalisationDetails &localisation_details) {
    m_localisation_details = localisation_details;
    m_localisation_details_isSet = true;
}

bool OAIError::is_localisation_details_Set() const{
    return m_localisation_details_isSet;
}

bool OAIError::is_localisation_details_Valid() const{
    return m_localisation_details_isValid;
}

QString OAIError::getLocation() const {
    return m_location;
}
void OAIError::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIError::is_location_Set() const{
    return m_location_isSet;
}

bool OAIError::is_location_Valid() const{
    return m_location_isValid;
}

QString OAIError::getLocationType() const {
    return m_location_type;
}
void OAIError::setLocationType(const QString &location_type) {
    m_location_type = location_type;
    m_location_type_isSet = true;
}

bool OAIError::is_location_type_Set() const{
    return m_location_type_isSet;
}

bool OAIError::is_location_type_Valid() const{
    return m_location_type_isValid;
}

QString OAIError::getReasonCode() const {
    return m_reason_code;
}
void OAIError::setReasonCode(const QString &reason_code) {
    m_reason_code = reason_code;
    m_reason_code_isSet = true;
}

bool OAIError::is_reason_code_Set() const{
    return m_reason_code_isSet;
}

bool OAIError::is_reason_code_Valid() const{
    return m_reason_code_isValid;
}

bool OAIError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_localisation_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
