/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBackendPool.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBackendPool::OAIBackendPool(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBackendPool::OAIBackendPool() {
    this->initializeModel();
}

OAIBackendPool::~OAIBackendPool() {}

void OAIBackendPool::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIBackendPool::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBackendPool::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIBackendPool::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBackendPool::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIBackendPool::getName() const {
    return m_name;
}
void OAIBackendPool::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBackendPool::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBackendPool::is_name_Valid() const{
    return m_name_isValid;
}

OAIBackendPoolProperties OAIBackendPool::getProperties() const {
    return m_properties;
}
void OAIBackendPool::setProperties(const OAIBackendPoolProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIBackendPool::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIBackendPool::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIBackendPool::getType() const {
    return m_type;
}
void OAIBackendPool::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIBackendPool::is_type_Set() const{
    return m_type_isSet;
}

bool OAIBackendPool::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIBackendPool::getId() const {
    return m_id;
}
void OAIBackendPool::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBackendPool::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBackendPool::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIBackendPool::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBackendPool::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
