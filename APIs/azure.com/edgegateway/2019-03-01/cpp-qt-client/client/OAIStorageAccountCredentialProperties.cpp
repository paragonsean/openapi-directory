/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStorageAccountCredentialProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStorageAccountCredentialProperties::OAIStorageAccountCredentialProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStorageAccountCredentialProperties::OAIStorageAccountCredentialProperties() {
    this->initializeModel();
}

OAIStorageAccountCredentialProperties::~OAIStorageAccountCredentialProperties() {}

void OAIStorageAccountCredentialProperties::initializeModel() {

    m_account_key_isSet = false;
    m_account_key_isValid = false;

    m_account_type_isSet = false;
    m_account_type_isValid = false;

    m_alias_isSet = false;
    m_alias_isValid = false;

    m_blob_domain_name_isSet = false;
    m_blob_domain_name_isValid = false;

    m_connection_string_isSet = false;
    m_connection_string_isValid = false;

    m_ssl_status_isSet = false;
    m_ssl_status_isValid = false;

    m_user_name_isSet = false;
    m_user_name_isValid = false;
}

void OAIStorageAccountCredentialProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStorageAccountCredentialProperties::fromJsonObject(QJsonObject json) {

    m_account_key_isValid = ::OpenAPI::fromJsonValue(m_account_key, json[QString("accountKey")]);
    m_account_key_isSet = !json[QString("accountKey")].isNull() && m_account_key_isValid;

    m_account_type_isValid = ::OpenAPI::fromJsonValue(m_account_type, json[QString("accountType")]);
    m_account_type_isSet = !json[QString("accountType")].isNull() && m_account_type_isValid;

    m_alias_isValid = ::OpenAPI::fromJsonValue(m_alias, json[QString("alias")]);
    m_alias_isSet = !json[QString("alias")].isNull() && m_alias_isValid;

    m_blob_domain_name_isValid = ::OpenAPI::fromJsonValue(m_blob_domain_name, json[QString("blobDomainName")]);
    m_blob_domain_name_isSet = !json[QString("blobDomainName")].isNull() && m_blob_domain_name_isValid;

    m_connection_string_isValid = ::OpenAPI::fromJsonValue(m_connection_string, json[QString("connectionString")]);
    m_connection_string_isSet = !json[QString("connectionString")].isNull() && m_connection_string_isValid;

    m_ssl_status_isValid = ::OpenAPI::fromJsonValue(m_ssl_status, json[QString("sslStatus")]);
    m_ssl_status_isSet = !json[QString("sslStatus")].isNull() && m_ssl_status_isValid;

    m_user_name_isValid = ::OpenAPI::fromJsonValue(m_user_name, json[QString("userName")]);
    m_user_name_isSet = !json[QString("userName")].isNull() && m_user_name_isValid;
}

QString OAIStorageAccountCredentialProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStorageAccountCredentialProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_account_key.isSet()) {
        obj.insert(QString("accountKey"), ::OpenAPI::toJsonValue(m_account_key));
    }
    if (m_account_type_isSet) {
        obj.insert(QString("accountType"), ::OpenAPI::toJsonValue(m_account_type));
    }
    if (m_alias_isSet) {
        obj.insert(QString("alias"), ::OpenAPI::toJsonValue(m_alias));
    }
    if (m_blob_domain_name_isSet) {
        obj.insert(QString("blobDomainName"), ::OpenAPI::toJsonValue(m_blob_domain_name));
    }
    if (m_connection_string_isSet) {
        obj.insert(QString("connectionString"), ::OpenAPI::toJsonValue(m_connection_string));
    }
    if (m_ssl_status_isSet) {
        obj.insert(QString("sslStatus"), ::OpenAPI::toJsonValue(m_ssl_status));
    }
    if (m_user_name_isSet) {
        obj.insert(QString("userName"), ::OpenAPI::toJsonValue(m_user_name));
    }
    return obj;
}

