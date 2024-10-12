/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAlertRuleProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlertRuleProperties::OAIAlertRuleProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlertRuleProperties::OAIAlertRuleProperties() {
    this->initializeModel();
}

OAIAlertRuleProperties::~OAIAlertRuleProperties() {}

void OAIAlertRuleProperties::initializeModel() {

    m_action_groups_isSet = false;
    m_action_groups_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_detector_isSet = false;
    m_detector_isValid = false;

    m_frequency_isSet = false;
    m_frequency_isValid = false;

    m_scope_isSet = false;
    m_scope_isValid = false;

    m_severity_isSet = false;
    m_severity_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_throttling_isSet = false;
    m_throttling_isValid = false;
}

void OAIAlertRuleProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlertRuleProperties::fromJsonObject(QJsonObject json) {

    m_action_groups_isValid = ::OpenAPI::fromJsonValue(m_action_groups, json[QString("actionGroups")]);
    m_action_groups_isSet = !json[QString("actionGroups")].isNull() && m_action_groups_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_detector_isValid = ::OpenAPI::fromJsonValue(m_detector, json[QString("detector")]);
    m_detector_isSet = !json[QString("detector")].isNull() && m_detector_isValid;

    m_frequency_isValid = ::OpenAPI::fromJsonValue(m_frequency, json[QString("frequency")]);
    m_frequency_isSet = !json[QString("frequency")].isNull() && m_frequency_isValid;

    m_scope_isValid = ::OpenAPI::fromJsonValue(m_scope, json[QString("scope")]);
    m_scope_isSet = !json[QString("scope")].isNull() && m_scope_isValid;

    m_severity_isValid = ::OpenAPI::fromJsonValue(m_severity, json[QString("severity")]);
    m_severity_isSet = !json[QString("severity")].isNull() && m_severity_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_throttling_isValid = ::OpenAPI::fromJsonValue(m_throttling, json[QString("throttling")]);
    m_throttling_isSet = !json[QString("throttling")].isNull() && m_throttling_isValid;
}

QString OAIAlertRuleProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlertRuleProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_action_groups.isSet()) {
        obj.insert(QString("actionGroups"), ::OpenAPI::toJsonValue(m_action_groups));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_detector.isSet()) {
        obj.insert(QString("detector"), ::OpenAPI::toJsonValue(m_detector));
    }
    if (m_frequency_isSet) {
        obj.insert(QString("frequency"), ::OpenAPI::toJsonValue(m_frequency));
    }
    if (m_scope.size() > 0) {
        obj.insert(QString("scope"), ::OpenAPI::toJsonValue(m_scope));
    }
    if (m_severity_isSet) {
        obj.insert(QString("severity"), ::OpenAPI::toJsonValue(m_severity));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_throttling.isSet()) {
        obj.insert(QString("throttling"), ::OpenAPI::toJsonValue(m_throttling));
    }
    return obj;
}

OAIActionGroupsInformation OAIAlertRuleProperties::getActionGroups() const {
    return m_action_groups;
}
void OAIAlertRuleProperties::setActionGroups(const OAIActionGroupsInformation &action_groups) {
    m_action_groups = action_groups;
    m_action_groups_isSet = true;
}

bool OAIAlertRuleProperties::is_action_groups_Set() const{
    return m_action_groups_isSet;
}

bool OAIAlertRuleProperties::is_action_groups_Valid() const{
    return m_action_groups_isValid;
}

QString OAIAlertRuleProperties::getDescription() const {
    return m_description;
}
void OAIAlertRuleProperties::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAlertRuleProperties::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAlertRuleProperties::is_description_Valid() const{
    return m_description_isValid;
}

OAIDetector OAIAlertRuleProperties::getDetector() const {
    return m_detector;
}
void OAIAlertRuleProperties::setDetector(const OAIDetector &detector) {
    m_detector = detector;
    m_detector_isSet = true;
}

bool OAIAlertRuleProperties::is_detector_Set() const{
    return m_detector_isSet;
}

bool OAIAlertRuleProperties::is_detector_Valid() const{
    return m_detector_isValid;
}

QString OAIAlertRuleProperties::getFrequency() const {
    return m_frequency;
}
void OAIAlertRuleProperties::setFrequency(const QString &frequency) {
    m_frequency = frequency;
    m_frequency_isSet = true;
}

bool OAIAlertRuleProperties::is_frequency_Set() const{
    return m_frequency_isSet;
}

bool OAIAlertRuleProperties::is_frequency_Valid() const{
    return m_frequency_isValid;
}

QList<QString> OAIAlertRuleProperties::getScope() const {
    return m_scope;
}
void OAIAlertRuleProperties::setScope(const QList<QString> &scope) {
    m_scope = scope;
    m_scope_isSet = true;
}

bool OAIAlertRuleProperties::is_scope_Set() const{
    return m_scope_isSet;
}

bool OAIAlertRuleProperties::is_scope_Valid() const{
    return m_scope_isValid;
}

QString OAIAlertRuleProperties::getSeverity() const {
    return m_severity;
}
void OAIAlertRuleProperties::setSeverity(const QString &severity) {
    m_severity = severity;
    m_severity_isSet = true;
}

bool OAIAlertRuleProperties::is_severity_Set() const{
    return m_severity_isSet;
}

bool OAIAlertRuleProperties::is_severity_Valid() const{
    return m_severity_isValid;
}

QString OAIAlertRuleProperties::getState() const {
    return m_state;
}
void OAIAlertRuleProperties::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIAlertRuleProperties::is_state_Set() const{
    return m_state_isSet;
}

bool OAIAlertRuleProperties::is_state_Valid() const{
    return m_state_isValid;
}

OAIThrottlingInformation OAIAlertRuleProperties::getThrottling() const {
    return m_throttling;
}
void OAIAlertRuleProperties::setThrottling(const OAIThrottlingInformation &throttling) {
    m_throttling = throttling;
    m_throttling_isSet = true;
}

bool OAIAlertRuleProperties::is_throttling_Set() const{
    return m_throttling_isSet;
}

bool OAIAlertRuleProperties::is_throttling_Valid() const{
    return m_throttling_isValid;
}

bool OAIAlertRuleProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_groups.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detector.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_frequency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scope.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_severity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_throttling.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAlertRuleProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_action_groups_isValid && m_detector_isValid && m_frequency_isValid && m_scope_isValid && m_severity_isValid && m_state_isValid && true;
}

} // namespace OpenAPI
