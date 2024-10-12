/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01-privatepreview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProxyResource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProxyResource::OAIProxyResource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProxyResource::OAIProxyResource() {
    this->initializeModel();
}

OAIProxyResource::~OAIProxyResource() {}

void OAIProxyResource::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIProxyResource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProxyResource::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIProxyResource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProxyResource::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIProxyResource::getId() const {
    return m_id;
}
void OAIProxyResource::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProxyResource::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProxyResource::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIProxyResource::getName() const {
    return m_name;
}
void OAIProxyResource::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProxyResource::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProxyResource::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIProxyResource::getType() const {
    return m_type;
}
void OAIProxyResource::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIProxyResource::is_type_Set() const{
    return m_type_isSet;
}

bool OAIProxyResource::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIProxyResource::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIProxyResource::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
