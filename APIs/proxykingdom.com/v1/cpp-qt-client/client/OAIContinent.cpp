/**
 * ProxyKingdom-Api
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIContinent.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContinent::OAIContinent(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContinent::OAIContinent() {
    this->initializeModel();
}

OAIContinent::~OAIContinent() {}

void OAIContinent::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIContinent::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContinent::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIContinent::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContinent::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIContinent::getCode() const {
    return m_code;
}
void OAIContinent::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIContinent::is_code_Set() const{
    return m_code_isSet;
}

bool OAIContinent::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIContinent::getName() const {
    return m_name;
}
void OAIContinent::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIContinent::is_name_Set() const{
    return m_name_isSet;
}

bool OAIContinent::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIContinent::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIContinent::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
