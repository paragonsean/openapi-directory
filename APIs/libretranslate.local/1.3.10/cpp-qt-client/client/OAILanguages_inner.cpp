/**
 * LibreTranslate
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.3.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILanguages_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILanguages_inner::OAILanguages_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILanguages_inner::OAILanguages_inner() {
    this->initializeModel();
}

OAILanguages_inner::~OAILanguages_inner() {}

void OAILanguages_inner::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_targets_isSet = false;
    m_targets_isValid = false;
}

void OAILanguages_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILanguages_inner::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_targets_isValid = ::OpenAPI::fromJsonValue(m_targets, json[QString("targets")]);
    m_targets_isSet = !json[QString("targets")].isNull() && m_targets_isValid;
}

QString OAILanguages_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILanguages_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_targets.size() > 0) {
        obj.insert(QString("targets"), ::OpenAPI::toJsonValue(m_targets));
    }
    return obj;
}

QString OAILanguages_inner::getCode() const {
    return m_code;
}
void OAILanguages_inner::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAILanguages_inner::is_code_Set() const{
    return m_code_isSet;
}

bool OAILanguages_inner::is_code_Valid() const{
    return m_code_isValid;
}

QString OAILanguages_inner::getName() const {
    return m_name;
}
void OAILanguages_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAILanguages_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAILanguages_inner::is_name_Valid() const{
    return m_name_isValid;
}

QList<QString> OAILanguages_inner::getTargets() const {
    return m_targets;
}
void OAILanguages_inner::setTargets(const QList<QString> &targets) {
    m_targets = targets;
    m_targets_isSet = true;
}

bool OAILanguages_inner::is_targets_Set() const{
    return m_targets_isSet;
}

bool OAILanguages_inner::is_targets_Valid() const{
    return m_targets_isValid;
}

bool OAILanguages_inner::isSet() const {
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

        if (m_targets.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILanguages_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
