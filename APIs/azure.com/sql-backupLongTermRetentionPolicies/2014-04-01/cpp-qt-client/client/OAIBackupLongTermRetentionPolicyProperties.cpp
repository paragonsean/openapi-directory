/**
 * Azure SQL Database Backup Long Term Retention Policy
 * Provides read and update functionality for Azure SQL Database backup long term retention policy
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBackupLongTermRetentionPolicyProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBackupLongTermRetentionPolicyProperties::OAIBackupLongTermRetentionPolicyProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBackupLongTermRetentionPolicyProperties::OAIBackupLongTermRetentionPolicyProperties() {
    this->initializeModel();
}

OAIBackupLongTermRetentionPolicyProperties::~OAIBackupLongTermRetentionPolicyProperties() {}

void OAIBackupLongTermRetentionPolicyProperties::initializeModel() {

    m_recovery_services_backup_policy_resource_id_isSet = false;
    m_recovery_services_backup_policy_resource_id_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIBackupLongTermRetentionPolicyProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBackupLongTermRetentionPolicyProperties::fromJsonObject(QJsonObject json) {

    m_recovery_services_backup_policy_resource_id_isValid = ::OpenAPI::fromJsonValue(m_recovery_services_backup_policy_resource_id, json[QString("recoveryServicesBackupPolicyResourceId")]);
    m_recovery_services_backup_policy_resource_id_isSet = !json[QString("recoveryServicesBackupPolicyResourceId")].isNull() && m_recovery_services_backup_policy_resource_id_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIBackupLongTermRetentionPolicyProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBackupLongTermRetentionPolicyProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_recovery_services_backup_policy_resource_id_isSet) {
        obj.insert(QString("recoveryServicesBackupPolicyResourceId"), ::OpenAPI::toJsonValue(m_recovery_services_backup_policy_resource_id));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

QString OAIBackupLongTermRetentionPolicyProperties::getRecoveryServicesBackupPolicyResourceId() const {
    return m_recovery_services_backup_policy_resource_id;
}
void OAIBackupLongTermRetentionPolicyProperties::setRecoveryServicesBackupPolicyResourceId(const QString &recovery_services_backup_policy_resource_id) {
    m_recovery_services_backup_policy_resource_id = recovery_services_backup_policy_resource_id;
    m_recovery_services_backup_policy_resource_id_isSet = true;
}

bool OAIBackupLongTermRetentionPolicyProperties::is_recovery_services_backup_policy_resource_id_Set() const{
    return m_recovery_services_backup_policy_resource_id_isSet;
}

bool OAIBackupLongTermRetentionPolicyProperties::is_recovery_services_backup_policy_resource_id_Valid() const{
    return m_recovery_services_backup_policy_resource_id_isValid;
}

QString OAIBackupLongTermRetentionPolicyProperties::getState() const {
    return m_state;
}
void OAIBackupLongTermRetentionPolicyProperties::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIBackupLongTermRetentionPolicyProperties::is_state_Set() const{
    return m_state_isSet;
}

bool OAIBackupLongTermRetentionPolicyProperties::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIBackupLongTermRetentionPolicyProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_recovery_services_backup_policy_resource_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBackupLongTermRetentionPolicyProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_recovery_services_backup_policy_resource_id_isValid && m_state_isValid && true;
}

} // namespace OpenAPI
