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

#include "OAIPayoutScheduleV3.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayoutScheduleV3::OAIPayoutScheduleV3(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayoutScheduleV3::OAIPayoutScheduleV3() {
    this->initializeModel();
}

OAIPayoutScheduleV3::~OAIPayoutScheduleV3() {}

void OAIPayoutScheduleV3::initializeModel() {

    m_notifications_enabled_isSet = false;
    m_notifications_enabled_isValid = false;

    m_schedule_status_isSet = false;
    m_schedule_status_isValid = false;

    m_scheduled_at_isSet = false;
    m_scheduled_at_isValid = false;

    m_scheduled_by_principal_id_isSet = false;
    m_scheduled_by_principal_id_isValid = false;

    m_scheduled_for_isSet = false;
    m_scheduled_for_isValid = false;
}

void OAIPayoutScheduleV3::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayoutScheduleV3::fromJsonObject(QJsonObject json) {

    m_notifications_enabled_isValid = ::OpenAPI::fromJsonValue(m_notifications_enabled, json[QString("notificationsEnabled")]);
    m_notifications_enabled_isSet = !json[QString("notificationsEnabled")].isNull() && m_notifications_enabled_isValid;

    m_schedule_status_isValid = ::OpenAPI::fromJsonValue(m_schedule_status, json[QString("scheduleStatus")]);
    m_schedule_status_isSet = !json[QString("scheduleStatus")].isNull() && m_schedule_status_isValid;

    m_scheduled_at_isValid = ::OpenAPI::fromJsonValue(m_scheduled_at, json[QString("scheduledAt")]);
    m_scheduled_at_isSet = !json[QString("scheduledAt")].isNull() && m_scheduled_at_isValid;

    m_scheduled_by_principal_id_isValid = ::OpenAPI::fromJsonValue(m_scheduled_by_principal_id, json[QString("scheduledByPrincipalId")]);
    m_scheduled_by_principal_id_isSet = !json[QString("scheduledByPrincipalId")].isNull() && m_scheduled_by_principal_id_isValid;

    m_scheduled_for_isValid = ::OpenAPI::fromJsonValue(m_scheduled_for, json[QString("scheduledFor")]);
    m_scheduled_for_isSet = !json[QString("scheduledFor")].isNull() && m_scheduled_for_isValid;
}

QString OAIPayoutScheduleV3::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayoutScheduleV3::asJsonObject() const {
    QJsonObject obj;
    if (m_notifications_enabled_isSet) {
        obj.insert(QString("notificationsEnabled"), ::OpenAPI::toJsonValue(m_notifications_enabled));
    }
    if (m_schedule_status_isSet) {
        obj.insert(QString("scheduleStatus"), ::OpenAPI::toJsonValue(m_schedule_status));
    }
    if (m_scheduled_at_isSet) {
        obj.insert(QString("scheduledAt"), ::OpenAPI::toJsonValue(m_scheduled_at));
    }
    if (m_scheduled_by_principal_id_isSet) {
        obj.insert(QString("scheduledByPrincipalId"), ::OpenAPI::toJsonValue(m_scheduled_by_principal_id));
    }
    if (m_scheduled_for_isSet) {
        obj.insert(QString("scheduledFor"), ::OpenAPI::toJsonValue(m_scheduled_for));
    }
    return obj;
}

bool OAIPayoutScheduleV3::isNotificationsEnabled() const {
    return m_notifications_enabled;
}
void OAIPayoutScheduleV3::setNotificationsEnabled(const bool &notifications_enabled) {
    m_notifications_enabled = notifications_enabled;
    m_notifications_enabled_isSet = true;
}

bool OAIPayoutScheduleV3::is_notifications_enabled_Set() const{
    return m_notifications_enabled_isSet;
}

bool OAIPayoutScheduleV3::is_notifications_enabled_Valid() const{
    return m_notifications_enabled_isValid;
}

QString OAIPayoutScheduleV3::getScheduleStatus() const {
    return m_schedule_status;
}
void OAIPayoutScheduleV3::setScheduleStatus(const QString &schedule_status) {
    m_schedule_status = schedule_status;
    m_schedule_status_isSet = true;
}

bool OAIPayoutScheduleV3::is_schedule_status_Set() const{
    return m_schedule_status_isSet;
}

bool OAIPayoutScheduleV3::is_schedule_status_Valid() const{
    return m_schedule_status_isValid;
}

QDateTime OAIPayoutScheduleV3::getScheduledAt() const {
    return m_scheduled_at;
}
void OAIPayoutScheduleV3::setScheduledAt(const QDateTime &scheduled_at) {
    m_scheduled_at = scheduled_at;
    m_scheduled_at_isSet = true;
}

bool OAIPayoutScheduleV3::is_scheduled_at_Set() const{
    return m_scheduled_at_isSet;
}

bool OAIPayoutScheduleV3::is_scheduled_at_Valid() const{
    return m_scheduled_at_isValid;
}

QString OAIPayoutScheduleV3::getScheduledByPrincipalId() const {
    return m_scheduled_by_principal_id;
}
void OAIPayoutScheduleV3::setScheduledByPrincipalId(const QString &scheduled_by_principal_id) {
    m_scheduled_by_principal_id = scheduled_by_principal_id;
    m_scheduled_by_principal_id_isSet = true;
}

bool OAIPayoutScheduleV3::is_scheduled_by_principal_id_Set() const{
    return m_scheduled_by_principal_id_isSet;
}

bool OAIPayoutScheduleV3::is_scheduled_by_principal_id_Valid() const{
    return m_scheduled_by_principal_id_isValid;
}

QDateTime OAIPayoutScheduleV3::getScheduledFor() const {
    return m_scheduled_for;
}
void OAIPayoutScheduleV3::setScheduledFor(const QDateTime &scheduled_for) {
    m_scheduled_for = scheduled_for;
    m_scheduled_for_isSet = true;
}

bool OAIPayoutScheduleV3::is_scheduled_for_Set() const{
    return m_scheduled_for_isSet;
}

bool OAIPayoutScheduleV3::is_scheduled_for_Valid() const{
    return m_scheduled_for_isValid;
}

bool OAIPayoutScheduleV3::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_notifications_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_by_principal_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_for_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPayoutScheduleV3::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_notifications_enabled_isValid && m_schedule_status_isValid && m_scheduled_at_isValid && m_scheduled_by_principal_id_isValid && m_scheduled_for_isValid && true;
}

} // namespace OpenAPI
