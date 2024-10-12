/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDeviceRolloverDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeviceRolloverDetails::OAIDeviceRolloverDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeviceRolloverDetails::OAIDeviceRolloverDetails() {
    this->initializeModel();
}

OAIDeviceRolloverDetails::~OAIDeviceRolloverDetails() {}

void OAIDeviceRolloverDetails::initializeModel() {

    m_authorization_eligibility_isSet = false;
    m_authorization_eligibility_isValid = false;

    m_authorization_status_isSet = false;
    m_authorization_status_isValid = false;

    m_in_eligibility_reason_isSet = false;
    m_in_eligibility_reason_isValid = false;
}

void OAIDeviceRolloverDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeviceRolloverDetails::fromJsonObject(QJsonObject json) {

    m_authorization_eligibility_isValid = ::OpenAPI::fromJsonValue(m_authorization_eligibility, json[QString("authorizationEligibility")]);
    m_authorization_eligibility_isSet = !json[QString("authorizationEligibility")].isNull() && m_authorization_eligibility_isValid;

    m_authorization_status_isValid = ::OpenAPI::fromJsonValue(m_authorization_status, json[QString("authorizationStatus")]);
    m_authorization_status_isSet = !json[QString("authorizationStatus")].isNull() && m_authorization_status_isValid;

    m_in_eligibility_reason_isValid = ::OpenAPI::fromJsonValue(m_in_eligibility_reason, json[QString("inEligibilityReason")]);
    m_in_eligibility_reason_isSet = !json[QString("inEligibilityReason")].isNull() && m_in_eligibility_reason_isValid;
}

QString OAIDeviceRolloverDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeviceRolloverDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_authorization_eligibility_isSet) {
        obj.insert(QString("authorizationEligibility"), ::OpenAPI::toJsonValue(m_authorization_eligibility));
    }
    if (m_authorization_status_isSet) {
        obj.insert(QString("authorizationStatus"), ::OpenAPI::toJsonValue(m_authorization_status));
    }
    if (m_in_eligibility_reason_isSet) {
        obj.insert(QString("inEligibilityReason"), ::OpenAPI::toJsonValue(m_in_eligibility_reason));
    }
    return obj;
}

QString OAIDeviceRolloverDetails::getAuthorizationEligibility() const {
    return m_authorization_eligibility;
}
void OAIDeviceRolloverDetails::setAuthorizationEligibility(const QString &authorization_eligibility) {
    m_authorization_eligibility = authorization_eligibility;
    m_authorization_eligibility_isSet = true;
}

bool OAIDeviceRolloverDetails::is_authorization_eligibility_Set() const{
    return m_authorization_eligibility_isSet;
}

bool OAIDeviceRolloverDetails::is_authorization_eligibility_Valid() const{
    return m_authorization_eligibility_isValid;
}

QString OAIDeviceRolloverDetails::getAuthorizationStatus() const {
    return m_authorization_status;
}
void OAIDeviceRolloverDetails::setAuthorizationStatus(const QString &authorization_status) {
    m_authorization_status = authorization_status;
    m_authorization_status_isSet = true;
}

bool OAIDeviceRolloverDetails::is_authorization_status_Set() const{
    return m_authorization_status_isSet;
}

bool OAIDeviceRolloverDetails::is_authorization_status_Valid() const{
    return m_authorization_status_isValid;
}

QString OAIDeviceRolloverDetails::getInEligibilityReason() const {
    return m_in_eligibility_reason;
}
void OAIDeviceRolloverDetails::setInEligibilityReason(const QString &in_eligibility_reason) {
    m_in_eligibility_reason = in_eligibility_reason;
    m_in_eligibility_reason_isSet = true;
}

bool OAIDeviceRolloverDetails::is_in_eligibility_reason_Set() const{
    return m_in_eligibility_reason_isSet;
}

bool OAIDeviceRolloverDetails::is_in_eligibility_reason_Valid() const{
    return m_in_eligibility_reason_isValid;
}

bool OAIDeviceRolloverDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_authorization_eligibility_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_authorization_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_in_eligibility_reason_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeviceRolloverDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
