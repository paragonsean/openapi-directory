/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetNetworkHealthAlerts_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkHealthAlerts_200_response_inner::OAIGetNetworkHealthAlerts_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkHealthAlerts_200_response_inner::OAIGetNetworkHealthAlerts_200_response_inner() {
    this->initializeModel();
}

OAIGetNetworkHealthAlerts_200_response_inner::~OAIGetNetworkHealthAlerts_200_response_inner() {}

void OAIGetNetworkHealthAlerts_200_response_inner::initializeModel() {

    m_category_isSet = false;
    m_category_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_scope_isSet = false;
    m_scope_isValid = false;

    m_severity_isSet = false;
    m_severity_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIGetNetworkHealthAlerts_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkHealthAlerts_200_response_inner::fromJsonObject(QJsonObject json) {

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_scope_isValid = ::OpenAPI::fromJsonValue(m_scope, json[QString("scope")]);
    m_scope_isSet = !json[QString("scope")].isNull() && m_scope_isValid;

    m_severity_isValid = ::OpenAPI::fromJsonValue(m_severity, json[QString("severity")]);
    m_severity_isSet = !json[QString("severity")].isNull() && m_severity_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIGetNetworkHealthAlerts_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkHealthAlerts_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_category_isSet) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_scope.isSet()) {
        obj.insert(QString("scope"), ::OpenAPI::toJsonValue(m_scope));
    }
    if (m_severity_isSet) {
        obj.insert(QString("severity"), ::OpenAPI::toJsonValue(m_severity));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIGetNetworkHealthAlerts_200_response_inner::getCategory() const {
    return m_category;
}
void OAIGetNetworkHealthAlerts_200_response_inner::setCategory(const QString &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_category_Set() const{
    return m_category_isSet;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_category_Valid() const{
    return m_category_isValid;
}

QString OAIGetNetworkHealthAlerts_200_response_inner::getId() const {
    return m_id;
}
void OAIGetNetworkHealthAlerts_200_response_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_id_Valid() const{
    return m_id_isValid;
}

OAIGetNetworkHealthAlerts_200_response_inner_scope OAIGetNetworkHealthAlerts_200_response_inner::getScope() const {
    return m_scope;
}
void OAIGetNetworkHealthAlerts_200_response_inner::setScope(const OAIGetNetworkHealthAlerts_200_response_inner_scope &scope) {
    m_scope = scope;
    m_scope_isSet = true;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_scope_Set() const{
    return m_scope_isSet;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_scope_Valid() const{
    return m_scope_isValid;
}

QString OAIGetNetworkHealthAlerts_200_response_inner::getSeverity() const {
    return m_severity;
}
void OAIGetNetworkHealthAlerts_200_response_inner::setSeverity(const QString &severity) {
    m_severity = severity;
    m_severity_isSet = true;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_severity_Set() const{
    return m_severity_isSet;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_severity_Valid() const{
    return m_severity_isValid;
}

QString OAIGetNetworkHealthAlerts_200_response_inner::getType() const {
    return m_type;
}
void OAIGetNetworkHealthAlerts_200_response_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIGetNetworkHealthAlerts_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scope.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_severity_isSet) {
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

bool OAIGetNetworkHealthAlerts_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
