/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserIdentityProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserIdentityProperties::OAIUserIdentityProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserIdentityProperties::OAIUserIdentityProperties() {
    this->initializeModel();
}

OAIUserIdentityProperties::~OAIUserIdentityProperties() {}

void OAIUserIdentityProperties::initializeModel() {

    m_client_id_isSet = false;
    m_client_id_isValid = false;

    m_principal_id_isSet = false;
    m_principal_id_isValid = false;
}

void OAIUserIdentityProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserIdentityProperties::fromJsonObject(QJsonObject json) {

    m_client_id_isValid = ::OpenAPI::fromJsonValue(m_client_id, json[QString("clientId")]);
    m_client_id_isSet = !json[QString("clientId")].isNull() && m_client_id_isValid;

    m_principal_id_isValid = ::OpenAPI::fromJsonValue(m_principal_id, json[QString("principalId")]);
    m_principal_id_isSet = !json[QString("principalId")].isNull() && m_principal_id_isValid;
}

QString OAIUserIdentityProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserIdentityProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_client_id_isSet) {
        obj.insert(QString("clientId"), ::OpenAPI::toJsonValue(m_client_id));
    }
    if (m_principal_id_isSet) {
        obj.insert(QString("principalId"), ::OpenAPI::toJsonValue(m_principal_id));
    }
    return obj;
}

QString OAIUserIdentityProperties::getClientId() const {
    return m_client_id;
}
void OAIUserIdentityProperties::setClientId(const QString &client_id) {
    m_client_id = client_id;
    m_client_id_isSet = true;
}

bool OAIUserIdentityProperties::is_client_id_Set() const{
    return m_client_id_isSet;
}

bool OAIUserIdentityProperties::is_client_id_Valid() const{
    return m_client_id_isValid;
}

QString OAIUserIdentityProperties::getPrincipalId() const {
    return m_principal_id;
}
void OAIUserIdentityProperties::setPrincipalId(const QString &principal_id) {
    m_principal_id = principal_id;
    m_principal_id_isSet = true;
}

bool OAIUserIdentityProperties::is_principal_id_Set() const{
    return m_principal_id_isSet;
}

bool OAIUserIdentityProperties::is_principal_id_Valid() const{
    return m_principal_id_isValid;
}

bool OAIUserIdentityProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_principal_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserIdentityProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