OAIAsymmetricEncryptedSecret OAIStorageAccountCredentialProperties::getAccountKey() const {
    return m_account_key;
}
void OAIStorageAccountCredentialProperties::setAccountKey(const OAIAsymmetricEncryptedSecret &account_key) {
    m_account_key = account_key;
    m_account_key_isSet = true;
}

bool OAIStorageAccountCredentialProperties::is_account_key_Set() const{
    return m_account_key_isSet;
}

bool OAIStorageAccountCredentialProperties::is_account_key_Valid() const{
    return m_account_key_isValid;
}

QString OAIStorageAccountCredentialProperties::getAccountType() const {
    return m_account_type;
}
void OAIStorageAccountCredentialProperties::setAccountType(const QString &account_type) {
    m_account_type = account_type;
    m_account_type_isSet = true;
}

bool OAIStorageAccountCredentialProperties::is_account_type_Set() const{
    return m_account_type_isSet;
}

bool OAIStorageAccountCredentialProperties::is_account_type_Valid() const{
    return m_account_type_isValid;
}

QString OAIStorageAccountCredentialProperties::getAlias() const {
    return m_alias;
}
void OAIStorageAccountCredentialProperties::setAlias(const QString &alias) {
    m_alias = alias;
    m_alias_isSet = true;
}

bool OAIStorageAccountCredentialProperties::is_alias_Set() const{
    return m_alias_isSet;
}

bool OAIStorageAccountCredentialProperties::is_alias_Valid() const{
    return m_alias_isValid;
}

QString OAIStorageAccountCredentialProperties::getBlobDomainName() const {
    return m_blob_domain_name;
}
void OAIStorageAccountCredentialProperties::setBlobDomainName(const QString &blob_domain_name) {
    m_blob_domain_name = blob_domain_name;
    m_blob_domain_name_isSet = true;
}

bool OAIStorageAccountCredentialProperties::is_blob_domain_name_Set() const{
    return m_blob_domain_name_isSet;
}

bool OAIStorageAccountCredentialProperties::is_blob_domain_name_Valid() const{
    return m_blob_domain_name_isValid;
}

QString OAIStorageAccountCredentialProperties::getConnectionString() const {
    return m_connection_string;
}
void OAIStorageAccountCredentialProperties::setConnectionString(const QString &connection_string) {
    m_connection_string = connection_string;
    m_connection_string_isSet = true;
}

bool OAIStorageAccountCredentialProperties::is_connection_string_Set() const{
    return m_connection_string_isSet;
}

bool OAIStorageAccountCredentialProperties::is_connection_string_Valid() const{
    return m_connection_string_isValid;
}

QString OAIStorageAccountCredentialProperties::getSslStatus() const {
    return m_ssl_status;
}
void OAIStorageAccountCredentialProperties::setSslStatus(const QString &ssl_status) {
    m_ssl_status = ssl_status;
    m_ssl_status_isSet = true;
}

bool OAIStorageAccountCredentialProperties::is_ssl_status_Set() const{
    return m_ssl_status_isSet;
}

bool OAIStorageAccountCredentialProperties::is_ssl_status_Valid() const{
    return m_ssl_status_isValid;
}

QString OAIStorageAccountCredentialProperties::getUserName() const {
    return m_user_name;
}
void OAIStorageAccountCredentialProperties::setUserName(const QString &user_name) {
    m_user_name = user_name;
    m_user_name_isSet = true;
}

bool OAIStorageAccountCredentialProperties::is_user_name_Set() const{
    return m_user_name_isSet;
}

bool OAIStorageAccountCredentialProperties::is_user_name_Valid() const{
    return m_user_name_isValid;
}

bool OAIStorageAccountCredentialProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_key.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_account_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_alias_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blob_domain_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_connection_string_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssl_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStorageAccountCredentialProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_account_type_isValid && m_alias_isValid && m_ssl_status_isValid && true;
}

} // namespace OpenAPI
