/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2015-10-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEncryptionIdentity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEncryptionIdentity::OAIEncryptionIdentity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEncryptionIdentity::OAIEncryptionIdentity() {
    this->initializeModel();
}

OAIEncryptionIdentity::~OAIEncryptionIdentity() {}

void OAIEncryptionIdentity::initializeModel() {

    m_principal_id_isSet = false;
    m_principal_id_isValid = false;

    m_tenant_id_isSet = false;
    m_tenant_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIEncryptionIdentity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEncryptionIdentity::fromJsonObject(QJsonObject json) {

    m_principal_id_isValid = ::OpenAPI::fromJsonValue(m_principal_id, json[QString("principalId")]);
    m_principal_id_isSet = !json[QString("principalId")].isNull() && m_principal_id_isValid;

    m_tenant_id_isValid = ::OpenAPI::fromJsonValue(m_tenant_id, json[QString("tenantId")]);
    m_tenant_id_isSet = !json[QString("tenantId")].isNull() && m_tenant_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIEncryptionIdentity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEncryptionIdentity::asJsonObject() const {
    QJsonObject obj;
    if (m_principal_id_isSet) {
        obj.insert(QString("principalId"), ::OpenAPI::toJsonValue(m_principal_id));
    }
    if (m_tenant_id_isSet) {
        obj.insert(QString("tenantId"), ::OpenAPI::toJsonValue(m_tenant_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIEncryptionIdentity::getPrincipalId() const {
    return m_principal_id;
}
void OAIEncryptionIdentity::setPrincipalId(const QString &principal_id) {
    m_principal_id = principal_id;
    m_principal_id_isSet = true;
}

bool OAIEncryptionIdentity::is_principal_id_Set() const{
    return m_principal_id_isSet;
}

bool OAIEncryptionIdentity::is_principal_id_Valid() const{
    return m_principal_id_isValid;
}

QString OAIEncryptionIdentity::getTenantId() const {
    return m_tenant_id;
}
void OAIEncryptionIdentity::setTenantId(const QString &tenant_id) {
    m_tenant_id = tenant_id;
    m_tenant_id_isSet = true;
}

bool OAIEncryptionIdentity::is_tenant_id_Set() const{
    return m_tenant_id_isSet;
}

bool OAIEncryptionIdentity::is_tenant_id_Valid() const{
    return m_tenant_id_isValid;
}

QString OAIEncryptionIdentity::getType() const {
    return m_type;
}
void OAIEncryptionIdentity::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIEncryptionIdentity::is_type_Set() const{
    return m_type_isSet;
}

bool OAIEncryptionIdentity::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIEncryptionIdentity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_principal_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tenant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEncryptionIdentity::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
