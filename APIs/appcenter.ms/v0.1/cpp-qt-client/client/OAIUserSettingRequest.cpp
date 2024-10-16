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

#include "OAIUserSettingRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserSettingRequest::OAIUserSettingRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserSettingRequest::OAIUserSettingRequest() {
    this->initializeModel();
}

OAIUserSettingRequest::~OAIUserSettingRequest() {}

void OAIUserSettingRequest::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIUserSettingRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserSettingRequest::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIUserSettingRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserSettingRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIUserSettingRequest::getValue() const {
    return m_value;
}
void OAIUserSettingRequest::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIUserSettingRequest::is_value_Set() const{
    return m_value_isSet;
}

bool OAIUserSettingRequest::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIUserSettingRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserSettingRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && true;
}

} // namespace OpenAPI
