/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILogFlowNumberProperty.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILogFlowNumberProperty::OAILogFlowNumberProperty(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILogFlowNumberProperty::OAILogFlowNumberProperty() {
    this->initializeModel();
}

OAILogFlowNumberProperty::~OAILogFlowNumberProperty() {}

void OAILogFlowNumberProperty::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAILogFlowNumberProperty::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILogFlowNumberProperty::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAILogFlowNumberProperty::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILogFlowNumberProperty::asJsonObject() const {
    QJsonObject obj;
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

double OAILogFlowNumberProperty::getValue() const {
    return m_value;
}
void OAILogFlowNumberProperty::setValue(const double &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAILogFlowNumberProperty::is_value_Set() const{
    return m_value_isSet;
}

bool OAILogFlowNumberProperty::is_value_Valid() const{
    return m_value_isValid;
}

QString OAILogFlowNumberProperty::getName() const {
    return m_name;
}
void OAILogFlowNumberProperty::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAILogFlowNumberProperty::is_name_Set() const{
    return m_name_isSet;
}

bool OAILogFlowNumberProperty::is_name_Valid() const{
    return m_name_isValid;
}

QString OAILogFlowNumberProperty::getType() const {
    return m_type;
}
void OAILogFlowNumberProperty::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAILogFlowNumberProperty::is_type_Set() const{
    return m_type_isSet;
}

bool OAILogFlowNumberProperty::is_type_Valid() const{
    return m_type_isValid;
}

bool OAILogFlowNumberProperty::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value_isSet) {
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

bool OAILogFlowNumberProperty::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && m_name_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
