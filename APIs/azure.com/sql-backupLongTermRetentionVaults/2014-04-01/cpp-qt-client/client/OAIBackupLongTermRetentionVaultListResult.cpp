/**
 * Azure SQL Server Backup Long Term Retention Vault
 * Provides read and update functionality for Azure SQL Server backup long term retention vault
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBackupLongTermRetentionVaultListResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBackupLongTermRetentionVaultListResult::OAIBackupLongTermRetentionVaultListResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBackupLongTermRetentionVaultListResult::OAIBackupLongTermRetentionVaultListResult() {
    this->initializeModel();
}

OAIBackupLongTermRetentionVaultListResult::~OAIBackupLongTermRetentionVaultListResult() {}

void OAIBackupLongTermRetentionVaultListResult::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIBackupLongTermRetentionVaultListResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBackupLongTermRetentionVaultListResult::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIBackupLongTermRetentionVaultListResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBackupLongTermRetentionVaultListResult::asJsonObject() const {
    QJsonObject obj;
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QList<OAIBackupLongTermRetentionVault> OAIBackupLongTermRetentionVaultListResult::getValue() const {
    return m_value;
}
void OAIBackupLongTermRetentionVaultListResult::setValue(const QList<OAIBackupLongTermRetentionVault> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIBackupLongTermRetentionVaultListResult::is_value_Set() const{
    return m_value_isSet;
}

bool OAIBackupLongTermRetentionVaultListResult::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIBackupLongTermRetentionVaultListResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBackupLongTermRetentionVaultListResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && true;
}

} // namespace OpenAPI
