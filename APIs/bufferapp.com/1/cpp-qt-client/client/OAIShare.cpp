/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIShare.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShare::OAIShare(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShare::OAIShare() {
    this->initializeModel();
}

OAIShare::~OAIShare() {}

void OAIShare::initializeModel() {

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAIShare::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShare::fromJsonObject(QJsonObject json) {

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAIShare::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShare::asJsonObject() const {
    QJsonObject obj;
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

bool OAIShare::isSuccess() const {
    return m_success;
}
void OAIShare::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAIShare::is_success_Set() const{
    return m_success_isSet;
}

bool OAIShare::is_success_Valid() const{
    return m_success_isValid;
}

bool OAIShare::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShare::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
