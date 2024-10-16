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

#include "OAINumberProperty_Diagnostics.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINumberProperty_Diagnostics::OAINumberProperty_Diagnostics(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINumberProperty_Diagnostics::OAINumberProperty_Diagnostics() {
    this->initializeModel();
}

OAINumberProperty_Diagnostics::~OAINumberProperty_Diagnostics() {}

void OAINumberProperty_Diagnostics::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAINumberProperty_Diagnostics::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINumberProperty_Diagnostics::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAINumberProperty_Diagnostics::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINumberProperty_Diagnostics::asJsonObject() const {
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

double OAINumberProperty_Diagnostics::getValue() const {
    return m_value;
}
void OAINumberProperty_Diagnostics::setValue(const double &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAINumberProperty_Diagnostics::is_value_Set() const{
    return m_value_isSet;
}

bool OAINumberProperty_Diagnostics::is_value_Valid() const{
    return m_value_isValid;
}

QString OAINumberProperty_Diagnostics::getName() const {
    return m_name;
}
void OAINumberProperty_Diagnostics::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAINumberProperty_Diagnostics::is_name_Set() const{
    return m_name_isSet;
}

bool OAINumberProperty_Diagnostics::is_name_Valid() const{
    return m_name_isValid;
}

QString OAINumberProperty_Diagnostics::getType() const {
    return m_type;
}
void OAINumberProperty_Diagnostics::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAINumberProperty_Diagnostics::is_type_Set() const{
    return m_type_isSet;
}

bool OAINumberProperty_Diagnostics::is_type_Valid() const{
    return m_type_isValid;
}

bool OAINumberProperty_Diagnostics::isSet() const {
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

bool OAINumberProperty_Diagnostics::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && m_name_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
