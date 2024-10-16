/**
 * LH Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIName.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIName::OAIName(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIName::OAIName() {
    this->initializeModel();
}

OAIName::~OAIName() {}

void OAIName::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;

    m_language_code_isSet = false;
    m_language_code_isValid = false;
}

void OAIName::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIName::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("$")]);
    m_value_isSet = !json[QString("$")].isNull() && m_value_isValid;

    m_language_code_isValid = ::OpenAPI::fromJsonValue(m_language_code, json[QString("@LanguageCode")]);
    m_language_code_isSet = !json[QString("@LanguageCode")].isNull() && m_language_code_isValid;
}

QString OAIName::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIName::asJsonObject() const {
    QJsonObject obj;
    if (m_value_isSet) {
        obj.insert(QString("$"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_language_code_isSet) {
        obj.insert(QString("@LanguageCode"), ::OpenAPI::toJsonValue(m_language_code));
    }
    return obj;
}

QString OAIName::getValue() const {
    return m_value;
}
void OAIName::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIName::is_value_Set() const{
    return m_value_isSet;
}

bool OAIName::is_value_Valid() const{
    return m_value_isValid;
}

QString OAIName::getLanguageCode() const {
    return m_language_code;
}
void OAIName::setLanguageCode(const QString &language_code) {
    m_language_code = language_code;
    m_language_code_isSet = true;
}

bool OAIName::is_language_code_Set() const{
    return m_language_code_isSet;
}

bool OAIName::is_language_code_Valid() const{
    return m_language_code_isValid;
}

bool OAIName::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIName::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
