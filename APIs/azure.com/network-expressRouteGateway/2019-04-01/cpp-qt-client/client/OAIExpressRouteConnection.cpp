/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExpressRouteConnection.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExpressRouteConnection::OAIExpressRouteConnection(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExpressRouteConnection::OAIExpressRouteConnection() {
    this->initializeModel();
}

OAIExpressRouteConnection::~OAIExpressRouteConnection() {}

void OAIExpressRouteConnection::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIExpressRouteConnection::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExpressRouteConnection::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIExpressRouteConnection::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExpressRouteConnection::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIExpressRouteConnection::getName() const {
    return m_name;
}
void OAIExpressRouteConnection::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIExpressRouteConnection::is_name_Set() const{
    return m_name_isSet;
}

bool OAIExpressRouteConnection::is_name_Valid() const{
    return m_name_isValid;
}

OAIExpressRouteConnectionProperties OAIExpressRouteConnection::getProperties() const {
    return m_properties;
}
void OAIExpressRouteConnection::setProperties(const OAIExpressRouteConnectionProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIExpressRouteConnection::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIExpressRouteConnection::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIExpressRouteConnection::getId() const {
    return m_id;
}
void OAIExpressRouteConnection::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIExpressRouteConnection::is_id_Set() const{
    return m_id_isSet;
}

bool OAIExpressRouteConnection::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIExpressRouteConnection::isSet() const {
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

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExpressRouteConnection::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
