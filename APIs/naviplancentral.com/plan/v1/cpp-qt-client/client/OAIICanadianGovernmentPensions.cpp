/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIICanadianGovernmentPensions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIICanadianGovernmentPensions::OAIICanadianGovernmentPensions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIICanadianGovernmentPensions::OAIICanadianGovernmentPensions() {
    this->initializeModel();
}

OAIICanadianGovernmentPensions::~OAIICanadianGovernmentPensions() {}

void OAIICanadianGovernmentPensions::initializeModel() {

    m_canadian_or_quebec_pension_plan_isSet = false;
    m_canadian_or_quebec_pension_plan_isValid = false;

    m_old_age_security_isSet = false;
    m_old_age_security_isValid = false;
}

void OAIICanadianGovernmentPensions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIICanadianGovernmentPensions::fromJsonObject(QJsonObject json) {

    m_canadian_or_quebec_pension_plan_isValid = ::OpenAPI::fromJsonValue(m_canadian_or_quebec_pension_plan, json[QString("canadianOrQuebecPensionPlan")]);
    m_canadian_or_quebec_pension_plan_isSet = !json[QString("canadianOrQuebecPensionPlan")].isNull() && m_canadian_or_quebec_pension_plan_isValid;

    m_old_age_security_isValid = ::OpenAPI::fromJsonValue(m_old_age_security, json[QString("oldAgeSecurity")]);
    m_old_age_security_isSet = !json[QString("oldAgeSecurity")].isNull() && m_old_age_security_isValid;
}

QString OAIICanadianGovernmentPensions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIICanadianGovernmentPensions::asJsonObject() const {
    QJsonObject obj;
    if (m_canadian_or_quebec_pension_plan.isSet()) {
        obj.insert(QString("canadianOrQuebecPensionPlan"), ::OpenAPI::toJsonValue(m_canadian_or_quebec_pension_plan));
    }
    if (m_old_age_security.isSet()) {
        obj.insert(QString("oldAgeSecurity"), ::OpenAPI::toJsonValue(m_old_age_security));
    }
    return obj;
}

OAICurrency OAIICanadianGovernmentPensions::getCanadianOrQuebecPensionPlan() const {
    return m_canadian_or_quebec_pension_plan;
}
void OAIICanadianGovernmentPensions::setCanadianOrQuebecPensionPlan(const OAICurrency &canadian_or_quebec_pension_plan) {
    m_canadian_or_quebec_pension_plan = canadian_or_quebec_pension_plan;
    m_canadian_or_quebec_pension_plan_isSet = true;
}

bool OAIICanadianGovernmentPensions::is_canadian_or_quebec_pension_plan_Set() const{
    return m_canadian_or_quebec_pension_plan_isSet;
}

bool OAIICanadianGovernmentPensions::is_canadian_or_quebec_pension_plan_Valid() const{
    return m_canadian_or_quebec_pension_plan_isValid;
}

OAICurrency OAIICanadianGovernmentPensions::getOldAgeSecurity() const {
    return m_old_age_security;
}
void OAIICanadianGovernmentPensions::setOldAgeSecurity(const OAICurrency &old_age_security) {
    m_old_age_security = old_age_security;
    m_old_age_security_isSet = true;
}

bool OAIICanadianGovernmentPensions::is_old_age_security_Set() const{
    return m_old_age_security_isSet;
}

bool OAIICanadianGovernmentPensions::is_old_age_security_Valid() const{
    return m_old_age_security_isValid;
}

bool OAIICanadianGovernmentPensions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_canadian_or_quebec_pension_plan.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_old_age_security.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIICanadianGovernmentPensions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
