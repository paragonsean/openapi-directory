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

#include "OAISchedules_update.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISchedules_update::OAISchedules_update(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISchedules_update::OAISchedules_update() {
    this->initializeModel();
}

OAISchedules_update::~OAISchedules_update() {}

void OAISchedules_update::initializeModel() {

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAISchedules_update::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISchedules_update::fromJsonObject(QJsonObject json) {

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAISchedules_update::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISchedules_update::asJsonObject() const {
    QJsonObject obj;
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

bool OAISchedules_update::isSuccess() const {
    return m_success;
}
void OAISchedules_update::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAISchedules_update::is_success_Set() const{
    return m_success_isSet;
}

bool OAISchedules_update::is_success_Valid() const{
    return m_success_isValid;
}

bool OAISchedules_update::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISchedules_update::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
