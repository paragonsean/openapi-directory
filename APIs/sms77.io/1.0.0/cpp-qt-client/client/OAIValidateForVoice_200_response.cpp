/**
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIValidateForVoice_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIValidateForVoice_200_response::OAIValidateForVoice_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIValidateForVoice_200_response::OAIValidateForVoice_200_response() {
    this->initializeModel();
}

OAIValidateForVoice_200_response::~OAIValidateForVoice_200_response() {}

void OAIValidateForVoice_200_response::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAIValidateForVoice_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIValidateForVoice_200_response::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAIValidateForVoice_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIValidateForVoice_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

QString OAIValidateForVoice_200_response::getCode() const {
    return m_code;
}
void OAIValidateForVoice_200_response::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIValidateForVoice_200_response::is_code_Set() const{
    return m_code_isSet;
}

bool OAIValidateForVoice_200_response::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIValidateForVoice_200_response::getError() const {
    return m_error;
}
void OAIValidateForVoice_200_response::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIValidateForVoice_200_response::is_error_Set() const{
    return m_error_isSet;
}

bool OAIValidateForVoice_200_response::is_error_Valid() const{
    return m_error_isValid;
}

bool OAIValidateForVoice_200_response::isSuccess() const {
    return m_success;
}
void OAIValidateForVoice_200_response::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAIValidateForVoice_200_response::is_success_Set() const{
    return m_success_isSet;
}

bool OAIValidateForVoice_200_response::is_success_Valid() const{
    return m_success_isValid;
}

bool OAIValidateForVoice_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIValidateForVoice_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
