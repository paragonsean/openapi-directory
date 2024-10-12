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

#include "OAISuggest_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISuggest_response::OAISuggest_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISuggest_response::OAISuggest_response() {
    this->initializeModel();
}

OAISuggest_response::~OAISuggest_response() {}

void OAISuggest_response::initializeModel() {

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAISuggest_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISuggest_response::fromJsonObject(QJsonObject json) {

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAISuggest_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISuggest_response::asJsonObject() const {
    QJsonObject obj;
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

bool OAISuggest_response::isSuccess() const {
    return m_success;
}
void OAISuggest_response::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAISuggest_response::is_success_Set() const{
    return m_success_isSet;
}

bool OAISuggest_response::is_success_Valid() const{
    return m_success_isValid;
}

bool OAISuggest_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISuggest_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
