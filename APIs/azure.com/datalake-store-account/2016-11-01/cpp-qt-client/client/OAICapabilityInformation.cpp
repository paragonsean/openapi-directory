/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICapabilityInformation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICapabilityInformation::OAICapabilityInformation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICapabilityInformation::OAICapabilityInformation() {
    this->initializeModel();
}

OAICapabilityInformation::~OAICapabilityInformation() {}

void OAICapabilityInformation::initializeModel() {

    m_account_count_isSet = false;
    m_account_count_isValid = false;

    m_max_account_count_isSet = false;
    m_max_account_count_isValid = false;

    m_migration_state_isSet = false;
    m_migration_state_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_subscription_id_isSet = false;
    m_subscription_id_isValid = false;
}

void OAICapabilityInformation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICapabilityInformation::fromJsonObject(QJsonObject json) {

    m_account_count_isValid = ::OpenAPI::fromJsonValue(m_account_count, json[QString("accountCount")]);
    m_account_count_isSet = !json[QString("accountCount")].isNull() && m_account_count_isValid;

    m_max_account_count_isValid = ::OpenAPI::fromJsonValue(m_max_account_count, json[QString("maxAccountCount")]);
    m_max_account_count_isSet = !json[QString("maxAccountCount")].isNull() && m_max_account_count_isValid;

    m_migration_state_isValid = ::OpenAPI::fromJsonValue(m_migration_state, json[QString("migrationState")]);
    m_migration_state_isSet = !json[QString("migrationState")].isNull() && m_migration_state_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_subscription_id_isValid = ::OpenAPI::fromJsonValue(m_subscription_id, json[QString("subscriptionId")]);
    m_subscription_id_isSet = !json[QString("subscriptionId")].isNull() && m_subscription_id_isValid;
}

QString OAICapabilityInformation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICapabilityInformation::asJsonObject() const {
    QJsonObject obj;
    if (m_account_count_isSet) {
        obj.insert(QString("accountCount"), ::OpenAPI::toJsonValue(m_account_count));
    }
    if (m_max_account_count_isSet) {
        obj.insert(QString("maxAccountCount"), ::OpenAPI::toJsonValue(m_max_account_count));
    }
    if (m_migration_state_isSet) {
        obj.insert(QString("migrationState"), ::OpenAPI::toJsonValue(m_migration_state));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_subscription_id_isSet) {
        obj.insert(QString("subscriptionId"), ::OpenAPI::toJsonValue(m_subscription_id));
    }
    return obj;
}

qint32 OAICapabilityInformation::getAccountCount() const {
    return m_account_count;
}
void OAICapabilityInformation::setAccountCount(const qint32 &account_count) {
    m_account_count = account_count;
    m_account_count_isSet = true;
}

bool OAICapabilityInformation::is_account_count_Set() const{
    return m_account_count_isSet;
}

bool OAICapabilityInformation::is_account_count_Valid() const{
    return m_account_count_isValid;
}

qint32 OAICapabilityInformation::getMaxAccountCount() const {
    return m_max_account_count;
}
void OAICapabilityInformation::setMaxAccountCount(const qint32 &max_account_count) {
    m_max_account_count = max_account_count;
    m_max_account_count_isSet = true;
}

bool OAICapabilityInformation::is_max_account_count_Set() const{
    return m_max_account_count_isSet;
}

bool OAICapabilityInformation::is_max_account_count_Valid() const{
    return m_max_account_count_isValid;
}

bool OAICapabilityInformation::isMigrationState() const {
    return m_migration_state;
}
void OAICapabilityInformation::setMigrationState(const bool &migration_state) {
    m_migration_state = migration_state;
    m_migration_state_isSet = true;
}

bool OAICapabilityInformation::is_migration_state_Set() const{
    return m_migration_state_isSet;
}

bool OAICapabilityInformation::is_migration_state_Valid() const{
    return m_migration_state_isValid;
}

QString OAICapabilityInformation::getState() const {
    return m_state;
}
void OAICapabilityInformation::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAICapabilityInformation::is_state_Set() const{
    return m_state_isSet;
}

bool OAICapabilityInformation::is_state_Valid() const{
    return m_state_isValid;
}

QString OAICapabilityInformation::getSubscriptionId() const {
    return m_subscription_id;
}
void OAICapabilityInformation::setSubscriptionId(const QString &subscription_id) {
    m_subscription_id = subscription_id;
    m_subscription_id_isSet = true;
}

bool OAICapabilityInformation::is_subscription_id_Set() const{
    return m_subscription_id_isSet;
}

bool OAICapabilityInformation::is_subscription_id_Valid() const{
    return m_subscription_id_isValid;
}

bool OAICapabilityInformation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_account_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_migration_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICapabilityInformation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
