/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAvatar.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvatar::OAIAvatar(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvatar::OAIAvatar() {
    this->initializeModel();
}

OAIAvatar::~OAIAvatar() {}

void OAIAvatar::initializeModel() {

    m_source_isSet = false;
    m_source_isValid = false;
}

void OAIAvatar::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvatar::fromJsonObject(QJsonObject json) {

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;
}

QString OAIAvatar::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvatar::asJsonObject() const {
    QJsonObject obj;
    if (m_source.isSet()) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    return obj;
}

OAIAvatar_source OAIAvatar::getSource() const {
    return m_source;
}
void OAIAvatar::setSource(const OAIAvatar_source &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIAvatar::is_source_Set() const{
    return m_source_isSet;
}

bool OAIAvatar::is_source_Valid() const{
    return m_source_isValid;
}

bool OAIAvatar::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_source.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvatar::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_source_isValid && true;
}

} // namespace OpenAPI
