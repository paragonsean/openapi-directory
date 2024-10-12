/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVnetValidationFailureDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVnetValidationFailureDetails::OAIVnetValidationFailureDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVnetValidationFailureDetails::OAIVnetValidationFailureDetails() {
    this->initializeModel();
}

OAIVnetValidationFailureDetails::~OAIVnetValidationFailureDetails() {}

void OAIVnetValidationFailureDetails::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_kind_isSet = false;
    m_kind_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIVnetValidationFailureDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVnetValidationFailureDetails::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_kind_isValid = ::OpenAPI::fromJsonValue(m_kind, json[QString("kind")]);
    m_kind_isSet = !json[QString("kind")].isNull() && m_kind_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIVnetValidationFailureDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVnetValidationFailureDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_kind_isSet) {
        obj.insert(QString("kind"), ::OpenAPI::toJsonValue(m_kind));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIObject OAIVnetValidationFailureDetails::getProperties() const {
    return m_properties;
}
void OAIVnetValidationFailureDetails::setProperties(const OAIObject &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIVnetValidationFailureDetails::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIVnetValidationFailureDetails::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIVnetValidationFailureDetails::getId() const {
    return m_id;
}
void OAIVnetValidationFailureDetails::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVnetValidationFailureDetails::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVnetValidationFailureDetails::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIVnetValidationFailureDetails::getKind() const {
    return m_kind;
}
void OAIVnetValidationFailureDetails::setKind(const QString &kind) {
    m_kind = kind;
    m_kind_isSet = true;
}

bool OAIVnetValidationFailureDetails::is_kind_Set() const{
    return m_kind_isSet;
}

bool OAIVnetValidationFailureDetails::is_kind_Valid() const{
    return m_kind_isValid;
}

QString OAIVnetValidationFailureDetails::getName() const {
    return m_name;
}
void OAIVnetValidationFailureDetails::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVnetValidationFailureDetails::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVnetValidationFailureDetails::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIVnetValidationFailureDetails::getType() const {
    return m_type;
}
void OAIVnetValidationFailureDetails::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIVnetValidationFailureDetails::is_type_Set() const{
    return m_type_isSet;
}

bool OAIVnetValidationFailureDetails::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIVnetValidationFailureDetails::isSet() const {
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

        if (m_kind_isSet) {
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

bool OAIVnetValidationFailureDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
