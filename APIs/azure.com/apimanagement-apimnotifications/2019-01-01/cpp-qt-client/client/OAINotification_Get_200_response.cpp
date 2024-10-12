/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINotification_Get_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotification_Get_200_response::OAINotification_Get_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotification_Get_200_response::OAINotification_Get_200_response() {
    this->initializeModel();
}

OAINotification_Get_200_response::~OAINotification_Get_200_response() {}

void OAINotification_Get_200_response::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAINotification_Get_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotification_Get_200_response::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAINotification_Get_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotification_Get_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
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

OAINotification_ListByService_200_response_value_inner_properties OAINotification_Get_200_response::getProperties() const {
    return m_properties;
}
void OAINotification_Get_200_response::setProperties(const OAINotification_ListByService_200_response_value_inner_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAINotification_Get_200_response::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAINotification_Get_200_response::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAINotification_Get_200_response::getId() const {
    return m_id;
}
void OAINotification_Get_200_response::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAINotification_Get_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAINotification_Get_200_response::is_id_Valid() const{
    return m_id_isValid;
}

QString OAINotification_Get_200_response::getName() const {
    return m_name;
}
void OAINotification_Get_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAINotification_Get_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAINotification_Get_200_response::is_name_Valid() const{
    return m_name_isValid;
}

QString OAINotification_Get_200_response::getType() const {
    return m_type;
}
void OAINotification_Get_200_response::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAINotification_Get_200_response::is_type_Set() const{
    return m_type_isSet;
}

bool OAINotification_Get_200_response::is_type_Valid() const{
    return m_type_isValid;
}

bool OAINotification_Get_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

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

bool OAINotification_Get_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
